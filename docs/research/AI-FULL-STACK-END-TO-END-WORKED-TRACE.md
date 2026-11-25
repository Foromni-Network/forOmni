# Autonomous Full-Stack Delivery: A Worked End-to-End Event Trace

**Status:** RESEARCH TABLETOP / HYPOTHETICAL EVENTS. No agent executions, code generation, merges, CI runs, deployments or human approvals actually occurred.  
**Date:** 2026-11-21  
**Project:** Foromni only. IE remains independent and untouched.  
**Companions:** AI-OPERATED-AINO-OVERSIGHT-MODEL.md, AI-WORKFORCE-AUTHORITY-EVENT-CONTRACT-V0.1.md, END-TO-END-FULL-STACK-AGENT-TEAM-RESEARCH-ROADMAP.md, CONVERGENCE-CONTRACT-V0.1.md.

## Research question

How does a founder's natural-language idea become an independently verified full-stack application while **agents do routine work**, a deterministic policy layer protects boundaries, independent QA validates evidence, and humans approve only meaningful objectives, exceptions and consequential release?

Test the structure without claiming to have built the software. Compare one generalist, three workers and eight workers against identical requirements and quality gates.

## The founder's example request (fictional)

> "Build a small workspace where an independent collective can create projects, invite teammates, manage tasks, track contributions and see what's finished. Make it approachable and mobile-friendly. Let the agents build the product; I want to approve important decisions, not every coding change."

### Initial objective envelope, to be confirmed by owner

- Scope: one isolated **synthetic** application, no real users or real-world data.
- Deliverable: accessible responsive app with UI, persistent database, authenticated API, basic roles and task activity history.
- Constraints: no third-party billable integrations or user invitations; no public release; sandbox only if separately authorized for future experiments.
- Budget: example capped values in trace are **fictional**, not granted spending permission.
- Human review: objective and privacy model, exceptional spending, identity/permission changes, real public launch.
- Evidence: acceptance rubric frozen before implementations; hostile permission and data-isolation tests included.
- The AI product agent may propose refinements; it cannot silently change requirements.

## Criteria for a complete staged vertical slice

| Code | Criterion | Independent evidence expectation |
|---|---|---|
| AC-01 | Accessible responsive homepage/project dashboard | Tested semantic navigation, keyboard use and basic mobile viewport |
| AC-02 | Authenticated membership and scoped project roles | Auth unit/integration tests with cross-tenant denial and privilege escalation attempts |
| AC-03 | Persistent projects and tasks with migrations | Clean-db setup, CRUD, rollback/seed test and migration review |
| AC-04 | Assignments, task state and activity provenance | API/database tests plus end-to-end work session |
| AC-05 | Clear error/loading states and no fictitious completed task | Browser E2E with failure injection |
| AC-06 | Secrets and private resources protected | Independent security review, dependency check, isolated test identities |
| AC-07 | Reproducible build and disposable staging | Pinned manifest, reproducible setup, health endpoint and generated artifact |
| AC-08 | Combined source integrates on exact expected mainline | Merge-group exact-revision checks and postmerge readback |
| AC-09 | Maintainer can reproduce and fix injected bug | Handoff packet, bug repro, independent repair demonstration |
| AC-10 | Release remains separate from staging acceptance | Specific accountable owner approval before publication |

**No criterion above has passed a real test in this exercise.**

## Actors (roles can be combined except where independence is required)

- `H-OWNER`: human objective/budget/policy owner, final consequential release approval.
- `A-INTENT`: AI product/spec agent; proposes outcome and slice decomposition.
- `A-ARCH`: AI architecture/contracts agent; proposes API/data boundary.
- `A-BE`: AI backend/data implementer, own candidate branch.
- `A-FE`: AI frontend implementer, own candidate branch.
- `A-REPAIR`: AI debugger/repair worker, separate task attempt.
- `A-REVIEW`: independent QA agent/service *under distinct authority when policy requires*.
- `S-POLICY`: deterministic trusted authorization and budget enforcement, not an LLM.
- `S-MERGE`: protected Git merge queue/controller; only scoped permission to update protected main.
- `S-LEDGER`: reconciles authoritative external evidence and event projections; never upgrades status on self-report.

For the **one-agent** cohort, one model does `A-INTENT + A-ARCH + A-BE + A-FE + A-REPAIR`; QA and policy stay separate. For the **three-agent** cohort, one coordinates/architects and two implement, while independent QA remains external. For the **eight-agent** cohort, more specialties can parallelize but share the same protected verification capacity.

