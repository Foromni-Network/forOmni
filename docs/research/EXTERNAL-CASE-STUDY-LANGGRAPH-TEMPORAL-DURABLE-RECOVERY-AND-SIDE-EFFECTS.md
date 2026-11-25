# Open-Source AINO Case Study 03 — LangGraph vs Temporal: Durable Recovery and Safe Side Effects

**Status:** Read-only, source-linked research; no software executed or benchmarked; no external outreach, fork, contribution, or integration.
**Date:** 2026-11-21 · **Scope:** Foromni only. Internet Embassy remains out of scope.
**Source snapshots:** `langchain-ai/langgraph@c6335a4255dc1d8abc25a7677f9c072c7ab27b9c`; `temporalio/temporal@32ef011fbd1e38ecddf656fc3f5026f6641cfeab`.
**Companions:** OPEN-SOURCE-AINO-CASE-STUDY-FLYWHEEL-PROTOCOL.md; CONVERGENCE-PACKET-FRESHNESS-AND-DECISION-RULES.md; EXTERNAL-CASE-STUDY-OPENHANDS-AGENT-CANVAS-OWNERSHIP-AND-CONVERGENCE.md; FULL-STACK-CONVERGENCE-TRIAL-PREREGISTRATION-V0.1.md.

## Why this comparison

The next key AINO failure mode is not simply "agent stops." It is **agent or orchestrator loses confirmation of a side effect**. Suppose an agent creates a Git commit, then its network connection dies before the reply arrives. Recovery may re-run the operation, but the allowed branch, task scope, human approval or source revision could have changed. Neither saved model memory nor a workflow replay automatically confers current permission.

The question: Which existing OSS mechanics let an AINO preserve useful completed work while safely resuming, reconciling uncertain effects and respecting revocation?

## 1. Directly observed source: LangGraph

- LangGraph README describes **long-running stateful graph execution**, persistence, interrupts and human-in-the-loop controls; this is an agent/workflow runtime, not a protected Git merger.
- `libs/checkpoint/README.md` defines checkpointer operations such as `put`, `put_writes`, `get_tuple`, `list`, `delete_thread`, and versioning. Saved checkpoints use a `thread_id` and optionally a `checkpoint_id`.
- The same checkpoint README says **pending writes** from successful sibling nodes can be saved when another node fails at the same graph superstep, avoiding unnecessary reruns of already-completed nodes.
- The checkpoint README warns that permissive deserialization of checkpoint data can be risky and recommends restricted MessagePack modules / strict mode for new apps.
- LangGraph's current `AGENTS.md` explicitly defines itself primarily as a low-level runtime and points agent-development use toward higher-level harnesses. That supports Foromni's goal of adopting a mature runtime rather than building another complete engine.

