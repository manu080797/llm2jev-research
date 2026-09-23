# Repository Guidelines

## Research Fork Context

This repository is the `llm2jev-research` fork of LLM2Jev. Its purpose is to research a model-agnostic, zero-training Jev-style semantic decision engine, with local CPU/GGUF inference as a first-class target.

Before making architectural or research changes, read:

- `docs/research-design.md` — source of truth for goals, architecture, accepted decisions, methodology, phases, and open questions.
- GitHub issue #1 — operational roadmap and task tracker.
- Existing relevant user-facing documentation under `docs/`.

Do not silently replace accepted design decisions. If evidence requires a change, add a new decision entry to `docs/research-design.md` and explicitly supersede the prior decision. Link meaningful implementation work to issue #1 or a more specific issue created from it.

## Project Structure & Module Organization

This repository uses a Python `src` layout. Keep stable public imports in `src/llm2jev/__init__.py`. Protocol and domain objects live in `src/llm2jev/models/`; inference, prompt rendering, scoring, normalization, backend integration, and response assembly live under `src/llm2jev/inference/`. Shared internal JSON and probability helpers belong in `src/llm2jev/utils/`, not the public package API. Tests mirror these responsibilities under `tests/` using `test_<module>.py` names.

User-facing and research documentation is version-controlled under `docs/`. Do not rely on ignored/local design documents for architectural authority.

## Architecture Constraints

Keep semantic scoring separate from model execution.

The target layering is:

```text
Jev-compatible API
        |
Typed question layer
        |
ScoringStrategy
  |        |           |
binary   label    continuation
        |
ModelBackend
  |          |          |
SGLang   Transformers  llama.cpp/GGUF
```

The existing independent yes/no scorer is the baseline, not a permanently fixed architecture. Preserve it while introducing alternative scorers behind a common abstraction.

Requirements:

- zero-training operation remains a hard baseline;
- preserve Jev-style Choice, Score, and Noul outputs;
- do not make the semantic layer BitNet-specific;
- do not introduce free-form generation when direct scoring/logits suffice;
- keep scoring strategy independent from runtime/backend;
- preserve or improve shared-prefix/KV reuse;
- expose raw scores separately from normalized relative probabilities when applicable;
- do not describe normalized candidate scores as calibrated correctness probabilities unless calibration has actually been measured;
- benchmark competing approaches before changing the preferred/default strategy.

Autoregressive and masked/diffusion runtimes may require different low-level primitives. Do not force masked models into an autoregressive interface merely for uniformity; normalize at the semantic candidate-score layer instead.

## Build, Test, and Development Commands

- `uv sync --extra sglang` creates `.venv` and installs the SGLang backend.
- `uv sync --extra transformers` installs the Transformers-only backend dependencies.
- `uv run python -m unittest discover -s tests -v` runs the complete test suite.
- `uv run python -m compileall -q src tests` recursively checks syntax for source and tests.
- `uv build` verifies source and wheel package construction.

Python 3.10 or newer is required unless project metadata is deliberately changed.

## Coding Style & Naming Conventions

Use four-space indentation, type annotations, and standard-library features unless a dependency has a demonstrated need. Use `PascalCase` for public classes, `snake_case` for functions and modules, and leading underscores for internal helpers. Keep public APIs small and re-export them deliberately from `llm2jev.__init__`. Prefer frozen, keyword-only dataclasses for immutable protocol objects. No formatter or linter is currently configured; follow the existing style and avoid unrelated formatting changes.

Prefer small explicit interfaces such as `ScoringStrategy` and `ModelBackend` over backend-specific conditionals distributed through protocol code.

## Testing Guidelines

Use `unittest.TestCase` and descriptive `test_<behavior>` methods. Every validation rule needs both a valid serialization case and an invalid-input case. Model-facing work should first use deterministic fake backends; ordinary tests must not require network access or model downloads.

For scorer refactors, retain regression tests proving the existing binary path is behaviorally unchanged. For continuation scoring, include unequal-token-length candidates and verify raw conditional scores independently of normalization. Backend-specific optimizations need correctness tests before performance claims.

Run the full suite and recursive compile check before submitting changes.

## Research and Benchmark Discipline

Keep experimental knobs explicit and configurable. Do not tune evaluator choices on held-out test data.

When reporting comparative results, record enough environment information to reproduce them, including model/revision, quantization, backend/runtime revision, hardware, thread settings, scorer configuration, dataset/split, and prompt/template configuration where relevant.

Track accuracy and robustness alongside performance. The current research plan includes accuracy, NLL/Brier/ECE where meaningful, order and prompt perturbation stability, selective prediction, latency, throughput, RAM/model footprint, and CPU efficiency.

## Commit & Pull Request Guidelines

Use concise imperative commit subjects, for example `Add continuation scoring strategy`. Keep commits focused. Pull requests should explain the behavior change, list verification commands, link the relevant issue, and identify protocol, scoring, probability, or performance assumptions.

For architecture, methodology, default-strategy, or benchmark-policy changes, update `docs/research-design.md` in the same PR and add/supersede a decision ID as appropriate.

Include sample JSON for wire-format changes. Include benchmark artifacts or machine-readable results for performance/quality claims when practical.

## Current Research Sequence

The current roadmap is tracked in issue #1. In broad terms:

1. establish and record the upstream baseline;
2. extract the existing binary scorer behind a scoring-strategy abstraction without changing behavior;
3. add a generic llama.cpp/GGUF backend and verify CPU execution/prefix reuse;
4. implement full candidate continuation likelihood and its explicit normalization/correction options;
5. integrate and benchmark BitNet through the generic backend boundary;
6. build reproducible comparative evaluation;
7. evaluate label-token and masked/diffusion approaches as additional experiments.

Do not skip baseline measurement or correctness validation merely to reach later experimental phases sooner.
