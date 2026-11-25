# AI Workforce Hosting and Synergy — Portable Runtime Research v0.1

**Status:** Research options, not chosen infrastructure or a deployed system.  
**Date:** 2026-11-21 · **Scope:** Foromni only. Internet Embassy infrastructure and projects are out of scope and unchanged.  
**Research companions:** CONVERGENCE-WORK-PACKET-TYPED-CONTRACT-V0.2.md; END-TO-END-AINO-EXPERIMENT-READINESS-AND-EVIDENCE-PLAN.md; CONVERGENCE-FIRST-CONTROLLER-ARCHITECTURE.md; AI-OPERATED-AINO-OVERSIGHT-MODEL.md.

## Question: How can many autonomous agents synergize without turning into a noisy swarm?

**Research hypothesis:** Separation between *coordination*, *execution*, and *independent admission* is more important than choosing a single grand orchestration framework. Agents should communicate through typed tasks, versioned evidence, durable queues and bounded permissions rather than relying on a group chat or shared mutable workspace.

A robust implementation may combine a small authorized controller, external worker providers, isolated runtimes, the canonical Git forge, independent CI, an event ledger, and human/collective governance. Avoid duplicating these responsibilities across multiple uncoordinated "chief" agents.

## 1. Logical architecture

```text
Human / collective objective + approved budget/rights
                         |
        Authoritative task & contract ledger
                         |
             Convergence Planner
          (AI advice; no merge power)
                         |
            Trusted Policy / Dispatcher
            |        |        |
         queue     queue     queue
          FE        BE       QA/Repair
            |        |        |
       isolated AI workers / workspaces
         local | cloud | hybrid
            |        |        |
        candidate branches + artifacts
                         |
         independent QA + evidence oracle
                         |
           protected Git merge controller
                         |
          observed canonical main commit
                         |
         staging / release / monitor
         (separate effective authority)
```

**Critical:** Independent QA can be triggered by the controller, but must execute under credentials and review policies the implementer cannot forge. Git status and actual merged commit, not a conversational agent's declaration, define accepted source state.

## 2. Hosting options, graduated by justified complexity

| Option | Agent locations | Good experimental fit | Limits/risk | Initial research stance |
|---|---|---|---|---|
| Developer workstation / local lab | Local containers or VMs, optional remote model APIs | 1–3-agent reproducible, low-cost discovery; privacy-sensitive synthetic fixtures | Availability, networking, laptop resource limits and sandbox boundaries | E0 baseline candidate |
| Single secured cloud VM | One virtual host with isolated per-attempt workers and small service/database | Small always-on team and straightforward remote operations | Single-host failure, noisy neighbor, secret and container escape concerns | Compare with local |
| Ephemeral hosted VM/sandbox per attempt | Disposable remote sandbox, worker launched on demand | Isolating untrusted coding tasks, clean reruns and resettable experiments | Boot/cold start, storage/egress charges, varying providers | Preferred security hypothesis, not proven |
| Hybrid control plane + local/cloud agents | One authoritative ledger/gates, worker placement based on privacy, cost, hardware and capability | Diverse AINOs and providers; private data can stay where authorized | Network partitions, proof of remote worker identity, consistency | Key portability research |
| Kubernetes Jobs + queue-driven autoscaling | Cluster jobs/pods via KEDA or analogous services | 8–100+ workers after demand is proven | Cluster operations overhead, queue and test bottlenecks persist, Kubernetes not a security boundary by itself | Defer until scale requires |
| Fully managed agent platforms | Provider-hosted agent workers with external trusted controller | Quick test, low operations burden | Vendor policy lock-in, cost observability and artifact portability | Evaluate against open worker adapters |

No host provider, plan, region, price or machine type is selected. Actual costs and available models require dated quotes and deployment reviews before a trial.

## 3. Upstream tools worth comparing

