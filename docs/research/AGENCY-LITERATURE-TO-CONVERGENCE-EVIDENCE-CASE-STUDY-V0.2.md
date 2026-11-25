# Agency Literature to Convergence Evidence — Comparative Case Study v0.2

**Date:** 2026-11-22 UTC · **Status:** READ-ONLY DESK STUDY + PROPOSED EXPERIMENT; NOT EXECUTED OR INTEGRATED.  
**Scope:** Foromni research branch only. Preserves frozen FOR-007; does not grant execution, CI, merge, deployment, external outreach or spending.  
**Extends (do not duplicate):** OPEN-SOURCE-AINO-CASE-STUDY-FLYWHEEL-PROTOCOL.md; EXTERNAL-CASE-STUDY-OPEN-SOURCE-AI-AGENCIES-AND-ORGANIZATIONS-V0.1.md; CONVERGENCE-WORK-PACKET-TYPED-CONTRACT-V0.2.md; EXTERNAL-CASE-STUDY-PAPERCLIP-SOURCE-LEVEL-AGENCY-CONTROL-PLANE-V0.2.md.

## Research question

Can publicly available **agent prompts, organizational schematics and SOP documentation** be converted into small typed work/evidence artifacts that satisfy Foromni's independent-source acceptance chain, without adopting their runtime, trusting agent self-report, or expanding the frozen MVP?

## Source-bound inspections and distinctions

