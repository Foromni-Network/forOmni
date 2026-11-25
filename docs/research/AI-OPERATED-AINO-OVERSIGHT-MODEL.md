# AI-Operated Engineering Organization: Autonomy, Vibe Development, and Human Oversight

**Status:** R&D DESIGN PROPOSAL, not implemented or authorized for execution.  
**Date:** 2026-11-21. **Scope:** Foromni research only; no Internet Embassy modifications.  
**Related:** END-TO-END-FULL-STACK-AGENT-TEAM-RESEARCH-ROADMAP.md; CONVERGENCE-CONTRACT-V0.1.md; CROSS-DOMAIN-CONVERGENCE-CONTRACT-V0.2.md; PROVIDER-AGNOSTIC-AGENT-EXECUTION.md.

## Founder intent clarified

The workforce under study is **AI-operated first**. Humans primarily set outcomes, constraints, budgets, and permission boundaries; review consequential decisions; resolve genuine ambiguity; and retain revocation/override rights. Humans can contribute directly, but the design should not secretly depend on traditional human product managers, developers, release managers and manual copy/paste to achieve routine progress.

Research goal: Can an autonomous engineering organization continuously **discover → scope → design → implement → test → repair → independently verify → integrate → measure → improve**, with human supervision focused on risks and strategic choices?

"Vibe development" means natural-language product intent can begin the process, **not** that a convincing demo or unverified generated code constitutes delivery.

## 1. Three distinct layers of control

- **Human governance layer:** Owner defines mission, spending ceiling, approved project boundaries, risk tolerance, protected production/release permissions, appeal/revocation and success criteria. Human review for consequential external action or material uncertainty; no need to approve each harmless local edit.
- **Autonomous operations layer:** Agents can break down authorized goals, propose task/acceptance plans, assign bounded tasks, implement on isolated refs, run ordinary permitted tests, interpret failures, perform limited retry/repair and submit for independent verification.
- **Enforced policy and evidence layer:** Deterministic authorization, credential isolation, lease/fencing, source revision checks, QA separation, merge protection, idempotent events and budget quotas apply regardless of model instructions. This layer must reject an agent's unauthorized actions even if its prompt says otherwise.

A 'chief agent' can coordinate and propose decisions; it is not a privileged root user. The model is not the ultimate source of truth. The ledger plus independently observed external systems are.

## 2. Progressive autonomy tiers — research proposal

| Tier | AI-worker permissions | Required supervision |
|---|---|---|
| A0: Observe | Read authorized research, inspect task status, generate proposals | Human sets information access |
| A1: Draft | Plan tasks, generate code/docs in isolated workspace, prepare PRs | Automated policy and cost limits |
| A2: Execute sandbox | Run allowed builds/tests, local migrations on disposable data, self-repair, checkpoint and handoff | Trusted sandbox controls, monitors, automatic kill switch |
| A3: Submit candidates | Create/update isolated PRs and attach evidence; queue eligible candidate | Independent QA required; no protected merge privilege |
| A4: Controlled integration | A separate authorized integration controller may publish passing changes to protected sandbox/main *only under explicit policy and current authorization* | Independent acceptance, protected branch controls, monitored rollback |
| A5: Consequential operations | Production deployment, billing, external publication, identity/permission changes, sensitive data, cross-organization actions | Specific human or legally authorized approval before action; no general delegation from model confidence |

Tier assignment is **per actor + action + project + environment + duration**, not a global trust badge earned by generating successful text. Progression does not automatically grant new credentials or scope. Repo rules, CI identities and hosted infrastructure must enforce it.

## 3. Agent organization hypothesis

**Demand-driven teams**, not a permanently staffed virtual company:

