# Research architecture and decision log

This document is the durable source of truth for research architecture, rationale, methodology, phase definitions, and design decisions. **GitHub issue #1 is the sole authoritative tracker for task completion/status.** Do not mirror operational checkboxes here.

## Goal

Turn LLM2Jev into a model-agnostic, zero-training semantic decision engine that can compare inference/scoring strategies on local models, with CPU execution as a first-class target.

Primary constraints:

- no fine-tuning or project-specific training data required;
- preserve Jev-style typed outputs (Choice, Score, Noul);
- support interchangeable model runtimes;
- avoid free-form generation when a distribution can be read/scored directly;
- make scoring strategy independent from model backend;
- optimize shared-prefix/KV reuse where the scorer/backend permits it;
- benchmark correctness, robustness, calibration-like behavior, latency, throughput, memory, and CPU efficiency.

## Architecture direction

```text
Jev-compatible API
        |
Typed question layer
        |
ScoringStrategy
  |        |           |
binary   label    continuation
yes/no   logits    likelihood
        |
ModelBackend
  |          |          |
SGLang   Transformers  llama.cpp/GGUF
                         |
                 Qwen / Gemma / BitNet / ...
```

Masked/diffusion models should use a separate low-level backend primitive rather than pretending to be autoregressive. The semantic layer should consume candidate scores without depending on how the backend produced them.

## Reference implementations and inspiration

These repositories are design references, not automatically runtime dependencies. Reuse concepts and validate behavior; do not copy backend-specific assumptions into the generic semantic API.

