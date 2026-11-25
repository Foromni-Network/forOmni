# Open-Source AINO Case Study 02 — OpenHands, Agent Canvas and Agent Ownership

**Status:** Read-only architecture research and prospective collaboration assessment; NOT deployed, executed, forked, benchmarked or independently security-audited.  
**Date:** 2026-11-21. **Foromni only:** No Internet Embassy access or changes. No OpenHands contact, issue, PR or endorsement.
**Primary target:** [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) currently **Agent Canvas**, not the older monolithic coding-agent repository. Reviewed main at `0f4cb6af95915fee776913c4aa8694e7c4b76033`. Related repos: [software-agent-sdk](https://github.com/OpenHands/software-agent-sdk), [automation](https://github.com/OpenHands/automation), [extensions](https://github.com/OpenHands/extensions).
**Comparative secondary:** [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph), reviewed main at `c6335a4255dc1d8abc25a7677f9c072c7ab27b9c`.
**Companion Foromni research:** EXTERNAL-CASE-STUDY-RERUN-BUILD-OPEN-SOURCE-AND-COLLABORATION.md, PERSISTENT-AGENT-REGISTRY-IDENTITY-AND-SHARED-CREDENTIALS.md, CONVERGENCE-FIRST-CONTROLLER-ARCHITECTURE.md, ECONOMETRICS-OF-CONVERGENCE-AND-COORDINATION-VARIANCE.md.

## Why this case study follows Rerun

Rerun showed that persistent coworker identities, shared model connections and personal workspaces can coexist. The next question is how a *coding-specific* open-source ecosystem structures execution, backend choice, persistent state, cross-repository contracts, human governance and independent verification. OpenHands is a strong comparison because its current maintainers make these boundaries explicit.

**Critical source evolution:** OpenHands' old `All-Hands-AI/OpenHands` address redirects. More importantly, today's `OpenHands/OpenHands` main is the **Agent Canvas control/UI** repository; agent execution belongs to `OpenHands/software-agent-sdk`, automation to `OpenHands/automation`, reusable extensions to `OpenHands/extensions`. Do not base an architectural evaluation on old articles describing the previous monorepo as current.

## 1. Directly observed architecture

| Question | OpenHands source observation | Foromni AINO significance |
|---|---|---|
| One user, many coding agents? | Agent Canvas advertises OpenHands, Codex, Claude Code, Gemini, Pi, OpenCode and ACP-compatible agents | Standard interfaces and backend adapters may reduce vendor-specific orchestrators |
| Local vs remote workers? | Canvas README describes local, Docker, VM, self-hosted and remote/cloud backends | Worker placement can be separated from roadmap/task coordination |
| Who owns implementation? | `AGENTS.md` maps UI to Canvas; agent/tools/events/API to SDK; scheduling/webhooks to automation; skills to extensions | **Cross-repository ownership is an explicit convergence contract**, not a vague organizational chart |
| What is an interface boundary? | SDK README says canonical Agent Server REST/WebSocket API → typed TypeScript client → Canvas | Stable typed contract propagation and compatibility should precede isolated implementation |
| How are checks independent? | Canvas `AGENTS.md`: implementation agents must not modify verify-skill maps/fixtures in same change; verification maintenance requires separate PR/context | Direct analogue of Foromni's independent QA and acceptance-oracle separation |
| Human vs agent approval? | Canvas `AGENTS.md` reserves PR `HUMAN:` section for humans; agents are told not to edit it | Human approval provenance cannot be replaced by a model writing 'approved' |
| What is a sandbox? | Canvas README warns the no-sandbox mode grants agents full host filesystem access; recommends separate sandbox deployment choices | Project directory settings alone are insufficient for safe untrusted execution |
| Licensing? | Agent Canvas root `LICENSE` and `package.json` identify MIT; SDK README describes MIT | License is favorable to learning but licenses of distinct related repos/dependencies require separate checks |
| Testing practices? | Canvas docs specify tests, lint, build, separate mock-LLM, Docker, E2E checks and custom verification skills | Useful benchmark for observed source/acceptance discipline, not proof all tests are green |

### Pinned source links

- [Agent Canvas README](https://github.com/OpenHands/OpenHands/blob/0f4cb6af95915fee776913c4aa8694e7c4b76033/README.md)
- [Agent Canvas architecture and contributor constraints](https://github.com/OpenHands/OpenHands/blob/0f4cb6af95915fee776913c4aa8694e7c4b76033/AGENTS.md)
- [Agent Canvas package manifest](https://github.com/OpenHands/OpenHands/blob/0f4cb6af95915fee776913c4aa8694e7c4b76033/package.json)
- [Agent Canvas license](https://github.com/OpenHands/OpenHands/blob/0f4cb6af95915fee776913c4aa8694e7c4b76033/LICENSE)
- [Software Agent SDK README](https://github.com/OpenHands/software-agent-sdk/blob/main/README.md)
- [SDK architecture ownership](https://github.com/OpenHands/software-agent-sdk/blob/main/AGENTS.md)

The two SDK links are moving `main` references because the SDK commit SHA was not recorded in this first pass; snapshot pin before any formal publication/experimental comparison. No SDK runtime was inspected in operation.

## 2. Important AINO lesson: ownership is part of the architecture

OpenHands' `AGENTS.md` instructs contributors to place changes in the correct repository, keep Agent Server contracts canonical and avoid duplicating backend APIs in the frontend. In a multi-agent AINO, this translates to a **relationship graph with edges for contractual ownership and change propagation**.

Illustrative Foromni mapping:
- Objective: add reliable task completion evidence.
- Owning domain: execution event schema vs UI rendering vs schedule dispatch.
- Affected contracts: agent run event, REST/WS API, typed client, UI state, acceptance oracle.
- Synchronization rule: a change cannot be called accepted if one supported downstream adapter silently drops the new field.
- Reviewer separation: implementation contributor should not change hidden acceptance fixtures to manufacture a passing result.

This directly supports the founder's hypothesis that roadmap/relationship synchronization may reduce rework. **It is qualitative architectural evidence, not an estimated improvement or causal proof.**

## 3. Important AINO lesson: verification independence can be specified in repo governance

The current Canvas `AGENTS.md` prohibits implementers from editing `.agents/skills/verify-*/` expected results/feature maps while implementing product changes; it separates verification maintenance into dedicated PRs and agent contexts. It also reserves human-authored PR content to humans.

This is unusually concrete and offers Foromni useful research questions:
1. How is this enforced *technically* beyond natural-language instructions? Are CODEOWNERS/CI/rulesets checking it?
2. Does the code-review process refuse an implementation PR that modifies its own acceptance oracle?
3. How does the separate SDK repo's contract evolve without creating an untestable compatibility gap in Canvas?
4. Can human-provenance checks use real GitHub identity and host policy rather than a writable `HUMAN:` string?

If enforcement is only an agent instruction, it remains a valuable norm but not a hard security boundary. No live enforcement audit was conducted.

## 4. Important AINO lesson: reuse standards and runtime infrastructure

OpenHands says its Canvas can use ACP-compatible agents and multiple backend types. That encourages a division between:
- **execution/runtime:** a coding agent working in a controlled workspace;
- **interaction/UI:** agent conversations, backend selection and observable controls;
- **orchestration:** task objectives, scheduling, dependencies and source reconciliation;
- **admission:** independent acceptance, Git protections and release permissions.

Foromni should research **small adapters** to established runtime/API boundaries rather than build another entire agent engine merely to obtain persistent worker identity or multi-provider access. AINOs may use different agent runtimes behind a shared task/contribution evidence model.

## 5. Companion comparison: LangGraph solves a different problem

LangGraph explicitly describes itself as a low-level **stateful workflow runtime** with durable execution, checkpoints, human interrupts and persistence. Its `AGENTS.md` states the project's current direction is toward runtime correctness, reducing API surface and using higher-level harnesses such as Deep Agents to construct agents.

Notable source-level mechanisms:
- Checkpointer interface stores graph state and intermediate writes, with `thread_id`/optional `checkpoint_id`.
- Pending writes avoid rerunning successful nodes when another node fails in the same superstep.
- The checkpoint README calls out deserialization safety and suggests restricted message-pack modules.
- A checkpoint is **not** independent business acceptance, Git merge authority or verified contributor identity.

**Complementarity, not winner:** OpenHands demonstrates multi-backend coding agent execution/control and cross-repo contract ownership. LangGraph demonstrates durable workflow/checkpoint mechanics. Rerun demonstrates persistent multi-coworker configuration, memory, team communication and shared provider connections. Foromni's research gap remains the **portable objective → relationship/dependency → authenticated work attempt → source/evidence → independent acceptance → real-world outcome contract** across any of them.

Sources:
- [LangGraph README](https://github.com/langchain-ai/langgraph/blob/c6335a4255dc1d8abc25a7677f9c072c7ab27b9c/README.md)
- [LangGraph AGENTS.md](https://github.com/langchain-ai/langgraph/blob/c6335a4255dc1d8abc25a7677f9c072c7ab27b9c/AGENTS.md)
- [Checkpoint README](https://github.com/langchain-ai/langgraph/blob/c6335a4255dc1d8abc25a7677f9c072c7ab27b9c/libs/checkpoint/README.md)

## 6. Comparative learning matrix

| Dimension | Rerun | OpenHands current ecosystem | LangGraph | Foromni open research |
|---|---|---|---|---|
| Persistent coworker/agent config | Documented per-agent dirs and run IDs | Agent/conversation execution under SDK, Canvas supports multiple backends | Threads and checkpoints, not a universal agent employee registry | Durable logical agent registry linked to authenticated work attempts |
| Multi-agent handoff | `call_agent`, `delegate_tasks` | Agents/automations/ACP through several repos | Durable graphs and handoff as application-defined nodes | Standardized versioned tasks/dependencies/ownership |
| Human governance | Product approvals reported | Human-only PR section and separate verify skill guidance | HITL interrupt/resume primitives | Enforceable policy outside model |
| Integration | Third-party tools and GitHub connector | SDK API → typed client → Canvas; GitHub automations | Runtime; not Git forge integration by default | Exact-source Git QA and protected convergence |
| Recovery | Run status and persistent coworker data | Agent server and automation lifecycle (details merit deeper study) | Graph checkpoints and pending writes | Durable retries plus source/ref reconciliation and lease fencing |
| Security | Per-agent tools, Vault; shared engine risk questions | Sandbox/no-sandbox explicitly documented; contributor QA independence normative | Durable state serialized; deserialization trust cautions | Trust boundaries, prompt injection gate, action-time authority |
| Contribution opportunity | Docs/fixes and external handoff provenance | Contract/evaluation docs or adapter review in owning repo | Checkpoint reliability/SDK correctness and safe replay docs | Source-backed empirical studies and minimal interoperability adapters |

Rows are high-level comparisons from visible documentation, **not a scored product benchmark**.

## 7. Collaboration opportunities ranked by value and burden (not a request to contact)

**A. High fit, low intrusion — source-linked knowledge contribution.** Publish an accurate, respectful study that cites OpenHands' actual repo ownership and independent verification rules, and invite technical correction only after Foromni review. Could help users understand correct repo routing.

**B. High fit, bounded artifact — reproducibility/acceptance test examples.** Propose a synthetic example demonstrating that a changed backend field must propagate Agent Server → typed client → Canvas, including a separately maintained negative test. Only after checking existing issues and obtaining maintainer interest.

**C. Medium fit — provenance metadata standard.** Explore a neutral `agent_id + attempt_id + task revision + source_sha + QA verdict` event that external orchestrators can produce without core modifications. Avoid expanding OpenHands public APIs without maintainers' invitation.

**D. Longer-term — cross-ecosystem AINO benchmark.** With permission, compare equivalent tasks executed using Rerun/OpenHands and possibly a LangGraph-driven controller under identical independently accepted outcomes and total cost. Do not manufacture cross-project results or imply involvement before consent.

**E. Later — optional Foromni network participation.** A relationship is voluntary, potentially only educational/technical, and never a condition of contributing. Avoid implying partnership or endorsement.

## 8. What not to do

- Do not say OpenHands or LangGraph have 'solved AINO coordination' merely because they offer agents/workflows.
- Do not copy their code or claim benchmarks without a running, permissioned experiment.
- Do not submit outreach, issues, PRs, integration patches or depend on their maintainers' time without explicit permission.
- Do not assume `AGENTS.md` prose makes a protected security boundary.
- Do not use an old tutorial's single-monorepo OpenHands model for the newly split current codebase.
- Do not interpret local/no-sandbox option as a recommended secure default.
- Do not confuse LangGraph `thread_id` with independently authenticated real-world contributor identity.

## 9. Specific next source-inspection questions

1. Which OpenHands `automation` records tie a schedule/webhook to a real agent conversation, output and GitHub source revision?
2. How does the SDK persist conversation/execution identity, state and error recovery?
3. What actual CI enforces verify-skill separate-context and `HUMAN:` source provenance? If it is only convention, mark the gap as enforcement unverified.
4. Which ACP backend capabilities can be discovered at runtime without brittle provider-specific branching?
5. Are there current maintainer-requested docs or test improvements in the right owning repository?
6. Could a minimal external evidence envelope map Rerun coworker IDs, OpenHands conversation IDs and LangGraph thread IDs to a stable Foromni agent registry ID without leaking private user data?

## Conclusion

The most valuable finding is **architectural specialization**. Mature OSS projects separate agent execution, runtime durability, connectors, UI, and ownership domains. Foromni should seek the unifying organizational/evidence contract that sits **across** these systems, rather than duplicate them.

**Study their interfaces, make a useful contribution when welcome, and let collaboration emerge from demonstrated value.**

*Build today, so others can enjoy tomorrow.* ❤️🐂
