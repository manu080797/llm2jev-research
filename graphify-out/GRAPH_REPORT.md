# Graph Report - llm2jev-research  (2026-09-24)

## Corpus Check
- 69 files · ~206,869 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .css 1, .lock 1)

## Summary
- 662 nodes · 1520 edges · 22 communities (19 shown, 3 thin omitted)
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 303 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `fc4019c7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- JevRequest
- sglang_server.py
- JevResponse
- Usage
- llm2jev/__init__.py
- BinaryQuestion
- snake.py
- mujoco_demo.py
- BinaryScorer
- app.js
- _parse_request
- Comparative evaluation plan
- ImageBackendTests
- Research architecture and decision log
- Implementation phases
- utils/__init__.py
- llm2jev
- Decisions
- .score
- Repository Guidelines
- 🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference
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
- `D003 — Separate scoring strategy from inference backend` --references--> `LLM2Jev`  [INFERRED]
  docs/research-design.md → src/llm2jev/inference/converter.py
- `🔬 Research Fork` --references--> `LLM2Jev`  [INFERRED]
  README.md → src/llm2jev/inference/converter.py
- `Coding Style & Naming Conventions` --references--> `ScoringStrategy`  [INFERRED]
  AGENTS.md → src/llm2jev/inference/scoring.py

## Import Cycles
- None detected.

## Communities (22 total, 3 thin omitted)

### Community 0 - "JevRequest"
Cohesion: 0.05
Nodes (41): LLM2Jev Web Demo, How do LLM requests and Jev requests differ?, main(), main(), main(), Normalizer, Question, Choice (+33 more)

### Community 1 - "sglang_server.py"
Cohesion: 0.08
Nodes (39): base64, collections_abc, copy, dataclasses, math, openai_types_chat, pathlib, SimpleNamespace (+31 more)

### Community 2 - "JevResponse"
Cohesion: 0.06
Nodes (21): K, ChoiceAnswer, NoulAnswer, A selected choice and the probability of every available choice., A probability-weighted score and its ordered rubric., The probability that the answer is yes or the statement is true., ScoreAnswer, _format_json() (+13 more)

### Community 3 - "Usage"
Cohesion: 0.05
Nodes (28): How does staging help the first request?, Outputs and cache behavior, Shared prefixes: reuse context across multiple decisions, Why is the same context processed more than once?, BinaryBackendOutput, Ordered yes probabilities and usage returned by a binary backend., Any, ChatPrompt (+20 more)

### Community 4 - "llm2jev/__init__.py"
Cohesion: 0.06
Nodes (15): argparse, contextlib, Score image evidence with Transformers or SGLang, without decoding., Evaluate a Jev request with a local SGLang engine., Run a mixed LLM2Jev request with a local Transformers model., io, normalize_l1(), Normalize non-negative values to sum to one, or return a uniform distribution. (+7 more)

### Community 5 - "BinaryQuestion"
Cohesion: 0.10
Nodes (15): Candidate, is_multimodal(), Any, BinaryQuestion, A model-independent yes/no task compiled from a Jev question., append_content(), ChatPrompt, JSONContent (+7 more)

### Community 6 - "snake.py"
Cohesion: 0.09
Nodes (12): Client, main(), Play Snake with one LLM2Jev Choice question per tick. Inspired by…, Persistent System One client; avoids reconnecting on every tick., _save_gif(), Snake, http_client, random (+4 more)

### Community 7 - "mujoco_demo.py"
Cohesion: 0.06
Nodes (31): concurrent_futures, fetch(), git_sha(), main(), download(), Fetch the pinned Apache-2.0 Panda assets used by the MuJoCo demo., action_criteria(), direction() (+23 more)

### Community 8 - "BinaryScorer"
Cohesion: 0.19
Nodes (12): Coding Style & Naming Conventions, D003 — Separate scoring strategy from inference backend, Phase 1 — Scoring abstraction, 🔬 Research Fork, BinaryBackend, Protocol, Batch scorer that returns one P(yes) for each rendered prompt., BinaryScorer (+4 more)

### Community 9 - "app.js"
Cohesion: 0.15
Nodes (19): addCriteriaRow(), addQuestion(), collectRequest(), connectionStatus, defaults, input(), parseState(), probabilityRows() (+11 more)

### Community 10 - "_parse_request"
Cohesion: 0.15
Nodes (10): main(), _parse_request(), _parse_submission_args(), Any, Register the System One endpoint on SGLang's existing FastAPI app., register_systemone_route(), systemone(), _validate_server_args() (+2 more)

### Community 11 - "Comparative evaluation plan"
Cohesion: 0.22
Nodes (8): Common result schema, Comparative evaluation plan, Early benchmark set, Fairness rules, First useful Pareto plots, Question A — What is the cost of the zero-training constraint?, Question B — Which zero-training scoring rule works best?, Question C — Which model/runtime gives the best local efficiency?

### Community 12 - "ImageBackendTests"
Cohesion: 0.07
Nodes (18): Baseline sandbox-safe run, Compile and package-build baseline, Current sandbox-safe command, External experiments when needed, External real-model integration, Important finding, Inherited suite inventory, Performance profiling suite (+10 more)

### Community 13 - "Research architecture and decision log"
Cohesion: 0.22
Nodes (8): Architecture direction, Change protocol, Decision template, Goal, Metrics, Open design questions, Reference implementations and inspiration, Research architecture and decision log

### Community 14 - "Implementation phases"
Cohesion: 0.25
Nodes (8): Implementation phases, Phase 0 — Repository baseline, Phase 2 — Early comparative scaffold, Phase 3 — llama.cpp/GGUF and profiling, Phase 4 — Zero-training scorer comparison, Phase 5 — Efficient model families, Phase 6 — Broader comparative evaluation, Phase 7 — Additional experimental backends

### Community 17 - "Decisions"
Cohesion: 0.18
Nodes (11): D001 — Fork LLM2Jev as the application base, D002 — No training is required, D004 — Add llama.cpp/GGUF as the first new backend, D005 — Full candidate continuation likelihood is an experimental scoring strategy, D006 — Preserve independent binary scoring as baseline, D007 — Benchmark before choosing a preferred scorer/model, D008 — Split testing by execution environment, D009 — Optimize for research velocity, not production hardening (+3 more)

### Community 19 - "Repository Guidelines"
Cohesion: 0.14
Nodes (13): Architecture Constraints, Build, Test, and Development Commands, Commit & Pull Request Guidelines, Current Research Sequence, Graphify Knowledge Graph, Maintaining AGENTS.md, Profiling Guidelines, Project Structure & Module Organization (+5 more)

### Community 20 - "🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference"
Cohesion: 0.05
Nodes (41): Attribution, Demo video, Dependencies, Fetch the Panda assets, LLM2Jev Pick & Place Arm Demo, Run the MuJoCo version, Start the local service, Installation (+33 more)

### Community 23 - "Performance profiling methodology"
Cohesion: 0.20
Nodes (9): Cache and prefix-reuse profiling, Common workload metrics, CPU profiling, Experiment matrix, GPU profiling, Interpretation, MoE-specific profiling, Performance profiling methodology (+1 more)

## Knowledge Gaps
- **101 isolated node(s):** `questionsElement`, `template`, `submitButton`, `validationMessage`, `connectionStatus` (+96 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 221 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `JevRequest` connect `JevRequest` to `sglang_server.py`, `JevResponse`, `llm2jev/__init__.py`, `BinaryScorer`, `_parse_request`, `🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Why does `ScoringStrategy` connect `BinaryScorer` to `JevRequest`, `sglang_server.py`, `JevResponse`, `llm2jev/__init__.py`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Why does `SGLangBackend` connect `Usage` to `JevRequest`, `sglang_server.py`, `🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference`, `llm2jev/__init__.py`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `JevRequest` (e.g. with `SGLang Python API` and `main()`) actually correct?**
  _`JevRequest` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Are the 36 inferred relationships involving `Noul` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Noul` has 36 INFERRED edges - model-reasoned connections that need verification._
- **Are the 31 inferred relationships involving `Choice` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Choice` has 31 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `compile_binary_questions()` (e.g. with `Choice` and `Noul`) actually correct?**
  _`compile_binary_questions()` has 27 INFERRED edges - model-reasoned connections that need verification._