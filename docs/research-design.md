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

Verify the inherited test suite, record current SGLang/Transformers behavior, and establish reproducible baseline performance/environment metadata before architectural refactoring.

### Phase 1 — Scoring abstraction

Define `ScoringStrategy`, move the existing yes/no behavior behind `BinaryScorer` without observable behavior change, preserve API compatibility, and add scorer-level regression tests.

### Phase 2 — llama.cpp backend

Define the minimal generic `ModelBackend` contract and implement llama.cpp/GGUF support for CPU execution. Expose only the inference primitives needed by scorers, test at least one conventional GGUF model, and measure shared-prefix/KV reuse rather than assuming its benefit.

### Phase 3 — Continuation scorer

Implement full conditional continuation log-likelihood, efficient candidate batching/branching where supported, explicit length normalization, optional null-context/prior correction, separate raw and normalized scores, and unequal-length candidate tests.

### Phase 4 — BitNet

Establish a known-good BitNet/bitnet.cpp baseline, verify model/runtime correctness, integrate it through the generic backend boundary, and compare binary versus continuation scoring on CPU without introducing BitNet-specific semantics.

### Phase 5 — Evaluation harness

Build reproducible benchmark configuration and machine-readable results. Cover representative tasks, option-order perturbations, prompt paraphrases, abstention/insufficient-information experiments, quality/uncertainty metrics, and performance measurements. Interoperate with lm-evaluation-harness where useful.

### Phase 6 — Experimental backends

Evaluate label-token scoring, define an appropriate `MaskedBackend` primitive, test small masked/diffusion models only when CPU feasibility is credible, and compare them against autoregressive baselines under the same semantic API.

## Change protocol

For meaningful research changes:

1. Link the change to issue #1 or a more specific issue derived from it.
2. Update this document when architecture, assumptions, interfaces, benchmark methodology, or accepted decisions change.
3. Keep operational completion/status only in GitHub issues; do not add mirrored task checkboxes here or in the README.
4. Add a new decision ID instead of silently rewriting an old rationale when a decision is reversed.
5. Record supersession explicitly (for example, “D004 superseded by D012”).
6. Keep experimental defaults configurable until evidence supports making them normative.
7. Commit benchmark configuration/results needed to reproduce conclusions; do not rely only on prose claims.

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
