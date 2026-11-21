# Foromni AINO Reference Architecture v0.1 — Cross-Case-Study Convergence

**Status:** Research synthesis and provisional architecture. No software built, tested, merged, deployed, or connected to an external system.  
**Date:** 2026-11-21 · **Scope:** Foromni only; Internet Embassy and its repositories/infrastructure remain excluded.
**Foundation:** Read-only case studies of Rerun, OpenHands, LangGraph/Temporal, SWE-bench and OpenTelemetry; project comparisons are *mechanism observations*, not scores or evidence of compatibility in a running combined stack.

## Executive decision

**Build the organizational convergence contract, not five duplicate products.** Separate (1) purpose and accepted requirements, (2) agent/task/relationship registry and authoritative versions, (3) independently authenticated execution and action-time authorization, (4) source and acceptance verification, and (5) outcome learning. Agent model inference, work-hosting, workflow durability, coding tools, testing and telemetry can be supplied by multiple implementations behind stable boundaries.

An AINO is not a swarm of independent chat windows. Its essential research object is the repeatable transformation:

`human/collective objective -> authorized plan -> eligible agent/attempt -> bounded work -> evidence -> independent acceptance -> protected integration -> authorized release -> verified outcome -> calibrated routing`.

No model, worker, trace, GitHub display name, source comment, or work packet can grant itself authority over another phase.

## 1. Logical component map

```text
 HUMAN / COLLECTIVE PURPOSE + GOVERNANCE
       approved goals, rights, budget, allowed risks
                         |
  AUTHORITATIVE ORGANIZATION REGISTRY  [Foromni research gap]
  objectives -> task DAG -> contract owners -> agent registry
  dependency revisions -> assignments -> relationship history
                         |
  PLANNER / ROUTER  [advisory; source can be agent model]
  choose eligible work, monitor capacity, ask questions
                         |
  TRUSTED DISPATCHER + POLICY + OPERATION LEDGER
  identity, current lease epoch, source SHA, risk, limits
                         |
        +----------------+------------------+
        |                |                  |
   CODING WORKER     RESEARCH WORKER    REVIEW WORKER
    isolated attempt, model provider access via broker
        |                |                  |
       candidate artifacts and operation-intent records
                         |
  RECONCILIATION GATE: read actual Git refs/side effects,
  verify effective grant and latest accepted contracts
                         |
  INDEPENDENT ACCEPTANCE / SECURITY REVIEW
  exact SHA; API/auth/DB/browser/negative tests;
  prompt injection action-time safety
                         |
  PROTECTED GIT INTEGRATION (separate principal)
                         |
  OBSERVED MAIN SHA + (separately approved) RELEASE
                         |
  EFFECT / BENEFICIARY OUTCOME + TOTAL COST
                         |
  TRUSTED EVIDENCE JOIN (not agent self-assessment)
             -> organizational learning -> registry
```

**Separation of planes:** organization's decisions and accepted relationships are a *control plane*. Worker model calls, tool execution and temporary state are an *execution plane*. External Git refs, independent tests and outcomes are an *evidence plane*. Authentication, budgets and release approval are an *authority plane*. Plans and observations may inform authority decisions but are never sufficient authorization on their own.

## 2. Responsibility ownership, with reusable components

| Capability | Authoritative Foromni responsibility | OSS mechanism to consider | Avoid rebuilding/assuming |
|---|---|---|---|
| Persistent worker identity | Logical `agent_id`, incarnation/attempt history, roles, owner links | Rerun IDs, OpenHands agent/conversation identities | Never infer identity from GitHub token name or model key |
| Task / relationship graph | Accepted objective, dependencies, contract owners, versioned routing and capacity | Existing databases/workflow metadata | Shared memory text is not an authoritative dependency graph |
| Agent execution | Authenticated attempt, isolated workspace, bounded permissions | Rerun coworkers, OpenHands SDK/Coding agents, other providers | Don't develop a new coding engine to get task ownership |
| Workflow durability | Restart, dependency readiness, retry scheduling | LangGraph checkpointing or Temporal workflows | Don't install both as a default; replay does not prove external effect status |
| Provider/model access | Trusted gateway/BYO provider project with per-attempt cost evidence | Existing provider adapters and connection management | Different API keys are not necessary to create unique agents |
| GitHub contribution | Brokered ref/path-checked candidate write, actual SHA read-back | GitHub Apps and protected Git rules | GitHub App token alone is not per-file or per-agent scope |
| Independent QA | Sealed or independently maintained suite, version-bound verdict | SWE-bench evaluation practices, E2E browser/API harnesses | Green tests from previous SHA and agent-printed PASS are not acceptance |
| Security | Enforce current principal grants, isolate workers, evaluate prompt injection exposure | Platform sandbox/policy controls, independent gate | Prompt filtering, untrusted content, and traces cannot expand privileges |
| Telemetry | Redacted spans and metrics correlated to actual work attempts | OpenTelemetry GenAI conventions and Collector (later) | Logs are not legal grants, financial truth or independent acceptance |
| Outcome economics | Full cost, time horizon, failures, accepted behavior and real-world effects | Independent data/statistical analysis | Don't optimize commits, worker count, or selected successes |
| External relationships | Transparent, source-linked case studies and opt-in contributor relationships | Maintainer contribution processes | Don't imply partnership, endorse, copy GPL/AGPL code without review |

