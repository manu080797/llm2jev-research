# Graph Report - llm2jev-research  (2026-09-23)

## Corpus Check
- 67 files · ~204,446 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .css 1, .lock 1)

## Summary
- 638 nodes · 1498 edges · 25 communities (21 shown, 4 thin omitted)
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 303 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2175d1cd`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- JevRequest
- sglang_server.py
- ChoiceAnswer
- Usage
- unittest
- BinaryQuestion
- staged_batches
- fetch_panda.py
- mujoco_demo.py
- app.js
- _parse_request
- README.md
- TransformersBackend
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
- Shared prefixes: reuse context across multiple decisions
- llm2jev/__init__.py

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
- `Shared prefixes: reuse context across multiple decisions` --references--> `SGLangBackend`  [INFERRED]
  docs/shared-prefix-cache.md → src/llm2jev/backend/sglang/backend.py
- `Shared prefixes: reuse context across multiple decisions` --references--> `TransformersBackend`  [INFERRED]
  docs/shared-prefix-cache.md → src/llm2jev/backend/transformers/backend.py

## Import Cycles
- None detected.

## Communities (25 total, 4 thin omitted)

### Community 0 - "JevRequest"
Cohesion: 0.06
Nodes (37): LLM2Jev Web Demo, How do LLM requests and Jev requests differ?, main(), main(), main(), Question, Choice, Noul (+29 more)

### Community 1 - "sglang_server.py"
Cohesion: 0.10
Nodes (33): base64, collections_abc, dataclasses, math, Normalizer, openai_types_chat, pathlib, prepare_score_batches() (+25 more)

### Community 2 - "ChoiceAnswer"
Cohesion: 0.07
Nodes (15): K, ChoiceAnswer, A selected choice and the probability of every available choice., A probability-weighted score and its ordered rubric., ScoreAnswer, copy_probability_distribution(), Validate and return one finite probability., Copy and validate a non-empty probability distribution. (+7 more)

### Community 3 - "Usage"
Cohesion: 0.06
Nodes (21): BinaryBackendOutput, ChatPrompt, Ordered yes probabilities and usage returned by a binary backend., Score prompts in input order without generating text., Any, ChatPrompt, Path, Prefill-only binary scorer using SGLang's native scoring and prefix cache. (+13 more)

### Community 4 - "unittest"
Cohesion: 0.08
Nodes (14): contextlib, copy, io, SimpleNamespace, sys, BinaryBackendOutputTests, FailingBackend, GenerateReqInput (+6 more)

### Community 5 - "BinaryQuestion"
Cohesion: 0.09
Nodes (15): Candidate, is_multimodal(), Any, BinaryQuestion, A model-independent yes/no task compiled from a Jev question., append_content(), ChatPrompt, JSONContent (+7 more)

### Community 6 - "staged_batches"
Cohesion: 0.26
Nodes (5): random, Plan complete-candidate submissions; KV storage belongs to the engine., Seed shared token paths before submitting their remaining branches. Each index…, staged_batches(), PrefixPlanTests

### Community 7 - "fetch_panda.py"
Cohesion: 0.11
Nodes (16): concurrent_futures, fetch(), git_sha(), main(), download(), Fetch the pinned Apache-2.0 Panda assets used by the MuJoCo demo., DemoHandler, Serve the web demo and proxy requests to an LLM2Jev HTTP server. (+8 more)

### Community 8 - "mujoco_demo.py"
Cohesion: 0.06
Nodes (26): argparse, action_criteria(), direction(), JevClient, main(), PandaPickPlace, Path, One-stage LLM2Jev control of a physical Panda pick-and-place scene. (+18 more)

### Community 9 - "app.js"
Cohesion: 0.15
Nodes (19): addCriteriaRow(), addQuestion(), collectRequest(), connectionStatus, defaults, input(), parseState(), probabilityRows() (+11 more)

### Community 10 - "_parse_request"
Cohesion: 0.15
Nodes (10): main(), _parse_request(), _parse_submission_args(), Any, Register the System One endpoint on SGLang's existing FastAPI app., register_systemone_route(), systemone(), _validate_server_args() (+2 more)

### Community 12 - "TransformersBackend"
Cohesion: 0.08
Nodes (21): Baseline sandbox-safe run, Compile and package-build baseline, Current sandbox-safe command, External experiments when needed, External real-model integration, Important finding, Inherited suite inventory, Sandbox-safe (+13 more)

### Community 13 - "From Jev Request to LLM Request"
Cohesion: 0.22
Nodes (9): Confidence is also calculated in code, From Jev Request to LLM Request, How does an LLM produce the same JSON output?, LLM2Jev: first construct independent yes/no judgments, More input tokens: could this make inference slower?, Then calculate probabilities from yes/no logits, Turning candidate scores into final answers, What does a yes/no input look like? (+1 more)

### Community 14 - "LLM2Jev Pick & Place Arm Demo"
Cohesion: 0.25
Nodes (7): Attribution, Demo video, Dependencies, Fetch the Panda assets, LLM2Jev Pick & Place Arm Demo, Run the MuJoCo version, Start the local service

### Community 17 - "Decisions"
Cohesion: 0.08
Nodes (24): Architecture direction, Change protocol, D001 — Fork LLM2Jev as the application base, D002 — No training is required, D004 — Add llama.cpp/GGUF as the first new backend, D005 — Full candidate continuation likelihood is an experimental scoring strategy, D006 — Preserve independent binary scoring as baseline, D007 — Benchmark before choosing a preferred scorer/model (+16 more)

### Community 18 - "Using multimodal data"
Cohesion: 0.29
Nodes (7): Building a request, Choosing where to place images, HTTP API calls, SGLang backend, Supported image sources, Transformers backend, Using multimodal data

### Community 19 - "Repository Guidelines"
Cohesion: 0.14
Nodes (13): Architecture Constraints, Build, Test, and Development Commands, Coding Style & Naming Conventions, Commit & Pull Request Guidelines, Current Research Sequence, Graphify Knowledge Graph, Maintaining AGENTS.md, Project Structure & Module Organization (+5 more)

### Community 20 - "🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference"
Cohesion: 0.18
Nodes (11): ✅ Current LLM2Jev Baseline, 🎮 Demos, 📊 Existing Baseline Benchmarks, 📖 Getting Started, 📦 Installation, 📄 License, 🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference, 🚀 Quick Start (+3 more)

### Community 22 - "Usage guide"
Cohesion: 0.40
Nodes (5): Choosing a mode, SGLang Python API, System One HTTP API, Transformers Backend, Usage guide

### Community 23 - "Shared prefixes: reuse context across multiple decisions"
Cohesion: 0.50
Nodes (4): How does staging help the first request?, Outputs and cache behavior, Shared prefixes: reuse context across multiple decisions, Why is the same context processed more than once?

### Community 28 - "llm2jev/__init__.py"
Cohesion: 0.10
Nodes (23): D003 — Separate scoring strategy from inference backend, Phase 1 — Scoring abstraction, 🔬 Research Fork, BinaryBackend, Protocol, Batch scorer that returns one P(yes) for each rendered prompt., _format_json(), JevResponse (+15 more)

## Knowledge Gaps
- **81 isolated node(s):** `questionsElement`, `template`, `submitButton`, `validationMessage`, `connectionStatus` (+76 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 199 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `JevRequest` connect `JevRequest` to `sglang_server.py`, `Usage`, `_parse_request`, `Usage guide`, `llm2jev/__init__.py`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._
- **Why does `ScoringStrategy` connect `llm2jev/__init__.py` to `JevRequest`, `Repository Guidelines`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Why does `SGLangBackend` connect `Usage` to `JevRequest`, `sglang_server.py`, `README.md`, `TransformersBackend`, `Shared prefixes: reuse context across multiple decisions`, `llm2jev/__init__.py`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `JevRequest` (e.g. with `SGLang Python API` and `main()`) actually correct?**
  _`JevRequest` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Are the 36 inferred relationships involving `Noul` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Noul` has 36 INFERRED edges - model-reasoned connections that need verification._
- **Are the 31 inferred relationships involving `Choice` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Choice` has 31 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `compile_binary_questions()` (e.g. with `Choice` and `Noul`) actually correct?**
  _`compile_binary_questions()` has 27 INFERRED edges - model-reasoned connections that need verification._