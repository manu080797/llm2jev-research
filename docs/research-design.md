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

## Metrics

At minimum record:

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

Inventory the inherited tests and classify them as sandbox-safe or real-model integration tests. Run and document all sandbox-safe tests, compile/build checks, and deterministic fake-backend coverage for the existing binary path. Document reproducible commands and environment requirements for the inherited Transformers/SGLang real-model tests; execute and record those baselines only on a suitable external/local environment. Establish benchmark metadata conventions before architectural refactoring.

### Phase 1 — Scoring abstraction

Define `ScoringStrategy`, move the existing yes/no behavior behind `BinaryScorer` without observable behavior change, preserve API compatibility, and add deterministic scorer-level regression tests using fake backends. Real-model regression remains an external integration check, not a prerequisite that can be falsely satisfied inside the sandbox.

### Phase 2 — llama.cpp backend

Define the minimal generic `ModelBackend` contract and implement llama.cpp/GGUF support for CPU execution. Validate request construction, parsing, error handling, scorer/backend contracts, and deterministic mocked responses in the sandbox. Commit a reproducible external integration command that runs at least one conventional GGUF model on CPU. KV reuse, numerical behavior, and performance claims require that external real-runtime test; measure them rather than assuming benefit.

### Phase 3 — Continuation scorer

Implement full conditional continuation log-likelihood, efficient candidate batching/branching where supported, explicit length normalization, optional null-context/prior correction, separate raw and normalized scores, and unequal-length candidate tests. The mathematics and backend contract must be fully unit-testable with deterministic logits/token sequences in the sandbox; real-model agreement and throughput are external integration checks.

### Phase 4 — BitNet

Implement the generic integration and unit-test its backend contract in the sandbox. Establish a known-good BitNet/bitnet.cpp model/runtime baseline, numerical correctness, binary-versus-continuation comparison, and CPU performance only in a suitable external environment with the actual BitNet runtime and weights. Do not introduce BitNet-specific semantics.

### Phase 5 — Evaluation harness

Build reproducible benchmark configuration and machine-readable result schemas. Unit-test dataset adapters, perturbation generation, metric calculations, aggregation, and result serialization from fixtures in the sandbox. Actual model quality, uncertainty, latency, throughput, memory, and energy results are produced only by external real-model runs. Interoperate with lm-evaluation-harness where useful.

### Phase 6 — Experimental backends

Implement and unit-test label-token and `MaskedBackend` semantic contracts with deterministic fixtures in the sandbox. Run small masked/diffusion models and compare them against autoregressive baselines only in an external environment where the required runtime/weights are available and CPU feasibility can be measured credibly.

## Change protocol

For meaningful research changes:

1. Link the change to issue #1 or a more specific issue derived from it.
2. Update this document when architecture, assumptions, interfaces, benchmark methodology, or accepted decisions change.
3. Keep operational completion/status only in GitHub issues; do not add mirrored task checkboxes here or in the README.
4. Add a new decision ID instead of silently rewriting an old rationale when a decision is reversed.
5. Record supersession explicitly (for example, “D004 superseded by D012”).
6. Keep experimental defaults configurable until evidence supports making them normative.
7. Commit benchmark configuration/results needed to reproduce conclusions; do not rely only on prose claims.
8. For every substantive change, record which sandbox-safe tests were actually run and list any required real-model integration tests as external/not-run until they are executed.

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