**Make-vs-reuse rule:** Extend the organization/evidence interfaces only where an existing solution does not satisfy the accepted requirement. Prefer small adapters and stable APIs to copy/paste, wholesale forks or introducing more orchestrators.

## 3. Minimum shared identifiers and where their meaning comes from

- `organization_id`: authoritative tenant/governance and rights boundary.
- `objective_id/revision`: accepted human or collective goal, fixed acceptance targets.
- `task_id/revision`: accepted task and dependency contract snapshot.
- `registry_agent_id`: persistent organizational identity (not an API key).
- `incarnation_id`: authenticated worker runtime/model instance; can change while `registry_agent_id` persists.
- `attempt_id`: bounded assignment and retry accounting.
- `operation_id`: trusted broker's external-effect intent and reconciliation key.
- `base_sha/candidate_sha/integrated_sha`: Git-observed stages of source.
- `evaluator_id/suite_revision`: independent acceptance provenance.
- `trace_id/span_id`: telemetry correlation, not independent auth proof.
- `cost_ledger_ref/outcome_ref`: reconciled real resource spend and externally observed benefits.

Never flatten candidate acceptance, integration acceptance, authorized public release and beneficiary impact into one `done` value.

## 4. Narrow interfaces necessary for E0 (research only)

**Registry to dispatcher**: task revision, dependency digest, eligible authenticated agent, workspace and effective scopes, budget, expected base source, expiration/lease epoch. Both sides verify accepted revisions.

**Worker to broker**: authenticated session + operation ID + intended branch/diff + current base/ref; request must be denied when task scope, path, source or lease changed. Credentials held by broker, not embedded in prompts.

**Broker to GitHub**: actual read/write result; read-back if ACK missing; compare-and-swap/conditional ref update when supported; conservatively handle ambiguity.

**Candidate to independent QA**: exact commit SHA, environment digest, suite revision, expected test count, negative fixtures, trust requirements and separate evaluator principal.

**Runtime to evidence correlation**: OTel standard spans (agent/tool/model); internal task/attempt/operation correlation IDs; authoritative ledger separately attests policy and Git/QA state.

**QA to protected integration**: immutable, current source-bound verdict + policy gate + accountable merge authorization; verify merged prospective SHA rather than inheriting green from an old branch.

**Integration to release/outcome**: actual merged SHA and staged artifact, then separate release approval, monitoring and validated beneficiary results.

## 5. A single end-to-end transaction through these layers

Illustrative synthetic Collective Lab task: manager creates a task, frontend renders it, backend persists it, viewer may read but not modify; project B cannot see project A's private tasks.

1. Reviewer approves exact objective, task versions and role matrix.
2. Registry assigns UI and API tasks to stable agents, records `UI -> API schema` dependency and ownership.
3. Workers obtain bounded tasks and separate attempts, even if both use a shared model provider key *held only by trusted gateway*.
4. Backend returns `displayName` per accepted contract; a mismatch is caught before source convergence.
5. An agent writes candidate via broker. If ACK is lost, broker queries GitHub first; duplicates and stale writes are not silently accepted.
6. An independent evaluator uses a fixed acceptance suite and separate identity; checks UI, authentication, server-side RBAC, migrations and security negatives.
7. Protected merger verifies the exact prospective combined source, actual checks and human/collective authorization.
8. Only a separately authorized activity promotes staging/release; no claim of a live deployment from research artifacts.
9. Cost ledger includes workers, provider calls, retries, QA, orchestration, hosting and human effort.
10. Registry updates *verified* contribution/relationship statistics only when evidence identifies the accepted integrated source and result.

