  <p align="center">
    <img src="assets/llm2jev-banner.jpeg" alt="LLM2Jev" width="100%">
  </p>

<div align="center">

# 🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference
<br/>

[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square)](pyproject.toml)
[![License](https://img.shields.io/badge/license-Apache--2.0-green?style=flat-square)](LICENSE)
[![Jev API](https://img.shields.io/badge/API-%2Fv1%2Fsystemone%20compatible-orange?style=flat-square)](docs/usage.md)

**Research fork of LLM2Jev for zero-training, model-agnostic structured decision inference across scoring strategies and local runtimes, with CPU/GGUF execution as a first-class target.**

</div>

> This repository is a research fork of [Yinsongxu/LLM2Jev](https://github.com/Yinsongxu/LLM2Jev). LLM2Jev is an independent open-source project and is not affiliated with or endorsed by Jev or TypeSafe.

## 🔬 Research Fork

The upstream independent yes/no candidate scorer remains the compatibility baseline. This fork is extending the architecture so **scoring strategy** and **model backend** are independent and can be compared under the same Jev-style API.

Current research architecture includes a thin `ScoringStrategy` protocol and `BinaryScorer` wrapper around the inherited yes/no method. `LLM2Jev` still supports the original `backend=` API and can also dispatch directly through `scoring_strategy=`.

Planned research includes:

- continuation and label-token strategies behind the scoring boundary;
- a generic `ModelBackend` boundary informed by the upcoming llama.cpp/GGUF experiment rather than designed fully in advance;
- CPU-oriented evaluation, including BitNet without making the semantic API BitNet-specific;
- shared-prefix/KV reuse across scoring methods where the runtime and scorer permit it;
- reproducible evaluation of decision quality, robustness, uncertainty diagnostics, latency, throughput, memory, and CPU efficiency;
- later masked/diffusion scoring experiments behind an appropriate backend primitive.

No fine-tuning or project-specific training data is required by the baseline design. Competing scorers and models are treated as experiments until comparative evidence supports a default.

See **[Research design and decision log](docs/research-design.md)** for architecture, accepted decisions, methodology, and open questions. **[Issue #1](https://github.com/manu080797/llm2jev-research/issues/1)** is the authoritative implementation task/status tracker.

## ✅ Current LLM2Jev Baseline

The current implementation inherited from upstream uses independent binary candidate judgments:

- **Prefill-only binary scoring:** each candidate is turned into a yes/no judgment and scored from the next-token `yes`/`no` logits without decoding an answer.
- **Candidate-score order independence:** each Choice candidate is evaluated independently, so reordering candidates does not change an individual candidate's input or score. Exact ties are resolved deterministically using the original `criteria` order.
- **Multimodal inputs:** text and images can be combined in `state` or `instructions` using SGLang or Transformers.
- **Shared-prefix reuse:** staged SGLang submissions reuse Radix Cache prefixes within a request.

These properties describe the **current binary scorer**, not hard constraints on every research scorer. In particular, full candidate-continuation likelihood teacher-forces candidate tokens and therefore is not the same single-next-token prefill-only operation.

Candidates share `state`, and candidates for the same question also share its `instructions`. LLM2Jev first scores a real `criteria` candidate to establish the prefix cache, then submits candidates that can reuse it. Each candidate is scored once, reducing repeated computation for long inputs with many candidates.

![Staged candidate scoring reuses state and question instructions through SGLang Radix Cache.](assets/shared-prefix-stages.svg)

Learn how the current baseline works: [From Jev Request to LLM Request](docs/request-to-model.md) → [Shared-prefix design](docs/shared-prefix-cache.md).

## 📰 Upstream Baseline News

- **September 23** - **[MuJoCo pick-and-place demo](demos/pick_place/README.md):** added LLM2Jev control of a simulated Panda arm with per-step decision.
- **September 22** - **[Multimodal inputs](docs/multimodal.md):** added text-and-image requests for SGLang, Transformers, and the System One HTTP API.
- **September 21** - **[Web and Snake demos](#demos):** added interactive examples for composing mixed questions and model-driven decisions.
- **September 21** - **Prefix reuse on cold requests:** added staged candidate submission for reusing SGLang's Radix Cache, with [architecture](docs/request-to-model.md), [usage](docs/shared-prefix-cache.md), and [benchmark](docs/shared-prefix-benchmarks.md) documentation.
- **September 20** - **SGLang and System One API:** added the SGLang scoring backend and a compatible [`POST /v1/systemone`](docs/usage.md#system-one-http-api) endpoint.

## 🚀 Quick Start

The currently implemented backends are the upstream SGLang and Transformers paths. llama.cpp/GGUF CPU support is part of the research roadmap and is not implemented yet.

On Linux with a supported NVIDIA GPU, run the current SGLang baseline:

```bash
git clone https://github.com/manu080797/llm2jev-research.git
cd llm2jev-research
uv sync --extra sglang
source .venv/bin/activate
python examples/sglang_inference.py --model-path /path/to/model
```

The example submits Choice, Score, and Noul questions and prints the response as JSON.
Replace `/path/to/model` with a local Hugging Face-compatible causal language model directory.

## 📦 Installation

See [Installation](docs/installation.md) for environment requirements, SGLang and Transformers dependencies, and uv or pip installation.

## 📖 Getting Started

See the [Usage guide](docs/usage.md) for complete examples:

- [SGLang Python API](docs/usage.md#sglang-python-api)
- [Transformers backend](docs/usage.md#transformers-backend)
- [System One HTTP API](docs/usage.md#system-one-http-api)
- [Choosing between `staged` and `all`](docs/usage.md#choosing-a-mode)
- [Multimodal inputs](docs/multimodal.md)

<a id="demos"></a>

## 🎮 Demos

<table>
  <tr>
    <td align="center" valign="middle" width="67%"><img src="assets/web-demo.gif" alt="LLM2Jev web demo" width="100%"></td>
    <td align="center" valign="middle" width="33%"><img src="assets/snake.gif" alt="LLM2Jev Snake demo" width="100%"></td>
  </tr>
  <tr>
    <td align="center"><a href="demos/web/README.md"><strong>Web demo</strong></a></td>
    <td align="center"><a href="demos/snake.py"><strong>Snake demo</strong></a></td>
  </tr>
  <tr>
    <td align="center" valign="middle"><video src="assets/mujoco.mp4" controls width="100%"></video><br><a href="demos/pick_place/README.md"><strong>MuJoCo pick-and-place demo</strong></a></td>
    <td></td>
  </tr>
</table>

## 📊 Existing Baseline Benchmarks

See [Performance benchmarks](docs/shared-prefix-benchmarks.md) for the upstream Qwen3-1.7B / RTX 5090 measurements, test conditions, and comparison of `staged` and `all` across cold and warm caches. Gains depend on input length, candidate count, and cache state. These are baseline runtime measurements, not evidence that one research scoring strategy is preferred.

## 🗺️ Research Roadmap

The authoritative task/status tracker is [issue #1](https://github.com/manu080797/llm2jev-research/issues/1). Architectural rationale and phase definitions live in [docs/research-design.md](docs/research-design.md).

The research sequence is:

1. establish and record the existing LLM2Jev baseline;
2. separate scoring strategy from inference backend while preserving binary-scoring behavior;
3. add a generic llama.cpp/GGUF CPU backend;
4. implement and evaluate full candidate-continuation likelihood;
5. integrate and benchmark BitNet through the generic backend interface;
6. build reproducible quality, robustness, uncertainty, and performance evaluation;
7. evaluate label-token and masked/diffusion scoring as additional experiments.

## 🧪 Tests

```bash
python -m unittest discover -s tests -v
```

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE).
