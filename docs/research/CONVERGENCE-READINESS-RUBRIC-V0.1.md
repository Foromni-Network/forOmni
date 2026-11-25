# Convergence Readiness Rubric v0.1 — AI Worker Preflight and Repair

**Status:** Research specification only; not an executable validator, authorized grant, or deployed controller.  
**Date:** 2026-11-21. **Scope:** Foromni only. Do not access, synchronize or modify Internet Embassy.  
**Companions:** CONVERGENCE-FIRST-CONTROLLER-ARCHITECTURE.md; CONVERGENCE-CONTRACT-V0.1.md; AI-WORKFORCE-AUTHORITY-EVENT-CONTRACT-V0.1.md; SYNTHETIC-TEN-WORKER-CONVERGENCE-TRACE.md.

## Research objective

Make agents **convergence-aware before they develop**. The autonomous planner should deliver work packets that explicitly fit current repository reality, nearby agent tasks, interfaces, permissions and independently verifiable acceptance. A preflight checker distinguishes *ready*, *repairable*, *human decision required* and *invalid*. Do not require founder interaction for routine missing metadata, but do not let a planning model invent decision rights or fabricate approvals.

A readiness score may be useful for prioritizing repairs. **No numeric score overrides a hard safety gate.**

## 1. Seven gate families

| Gate | Must be established | Hard stop conditions | Autonomous repair possibilities |
|---|---|---|---|
| G1 Objective/acceptance | Authorized outcome, task revision, explicit observable acceptance and exclusions | No accountable owner; unapproved scope expansion; contradictory safety requirements | Draft criteria and request review of material ambiguity |
| G2 Repo/source truth | Target repository/ref, fresh observed base SHA, relevant architecture context | Untrusted or missing baseline; unauthorized repository | Re-fetch authorized metadata; regenerate packet |
| G3 Ownership/isolation | Stable task/attempt IDs, isolated branch/workspace, effective grant, lease if applicable | Overlapping exclusive authority, expired/revoked lease, direct main write permission for untrusted worker | Reassign isolated branch or reroute to coordinator |
| G4 Dependencies/interfaces | Current dependency graph, interface/schema version, migration/flag compatibility | Unsatisfied prerequisite without allowed incremental plan; contradictory interface contracts | Propose shared API/schema fixture, compatibility adapter, split smaller vertical slice |
| G5 Evidence/QA | Acceptance methods, version-bound tests, independent reviewer and gate policy | Self-verification offered as sole proof; impossible or missing critical security checks | Generate test plan, clarify independent verifier, add synthetic fixtures |
| G6 Risk/resources | Data classification, allowed tools/network, bounded costs/retries, rollback scope | Unauthorized external data transfer, production secrets, unapproved spend, irreversible action | Reduce tool/data scope, choose local model, request bounded permission |
| G7 Integration handoff | Expected target main, merge strategy, conflict/repair route, PR evidence manifest, actual merged SHA readback plan | No protected integration authority or proposed bypass of required checks | Supply manifest, queue instructions, handoff/reconciliation plan |

All checks must be evaluated against current authoritative evidence. Work packet declarations are claims until independently verified by the chosen Git and policy backends.

## 2. Preflight decision states

- `READY`: all hard gates satisfied for **the specified action scope and expiry**; doesn't mean completed or preapproved for merge.
- `REPAIRABLE`: ordinary missing/superseded metadata, incomplete test plan, or reconcilable dependency whose repair remains within approved authority. Agent may revise packet; recheck.
- `BLOCKED_DEPENDENCY`: required owner/artifact/interface isn't yet accepted; agent may perform unrelated permitted work, not dependent publication.
- `HUMAN_DECISION`: consequential project scope, security/privacy rights, financial approval, incompatible objectives, high-impact architecture or protected release authorization.
- `DENIED`: revoked/unauthorized action, attempted privilege escalation, forbidden data movement, or direct protected write outside policy.
- `STALE`: observed main/task/lease/interface changed after readiness; invalidate affected gates and recompute; avoid claiming earlier green is current.

A `READY` outcome is scoped and ephemeral, not a durable global badge. The work packet may still fail at independent QA or merge admission.

## 3. Proposed failure/reason codes

