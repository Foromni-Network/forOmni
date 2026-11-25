# Convergence Controller — Freshness, Reassessment and Action-Time Decision Rules

**Status:** RESEARCH SPECIFICATION ONLY; not an executable policy service, installed controller, or permission grant.  
**Date:** 2026-11-21 · **Scope:** Foromni only, no Internet Embassy changes.  
**Continuity:** CONVERGENCE-READINESS-RUBRIC-V0.1.md; CONVERGENCE-FIRST-CONTROLLER-ARCHITECTURE.md; AI-WORKFORCE-AUTHORITY-EVENT-CONTRACT-V0.1.md.

## Design question

What should happen when autonomous worker A is implementing a task, and autonomous worker B changes main, an interface, a task requirement, ownership, or the worker's grant? A convergence-aware *preflight* is a snapshot of permitted assumptions, not a permanent approval. Yet redoing every test and restarting every worker after any main commit would destroy throughput.

**Proposal:** preserve local work, recompute only what can be shown to be affected, and always recheck privileged actions against authoritative current state. Do not infer independence merely from different filenames or a model's judgment.

## Readiness is not permission

Maintain **three separate outputs**:
1. `readiness`—enough current information to implement safely?
2. `allowed_action_classes`—which specific scoped operations can this authenticated worker execute under its current effective grant?
3. `admission`—is a submitted candidate independently verified and allowed to enter the protected target ref **now**?

A task can be `REPAIRABLE` while contract negotiation is allowed and code affecting a blocked dependency is not. A packet can be `READY` while the worker still lacks the right to run tests on a new network or to merge main.

## Minimal freshness tuple (illustrative)

```json
{
  "packet_revision": 4,
  "observed": {
    "task_revision": 3,
    "acceptance_digest": "sha256:EXAMPLE_NOT_VALID",
    "main_oid": "EXAMPLE_NOT_A_GIT_OID",
    "dependency_revisions": {"API-TASK": 7},
    "interface_digests": {"GET /members": "sha256:EXAMPLE"},
    "policy_revision": "P-6",
    "grant_id": "G-7",
    "grant_epoch": 2,
    "lease_epoch": 8,
    "test_plan_revision": 5
  },
  "allowed_actions": ["isolated_draft", "submit_candidate"],
  "merge_allowed": false,
  "observed_at": "2026-11-21T00:00:00Z"
}
```

This is neither a real attestation nor an authenticated capability. Actual implementation needs resource-specific version selectors, signed/authenticated actor identities and trusted readback from each source system. A TTL alone does not prove freshness.

## Invalidation and re-evaluation matrix

| Event observed | May continue autonomously | Must invalidate or reassess | Blocked until |
|---|---|---|---|
| Unrelated main commit, verified no relevant dependency effects | Isolated drafting and source-local tests | Merge-group integration evidence *on the new base*; conservatively recheck if impact inference is uncertain | Fresh protected admission checks |
| Main change touches owned module or shared runtime/API | Preserve branch draft, run permitted diagnostics | Source assumptions, interface compatibility, dependency graph, integration tests | Rebase/reconcile and independently verify |
| New API/schema contract revision | Continue unrelated tasks | Consumer/provider acceptance and dependent work packet | Versioned contract agreement and updated checks |
| Task acceptance criteria updated | Preserve attributable drafts | Readiness and acceptance plan; claims bound to old task revision | Authorized new task scope and QA requirements |
| Task ownership transferred | Read permitted history | Old attempt's authoritative writes and lease | New effective grant/lease and sanitized handoff |
| Grant revoked or narrower policy applies | Only operations still separately authorized by current policy | All prohibited tool calls immediately; previous packet cannot regrant | Trusted policy approves any new authority |
| Test/check on old source SHA arrives | Preserve old result as historical evidence | Candidate acceptance for newer source SHA | Exact current-source or prospective merge evidence |
| Independent QA reviewer revoked/has conflict | Work remains submitted | QA admission verdict affected by independence policy | Valid separate reviewer checks current evidence |
| Another agent merges prerequisite | Continue preparing dependent isolated work | Dependency preflight, applicable interface baseline and merge-group evidence | Prerequisite version observed, checks rerun as needed |
| Budget exhausted | Checkpoint and read-only authorized inspection | New spending/test executions | Updated explicit budget grant |
| Model/provider switch | Continue only if tool/data scope allows | Capability routing, privacy boundary, authenticated principal/grant | Verified alternate worker and permitted data path |
| CI outage or uncertain result | Isolated drafts and no-privilege repair | Any check requiring successful trusted run | Independently observed green on exact revision |
| Controller crashes after merge but before ledger event | No automatic repeat merge | Ledger projection against actual Git ref and merge event | Reconciliation with real mainline history |

