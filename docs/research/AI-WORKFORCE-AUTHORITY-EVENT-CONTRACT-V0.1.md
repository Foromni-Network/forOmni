# AI Workforce Authority and Event Contract v0.1 (Research Proposal)

**Research-only, unimplemented** · 2026-11-21 · Foromni only · No IE modification or production changes.  
**Paired with:** AI-OPERATED-AINO-OVERSIGHT-MODEL.md, CONVERGENCE-CONTRACT-V0.1.md and CROSS-DOMAIN-CONVERGENCE-CONTRACT-V0.2.md.

## Purpose

Specify the *minimum machine-readable coordination semantics* required for **AI-operated work**, not merely a human-owned issue tracker. An AI supervisor and workers may plan, assign, implement, checkpoint, request reviews and propose integrations; a deterministic trusted authority independently enforces grants, concurrency, budgets and protected gates. Humans configure policy, approve consequential changes, and may revoke rights.

The examples are **illustrative JSON**, not executable schemas or authenticated messages. Do not import these into a runtime or grant privileges based on their declared fields.

## 1. Typed entities

- **Objective:** approved intent, policy version, project boundary, success criteria, spend limit and prohibited actions.
- **Agent principal:** authenticated accountable operator/organization, agent instance ID, permitted capabilities. Model/provider identifier is descriptive only.
- **Delegation grant:** `grant_id`, granter, grantee, project/task scope, allowed action set, environment, expiry, budgets, delegation depth and revocation epoch.
- **Task attempt:** immutable `attempt_id`, task/outcome version, assigned principal, bounded lease/fencing token, checkpoint and current progress.
- **Proposed action:** exact tool operation, argument/resource digest, authorization intent, irreversible flag and idempotency key.
- **Policy decision:** allow/deny/require_human, effective scope, reason and `policy_revision`; authenticated by trusted policy service, not an LLM.
- **Evidence event:** artifact digest, source revision, check run, independently observed result, verification scope and limitations.
- **Review verdict:** reviewer authority and separation-of-duties proof, exact candidate revision and independently verified acceptance.
- **Integration event:** merge group, checked result, authorized controller, observed final mainline SHA and post-merge verification.
- **Human intervention event:** question requiring accountable approval, cost/risk rationale, bounded approval options and expiry.
- **Audit event:** append/protect according to privacy/retention policy; privacy rights may require deletion/redaction of personal content.

## 2. Example machine-readable delegation (NOT a valid grant)

```json
{
  "contract": "foromni.ai-workforce.v0.1-proposal",
  "event_type": "delegation_requested",
  "event_id": "evt-demo-0001",
  "objective_id": "obj-demo-0001",
  "task_id": "task-demo-0001",
  "task_revision": 2,
  "actor_id": "collective/agent-supervisor",
  "proposed_grantee": "collective/agent-coder-04",
  "actions": [
    "read_scoped_source",
    "write_isolated_candidate",
    "run_disposable_tests",
    "submit_review_request"
  ],
  "resources": ["repo:foromni-example", "ref:work/task-demo-0001/*"],
  "environment": "disposable_sandbox",
  "expires_at": "2026-11-22T00:00:00Z",
  "max_spend_usd": 2,
  "delegation_depth": 0,
  "policy_revision": "P3",
  "status": "PENDING_TRUSTED_POLICY_DECISION"
}
```

A request is not an effective credential. A grant is activated only by the trusted policy/identity service, with independently authenticated principal and on-action enforcement. A legitimate grant would be cryptographically/authentically bound to identity and exact resources; the demonstration fields are insufficient as security.

## 3. Agent action decision sequence

```text
Agent proposes a tool action
    ↓
Trusted gateway authenticates effective actor and grant
    ↓
Verify task/attempt revision, lease epoch, target resource, allowed action,
environment, budget, current policy, expiry, approval requirement
    ↓
DENY / REQUIRE_HUMAN / ALLOW
    ↓
If ALLOW: perform under narrow runtime credential + idempotency key
    ↓
Observe external result independently; commit event tied to actual system state
    ↓
On uncertainty: reconcile rather than blindly retry
```

Fail closed for protected/irreversible actions. Harmless draft computations may proceed while a separate approval is pending. Never rely on the prompt alone for restricting tool access.

## 4. Event envelope and projection invariants

Every state-changing event has:
- `event_id`, globally stable within namespace;
- `aggregate_type` + `aggregate_id`;
- `expected_aggregate_revision` and new revision after authorized commit;
- `occurred_at` (worker assertion), `observed_at` (trusted observation);
- authenticated `actor_id`, `grant_id` and policy version;
- `attempt_id` / current lease epoch when worker-owned;
- idempotency key and causation/correlation IDs;
- semantic action type, scoped resource ref and digest;
- decision/result status with reason and evidence references;
- privacy classification and retention applicability.