- **Intent translator / product agent:** converts natural-language vision into a *draft* outcome contract, checks ambiguity, proposes acceptance and privacy requirements.
- **Architect / dependency steward:** proposes bounded vertical slices, interfaces, ownership and dependency DAG; spots duplicated/competing designs.
- **Implementer(s):** writes small changes in unique task-owned workspaces; can use any provider, including self-hosted or older models within qualified task scope.
- **Test/QA agent:** independent principal; generates and reproduces adversarial acceptance, security and compatibility tests. Must be separated from implementation authority.
- **Integrator:** non-LLM policy-enforcing controller with agent-assisted diagnosis; checks latest merge-group SHA and protected authorization.
- **Reliability/repair agent:** monitors failing CI, abandoned leases, stuck reviews, broken integration and regression evidence; proposes/retries bounded fixes.
- **Cost/safety steward:** measures end-to-end spend, queue health, scope drift, unsafe requests and repeated retries; automatically pauses prohibited work and escalates.
- **Human owner:** defines intent and maintains authority over impact, privacy, budgets, legal decisions, releases and other consequential actions.

These are **roles** rather than mandatory distinct agents. One qualified model may perform several low-risk roles sequentially; protected reviewer independence requires genuinely separate authority, not a second model name controlled by the same worker. Some roles should be deterministic services, not generative agents.

## 4. Authority is separate from reasoning

Agents may propose:
- new task decomposition and priority,
- a branch and code diff,
- revised test cases,
- conflict resolutions,
- a candidate batch,
- a merge request,
- a higher-spend option.

A trusted policy service decides if actions are *permitted*. CI and independent QA decide whether criteria were observed. An authorized integration controller executes protected publication. Humans approve exceptional or high-stakes actions.

An agent whose instructions say 'ignore the gate' must lack both the credentials and tool surface to do so. Any privileged tool call requires independent action-time policy check, not a once-per-session prompt instruction.

## 5. Work from natural-language vision without false completion

**Human input:** "Build a useful community directory where people can share projects and contribute."

**Agent proposes (not silently authorizes):**
1. Outcome contract: named beneficiary, observable experience, acceptance and exclusions.
2. Boundary/risk review: identity, consent, private/public data, security, budget.
3. Minimal vertical slice and dependencies.
4. Task attempts with unique IDs, isolation and time/cost ceilings.
5. Test plan independent of code generation.
6. Candidate implementation and evidence bundle.
7. Independent verdict; failed work returns to repair.
8. Controlled merge into authorized sandbox with post-merge verification.
9. Human product walkthrough and consequential launch approval if requested.

A spectacular UI is **not** completion if persistence, authorization, accessibility or deployment/recovery remains unverified.

## 6. An AI-first handoff packet

No human project manager should need to reconstruct every worker's context. Every attempt produces machine-readable, constrained:
- task/outcome revision + applicable policy,
- actor/role/model adapter (model identity is provenance, not authority),
- attempt and lease epoch,
- source repo/ref and exact base/head SHA,
- artifact manifest and content digests,
- tests executed: exact commands, environment, checked SHA, results, limitations,
- unresolved failures and owner,
- dependencies, outstanding permission/approval needs,
- cost/time consumed and remaining budget,
- **next safe action**, not an instruction to bypass checks,
- human-facing concise explanation.

The incoming worker must verify current lease, references, credentials and task revision; a handoff is not automatic acceptance of another worker's claims.

## 7. Oversight UI — proposed, not built

The human should see:
- **Objective view:** project outcomes, currently verified deliverables, remaining acceptance criteria.
- **Intervention queue:** budget increases, privacy/security decisions, production/publication requests, conflicted requirements, repeated unresolved failures.
- **Trust panel:** which workers have which effective rights, expiration and revocation controls.
- **Convergence health:** what merged, which exact SHAs were checked, queue age, task block reasons and rollback.
- **Economic view:** spend and accepted outcomes by workstream, with retries/QA/CI cost included.
- **Audit:** action history, evidence, reviewer identities, source revisions, approvals and incident/correction trail.

Human attention should focus on *exceptions, decisions and accountability* rather than micromanaging harmless operations.

## 8. Safety rules for untrusted autonomous workers