| Code | Class | Expected response |
|---|---|---|
| `OBJ_UNAPPROVED` | hard | Stop dispatch; obtain accountable approval |
| `ACCEPTANCE_UNTESTABLE` | repairable/decision | Draft measurable criterion or escalate |
| `BASE_SHA_STALE` | stale | Refetch main, recalculate affected plan/tests |
| `TASK_REVISION_STALE` | stale | Replay updates, renew packet |
| `DUPLICATE_ACTIVE_TASK` | repairable | Reuse or coordinate existing task; no silent duplicate |
| `BRANCH_OWNERSHIP_CONFLICT` | blocked | Allocate isolated attempt/ref and reconcile interface ownership |
| `LEASE_EXPIRED` | denied/stale | Fence write; preserve offline artifact as proposal |
| `DEPENDENCY_UNSATISFIED` | blocked | Wait or work on allowable prerequisite |
| `API_CONTRACT_MISMATCH` | repairable/decision | Negotiate versioned consumer/provider contract |
| `MIGRATION_INCOMPATIBLE` | hard | Require safe migration/rollback plan |
| `INDEPENDENT_QA_UNASSIGNED` | repairable | Allocate separate authorized verifier |
| `EVIDENCE_NOT_BOUND_TO_REVISION` | hard | Require checks on exact source/merge result |
| `GRANT_SCOPE_MISMATCH` | denied | Deny and request appropriately scoped grant |
| `DATA_BOUNDARY_VIOLATION` | denied | Prevent transfer, require new policy decision |
| `BUDGET_EXHAUSTED` | blocked/decision | Pause and ask for approved budget if needed |
| `PROTECTED_MERGE_BYPASS` | denied | Enforce repository rules |
| `RELEASE_NOT_AUTHORIZED` | denied | Staging allowed only where separately permitted |

These codes are proposals, not the actual statuses of any current Foromni service.

## 4. Conceptual work packet result

```json
{
  "schema": "foromni.convergence-readiness.v0.1-research",
  "task_id": "TASK-DEMO",
  "task_revision": 3,
  "attempt_id": "ATT-DEMO-2",
  "observed_target": {
    "repo": "fictional/repo",
    "ref": "refs/heads/main",
    "sha": "PLACEHOLDER_NOT_GIT_OID"
  },
  "gate_results": {
    "G1": "READY",
    "G2": "READY",
    "G3": "READY",
    "G4": "REPAIRABLE",
    "G5": "READY",
    "G6": "READY",
    "G7": "BLOCKED_DEPENDENCY"
  },
  "decision": "REPAIRABLE",
  "reasons": ["API_CONTRACT_MISMATCH", "DEPENDENCY_UNSATISFIED"],
  "recommended_actions": [
    "propose-api-contract-v4",
    "wait-for-required-schema-task"
  ],
  "effective_authority": "NONE_GRANTED_BY_THIS_RECORD",
  "valid_until": null
}
```

**Status caveat:** The aggregate `decision` above is an illustrative *remediation workflow state*, not global permission to work. A real evaluator must state allowed work classes separately: here, tasks dependent on the schema are blocked even though packet repair work is possible. Avoid treating a single summary status as overriding individual hard gates. Full SHA, signed/observed identities, policy revision, evidence integrity, idempotency and canonical serialization are required in implementation.

## 5. Worked example — two AI developers disagree before coding

**Founder objective (fictional):** "Add member profiles to an isolated collaborative app."

**Existing reality:** UI agent U proposes `GET /api/members` results with `displayName`; backend agent B proposes `name`; schema task S is not yet accepted; both agents otherwise have isolated branches and no main write permission.

### Reactive process — control condition

1. U builds UI assuming `displayName`; B implements API returning `name`.
2. Each branch may pass separate tests.
3. On integration, files merge cleanly but end-to-end profile display breaks.
4. QA rejects combined candidate, agents repair/retest, queue and CI budget consumed.

**This is a hypothetical teaching case.**

### Convergence-aware process — treatment condition