### OpenHands Software Agent SDK and Agent Server
- Candidate coding-agent runtime with API/workspace and remote execution model; evaluate current SDK licensing, agent-server authentication, sandbox provider and tool permission semantics.
- Source: https://github.com/OpenHands/software-agent-sdk
- Docs: https://github.com/OpenHands/docs/blob/main/sdk/arch/agent-server.mdx
- **Gap:** Does not by itself establish Foromni objective/task governance, independent QA authority or safe protected Git admission.

### Temporal task queues and durable workflows
- Service persists event history; workers poll task queues; replay permits recovering workflows after worker failures. Evaluate operational overhead, deterministic workflow constraints, idempotent external effects, and versioning.
- Sources: https://docs.temporal.io/tasks ; https://docs.temporal.io/durable-execution ; https://docs.temporal.io/best-practices/worker
- **Gap:** Durable workflow transport is not proof task results are correct, authorized or integrated.

### LangGraph / supervisor patterns
- Research option for bounded agent planning/handoff and human-in-the-loop workflow state; consider whether this duplicates an external durable scheduler.
- Sources: https://langchain-ai.github.io/langgraph/ ; https://reference.langchain.com/python/langgraph-supervisor/supervisor/create_supervisor
- **Gap:** LLM supervisor outputs must not substitute for authenticated policy decisions or protected mainline gates.

### GitHub native controls / ephemeral CI
- Branch protection and merge queues provide controlled source admission; ephemeral CI runners can help isolate jobs. GitHub recommends ephemeral rather than persistent self-hosted runners for autoscaling. Avoid untrusted repository jobs with persistent high-privilege credentials.
- Sources: https://docs.github.com/en/actions/reference/runners/self-hosted-runners ; https://docs.github.com/en/actions/reference/security/secure-use ; https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
- **Gap:** GitHub is source-control/CI authority, not a complete agent scheduling, learning or human governance system.

### KEDA event-driven Kubernetes Jobs
- Candidate for scaling isolated batch workers from queue/event backlog once a cluster is genuinely necessary.
- Source: https://keda.sh/docs/2.21/concepts/scaling-jobs/
- **Gap:** Autoscaling agent count may oversubscribe QA, Git provider/API quotas or budget, so it must be downstream of the convergence capacity budget.

### OpenTelemetry
- Candidate for portable request/attempt traces, latency, errors and operational costs; collect with appropriate data minimization, sampling, consent and source authentication.
- Source: https://opentelemetry.io/docs/
- **Gap:** Observability does not prove a model-generated claim or beneficiary value.

## 4. How agents work in harmony: required coordination rules

1. **Single authoritative task identity**, independent of model/vendor and UI. One task UUID; attempts and retries have independent IDs.
2. **One accepted objective/spec revision** with measurable acceptance criteria. A worker may propose changes, not rewrite founder objectives.
3. **Typed versioned work packet** specifying branch, ownership, dependencies, API contracts, source SHA and budget.
4. **No shared writable worktree across independent code agents** by default. Branches/workspaces and trusted credentials isolate the work.
5. **Shared knowledge as referenced artifacts**, not hidden prompt memory or a single context thread. Use immutable docs, source SHAs and versioned decisions.
6. **Explicit dependency DAG**. Parallelize independent UI/backend/research slices, serialize unavoidable changes to shared interfaces and migrations.
7. **Model-provider-independent adapters**. Route based on tested capability, privacy and cost; preserve a recoverable handoff across provider failures.
8. **Durable queue with idempotent handlers**. External writes need dedupe and actual state reconciliation; lease expiry alone cannot undo a write.
9. **Early conflict notifications and bounded replanning**. If main/API/task revision changes, preserve useful draft and invalidate only affected work before protected admission.
10. **Independent QA authority and strict current-merge evidence**. Model grading its own code is not enough; current integration result must be checked.
11. **Budget and backpressure**. Don't launch eight workers if only one QA slot and a high-conflict shared file are available. Count queue/CI/model/human total cost.
12. **Humans govern purpose and consequential rights**. Agent planning and repairs can be autonomous within permissions; policy, spending expansion, production publication and collective rights require their own authorization.

