# Repository Guidelines

## Research Fork Context

This repository is the `llm2jev-research` fork of LLM2Jev. Its purpose is to research a model-agnostic, zero-training Jev-style semantic decision engine, with local CPU/GGUF inference as a first-class target.

Before making architectural or research changes, read:

- `docs/research-design.md` — source of truth for goals, architecture, accepted decisions, methodology, phase definitions, and open questions.
- GitHub issue #1 — **authoritative operational task/status tracker**.
- Existing relevant user-facing documentation under `docs/`.

Do not duplicate task completion state in `README.md` or `docs/research-design.md`; keep checkboxes and operational status in issue #1. Do not silently replace accepted design decisions. If evidence requires a change, add a new decision entry to `docs/research-design.md` and explicitly supersede the prior decision. Link meaningful implementation work to issue #1 or a more specific issue created from it.

## Maintaining AGENTS.md

Keep this file current. When a repository change makes any instruction in `AGENTS.md` inaccurate or incomplete—including repository structure, architectural boundaries, canonical documents, development commands, supported runtimes, testing requirements, or required workflows—update `AGENTS.md` in the same commit or pull request.

Do not use `AGENTS.md` for transient state such as task completion, active branches, benchmark results, temporary experiments, or current issue status. Put those in their designated trackers or documentation.

Before completing a substantive repository change, check whether it invalidates any statement in `AGENTS.md`, `README.md`, or `docs/research-design.md`, and update the appropriate authoritative document in the same change.

## Project Structure & Module Organization

This repository uses a Python `src` layout. Keep stable public imports in `src/llm2jev/__init__.py`. Protocol and domain objects live in `src/llm2jev/models/`; inference, prompt rendering, scoring, normalization, backend integration, and response assembly live under `src/llm2jev/inference/`. Shared internal JSON and probability helpers belong in `src/llm2jev/utils/`, not the public package API. Tests mirror these responsibilities under `tests/` using `test_<module>.py` names.

User-facing and research documentation is version-controlled under `docs/`. Do not rely on ignored/local design documents for architectural authority.

## Graphify Knowledge Graph

The repository keeps a shared Graphify code knowledge graph under `graphify-out/`. GitHub Actions refreshes it on pushes to `main` using pinned `graphifyy==0.9.66`, with AST/code-only extraction so CI requires no model API key.

When `graphify-out/graph.json` exists:

- use `graphify query "<question>"` for codebase orientation before broad source browsing;
- use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts;
- treat `graphify-out/GRAPH_REPORT.md` as broad architecture context, not as a substitute for source-of-truth code;
- after local code changes, refresh with `uvx --from graphifyy==0.9.66 graphify update .` when an up-to-date graph is useful during the same working session;
- do not assume documentation/PDF semantic nodes are refreshed by CI: the GitHub workflow intentionally maintains the code graph only.

The workflow is `.github/workflows/update-graphify.yml`. If its Graphify version, output layout, maintenance commands, or CI behavior changes, update this section in the same change.

## Reference Implementations

For architecture/scoring/backend work, consult the role-specific references listed in `docs/research-design.md` before inventing a new mechanism. In particular: upstream LLM2Jev for the current binary/API behavior; AnyJev for label-token debiasing; daseinlabs/open-jev for continuation likelihood and prefix-shared option scoring; lm-evaluation-harness for evaluation abstractions; llama.cpp for GGUF/CPU runtime behavior; Microsoft BitNet for ternary inference; and razorback16/openjev for masked/diffusion readout.

Treat these as references, not specifications. Preserve this repository's accepted decisions and generic interfaces unless evidence justifies a documented design change.

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

The existing independent yes/no scorer is the baseline, not a permanently fixed architecture. Preserve it while introducing alternative scorers behind a common abstraction. Its prefill-only next-token behavior is a property of the current binary strategy, not a requirement that should be imposed on continuation or masked/diffusion strategies.

Requirements:

- zero-training operation remains a hard baseline;
- preserve Jev-style Choice, Score, and Noul outputs;
- do not make the semantic layer BitNet-specific;
- do not introduce free-form generation when direct scoring/logits suffice;
- keep scoring strategy independent from runtime/backend;
- preserve or improve shared-prefix/KV reuse where the scorer/backend permits it;
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

This is a research repository. Use testing to keep experiments interpretable, not to pursue production-grade coverage.

`docs/testing.md` records the inherited model-free baseline. The CI workflow in `.github/workflows/unit-tests.yml` is a lightweight regression guardrail for `main`.

Guidelines:

- run the existing model-free suite for changes intended for `main`;
- add small deterministic tests for scoring equations, normalization, token/candidate alignment, serialization that feeds experiments, and regressions that would make results misleading;
- fake backends are useful when they make semantic logic easy to test, but do not build elaborate mocks solely to satisfy coverage;
- do not require a unit test for every validation branch or temporary research knob;
- real-model validation is performed when the experiment actually depends on model/runtime behavior; it does not block unrelated code work;
- do not claim a real-model result unless that model/runtime was actually run;
- exploratory branches may temporarily break compatibility or omit tests if that materially accelerates learning; clean up the winning path before treating it as adopted.

The standard lightweight checks are:

```bash
uv run python -m unittest discover -s tests -v
uv run python -m compileall -q src tests
uv build
```

Use additional external integration or benchmark scripts only when needed to answer the current research question.

## Research and Benchmark Discipline

Optimize first for fast, informative comparisons. Do not build a general benchmark framework before a concrete comparison needs it.

For quick exploratory runs, record only enough context to understand the result. When an experiment is used to choose a preferred scorer/model/runtime or support a durable claim, then capture the relevant model/revision, quantization, backend/runtime revision, hardware, thread settings, scorer configuration, dataset/split, prompt/template, and result artifacts.

Use the relevant metrics for the hypothesis being tested rather than computing the full metric catalog every time. Accuracy/robustness and CPU latency/throughput are likely early discriminators; calibration, perturbation suites, RAM/energy, and selective prediction can be added when they materially affect a decision.

Do not tune final evaluator choices on held-out test data. For independent binary scoring, remember that candidate scores are order-independent by construction while deterministic tie-breaking may still depend on original criteria order.

## Commit & Pull Request Guidelines

Use concise imperative commit subjects, for example `Add continuation scoring strategy`. Keep commits focused. Pull requests for durable changes should explain the research question/behavior change and note meaningful verification. Small exploratory commits do not need production-style PR ceremony.

For architecture, methodology, default-strategy, or benchmark-policy changes, update `docs/research-design.md` in the same PR and add/supersede a decision ID as appropriate.

Include reproducible benchmark artifacts when a performance/quality result is being used to make a durable design decision.

## Current Research Sequence

Issue #1 owns task completion status. The non-status phase sequence is:

1. establish and record the upstream baseline;
2. extract the existing binary scorer behind a scoring-strategy abstraction without changing behavior;
3. add a generic llama.cpp/GGUF backend and verify CPU execution/prefix reuse;
4. implement full candidate continuation likelihood and its explicit normalization/correction options;
5. integrate and benchmark BitNet through the generic backend boundary;
6. build reproducible comparative evaluation;
7. evaluate label-token and masked/diffusion approaches as additional experiments.

The phase order is advisory. Spike later ideas early when doing so can invalidate an assumption or avoid unnecessary abstraction work.
