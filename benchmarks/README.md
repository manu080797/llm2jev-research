# Compact Jev research workload

`compact_jev_v1.json` is the first fixed workload for quick comparisons across Laya, Laya.cpp, the inherited binary LLM2Jev path, llama.cpp/GGUF, and later scoring strategies.

It is intentionally small and synthetic. Its job is to expose obvious semantic or runtime differences quickly without requiring dataset downloads or benchmark-specific dependencies.

Coverage:

- Noul: plain and explicit true/false criteria;
- Choice: 3, 4, 5, and 12 options;
- Score: five ordered levels;
- short and long state;
- unequal candidate-description lengths;
- simple retrieval and negation.

Each case contains exactly one Jev question. The request uses `"__MODEL__"` as a placeholder so a runner can substitute the actual served/model identifier without changing the workload.

The `reference` object records the expected semantic answer:

- Choice: target is the correct option key;
- Noul: target is a boolean;
- Score: target is the intended ordinal level index.

For early Score comparisons, use the predicted probability-weighted score and report both absolute error from the target level and a rounded-level hit if useful. Do not silently convert all Score outputs into classification accuracy.

## Result record

`result.schema.json` defines the minimal result envelope for early experiments. It deliberately distinguishes training exposure:

- `zero-training`
- `general-trained-specialist`
- `task-finetuned-specialist`
- `unknown`

This is required so Laya specialist controls are not confused with zero-training model/scorer comparisons.

The schema captures only the fields needed for the first Pareto comparisons: model/runtime/scorer identity, device mode, case-level prediction/latency, aggregate elapsed time, and optional accuracy/RAM/VRAM/energy.

Add profiler-specific artifacts separately rather than expanding the core result record with every hardware counter.

## Validation

The repository test `tests/test_compact_benchmark.py` validates every request through the same Jev wire parser used by the HTTP path and checks that references match the question type/options.

The workload is a research smoke benchmark, not a substitute for held-out public evaluation datasets.


## Running the Transformers binary baseline

`run_baseline.py` executes the compact workload through the existing zero-training binary yes/no scorer and writes a result compatible with `result.schema.json`.

The model must already exist locally because `TransformersBackend` uses `local_files_only=True`.

For the intended first LFM2.5-2.6B run:

```bash
uv sync --extra transformers

uv run python benchmarks/run_baseline.py \
  --model-path /path/to/LFM2.5-2.6B \
  --device cpu \
  --dtype bfloat16 \
  --output results/lfm2.5-2.6b-transformers-cpu.json
```

For CUDA:

```bash
uv run python benchmarks/run_baseline.py \
  --model-path /path/to/LFM2.5-2.6B \
  --device cuda \
  --dtype bfloat16 \
  --output results/lfm2.5-2.6b-transformers-gpu.json
```

The runner records model-load time separately from benchmark elapsed time. It reports per-case latency, exact/rounded hits, Score absolute error, process peak RSS, and CUDA peak allocated VRAM when applicable.

The binary scorer requires the configured `yes` and `no` labels to each tokenize to exactly one token. If a model's tokenizer does not satisfy that assumption, the backend fails explicitly. Use `--yes-label` / `--no-label` only when the alternative labels preserve the intended binary semantics.

The initial runner deliberately does not collect `perf`, Nsight, energy, or memory-controller counters. Phase 3 profiling wraps the same fixed workload with those collectors.