## 5. Control/data/authority planes should remain distinct

| Plane | What it handles | May it directly merge/release? |
|---|---|---|
| Coordination / control | task priorities, DAG, routing, retries, worker capacity and handoff | No, not merely by being controller |
| Evidence / data | tasks, source refs, reproducible artifacts, model/tool event logs, privacy-safe telemetry | No |
| Policy / authority | authenticated grants, revocations, budgets, action-time permissions | May authorize narrowly scoped operations, but separate service executes |
| Integration | independent QA, prospective merge checks, actual protected Git ref | Only trusted merger following configured rules |
| Publication / operations | release artifact, monitoring, rollback and public/social publication | Only separately authorized |
| Learning | analyze errors and suggest workflow changes | Never self-apply security/governance bypass |

Centralized coordination should not imply centralized ownership of independently operated collectives. They may expose a bounded permissioned task adapter rather than hand over their resources.

## 6. Candidate experimental profiles

### Profile A: Solo AINO
- One generalist coding agent + independent QA service.
- One local or hosted disposable workspace; Git remote and protected main.
- No heavy dedicated orchestration service unless failure recovery requires it.
- Test task-packet value against additional overhead.

### Profile B: Three-agent AINO
- Planner/architect, UI implementer, backend implementer + separate independent QA.
- Queue worker allocation; per-worker repo and network scopes.
- Shared API contract and task ledger.
- Study interface drift and queue coordination cost.

### Profile C: Eight-agent AI studio
- Goal/task steward; architecture/API; UX/accessibility; frontend; backend; auth/data; reliability/repair; documentation/integration assistance + independent QA outside implementer authority.
- Isolated disposable workspaces; durable queue or well-audited scheduler; backpressure on QA and protected merger.
- Measure worker idle time, collisions, CI invalidation and resource spend.

### Profile D: Adaptive hybrid AINO
- Start small, add workers only with enough independent ready tasks and verification capacity.
- Workers can run locally for approved private/offline tasks or cloud in tightly scoped disposable sandboxes.
- Model/provider switching must preserve provenance and effective permissions; network splits fence stale work.
- Judge fairness by *verified integrated output for full cost*, not agent count or task-start rate.

## 7. Hosting threat and resilience cases

- Untrusted coding agent tries to read another agent's workspace or a real user database.
- A public PR CI job tries to access an always-on self-hosted runner's host filesystem.
- Remote worker drops offline; lease expires; stale result later appears.
- Worker crashes after publishing branch ref but before acknowledgement; retries must reconcile.
- Orchestrator loses a message and assigns one task twice.
- Agent switches model vendors without data classification checks.
- QA is running on a worker controlled by same principal as implementer.
- Secret appears in terminal log and telemetry exporter proposes to store it publicly.
- Controller is unavailable during an emergency; safe stop and supervised recovery.
- 100 workers generate jobs faster than merge group and independent QA slots can verify.
- Compute spend reaches ceiling during repeated failures; no silent budget expansion.
- A collector misattributes telemetry from one tenant/project to another.

Treat these as future tabletop or disposable synthetic tests; none executed.

## 8. Open research decisions and recommendation

**Recommended first experimental architecture:** low-complexity control plane (task registry + durable-enough ledger/queue), protected GitHub main, isolated worker sandboxes using one agent runtime (OpenHands as a candidate, not selected), independent GitHub-hosted CI/QA, object/artifact manifests, and simple metrics. Start on local/disposable infrastructure; assess a single-VM/cloud worker variant for repeatability. Add Temporal or Kubernetes/KEDA **only** when controlled failures and throughput numbers justify the added operational cost.

The critical metric is not 'agents running simultaneously' but **verified integrated full-stack behaviors per total dollar and per human intervention**.

Research prerequisites: concrete reference app, trial environment/cost caps, data rights, secrets/host isolation controls, protected main behavior, independent QA authority and owner-approved experiment scope. This document does not approve deployment or tests.

*Build today, so others can enjoy tomorrow.*
