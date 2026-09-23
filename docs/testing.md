# Testing environments and inherited-suite inventory

This document records how tests are classified for this research fork. GitHub issue #1 remains the authoritative tracker for task completion.

## Validation classes

### Sandbox-safe

A sandbox-safe test must be deterministic and must not require:

- downloading model weights;
- network access;
- a GPU;
- an external model/API service;
- a running SGLang, llama.cpp, or BitNet server/process;
- performance characteristics of specific hardware.

Optional Python packages may be used when already installed, provided the test either remains local/deterministic or skips cleanly when the optional package is unavailable.

### External real-model integration

An external integration test exercises an actual model/runtime or hardware-sensitive behavior, including:

- loading Transformers/SGLang model weights;
- llama.cpp/GGUF execution;
- BitNet/bitnet.cpp execution;
- real KV/Radix-cache behavior;
- numerical comparison across real runtimes;
- model-quality benchmarks;
- latency, throughput, RAM, or energy measurements.

These tests must never be reported as passed from the OpenAI sandbox unless an appropriate runtime and model were actually executed.

## Inherited suite inventory

Inventory performed against the research fork after the Graphify setup. The inherited suite contains **134 test methods in 15 executable test modules plus one helper module**.

| File | Tests | Classification | Notes |
| --- | ---: | --- | --- |
| `tests/test_assembler.py` | 8 | Sandbox-safe | Pure response assembly and normalization. |
| `tests/test_binary.py` | 10 | Sandbox-safe | Binary-question validation/compilation only. |
| `tests/test_converter.py` | 6 | Sandbox-safe | Uses deterministic fake backends; no model runtime. |
| `tests/test_multimodal.py` | 22 | Sandbox-safe | Uses local temporary images and mocked SGLang/runtime paths. Some tests skip cleanly when Pillow, Transformers vision dependencies, or torch are unavailable. No model weights are loaded. HTTP(S) image strings are forwarded under mocks rather than fetched. |
| `tests/test_normalization.py` | 4 | Sandbox-safe | Pure probability math. |
| `tests/test_prefix_plan.py` | 4 | Sandbox-safe | Pure prefix-planning algorithm. |
| `tests/test_prompt.py` | 9 | Sandbox-safe | Prompt rendering/serialization. |
| `tests/test_questions.py` | 11 | Sandbox-safe | Question-domain validation/serialization. |
| `tests/test_request.py` | 7 | Sandbox-safe | Request validation/serialization. |
| `tests/test_response.py` | 14 | Sandbox-safe | Response validation/serialization. |
| `tests/test_sglang_backend.py` | 13 | Sandbox-safe | SGLang and tokenizer modules/engine are mocked; no live server or model. |
| `tests/test_sglang_fakes.py` | 0 | Sandbox-safe helper | Test doubles used by SGLang tests; contains no discovered test methods. |
| `tests/test_sglang_scoring.py` | 3 | Sandbox-safe | Uses fake native SGLang modules and mocked tokenization/content conversion. |
| `tests/test_sglang_server.py` | 14 | Sandbox-safe | Server internals and async generation are mocked; no live HTTP server/model. |
| `tests/test_transformers_backend.py` | 3 | Sandbox-safe | Fake tokenizer and constructor validation; no model loading. |
| `tests/test_utils.py` | 6 | Sandbox-safe | Pure JSON/probability utilities. |

## Important finding

The inherited suite contains **no real-model integration tests**.

Existing backend tests validate orchestration and contracts through mocks/fakes. They do not establish that:

- a real Transformers model produces the expected yes/no readout;
- a real SGLang model produces equivalent scoring;
- SGLang Radix Cache is actually reused as expected on a live runtime;
- multimodal scoring works with a real VLM;
- probabilities agree across real backends;
- any reported latency/throughput measurements are reproducible.

Those are external integration/baseline tasks and must remain separate from sandbox-safe unit-test status.

## Current sandbox-safe command

The intended full inherited unit-test command is:

```bash
uv run python -m unittest discover -s tests -v
```

Additional repository checks are:

```bash
uv run python -m compileall -q src tests
uv build
```

The model-free CI workflow `.github/workflows/unit-tests.yml` runs this command on pushes to `main`, pull requests, and manual dispatches. It installs only the project's base dependencies; tests guarded by optional Pillow/Transformers/torch dependencies may therefore skip. This is intentional for the baseline sandbox-safe lane and skips must be reported rather than silently treated as executed coverage.

The next task in issue #1 is to run and document the sandbox-safe suite. Optional multimodal tests may be skipped when their optional local dependencies are not installed; skips must be reported rather than silently treated as executed coverage.

## External baseline coverage to add

Before making claims about real-model behavior, provide reproducible external smoke/integration commands for at least:

1. Transformers text-only binary scoring with an actual local model;
2. SGLang text-only binary scoring using the same or equivalent model;
3. comparison of candidate probabilities/tolerances across supported backends;
4. staged versus all-submission behavior on a live SGLang runtime, including cache/performance metadata;
5. multimodal scoring with a real supported VLM, if multimodal behavior remains in scope.

Future llama.cpp/GGUF and BitNet work must add their own external integration commands as those backends are introduced.