**Evidence:** [README](https://github.com/langchain-ai/langgraph/blob/c6335a4255dc1d8abc25a7677f9c072c7ab27b9c/README.md), [checkpointer contract](https://github.com/langchain-ai/langgraph/blob/c6335a4255dc1d8abc25a7677f9c072c7ab27b9c/libs/checkpoint/README.md), [project contribution architecture](https://github.com/langchain-ai/langgraph/blob/c6335a4255dc1d8abc25a7677f9c072c7ab27b9c/AGENTS.md).

**Not established:** LangGraph alone does not prove GitHub writes are idempotent, independently attributable, or safe against stale agent grants. Graph checkpoints should not be confused with real-world side-effect deduplication or independent acceptance.

## 2. Directly observed source: Temporal

- Temporal server README describes a durable execution system that handles intermittent failures and retries failed operations. The repo is the **server**; application Workflow/Activity code runs in separate language SDK worker processes.
- `docs/architecture/README.md` describes event-sourced, append-only execution history from which workflow state can be replayed.
- This architecture states that workflow code must be deterministic and avoid side effects (with documented exceptions), while Activities performing external operations must be **idempotent or non-retryable**. This is the most actionable operational warning for GitHub-writing AINOs.
- Temporal workers poll Workflow and Activity Task queues; History Service appends events, Matching Service handles delivery, and user-hosted workers execute application code.
- `docs/architecture/history-service.md` describes history shards, durable state, transfer tasks, timers, and an increasing `RangeID` to fence ownership. The underlying cluster's fencing cannot automatically fence a third-party GitHub write; an application must integrate its own correct external authority checks.
- Temporal contributor guide separates unit, integration and functional test suites and requires a contributor license agreement for merged contributions.

**Evidence:** [README](https://github.com/temporalio/temporal/blob/32ef011fbd1e38ecddf656fc3f5026f6641cfeab/README.md), [Temporal architecture](https://github.com/temporalio/temporal/blob/32ef011fbd1e38ecddf656fc3f5026f6641cfeab/docs/architecture/README.md), [history service](https://github.com/temporalio/temporal/blob/32ef011fbd1e38ecddf656fc3f5026f6641cfeab/docs/architecture/history-service.md), [contribution and testing guide](https://github.com/temporalio/temporal/blob/32ef011fbd1e38ecddf656fc3f5026f6641cfeab/CONTRIBUTING.md).

**Not established:** Durable workflow history does not make external tools exactly-once. A third-party API call can succeed even if the Activity's completion event is lost. Auth, request idempotency, read-back reconciliation and effective policy checks must be designed by the application.

## 3. What each solves, and what neither solves by default

| Concern | LangGraph | Temporal | Necessary Foromni boundary |
|---|---|---|---|
| In-flight agent state | Graph checkpoints and threads | Durable event history and workflow replay | Bind state to actual task/agent identity and requirements |
| Retain partial successful computation | Pending graph writes at superstep | Completed Activity outcomes in history | Verify completed work remains semantically valid after newer source revisions |
| Human pause | Interrupt/inspect/resume patterns | Workflow updates/signals and worker queues | Human approval is an authenticated external grant, not a text continuation |
| Delayed/retried work | Resume from saved checkpoint | Activity retry semantics | Always reconcile unknown side effects before repeating |
| External GitHub write | Application-defined tool call | Side-effecting Activity | Effective ref/path/task grant, source check, idempotency and read-back |
| Revocation | Not inherent in a checkpoint | Not inherent in workflow replay | Trusted broker checks latest rights at action time |
| Independent QA | Not automatically provided | Not automatically provided | Distinct evaluator and exact source/prospective merge state |
| Cost/complexity | App-level graph/checkpointer components | Workflow service/SDK/worker infrastructure | Pilot should not add a platform if a simpler durable ledger suffices |

A case study cannot prove a winner without an authorized, workload-matched trial.

## 4. A full-stack GitHub recovery trace (synthetic)

**Premise:** Accepted Foromni research experiment task `task-demo-22` authorizes agent `ag-be-01` to submit a patch for candidate branch `agents/demo-be` based on `BASE_A`. This is an illustration, not a real grant.

1. **Preflight:** Trusted broker authenticates agent/session, task revision and lease epoch; checks source `BASE_A`, allowed operations and policy. It records an intent with stable `operation_id` before a potentially external write.
2. **Submit:** Broker validates patch paths and base SHA, then performs a permitted candidate update. The Git server creates commit `COMMIT_B`.
3. **Failure:** Response is lost. Workflow process restarts; last local record says `UNKNOWN`, not `FAILED` or `SUCCESS`.
4. **Reconcile:** Before retry, trusted service reads GitHub's actual branch ref, reachable commit and operation marker/event mapping. Check if `COMMIT_B` happened; correlate unique operation ID to authenticated broker records. Git commit author is not proof of agent identity.
5. **New authority check:** Even if task approval existed earlier, the action's current grant, lease, source and protected-branch rules must be re-evaluated. If revoked, do not make a new write or promote to main; preserve already-existing evidence and route incident/review.
6. **Conditional recovery:** If first write landed and still matches permitted state, mark the operation `ALREADY_APPLIED` without repeat; if definitely absent and current authority allows, retry once under original stable idempotency key and compare-and-swap branch ref semantics; if ambiguous, escalate `MANUAL_RECONCILIATION` and stop.
7. **Admission:** Independent QA checks exact candidate (and later combined prospective target); protected integration authority is separate. An agent cannot graduate an `UNKNOWN` candidate merely by asserting it built successfully.
8. **Learning:** Record actual runtime failure, attempts, recovery decisions and cost, including time spent on reconciliations. Do not reclassify an ambiguous write as failed or successful without evidence.

**Critical caveat:** A GitHub REST endpoint may not support caller-provided idempotency keys for every action. If the external operation lacks native deduplication, the broker needs an operation ledger, read-back, conditional ref updates/compare-and-swap where available, and explicit uncertain-result handling. Even these mechanisms can require serializing conflicting writes. Never promise unconditional exactly-once side effects.

## 5. Failure and denial matrix for eventual research experiment

| ID | Event | Safe observable outcome |
|---|---|---|
| REC-01 | Worker crashes before external write | No write; permitted action may be retried |
| REC-02 | Worker crashes after write, before acknowledgment | Trusted ref read-back detects existing effect; avoids duplicate |
| REC-03 | Main or candidate base advances | Old attempt marked stale, valid diff may be rebased/reviewed separately |
| REC-04 | Task/agent grant revoked during outage | No renewed write despite persisted retry intent |
| REC-05 | Two workers race to update same ref | One conditional update wins; loser rechecks/repairs |
| REC-06 | QA verdict from prior SHA reappears after resume | Verdict rejected for current candidate |
| REC-07 | Human pause expires or changes | New action requires fresh authenticated approval |
| REC-08 | Checkpoint contains untrusted deserialization content | Restricted loading or independent validation rejects unsafe payload |
| REC-09 | Retry budget exhausted | Honest incomplete/failure state with full consumed costs |
| REC-10 | Git API unavailable at reconciliation | `UNKNOWN` and no blind retry until permissible state can be observed |
| REC-11 | Worker changes model/runtime after restore | Identity continuity retained but model/permission/evidence revision updated |
| REC-12 | Prompt-injected README requests bypass of permission check | Actual trusted broker denies regardless of model continuation |

These are **proposed scenarios**, not passing tests or observed bugs in the studied OSS systems.

## 6. Relationship graph for recovery — a new Foromni insight

The task/agent registry should maintain relationships that permit recovery queries:
- Task revision → accepted objective and acceptance/evaluator revisions;
- Attempt/session → authenticated agent ID and effective authority epoch;
- Operation ID → intended external action, target Git ref and precondition SHA;
- Applied commit → GitHub-observed SHA and candidate PR;
- QA verdict → exact checked source/merge-group SHA;
- Change in upstream contract → affected dependent tasks and potentially stale checkpoints.

**Key synthesis:** Recovering a workflow is not merely restoring a serialized state. It is *reconciling the workflow's remembered world with the current authoritative world*. That is precisely the roadmap/relationship/synchronization mechanism in Foromni's econometric convergence hypothesis.

The hypothesis is that version-bound reconciliation before resuming may lower duplicated operations and late integration rework, at the expense of additional preflight overhead. Measure net value in a controlled study; don't assume.

## 7. Collaboration ladder and useful, nonintrusive contributions

**For LangGraph:** Focus on a reproducible documentation/example of a checkpointed agent tool call that performs an *external* effect and demonstrates why idempotency/read-back are required. Review current issues first and follow their runtime-first focus; avoid proposing agent feature creep in the low-level engine.

**For Temporal:** Focus on application-level examples or documentation of a source-revision/authorization-aware GitHub Activity, possibly better suited to a samples repository than a core server PR. Their proposal/contribution channels and CLA are explicit. Avoid asserting the server is missing guarantees it never claims.

**For both:** A Foromni-owned independent research artifact comparing failure semantics could be valuable without asking maintainers to adopt Foromni. Actual contribution and communication await explicit user authorization and maintainer interest.

**Respect:** No unsolicited PR, no partnership implication, no vulnerability disclosure through a public issue; no code copied or merged.

## 8. Open research questions

1. What minimal read-back + operation ledger is sufficient for the authorized E0 one-agent case without installing an entire Temporal service?
2. Can LangGraph's checkpoint persistence represent an authoritative operation intent and guarantee against a second attempt? (Likely requires trusted external ledger; validate later.)
3. Which Temporal SDK retry hooks and heartbeat/cancellation controls best fit GitHub operations? Do not conflate server with language SDK internals.
4. What is the most robust actor/task/commit attribution when a shared GitHub App performs every worker write?
5. Can we preregister a small number of REC-01..12 failure injections without biasing which runtime is favored?
6. How does coordination overhead compare with prevented rework by task dependency density and workforce size?
7. Where does a thin adapter end and an unnecessary duplicate orchestrator begin?

## 9. Research recommendation

For **E0**, continue planning a simple isolated worker and trusted branch-write/QA evidence procedure, with a durable minimal operation intent ledger. Do not add both LangGraph and Temporal or build a universal event engine as a prerequisite.

For larger autonomous teams **after** evidence and authorization, investigate LangGraph if workflow complexity is primarily graph/state/interrupt behavior; investigate Temporal if long-running reliable queueing, retried side effects and distributed workflow recoverability dominate. These are workload hypotheses, not vendor rankings.

**No trial, security test, external Git write, or new infrastructure was run.**

*Build today, so others can enjoy tomorrow.*
