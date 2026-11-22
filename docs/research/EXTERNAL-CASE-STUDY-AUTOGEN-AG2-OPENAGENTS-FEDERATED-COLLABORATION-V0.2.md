# AutoGen Lineage, AG2 and OpenAgents — Federated Human/Agent Collaboration Case Study v0.2

**Date:** 2026-11-22 UTC. **Status:** Source-level research / proposed experiments, NOT software execution, vulnerability confirmation, independent security audit, or Foromni integration. Foromni only.  
**Prior basis:** [agency landscape v0.1](EXTERNAL-CASE-STUDY-OPEN-SOURCE-AI-AGENCIES-AND-ORGANIZATIONS-V0.1.md); [SOP-to-convergence crosswalk](AGENCY-SOP-TO-CONVERGENCE-WORK-PACKET-FIELD-CROSSWALK-V0.1.md); [FOR-007 reference architecture](AINO-END-TO-END-OPEN-SOURCE-CONVERGENCE-REFERENCE-ARCHITECTURE-V0.1.md). Do not alter frozen acceptance criteria or grant runtime authority.

## 1. The real AutoGen family in late 2026

- [microsoft/autogen](https://github.com/microsoft/autogen) is marked **archived and no longer maintained** in its official README (Git blob inspected `042b9df197a220ec7072a116d694cd497ec332ad`). It explicitly recommends [microsoft/agent-framework](https://github.com/microsoft/agent-framework) for new systems and says the latter is the Microsoft successor. Do not recommend archived AutoGen as a production dependency. Archive date is reported by GitHub public listing as 2026-11-20; do not confuse this with the earlier engineering transition.
- [ag2ai/ag2](https://github.com/ag2ai/ag2) is the independently maintained AG2 community continuation, **not** the same codebase as Microsoft Agent Framework. Its README (blob `75c325639e6aae2f261fb57e7d29e75c23e9e968`) distinguishes the v1 `ag2.Agent` + Network channels from original AutoGen-derived `ConversableAgent`/`GroupChat`, moved to [ag2ai/ag2-classic](https://github.com/ag2ai/ag2-classic). Incompatible import/runtime models must not be conflated. README documents Python >=3.11 and first-agent async example. No packages installed in this case study.
- [openagents-org/openagents](https://github.com/openagents-org/openagents) is a separate human-agent workspace/network project (README blob `ea99f1a79427ec8cba29c0d9b790155e08cffdfe`); it is **not** a successor/fork of AutoGen. The model includes Workspace, Launcher and Network SDK.

## 2. AG2 direct source mechanisms

**Pinned source snapshot:** [ag2ai/ag2@9bdd9d493a9a3a01308949b67d5a18219cb6c71c](https://github.com/ag2ai/ag2/tree/9bdd9d493a9a3a01308949b67d5a18219cb6c71c).

- [ag2/network/client/network_client.py](https://github.com/ag2ai/ag2/blob/9bdd9d493a9a3a01308949b67d5a18219cb6c71c/ag2/network/client/network_client.py) (blob `a9c8eae41953bfcf029c700f7b109629a5850742`): `NetworkClient` is a structural Protocol with participant identity/passport/resume, inbound envelope delivery and disconnect. Documentation explicitly contemplates non-LLM participants (queue/UI bridges or human clients). **Harvest:** a transport/worker-neutral participant adapter instead of requiring all members to inherit an AI-agent class. Caution: `Passport` is AG2's networking object, not Foromni's member identity product.
- [ag2/network/channel.py](https://github.com/ag2ai/ag2/blob/9bdd9d493a9a3a01308949b67d5a18219cb6c71c/ag2/network/channel.py) (blob `4b79d33f026896d6ae878a7b67675ee089018e5b`): manifest/version, participant roles, PENDING/ACTIVE/CLOSING/CLOSED/EXPIRED lifecycle, explicit acknowledgement/rejection and protocol-shape expectations. Channel metadata snapshots manifest so adapter changes do not silently mutate running channels. **Harvest:** versioned collaboration envelopes and admission acknowledgement (distinct from task lease and authorization).
- [ag2/network/rule.py](https://github.com/ag2ai/ag2/blob/9bdd9d493a9a3a01308949b67d5a18219cb6c71c/ag2/network/rule.py) (blob `fe89ad3f86688ca7aa0c827334bc1ed262a063a0`): limits/access are **permissive by default** and the source explicitly states `AccessBlock.channel_types` and `LimitsBlock.rate` are *stored but ignored by the in-process hub*. Other inbox overflow modes are recognized but treated as `reject`. **Critical source-scoped compatibility warning:** a declared rule is not necessarily enforced. Requires independent black-box permission/rate tests if considered for Foromni. This is not a confirmed exploitable vulnerability, and external deployment topologies may add enforcement.

## 3. OpenAgents direct source mechanisms

**Pinned source snapshot:** [openagents-org/openagents@93e334783747f6f35eb5133c0dec4351b7fffa10](https://github.com/openagents-org/openagents/tree/93e334783747f6f35eb5133c0dec4351b7fffa10).

- [docs/openagents_network_model.md](https://github.com/openagents-org/openagents/blob/93e334783747f6f35eb5133c0dec4351b7fffa10/docs/openagents_network_model.md), blob `e3141f6c8f16dbf9096195b90e8c19ea7e9ce075`: proposed event-centric networks with bounded contexts, explicit bridges, addressing, progressive identity verification (levels 0–3), mods/guards and transport abstraction. It is a model specification, not proof every runtime/path enforces each stated invariant.
- [workspace/README.md](https://github.com/openagents-org/openagents/blob/93e334783747f6f35eb5133c0dec4351b7fffa10/workspace/README.md), blob `f69622e21e7ca0fbc08d7baad1baa379fc0295d4`: FastAPI/SQLAlchemy backend, Next.js frontend, shared workspace events, issues and task links. Issue creation or comments do **not automatically start agent work**; explicit 'Bring in an agent' starts the linked execution thread. This separation is especially valuable for Foromni.
- [workspace/backend/app/access.py](https://github.com/openagents-org/openagents/blob/93e334783747f6f35eb5133c0dec4351b7fffa10/workspace/backend/app/access.py), blob `120e86c7112c75a39da7f12afb5776688efaa54c`: code checks deleted workspace, machine workspace token, verified human membership, legacy open workspace mode. Code says machine token is trusted even if require_login is on and is owner-equivalent for role minimums. **Trust implication:** a machine workspace credential is too broad for Foromni's untrusted external contributors if used unmodified. Review actual distribution, per-agent scopes, revocation and every endpoint; do not mistake documented 'private by default' for all-channel/tenant security proof.
- [workspace/backend/app/routers/shares.py](https://github.com/openagents-org/openagents/blob/93e334783747f6f35eb5133c0dec4351b7fffa10/workspace/backend/app/routers/shares.py), blob `c3b05ecdf8f02c1d5bc6b8c272ee43f8dc332a43`: checks workspace access and viewer visibility before share, requires a human-origin decision (with legacy-open exception); public snapshot endpoint is anonymous by token. **Harvest:** human-initiated publication separated from agent work. **Test question:** verify newly revoked channel access and private content do not become accessible via old snapshots, and test legacy-open attribution handling. Not a demonstrated exploit.

## 4. Why this matters for Foromni's global member model

Use three distinct identities: **human member**, **agent/provider**, and **actual execution incarnation**, with a project-scoped delegated authority graph. A communication channel does not authorize code execution, and a shared workspace token must never imply blanket protected repository access.

Proposed architecture:

```
Human member / external agent provider / authorized project steward
 -> discover project and public task proposal
 -> authenticated participation in scoped project network
 -> request explicit task lease + budget + sandbox grant from trusted policy
 -> work in separate sandbox (no protected Git credentials)
 -> submit patch and source/provenance digest
 -> independent source observer and sealed evaluator
 -> human candidate decision for that exact SHA
 -> separately authorized protected integration / release
```

AG2 can inform *participant/channel semantics*; OpenAgents can inform *user experience, workspaces, presence, explicit bridging and discussion-to-execution boundary*. Neither supplies Foromni's existing FOR-007 end-to-end source custody and independent acceptance just by supporting a conversation or role.

## 5. Twelve preregistered negative/failure fixtures (not run)

| ID | Stimulus | Expected Foromni behavior |
|---|---|---|
| FED-01 | Agent with public discovery tries to read private project channel | Deny / no data |
| FED-02 | External agent possesses collaboration-room invite but no task lease | Conversation allowed if scoped; execution denied |
| FED-03 | Agent A's message claims identity of agent B / QA principal | Ignore claim; independently verify principal |
| FED-04 | AG2 in-process rule denies a channel type whose source says check not enforced | Under Foromni adapter, deny at trusted boundary regardless of AG2 rule storage |
| FED-05 | Rate limit documented but not enforced by transport | Enforce trusted ingress cap; measure rejects and observability |
| FED-06 | Shared workspace machine token used by untrusted participant | Reject unless separately scoped credential; no owner-level privilege |
| FED-07 | Project A event addressed to project B without explicit bridge grant | Deny and audit |
| FED-08 | Cross-project bridge is revoked while queued message remains | Reevaluate at delivery/action time, deny stale access |
| FED-09 | Public snapshot after private thread/channel revocation | Apply publication policy, redact/block unauthorized disclosure |
| FED-10 | Issue mention or comment automatically starts agent without authorization | No work; explicit accepted task/lease required |
| FED-11 | Participant sends a beautiful 'PASS' summary for unexecuted code | Remain unverified; source SHA and independent QA required |
| FED-12 | Same agent reconnects with changed runtime identity after revoke | Do not restore grants based on display agent name/passport alone |

Important: these are **proposed tests**. Neither upstream project was installed or run. Source comments about missing checks must be verified under a specific deployment before making security conclusions.

## 6. Engineering-evidence harvest into existing convergence path

| Pattern record | Candidate roadmap linkage | Decision | Validation required |
|---|---|---|---|
| `AG2-network-client-interface` | FOR-009, FOR-016 | ADAPT concept later | Human/agent adapter respects authorization independent of inbound content |
| `AG2-versioned-channel-lifecycle` | FOR-016 | ADAPT later | Acks, expiry/revocation, replay and version mismatch |
| `AG2-rule-enforcement-gap` | FOR-009/016 | CAUTION; do not rely on defaults | Actual deny/rate cases on target topology |
| `OA-bounded-network-events` | FOR-016 | STUDY / adapt bridge idea | No cross-network leakage under queued/replayed events |
| `OA-human-agent-issue-to-work` | FOR-016/FOR-009 | ADAPT UX concept | Comment does not grant execution authority |
| `OA-machine-token-owner-equivalence` | FOR-009/FOR-016 | REJECT as Foromni BYOA authority model | Least-privilege agent creds, per-project scoping, revocation |
| `OA-human-public-share-gate` | FOR-013/FOR-016 | ADAPT with safeguards | Snapshot access, publication/revocation, audit |
| `original-AutoGen-runtime` | later historical studies | DO NOT SELECT as fresh dependency | Archived; successor/fork comparison if needed |
| `AG2-or-MAF-runtime` | FOR-010 later adapter comparison | DEFER | Single-worker FOR-007 gate first; cost/performance experiment later |

Each record should link upstream repository and pinned revision, exact source file/blob, observation class `code_inspected`, failure hypothesis, scope limitations, dependency/license check and proposed fixture. Until experiments exist, `result_evidence_ref = null`, `authority_status = research_only`. The committed study provides evidence for an architecture decision, **not executable convergence PASS**.

## 7. Next smallest evidence-rich experiment

A **two-project / two-human / two-agent tabletop and later executable** fixture: Project A public, B private; one external agent can discover A, join a scoped A collaboration channel, then attempts B reads, an A-task execution without lease, and a forged evaluator completion. The trusted service must permit only the explicitly granted actions. Compare AG2 channel envelope and OpenAgents network event translation, with frozen task rev, agent incarnation, lease epoch and cost receipt metadata. No foreign framework must gain Git write credentials.

Measurements: verified deny rate (including revocation), missing/ambiguous identity, correct task-grant attribution, consented publication, message delivery fidelity and full attempt costs. Do not grade narrative success as acceptance; no real test claim without executed evidence.

## Limitations

This is a narrow set of direct files, not exhaustive repo audit. AG2 and OpenAgents snapshots differ, and upstream docs, branches and Git metadata can evolve. Model/docs claims of features are not independent proof of deployment security. No authorization to test these external products, connect accounts, publish, merge, spend or deploy was requested or exercised.

*Build today, so others can enjoy tomorrow.* ❤️🐂
