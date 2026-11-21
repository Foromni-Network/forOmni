# FOR-007 — AINO Execution MVP Contract v1.0-RC1

**State:** **SPECIFICATION CANDIDATE FROZEN FOR REVIEW**. Not approved, independently reviewed, implemented, tested or released.  
**Date:** 2026-11-21 · **Scope:** Foromni only.  
**Change policy:** This version is immutable by convention after review handoff. Any material change creates v1.0-RC2 with a signed decision log and refreshed dependencies; no silent editorial modification may change test expectations. GitHub commit SHA of this document is the source identifier and must be pinned by the eventual independent reviewer.  
**Canonical roadmap task:** FOR-007.  
**Related existing docs:** `docs/architecture/MVP-DOMAIN-MODEL.md` (member/project/discovery concepts remain distinct); `docs/architecture/CAPABILITY-EXCHANGE-CONTRACT.md` (capability advertising is not execution authority); `ROADMAP.md`; `roadmap/tasks.json`.  
**Research inputs (not imported implementations):** Foromni research branch `research/global-agent-roadmap-execution`, H0-M/H0-S/H0-R local experiment summaries, sandbox studies and global contributor ADR. No IE implementation/data/credentials.

## 1. One end-to-end outcome and strict exclusions

**Required vertical slice:** An authenticated human custodian creates one synthetic coding task with immutable acceptance criteria, selects an enrolled logical agent, explicitly authorizes a bounded worker attempt, obtains an isolated patch, sees an independent observer reconstruct its Git SHA, receives independent evaluator evidence and full attempt accounting, then **accepts/rejects/requests repair**; task, worker, permissions, attempts, source and decisions remain queryable after restarting the application.

A **contribution accepted in the MVP** means the custodian accepted an independently verified **candidate**. It does **not** mean mainline merge, deployment, publication, release or a measured benefit to end users.

**In:** Foromni-only local CLI or minimal authenticated UI; one member/custodian; one test project; stable agent identity; task, lease, attempt, sandbox, patch, source SHA, QA verdict, human review, persistent evidence; restart and retry as new attempts; one qualified offline sandbox runner.

**Out:** live community signups, public profile discovery UI (existing FOR-004/FOR-005 track); general AI marketplace, agent reputation scores, multiple agents on one task, live cross-project federation, arbitrary GitHub writes, production integrations, automatic protected merges, deployment, network-dependent tools, persistent uncontrolled worker access, payments, tokenization, multiple orchestration engines, public hosting and Internet Embassy integrations.

**Future global-OSS compatibility:** externally submitted, untrusted patches must fit the same Candidate/Evidence interface; trust level is tracked by independently verified provenance, never inferred from popularity, provider choice, location or contributor self-description. Different models and worker operating systems must not change acceptance semantics. New community participation is FOR-016, not FOR-007.

## 2. Authoritative entities (normative minimum)

Every record has a stable opaque identifier, `schema_version`, UTC timestamp and immutable creation provenance; write operations require authenticated authorization and recorded audit outcomes. These objects are conceptually distinct even if the first implementation uses one database or few tables.

