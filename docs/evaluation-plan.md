# Comparative evaluation plan

The project should answer three different research questions without mixing them together.

## Question A — What is the cost of the zero-training constraint?

Compare a purpose-trained typed-decision specialist against zero-training general-purpose models on the same Jev-style workload.

Controls:

- Laya general checkpoint as a trained specialist control;
- Laya typed-decisions only on datasets/splits for which its training relationship is explicitly known and reported;
- optionally laya.cpp as a native-runtime implementation of the same Laya semantics.

Zero-training candidates:

- the inherited independent binary scorer;
- label-token scoring;
- continuation likelihood;
- later masked/diffusion scoring.

The purpose is not to "beat Laya" at any cost. The useful result is a Pareto comparison showing how much decision quality, context flexibility, and model generality are obtained for extra latency/memory/energy.

Do not compare an in-domain fine-tuned Laya checkpoint against a zero-shot model and describe the difference as an architecture effect. Label training exposure explicitly.

## Question B — Which zero-training scoring rule works best?

Hold model, runtime, prompt template, dataset, and hardware fixed. Compare:

1. independent binary yes/no;
2. label-token scoring;
3. continuation likelihood;
4. optional null/prior correction variants.

Primary outputs:

- task accuracy or task-appropriate score;
- NLL/Brier/ECE where meaningful;
- order/paraphrase robustness where useful;
- requests/s and candidates/s;
- additional model evaluations required per Jev request.

This isolates the semantic readout method from model/runtime effects.

## Question C — Which model/runtime gives the best local efficiency?

Hold scoring method and workload fixed. Compare:

- small dense models;
- sparse MoE models with similar active-parameter scale;
- BitNet/ternary models;
- CPU, GPU, and hybrid/offload execution;
- llama.cpp/GGUF, BitNet runtime, and other runtimes where relevant.

Measure semantic decision quality together with latency, throughput, RAM/VRAM, memory bandwidth, cache locality, expert reuse, and energy.

This isolates hardware/runtime/model-architecture effects from scoring-method effects.

## Early benchmark set

Do not begin with the full benchmark catalog. Start with a compact research set that exercises the Jev primitives and exposes obvious weaknesses quickly.

The first set should contain:

- binary/noul decisions;
- ordinary multiple-choice questions;
- ordinal score questions;
- both short and long context;
- small and moderately large option counts;
- at least one task where candidate strings vary materially in length;
- a small option-order perturbation subset.

Use public held-out/dev data with no task-specific training. Avoid selecting prompts or normalization variants using the final held-out test split.

Expand to MMLU-Pro, ARC-Challenge, HellaSwag, PIQA, BoolQ, WinoGrande, TruthfulQA-MC, ANLI/MNLI, BBH, or other datasets only after the early set produces informative differences.

## Common result schema

Every comparative run that informs a durable decision should identify:

- experiment ID;
- model and exact revision/checkpoint;
- whether the model/checkpoint has task-specific training exposure;
- quantization/dtype;
- scoring strategy and its parameters;
- runtime and revision;
- CPU/GPU/hybrid mode;
- hardware identity;
- thread/batch/candidate settings;
- dataset and split;
- prompt/template revision;
- accuracy/task score;
- probability metrics where meaningful;
- latency and throughput;
- peak RAM/VRAM;
- profiling artifact references when collected.

Keep the schema small initially. Add fields only when an experiment needs them.

## Fairness rules

- Compare scoring methods on the same model whenever possible.
- Compare runtimes using the same model weights/quantization whenever possible.
- Compare dense vs MoE using both total parameters and active parameters/token.
- Label trained specialist controls separately from zero-training methods.
- Treat Laya typed-decisions as an in-domain fine-tuned control on its own known benchmark, not as a generic zero-shot baseline.
- Do not use raw tokens/s as the main decision metric.
- Prefer Pareto plots over a single composite score.

## First useful Pareto plots

1. decision quality vs median request latency;
2. decision quality vs requests/s;
3. decision quality vs peak RAM/VRAM;
4. decision quality vs energy/request when available;
5. for CPU models: quality vs effective DRAM bandwidth pressure;
6. for MoE models: quality/throughput vs expert reuse and memory traffic.

The expected outcome is a map of useful operating regimes, not one universal winner.