- **[Yinsongxu/LLM2Jev](https://github.com/Yinsongxu/LLM2Jev)** — upstream application base. Reference for the Jev-compatible API, typed Choice/Score/Noul handling, independent binary yes/no candidate scoring, SGLang/Transformers backends, and staged shared-prefix reuse.
- **[nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev)** — reference for training-free label-token readout, option-order debiasing through repeated/permuted readouts, and content-free/intrinsic label-prior correction. Its optional labeled calibration is not part of this project's zero-training baseline.
- **[daseinlabs/open-jev](https://github.com/daseinlabs/open-jev)** — primary reference for full candidate-continuation likelihood: prefill the shared context once, branch/expand the KV state, score complete option token sequences in a batch, and compare explicit sum/mean/PMI-style normalization. Its MLX/Gemma-specific implementation is a reference, not an architectural constraint.
- **[EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)** — reference for benchmark/task abstractions, conditional log-likelihood interfaces, reproducible task configuration, and result metadata. Prefer interoperability over reimplementing mature benchmark plumbing.
- **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** — target generic GGUF/CPU inference runtime and reference for tokenization, logits, KV-cache/session behavior, batching, and local server/library APIs. Do not fork or modify optimized internals unless profiling demonstrates that the public/runtime interfaces cannot meet requirements.
- **[microsoft/BitNet](https://github.com/microsoft/BitNet)** — official bitnet.cpp reference for 1-bit/ternary model inference and optimized CPU kernels. BitNet support must enter through the generic backend boundary rather than creating BitNet-specific semantic logic.
- **[razorback16/openjev](https://github.com/razorback16/openjev)** — reference for masked/discrete-diffusion decision readout, where several answer slots can be scored in parallel. Use it to inform a distinct masked-backend primitive rather than forcing diffusion models into the autoregressive continuation interface.

When a new external project materially influences an interface, scoring method, benchmark methodology, or optimization, add it here with the exact concept being adopted or compared.

## Decisions

### D001 — Fork LLM2Jev as the application base
**Status:** accepted

Keep its Jev-compatible API, typed questions, tests, and existing SGLang/Transformers support. Extend rather than rewrite.

### D002 — No training is required
**Status:** accepted

The baseline must work zero-shot. Optional empirical calibration may be researched later, but cannot be required for normal operation.

### D003 — Separate scoring strategy from inference backend
**Status:** accepted

Do not encode binary yes/no scoring into the backend interface. A backend exposes model inference primitives; a scoring strategy converts those primitives into candidate scores.

This allows the same model/runtime to compare:
1. LLM2Jev-style independent binary yes/no scoring;
2. label-token scoring;
3. full candidate continuation likelihood.

Current thin implementation: `ScoringStrategy` exposes only `score(request: JevRequest) -> JevResponse`. `BinaryScorer` owns the existing `BinaryBackend`, prompt renderer, normalization, and response assembly path. `LLM2Jev` accepts either the legacy `backend=` path or an explicit `scoring_strategy=`. This boundary is intentionally provisional: the llama.cpp and continuation experiments should determine whether a lower-level generic `ModelBackend` contract is actually needed and what it must expose.

### D004 — Add llama.cpp/GGUF as the first new backend
**Status:** accepted

Reason: broad local-model support and CPU-oriented execution. BitNet is an important target, but the interface must not be BitNet-specific.

Initial implementation should avoid modifying llama.cpp itself. Optimize/native-extend only if profiling justifies it.

### D005 — Full candidate continuation likelihood is an experimental scoring strategy
**Status:** accepted for implementation and comparison; not selected as default

For candidate C=(c1,...,cN), score conditional token likelihood:

```text
L(C|X) = sum_t log P(c_t | X, c_<t)
```

Length normalization and null-context/prior correction must be explicit experimental parameters, not hidden behavior. Unlike the current binary scorer's single next-token yes/no readout, continuation likelihood teacher-forces the candidate token sequence.

### D006 — Preserve independent binary scoring as baseline
**Status:** accepted

LLM2Jev's yes/no candidate scoring remains the compatibility/reference strategy. Individual candidate inputs and scores are order-independent by construction because candidates are evaluated independently. Deterministic tie-breaking may still depend on the original `criteria` order.

### D007 — Benchmark before choosing a preferred scorer/model
**Status:** accepted

Do not declare binary, label, continuation, BitNet, Qwen, or diffusion superior without benchmark evidence.

### D008 — Split testing by execution environment
**Status:** accepted

Development may be performed in an OpenAI cloud sandbox that is suitable for ordinary Python/unit testing but cannot be assumed to have GPU access, persistent multi-gigabyte model weights, specialized runtimes, or reliable access to download/run real LLMs.

Therefore correctness validation is split into two explicit layers:

1. **Sandbox-safe tests (mandatory for implementation changes):** deterministic unit/regression tests, fake/model-stub backends, scorer mathematics, prompt/request compilation, serialization, normalization, API contracts, mocked runtime/HTTP behavior, syntax checks, and package builds. These tests must not require model downloads, network access, GPUs, or external API keys.
2. **External real-model integration tests:** actual Transformers/SGLang model loading, llama.cpp/GGUF execution, BitNet/bitnet.cpp numerical/runtime validation, KV-cache behavior against a real runtime, quality benchmarks, latency/throughput/RAM/energy measurements, and cross-runtime numerical comparisons. These run on an explicitly provisioned local/external machine or future self-hosted runner.

The sandbox limitation must never be hidden by marking a real-model test as passed. A change that requires external validation must commit the test command/configuration and state that it was not run in the sandbox until external results are available. Architecture should remain testable through deterministic backend contracts so most logic can be validated without model weights.

Ordinary hosted CI should remain model-free unless a deliberately provisioned integration runner is added later.

### D009 — Optimize for research velocity, not production hardening
**Status:** accepted

This is an exploratory research fork. The primary objective is to obtain useful comparative evidence quickly, not to reach production-grade test coverage, interface stability, deployment hardening, or exhaustive validation before trying an idea.

Consequences:

- implementation phases are a direction of travel, not blocking stage gates;
- small spikes and temporary experimental code are acceptable when they answer a research question faster;
- prefer the simplest implementation that can produce trustworthy evidence, then refactor abstractions that survive comparison;
- add tests where they protect scoring mathematics, important transformations, or regressions likely to confuse experiments; do not add tests merely for coverage completeness;
- the existing model-free CI is a lightweight guardrail, not a definition of research completeness;
- real-model commands, environment metadata, and benchmark artifacts only need to become reproducible when a result is being compared, reported, or used to make a durable design/default decision;
- exploratory real-model runs may be manual and minimally scripted;
- API compatibility may be temporarily broken on research branches when that substantially speeds an experiment, provided durable/public behavior is reconciled before declaring an approach adopted;
- avoid building generalized infrastructure before at least one concrete experiment demonstrates that it is needed.

D009 supersedes the process-heavy interpretation of D008. D008 still defines the difference between model-free and real-model validation, but it does not require both layers for every implementation change.

## Metrics

When making a comparative claim or choosing a preferred approach, record the relevant subset of:

- task accuracy;
- NLL where meaningful;
- Brier score where meaningful;
- ECE/reliability diagnostics with limitations stated;
- candidate/order perturbation consistency;
- prompt paraphrase consistency;
- selective prediction / coverage vs accuracy;
- top-two margin and entropy;
- prefill latency;
- scoring latency;
- questions/s and candidates/s;
- peak RAM;
- model footprint;
- CPU utilization and, where measurable, energy/question.

Candidate benchmark sources include MMLU-Pro, ARC-Challenge, HellaSwag, PIQA, BoolQ, WinoGrande, TruthfulQA-MC, ANLI/MNLI and selected BBH tasks. Use development data for evaluator choices and preserve held-out evaluation data.

## Implementation phases

Operational task state for every phase belongs in [issue #1](https://github.com/manu080797/llm2jev-research/issues/1). The phase descriptions here define scope and sequencing only.

### Phase 0 — Repository baseline

Establish a lightweight baseline: inventory the inherited tests, run the model-free suite, compile the package, and confirm that the existing binary path has fake-backend coverage. This is enough to begin research. Real-model baselines, detailed environment schemas, and additional integration infrastructure are deferred until they are needed for an actual comparison.

### Phase 1 — Scoring abstraction

Introduce the thinnest useful `ScoringStrategy` boundary and place the current yes/no path behind `BinaryScorer`. Preserve behavior where convenient, but do not over-design the interface before continuation and llama.cpp experiments exercise it. Add only targeted tests needed to protect scorer math and the existing baseline.

### Phase 2 — llama.cpp backend

Get a conventional GGUF model scoring candidates through llama.cpp on CPU by the simplest maintainable route. Let that concrete implementation inform the eventual `ModelBackend` contract rather than designing the full abstraction up front. Add lightweight contract tests for fragile parsing/scoring logic; investigate KV reuse once basic scoring works.

### Phase 3 — Continuation scorer

Implement full conditional continuation log-likelihood early enough to compare it with the binary baseline. Start with a correct simple version; add batching/KV branching, length normalization variants, and null-context correction only as experiments require them. Use small deterministic tests for the scoring equation and unequal-length candidates.

### Phase 4 — BitNet

Try BitNet through the emerging generic boundary as soon as llama.cpp/continuation experiments make that boundary concrete. Prioritize getting real CPU measurements over building exhaustive mocks. Keep BitNet-specific details below the semantic scoring layer and compare only the metrics needed to decide whether the runtime is promising.

### Phase 5 — Comparative evaluation

Once two or more approaches are worth comparing, add the minimum evaluation plumbing needed for a fair comparison. Reuse lm-evaluation-harness or small scripts before building a custom harness. Increase reproducibility, perturbation testing, uncertainty metrics, and machine-readable result capture only for experiments that influence durable design decisions.

### Phase 6 — Experimental backends

Spike label-token and masked/diffusion approaches with minimal plumbing. Promote an experiment into the common architecture only if results justify continued work; otherwise keep the prototype disposable.

## Change protocol

Keep process proportional to the research value of the change:

1. Use issue #1 as the task tracker, but do not create extra process artifacts for small experiments.
2. Update this document when a **durable** architecture, methodology, or default decision changes; temporary implementation details do not need decision-log entries.
3. Keep operational completion/status only in GitHub issues.
4. When reversing an accepted durable decision, add a new decision ID and explicitly supersede the old one.
5. Keep experimental knobs configurable while they are genuinely under comparison; remove dead knobs after experiments settle.
6. Preserve enough commands/results to reproduce evidence that is used to choose an approach. Disposable exploratory runs do not need production-grade provenance.
7. Run the lightweight CI guardrail for changes headed to `main`; add targeted tests when a failure would invalidate or confuse an experiment.

## Decision template

```markdown
### Dxxx — Decision title
**Status:** proposed | accepted | rejected | superseded

**Context:** What problem requires a decision?

**Decision:** What are we doing?

**Rationale:** Why?

**Alternatives:** What else was considered?

**Evidence:** Benchmarks/issues/commits supporting the decision.

**Consequences:** Tradeoffs and follow-up work.
```

## Open design questions

- What is the smallest backend interface that supports both efficient next-token scoring and batched continuation likelihood without leaking runtime-specific concepts?
- Should continuation length normalization default to sum, mean, or a configurable exponent only?
- How should null-context correction be defined across Choice, Score and Noul?
- Can llama.cpp expose sufficiently efficient KV branching through the selected integration, or will a native extension eventually be justified?
- Does BitNet's CPU efficiency offset any semantic-quality loss relative to conventional 1–4B quantized models?
- Which confidence/uncertainty quantities are useful without claiming statistical calibration that has not been measured?