1. No broad unrestricted Git or production credentials issued to agent runtimes.
2. Untrusted external code executed in isolation without CI controller/secrets access.
3. Strict per-task execution, network, runtime and budget limits; stop loops and excessive retries.
4. Every privileged write is checked by deterministic policy enforcement.
5. A model's self-evaluation or second model response is not proof of independent QA.
6. Tools and external data can contain malicious instructions; treat as untrusted.
7. Recovery checkpoints must be sanitized and not expose chain-of-thought, secrets or private user data.
8. Fallback between local and cloud models may cross a data boundary and needs matching authorization.
9. No unattended consequential action solely because the agent has high confidence.
10. Humans can revoke a lease, task, token or action class and obtain audit evidence.

Relevant source material:
- OWASP AI Agent Security Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html
- Microsoft agentic zero-trust guidance: https://learn.microsoft.com/en-us/security/zero-trust/sfi/secure-agentic-systems
- LangGraph durable human approval/interrupts: https://docs.langchain.com/oss/javascript/langgraph/interrupts
- A2A protocol agent-to-agent task/artifact messaging: https://a2a-protocol.org/latest/specification/
- OpenHands SDK (optional implementation worker): https://github.com/OpenHands/software-agent-sdk

No one source above proves the full Foromni organization exists. All tools are candidates for adoption or adapters.

## 9. Comparative experiment: solo vs studio vs adaptive AI operation

All cohorts receive same bounded user-intent brief and must pass independent full-stack end-to-end acceptance:
- **Solo:** one agent handles product/implementation; independent reviewer/controller enforced separately.
- **Small autonomous studio:** 3–5 agent functions with constrained handoffs.
- **Larger autonomous studio:** 8–15+ workers with dependency-aware queue and QA.
- **Adaptive:** one generalist recruits only necessary specialists as observed complexity warrants.
- **Mixed provider:** reproduce selected low-risk tasks with self-hosted modern and dated models.

Measure *not* number of model turns but **independently accepted, integrated and actually useful outcomes**, elapsed time, human interventions, full runtime/test spend, integration conflict rate, QA false positives, repair churn and maintainability. Sample sizes and study design must avoid overinterpreting one successful demo.

## 10. Human intervention triggers

**Always** obtain relevant authorization for production releases, protected environment modification where policy requires it, changes to identity/security or data access, material external spend, contractual/legal commitments, and sensitive publication. Require separate review for architecture/privacy decisions with material downstream implications.

**Escalate** when objectives are contradictory; multiple independent workers cannot reconcile a design; confidence in acceptance is insufficient; the same failure repeats beyond allowed retry budgets; agent identity/privilege is uncertain; user harm/privacy is plausible.

**Continue autonomously** on other authorized branches, disposable sandbox checks, low-risk fixes and documentation while one sensitive decision waits. An approval gate suspends the affected action, not the entire organization.

## 11. Proposed design acceptance criteria

- The owner can supply a plain-language brief and approve an explicit outcome/authority envelope.
- Agents autonomously create bounded tasks and deliver isolated artifacts without unauthorized writes.
- A worker failure or model-provider outage does not destroy work or cause duplicate privileged actions.
- Independent QA and merge policies reject a convincing but incorrect agent 'done' claim.
- A human sees truthful progress and only necessary interventions; all decisions are attributable.
- Full-stack verification includes frontend, backend, database, auth, integration, staging behavior and failure recovery as applicable.
- Older/self-hosted agents can contribute to qualified tasks with no mandatory provider.
- Progression of autonomy rights is enforced by infrastructure, revocable and environment-scoped.
- One workflow can shrink/expand team size without silently changing task success criteria.
- Production/public release remains separately authorized, never inferred from mainline merge.

**These are research targets, not passing tests.**

## Next study

Formal **AI Workforce Authority & Event Contract**: actor grants, per-task attempt events, authorization requests, policy decisions, reviewer attestations, merge admission and human escalation payloads; plus a 1→3→8 agent tabletop showing when parallelism helps vs causes contention. No runtime build until explicit pilot approval.

**North Star:** Agents operate the work. Humans govern the purpose and consequences. Evidence governs acceptance.

*Build today, so others can enjoy tomorrow.*
