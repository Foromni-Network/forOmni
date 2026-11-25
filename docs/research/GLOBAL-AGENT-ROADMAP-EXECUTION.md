# Research: Global Agent Roadmap Execution as Foromni's Foundational Utility

**Status:** Research proposal — not an accepted architecture decision or implementation authorization  
**Date:** 2026-11-20  
**Repository:** `Foromni-Network/forOmni`  
**Scope:** Foromni only; IE remains isolated and must not be modified or merged  
**Priority:** P0: prove roadmap-to-completion before expanding feature development

## Executive conclusion

The hardest problem is not generating tasks, scheduling agents, or showing a board. It is enabling geographically and organizationally distributed human/AI workers to **reliably take a task from a verifiable definition of done to independently proven completion**, despite concurrency, downtime, poor-quality claims, multiple runtimes, different trust levels and revisions of work.

**Recommendation (hypothesis to test):** Build the smallest vendor-neutral **Roadmap Execution Protocol and Evidence Ledger** before building a broad network app or general autonomous-agent orchestration platform. Treat the roadmap as a dependency graph plus a verifiable event trail, not a sequence of self-reported status fields. Use existing workflow, repository and communication technologies rather than inventing new equivalents prematurely.

A roadmap is **not** a task queue. An execution agent's "completed" result is **not** acceptance. A passing test is **not** the same as integration. An accepted change is **not** necessarily a released capability.

## 1. Research questions and hard constraints

1. How can agents running different vendors, models, locales, organizations and time zones coordinate on the same roadmap without sharing proprietary prompts, secrets or source control?
2. Who owns a task, and how do other workers detect expiration, duplicate attempts, conflicting edits, stale evidence and lost context?
3. Who has authority to change states, approve sensitive actions, and accept a finished task?
4. What machine-verifiable evidence demonstrates the acceptance criteria rather than simply asserting completion?
5. How can a worker restart after interruption, transfer a task, and retain enough context for an unrelated worker to continue?
6. How does the system reconcile GitHub, CI, databases and releases without writing over authoritative changes?
7. How can the system measure task value, cost, successful outcomes, regressions and time stuck at each gate?
8. Can an outside agent participate with low trust and limited permission without exposing internal resources?

Constraints: Foromni owns its own governance and task state; no IE merge or dependency. Human approval for production, privileged access, external communications, protected code merges, material spending and sensitive data operations. Fail closed on unverifiable evidence. Keep permanent provenance and repair history.

## 2. Findings from existing solutions

| Building block | Demonstrated capability | What it does NOT solve alone | Recommended role |
|---|---|---|---|
| GitHub Issues + Projects + PRs + Actions + branch protection | Issue-to-code linkage, visual roadmaps, review, CI, merge policy; API and automation | Cross-provider execution leases; independent acceptance semantics; global task event reconciliation | Initial developer-facing surface, canonical source-control evidence |
| A2A protocol | Independent agents exchange messages, task state, artifacts, and long-running updates | Foromni roadmap ownership, task acceptance, audit/evidence policy or source-code governance | Candidate communication adapter; not system of record |
| MCP | Standardized tool/resource connectivity with OAuth-based HTTP authorization | Agent-to-agent task governance or a global roadmap | Constrained tool access for authorized workers |
| Temporal | Durable workflows, retries, worker failure recovery, history, signals/updates | Which business evidence proves roadmap acceptance or who is authorized to approve | Later orchestration option *if* simpler GitHub/webhook pilot proves insufficient |
| LangGraph/Deep Agents | Checkpoints, interrupts, bounded agent execution and sandbox patterns | A neutral shared cross-vendor roadmapping authority | Optional internal worker runtime, never required membership |
| OpenTelemetry GenAI semantic conventions | Common trace/model/tool/token telemetry | Outcome correctness, acceptance criteria or product value | Cost, latency, traceability and operational reporting |
| OpenAI Agents SDK | Agent handoffs, session continuations and tracing | Multi-organization authorization and authoritative completion | Optional worker integration, not Foromni's mandatory framework |

**Important boundary:** A2A task states describe the remote execution's progress; Foromni task admission statuses describe acceptance in the roadmap. They must be separate IDs and state machines.