**Conservative rule:** a change that cannot be proven unrelated to an acceptance gate is **possibly relevant**. The system may allow safe isolated work but cannot reuse old integration evidence solely to save compute.

## Action-time guard, not just preflight

For every privileged or authoritative operation, a trusted service verifies:
- authenticated worker/principal and delegation grant;
- project/repository, task/attempt, branch/ref and exact requested operation;
- effective expiry/revocation epoch and lease fencing;
- current task/acceptance and policy revision;
- budget/network/data rules;
- idempotency and expected resource revision;
- where protected merge is involved, valid current merge-group and independent review.

**Sequencing hazard:** checking a Git ref and writing it are two separate operations unless a supported server mechanism or single serialized trusted writer enforces the transition. A read-then-write race is not solved by putting a version string in JSON. GitHub native merge queue and required checks are preferred where they supply the actual guarantees.

## Proposed deterministic decision priorities

1. **DENY** forbidden/expired/revoked scope and unsafe sensitive operations; no repair can bypass.
2. **REQUIRE_OWNER_DECISION** for material changes to purpose, data rights, spend or release.
3. **BLOCK_DEPENDENCY** for work depending on an unmet/contradictory prerequisite or unresolved interface decision.
4. **RENEW_PACKET** when relevant observed versions are stale but original authority remains.
5. **REPAIR_PACKET** for incomplete scope, task handoff, evidence method, or noncritical metadata.
6. **ALLOW_SPECIFIED_ACTIONS** only when all relevant gates hold for those actions.
7. **INTEGRATE** only through separate current, protected admission checks.

The output must include per-action decisions and reason codes; **do not compress mixed outcomes into one green status**. For example, allowed: `read_scoped_repo`, `draft_api_proposal`; denied: `write_shared_schema`, `merge_protected_main`.

## Synthetic case: UI worker begins at M0, backend merges at M1

**Initial:** task UI-7 depends on API contract V2. Both agent packets refer to main M0. Backend branch proposes `displayName` field.

**Step 1:** UI worker drafts consumer against V2 in its own branch. Safe isolated progress is recorded.

**Step 2:** Backend is independently reviewed and merged to main M1; actual API contract is V3 and field is `name` (this divergence should itself have been detected by contract checks; use as adversarial scenario).

**Step 3:** Controller observes M1 and compares current interface digest to UI packet. Signals `INTERFACE_REVISION_CHANGED` and `BASE_SHA_STALE`. UI worker may retain work but is **not ready for admission**.

**Step 4:** AI coordinator proposes a versioned contract decision: adjust UI to V3, implement compatibility adapter under approved contract, or correct backend via new PR. It cannot unilaterally rewrite stakeholder acceptance.

**Step 5:** Authorized owner or preapproved architecture policy resolves the interface. UI worker renews packet, rebases/reconciles code and reruns independent consumer/provider/end-to-end checks on combined candidate.

**Step 6:** Protected merge gate verifies new source and latest prospective main result, merges if all checks pass, then reads actual SHA from Git. Staging/release remain separate.

**Failure to expose:** If all workers blindly trust the original M0 work packet, they may produce independently green but incompatible code.

## Research-specific acceptance tests

- Decision oracle always rejects revoked grant, stale lease, self-certified QA, unsigned/unknown main SHA and protected-merge bypass.
- Unrelated changes may keep safe local work alive while merge-group results are properly reassessed.
- Direct dependencies invalidate consumer/provider acceptance even when source files do not overlap.
- Changed acceptance policy cannot retroactively mark an old artifact complete.
- Invalidated checks cannot be resurrected through delayed/duplicate webhook events.
- Each proposal retains provenance and reason for repair, not silent data loss.
- Event replay resolves to same authorized state even after crash, barring explicit unresolved external observations.
- Outcome and release status remain distinct from integrated-source state.
- Overall throughput test counts full recheck/repair cost, not just time spent generating changes.

**No tests were executed; these are a draft oracle.**

## Research continuation

Next: formalize this matrix into revision-bound JSON Schemas plus an independent deterministic transition specification; then map which gates are actually enforceable by GitHub protections/queues, which require an external policy service, and which require human governance. Avoid introducing a new universal controller if an adapter layer over existing tools suffices.

*Build today, so others can enjoy tomorrow.*
