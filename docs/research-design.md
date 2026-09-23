# Research architecture and decision log

This document is the durable source of truth for the research fork. Keep implementation rationale here; use the tracking issue for operational task status.

## Goal

Turn LLM2Jev into a model-agnostic, zero-training semantic decision engine that can compare inference/scoring strategies on local models, with CPU execution as a first-class target.

Primary constraints:

- no fine-tuning or project-specific training data required;
- preserve Jev-style typed outputs (Choice, Score, Noul);
- support interchangeable model runtimes;
- avoid free-form generation when a distribution can be read/scored directly;
- make scoring strategy independent from model backend;
- optimize shared-prefix/KV reuse;
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

## Initial decisions

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

Length normalization and null-context/prior correction must be explicit experimental parameters, not hidden behavior.

### D006 — Preserve independent binary scoring as baseline
**Status:** accepted

LLM2Jev's yes/no candidate scoring remains the compatibility/reference strategy. It is naturally candidate-order invariant and provides a direct comparison against continuation scoring.

### D007 — Benchmark before choosing a preferred scorer/model
**Status:** accepted

Do not declare binary, label, continuation, BitNet, Qwen, or diffusion superior without benchmark evidence.

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

## Planned implementation phases

### Phase 0 — Repository baseline
- [x] Fork upstream LLM2Jev.
- [x] Remove Chinese duplicate documentation.
- [ ] Verify existing tests on the research fork.
- [ ] Record baseline behavior/performance for existing backends.

### Phase 1 — Scoring abstraction
- [ ] Define `ScoringStrategy` interface.
- [ ] Refactor current yes/no implementation behind `BinaryScorer` without behavior change.
- [ ] Add scorer-level unit tests.
- [ ] Keep API compatibility.

### Phase 2 — llama.cpp backend
- [ ] Define minimal generic `ModelBackend` contract.
- [ ] Implement llama.cpp/GGUF backend.
- [ ] Expose tokenization, prefill/logits and continuation scoring primitives needed by scorers.
- [ ] Test with at least one conventional GGUF model.
- [ ] Test CPU-only execution.
- [ ] Measure shared-prefix/KV reuse.

### Phase 3 — Continuation scorer
- [ ] Implement full conditional continuation log-likelihood.
- [ ] Batch candidate suffixes where backend permits.
- [ ] Implement configurable length normalization.
- [ ] Implement optional null-context/prior correction.
- [ ] Return raw and normalized scores separately.
- [ ] Test candidates with unequal token lengths.

### Phase 4 — BitNet
- [ ] Establish a known-good BitNet/bitnet.cpp model/runtime baseline.
- [ ] Integrate through the generic backend boundary.
- [ ] Verify model-specific activation/runtime correctness before benchmarking.
- [ ] Benchmark binary vs continuation scoring on CPU.

### Phase 5 — Evaluation harness
- [ ] Build reproducible benchmark configuration.
- [ ] Add option-order perturbations.
- [ ] Add prompt-paraphrase perturbations.
- [ ] Add abstention/insufficient-information experiments.
- [ ] Integrate or interoperate with lm-evaluation-harness where useful.
- [ ] Save machine-readable results and environment metadata.

### Phase 6 — Experimental backends
- [ ] Evaluate label-token scorer.
- [ ] Define `MaskedBackend` scoring primitive.
- [ ] Evaluate small masked/diffusion models if CPU feasibility is credible.
- [ ] Compare against autoregressive baselines under the same semantic API.

## Change protocol

For meaningful research changes:

1. Link the change to the tracking issue.
2. Update this document when architecture, assumptions, interfaces, benchmark methodology, or accepted decisions change.
3. Add a new decision ID instead of silently rewriting an old rationale when a decision is reversed.
4. Record supersession explicitly (for example, “D004 superseded by D012”).
5. Keep experimental defaults configurable until evidence supports making them normative.
6. Commit benchmark configuration/results needed to reproduce conclusions; do not rely only on prose claims.

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