| Entity | Required fields (minimum) | Immutable/core rule |
|---|---|---|
| **Member** | `member_id`, `auth_subject`, `display_label`, `status` | Private auth binding separate from public display; owner must be authenticated |
| **Project** | `project_id`, `owner_member_id`, `visibility`, `revision` | All tasks and access are project-scoped; synthetic-only initial project |
| **AgentDefinition** | `agent_id`, `owner_member_id`, `capabilities`, `adapter_type`, `status` | Logical agent identity is stable and is not the provider API key |
| **AgentIncarnation** | `incarnation_id`, `agent_id`, `runtime_ref`, `created_at` | Each execution session gets a new incarnation, not a new logical agent |
| **Task** | `task_id`, `project_id`, `owner_member_id`, `revision`, `base_sha`, `allowed_paths`, `acceptance_ref`, `dependencies`, `admission_state` | Requirement revision is frozen for each attempt; task admission state is not worker state |
| **Lease** | `lease_id`, `task_id`, `task_revision`, `agent_id`, `incarnation_id`, `scope`, `expires_at`, `fencing_epoch`, `budget_ref`, `grant_ref`, `status` | Trusted controller issues; no worker-minted grants; action-time checks; no shared write lease |
| **Sandbox** | `sandbox_id`, `lease_id`, `runner_name`, `runtime_digest`, `effective_policy_digest`, `status`, `teardown_evidence_ref` | Disposable; limits and isolation must be measured; instance is not an authority |
| **Attempt** | `attempt_id`, `task_id`, `lease_id`, `incarnation_id`, `base_sha`, `started_at`, `ended_at?`, `execution_state`, `failure_reason?` | Every retry is a distinct attempt and is counted, including failures |
| **Candidate** | `candidate_id`, `attempt_id`, `patch_digest`, `base_sha`, `observed_candidate_sha`, `source_observer_id`, `source_status` | Candidate SHA derived from independently reconstructed clean Git source; worker claim is untrusted |
| **Evidence** | `evidence_id`, `candidate_id`, `evaluator_principal`, `evaluated_sha`, `suite_digest`, `environment_digest`, `positive_required`, `positive_executed`, `negative_required`, `negative_executed`, `case_results_ref`, `security_tags`, `primary_grade`, `cost_completeness` | QA principal and protected suite/results separate from worker; actual test executions observed |
| **Decision** | `decision_id`, `task_id`, `task_revision`, `candidate_id`, `evidence_id`, `actor_member_id`, `decision`, `reason`, `at` | Human approval is attributed and never confers merge/release authority automatically |
| **OperationEvent** | `operation_id`, `authenticated_actor`, `action`, `scope`, `task_revision`, `decision`, `observed_effect`, `timestamp` | Append-only audit of relevant trust-changing actions; missing acknowledgment is UNKNOWN |
| **CostRecord** | `attempt_id`, `category`, `amount_or_unknown`, `currency`, `source_ref`, `reconciliation_state` | Include model, host, tool, tests, retries and human review; unknown is not zero |

Private security-sensitive fields, credentials, secrets and sealed evaluation cases stay out of public member, task and contribution projections. Minimum `visibility` may be `private` or `public` by explicit owner choice; in first execution MVP only synthetic private work is permitted.

## 3. State machines: deliberately do not reuse one ambiguous "complete"

**Task admission:** `draft -> ready -> leased -> candidate_submitted -> evaluating -> review_required -> accepted_candidate | rejected_candidate | repair_requested | cancelled`. After `repair_requested` or `rejected_candidate`, a new attempt is created from a current approved revision; never mutate a historical attempt to overwrite evidence. An accepted candidate is terminal for that revision and does not mean integrated.

**Attempt execution:** `allocated -> running -> candidate_submitted | failed | timed_out | revoked | cancelled | unknown`. Execution progress is not roadmap/task acceptance.

**Lease:** `issued -> active -> expired | revoked | consumed`. A lease can become invalid while worker is running; controller must recheck authoritative validity at every privileged action. Epochs prevent stale holder writes.

**Sandbox:** `provisioning -> ready -> running -> stopping -> destroyed`, with independent `provision_failed` / `cleanup_failed` statuses and teardown evidence. An unsafe or unknown setup never transitions to ready.

**Source evaluation:** `not_observed -> reconstructed -> verified | invalid_patch | stale_source | unknown`.

**Independent QA:** `not_run -> running -> verified_accepted_for_candidate | verified_rejected | incomplete | invalid_patch | no_test_execution | stale_evidence | infra_error | unknown_or_ambiguous | security_blocked`. Grade naming is **candidate-scoped**. Proposed E0 schema and earlier grade docs are research inputs, not automatically accepted MVP public API values; final exact grade codes require QA-owner review. In implementation, a single fixed mapping must be pinned; never silently alias incompatible grades.

**Human decision:** `accept_candidate | reject_candidate | request_repair`; only authorized human member may write. No merge/deploy action in this MVP surface.

**Events:** all transitions carry prior/current state, version, actor, timestamp, reason and correlation/attempt. Invalid, stale or unauthorized transitions fail without side effects. Append-only authoritative audit must distinguish observed success from unknown outcome after a lost acknowledgment.

## 4. Minimum operations and error contract (transport neutral)

The first implementation may use CLI commands or authenticated internal API. Every mutation checks project ownership, expected revision, current lease, scope and action-time policy. Never place privileged GitHub tokens into a worker environment.

