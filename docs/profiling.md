# Performance profiling methodology

This project compares semantic-decision inference rather than generic chat generation. Profiling should therefore use the actual Jev workloads: shared prefixes, multiple candidates, binary and continuation scoring, and candidate batching.

The goal is to explain *why* an approach is fast or slow, not just report tokens/s.

## Experiment matrix

When profiling a model/runtime that matters to a research decision, compare the relevant subset of:

- dense versus sparse/MoE models at similar active-parameter scale;
- CPU-only;
- GPU-only;
- CPU+GPU/hybrid offload where supported;
- batch/candidate counts representative of Jev requests;
- short versus long shared prefixes;
- binary next-token scoring versus continuation scoring;
- cold versus warm cache where meaningful.

For MoE models, record both total parameter count and estimated/declared active parameters per token. Do not use total parameters alone as a compute proxy.

## Common workload metrics

Always prefer semantic-work metrics over generic generation metrics:

- requests/s;
- candidates/s;
- prefill tokens/s;
- scored candidate tokens/s where continuation scoring is used;
- end-to-end latency per Jev request;
- time spent in prefill versus candidate scoring;
- peak resident RAM and VRAM;
- model footprint and KV-cache footprint;
- CPU/GPU energy when it is easy to obtain;
- decision quality on the same workload when comparing different models.

Generic tokens/s may also be recorded, but it is not the primary optimization target.

## CPU profiling

Use lightweight wall-clock/RSS measurements first, then hardware counters for runs that influence optimization choices.

Recommended tools:

- `llama-bench` or equivalent runtime-native benchmark for a baseline;
- Linux `perf stat` for cycles, instructions, IPC, cache references/misses, branch behavior, page faults, and elapsed CPU time;
- `perf record/report` for hotspot attribution when needed;
- Intel PCM on supported Intel hosts for memory-controller bandwidth, memory traffic, cache behavior, and NUMA/socket effects;
- platform/vendor equivalents on AMD or other CPUs where available;
- `numactl` / topology inspection to make socket and memory placement explicit for multi-socket systems.

For CPU comparisons, capture when practical:

- effective DRAM read/write bandwidth and fraction of measured sustainable bandwidth;
- LLC misses and LLC miss rate;
- L1/L2/LLC behavior when available;
- IPC and cycles per scored token/candidate;
- context switches and major page faults;
- NUMA remote-memory traffic on multi-socket systems;
- thread count, affinity/pinning, SIMD capability, and runtime build flags.

A simple STREAM-like memory-bandwidth baseline should be measured on the same host so model bandwidth can be interpreted relative to achievable memory bandwidth.

## GPU profiling

GPU profiling is required for meaningful CPU-vs-GPU or hybrid conclusions.

Recommended NVIDIA tools:

- `nvidia-smi` / `nvidia-smi dmon` for coarse utilization, clocks, power, temperature, VRAM use, and PCIe activity;
- Nsight Systems for CPU/GPU timelines, kernel launch gaps, synchronization, transfers, and overlap;
- Nsight Compute for selected kernels when deeper analysis is needed, including memory throughput, cache hit behavior, occupancy, warp utilization, and compute/memory bottlenecks.

Recommended AMD tools where applicable:

- ROCm system monitoring tools for utilization, clocks, power, memory use, and transfers;
- `rocprof`/rocprofiler tooling for kernel timelines and hardware counters.

For GPU comparisons, capture when practical:

- HBM/VRAM bandwidth and percentage of available bandwidth;
- SM/CU utilization;
- achieved occupancy;
- L2/cache hit behavior;
- kernel launch count and launch gaps;
- host-to-device/device-to-host transfer volume and time;
- PCIe or interconnect utilization for offloaded/hybrid runs;
- VRAM footprint and KV-cache footprint;
- power and energy/request where easy to measure.

Do not infer that low GPU utilization means the model is compute-light without checking memory bandwidth, launch/synchronization overhead, and CPU-side feeding.

## MoE-specific profiling

Sparse MoE experiments need routing and reuse measurements in addition to ordinary CPU/GPU counters.

Record or instrument, where the runtime exposes enough information:

- experts selected per token;
- distribution of tokens across experts;
- expert-load imbalance;
- unique experts touched per layer and per batch;
- repeated expert selections within a candidate batch;
- expert reuse across candidates sharing a prefix;
- expert reuse across continuation tokens;
- estimated bytes of expert weights touched per scored token;
- routing overhead as a fraction of runtime;
- batching/grouping effectiveness for tokens routed to the same expert.

Useful derived quantities include:

```text
expert_reuse = routed_token_expert_uses / unique_expert_load_events
expert_batch_size = routed_tokens_to_expert / expert_invocations
bandwidth_per_scored_candidate = memory_bytes / candidates_scored
```

The exact notion of an "expert load event" depends on the runtime/cache hierarchy. Treat it as an instrumentation metric, not a universal architectural quantity.

If llama.cpp or another runtime does not expose routing statistics, prefer a small optional tracing/instrumentation patch or profiler hook over redesigning the semantic API.

## Cache and prefix-reuse profiling

For Jev workloads, distinguish three different reuse mechanisms:

1. shared prompt/KV reuse;
2. CPU/GPU hardware-cache reuse of model/expert weights;
3. MoE expert reuse from batching tokens that route to the same experts.

Measure them separately.

Experiments should vary:

- number of candidates;
- shared-prefix length;
- continuation length;
- batch size;
- cold versus warm execution;
- candidate ordering where it may change runtime grouping.

A useful research question is whether increasing candidate batching reduces effective memory bytes per candidate even when latency per individual token does not improve.

## Test/profiling suite structure

Performance profiling is an external research suite, not part of model-free CI.

As the llama.cpp experiment becomes runnable, add lightweight scripts under a dedicated profiling/benchmark directory that can:

1. run a fixed Jev workload and emit machine-readable timing/memory results;
2. optionally wrap the run with `perf stat`;
3. optionally collect Intel PCM or platform-equivalent bandwidth counters;
4. optionally wrap NVIDIA runs with Nsight Systems and coarse `nvidia-smi` telemetry;
5. optionally collect selected Nsight Compute or ROCm counters for focused kernels;
6. capture MoE routing/expert-reuse traces when available;
7. label each run as CPU, GPU, or hybrid/offload;
8. record model, quantization, runtime revision, threads, batch size, candidate count, prefix length, and hardware identity.

Do not make every profiler a hard dependency. Each collector should be optional, and the experiment should still run with basic timing if a profiler is unavailable.

## Interpretation

The main MoE hypothesis to test is:

> A model with a much larger total parameter count but a small active parameter count per token may provide better semantic-decision quality per unit of compute, especially when RAM capacity is plentiful and Jev candidate batching creates expert reuse.

The competing hypothesis is that irregular expert access and memory traffic dominate, making the MoE bandwidth-bound enough that a smaller dense model is faster or more efficient.

CPU, GPU, and hybrid profiling should determine which regime actually applies rather than assuming either outcome.
