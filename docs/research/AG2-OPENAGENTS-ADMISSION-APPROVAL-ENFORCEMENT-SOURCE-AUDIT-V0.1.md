# Foromni Federation Admission Enforcement — AG2 Invitation and OpenAgents Sharing Source Audit v0.1

**Date:** 2026-11-22 · **Scope:** Foromni research only · **Evidence grade:** source inspected, no execution/independent reproduction. No runtime, tests, production permissions, merges, deployments or frozen FOR-007 changes.  
**Relates to:** [FED-0 tabletop](FED-0-TWO-PROJECT-TWO-HUMAN-TWO-AGENT-ADMISSION-TABLETOP-V0.1.md), [Agent Trust Ladder](AGENT-TRUST-REPUTATION-CAPABILITY-ELIGIBILITY-AND-REVOCATION-V0.1.md), [Foromni workforce authority](AI-WORKFORCE-AUTHORITY-EVENT-CONTRACT-V0.1.md).

## What was actually read

| Evidence | Pinned Git source and Git blob | Direct observation |
|---|---|---|
| AG2-INV-01 | [AG2 core.py@9bdd9d4](https://github.com/ag2ai/ag2/blob/9bdd9d493a9a3a01308949b67d5a18219cb6c71c/ag2/network/hub/core.py), blob `32e1573e505ecc26d08dcd215a855031ce302dd4` | Channel creation stores `PENDING` metadata, `pending_acks` invitees, sends invite envelopes; self-only channels activate immediately; invite timeouts close with `invite_timeout`. `_handle_invite_ack` removes a matching pending invitee and activates only if none pending/rejected. `_handle_invite_reject` closes with `invite_rejected`. |
| AG2-INV-02 | [AG2 channel.py@9bdd9d4](https://github.com/ag2ai/ag2/blob/9bdd9d493a9a3a01308949b67d5a18219cb6c71c/ag2/network/channel.py), blob `4b79d33f026896d6ae878a7b67675ee089018e5b` | Versioned manifest/participant metadata, status states `PENDING ACTIVE CLOSING CLOSED EXPIRED`, snapshot manifest. |
| AG2-RISK-03 | [AG2 rule.py@9bdd9d4](https://github.com/ag2ai/ag2/blob/9bdd9d493a9a3a01308949b67d5a18219cb6c71c/ag2/network/rule.py), blob `fe89ad3f86688ca7aa0c827334bc1ed262a063a0` | The source explicitly says access channel-type restrictions and rate controls are stored but ignored by the in-process hub; defaults permissive. Valid invitation lifecycle alone is insufficient privileged-task admission. |
| OA-APP-01 | [OpenAgents agent_sharing_requests.py@93e3347](https://github.com/openagents-org/openagents/blob/93e334783747f6f35eb5133c0dec4351b7fffa10/workspace/backend/app/services/agent_sharing_requests.py), blob `1d642c954cbd290555157e858962c8b9960f7cc4` | Owner-reviewed thread-only or direct agent-sharing request. `resolve_request` denies non-owner decisions; on approval locks current agent row and rechecks owner, active agent, channel, requester and owner thread participation, and requester membership. Then creates resource-specific `read, act` grant. |
| OA-APP-02 | [OpenAgents approvals.py@93e3347](https://github.com/openagents-org/openagents/blob/93e334783747f6f35eb5133c0dec4351b7fffa10/workspace/backend/app/services/approvals.py), blob `14ed20244a232c4ca53955aa36bafd1d905238ee` | Approval resolution rejects non-pending items; records required-human approvals and partial decisions; dispatches sharing request to owner-checking resolver. This is a code-path inspection, not proof of every caller's authenticated principal. |
| OA-GR-03 | [OpenAgents access_model.py@93e3347](https://github.com/openagents-org/openagents/blob/93e334783747f6f35eb5133c0dec4351b7fffa10/workspace/backend/app/services/access_model.py), blob `aa4f19c47c40f41dc421e9e9d4c60b8dcb8f04ba` | `create_grant` supports `resource_kind`, `resource_id`, human/agent/grantee, normalized `rights`, optional scope, expiry, budget. `_grant_is_live` rejects revoked/expired grants. `revoke_grant` writes revocation time. Grant equivalence short-circuits repeated issuance for same resource/grantee/rights/expiration; separate event/idempotency design required for Foromni. |
| OA-RISK-04 | [OpenAgents access.py@93e3347](https://github.com/openagents-org/openagents/blob/93e334783747f6f35eb5133c0dec4351b7fffa10/workspace/backend/app/access.py), blob `120e86c7112c75a39da7f12afb5776688efaa54c` | Verified machine workspace token OR per-node token for this workspace passes helper even when human role gate is higher; broad machine access requires a separate Foromni task authorization boundary. |

All URLs are source pins. **Not independently tested:** outbound sender authenticity before AG2 ack/reject, concurrent approval transaction and entire OpenAgents API's effective enforcement. Do not infer exploitable access from the helper snippets alone. Follow call sites and execute isolated negative tests before adopting any library.

## Small state diagram and where privilege diverges

```
AG2 channel: REQUESTED -> PENDING --(valid acks)--> ACTIVE
                           |--(reject)---------> CLOSED
                           |--(timeout)--------> CLOSED

OpenAgents share: REQUESTED -> PENDING --(owner approval with state rechecks)--> GRANTED
                          |--(reject/expire)-----------------------------> DENIED
Resource grant: ACTIVE --(revoked/expired)--> INACTIVE

Foromni task: COLLABORATION_GRANTED --X--> TASK_EXECUTION
              Must additionally obtain trusted accepted task revision,
              policy-approved project scope, sandbox, budget, lease, epoch and grant.
```

Neither an AG2 ACTIVE channel nor an OpenAgents `read, act` grant is accepted as a Foromni task execution, QA, protected Git or release capability. Trust-reputation tier T0–T5 is advisory eligibility, not a bypass.

## Specific convergence harvest

| Mechanism | Judgment | Foromni mapping | Needed evidence to advance |
|---|---|---|---|
| AG2 invite/ack timeout & reject | ADAPT concept for collaboration admission | FOR-016 room/channel participation | Authentic sender check, duplicate/late ack, timeout/replay tests |
| AG2 manifest snapshot per channel | ADAPT concept | FOR-016 protocol version and upgrade safety | Version mismatch and revoke-in-flight tests |
| AG2 communication/rate rule | DO NOT TRUST DEFAULT | FOR-009 independent authorization / ingress rate | Enforced-denial tests on chosen hub topology |
| OA owner-scoped approval + membership recheck | ADAPT | FOR-016 consenting agent sharing; FOR-013 role of human approver | Current owner, requester, agent and thread state during racing revoke |
| OA typed revocable and expiring grant | ADAPT DATA MODEL, not credential | FOR-009 scope/lease/epoch | Action-time revalidation, conflict/replay/cross-project tests |
| OA workspace machine credential | REJECT as execution authority | FOR-009 trusted service issues narrow task creds | Prove machine token cannot inherit extra tasks/ref access |
| Trust ladder | ADVISORY ONLY | FOR-009 eligibility + FOR-012 verified record | Calibrated independent results, sampled complexity, appeals, anti-farming |
| Foromni protected QA/integration | RETAIN INTERNAL | FOR-011/012/013 and FOR-007 | Separate credentialed evaluator, candidate SHA and real test execution |

## Adversarial conformance additions (DESIGNED, NOT RUN)

| Fixture | Perturbation | Expected protection |
|---|---|---|
| ADMIT-01 | Invited AG2 participant acknowledges once | PENDING -> ACTIVE only under authentic participant identity |
| ADMIT-02 | Uninvited sender posts ACK | No admission; independent sender authorization enforced |
| ADMIT-03 | One participant rejects | CLOSED; no partially usable channel |
| ADMIT-04 | Invite never answered | CLOSED or EXPIRED; no silent promotion |
| ADMIT-05 | Duplicate ACK after channel closes | Terminal state remains terminal |
| ADMIT-06 | Manifests upgraded during existing channel | Existing manifest stays pinned; no silent permission shift |
| ADMIT-07 | OpenAgents approval by non-owner | Deny; no grant created |
| ADMIT-08 | Owner changes just before approval resolves | Deny if current owner differs |
| ADMIT-09 | Requester removed from thread before approval | Deny and require new request |
| ADMIT-10 | Approved sharing grant revoked then cached caller retries | Deny at action-time grant check |
| ADMIT-11 | Expired grant reused with refreshed agent score | Deny; reputation never reactivates grant |
| ADMIT-12 | Shared agent granted thread-only, invoked from another thread | Deny outside thread |
| ADMIT-13 | Valid machine token attempts unrelated private project write | Foromni denies without project-task scope |
| ADMIT-14 | T4 trusted agent tries to delegate protected merge | Deny absent separately authorized protected service |
| ADMIT-15 | T0 new agent gets isolated public benchmark grant | Permit narrow scoped trial with no confidential data |
| ADMIT-16 | A trusted agent fails a critical security test | Quarantine relevant rights pending owner/incident review, not numeric averaging |
| ADMIT-17 | Request approval races with agent removal | No resurrected grant from stale approval |
| ADMIT-18 | Invite/approval event is replayed after revocation | Deny; current revocation epoch takes precedence |

These are **specifications for future synthetic tests**. Source inspection suggests implementation paths, but it does not satisfy them.

## Decision and smallest next experiment

Adopt a **two-layer admission**: (1) human/agent collaborative channel admission and (2) task-specific, owner-authorized work admission using trusted authenticated grants. The trust ladder recommends eligible agents, but the policy engine alone decides actual operations. Combine AG2's channel acknowledgments with OpenAgents' owner review + revocable grant semantics *as concepts*; avoid importing implicit high privilege from either system.

Before testing, freeze four identities, two synthetic projects, a task lease state and a fake credential matrix, use code fixtures with a trusted evaluator, and preregister ADMIT-01..18. Separate protocol-admission observations from Foromni authorization results. Report missing/ambiguous and charged-but-failed outcomes rather than PASS. The next study should look at how reputation-driven *assignment recommendations* can be evaluated without disadvantaging new agents or incentivizing sham tasks.

**Research result:** evidence-backed compatibility mapping committed. **Runtime result:** none. **Authorization:** none.