**Source references (checked 2026-11-20):**

- GitHub Projects: https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects
- GitHub branch protections: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- GitHub App least-privilege permissions: https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app
- A2A specification: https://a2a-protocol.org/dev/specification/
- MCP authorization specification (2026-07-28): https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization
- Temporal durable execution: https://docs.temporal.io/durable-execution
- Temporal design patterns: https://docs.temporal.io/design-patterns
- LangGraph durability and human-in-the-loop: https://docs.langchain.com/oss/javascript/langgraph/thinking-in-langgraph
- OpenAI Agents SDK running and handoffs: https://openai.github.io/openai-agents-python/running_agents/
- OpenTelemetry GenAI instrumentation: https://opentelemetry.io/blog/2026/agent-harness-genai-instrumentation/

These sources document capabilities; they do not prove an integrated Foromni system exists.

## 3. Core model: five separate objects, not one task row

1. **Roadmap Task**: stable ID, project scope, requirements, acceptance criteria, priority, dependencies, authority policy, owner/custodian, requested outcomes, due/review time, current *admission* state. Versioned specification.
2. **Execution Attempt**: separately identified run that claims a specific task revision, worker identity, lease/fencing token, start/end, checkpoints, cost budget, outputs and reason for stopping. Multiple attempts can belong to one task; no simultaneous uncoordinated write authority.
3. **Artifact/Evidence Bundle**: immutable or content-addressed links to commits, CI runs, test commands, acceptance assertions, build artifacts, review decisions, deployment hashes, verifiable external outcomes and environment signatures.
4. **Decision/Admission Event**: independent verifier identity, rule version, exact task/attempt/artifact versions, finding, reason, time and authority; append-only and auditable. Status is a projection derived from accepted events, not a free-form assertion.
5. **Dependency/Integration Record**: linked upstream tasks, compatibility versions, validation cohort, base revision, resulting integration commit, sandbox checks, rollback and release decision.

Additional concepts: actor/organization identity; capability profile (what worker can do, with evidence); project membership; scoped authorization; task comments; escalation; approval decision; cost/trace record.

## 4. Proposed lifecycle: task vs execution vs verification

**Task admission lifecycle (candidate, not imposed on any existing project):**

`proposed → scoped → ready → leased → implementation_review → batch_ready → build_verified → independent_qa → integration_ready → sandbox_integrated → released → closed`.

Failures generate explicit events and return to a repairable state; no destructive status rewriting. Alternative shorter vocabulary can be chosen after tests. `blocked`, `awaiting_approval`, `stale` and `rejected` may be orthogonal *conditions* rather than permanent lifecycle stages.

**Execution attempt lifecycle:** `offered → claimed → running → checkpointed → submitted | failed | cancelled | expired`.

**Verifier verdicts:** `unverified | pass | fail | inconclusive | invalidated_by_new_revision`.

Do not conflate these: an agent may submit completed work while the roadmap task remains in review. A CI pass on SHA A is invalidated as evidence for changed SHA B unless the applicable evidence scope explicitly permits it. Post-integration tests must target the integrated result, not only source PR commits.

## 5. Reliable world-wide assignment and handoff

**Discovery:** A worker advertises a signed/policy-bound capability profile, organization, supported tools, languages, rate/cost limits and privacy constraints. Claims are not trusted without evidence.

**Assignment:** A scheduler/human selects eligible work based on dependencies, priority, capabilities, budgets, trust level and least-privilege policy. Phase 1: manual or rule-based selection before autonomous brokerage.

**Leases:** Workers request a bounded lease with `task_id`, `task_version`, `actor_id`, `attempt_id`, `lease_expires_at` and monotonically increasing **fencing token**. Only the current token can mutate attempt-owned fields or submit exclusive candidate artifacts. Heartbeats renew leases. After expiry the task is eligible for re-claim; the old worker's write attempts must be rejected.

**Idempotency:** All state-changing requests carry a stable idempotency key. State updates use compare-and-swap/version checks to reject stale clients. Duplicated webhooks and out-of-order events should not generate duplicate transitions. Treat queue delivery as at-least-once; enforce side-effect idempotence where technically possible.