| Command | Actor | Outcome |
|---|---|---|
| `project.create` | Human custodian | Synthetic project ID and owner |
| `agent.register` | Human custodian | Stable logical agent ID |
| `task.create` / `task.read` | Human custodian; viewer with grant | Accepted task spec/revision, allowed paths, QA requirements |
| `task.assign` | Human custodian/controller | Agent/attempt draft with immutable revision |
| `lease.issue` / `lease.revoke` | Trusted controller with human authorization | Scoped, expiring lease and current fencing epoch |
| `sandbox.start` / `sandbox.stop` | Trusted dispatcher/supervisor | Observed policy digest and teardown proof |
| `attempt.submit_patch` | Assigned worker via bounded artifact channel | Untrusted patch artifact; no verdict |
| `candidate.reconstruct` | Independent source observer | Clean candidate SHA or explicit source rejection |
| `qa.evaluate` | Independently authenticated evaluator | Actual positive/negative case evidence and one primary grade |
| `decision.record` | Human custodian | Accept/reject/repair linked to exact candidate and QA evidence |
| `history.read` | Authorized member/reviewer | Task/agent attempts, evidence, audit, full cost and limitations |

Required error classes: `UNAUTHENTICATED`, `FORBIDDEN`, `NOT_FOUND` (privacy-preserving when needed), `STALE_REVISION`, `LEASE_EXPIRED`, `SCOPE_DENIED`, `INVALID_PATCH`, `EVIDENCE_MISSING`, `ENVIRONMENT_UNVERIFIED`, `BUDGET_EXCEEDED`, `UNKNOWN_EFFECT`. Each returns no privileged data and never silently falls back to unsandboxed execution. Transport-specific HTTP codes are deferred until implementation API choice; no extra endpoints are implied.

## 5. Threat model and security invariants

- **Untrusted inputs:** worker prompts, model outputs, repository READMEs, dependency scripts, patches, process stdout/stderr, external contributor artifacts and self-reported agent telemetry.
- **Trusted authorities:** authenticated project custodian (scope/decision), task policy controller (lease), sandbox supervisor (enforcement), source observer (SHA) and independent evaluator (test evidence). These authorities may share a human operator initially but **must not share worker-writable security material**; human same-operator review is not automatically independent validation.
- **Denied paths:** IE/production systems, host home, host Docker/systemd/SSH sockets, secrets, master model/GitHub tokens, evaluator fixtures and results, unrestricted network and any writable `.git` that could affect authoritative source.
- **H0-A sandbox requirements:** separately authorized runner with proven filesystem/network/IPC/process/syscall/resource/credential controls, failed setup and teardown reported, no unverified fallback. A working namespace alone is insufficient.
- **Patch custody:** worker only writes its disposable scratch and emits patch; source observer verifies allowed paths and reconstructs against approved immutable base. SHA mismatch invalidates old grades.
- **Independent QA:** separately owned fixture/test suite, real execution evidence, positive *and* negative mandatory tests, false-PASS rejection, no test-count substitution; exact candidate SHA.
- **Approvals:** human decision is independent from worker claim; high-risk source-host write, integration, deployment and additional spending require separate authorization, even after `accept_candidate`.
- **Privacy/community:** future globally distributed contributors may submit external untrusted source artifacts without requiring Foromni-controlled compute; public discovery entities are not default authority grants.
- **Failure behavior:** unknown side effect -> stop and reconcile by independent readback; never auto-retry a Git/main write or sensitive action after ambiguous acknowledgment.

## 6. One scientific MVP acceptance matrix (to be independently executed)