## Sequential event and handoff trace (all fictional)

| # | Event, actor and authorized action | Expected evidence / status | If it fails |
|---|---|---|---|
| E01 | H-OWNER submits natural-language objective and nonnegotiable boundaries | `objective.proposed`; no worker write grant yet | Clarify conflicting goals, no agent launch |
| E02 | A-INTENT creates measurable AC-01..AC-10 and exclusions | `requirements.draft` linked to objective revision | H-OWNER approves/edits scope once, not each task |
| E03 | H-OWNER approves objective envelope, cost ceiling and risk policy | Time-bounded authenticated `objective.approved` | Deny implementation authorization |
| E04 | A-ARCH proposes architecture: UI, API, database, auth, interfaces and migration policy | Dependency DAG and architecture decision draft | Material privacy change escalates |
| E05 | S-POLICY assigns only isolated worker grants, with branch prefixes, tool allowlist, network restrictions, expiry | Trusted `grant.issued` events; no protected main credentials | Reject grant if overbroad or attempts escalation |
| E06 | A-BE produces API schema and persistence slice on `work/be-01`; A-FE builds UI on `work/fe-01` | Two versioned candidate manifests, task revisions and SHAs | Interface drift returns to contract negotiation |
| E07 | A-ARCH checks both API contracts and dependency revisions | Reconciled shared schema and task graph | Conflicting changes remain blocked |
| E08 | A-BE and A-FE run permitted unit/type/build checks in sandbox | Worker-supplied raw artifacts, not authoritative QA verdict | Repair in isolated workspace |
| E09 | A-FE submits PR-UI and A-BE submits PR-API; each carries handoff packet | `candidate.submitted` with exact SHA, test commands and limits | Missing evidence → incomplete candidate |
| E10 | A-REVIEW independently checks authenticated test executions and runs adversarial cross-tenant tests | Exact SHA-bound verdict; suppose first review fails AC-02 | Fail only affected task, preserve failures |
| E11 | A-REPAIR receives bounded failure packet, fixes missing server-side authorization on new attempt | New source SHA and retest request, no retroactive reuse of old-green result | Escalate after allowed retries |
| E12 | Independent QA now passes fixes under fictional oracle assumptions | `candidate.verified` for exact source/test context | If check fails, no merge |
| E13 | S-MERGE constructs speculative combined result against current main; merge-group integration tests run | Verdict bound to actual proposed merge-group SHA | Base changes → regenerate affected tests |
| E14 | S-POLICY checks independent review, permissions, cost, branch protections and current acceptance revision | `admission.allowed` iff all gates pass | Deny, hold or return to repair |
| E15 | S-MERGE performs approved protected merge; S-LEDGER reads actual mainline SHA | `integrated` only after observed merge and successful required verification | Crash → reconcile actual Git ref, don't blindly merge again |
| E16 | A-REVIEW performs final isolated staging verification and injected defect repair exercise | `staging_verified` only if all AC-01..AC-09 pass | Corrective PR back through same gate |
| E17 | H-OWNER receives concise briefing with product walkthrough, risk, cost and release implications | `release_approval.requested`; **not** published | Human may decline or request changes |
| E18 | No actual human approval is given in this tabletop | `release.not_authorized`, `impact.unverified` | Never infer approval from silence |

### Critical separation

- Agent saying "done" ≠ independent reviewer asserting supported criterion.
- Verified PR ≠ tested combined mainline.
- Merge on main ≠ deployed staging.
- Staging tests ≠ permission to release.
- Published app ≠ demonstrated value to intended collective.
- Human approval is not proof of software safety; technical gates remain necessary.

## Compact illustrative event records (not validated schemas)

```json
{"type":"objective_approval","objective_id":"OBJ-DEMO","revision":3,"actor":"H-OWNER","scope":"disposable-only","granted_actions":["draft","sandbox_test","open_pr"],"release_authorized":false,"policy_revision":"P1"}
{"type":"task_attempt_started","task_id":"T-BE","task_revision":2,"attempt_id":"ATT-7","actor":"A-BE","grant_id":"G-7","lease_epoch":4,"expected_branch_head":"EXAMPLE_BASE","budget_cap":"fictional"}
{"type":"candidate_submitted","task_id":"T-BE","attempt_id":"ATT-7","source_sha":"EXAMPLE_SOURCE","acceptance_revision":3,"evidence_refs":["test-report-01"],"verification":"UNVERIFIED"}
{"type":"qa_verdict","candidate_id":"C-BE","reviewer":"A-REVIEW","independent_policy_check":"REQUIRED","tested_sha":"EXAMPLE_SOURCE","criterion":"AC-02","verdict":"FAIL","reason":"cross-tenant access"}
{"type":"candidate_revised","candidate_id":"C-BE","old_sha":"EXAMPLE_SOURCE","new_sha":"EXAMPLE_FIXED","invalidate_checks":true}
{"type":"integration_admission","candidate_id":"C-BE","checked_merge_group_sha":"EXAMPLE_GROUP","policy_revision":"P1","controller":"S-MERGE","decision":"CONDITIONAL_ON_ALL_REQUIRED_GATES"}
{"type":"release_status","objective_id":"OBJ-DEMO","status":"NOT_AUTHORIZED","actor":"S-LEDGER"}
```

