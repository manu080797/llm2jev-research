"""Run the compact Jev baseline with the existing Transformers binary scorer."""

from __future__ import annotations

import argparse
import json
import math
import platform
import sys
import time
from pathlib import Path
from typing import Any

try:
    import resource
except ImportError:  # pragma: no cover - Windows fallback
    resource = None  # type: ignore[assignment]

from llm2jev import (
    ChoiceAnswer,
    LLM2Jev,
    NoulAnswer,
    ScoreAnswer,
    TransformersBackend,
)
from llm2jev.sglang_server import _parse_request


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WORKLOAD = ROOT / "benchmarks" / "compact_jev_v1.json"


def _peak_rss_mb() -> float | None:
    if resource is None:
        return None
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # Linux reports KiB; macOS reports bytes.
    divisor = 1024.0 * 1024.0 if sys.platform == "darwin" else 1024.0
    return float(usage) / divisor


def _sync_cuda(backend: TransformersBackend) -> None:
    if str(backend.device).startswith("cuda"):
        backend._torch.cuda.synchronize()  # type: ignore[attr-defined]


def _peak_vram_mb(backend: TransformersBackend) -> float | None:
    if not str(backend.device).startswith("cuda"):
        return None
    return float(backend._torch.cuda.max_memory_allocated()) / (1024.0 * 1024.0)  # type: ignore[attr-defined]


def _hardware_name(backend: TransformersBackend) -> str:
    if str(backend.device).startswith("cuda"):
        return str(backend._torch.cuda.get_device_name())  # type: ignore[attr-defined]
    return platform.processor() or platform.machine() or "unknown"


def _score_prediction(response: Any, reference: dict[str, Any]) -> dict[str, Any]:
    question_id = reference["question_id"]
    answer = response.answers[question_id]
    target = reference["target"]

    if isinstance(answer, ChoiceAnswer):
        return {
            "prediction": answer.choice,
            "correct": answer.choice == target,
        }

    if isinstance(answer, NoulAnswer):
        predicted = answer.noul >= 0.5
        return {
            "prediction": predicted,
            "correct": predicted is target,
            "noul_probability": answer.noul,
        }

    if isinstance(answer, ScoreAnswer):
        nearest_level = int(math.floor(answer.score + 0.5))
        nearest_level = min(max(nearest_level, min(answer.legend)), max(answer.legend))
        return {
            "prediction": answer.score,
            "rounded_level": nearest_level,
            "target_level": target,
            "absolute_error": abs(answer.score - target),
            "correct": nearest_level == target,
        }

    raise TypeError(f"unsupported answer type: {type(answer).__name__}")


def _load_workload(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("cases"), list):
        raise ValueError("workload must be a JSON object containing a cases array")
    return payload


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the compact Jev workload through the Transformers binary baseline."
    )
    parser.add_argument(
        "--model-path",
        required=True,
        help="Local Hugging Face model directory. The backend does not download weights.",
    )
    parser.add_argument(
        "--workload",
        type=Path,
        default=DEFAULT_WORKLOAD,
        help=f"Workload JSON (default: {DEFAULT_WORKLOAD})",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Destination JSON result file.",
    )
    parser.add_argument(
        "--experiment-id",
        default=None,
        help="Experiment identifier. Defaults to a timestamp-derived value.",
    )
    parser.add_argument(
        "--device",
        default=None,
        help="Torch device, e.g. cpu, cuda, cuda:0. Default: CUDA if available, otherwise CPU.",
    )
    parser.add_argument(
        "--dtype",
        default="auto",
        help="Torch dtype name accepted by TransformersBackend, e.g. bfloat16 or float16.",
    )
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--yes-label", default="yes")
    parser.add_argument("--no-label", default="no")
    parser.add_argument(
        "--enable-thinking",
        action="store_true",
        help="Enable the model chat template's thinking mode where supported.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    workload = _load_workload(args.workload)

    load_started = time.perf_counter()
    backend = TransformersBackend(
        args.model_path,
        device=args.device,
        dtype=args.dtype,
        yes_label=args.yes_label,
        no_label=args.no_label,
        batch_size=args.batch_size,
        enable_thinking=args.enable_thinking,
    )
    _sync_cuda(backend)
    model_load_seconds = time.perf_counter() - load_started

    if str(backend.device).startswith("cuda"):
        backend._torch.cuda.reset_peak_memory_stats()  # type: ignore[attr-defined]

    engine = LLM2Jev(backend=backend)
    cases: list[dict[str, Any]] = []
    correct_count = 0
    score_absolute_errors: list[float] = []

    run_started = time.perf_counter()
    for case in workload["cases"]:
        request_payload = dict(case["request"])
        request_payload["model"] = args.model_path
        request = _parse_request(request_payload)

        _sync_cuda(backend)
        started = time.perf_counter()
        response = engine.evaluate(request)
        _sync_cuda(backend)
        latency_ms = (time.perf_counter() - started) * 1000.0

        scored = _score_prediction(response, case["reference"])
        if scored["correct"]:
            correct_count += 1
        if "absolute_error" in scored:
            score_absolute_errors.append(float(scored["absolute_error"]))

        cases.append(
            {
                "id": case["id"],
                "latency_ms": latency_ms,
                **scored,
                "response": response.to_dict(),
            }
        )

    _sync_cuda(backend)
    elapsed_seconds = time.perf_counter() - run_started
    case_count = len(cases)
    accuracy = correct_count / case_count if case_count else None

    try:
        import transformers

        runtime_revision: str | None = transformers.__version__
    except ImportError:  # pragma: no cover - backend import would already fail
        runtime_revision = None

    result = {
        "schema_version": "0.1",
        "experiment_id": args.experiment_id
        or f"transformers-binary-{int(time.time())}",
        "workload": {
            "name": workload["name"],
            "version": workload["version"],
        },
        "system": {
            "model": args.model_path,
            "model_revision": None,
            "training_exposure": "zero-training",
            "quantization": None,
            "runtime": "transformers",
            "runtime_revision": runtime_revision,
            "device_mode": "gpu" if str(backend.device).startswith("cuda") else "cpu",
            "hardware": _hardware_name(backend),
            "dtype": args.dtype,
            "batch_size": args.batch_size,
            "model_load_seconds": model_load_seconds,
        },
        "scorer": {
            "name": "binary-yes-no",
            "parameters": {
                "yes_label": args.yes_label,
                "no_label": args.no_label,
                "enable_thinking": args.enable_thinking,
            },
        },
        "aggregate": {
            "case_count": case_count,
            "correct_count": correct_count,
            "accuracy": accuracy,
            "elapsed_seconds": elapsed_seconds,
            "requests_per_second": case_count / elapsed_seconds if elapsed_seconds else None,
            "peak_rss_mb": _peak_rss_mb(),
            "peak_vram_mb": _peak_vram_mb(backend),
            "energy_joules": None,
            "score_mae": (
                sum(score_absolute_errors) / len(score_absolute_errors)
                if score_absolute_errors
                else None
            ),
        },
        "cases": cases,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        f"Wrote {args.output} | "
        f"{correct_count}/{case_count} rounded/exact hits | "
        f"{elapsed_seconds:.3f}s | "
        f"{result['aggregate']['requests_per_second']:.3f} req/s"
    )


if __name__ == "__main__":
    main()
