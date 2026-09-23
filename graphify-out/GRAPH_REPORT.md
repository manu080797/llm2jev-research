# Graph Report - llm2jev-research  (2026-09-23)

## Corpus Check
- 64 files · ~202,788 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .css 1, .lock 1)

## Summary
- 606 nodes · 1402 edges · 30 communities (23 shown, 7 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 271 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `31b87a87`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- JevRequest
- sglang_server.py
- test_response.py
- SGLangBackend
- test_multimodal.py
- BinaryQuestion
- snake.py
- fetch_panda.py
- mujoco_demo.py
- app.js
- ServerArgumentTests
- validate_probabilities
- ImageBackendTests
- FakeTokenizer
- BinaryBackendOutputTests
- utils/__init__.py
- llm2jev
- Research architecture and decision log
- is_json_content
- Repository Guidelines
- 🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference
- llm2jev/__init__.py
- README.md
- From Jev Request to LLM Request
- LLM2Jev Pick & Place Arm Demo
- argparse
- Using multimodal data
- normalize_l1
- test_questions.py
- Usage guide

## God Nodes (most connected - your core abstractions)
1. `JevRequest` - 64 edges
2. `Noul` - 45 edges
3. `Choice` - 41 edges
4. `compile_binary_questions()` - 38 edges
5. `assemble_response()` - 31 edges
6. `Usage` - 30 edges
7. `SGLangBackend` - 29 edges
8. `Score` - 28 edges
9. `JevResponse` - 23 edges
10. `BinaryQuestion` - 22 edges

## Surprising Connections (you probably didn't know these)
- `Shared prefixes: performance benchmarks` --references--> `SGLangBackend`  [INFERRED]
  docs/shared-prefix-benchmarks.md → src/llm2jev/backend/sglang/backend.py
- `SGLang Python API` --references--> `JevRequest`  [INFERRED]
  docs/usage.md → src/llm2jev/core/request.py
- `Shared prefixes: reuse context across multiple decisions` --references--> `SGLangBackend`  [INFERRED]
  docs/shared-prefix-cache.md → src/llm2jev/backend/sglang/backend.py
- `Shared prefixes: reuse context across multiple decisions` --references--> `TransformersBackend`  [INFERRED]
  docs/shared-prefix-cache.md → src/llm2jev/backend/transformers/backend.py
- `LLM2Jev Web Demo` --references--> `Choice`  [INFERRED]
  demos/web/README.md → src/llm2jev/core/questions.py

## Import Cycles
- None detected.

## Communities (30 total, 7 thin omitted)

### Community 0 - "JevRequest"
Cohesion: 0.06
Nodes (37): LLM2Jev Web Demo, How do LLM requests and Jev requests differ?, main(), main(), main(), Question, Choice, Noul (+29 more)

### Community 1 - "sglang_server.py"
Cohesion: 0.09
Nodes (31): collections_abc, dataclasses, math, openai_types_chat, pathlib, Plan complete-candidate submissions; KV storage belongs to the engine., Shared text/image request preparation and zero-generation SGLang scoring., _apply_chat_template() (+23 more)

### Community 2 - "test_response.py"
Cohesion: 0.15
Nodes (4): ChoiceAnswerTests, NoulAnswerTests, ProbabilityValidationTests, UsageTests

### Community 3 - "SGLangBackend"
Cohesion: 0.06
Nodes (23): How does staging help the first request?, Outputs and cache behavior, Shared prefixes: reuse context across multiple decisions, Why is the same context processed more than once?, BinaryBackend, BinaryBackendOutput, ChatPrompt, Protocol (+15 more)

### Community 4 - "test_multimodal.py"
Cohesion: 0.08
Nodes (22): base64, contextlib, copy, io, SimpleNamespace, prepare_score_batches(), Any, ChatPrompt (+14 more)

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
Cohesion: 0.13
Nodes (13): action_criteria(), direction(), JevClient, main(), PandaPickPlace, Path, One-stage LLM2Jev control of a physical Panda pick-and-place scene., relation() (+5 more)

### Community 9 - "app.js"
Cohesion: 0.15
Nodes (19): addCriteriaRow(), addQuestion(), collectRequest(), connectionStatus, defaults, input(), parseState(), probabilityRows() (+11 more)

### Community 10 - "ServerArgumentTests"
Cohesion: 0.22
Nodes (7): main(), _parse_submission_args(), Any, Register the System One endpoint on SGLang's existing FastAPI app., register_systemone_route(), _validate_server_args(), ServerArgumentTests

### Community 11 - "validate_probabilities"
Cohesion: 0.15
Nodes (10): K, Normalizer, _normalize(), copy_probability_distribution(), Validate and return one finite probability., Validate a non-empty sequence of probabilities., Copy and validate a non-empty probability distribution., validate_probabilities() (+2 more)

### Community 12 - "ImageBackendTests"
Cohesion: 0.18
Nodes (8): Any, ChatPrompt, has_images(), load_transformers_images(), prepare_image_prompts(), Any, ChatPrompt, ImageBackendTests

### Community 17 - "Research architecture and decision log"
Cohesion: 0.08
Nodes (25): Architecture direction, Change protocol, D001 — Fork LLM2Jev as the application base, D002 — No training is required, D003 — Separate scoring strategy from inference backend, D004 — Add llama.cpp/GGUF as the first new backend, D005 — Full candidate continuation likelihood is an experimental scoring strategy, D006 — Preserve independent binary scoring as baseline (+17 more)

### Community 18 - "is_json_content"
Cohesion: 0.17
Nodes (8): JSONContent, _validate_instructions(), copy_json_content(), is_json_content(), is_json_value(), Recursively copy JSON containers while preserving scalar values., T, JsonUtilsTests

### Community 19 - "Repository Guidelines"
Cohesion: 0.14
Nodes (13): Architecture Constraints, Build, Test, and Development Commands, Coding Style & Naming Conventions, Commit & Pull Request Guidelines, Current Research Sequence, Graphify Knowledge Graph, Maintaining AGENTS.md, Project Structure & Module Organization (+5 more)

### Community 20 - "🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference"
Cohesion: 0.17
Nodes (12): ✅ Current LLM2Jev Baseline, 🎮 Demos, 📊 Existing Baseline Benchmarks, 📖 Getting Started, 📦 Installation, 📄 License, 🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference, 🚀 Quick Start (+4 more)

### Community 23 - "From Jev Request to LLM Request"
Cohesion: 0.22
Nodes (9): Confidence is also calculated in code, From Jev Request to LLM Request, How does an LLM produce the same JSON output?, LLM2Jev: first construct independent yes/no judgments, More input tokens: could this make inference slower?, Then calculate probabilities from yes/no logits, Turning candidate scores into final answers, What does a yes/no input look like? (+1 more)

### Community 24 - "LLM2Jev Pick & Place Arm Demo"
Cohesion: 0.25
Nodes (7): Attribution, Demo video, Dependencies, Fetch the Panda assets, LLM2Jev Pick & Place Arm Demo, Run the MuJoCo version, Start the local service

### Community 25 - "argparse"
Cohesion: 0.29
Nodes (4): argparse, Score image evidence with Transformers or SGLang, without decoding., Evaluate a Jev request with a local SGLang engine., Run a mixed LLM2Jev request with a local Transformers model.

### Community 26 - "Using multimodal data"
Cohesion: 0.29
Nodes (7): Building a request, Choosing where to place images, HTTP API calls, SGLang backend, Supported image sources, Transformers backend, Using multimodal data

### Community 27 - "normalize_l1"
Cohesion: 0.43
Nodes (3): normalize_l1(), Normalize non-negative values to sum to one, or return a uniform distribution., NormalizeL1Tests

### Community 29 - "Usage guide"
Cohesion: 0.40
Nodes (5): Choosing a mode, SGLang Python API, System One HTTP API, Transformers Backend, Usage guide

## Knowledge Gaps
- **77 isolated node(s):** `questionsElement`, `template`, `submitButton`, `validationMessage`, `connectionStatus` (+72 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 188 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SGLangBackend` connect `SGLangBackend` to `JevRequest`, `sglang_server.py`, `llm2jev/__init__.py`, `README.md`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Why does `JevRequest` connect `JevRequest` to `sglang_server.py`, `is_json_content`, `llm2jev/__init__.py`, `Usage guide`?**
  _High betweenness centrality (0.097) - this node is a cross-community bridge._
- **Why does `Shared prefixes: reuse context across multiple decisions` connect `SGLangBackend` to `README.md`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Are the 52 inferred relationships involving `JevRequest` (e.g. with `SGLang Python API` and `main()`) actually correct?**
  _`JevRequest` has 52 INFERRED edges - model-reasoned connections that need verification._
- **Are the 34 inferred relationships involving `Noul` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Noul` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Are the 30 inferred relationships involving `Choice` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Choice` has 30 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `compile_binary_questions()` (e.g. with `Choice` and `Noul`) actually correct?**
  _`compile_binary_questions()` has 27 INFERRED edges - model-reasoned connections that need verification._