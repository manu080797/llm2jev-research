# Graph Report - llm2jev-research  (2026-09-24)

## Corpus Check
- 75 files · ~209,521 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .css 1, .lock 1)

## Summary
- 796 nodes · 1687 edges · 37 communities (31 shown, 6 thin omitted)
- Extraction: 82% EXTRACTED · 18% INFERRED · 0% AMBIGUOUS · INFERRED: 310 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `ad71729f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- JevRequest
- sglang_server.py
- Usage
- ImageBackendTests
- FakeTokenizer
- llm2jev/__init__.py
- run_baseline.py
- fetch_panda.py
- test_multimodal.py
- app.js
- ServerArgumentTests
- Comparative evaluation plan
- README.md
- mujoco_demo.py
- SGLangBackend
- utils/__init__.py
- llm2jev
- Decisions
- properties
- Repository Guidelines
- 🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference
- properties
- properties
- Performance profiling methodology
- properties
- scorer
- From Jev Request to LLM Request
- LLM2Jev Pick & Place Arm Demo
- workload
- PrefixPlanTests
- Using multimodal data
- result.schema.json
- CompactBenchmarkTests
- Usage guide
- system
- model
- test_converter.py

## God Nodes (most connected - your core abstractions)
1. `JevRequest` - 70 edges
2. `Noul` - 47 edges
3. `Choice` - 42 edges
4. `compile_binary_questions()` - 38 edges
5. `Usage` - 34 edges
6. `assemble_response()` - 31 edges
7. `JevResponse` - 30 edges
8. `SGLangBackend` - 29 edges
9. `Score` - 28 edges
10. `LLM2Jev` - 27 edges

## Surprising Connections (you probably didn't know these)
- `Shared prefixes: performance benchmarks` --references--> `SGLangBackend`  [INFERRED]
  docs/shared-prefix-benchmarks.md → src/llm2jev/backend/sglang/backend.py
- `SGLang Python API` --references--> `JevRequest`  [INFERRED]
  docs/usage.md → src/llm2jev/core/request.py
- `Coding Style & Naming Conventions` --references--> `ScoringStrategy`  [INFERRED]
  AGENTS.md → src/llm2jev/inference/scoring.py
- `Running the Transformers binary baseline` --references--> `TransformersBackend`  [INFERRED]
  benchmarks/README.md → src/llm2jev/backend/transformers/backend.py
- `Shared prefixes: reuse context across multiple decisions` --references--> `TransformersBackend`  [INFERRED]
  docs/shared-prefix-cache.md → src/llm2jev/backend/transformers/backend.py

## Import Cycles
- None detected.

## Communities (37 total, 6 thin omitted)

### Community 0 - "JevRequest"
Cohesion: 0.05
Nodes (38): LLM2Jev Web Demo, How do LLM requests and Jev requests differ?, main(), main(), main(), Normalizer, Question, Choice (+30 more)

### Community 1 - "sglang_server.py"
Cohesion: 0.06
Nodes (46): collections_abc, dataclasses, K, math, openai_types_chat, pathlib, BinaryBackendOutput, Ordered yes probabilities and usage returned by a binary backend. (+38 more)

### Community 2 - "Usage"
Cohesion: 0.05
Nodes (19): importlib_util, ChoiceAnswer, NoulAnswer, A selected choice and the probability of every available choice., A probability-weighted score and its ordered rubric., The probability that the answer is yes or the statement is true., ScoreAnswer, Input and output token counts, when reported by the model backend. (+11 more)

### Community 3 - "ImageBackendTests"
Cohesion: 0.11
Nodes (14): Baseline sandbox-safe run, Compile and package-build baseline, Current sandbox-safe command, External experiments when needed, External real-model integration, Important finding, Inherited suite inventory, Performance profiling suite (+6 more)

### Community 5 - "llm2jev/__init__.py"
Cohesion: 0.06
Nodes (37): Candidate, D003 — Separate scoring strategy from inference backend, Phase 1 — Scoring abstraction, 🔬 Research Fork, BinaryBackend, ChatPrompt, Protocol, Batch scorer that returns one P(yes) for each rendered prompt. (+29 more)

### Community 6 - "run_baseline.py"
Cohesion: 0.05
Nodes (35): argparse, Compact Jev research workload, Result record, Running the Transformers binary baseline, Validation, _hardware_name(), _load_workload(), main() (+27 more)

### Community 7 - "fetch_panda.py"
Cohesion: 0.10
Nodes (17): concurrent_futures, fetch(), git_sha(), main(), download(), Fetch the pinned Apache-2.0 Panda assets used by the MuJoCo demo., DemoHandler, Serve the web demo and proxy requests to an LLM2Jev HTTP server. (+9 more)

### Community 8 - "test_multimodal.py"
Cohesion: 0.08
Nodes (20): base64, contextlib, copy, io, SimpleNamespace, Any, score_output(), tempfile (+12 more)

### Community 9 - "app.js"
Cohesion: 0.15
Nodes (19): addCriteriaRow(), addQuestion(), collectRequest(), connectionStatus, defaults, input(), parseState(), probabilityRows() (+11 more)

### Community 10 - "ServerArgumentTests"
Cohesion: 0.22
Nodes (7): main(), _parse_submission_args(), Any, Register the System One endpoint on SGLang's existing FastAPI app., register_systemone_route(), _validate_server_args(), ServerArgumentTests

### Community 11 - "Comparative evaluation plan"
Cohesion: 0.22
Nodes (8): Common result schema, Comparative evaluation plan, Early benchmark set, Fairness rules, First useful Pareto plots, Question A — What is the cost of the zero-training constraint?, Question B — Which zero-training scoring rule works best?, Question C — Which model/runtime gives the best local efficiency?

### Community 13 - "mujoco_demo.py"
Cohesion: 0.13
Nodes (13): action_criteria(), direction(), JevClient, main(), PandaPickPlace, Path, One-stage LLM2Jev control of a physical Panda pick-and-place scene., relation() (+5 more)

### Community 14 - "SGLangBackend"
Cohesion: 0.11
Nodes (10): How does staging help the first request?, Outputs and cache behavior, Shared prefixes: reuse context across multiple decisions, Why is the same context processed more than once?, Any, Path, Prefill-only binary scorer using SGLang's native scoring and prefix cache., Shut down this backend's SGLang engine and release GPU resources. (+2 more)

### Community 17 - "Decisions"
Cohesion: 0.07
Nodes (27): Architecture direction, Change protocol, D001 — Fork LLM2Jev as the application base, D002 — No training is required, D004 — Add llama.cpp/GGUF as the first new backend, D005 — Full candidate continuation likelihood is an experimental scoring strategy, D006 — Preserve independent binary scoring as baseline, D007 — Benchmark before choosing a preferred scorer/model (+19 more)

### Community 18 - "properties"
Cohesion: 0.08
Nodes (26): maximum, minimum, type, properties, minimum, type, minimum, type (+18 more)

### Community 19 - "Repository Guidelines"
Cohesion: 0.13
Nodes (14): Architecture Constraints, Build, Test, and Development Commands, Coding Style & Naming Conventions, Commit & Pull Request Guidelines, Current Research Sequence, Graphify Knowledge Graph, Maintaining AGENTS.md, Profiling Guidelines (+6 more)

### Community 20 - "🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference"
Cohesion: 0.18
Nodes (11): ✅ Current LLM2Jev Baseline, 🎮 Demos, 📊 Existing Baseline Benchmarks, 📖 Getting Started, 📦 Installation, 📄 License, 🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference, 🚀 Quick Start (+3 more)

### Community 21 - "properties"
Cohesion: 0.11
Nodes (19): items, minItems, type, type, minLength, type, additionalProperties, properties (+11 more)

### Community 22 - "properties"
Cohesion: 0.12
Nodes (16): enum, type, type, device_mode, hardware, model_revision, quantization, runtime (+8 more)

### Community 23 - "Performance profiling methodology"
Cohesion: 0.20
Nodes (9): Cache and prefix-reuse profiling, Common workload metrics, CPU profiling, Experiment matrix, GPU profiling, Interpretation, MoE-specific profiling, Performance profiling methodology (+1 more)

### Community 24 - "properties"
Cohesion: 0.20
Nodes (10): additionalProperties, required, type, minLength, type, properties, aggregate, experiment_id (+2 more)

### Community 25 - "scorer"
Cohesion: 0.20
Nodes (10): minLength, type, type, name, parameters, scorer, additionalProperties, properties (+2 more)

### Community 26 - "From Jev Request to LLM Request"
Cohesion: 0.22
Nodes (9): Confidence is also calculated in code, From Jev Request to LLM Request, How does an LLM produce the same JSON output?, LLM2Jev: first construct independent yes/no judgments, More input tokens: could this make inference slower?, Then calculate probabilities from yes/no logits, Turning candidate scores into final answers, What does a yes/no input look like? (+1 more)

### Community 27 - "LLM2Jev Pick & Place Arm Demo"
Cohesion: 0.25
Nodes (7): Attribution, Demo video, Dependencies, Fetch the Panda assets, LLM2Jev Pick & Place Arm Demo, Run the MuJoCo version, Start the local service

### Community 28 - "workload"
Cohesion: 0.25
Nodes (8): version, workload, minLength, type, additionalProperties, properties, required, type

### Community 30 - "Using multimodal data"
Cohesion: 0.29
Nodes (7): Building a request, Choosing where to place images, HTTP API calls, SGLang backend, Supported image sources, Transformers backend, Using multimodal data

### Community 31 - "result.schema.json"
Cohesion: 0.29
Nodes (6): additionalProperties, $id, required, $schema, title, type

### Community 33 - "Usage guide"
Cohesion: 0.40
Nodes (5): Choosing a mode, SGLang Python API, System One HTTP API, Transformers Backend, Usage guide

### Community 34 - "system"
Cohesion: 0.50
Nodes (4): system, additionalProperties, required, type

### Community 35 - "model"
Cohesion: 0.67
Nodes (3): minLength, type, model

### Community 36 - "test_converter.py"
Cohesion: 0.25
Nodes (3): BinaryBackendOutputTests, FailingBackend, ChatPrompt

## Knowledge Gaps
- **168 isolated node(s):** `$schema`, `$id`, `title`, `type`, `additionalProperties` (+163 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 299 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `JevRequest` connect `JevRequest` to `Usage guide`, `Usage`, `sglang_server.py`, `llm2jev/__init__.py`, `SGLangBackend`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Why does `ScoringStrategy` connect `llm2jev/__init__.py` to `JevRequest`, `Repository Guidelines`?**
  _High betweenness centrality (0.056) - this node is a cross-community bridge._
- **Why does `SGLangBackend` connect `SGLangBackend` to `JevRequest`, `sglang_server.py`, `Usage`, `llm2jev/__init__.py`, `README.md`?**
  _High betweenness centrality (0.050) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `JevRequest` (e.g. with `SGLang Python API` and `main()`) actually correct?**
  _`JevRequest` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Are the 36 inferred relationships involving `Noul` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Noul` has 36 INFERRED edges - model-reasoned connections that need verification._
- **Are the 31 inferred relationships involving `Choice` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Choice` has 31 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `compile_binary_questions()` (e.g. with `Choice` and `Noul`) actually correct?**
  _`compile_binary_questions()` has 27 INFERRED edges - model-reasoned connections that need verification._