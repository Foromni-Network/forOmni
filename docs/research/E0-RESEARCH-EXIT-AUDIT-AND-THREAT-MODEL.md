# Full-Stack E0 Research Exit Audit and Threat-Model Checklist

**Status:** Independent-review checklist; findings not yet validated.  
**Date:** 2026-11-21. **Project:** Foromni only; no IE systems or artifacts accessed.
**Linked:** E0-PILOT-ARCHITECTURE-DECISION-ADR-001.md, FULL-STACK-CONVERGENCE-TRIAL-PREREGISTRATION-V0.1.md, FULL-STACK-REFERENCE-APP-CONFORMANCE-V0.2.md, CONVERGENCE-WORK-PACKET-TYPED-CONTRACT-V0.2.md.

## The decision we are not yet allowed to claim

A growing library of research does not show that one complete full-stack AI development process is ready for a trustworthy experiment. This audit names open questions and the exact evidence needed for a future human-governed go/no-go review. Nothing in this file authorizes development, tests, merges, deployment, external publishing or access to confidential data.

## Proposed exit audit

| Gate | Evidence required before approved trial | Current assessment |
|---|---|---|
| A. Objective and use case | Approved fixed Collective Lab behavior, user/role matrix and expected outcome | Candidate specification only — review pending |
| B. Product/API contracts | Exact response schemas, pagination/version/error rules, session/invitation lifecycle | Partial; some API details unresolved |
| C. Architecture | Accepted ADR, current versions/lockfiles and reproducible clean setup | Candidate ADR; no implementation evidence |
| D. Worker placement | Selected isolation mechanism, model/runtime constraints, storage/network policies | Hosting study only; no evaluated sandbox |
| E. Work packet + delegation | Structured fields, freshness/lease decision semantics, effective principal scopes | Typed draft; not executable or security-verified |
| F. Independent QA | Separate principal, immutable hidden test suite, reproducible browser/API/security check cases | QA design only; no runner/provenance proof |
| G. Protected integration | Host feature check, required status configuration, exact prospective merge-group verification | No actual protection configuration audit |
| H. Reproducibility | Fixed dataset/migration reset, resource caps, deterministic setup and teardown | Planned, not measured |
| I. Threat review | Principals/assets/trust boundaries, specific attacks and mitigations assessed | Draft model below; independent review pending |
| J. Econometric protocol | Matching/randomization, repeated task strata, failures and censoring, full cost denominator | Preregistration draft; sample/analysis plan not frozen |
| K. Human authorization | Exact allowed repo/runtime, tool/network limits, cost cap, access and stop conditions | Not given |
| L. Publication | Claim provenance, independent assessment, rights and correction support | Publication contract draft; no empirical results |

**Result: NOT READY FOR EXECUTION.** This is a research assessment, not a completed security audit. No gate in the table has been independently verified in a running system.

## Threat model: minimum attack paths

### Assets that must be protected
- The protected mainline and history; task/requirements acceptance state.
- Independent evaluation suite, scoring rubric and raw test evidence.
- Worker and evaluator credentials, identity/lease permissions, secrets and billing controls.
- Database contents, including even synthetic fixtures when reused across workers.
- Run logs, model prompts, artifact attestations and any future human/collective data.
- Publish and deployment authority.

### Trust boundaries and concrete cases

| Boundary | Failure/attack | Required invariant | Research mitigation |
|---|---|---|---|
| Natural-language instructions → work packet | Prompt injection or source comments impersonate governance | No untrusted text becomes effective grant | Separate trusted policy service; explicit authenticated owner decisions |
| Planner → worker | Packet claims broad path/lease scope | Claimed paths alone grant nothing | Real scoped credentials and server-checked lease/epoch |
| Worker → source/CI | Generated code runs malicious commands, reads host secrets | No privilege or secret escalation from trial code | Ephemeral isolated runner, limited egress, no mounted privileged host socket |
| Worker → evaluator | Worker alters hidden tests or forges green result | Authoritative acceptance outside worker authority | Separate QA principal and evidence store; exact-source verdict |
| Database/auth | RLS bypass via elevated service key or missing policy | Cross-project access denied server-side | Privileged keys isolated; independent role-matrix negative cases |
| Git merge admission | Stale source checked; current main changed | Required checks bind to prospective merge state | Host-enforced protected queue and current group checks |
| Retry/recovery | Controller retries a merge after lost ACK | No ambiguous duplicate state transition | Read actual Git ref, idempotency/fencing, durable event provenance |
| Cost/model tools | Infinite retry loop or unapproved provider transfer | Effective budget and data egress limits | Provider/runtime ceilings, not only prompt-level guidance |
| Observability | Log captures secret or incorrectly claims success | Minimize sensitive data; statuses reflect real observation | Redaction and readback reconciliation |
| Publication | Simulation presented as measured proof | Public claim linked to actual evidence and rights | Separate publication authorization and claim ledger |

### Required negative-case review
The independent reviewer must demonstrate what should happen when a worker requests protected main write, a stale grant is replayed, a synthetic account crosses project boundaries, the source SHA differs from the QA-tested one, the QA principal equals the implementer, a backend contract changes under an active UI task, or a teardown operation is ambiguously pointed at a remote database. **The tests remain to be designed, not run.**

## Minimum acceptable bounded first trial

A one-agent synthetic full-stack smoke experiment with genuinely independent QA and protected Git candidate admission is the **smallest evidence-producing slice** worth asking permission to run. One worker can still have separate independent reviewer services; that does not turn it into an eight-agent study.

The future authorization request must be unambiguous about the chosen repository, isolated runtime, permitted external calls, data, spending cap, source-control actions, reviewer ownership, stop criteria and whether any staging deployment is permitted. Public deployment/marketing and project-to-project data exchange must default to not permitted.

## Econometric constraints to freeze

Primary: independently accepted integrated behaviors per full observed cost plus completion probability by a prespecified horizon. Handle missing cost and noncompletions explicitly rather than reporting only successes.

A baseline one-agent trial tests *reproducibility*; it cannot establish the causal benefit of convergence-first coordination. For that, run paired/randomized control and treatment trials with equivalent inputs and independent evaluation. Large team, hosting and backend comparisons follow only after E0 repeatability.

## Actionable research gap queue — not new canonical tasks

1. Resolve exact API pagination/identity/invitation/version-error choices and freeze product behavior.
2. Independently review the candidate Supabase local/RLS versus vanilla Postgres/adapter tradeoff and current support/security.
3. Map which Git host rules can be relied upon in a disposable experiment repository.
4. Specify evaluator isolation, controlled test scripts and hidden-fixture ownership.
5. Write strict host cleanup/credential revocation requirements and prove they can be observed.
6. Confirm the first trial's unit, budget, execution/stop rules and evidence collection.
7. Request explicit bounded founder authorization *after* gaps above are resolved.

The broader agent-to-agent communication protocol remains next-topic research, not a competing P0. Dedicated cybersecurity products remain future R&D; baseline security of this experimental system is inseparable from P0.

**Research conclusion:** A good coordinator reduces avoidable ambiguity, but honest experiments need a durable source of truth, independently verifiable boundaries, and explicit treatment of uncertainty. Study those first.

*Build today, so others can enjoy tomorrow.*