**Checkpoint/handoff packet:** Must fit a short, standardized manifest: task ID/revision; intent and measurable acceptance; exact base/head SHAs; scope of already-changed files; executed commands/results; open failures; environment/setup references; current dependencies; safe next action; cost; lease/expiry and handoff actor; sanitized context. Do not rely on transmitting full private conversation histories.

**Cross-time-zone execution:** UTC timestamps, explicit availability windows, asynchronous event stream, predictable lease expiration and requeue, public or consent-based language metadata, and no assumptions that a handoff means the receiving agent accepted the work.

**Contributors outside trusted organizations:** Start with read-only tasks, proposals, issue triage and test reproduction. Authorize writes only to an isolated branch or scoped repository. Credentials never cross organizations. Privileged work requires attestation/approval under policy.

## 6. How to prove completion

A task is eligible for a given gate only if all required acceptance checks are supported by **evidence bound to the exact specification and code revision**:

- Acceptance criteria expressed as checkable statements with a named verifier and expected evidence type.
- Test run identity, command, exit status, target revision and environment, not just an agent narrative.
- Reproducible build/typecheck/security checks.
- Branch/PR review and approval roles, if relevant.
- Dependency and compatibility evidence for the candidate batch.
- Sandbox integration on *the integrated SHA* followed by post-integration acceptance.
- Release approval and deployment evidence, when required.
- An independently authorized verifier must make a separate judgment; author and verifier cannot be the same principal for protected gates.

**Evidence is not binary:** differentiate `claimed`, `generated`, `observed`, `independently_reproduced`, `accepted`. A URL to a test run can be structurally valid yet dishonest, inaccessible or for the wrong SHA. Validate its content, execution provenance and permissions.

**Repair loop:** A failing verifier event identifies failed criteria, exact revision, logs and owner; the task remains discoverable, generates a new attempt, and resubmits without erasing failures. Limit blind retry storms; escalate repeated identical failures or expired leases.

## 7. Architecture options and recommendation

### Option A — GitHub-first proof of concept (recommended first)
GitHub Issues/Projects for visibility, PRs/Actions for source-control proof, a tiny immutable event/evidence manifest in a Foromni-owned repository or authorized durable store, and manual/rule-based verifier gates. Build no new generalized task UI initially.

- Pros: small surface, immediately inspectable work/evidence, GitHub-native contributor path.
- Cons: repository writes are not a high-throughput concurrency datastore, GitHub does not natively enforce agent leases or multi-org governance, and external/non-code tasks need separate evidence stores.
- Decision: best **research/pilot** option, not automatic long-term architecture.

### Option B — Event-ledger service with Postgres and GitHub projection
Foromni-owned transactional task/event DB; GitHub issues/PRs/CI sync as read-models and evidence sources; least-privilege API; versioned projections and independently owned gate controller.

- Pros: atomic leases, fencing, concurrency, auditability, cross-platform tasks.
- Cons: significant security, operations, multi-tenancy and reconciliation burden; difficult to justify before A proves failure cases.
- Decision: likely medium-term if pilot measures show need.

### Option C — Workflow-engine-centered orchestration (Temporal or similar)
Use a durable workflow per task/integration cohort plus explicit event/evidence policy.

- Pros: mature resumption, retries, approvals and timeouts.
- Cons: workflow engine is not the source of truth for acceptance; adoption and runtime complexity.
- Decision: optional execution backbone after researching scale/durability needs; do **not** couple the public protocol to one vendor.

**Preferred layering:**

```text
Independent agents / human contributors (any framework, any time zone)
          |
Identity + trust policies + narrowly scoped authorization
          |
Task contract API / events / A2A adapter / MCP tool adapter
          |
Foromni-owned task & attempt ledger + leases + dependency rules
          |
Evidence bundles + independent admission gate + integration controller
          |
GitHub / CI / sandbox / other actual systems of record
          |
Read-only roadmap projections, dashboards, outcome/cost reports
```

Contribute interfaces, reference fixtures and adapters before offering centralized hosted brokerage to strangers.

## 8. Explicit failure modes to research and simulate

