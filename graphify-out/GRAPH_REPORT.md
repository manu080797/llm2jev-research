# Graph Report - llm2jev-research  (2026-09-23)

## Corpus Check
- 68 files · ~205,935 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .css 1, .lock 1)

## Summary
- 651 nodes · 1510 edges · 24 communities (20 shown, 4 thin omitted)
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 303 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `31f42f6d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- JevRequest
- assembler.py
- JevResponse
- Usage
- llm2jev/__init__.py
- BinaryQuestion
- snake.py
- fetch_panda.py
- mujoco_demo.py
- app.js
- sglang_server.py
- README.md
- ImageBackendTests
- From Jev Request to LLM Request
- LLM2Jev Pick & Place Arm Demo
- utils/__init__.py
- llm2jev
- Decisions
- Using multimodal data
- Repository Guidelines
- 🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference
- FakeTokenizer
- Usage guide
- Performance profiling methodology

## God Nodes (most connected - your core abstractions)
1. `JevRequest` - 70 edges
2. `Noul` - 47 edges
3. `Choice` - 42 edges
4. `compile_binary_questions()` - 38 edges
5. `Usage` - 33 edges
6. `assemble_response()` - 31 edges
7. `SGLangBackend` - 29 edges
8. `JevResponse` - 29 edges
9. `Score` - 28 edges
10. `LLM2Jev` - 26 edges

## Surprising Connections (you probably didn't know these)
- `Shared prefixes: performance benchmarks` --references--> `SGLangBackend`  [INFERRED]
  docs/shared-prefix-benchmarks.md → src/llm2jev/backend/sglang/backend.py
- `SGLang Python API` --references--> `JevRequest`  [INFERRED]
  docs/usage.md → src/llm2jev/core/request.py
- `Coding Style & Naming Conventions` --references--> `ScoringStrategy`  [INFERRED]
  AGENTS.md → src/llm2jev/inference/scoring.py
- `How do LLM requests and Jev requests differ?` --references--> `Choice`  [INFERRED]
  docs/request-to-model.md → src/llm2jev/core/questions.py
- `How do LLM requests and Jev requests differ?` --references--> `Score`  [INFERRED]
  docs/request-to-model.md → src/llm2jev/core/questions.py

## Import Cycles
- None detected.

## Communities (24 total, 4 thin omitted)

### Community 0 - "JevRequest"
Cohesion: 0.05
Nodes (36): LLM2Jev Web Demo, main(), main(), Evaluate a Jev request with a local SGLang engine., main(), Run a mixed LLM2Jev request with a local Transformers model., Normalizer, Choice (+28 more)

### Community 1 - "assembler.py"
Cohesion: 0.07
Nodes (47): collections_abc, dataclasses, D003 — Separate scoring strategy from inference backend, Phase 1 — Scoring abstraction, math, openai_types_chat, pathlib, 🔬 Research Fork (+39 more)

### Community 2 - "JevResponse"
Cohesion: 0.05
Nodes (22): K, ChoiceAnswer, NoulAnswer, A selected choice and the probability of every available choice., A probability-weighted score and its ordered rubric., The probability that the answer is yes or the statement is true., ScoreAnswer, _format_json() (+14 more)

### Community 3 - "Usage"
Cohesion: 0.06
Nodes (19): How does staging help the first request?, Outputs and cache behavior, Shared prefixes: reuse context across multiple decisions, Why is the same context processed more than once?, Any, ChatPrompt, Path, Prefill-only binary scorer using SGLang's native scoring and prefix cache. (+11 more)

### Community 4 - "llm2jev/__init__.py"
Cohesion: 0.08
Nodes (18): base64, contextlib, copy, io, Any, score_output(), tempfile, BinaryBackendOutputTests (+10 more)

### Community 5 - "BinaryQuestion"
Cohesion: 0.10
Nodes (15): Candidate, is_multimodal(), Any, BinaryQuestion, A model-independent yes/no task compiled from a Jev question., append_content(), ChatPrompt, JSONContent (+7 more)

### Community 6 - "snake.py"
Cohesion: 0.09
Nodes (13): Client, main(), Play Snake with one LLM2Jev Choice question per tick. Inspired by…, Persistent System One client; avoids reconnecting on every tick., _save_gif(), Snake, http_client, random (+5 more)

### Community 7 - "fetch_panda.py"
Cohesion: 0.10
Nodes (17): concurrent_futures, fetch(), git_sha(), main(), download(), Fetch the pinned Apache-2.0 Panda assets used by the MuJoCo demo., DemoHandler, Serve the web demo and proxy requests to an LLM2Jev HTTP server. (+9 more)

### Community 8 - "mujoco_demo.py"
Cohesion: 0.11
Nodes (15): argparse, action_criteria(), direction(), JevClient, main(), PandaPickPlace, Path, One-stage LLM2Jev control of a physical Panda pick-and-place scene. (+7 more)

### Community 9 - "app.js"
Cohesion: 0.15
Nodes (19): addCriteriaRow(), addQuestion(), collectRequest(), connectionStatus, defaults, input(), parseState(), probabilityRows() (+11 more)

### Community 10 - "sglang_server.py"
Cohesion: 0.08
Nodes (22): Question, SimpleNamespace, prepare_score_batches(), ChatPrompt, Any, _single_token_id(), _evaluate_request(), main() (+14 more)

### Community 12 - "ImageBackendTests"
Cohesion: 0.11
Nodes (16): Baseline sandbox-safe run, Compile and package-build baseline, Current sandbox-safe command, External experiments when needed, External real-model integration, Important finding, Inherited suite inventory, Performance profiling suite (+8 more)

### Community 13 - "From Jev Request to LLM Request"
Cohesion: 0.20
Nodes (10): Confidence is also calculated in code, From Jev Request to LLM Request, How do LLM requests and Jev requests differ?, How does an LLM produce the same JSON output?, LLM2Jev: first construct independent yes/no judgments, More input tokens: could this make inference slower?, Then calculate probabilities from yes/no logits, Turning candidate scores into final answers (+2 more)

### Community 14 - "LLM2Jev Pick & Place Arm Demo"
Cohesion: 0.25
Nodes (7): Attribution, Demo video, Dependencies, Fetch the Panda assets, LLM2Jev Pick & Place Arm Demo, Run the MuJoCo version, Start the local service

### Community 17 - "Decisions"
Cohesion: 0.08
Nodes (25): Architecture direction, Change protocol, D001 — Fork LLM2Jev as the application base, D002 — No training is required, D004 — Add llama.cpp/GGUF as the first new backend, D005 — Full candidate continuation likelihood is an experimental scoring strategy, D006 — Preserve independent binary scoring as baseline, D007 — Benchmark before choosing a preferred scorer/model (+17 more)

### Community 18 - "Using multimodal data"
Cohesion: 0.29
Nodes (7): Building a request, Choosing where to place images, HTTP API calls, SGLang backend, Supported image sources, Transformers backend, Using multimodal data

### Community 19 - "Repository Guidelines"
Cohesion: 0.13
Nodes (14): Architecture Constraints, Build, Test, and Development Commands, Coding Style & Naming Conventions, Commit & Pull Request Guidelines, Current Research Sequence, Graphify Knowledge Graph, Maintaining AGENTS.md, Profiling Guidelines (+6 more)

### Community 20 - "🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference"
Cohesion: 0.18
Nodes (11): ✅ Current LLM2Jev Baseline, 🎮 Demos, 📊 Existing Baseline Benchmarks, 📖 Getting Started, 📦 Installation, 📄 License, 🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference, 🚀 Quick Start (+3 more)

### Community 22 - "Usage guide"
Cohesion: 0.40
Nodes (5): Choosing a mode, SGLang Python API, System One HTTP API, Transformers Backend, Usage guide

### Community 23 - "Performance profiling methodology"
Cohesion: 0.20
Nodes (9): Cache and prefix-reuse profiling, Common workload metrics, CPU profiling, Experiment matrix, GPU profiling, Interpretation, MoE-specific profiling, Performance profiling methodology (+1 more)

## Knowledge Gaps
- **92 isolated node(s):** `questionsElement`, `template`, `submitButton`, `validationMessage`, `connectionStatus` (+87 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 211 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `JevRequest` connect `JevRequest` to `assembler.py`, `JevResponse`, `Usage`, `llm2jev/__init__.py`, `sglang_server.py`, `Usage guide`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **Why does `ScoringStrategy` connect `assembler.py` to `JevRequest`, `JevResponse`, `Repository Guidelines`, `llm2jev/__init__.py`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Why does `SGLangBackend` connect `Usage` to `JevRequest`, `assembler.py`, `README.md`, `llm2jev/__init__.py`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `JevRequest` (e.g. with `SGLang Python API` and `main()`) actually correct?**
  _`JevRequest` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Are the 36 inferred relationships involving `Noul` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Noul` has 36 INFERRED edges - model-reasoned connections that need verification._
- **Are the 31 inferred relationships involving `Choice` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Choice` has 31 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `compile_binary_questions()` (e.g. with `Choice` and `Noul`) actually correct?**
  _`compile_binary_questions()` has 27 INFERRED edges - model-reasoned connections that need verification._