Placeholder SHAs are deliberate and **must never be treated as actual hashes or security evidence**. In a real implementation events need trusted authentication, canonical serialization, revision checks, authorization, schema validation and durable reconciliation.

## Comparison using identical requirements

| Cohort | Work partition | Potential advantage | Failure pressure to test |
|---|---|---|---|
| 1 AI builder + external QA | One long context owns full code | Less handoff/contract conflict | Context drift, sequential latency, self-review bias |
| 3 AI workers + external QA | Architect/coordinator, frontend, backend | Parallel UI and persistence | API drift, duplicated fixes, coordination cost |
| 8 AI workers + external QA | More specialists: design, data, auth, UI, QA support, reliability, etc. | Parallel narrow work | Queue saturation, duplicate tasks, integration invalidations |
| Adaptive 1→3→8 + external QA | Recruit only if observable blockers justify | Potential lower cost for equivalent quality | Incorrect staffing decisions; scaling overhead |

**Fairness:** Include independent QA, policy, CI, human review time and all repair costs in **every** cohort. If the solo cohort also uses external review, don't mislabel it "literally one agent in the entire system." Hold product specification, acceptance tests, cost ceiling and environment constant.

### Staffing/parallelism triggers to test (hypotheses)

- Expand 1→3 if ≥2 truly independent implementation slices remain after API contract is frozen, *and* expected critical-path reduction outweighs setup/handoff cost.
- Expand 3→8 only if pending independently verifiable work is sufficient, QA queue is not saturated, and source churn/conflicts stay within cost ceiling.
- Contract back to repair-focused team if stale tests, blocker age or failed batches exceed predefined thresholds.
- Escalate to human if risk, privacy, contractual or architecture ambiguity cannot be resolved under approved objectives.

No threshold numbers are validated yet. These are hypotheses to preregister before a trial, not current Foromni automation rules.

## Evaluation metrics

- AC-01..AC-09 pass rate on independent staging verification; AC-10 release authorization separate.
- Time and total cost from approved objective to first genuinely integrated, independently checked vertical slice.
- Change conflicts, stale tests, duplicated task attempts, unsafe privilege requests and regression escapes.
- Human time spent on necessary approvals, emergency interventions and decision corrections.
- Handoff completeness: can a different agent reproduce test and safely continue?
- Recoverability after one worker/provider disappearance and a controller crash.
- Cost per **verified integrated feature** and cost per **staging-verified product**, not number of prompts or generated branches.
- Maintainability based on fresh reviewer modifying one accepted feature with tests.

## Adversarial variants to add

1. Product request lacks a crucial tenancy requirement; agent must escalate instead of inventing permissive defaults.
2. Frontend and backend both pass their own checks but disagree on the API.
3. QA agent is controlled by same principal as the implementer; independence check rejects it.
4. Main advances after green check; old merge-group result cannot authorize new state.
5. An agent tries to upgrade its own grant to mainline write; deterministic gateway denies.
6. Repair agent gets obsolete task revision after a requirements change; new work waits for re-scoping.
7. Build passes but end-to-end tests reveal shared-user data leakage.
8. Worker loops on same bug beyond retry budget; cost steward stops retries.
9. Model provider fails mid-task; replacement uses sanitized checkpoint and revalidates lease.
10. Founder declines publication; staged work remains preserved but not released.

## Research conclusion

The testable unit is **one independently verified vertical slice of useful full-stack behavior**. Natural-language intent may drive autonomous agents from planning to candidate integration, but evidence and credentials—not a chief-agent confidence score—determine which transitions occur.

**Next:** Convert the event examples to formal JSON Schema and an independent deterministic decision oracle; compare source-level candidate components (agent SDK, task orchestrator, merge gate), then propose a small disposable controlled trial for separate Founder authorization.

*Build today, so others can enjoy tomorrow.*
