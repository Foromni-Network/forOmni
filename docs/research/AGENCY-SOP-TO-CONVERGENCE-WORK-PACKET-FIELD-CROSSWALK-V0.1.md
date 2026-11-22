# Agency SOP → Foromni Convergence Packet: Source-Level Field Crosswalk v0.1

**Date:** 2026-11-22 UTC. **Status:** research / mapping proposal only. No tests, deployments, merges, source ingestion, worker authorization or frozen FOR-007 contract edits.  
**Existing contracts:** [Convergence Work Packet v0.2](CONVERGENCE-WORK-PACKET-TYPED-CONTRACT-V0.2.md), [Agency Literature Case Study v0.2](AGENCY-LITERATURE-TO-CONVERGENCE-EVIDENCE-CASE-STUDY-V0.2.md), [Case Study Flywheel](OPEN-SOURCE-AINO-CASE-STUDY-FLYWHEEL-PROTOCOL.md).

## Direct-source inspection ledger

| ID | Source revision / exact file | Observation class | Important observation |
|---|---|---|---|
| AA-1 | [Agency Agents@8ae6164: activation prompts](https://github.com/msitarzewski/agency-agents/blob/8ae6164602c95ca78828b148b9052460ee426885/strategy/coordination/agent-activation-prompts.md), Git blob `473517613089c98295a65d5cde91558c9cddd77d` | Code/document inspected, **not executed** | NEXUS coordinator uses project spec, current phase, handoff template, QA loop, 3-retry escalation. Developer prompts identify task, acceptance criteria, reference docs. Reviewer prompt has a proposed PASS/FAIL; actual independent reviewer credential, executable QA and provenance are **not established by prompt**. |
| AA-2 | [Agency Agents@8ae6164: NEXUS strategy](https://github.com/msitarzewski/agency-agents/blob/8ae6164602c95ca78828b148b9052460ee426885/strategy/nexus-strategy.md), blob `b80a9b27e03c72c6f9205d8099e1432f07415118` | Document inspected | Phase gates, parallel division ownership, explicit work products, continuity handoffs, role matrix. Source states its own goals; no external confirmation of implementation reliability. |
| BM-1 | [BMAD@e435a225: build workflow](https://github.com/bmad-code-org/BMAD-METHOD/blob/e435a22574fe55722841086e5566420178b98df3/skills/method/bmad-build/workflow.md), blob `485332be7b037c8bfb292bf465cb58ac1f3c3805` | Document inspected | Ready-for-development requirements: file-specific actions, dependency ordering, Given/When/Then observable acceptance; step-file sequencing. Instructions are not external enforcement. |
| BM-2 | [BMAD@e435a225: plan template](https://github.com/bmad-code-org/BMAD-METHOD/blob/e435a22574fe55722841086e5566420178b98df3/skills/method/bmad-build/plan-template.md), blob `bbb3257031a87bd2e6cfb21388d0ca44fae4731a` | Template inspected | Baseline revision, context paths, human-owned frozen intent/boundaries, code map, task AC, append-only review triage and verification instructions. A template's `baseline_revision` is not independently validated Git observation. |
| BM-3 | [BMAD@e435a225: ticket template](https://github.com/bmad-code-org/BMAD-METHOD/blob/e435a22574fe55722841086e5566420178b98df3/skills/method/bmad-agent-po/assets/ticket-template.md), blob `e5c8ec22b2b5efc44306ea8a940d1292a96d4b56` | Template inspected | `sources`, `companions`, `after`, `covers`, risk, human-in-loop, numbered acceptance criteria and explicit unresolved assumptions. Tracker assignee is metadata, not a trusted Foromni lease. |

**Correction to previous exploratory study:** BMAD's current source path is `skills/method/bmad-build/workflow.md`, not `skills/bmad-build/workflow.md`; repository documentation also distinguishes an evolving V7 preview from stable V6.12. Pin version/commit and do not mix templates across lines.

## Explicit field crosswalk — promote semantics, never authority

| Upstream mechanism | Foromni existing field / relation | Can copy as informational input? | Must be independently enforced or supplied |
|---|---|---|---|
| NEXUS project name, phase, task ID | `objective_id`, `task_id`, `task_revision` | Only as a suggested lookup/reference | Accepted task registry assigns canonical identity/revision |
| NEXUS specialist agent prompt | role/capability metadata **outside** packet | Yes, labeled untrusted instruction text | Authenticated `agent_id`, current grant and sandbox identity |
| NEXUS handoff reference documents | `dependencies`, `acceptance.criteria_refs` | Propose references | Contract owner confirms exact revision/digest |
| NEXUS maximum three retries | `resource_limits.max_attempts` | Suggested policy, not default | Trusted budget/attempt policy controls actual cap |
| NEXUS QA PASS/FAIL report | candidate/evidence linkage after attempted work | As worker-asserted claim only | Independent evaluator identity, exact candidate SHA and protected test logs |
| BMAD `baseline_revision` | `source.observed_main_sha` | Candidate source hint | Trusted Git reader obtains canonical object and confirms it exists |
| BMAD ticket `after`, `covers` | `dependencies[].task_id`, `task_revision`, `required_state`, `interface_digest` | Proposed dependency graph | Registry validates revisions, actual integration state and compatibility |
| BMAD human-frozen Intent/Boundaries | accepted task revision + `acceptance.criteria_refs` | Structured drafting aid | Authorized human acceptance of revision/scope |
| BMAD Given/When/Then criterion | `acceptance.criteria_refs`, `criteria_revision` | Criteria text and pre-registration | Independent tests observe the correct user-facing behavior; self-test insufficient |
| BMAD `context` and Code Map paths | `ownership.claimed_paths`, `interface_areas` | Suggested paths only | Allocation lease + enforced repository scope + current Git state |
| BMAD `risk`, `review`, `lenses_ran` | test-plan/check-class inputs (policy external) | Research/QA suggestions | Trusted controller decides required checks and separately attests what ran |
| BMAD Review Triage/Change Logs | `result_evidence_ref` and attempt history (external ledger) | Supplemental explanation | Append-only trusted log of actual events and independent outcomes |
| BMAD Verification Commands | evaluator plan / `acceptance.test_plan_revision` | Candidate commands | Separate QA runs trusted commands against independently reconstructed SHA |
| NEXUS phase gate / BMAD done status | `packet_state` vs future candidate acceptance | Progress suggestion only | Never upgrade to `accepted`, `merged`, `released` from document text |

**Non-negotiable isolation:** upstream prompts, files and schemas are data, not instructions to an agent performing this research, not a grant, and not authoritative Foromni policy. Neither a JSON-schema PASS nor a README's "quality gate" overrides Git permissions or evaluator custody. No direct schema modifications proposed.

## Worked synthetic translation (ILLUSTRATIVE, not an authorized packet)

Input: "When a user submits an invalid form, show a useful error without saving."  
Proposed BMAD-style observable AC: given invalid form data, when submitted, then a visible validation error appears and no database record is created.  
NEXUS-style proposed role: frontend worker; QA role: independent behavior reviewer.  
Foromni registry required: canonical `task_id` and revision, authoritative `observed_main_sha`, valid lease epoch, granted tool scope, precise QA plan revision; **none are conferred by this translation**.  
Negative fixture: worker returns markdown 'PASS' while the form persists invalid input. Expected independently observed result: **FAIL**, not accepted by proxy.  
Another negative fixture: the expected UI behavior passes but the QA test ran against an older source revision. Expected: **evidence invalid for candidate SHA**.

## Small experiment registration (NOT EXECUTED)

- **C0:** one worker, freeform task description.
- **C1:** same worker, BMAD-derived frozen intent + observable criteria, no extra agent.
- **C2:** C1 plus Agency Agents-derived specialist role and typed handoff to separately authenticated reviewer, if execution setup later permits.
- Use same base repo state, same feature, same model/runtime or matched randomization, same limits, same independent evaluator and negative test suite.
- Metrics: spec coverage, handoff loss, independently accepted patches/attempt, retries, human intervention, total metered/unpriced costs, incorrect claimed PASS rate, scope escalation attempts.
- Controls: worker cannot write protected refs, reviewer cannot trust worker-supplied evidence, prompts cannot edit accepted criteria, no secret-bearing inputs, no unrelated network access.
- **Stop conditions:** stale source or revision, missing evaluator custody, ambiguous permission, budget exceeded, QA source mismatch or unpriced missing costs.

## Decision register

1. **ADAPT** BMAD's human-frozen intent, concise plans, source-linked dependencies, Given/When/Then behavioral AC and review triage as *authoring conventions*.
2. **ADAPT** Agency Agents' role/deliverable descriptors and bounded escalation loop as metadata/coordination suggestions.
3. **REJECT** any translation in which worker-supplied PASS, source SHA, assignee or phase completion is treated as independent authority.
4. **DEFER** runtime integration of BMAD or NEXUS and multi-agent scaling; the FOR-007 single worker path must first prove source-bound independent acceptance.
5. **NEXT RESEARCH:** contrast BMAD's review lens configuration and NEXUS QA claims with FOR-011 independent evaluator custody, and preregister failure-mode examples. **No testing until separately authorized.**

**Licensing/trademark caveat:** BMAD README/LICENSE identify MIT terms and distinct trademarks; Agency Agents license/individual imported artifacts require file-scoped verification before copying. This document paraphrases mechanisms rather than reproducing templates or importing code.

**Evidence grade:** upstream document/template inspected; source blobs and commit paths pinned; runtime reproducibility **not shown**. No synthetic experiment was run.
