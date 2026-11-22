# Foromni — Open-Source AI Agencies and Agent Organizations: Comparative Landscape v0.1

**Date:** 2026-11-21 · **Status:** Public GitHub source/README + metadata exploratory study; **no system installed, executed, benchmarked, penetrated, or integrated**. **Foromni only.**  
**Goal:** Identify mechanisms useful to the frozen **FOR-007 AINO execution-MVP contract** without reopening or expanding its acceptance boundary. Paperclip, MetaGPT, ChatDev and CrewAI are *different product categories*, not interchangeable contenders.

## 1. Survey method and limits

Repositories selected for clear AI-agency/company/org/team behavior, adoption, model/framework relevance and community participation. Primary evidence: GitHub repository API metadata and README, plus deeper Paperclip core concepts. Star counts are a volatile **discovery signal only**, not safety, activity quality, successful work or independent evidence. Pinned public refs below are *source snapshots*, not dependency selections. GitHub API dates near midnight UTC can differ from founder-local 2026-11-21.

| Repository | GitHub stars observed (approx.) | License seen | Source snapshot / state | What it actually is |
|---|---:|---|---|---|
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 169.7k | MIT | `8ae6164602c95ca78828b148b9052460ee426885`; active | Portable **specialist agent role/prompt catalog**, with separate app for installing definitions |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | 115.7k | MIT | `324ec1f537a9ba1e84239faa81bcef326a5dd1b7`; active | **Agent organization control plane**: goals, roles, reporting, tasks, budgets, human board and adapters |
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 71.4k | MIT | `11cdf466d042aece04fc6cfd13b28e1a70341b1f`; last observed push Jan 2026 | Role-based software company and standard operating procedure (SOP) workflows |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 61.2k | MIT | `56c26a7fb3ece62c64de52e8b4228d15c9c81492`; active | Autonomous role-based **Crews** + deterministic/event-driven **Flows** |
| [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | 34.8k | Apache-2.0 | `464a681ba7bda869db97a50c5fa707c9a0fb57a0`; active | **ChatDev 2.0** configurable multi-agent platform; older virtual software company lives on `chatdev1.0` branch |
| [VRSEN/agency-swarm](https://github.com/VRSEN/agency-swarm) | 4.6k | MIT | `016189784354b4298ed25de752d22013ee5b5511`; active | Organizational agent roles, directional `communication_flows`, `send_message`; built on OpenAI Agents SDK |
| [ag2ai/ag2](https://github.com/ag2ai/ag2) | 5.1k | Apache-2.0 | `9bdd9d493a9a3a01308949b67d5a18219cb6c71c`; active | Community-governed multi-agent **AgentOS**; v1 API protocol-oriented, classical AutoGen APIs separate |
| [openagents-org/openagents](https://github.com/openagents-org/openagents) | 4.4k | Apache-2.0 | branch `develop`, not commit pinned in this review | **Collaboration OS** connecting heterogeneous agents and human members across machines/workspaces |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 94k | MIT | README and prior Foromni pinned case study | Open coding worker/environment, **not** overarching organizational authority |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 62k historic | GitHub metadata CC-BY-4.0; inspect file-level licenses | `8390985108cb1e3881f5f7297765758d8ad2540c`; **archived** | Historic conversational agents; **not** recommended as fresh primary dependency |

**Adjacent controls:** [microsoft/agent-framework](https://github.com/microsoft/agent-framework) (up-to-date Microsoft successor to AutoGen; GitHub file metadata access via connector returned 404 despite public browser presence), [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) (checkpointed workflows), [openai/openai-agents-python](https://github.com/openai/openai-agents-python) (lightweight handoffs/guardrails/tracing), [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) (developer worker harness). These are useful adapters, not necessarily organizations.

Counts and implementation claims were observed from public metadata/README at time of review; no repo-wide source audit or reproducibility experiment. Public stars are **not** ranking of verified reliability.

## 2. Highest-value case studies for Foromni

### Paperclip — closest organization-control-plane analogue

**Detailed source:** [paperclip core concepts at pinned SHA](https://github.com/paperclipai/paperclip/blob/324ec1f537a9ba1e84239faa81bcef326a5dd1b7/docs/start/core-concepts.md). 
- It models an organization goal, agents with adapters/roles/reports/budgets, task hierarchy and human board.
- Tasks use **atomic checkout** so only one agent claims the issue; concurrent claims return conflict, important for our lease/fencing concerns.
- **Heartbeats** wake agents on assignment, schedule, mention, manual invocation or approval; no assumption agents remain constantly awake.
- Human approval gates govern some strategy/hiring decisions and board overrides; logs/audit track changes.
- **Foromni harvest:** compare goal->task linkage, atomic checkout, lease vs heartbeat, approval limits, cost attribution, heterogeneous agent adapters and task/agent IDs.
- **Foromni divergence:** a company with a strict tree of reporting relationships is not the same as a global open-source federation of people, community projects and untrusted external contribution sources. A single agent manager cannot be default decision authority for unrelated member-owned projects. A completed Paperclip issue or recorded agent heartbeat is **not** proof of independent test execution, sealed QA or exact-source acceptance. Keep Foromni ledger/admission independent.
- **Candidate study challenge:** simultaneous claim and stale lease; verify conflicting attempts cannot both submit authoritative decisions. No benchmark run yet.

### Agency Agents — global reusable expertise, not runtime

The large prompt/role collection can seed a **versioned agent capability catalog** with predefined skills, deliverables and acceptance expectations. Descriptions and prompt instructions must never grant security roles. The large star count should not make us mistake role markdown for sandbox or QA engine. Favor linked/citable role definitions over copying massive prompt trees; inspect licenses and source provenance for imported content.

### MetaGPT — SOP-driven software company

Models product manager, architect, project manager and engineer as cooperating agents with structured documentation and sequential SOPs. **Harvest:** artifacts/contract handoffs and role specialization. **Risk:** generating specs/docs/code says little about approved source, actual tests, safe integration or full cost. Last observed push much older than current active alternatives. A full multi-role SOP is **not** H0's minimal required team.

### ChatDev 2.0 — configurable workflows and old company simulation

The current mainline is **DevAll / ChatDev 2.0**, a configurable multi-agent platform. Legacy CEO/CTO/programmer virtual-company scenario lives on `chatdev1.0`; do not score the old implementation as if it describes the current mainline. The research includes collaboration-topology work (e.g. MacNet and learned orchestration), useful for **later controlled team-size comparisons**, not evidence of safer H0 patches.

### CrewAI — orchestration model split

Crews support collaborative autonomous role-based execution; Flows provide explicit event-driven/conditional workflows. **Harvest:** keep deterministic control/approval path separate from model decision-making. Many management/observability/governance conveniences described in the README belong to commercial **AMP**, not necessarily the MIT framework; check open-core boundary per feature. CrewAI alone does not provide independently authenticated evaluator custody.

### Agency Swarm — bounded directed communication

Extends OpenAI Agents SDK and uses explicit directed `communication_flows`, typed tools and optional persistent thread callbacks. **Harvest:** only preauthorized role-to-role communication edges, typed task handoffs and clear context authority. Not necessarily model/provider neutral in the same sense as Foromni; README notes native OpenAI SDK/Responses integration plus LiteLLM alternatives. Still requires sandbox, independent QA and work acceptance.

### AG2 — open community AgentOS

Community-maintained v1 protocol-driven design, human-in-loop and multi-agent collaboration. **Harvest:** membership openness and portable communication channels. Migration matters: classic `ConversableAgent` / `GroupChat` are in a separate `ag2-classic` repo. Do not copy v0 tutorials into a v1 comparison.

### OpenAgents — distributed mixed human-agent participation

Connects externally hosted/local agents in workspaces, with humans, conversation threads and shared files. **Harvest:** cross-device federation UX, bringing own agent and asynchronous collaboration. **Risk:** collaborative shared files/contexts are distinct from isolated per-tenant execution and authoritative QA; need to test workspace permission and isolation boundaries before adoption.

## 3. Not one leaderboard — four independent research axes

| Axis | Best exemplars in this scan | Foromni ownership |
|---|---|---|
| **Agent/organization representation** | Paperclip, MetaGPT, Agency Agents | Member/Agent/Project/Task graph with explicit owners and identities |
| **Workflow / coordination** | CrewAI, Agency Swarm, ChatDev, AG2 | Typed task lease, traceable handoff, bounded control; runtime adapter optional |
| **Open community collaboration** | OpenAgents, AG2, Agency Agents | BYO agent/compute, contribution/attribution and project boundaries |
| **Verifiable delivery and safety** | OpenHands coding worker + sandbox case studies + Foromni H0-M/S/R | Foromni source observer, separate evaluator, human admission, protected integration |

None of these were independently confirmed to implement **all** elements of FOR-007: frozen task revision; verified sandbox; worker without protected Git write; independent source SHA reconstruction; sealed evaluator QA; full attempt accounting; human candidate acceptance distinct from merge/release; portable external contribution. **Absence of confirmed demonstration is not proof a repo has no such feature.**

## 4. Candidate hybrid for the *frozen* FOR-007 MVP

```text
FOR-007 task contract + trusted member/agent/project registry
   -> task lease with epoch/budget and human approval
   -> ONE qualified sandbox with ONE real coding worker
   -> patch-only artifact (worker has no GitHub write credential)
   -> trusted independent source observer (clean candidate SHA)
   -> separate independent evaluator (real protected tests)
   -> candidate-scoped human decision + cost/evidence ledger
```

**No architectural change to frozen FOR-007-RC1 is proposed by this survey.** The following are **mechanism candidates**, not implementation assignments:

- **Paperclip:** task checkout and budgeted agent wake/heartbeat semantics for FOR-009/FOR-012.
- **Agency Agents:** catalog entries for agent specialization once providers/roles exist; no need for the entire roster before H0-A.
- **CrewAI / Agency Swarm / AG2:** choose at most one as future **worker/handoff adapter**, if and only if it reduces real measured workload after the single-worker slice.
- **OpenAgents:** BYO agent and human collaboration design for FOR-016 (global community pilot).
- **MetaGPT/ChatDev:** preregister as later **multi-agent team-size and SOP experiments** against solo and adaptive baselines; judge accepted full-stack results per cost, not number of generated files.
- **Autogen archived:** historical reference, not new MVP dependency.

## 5. Five unanswered research questions, with discriminating follow-ups

1. **Paperclip concurrency / budget:** What is the exact atomic task claim and budget limit semantics, including retries, agent pauses and expired leases? Does a worker terminate after revoke, or merely stop receiving new assignments?
2. **Paperclip provenance:** Can a completed issue be tied to a separately reconstructed SHA and independently authenticated evaluator, or would Foromni have to supply those records?
3. **OpenAgents tenant safety:** Are files and threads isolated across distinct workspace/project ownership contexts, and what can a remote participant read by default?
4. **CrewAI vs Agency Swarm:** Under matched synthetic task, which handoff mechanism preserves revision/lease grant and costs with fewer failures? A comparative test is later, not authorized by this research.
5. **Global OSS governance:** How do outside contributors challenge incorrect evaluations, appeal task rejection, preserve attribution and maintain ownership without permanent central agent control?

Do **not** add a new project-wide dependency solely because stars are high. Before selecting any product: read authoritative source paths (not only README), verify chosen artifact license/edition, pin release and dependency hashes, test authentication/permissions under current host, estimate migration/maintenance cost, and demonstrate actual incremental benefit.

## 6. Decision and sequencing

**Top deep-dive priority:** **Paperclip**, because it most directly matches Foromni's future organizational control-plane needs.  
**Second:** **OpenAgents**, because it serves the open global mixed human-agent membership mission.  
**Third:** **Agency Swarm + CrewAI** mechanisms, for bounded handoff/human gates (not two simultaneous orchestrators).  
**Fourth:** **MetaGPT + ChatDev** as scientific workforce-structure comparators.  
**Agency Agents:** strong modular role catalog; future capability registry content, not foundational security.  
**AG2:** relevant community/protocol reference, especially if Foromni later needs peer-to-peer agent coordination.

**MVP freeze and founder authority are unchanged.** Research is additive only; no CI, branch merge, installations, experiments, spending, external outreach, live user data or Internet Embassy access occurred. Later decisions must explicitly change FOR-007 via a new reviewed contract version rather than silently back-propagating a case study.

*Build today, so others can enjoy tomorrow.* ❤️🐂
