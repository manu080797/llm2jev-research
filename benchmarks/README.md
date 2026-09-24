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
