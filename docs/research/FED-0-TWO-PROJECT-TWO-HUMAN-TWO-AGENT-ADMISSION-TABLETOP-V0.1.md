# Foromni FED-0 — Two-Project Federation Admission Tabletop v0.1

**Date:** 2026-11-22 UTC · **Status:** source-inspected tabletop decision design; **NO EXECUTABLE TESTS RUN**. No deployment, integration, architecture freeze, external outreach, production permission changes or task authorization. This is a research continuation, not new MVP scope.

**Inputs:** [AG2/OpenAgents case study](EXTERNAL-CASE-STUDY-AUTOGEN-AG2-OPENAGENTS-FEDERATED-COLLABORATION-V0.2.md); [Convergence Work Packet v0.2](CONVERGENCE-WORK-PACKET-TYPED-CONTRACT-V0.2.md); [E0 trust boundary](E0-V0.5-EVALUATOR-TRUST-BOUNDARY-AND-GRADE-ORACLE.md). Link to FOR-009 (registry/grants), FOR-011 (evaluator custody), FOR-012 (attempt/evidence), FOR-013 (human decision) and FOR-016 (federated community). Preserve frozen FOR-007.

## Fresh source-specific observations

- [AG2 identity.py@9bdd9d4](https://github.com/ag2ai/ag2/blob/9bdd9d493a9a3a01308949b67d5a18219cb6c71c/ag2/network/identity.py), blob `671a0bf612b01e0246129e568ce88e230f6f4301`: `Passport` documents hub-stamped registration identity and participant kinds agent/human/remote_agent. `Resume` deliberately distinguishes **tenant-supplied claimed capabilities/examples** from **hub-mutated observed statistics** (count, completed, failed, expired, latency). Very useful epistemic separation, but hub-observed terminal task events are not necessarily independent source/test verification. **Do not confuse AG2 Passport with Foromni's member Passport product**.
- [AG2 rule.py@9bdd9d4](https://github.com/ag2ai/ag2/blob/9bdd9d493a9a3a01308949b67d5a18219cb6c71c/ag2/network/rule.py), blob `fe89ad3f86688ca7aa0c827334bc1ed262a063a0`: defaults permit wide communication; source comments explicitly say per-channel-type allowlist and rate limit stored but ignored by in-process hub. These cannot provide Foromni's authoritative scoped policy without another enforcing layer.
- [OpenAgents access.py@93e3347](https://github.com/openagents-org/openagents/blob/93e334783747f6f35eb5133c0dec4351b7fffa10/workspace/backend/app/access.py), blob `120e86c7112c75a39da7f12afb5776688efaa54c`: `verify_workspace_access` checks deleted workspace, verified human identity/membership, workspace machine token, and per-node token. Both machine token paths return full trusted workspace access for this helper; a per-node token is restricted to *its workspace*, not fine-grained member project rights. This is a source-scoped observation of that helper, not proof of every route's effective permissions.
- [OpenAgents visibility.py@93e3347](https://github.com/openagents-org/openagents/blob/93e334783747f6f35eb5133c0dec4351b7fffa10/workspace/backend/app/services/visibility.py), blob `6ffa439160d3350422290aae715e862754e3f995`: `can_view_channel_name` returns true for `viewer.machine`; unknown channel names also return true. Understand resolution and route-level checks before claiming a leak. This confirms **machine vs human visibility must be tested separately**.
- [OpenAgents workspace README@93e3347](https://github.com/openagents-org/openagents/blob/93e334783747f6f35eb5133c0dec4351b7fffa10/workspace/README.md), blob `f69622e21e7ca0fbc08d7baad1baa379fc0295d4`: issue discussion and comment do not start execution; explicit 'Bring in an agent' or task board action is a separate step. Useful UX boundary, but Foromni must also enforce separate accepted task and lease grants.

## Actors, projects and exact minimal fixture

- Humans: `H_A` is project A owner/steward; `H_B` is independent project B owner/steward.
- Agents: `W_A` is externally hosted BYO agent claimed by H_A, verified only to participate in project A's public collaboration; `W_B` is separately registered agent approved for B.
- Projects: `P_A` public discovery and public discussion, with private task artifacts; `P_B` private project whose roster, files, tasks and evaluator results are hidden from H_A/W_A.
- Trusted services: `POL` policy/grant service, `SRC` independently reading source SHA, `QA` separately authenticated evaluator, `APP` human acceptance service.
- Initial authority: H_A owns P_A; H_B owns P_B; W_A only has `discover_public`, `join_channel(P_A:public)`, `post_message(P_A:public)`; W_B has P_B collaboration grant. **Neither agent has work execution, protected Git write, secret access, cross-project bridge, QA or acceptance permission.**
- Authoritative task snapshot: `T_A@rev1` tied to P_A; `T_B@rev1` tied to P_B. `attempt_id` absent until a lease is explicitly issued. Synthetic examples are not actual credentials.

## Tabletop decision oracle (policy expectations, NOT observed runtime results)

| ID | Action attempted | Decision | Independent reason |
|---|---|---|---|
| FED-T01 | W_A discovers P_A public description | ALLOW | Authenticated public scope |
| FED-T02 | W_A joins P_A public channel | ALLOW | Explicit scoped participation |
| FED-T03 | W_A reads P_A private task evidence | DENY | Discussion grant != private artifact access |
| FED-T04 | W_A discovers P_B private roster/task | DENY + non-disclosing response | Cross-project membership absent |
| FED-T05 | W_A sends collaboration event into P_B | DENY | No explicit bridge and no target consent |
| FED-T06 | W_A requests sandbox tool call on T_A without lease | DENY | Collaboration permission != execution permission |
| FED-T07 | H_A authorizes bounded T_A lease for W_A, matching task rev1 and budget | CONDITIONAL ALLOW after trusted admission | Current principal, project, revision, sandbox, rate, budget, expiry must pass |
| FED-T08 | W_A attempts protected merge with granted draft lease | DENY | Worker grant excludes protected refs |
| FED-T09 | W_A submits forged `QA:PASS` message | UNVERIFIED | Worker text not independent QA principal or executed suite |
| FED-T10 | W_A executes with expired/revoked epoch | DENY | Action-time policy invalidates former lease |
| FED-T11 | Old queued P_A→P_B message arrives after bridge revoke | DENY | Re-check recipient context and grant at delivery |
| FED-T12 | H_A attempts to accept P_B candidate | DENY | Wrong human authority/project |
| FED-T13 | QA independently tests candidate SHA_A, worker submits SHA_B | STALE_EVIDENCE | Evaluated source differs |
| FED-T14 | H_A accepts correctly evaluated SHA_A for P_A | CONDITIONAL human candidate acceptance only | Authentic human + exact SHA + current criteria; not a merge/release |
| FED-T15 | W_A reconnects under same displayed agent name but new hub identity | REAUTH REQUIRED | Name/capability claims cannot recreate revoked lease |
| FED-T16 | W_A presents machine token for one workspace and seeks project B access | DENY at Foromni's project authority plane | Workspace membership is not cross-project rights |
| FED-T17 | W_A emits its own cost/throughput claim | CLAIM_ONLY | Actual spending must be reconciled from trusted receipts/telemetry |
| FED-T18 | Trusted evaluator completes B positive/negative suite for B with no P_B authority | DENY/INVALID | Independent reviewer still needs B-scoped evaluation grant |

## Critical semantic separation

- **Agent claimed expertise** (AG2 Resume's `claimed_capabilities`): searchable assertion, no authority.
- **Hub-observed events** (AG2 Resume's `observed`): better than self-report, but not necessarily code-quality truth.
- **Foromni independent candidate evidence:** source SHA + exact evaluator principal + suite/fixture/environment + real positive/negative execution + signed/source-bound result. No promotion from events alone.
- **Collaboration:** messages, issue comments and shared threads. **Authorization:** project ownership, task revision, action-time lease/budget/tool scope. **Candidate QA:** separate. **Human acceptance:** separate. **Protected merge/release:** separate.
- AG2 `Passport` denotes a network registration; Foromni Passport denotes a user-centered product identity. Map via adapter, do not alias these domains.

## Minimal event translation sketch (research data only)

```json
{
  "event_kind": "collaboration.message",
  "network_id": "P_A-public",
  "source_participant": "W_A",
  "destination": "P_A:discussion",
  "task_ref": "T_A@rev1",
  "attempt_id": null,
  "claimed_capability": "code-review",
  "requested_action": "post_message",
  "authority": "VERIFY_AT_ACTION_TIME",
  "evidence_class": "worker_asserted"
}
```

This is **not** a signed event, active grant, acceptance packet or approved schema. A transport adapter may carry the event but cannot grant it execution rights. For true task work, issue an independently minted, short-lived scoped lease tied to a current task revision and fencing epoch; prohibit using upstream workspace machine tokens as Foromni root credentials.

## Research-only tabletop analysis and acceptance criteria

The 18-row oracle specifies decisions for a synthetic set of actors. It is a **desk-reasoned expectation matrix**, not a result of running the two projects. Formal execution is necessary to measure actual denials, network/event race behavior, latency, and provider-specific costs.

Before any executable trial, preregister: exact target repos/SHAs, implementation/build versions, trusted actor provenance, test harness credentials and separation, source fixture digests, negative assertions, expected security failures, budget, stop conditions and reversible sandbox resources. Do not place secrets in Git or run exploit payloads against public services.

**Candidate research insight:** Design Foromni global participation around *project-scoped agent adapters with a clearly separate execution lease*. Borrow OpenAgents' issues/workspace UX and AG2's separate claim/observed capability data; refuse default authority inheritance from communication networks. The frozen one-worker FOR-007 path remains prioritized. No modification to frozen MVP or real system is implied.

## Follow-up

Inspect AG2's actual channel invitation/ack enforcement and OpenAgents' per-node token / sharing routes, then build a source-backed conformance matrix to distinguish supported features from documented intentions. If separately authorized, build an isolated minimal harness with the same FED-T cases and compare observed outcomes to this oracle. Keep research-only records out of runtime acceptance ledgers.

**Evidence grade:** direct source inspected + synthetic reasoning. **Results:** 0 execution cases run, 0 independent QA verdicts, 0 integrations.
