# Graph Report - llm2jev-research  (2026-09-24)

## Corpus Check
- 73 files · ~208,482 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 6 file(s) not represented in the graph (top: (none) 4, .css 1, .lock 1)

## Summary
- 775 nodes · 1637 edges · 37 communities (32 shown, 5 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 303 edges (avg confidence: 0.87)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c93da819`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- JevRequest
- sglang_server.py
- ChoiceAnswer
- Usage
- llm2jev/__init__.py
- BinaryQuestion
- snake.py
- fetch_panda.py
- test_multimodal.py
- app.js
- ServerArgumentTests
- Comparative evaluation plan
- Testing environments and inherited-suite inventory
- mujoco_demo.py
- SGLangBackend
- utils/__init__.py
- llm2jev
- Decisions
- properties
- LLM2Jev
- 🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference
- properties
- properties
- Performance profiling methodology
- properties
- scorer
- NoulAnswer
- JevResponse
- workload
- ScoreAnswer
- argparse
- result.schema.json
- CompactBenchmarkTests
- Compact Jev research workload
- system
- model
- BinaryBackendOutputTests

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
- `Baseline sandbox-safe run` --references--> `ImageBackendTests`  [INFERRED]
  docs/testing.md → tests/test_multimodal.py
- `Shared prefixes: reuse context across multiple decisions` --references--> `TransformersBackend`  [INFERRED]
  docs/shared-prefix-cache.md → src/llm2jev/backend/transformers/backend.py
- `Coding Style & Naming Conventions` --references--> `ScoringStrategy`  [INFERRED]
  AGENTS.md → src/llm2jev/inference/scoring.py

## Import Cycles
- None detected.

## Communities (37 total, 5 thin omitted)

### Community 0 - "JevRequest"
Cohesion: 0.06
Nodes (37): LLM2Jev Web Demo, How do LLM requests and Jev requests differ?, main(), main(), main(), Question, Choice, Noul (+29 more)

### Community 1 - "sglang_server.py"
Cohesion: 0.09
Nodes (31): collections_abc, dataclasses, K, math, Normalizer, openai_types_chat, Explicit image evidence inside otherwise arbitrary JSON content., validate_multimodal() (+23 more)

### Community 2 - "ChoiceAnswer"
Cohesion: 0.24
Nodes (4): ChoiceAnswer, A selected choice and the probability of every available choice., ChoiceAnswerTests, ProbabilityValidationTests

### Community 3 - "Usage"
Cohesion: 0.05
Nodes (33): pathlib, BinaryBackendOutput, Ordered yes probabilities and usage returned by a binary backend., ChatPrompt, Plan complete-candidate submissions; KV storage belongs to the engine., Seed shared token paths before submitting their remaining branches. Each index…, staged_batches(), prepare_score_batches() (+25 more)

### Community 5 - "BinaryQuestion"
Cohesion: 0.10
Nodes (15): Candidate, is_multimodal(), Any, BinaryQuestion, A model-independent yes/no task compiled from a Jev question., append_content(), ChatPrompt, JSONContent (+7 more)

### Community 6 - "snake.py"
Cohesion: 0.10
Nodes (11): Client, main(), Play Snake with one LLM2Jev Choice question per tick. Inspired by…, Persistent System One client; avoids reconnecting on every tick., _save_gif(), Snake, http_client, random (+3 more)

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

### Community 12 - "Testing environments and inherited-suite inventory"
Cohesion: 0.17
Nodes (11): Baseline sandbox-safe run, Compile and package-build baseline, Current sandbox-safe command, External experiments when needed, External real-model integration, Important finding, Inherited suite inventory, Performance profiling suite (+3 more)

### Community 13 - "mujoco_demo.py"
Cohesion: 0.13
Nodes (13): action_criteria(), direction(), JevClient, main(), PandaPickPlace, Path, One-stage LLM2Jev control of a physical Panda pick-and-place scene., relation() (+5 more)

### Community 14 - "SGLangBackend"
Cohesion: 0.11
Nodes (10): How does staging help the first request?, Outputs and cache behavior, Shared prefixes: reuse context across multiple decisions, Why is the same context processed more than once?, Any, Path, Prefill-only binary scorer using SGLang's native scoring and prefix cache., Shut down this backend's SGLang engine and release GPU resources. (+2 more)

### Community 17 - "Decisions"
Cohesion: 0.10
Nodes (19): Architecture direction, Change protocol, D001 — Fork LLM2Jev as the application base, D002 — No training is required, D004 — Add llama.cpp/GGUF as the first new backend, D005 — Full candidate continuation likelihood is an experimental scoring strategy, D006 — Preserve independent binary scoring as baseline, D007 — Benchmark before choosing a preferred scorer/model (+11 more)

### Community 18 - "properties"
Cohesion: 0.08
Nodes (26): maximum, minimum, type, properties, minimum, type, minimum, type (+18 more)

### Community 19 - "LLM2Jev"
Cohesion: 0.05
Nodes (39): Architecture Constraints, Build, Test, and Development Commands, Coding Style & Naming Conventions, Commit & Pull Request Guidelines, Current Research Sequence, Graphify Knowledge Graph, Maintaining AGENTS.md, Profiling Guidelines (+31 more)

### Community 20 - "🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference"
Cohesion: 0.05
Nodes (41): Attribution, Demo video, Dependencies, Fetch the Panda assets, LLM2Jev Pick & Place Arm Demo, Run the MuJoCo version, Start the local service, Installation (+33 more)

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

### Community 26 - "NoulAnswer"
Cohesion: 0.22
Nodes (4): NoulAnswer, The probability that the answer is yes or the statement is true., NoulAnswerTests, FixedStrategy

### Community 27 - "JevResponse"
Cohesion: 0.27
Nodes (4): _format_json(), JevResponse, Answers produced by a model for a Jev request., JevResponseTests

### Community 28 - "workload"
Cohesion: 0.25
Nodes (8): version, workload, minLength, type, additionalProperties, properties, required, type

### Community 29 - "ScoreAnswer"
Cohesion: 0.32
Nodes (3): A probability-weighted score and its ordered rubric., ScoreAnswer, ScoreAnswerTests

### Community 30 - "argparse"
Cohesion: 0.29
Nodes (4): argparse, Score image evidence with Transformers or SGLang, without decoding., Evaluate a Jev request with a local SGLang engine., Run a mixed LLM2Jev request with a local Transformers model.

### Community 31 - "result.schema.json"
Cohesion: 0.29
Nodes (6): additionalProperties, $id, required, $schema, title, type

### Community 33 - "Compact Jev research workload"
Cohesion: 0.50
Nodes (3): Compact Jev research workload, Result record, Validation

### Community 34 - "system"
Cohesion: 0.50
Nodes (4): system, additionalProperties, required, type

### Community 35 - "model"
Cohesion: 0.67
Nodes (3): minLength, type, model

## Knowledge Gaps
- **168 isolated node(s):** `$schema`, `$id`, `title`, `type`, `additionalProperties` (+163 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 292 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `JevRequest` connect `JevRequest` to `sglang_server.py`, `llm2jev/__init__.py`, `SGLangBackend`, `LLM2Jev`, `🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference`, `NoulAnswer`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Why does `ScoringStrategy` connect `LLM2Jev` to `JevRequest`, `sglang_server.py`, `JevResponse`, `llm2jev/__init__.py`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Why does `SGLangBackend` connect `SGLangBackend` to `JevRequest`, `Usage`, `🧠 LLM2Jev Research: Model-Agnostic Jev-Style Decision Inference`, `llm2jev/__init__.py`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `JevRequest` (e.g. with `SGLang Python API` and `main()`) actually correct?**
  _`JevRequest` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Are the 36 inferred relationships involving `Noul` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Noul` has 36 INFERRED edges - model-reasoned connections that need verification._
- **Are the 31 inferred relationships involving `Choice` (e.g. with `LLM2Jev Web Demo` and `How do LLM requests and Jev requests differ?`) actually correct?**
  _`Choice` has 31 INFERRED edges - model-reasoned connections that need verification._
- **Are the 27 inferred relationships involving `compile_binary_questions()` (e.g. with `Choice` and `Noul`) actually correct?**
  _`compile_binary_questions()` has 27 INFERRED edges - model-reasoned connections that need verification._