**This is a worked research design, not a completed pilot or observed behavior.**

## 6. Failure conditions that stop convergence

| Condition | Safe result | Source of truth |
|---|---|---|
| Other agent changes contract/base source | Revalidate dependent tasks before accepting patch | Registry + actual Git refs |
| Agent claims task complete without candidate SHA | No accepted code | Git host |
| GitHub write ACK lost | UNKNOWN, inspect real ref before retry | Operation ledger + remote Git |
| Agent attempts unauthorized file/ref | Deny via trusted enforcement; don't trust packet claim | Policy/broker |
| QA result from old source | STALE_EVIDENCE, rerun on required SHA | Independent evaluator manifest |
| Required tests did not run | NO_TEST_EXECUTION | Independent runner logs |
| Prompt injection requests protected merge | Deny at action time; security gate blocks if critical | Trusted policy + independent review |
| Trace reports success but Git has no evidence | TRACE_NO_AUTHORITATIVE_OPERATION; no credit | Git + ledger |
| Provider costs missing | COST_UNRECONCILED; never assume zero | Billing ledger |
| Release not separately authorized | Integrated source may exist, but no deployment claim | Release policy |

## 7. Current research synthesis / status audit

**More coherent now:** Five case studies supply complementary mechanisms for identity, coding runtime, durability, grading and observability. They suggest Foromni's distinctive research focus is cross-tool organizational coordination and evidence.

**Not established:** A working universal stack, independent experimental proof, rigorous comparison against baselines, host-specific Git authority verification, stable approved E0 API fixture, sealed evaluator, reproduced setup, measured cost or maintainer collaboration. A growing documentation count is not a readiness metric.

**Open decisions to close before a bounded E0 trial:**
1. Accept/freeze the reference application API, roles, invitation semantics, fixtures and grading rubric.
2. Choose whether one-agent E0 requires any external orchestrator; prefer a disposable process plus trusted manually audited records unless functionality demands more.
3. Design and independently verify isolated worker versus separate reviewer identities and Git permissions.
4. Pin packages, migrations, test harness, hosting network and no-secret boundaries.
5. Write one source-bound evidence manifest with operational reconciliation and refusal states.
6. Predeclare costs, resource and human oversight budgets, failure accounting and stop rules.
7. Seek **separate** founder authorization for the exact bounded trial.

**Next research deliverable:** A contract boundary decision record covering minimum-versus-deferred components, clear component owners, and the shortest evidence path through E0. Do not add an agent communication protocol, SIEM, custom orchestration suite or extra services as E0 prerequisites.

## 8. Source lineage (read-only case studies)

- [Rerun](https://github.com/rerun-build/rerun) — stable coworkers/shared connections; external case study `EXTERNAL-CASE-STUDY-RERUN-BUILD-OPEN-SOURCE-AND-COLLABORATION.md`.
- [OpenHands](https://github.com/OpenHands/OpenHands) and [SDK](https://github.com/OpenHands/software-agent-sdk) — coding workers, ownership and verification independence; case study `EXTERNAL-CASE-STUDY-OPENHANDS-AGENT-CANVAS-OWNERSHIP-AND-CONVERGENCE.md`.
- [LangGraph](https://github.com/langchain-ai/langgraph) and [Temporal](https://github.com/temporalio/temporal) — durable workflows and side effect safeguards; case study `EXTERNAL-CASE-STUDY-LANGGRAPH-TEMPORAL-DURABLE-RECOVERY-AND-SIDE-EFFECTS.md`.
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) — external benchmark and false-green testing; case study `EXTERNAL-CASE-STUDY-SWE-BENCH-ACCEPTANCE-EVIDENCE-AND-BENCHMARK-INTEGRITY.md`.
- [OpenTelemetry GenAI](https://github.com/open-telemetry/semantic-conventions-genai) — spans/metrics, distinct from accepted evidence; case study `EXTERNAL-CASE-STUDY-OPENTELEMETRY-AGENT-OBSERVABILITY-AND-EVIDENCE.md`.

**No live changes, integration, testing or deployment.**

*Build today, so others can enjoy tomorrow.* ❤️🐂
