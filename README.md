  <p align="center">
    <img src="assets/llm2jev-banner.jpeg" alt="LLM2Jev" width="100%">
  </p>

<div align="center">

# 🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference
<br/>

[![Python](https://img.shields.io/badge/python-3.12%2B-blue?style=flat-square)](pyproject.toml)
[![License](https://img.shields.io/badge/license-Apache--2.0-green?style=flat-square)](LICENSE)
[![Jev API](https://img.shields.io/badge/API-%2Fv1%2Fsystemone%20compatible-orange?style=flat-square)](docs/usage.md)

**Research fork of LLM2Jev for zero-training, model-agnostic structured decision inference across scoring strategies and local runtimes, with CPU/GGUF execution as a first-class target.**

</div>

> This repository is a research fork of [Yinsongxu/LLM2Jev](https://github.com/Yinsongxu/LLM2Jev). LLM2Jev is an independent open-source project and is not affiliated with or endorsed by Jev or TypeSafe.

## 🔬 Research Fork

The upstream independent yes/no candidate scorer remains the compatibility baseline. This fork is extending the architecture so **scoring strategy** and **model backend** are independent and can be compared under the same Jev-style API.

Planned research includes:

- a generic `ScoringStrategy` layer retaining the current binary yes/no method while adding label-token and full candidate-continuation likelihood experiments;
- a generic `ModelBackend` boundary spanning the existing SGLang/Transformers implementations and a planned llama.cpp/GGUF backend;
- CPU-oriented evaluation, including BitNet without making the semantic API BitNet-specific;
- shared-prefix/KV reuse across scoring methods;
- reproducible evaluation of decision quality, robustness, uncertainty diagnostics, latency, throughput, memory, and CPU efficiency;
- later masked/diffusion scoring experiments behind an appropriate backend primitive.

No fine-tuning or project-specific training data is required by the baseline design. Competing scorers and models are treated as experiments until comparative evidence supports a default.

See **[Research design and decision log](docs/research-design.md)** for the architecture, accepted decisions, methodology, and open questions. Implementation progress is tracked in **[issue #1](https://github.com/manu080797/llm2jev-research/issues/1)**.


## 📰 News

- **September 23** - **[MuJoCo pick-and-place demo](demos/pick_place/README.md):** added LLM2Jev control of a simulated Panda arm with per-step decision.
- **September 22** - **[Multimodal inputs](docs/multimodal.md):** added text-and-image requests for SGLang, Transformers, and the System One HTTP API.
- **September 21** - **[Web and Snake demos](#demos):** added interactive examples for composing mixed questions and model-driven decisions.
- **September 21** - **Prefix reuse on cold requests:** added staged candidate submission for reusing SGLang's Radix Cache, with [architecture](docs/request-to-model.md), [usage](docs/shared-prefix-cache.md), and [benchmark](docs/shared-prefix-benchmarks.md) documentation.
- **September 20** - **SGLang and System One API:** added the SGLang scoring backend and a compatible [`POST /v1/systemone`](docs/usage.md#system-one-http-api) endpoint.

## ✨ Key Features

- **Prefill only:** compute probabilities from logits during prefill and assemble results directly, without token-by-token decoding.
- **Multimodal inputs:** combine text and images in `state` or `instructions`, with support for both SGLang and Transformers.
- **Order-independent options:** evaluate each Choice candidate independently, so reordering options does not introduce a positional preference or change their scores.
- **Prefix reuse on cold requests:** stage candidate submissions to reuse SGLang's Radix Cache within a single request, including a first request with no relevant cached prefix.

Candidates share `state`, and candidates for the same question also share its `instructions`. LLM2Jev first scores a real `criteria` candidate to establish the prefix cache, then submits candidates that can reuse it. Each candidate is scored once, reducing repeated computation for long inputs with many candidates.

![Staged candidate scoring reuses state and question instructions through SGLang Radix Cache.](assets/shared-prefix-stages.svg)

Learn how it works: [From Jev Request to LLM Request](docs/request-to-model.md) → [Shared-prefix design](docs/shared-prefix-cache.md).

## 🚀 Quick Start

On Linux with a supported NVIDIA GPU, run a local model through SGLang:

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


## 📊 Benchmarks

See [Performance benchmarks](docs/shared-prefix-benchmarks.md) for the Qwen3-1.7B / RTX 5090 measurements, test conditions, and comparison of `staged` and `all` across cold and warm caches. Gains depend on input length, candidate count, and cache state.

## 🗺️ Research Roadmap

The detailed, actively maintained roadmap is in [issue #1](https://github.com/manu080797/llm2jev-research/issues/1), with architectural decisions in [docs/research-design.md](docs/research-design.md).

Current phases are:

- [ ] Establish and record the existing LLM2Jev baseline.
- [ ] Separate scoring strategy from inference backend while preserving binary-scoring behavior.
- [ ] Add a generic llama.cpp/GGUF CPU backend.
- [ ] Implement and evaluate full candidate continuation likelihood.
- [ ] Integrate and benchmark BitNet through the generic backend interface.
- [ ] Build reproducible quality, robustness, calibration-diagnostic, and performance evaluation.
- [ ] Evaluate label-token and masked/diffusion scoring as additional experiments.

## 🧪 Tests

```bash
python -m unittest discover -s tests -v
```

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE).
