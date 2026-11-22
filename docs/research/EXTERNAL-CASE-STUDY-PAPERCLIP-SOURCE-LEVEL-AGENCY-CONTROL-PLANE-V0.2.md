# Paperclip Source-Level Audit — Agency Control Plane vs Foromni AINO v0.2

**Date:** 2026-11-22 UTC. **State:** READ-ONLY SOURCE ANALYSIS. No Paperclip installation, no tests executed, no copies of upstream implementation, no permission changes, no changes to frozen FOR-007.  
**Pinned upstream:** [paperclipai/paperclip@324ec1f537a9ba1e84239faa81bcef326a5dd1b7](https://github.com/paperclipai/paperclip/tree/324ec1f537a9ba1e84239faa81bcef326a5dd1b7) (MIT reported in public repo metadata; audit imported dependencies at any reuse decision).  
**Foromni target:** [FOR-007 v1.0-RC1](https://github.com/Foromni-Network/forOmni/blob/feat/repo-native-roadmap-system/docs/architecture/FOR-007-AINO-EXECUTION-MVP-CONTRACT-V1.0-RC1.md), roadmap FOR-009 (persistent registry), FOR-011 (independent QA), FOR-012 (evidence/cost), FOR-013 (human acceptance), FOR-016 (global community). This audit records integration hypotheses, not approval to change contract or implementation.

## Executive finding

Paperclip is the **closest organizational-control-plane reference** in the survey: it has modeled companies, hierarchical agents, issue checkout, budget policy and reservations, run scheduling/recovery, cost receipts, approval decisions and activity events. Its actual source is more sophisticated than a simple multi-agent chat system. However, no reviewed code establishes that a completed issue means independently reconstructed source SHA + separately authenticated evaluator + human candidate acceptance under Foromni's frozen release semantics. This is a **gap in evidence of compatibility**, not a claim that Paperclip entirely lacks these features.

**Convergence thesis:** Harvest five concrete **mechanisms**: transactional task claims; separately attributable runtime/run identities; budget reservations plus charge receipts; interrupt/recover lifecycle; explicit human approvals with audit. Preserve Foromni's different member/project ownership, future global open-source participants, independent verification and controlled integration.

## A. Task claims and concurrency — source evidence

**Source:** [issues.ts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/server/src/services/issues.ts) and [schema/issues.ts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/packages/db/src/schema/issues.ts).

- The issue service exposes `checkout(id, agentId, expectedStatuses, checkoutRunId, options)` around line **12837**, validates the assignable agent and uses database state checks to enforce assignment. This is more substantial than setting `status=in_progress` in a chat.
- Separate source paths around lines **8109–8240** require matching issue status, assignee agent ID and `checkoutRunId`; the code uses transactional row locks when adopting a running checkout. The exact concurrency guarantees and races must be tested, not assumed from this reading.
- The core-concepts documentation says simultaneous checkout conflict produces HTTP 409. [Paperclip core concepts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/docs/start/core-concepts.md).
- A single issue assignee is checked in issue updates; one assignee is not synonymous with one authorized sandbox or one permitted branch.

**Foromni design interpretation:** FOR-009 should represent `task_revision`, `attempt_id`, `lease_id`, `fencing_epoch` and `expected_checkout_run_id` separately. Require compare-and-swap or transactional claim with refusal of a second active writer, expired holder, and stale epoch. Never derive authority from an issue status or worker-supplied ID. Before importing code, demonstrate collision, crash and reassignment tests.

## B. Heartbeats, execution recovery, and lifecycle

**Sources:** [heartbeat.ts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/server/src/services/heartbeat.ts), [run-admission.ts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/server/src/services/heartbeat/run-admission.ts), [recovery.ts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/server/src/services/heartbeat/recovery.ts), [run-control.ts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/server/src/services/heartbeat/run-control.ts).

- Paperclip's heartbeat is an execution window, not a constantly resident autonomous employee; its documented wake triggers include assignment, schedule, comment, manual invocation and approval resolution.
- The code distinguishes existing run ownership, reattachment and recovery. `run-admission.ts` specifies claimable reasons `handed_over`, `owner_gone`, `lease_expired`; recovery/cleanup are distinct modules and include tests.
- The codebase contains extensive source-level recovery test files, but their presence **is not proof they passed in this audit or prevent all orphaned processes**.
- Reattach and recovery should retain attempt provenance rather than silently reclassifying an interrupted attempt as accepted.

**Foromni design interpretation:** H0 needs just a bounded one-shot execution and explicit stop/failure state, not full heartbeat scheduling. Preserve an adapter-friendly `incarnation_id`, `sandbox_id`, `lease_expiry`, `attempt_id` and observed teardown. Add periodic wake/recovery only when later repeated tasks justify it. Record missing process and lost acknowledgment as `unknown`, not `done`.

## C. Budget admission and cost accuracy

**Sources:** [budgets.ts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/server/src/services/budgets.ts), [costs.ts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/server/src/services/costs.ts), [budget-exposure.ts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/server/src/services/budget-exposure.ts).

- `hardStopReached()` in budgets.ts around line **256** compares precise observed spend to policy and additionally considers an explicit unpriced-usage blocking policy.
- `recheckAdmittedRunBudgetReadOnly()` around line **266** rechecks admitted runs while accounting for held reservations; code comments note avoiding lock inversion and double denying already reserved recoveries.
- `pauseAndCancelScopeForBudget()` around line **410** pauses scope and queues a durable cancellation/enforcement notification.
- `createCostEventInTransaction()` around line **65** in costs.ts checks idempotency key against receipt hash; a repeated key with changed receipt triggers conflict and cross-company attribution is checked.
- Budget *reservation* is not the same as actual usage receipt, and exact cents are not the same as unpriced usage. A budget stop may require reconciliation and process termination.

**Foromni design interpretation:** In FOR-012 distinguish `budget_cap`, `reserved_amount`, `observed_charge`, `unknown_unpriced_usage`, `cost_receipt_digest` and `budget_decision`. Include failed, cancelled, rejected and recovered attempts in the denominator. No price-less usage may be silently assigned $0. Require time/CPU/disk/test/human overhead even if no model token bill arrives. Do not assume provider telemetry is authentic without an independent accounting trust classification.

## D. Human approvals and audit

**Sources:** [approvals.ts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/server/src/services/approvals.ts), [activity-log.ts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/server/src/services/activity-log.ts).

- `decideHire` and `decide` around lines **182–205** route `approved` / `rejected` through a lifecycle/approval record, with user ID and note. Other paths support `revision_requested` and `cancelled` states.
- Source uses `writeApprovalChange()` and `notifyToolReviewChange()` to connect persisted approval changes and downstream notification.
- Activity logging covers approval decisions, budget incidents and other state changes; source includes redaction of details and attribution to a responsible user. Whether that redaction/attribution is sufficient for every community privacy model needs an independent audit.
- Hiring/strategy approval is not interchangeable with independent *code candidate acceptance*, and human confirmation is not a substitute for QA.

**Foromni design interpretation:** FOR-013 must pin `decision.actor_member_id`, exact `candidate_sha`, evaluator `evidence_id` and action scope. Record separate choices `accept_candidate | reject_candidate | request_repair`; no decision automatically grants merged/released status or elevated worker permissions. An invalid or stale approval must fail closed.

## E. Organizational structure vs global open-source community

**Sources:** [Paperclip core concepts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/docs/start/core-concepts.md); [agents.ts](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/server/src/services/agents.ts).

- Paperclip treats agent organization largely as a managerial **tree**; each employee has one manager except CEO. Company goals align issue work and budgets.
- Foromni will also host independent community members, agent providers, projects and outside organizations, with consented **graph relationships** rather than one universal supervisor hierarchy.
- A project custodian may authorize work on one project but has no ambient power over another. Ownership, attribution, visibility and federation are different relationships from employment/reporting.

**Foromni design interpretation:** Model managerial hierarchy as an optional project-specific relationship, not the fundamental authorization graph. Maintain explicit `member_id`, `project_id`, `agent_id`, `lease/grant`, `contribution_id` and `source/evidence` objects. Open contribution must remain available without hosting an untrusted contributor's code.

## F. Gap / mechanism register mapped to frozen MVP

| Foromni task | What Paperclip may teach | Source-backed observation | Necessary Foromni requirement | Decision |
|---|---|---|---|---|
| FOR-009 Agent/task registry | Issue checkout; matching agent/run ownership; recoverable runs | `issues.ts`, `run-admission.ts` | Fenced task lease tied to frozen revision and explicit project owner | **Pattern candidate** |
| FOR-010 One AI worker | Adapter/runs/heartbeat context | `heartbeat.ts` | Sandbox qualified independently; worker only submits patch | **Defer integration** |
| FOR-011 QA custody | No independent graded source workflow established in files inspected | Source search was scoped, not exhaustive | Separate SHA observer + sealed evaluator + fake PASS defense | **Foromni-owned** |
| FOR-012 Accounting | Hard stop, reservations, receipt idempotency | `budgets.ts`, `costs.ts` | Complete attempt costs incl. missing data and failures | **Pattern candidate** |
| FOR-013 Human review | Approval resolution and audit | `approvals.ts`, `activity-log.ts` | Exact candidate-bound human decision with no release privilege | **Pattern candidate** |
| FOR-014 E2E validation | Recovery/concurrency test cases | Existing test source paths observed | Real independent positive and negative acceptance suite | **Not demonstrated** |
| FOR-016 Open community | Teams and company goals | `core-concepts.md` | Cross-tenant privacy, BYO agents, attribution, portable candidate ingestion | **Not directly equivalent** |

## G. Future discriminating experiment proposals (NOT EXECUTED)

1. **PCL-01 Atomic claim:** Two authenticated agents race on one task; only one receives effective lease, both submissions remain auditable.
2. **PCL-02 Crash/reassign:** Worker disappears after claiming; another can take over only after revocation/expiry and new fencing epoch, stale attempt cannot mutate accepted state.
3. **PCL-03 Budget reservation:** Two concurrent attempts competing for a capped budget; combined admitted estimated/held spend cannot silently exceed policy.
4. **PCL-04 Cost idempotency:** Replay same cost event yields one charge, conflicting payload with same key is rejected, unknown provider price remains unknown.
5. **PCL-05 Human approval spoof:** Worker marks itself done/approved; evaluator and human acceptance stay unchanged.
6. **PCL-06 Cross-project:** Agent from one member/project cannot read other project's issue data or QA oracle without separate grant.
7. **PCL-07 Output provenance:** Worker reports success with incorrect patch; clean Git reconstruction + separate QA rejects it.
8. **PCL-08 Revocation:** Budget/human policy revokes in-flight work; new external effects cease and any uncertain effects are reconciled.

Run PCL only with frozen fixtures, independent observation and a separately authorized, secure execution context. They should be grouped with existing FOR-007 MVP-01..16/R1 tests rather than added as separate competing task IDs.

## Decision and integration boundary

**Recommended now:** Read and model Paperclip-style **atomic checkout + receipt-level accounting + approval event semantics** in the existing Foromni FOR-009/FOR-012/FOR-013 tasks. **Not recommended now:** vendoring Paperclip, hosting its services, introducing a CEO swarm, shipping a board UI or replacing FOR-007 objects. The primary blocker remains qualification of one secure sandbox and then a single source-bound real worker+independent QA loop.

**Research-only evidence:** Published upstream source paths at exact commit; no benchmark, runtime performance or independent security assertions. A source inspection can reveal an implementation pattern; it cannot prove its safety or operational suitability. No founder controls were changed.

*Build today, so others can enjoy tomorrow.* ❤️🐂