1. **Agency Agents — prompts and human-readable NEXUS handoffs.** Prior pinned repository snapshot: [msitarzewski/agency-agents@8ae6164602c95ca78828b148b9052460ee426885](https://github.com/msitarzewski/agency-agents/tree/8ae6164602c95ca78828b148b9052460ee426885). Inspect [strategy/QUICKSTART.md](https://github.com/msitarzewski/agency-agents/blob/main/strategy/QUICKSTART.md), [strategy/nexus-strategy.md](https://github.com/msitarzewski/agency-agents/blob/main/strategy/nexus-strategy.md), and [strategy/coordination/agent-activation-prompts.md](https://github.com/msitarzewski/agency-agents/blob/main/strategy/coordination/agent-activation-prompts.md). The materials show role activation instructions, specialist coordination, and expectations for staged outputs. **Harvest:** versioned role descriptors and deliverable templates. **Do not infer:** authenticated worker identity, real claim leases, verified tool execution, independent grader or safe artifact provenance from a role prompt. Paths were web-checked against the current public tree; historical pinned file-by-file equivalence has NOT been independently checked in this pass.

2. **BMAD Method — structured requirements/acceptance as handoff documents.** [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD); [skills/bmad-build/workflow.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/skills/bmad-build/workflow.md) documents step-file workflow and Given/When/Then acceptance checks. The README explicitly permits using its briefs, specs and architecture with a separate existing delivery workflow. **Harvest:** explicit pre-implementation requirements, structured expected behaviors, and traceable handoff files. **Do not infer:** these docs establish independent proof of execution, trusted policy checks, or candidate-SHA acceptance. **Pinning gap:** this study references moving main-branch docs; pin exact upstream SHA before importing a particular file or code.

3. **MetaGPT — SOP-driven company with production of structured artifacts.** Prior pinned snapshot: [FoundationAgents/MetaGPT@11cdf466d042aece04fc6cfd13b28e1a70341b1f](https://github.com/FoundationAgents/MetaGPT/tree/11cdf466d042aece04fc6cfd13b28e1a70341b1f). Its project documents describe role/SOP coordination and generated project artifacts. **Harvest:** lifecycle between requirement → design → implementation artifacts, not simulated managerial authority. **Do not infer:** a generated PRD, API design, or source code file proves correct runtime behavior or a protected reviewer identity. Current main README and historic version are distinct until pinned module inspection.

4. **ChatDev 2.0 — explicit role graph / context-preserving message edges.** Prior pinned snapshot: [OpenBMB/ChatDev@464a681ba7bda869db97a50c5fa707c9a0fb57a0](https://github.com/OpenBMB/ChatDev/tree/464a681ba7bda869db97a50c5fa707c9a0fb57a0); [current tutorial](https://github.com/OpenBMB/ChatDev/blob/main/frontend/public/tutorial-en.md) specifies agent-node roles, edge settings to retain original message, and graph-based configuration. **Harvest:** make original objective and immutable task revision explicit at every handoff. **Do not infer:** preserving message text enforces authorization or stops context injection. Legacy company-simulation branch differs from current 2.0.

5. **Paperclip — actual control plane benchmark, not a replacement for above literature.** [Source-level audit](EXTERNAL-CASE-STUDY-PAPERCLIP-SOURCE-LEVEL-AGENCY-CONTROL-PLANE-V0.2.md) pinned to [paperclip@324ec1f](https://github.com/paperclipai/paperclip/tree/324ec1f537a9ba1e84239faa81bcef326a5dd1b7). **Harvest:** transactional claim, budget reservations, idempotent receipts, human approval history. **Do not infer:** independently reconstructed candidate-SHA QA is proven by task checkout or human approval alone.

## Convergence bridge: evidence, not prose-as-authority

Proposed *research-stage* `pattern_evidence_record` (not an approved database schema or grants contract):

| Field | Expected meaning |
|---|---|
| `pattern_id`, `study_id`, `research_question` | Unambiguous link to existing study/frozen objective |
| `upstream_repo`, `upstream_commit_sha`, `upstream_paths` | Reconstructible external source snapshot; mark unknown if not pinned |
| `observation_class` | `docs_described`, `code_inspected`, `test_executed`, `independent_reproduced` |
| `mechanism`, `counterexample`, `limitations` | Precise claim, failure mode, and source-scoped uncertainty |
| `foromni_task_refs`, `contract_refs` | Existing FOR-007 / FOR-009 / FOR-011 / FOR-012 / FOR-013 / FOR-016 mapping only |
| `candidate_delta`, `implementation_dependency`, `license_review` | Narrow proposed modification; explicit license gate |
| `experiment_fixture_digest`, `result_evidence_ref` | Empty/unknown until an experiment is actually run |
| `authority_status` | Always `research_only` until separately reviewed/authorized |

**Conversion rule:** a written claim never becomes a granted task, a PASS, or an accepted candidate. A trusted policy controller validates task revision, source SHA, lease, actor, project boundary, test custody and approval at action time. Research may suggest acceptance criteria; only authorized project governance adopts them.

## Smallest comparable experiment — design, not execution

**Objective:** for one synthetic feature request, compare three SOP/handoff variants with the same coding task, source baseline, time limit, tools and evaluator:
- A: freeform single worker baseline;
- B: Agency Agents role prompt + NEXUS-style handoff;
- C: BMAD-style specification/acceptance + MetaGPT-style staged artifact handoff.

**Pre-register outputs:** task revision and acceptance conditions, role descriptor digest, handoff manifest, source candidate SHA, independent test invocation and test outcome, cost/time, failure/retry record, source-to-spec correspondence. Do not count a beautifully formatted plan as code completion.

**Adversarial cases:** changed requirement after handoff; forged test PASS in generated document; missing original objective during delegation; stale source SHA; role prompt requesting privilege elevation; broken implementation with persuasive completion message; independent reviewer receiving model-generated tests only.

**Scoring:** prioritize independently accepted outcome per total attempt cost and human review time; separately measure specification completeness, handoff fidelity, unverified claims, security-policy violations, source provenance and recovery. Failure or missing telemetry is recorded as unknown/failure, not zero cost or a PASS.

**Provisional decisions:**
- Agency Agents: **ADAPT role/deliverable metadata**, not security capability or full agent roster.
- BMAD: **ADAPT acceptance-oriented specification conventions**, pending exact pinned artifact/license check.
- MetaGPT: **STUDY structured SOP artifacts**; defer runtime dependency.
- ChatDev: **STUDY context-retention/topology patterns**; defer runtime dependency.
- Paperclip: continue source-level control-plane tests under existing FOR-009/012/013 targets.
- Foromni: **RETAIN independent source observer, isolated executor, QA custody and human candidate acceptance** as nondelegable authority boundaries.

## Research follow-ups in order

1. Pin exact BMAD and role-template source SHAs, inspect corresponding actual files and license scope.
2. Build a one-page crosswalk from SOP output fields into existing Convergence Work Packet v0.2 without modifying its frozen/accepted authority.
3. Prepare synthetic fixtures and negative cases for independent evaluation; do not execute until separately authorized.
4. Compare with Agency Swarm, CrewAI, OpenAgents or AG2 only if the result exposes a specific unresolved coordination bottleneck.

**Not done:** no upstream software cloned or executed, no experiment run, no schema approved, no Foromni runtime altered, no acceptance gate passed. Source/branch citations are research pointers rather than proof of compatibility.