| ID | Testable criterion | Expected safe outcome |
|---|---|---|
| MVP-01 | Create project/task and register stable agent; restart service | Correct scoped records survive and agent ID remains stable |
| MVP-02 | Assign task to one incarnation, issue expiring fenced lease | Only that scoped incarnation/attempt is eligible for execution |
| MVP-03 | Expired, revoked, stale-epoch or out-of-scope lease used | Action refused; no authoritative state change |
| MVP-04 | Start runner with invalid/missing security control | No worker execution; explicit failure evidence |
| MVP-05 | Worker attempts read hidden QA secret or host credential | Denied and independently observed; secret digest unchanged |
| MVP-06 | Worker attempts network/GitHub write or forbidden filesystem edit | Denied by host/permission boundary; no production effect |
| MVP-07 | Correct code patch submitted | Observer reconstructs correct clean SHA; evaluator runs required cases; candidate eligible for human review |
| MVP-08 | Wrong code prints forged PASS | Rejected on actual evaluator cases; stdout not grading authority |
| MVP-09 | Patch stale base, modifies tests or changes after grading | Invalid/stale and cannot inherit earlier acceptance |
| MVP-10 | Evaluator missing mandatory tests or crashes | No verified acceptance; full failure/unknown record |
| MVP-11 | Human accepts an independently verified candidate | Decision linked to exact candidate/evidence; no merge/deploy automatically |
| MVP-12 | Human rejects/requests repair, agent retries | New attempt linked, prior evidence retained, full cost denominator includes failures |
| MVP-13 | Concurrent stale revision or duplicate operation | Conflict/unknown audited without uncontrolled duplicate side effects |
| MVP-14 | Model/provider or runner cost not reconciled | Mark incomplete cost; never report unknown as $0 |
| MVP-15 | New member/contributor submits patch without trusted host grant | Source untrusted until rebuilt/tested; no automatic elevated permissions |
| MVP-16 | Recreate environment from pinned dependencies and source | Same mandatory acceptance workflow reproducible, with limitations disclosed |

**Passing rule:** No MVP is declared accepted if MVP-01..14 and MVP-16 lack independent observed evidence. MVP-15 is a forward-compatibility contract review and belongs to external pilot FOR-016 for actual remote execution. Record each `pass | fail | not_run | unknown | infra_blocked` on exact accepted SHA; not-run is never pass. At least one correct and one deliberately incorrect real coding attempt must be independently evaluated. Repetition counts and cost thresholds are to be preregistered before experiment execution, not invented retroactively.

## 7. Evidence-to-release gate and dependencies

| Roadmap task | Product deliverable | Prerequisite |
|---|---|---|
| FOR-007 | Approved/pinned execution MVP contract | Independent reviewer explicitly signs RC and accepted SHA |
| FOR-008 | One admitted secure sandbox runner | FOR-007 and separately authorized safe R1 |
| FOR-009 | Persistent agent/task/attempt storage and lease authority | FOR-002 and FOR-007 |
| FOR-010 | One real AI worker outputs patch | FOR-008 + FOR-009 |
| FOR-011 | Trusted source observer / independent QA | FOR-007 + FOR-008 |
| FOR-012 | Evidence ledger + full attempt economics | FOR-009 + FOR-011 |
| FOR-013 | Human intake and acceptance CLI/UI | FOR-009 + FOR-011 + FOR-012 |
| FOR-014 | Independent end-to-end MVP validation | FOR-010..013 |
| FOR-015 | Protected source integration and release readiness | FOR-001, FOR-002, FOR-014; separately controlled release |
| FOR-016 | Outside community contribution pilot | FOR-015 and FOR-004 |

**Founder controls remain effective:** no CI/tests/merges/deployments unless separately approved; creating this specification is not an experiment authorization. No Foromni-main change implied. Existing `FOR-004/005` discovery track remains intact.

## 8. Independent reviewer freeze record — intentionally incomplete

| Gate | Decision | Evidence needed |
|---|---|---|
| Contract scope and exclusions | **AWAITING REVIEW** | Authenticated reviewer and founder sign off on one authoritative RC SHA |
| Identity/data ownership | **AWAITING REVIEW** | Confirm Member/Project/Agent role boundaries and no overlap with discovery MVP |
| Task state and lease semantics | **AWAITING REVIEW** | Review invalid transitions, fencing epoch, expiry and lost ACK |
| Sandbox admission and teardown | **AWAITING REVIEW** | Host-enforced profile, candidate runner and stop/unknown behavior |
| SHA custody and independent QA | **AWAITING REVIEW** | QA owner and validated positive/negative case inventory |
| Economic accounting | **AWAITING REVIEW** | Cost completeness, retries and human time methodology |
| Security, privacy and global OSS | **AWAITING REVIEW** | Cross-tenant and contribution model constraints |
| Release-governance boundary | **AWAITING REVIEW** | Explicit candidate vs integrated vs released semantics |

**Freeze definition:** `FOR-007` may advance to `ready` only when independent reviewer/founder record **APPROVED** with the exact Git commit SHA and accepted requirements, or return `review` with revisions requested. Document publication alone is not acceptance, and downstream tasks may prepare interfaces but cannot claim approved dependency closure.

*Build today, so others can enjoy tomorrow.* ❤️🐂