Reducer rules:
1. Duplicate event IDs/idempotency keys are applied once; conflicting payload under same key fails.
2. Task revisions and effective leases reject stale attempts.
3. Events from untrusted providers do not directly raise trusted acceptance state.
4. Separate execution, verification, integration, release and real-world outcome axes.
5. If a protected Git ref changed but local ledger did not record it, reconcile from external ref/PR history.
6. Cross-collective state changes require separate scope/permissions; no ambient federation.
7. An event may be superseded, corrected or redacted under policy; never silently fabricate history.

## 5. Risk-based autonomy matrix (proposal)

| Action | AI autonomous? | Enforcement |
|---|---|---|
| Suggest task breakdown and estimates | Yes, within approved objective | Versioned draft, no automatic scope expansion |
| Edit isolated task branch | Yes, with scoped grant | Current attempt, branch ACL, lease and budget |
| Run disposable unit/integration tests | Yes, constrained | Sandbox and network controls |
| Submit candidate PR and evidence | Yes | Readback, immutable artifacts, current SHA |
| Self-certify completion | No | Separate independent QA |
| Re-run failed test / small repair | Yes, within retry/time budget | Deterministic caps and blocker escalation |
| Merge protected main | Only gated service under explicitly approved policy; not arbitrary worker | Branch protection, exact merge-group checks, admission record |
| Publish to users or production | Human or legally accountable explicit decision when consequential | Time-bound approval and audited action |
| Change access, spend materially, publish sensitive info, enter contracts | Human approval according to risk policy | Hard policy gate, not prompt |
| Create subordinate agents | Only bounded delegation | Non-escalating privileges, no scope amplification |

## 6. One-versus-many agent organization tabletop

### Cohort 1: one autonomous builder
Given a scoped product brief, one agent plans, implements and fixes isolated code. Independent QA/controller remain separate infrastructure. Hypothesis: best for tightly coupled small product slices.

### Cohort 3: adaptive small studio
A coordinator agent delegates API/data and UX implementation to two isolated workers; a separate QA principal validates. Each worker gets task-specific branch and context; coordinator cannot merge merely because both agents report completion. Hypothesis: lower time-to-acceptance on cleanly separable slices if interface contract is fixed early.

### Cohort 8: broader autonomous studio
Specialists span requirements, design, backend, frontend, tests, accessibility, security and reliability; scheduler runs tasks with dependencies and limited QA capacity. Hypothesis: higher candidate throughput but potentially worse accepted integration/cost ratio without backpressure.

Use **same** versioned product brief, task success criteria, risk controls and objective budget across cohorts. Track human interventions, permission exceptions, merge conflicts, stale tests, queue latency, independent acceptance, true fully-loaded costs, time-to-integrated slice and maintenance effort. One generated demo is not evidence for broader superiority.

## 7. Failure tabletop cases

1. Chief agent tries to delegate production credentials -> deny privilege escalation.
2. Coding agent requests scope expansion to private unrelated repository -> deny.
3. Agent submits fabricated CI URL -> independently verify run identity/checked SHA.
4. QA agent is another model but same principal as coder -> reject independence if policy requires distinct control.
5. Agent restarts on expired lease and writes old branch -> deny authoritative mutation; preserve proposal.
6. QA passes but main changed before merge -> invalidate affected prospective merge test.
7. Model switches local→cloud with confidential data -> require data-transfer authorization or deny.
8. Two agents start the same costly task -> bound lease, queue idempotency and cost cap.
9. Budget exhausted mid-work -> pause execution; retain safe checkpoint and ask for authorized increase.
10. Founder approval delayed -> block only gated action; continue unrelated permitted work.
11. Controller crashes after protected merge -> read actual Git ref before retrying.
12. A natural-language founder brief asks for impossible/contradictory acceptance -> agent escalates a choice rather than silently redefine success.

## 8. Source and architecture notes

- OWASP agent security: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
- Microsoft zero-trust agent systems: https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems
- LangGraph interrupts and durable checkpoints: https://docs.langchain.com/oss/javascript/langgraph/interrupts
- A2A task handoff concepts: https://a2a-protocol.org/latest/specification/
- OpenHands SDK optional worker layer: https://github.com/OpenHands/software-agent-sdk

No external framework is mandatory and no current Foromni implementation is claimed. Actual security requires tested server-side authorization, independent IAM and restrictive token scopes—not descriptive JSON documents.

## 9. Next research gate

Formal JSON Schemas + deterministic decision-table fixtures for proposed actions, policy decisions and protected admission. Include one end-to-end trace from human product brief through agent implementation, independent QA, controlled integration and founder release approval. Only then decide whether an executable sandbox proof is justified.

**Principle:** Maximum safe autonomy inside bounded authority; minimum unnecessary human interruption; independently verified outcomes.

*Build today, so others can enjoy tomorrow.*
