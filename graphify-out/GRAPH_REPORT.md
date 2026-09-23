# Graph Report - llm2jev-research  (2026-09-23)

## Corpus Check
- 65 files · ~204,069 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .css 1, .lock 1)

## Summary
- 618 nodes · 1414 edges · 30 communities (26 shown, 4 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 272 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e7b2331d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- JevRequest
- sglang_server.py
- Usage
- SGLangBackend
- llm2jev/__init__.py
- BinaryQuestion
- prepare_score_batches
- fetch_panda.py
- mujoco_demo.py
- app.js
- ServerArgumentTests
- JevResponse
- ImageBackendTests
- TransformersBackend
- BinaryBackendOutput
- utils/__init__.py
- llm2jev
- Decisions
- .__init__
- Repository Guidelines
- 🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference
- FakeTokenizer
- README.md
- From Jev Request to LLM Request
- LLM2Jev Pick & Place Arm Demo
- Shared prefixes: reuse context across multiple decisions
- Using multimodal data
- normalize_l1
- BinaryBackend
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
- `Baseline sandbox-safe run` --references--> `ImageBackendTests`  [INFERRED]
  docs/testing.md → tests/test_multimodal.py

## Import Cycles
- None detected.

## Communities (30 total, 4 thin omitted)

### Community 0 - "JevRequest"
Cohesion: 0.06
Nodes (38): LLM2Jev Web Demo, How do LLM requests and Jev requests differ?, main(), main(), main(), Question, Choice, Noul (+30 more)

### Community 1 - "sglang_server.py"
Cohesion: 0.10
Nodes (34): collections_abc, dataclasses, math, Normalizer, openai_types_chat, pathlib, Plan complete-candidate submissions; KV storage belongs to the engine., Shared text/image request preparation and zero-generation SGLang scoring. (+26 more)

### Community 2 - "Usage"
Cohesion: 0.29
Nodes (3): Input and output token counts, when reported by the model backend., Usage, UsageTests

### Community 3 - "SGLangBackend"
Cohesion: 0.22
Nodes (3): Prefill-only binary scorer using SGLang's native scoring and prefix cache., SGLangBackend, SGLangBackendTests

### Community 4 - "llm2jev/__init__.py"
Cohesion: 0.06
Nodes (23): argparse, base64, contextlib, copy, Score image evidence with Transformers or SGLang, without decoding., Evaluate a Jev request with a local SGLang engine., Run a mixed LLM2Jev request with a local Transformers model., io (+15 more)

### Community 5 - "BinaryQuestion"
Cohesion: 0.11
Nodes (12): Candidate, BinaryQuestion, A model-independent yes/no task compiled from a Jev question., append_content(), ChatPrompt, JSONContent, Render one binary question for a model backend., Serialize prompt content deterministically while keeping strings readable. (+4 more)

### Community 6 - "prepare_score_batches"
Cohesion: 0.14
Nodes (9): SimpleNamespace, Seed shared token paths before submitting their remaining branches. Each index…, staged_batches(), prepare_score_batches(), Any, ChatPrompt, PrefixPlanTests, GenerateReqInput (+1 more)

### Community 7 - "fetch_panda.py"
Cohesion: 0.06
Nodes (26): concurrent_futures, fetch(), git_sha(), main(), download(), Fetch the pinned Apache-2.0 Panda assets used by the MuJoCo demo., Client, main() (+18 more)

### Community 8 - "mujoco_demo.py"
Cohesion: 0.12
Nodes (14): action_criteria(), direction(), JevClient, main(), PandaPickPlace, Path, One-stage LLM2Jev control of a physical Panda pick-and-place scene., relation() (+6 more)

### Community 9 - "app.js"
Cohesion: 0.15
Nodes (19): addCriteriaRow(), addQuestion(), collectRequest(), connectionStatus, defaults, input(), parseState(), probabilityRows() (+11 more)

### Community 10 - "ServerArgumentTests"
Cohesion: 0.22
Nodes (7): main(), _parse_submission_args(), Any, Register the System One endpoint on SGLang's existing FastAPI app., register_systemone_route(), _validate_server_args(), ServerArgumentTests

### Community 11 - "JevResponse"
Cohesion: 0.06
Nodes (20): K, ChoiceAnswer, NoulAnswer, A selected choice and the probability of every available choice., A probability-weighted score and its ordered rubric., The probability that the answer is yes or the statement is true., ScoreAnswer, _format_json() (+12 more)

### Community 12 - "ImageBackendTests"
Cohesion: 0.12
Nodes (15): Baseline sandbox-safe run, Compile and package-build baseline, Current sandbox-safe command, External experiments when needed, External real-model integration, Important finding, Inherited suite inventory, Sandbox-safe (+7 more)

### Community 13 - "TransformersBackend"
Cohesion: 0.20
Nodes (5): Any, ChatPrompt, Path, Prefill-only binary scorer backed by a Transformers causal language model., TransformersBackend

### Community 14 - "BinaryBackendOutput"
Cohesion: 0.25
Nodes (5): BinaryBackendOutput, Ordered yes probabilities and usage returned by a binary backend., ChatPrompt, FailingBackend, ChatPrompt

### Community 17 - "Decisions"
Cohesion: 0.07
Nodes (26): Architecture direction, Change protocol, D001 — Fork LLM2Jev as the application base, D002 — No training is required, D003 — Separate scoring strategy from inference backend, D004 — Add llama.cpp/GGUF as the first new backend, D005 — Full candidate continuation likelihood is an experimental scoring strategy, D006 — Preserve independent binary scoring as baseline (+18 more)

### Community 18 - ".__init__"
Cohesion: 0.33
Nodes (3): Any, Path, Shut down this backend's SGLang engine and release GPU resources.

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

### Community 25 - "Shared prefixes: reuse context across multiple decisions"
Cohesion: 0.50
Nodes (4): How does staging help the first request?, Outputs and cache behavior, Shared prefixes: reuse context across multiple decisions, Why is the same context processed more than once?

### Community 26 - "Using multimodal data"
Cohesion: 0.29
Nodes (7): Building a request, Choosing where to place images, HTTP API calls, SGLang backend, Supported image sources, Transformers backend, Using multimodal data

### Community 27 - "normalize_l1"
Cohesion: 0.43
Nodes (3): normalize_l1(), Normalize non-negative values to sum to one, or return a uniform distribution., NormalizeL1Tests

### Community 28 - "BinaryBackend"
Cohesion: 0.33
Nodes (5): BinaryBackend, ChatPrompt, Protocol, Batch scorer that returns one P(yes) for each rendered prompt., Score prompts in input order without generating text.

### Community 29 - "Usage guide"
Cohesion: 0.40
Nodes (5): Choosing a mode, SGLang Python API, System One HTTP API, Transformers Backend, Usage guide

## Knowledge Gaps
- **85 isolated node(s):** `questionsElement`, `template`, `submitButton`, `validationMessage`, `connectionStatus` (+80 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 197 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SGLangBackend` connect `SGLangBackend` to `JevRequest`, `sglang_server.py`, `Usage`, `llm2jev/__init__.py`, `TransformersBackend`, `BinaryBackendOutput`, `.__init__`, `README.md`, `Shared prefixes: reuse context across multiple decisions`?**
  _High betweenness centrality (0.123) - this node is a cross-community bridge._
- **Why does `JevRequest` connect `JevRequest` to `sglang_server.py`, `llm2jev/__init__.py`, `Usage guide`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Why does `Shared prefixes: reuse context across multiple decisions` connect `Shared prefixes: reuse context across multiple decisions` to `SGLangBackend`, `TransformersBackend`, `README.md`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 52 inferred relationships involving `JevRequest` (e.g. with `SGLang Python API` and `main()`) actually correct?**
  _`JevRequest` has 52 INFERRED edges - model-reasoned connections that need verification._
- **Are the 34 inferred relationships involving `Noul` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Noul` has 34 INFERRED edges - model-reasoned connections that need verification._
- **Are the 30 inferred relationships involving `Choice` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Choice` has 30 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `compile_binary_questions()` (e.g. with `Choice` and `Noul`) actually correct?**
  _`compile_binary_questions()` has 27 INFERRED edges - model-reasoned connections that need verification._