1. Planner reads objective, current approved task graph and target SHA.
2. Preflight identifies `API_CONTRACT_MISMATCH` plus `DEPENDENCY_UNSATISFIED`.
3. Planner drafts API contract revision `members-v4`; legitimate owner/architecture decision approves if required.
4. Independent consumer/provider expectations are generated and assigned to B and U.
5. U can build local mocked UI against the agreed version, B can implement compatible API; *neither gets integration admission until relevant prerequisites and independent checks pass*.
6. Workers submit bounded PRs, source- and version-bound evidence and handoff packets.
7. Separate QA validates both provider and consumer expectations and the combined result on current prospective main.
8. Protected merger records actual integrated SHA; later staging/release gates remain independent.

**Hypothesis:** Earlier coordination may reduce late rework, but the additional planning cost might outweigh benefits for some trivial changes. Run matched trials before claiming improvement.

## 6. Integration admission is a separate recheck

Ready-to-develop does **not** mean ready-to-merge. The post-development gate must independently re-observe: actual source SHA, refreshed main SHA, task/acceptance revision, grants, reviewer independence, dependency and merge-group result.

The merge queue may test speculative combinations of current base and queued changes; for GitHub Actions, required checks need the `merge_group` trigger where used. A preflight packet cannot replace those server-enforced checks.

## 7. Experiment plan — readiness rubric vs ordinary task prompt

**Question:** Does a convergence-aware preflight reduce *verified end-to-end integration cost and failure* rather than only make task tickets look more detailed?

- Use identical synthetic app requirements and risk/permission rules, 1/3/8 AI-worker cohorts.
- **Control:** standard task prompt + Git branches/PRs/CI; no special readiness rubric.
- **Treatment:** same base input and resources plus controller preflight and documented work packet; charge planner and additional tests to treatment.
- Freeze task set, objective criteria, independent QA and budgets before trials; rotate workload order and use repeated runs.
- Primary: independently verified integrated vertical slices per total cost, including agent planning, verification, merge reruns and human attention.
- Secondary: mismatched API detection timing, rework and branch conflict rate, wait time, task duplication, stale evidence, human escalations, regressions.
- Hard safety: unauthorized main writes, data leakage, false QA independence or fabricated evidence reject safety claims regardless of throughput.
- Record failed, inconclusive and negative experiments. No fabricated productivity percentage.

### Reviewer adversarial questions

- Did the treatment receive hidden requirements unavailable to the control?
- Are agents' model versions, tools and compute budgets matched?
- Can planner-generated false confidence bypass policy, QA or human approval?
- Does the rubric starve useful independent work while waiting on a minor prerequisite?
- Can a stale packet be replayed under a different task or repository?
- Can different agents claim exclusive file ownership without enforcement?
- Is independent QA actually outside the implementing actor's authority?
- Can late offline agents preserve contributions without mutating protected refs?
- Does the system penalize sophisticated work by excessively optimizing trivial PR throughput?
- Do human reviews concentrate on meaningful policy decisions rather than routine metadata?

## 8. Adopt / extend / reject components

**Adopt (candidate):** GitHub merge queue and protected checks for mainline; Pact-style consumer/provider checks for interface compatibility; short-lived and incremental integration patterns from trunk-based development; existing issue/task registry for task ownership.

**Extend:** cross-provider, revision-bound preflight packets; agent authority and dependency rules; persistent event/outcome ledger; preflight/merge validation linkage; repair workflow and ownership transparency.

**Reject initially:** build a new Git host, duplicate CI engine, untested universal planner, manual file-copy pipeline, self-declared green status or global agent root credentials.

Sources:
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
- https://docs.pact.io/getting_started/verifying_pacts
- https://trunkbaseddevelopment.com/

## 9. Research decisions for next milestone

1. Distinguish *readiness assessment* from *permission grant* in a formal schema.
2. Write a deterministic state-transition/reason-code decision table, including mixed `REPAIRABLE` and `BLOCKED_DEPENDENCY` cases.
3. Specify a freshness envelope: what changes invalidate only some gates, and what must always force reauthorization.
4. Document work-packet renewal/repair after another agent merges relevant source.
5. Compare rubric fields against actual open-source API support before proposing custom services.
6. Define a minimal **synthetic** demo fixture; no implementation until authorized.

**Conclusion:** A convergence controller is most useful when it prevents foreseeable incompatibilities *before* code is authored and then refuses unsupported claims at integration. It is an advisor at planning time and an enforceable evidence gate at publication time.

*Build today, so others can enjoy tomorrow.*