| Failure | Must-have invariant |
|---|---|
| Two agents claim same task | Exactly one current write lease/fencing token; both attempts auditable |
| Worker disappears mid-task | Requeue after expiry; context and artifacts remain; no fake completion |
| Expired agent submits later | Stale token rejected |
| Same webhook arrives 3 times | No duplicated status or side effects |
| CI passes old SHA | Candidate stays unverified on new SHA |
| Developer self-approves | Independent gate refuses |
| PR tests pass but integration fails | Status returns to repair with integration evidence |
| Dependency is changed after candidate approval | Dependent admission invalidated or reevaluated |
| Untrusted agent requests broader permission | Denied; recorded without granting tool access |
| Human approval remains pending | Only gated action waits; unrelated tasks advance |
| Task closure later proves defective | Reopen/incident linked without deleting prior accepted evidence |
| Budget exhausted or retry loop | Suspend execution and require new budget/policy decision |
| Agent falsely reports pass | External verifier rejects unsupported assertion |
| Two repositories disagree | Defined authority rule + reconciliation report, never silent overwrite |

## 9. Proposed research-only phased validation plan

**R0 — Validate problem framing (no implementation):** Interview/compare 3+ actual workflow failures, including stale checks, unowned tasks, agent timeouts, and optimistic statuses. Map each to an invariant and source of evidence.

**R1 — Formalize protocol (documentation only):** Publish versioned task, attempt, evidence and decision JSON Schemas *as a proposal*; define authority matrix, allowed transitions, expiry and conflict policy, and replay/reconciliation cases.

**R2 — Tabletop replay (research fixtures only):** Work through 12 failure scenarios above with manually authored synthetic events; determine whether independent observers reach the same task state. No production tokens, repositories or deployments.

**R3 — Isolated small technical spike (requires separate authorization):** 3 unrelated agents, 2 separate runtimes, 10 synthetic tasks, 2 competing claims, 1 interrupted worker, 2 failed checks, 1 integration candidate, 1 required human gate. Demonstrate no duplicate exclusive ownership and zero unsupported green statuses.

**R4 — Measured multi-agent pilot (separate authorization):** 3+ organizations/time zones, portable task manifests and explicit opt-in participation, independent reproducible evidence, concurrency/load/privacy testing, cost accounting and fallback recovery.

**R5 — Productization decision:** Select GitHub-first versus transactional event service versus durable workflow engine only with recorded experimental results.

**Success criteria for authorizing major feature development:**
- Every task can be traced to an existing immutable ID and versioned acceptance contract.
- 100% of protected state transitions have independently verifiable evidence.
- Zero stale-SHA approvals and zero unauthorized cross-project/production actions in adversarial trials.
- Interrupted workers resume or safely requeue without losing committed progress.
- Independent agents can hand off using a small standard packet, without sharing internal prompts or secrets.
- Repeated failures are visible and actively assigned; tasks do not sit indefinitely with no recovery path.
- Measurable completion-to-integration rate and cost per accepted task, not only tasks authored or PRs opened.

These are **test targets**, not measured results.

## 10. Risks and open decisions

- Identity proof and worker reputation without surveillance or global centralization.
- Who can attest to independent QA, including when agents share the same operator.
- Whether GitHub issue/project state is human-facing only or has authoritative aspects.
- Task/evidence retention, right to delete sensitive operational traces and public/private partitions.
- License for the proposed shared task schema; review before inviting open external contributions.
- Cost responsibility, malicious workers, sybil claims, reputation gaming and denial of service.
- How to define acceptance for creative, interpersonal or offline outcomes without false mechanistic confidence.
- What is truly decentralized: independent workers and data ownership vs one common coordination API.
- A2A version and MCP profile compatibility; their task status semantics should not be copied directly.

## 11. Decision requested before any major implementation

Adopt **roadmap execution and verified task closure as Foromni's first core utility**. Keep the current workstream research/documentation only. Do not build a general app, cross-project integration, hosted agent marketplace or autonomous production system before a small verified protocol is demonstrated.

Next documentation deliverables: authority matrix, task/evidence schema proposal, state transition decision table, failure-injection scenario fixtures, and a comparison of 2–3 real task-management failure histories.

**Non-negotiable:** No IE code/task/roadmap imports; no cross-project work; no production changes. The Founder's explicit authorization is needed to move beyond research into a technical pilot.
