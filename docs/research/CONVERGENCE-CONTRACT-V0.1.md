# Convergence Contract v0.1 — Safe Concurrent Agent Work and Mainline Admission

**Status:** RESEARCH DRAFT — not implemented or approved  
**Date:** 2026-11-20  
**Scope:** Foromni only, no Internet Embassy changes  
**Related:** [Global Agent Roadmap Execution](GLOBAL-AGENT-ROADMAP-EXECUTION.md), [Massive Parallel to Mainline](MASSIVE-PARALLEL-TO-ONE-MAINLINE.md), [Provider-Agnostic Agents](PROVIDER-AGNOSTIC-AGENT-EXECUTION.md)

## Decision to test

A Convergence Contract is a **vendor-neutral, versioned agreement** for safe, auditable transitions from distributed worker attempts to a verified shared product revision. It governs:

1. who may propose a change and to what task revision;
2. who has write authority for a candidate branch/ref;
3. which exact source and target revisions were independently tested;
4. how concurrent writes, stale branches and retries are handled;
5. how a candidate is reconciled with dependencies and main;
6. who may authorize a protected merge, integration, and release;
7. how failures retain audit trails and become repairable rather than green.

**Main invariant:** no agent's self-report or successful local test can mutate authoritative acceptance state or protected mainline without independent admission.

Git provides content-addressed commit history and protects ordinary branch updates against non-fast-forward overwrites. It does not provide task ownership, compatible domain changes, independent acceptance or integration guarantees. Source: https://git-scm.com/docs/git-push ; https://docs.github.com/en/rest/git/refs

## 1. Clarify the races

**Race A: Two agents fetch A; both push shared branch.** Agent 1 pushes A→B. Agent 2 tries to push A→C. A normal push fails (not fast-forward). An indiscriminate force push can overwrite B. Correct action: preserve C, fetch B, reconcile, test D=B+C, push D with a conditional remote-ref check. Do not silently discard B.

**Race B: Both agents create new commits from the same HEAD and push in quick succession.** Fast-forward protection still prevents the second divergent update unless the second includes the first; ordinary push race is primarily a **conflict/retry** problem, not automatically data loss.

**Race C: Agent fetches while another pushes.** Fetch is a local read that updates local references/objects; it is not a shared remote write. The worker simply sees a snapshot. The hazard is acting on a stale snapshot later; reread and compare the authoritative ref immediately before protected writes.

**Race D: Two agents change different files but one shared API.** Git may merge cleanly despite semantic incompatibility. Require contract/integration tests against the combined merge result.

**Race E: A CI pass references source SHA S on base M1, but main is now M2.** Revalidate the current prospective merge group; never reuse the outdated success as merge-result proof.

**Race F: A job reruns a retry after its lease expires.** A previously valid agent can issue late writes. Its lease token must be fenced off; Git push alone does not understand worker lease expiry.

**Race G: Separate automation processes write the same branch using a GitHub file-content API.** The API's file SHA check guards an existing file version, but does **not** substitute for task authorization or a repository-wide atomic update. Use isolated branches plus coordinator; verify branch HEAD after operations.

**Race H: Integration succeeds but ledger write fails.** Durable reconciliation must discover the actual merged SHA; never repeat a merge simply because the acknowledgement was lost.

## 2. Hard recommendation: branches are cheap; shared write authority is not

**Default:** one task/candidate integration workspace = one write-authorized actor at a time, with distinct short-lived branch names and immutable attempt IDs.

- Allow thousands of agents to fetch/read the same repository concurrently.
- Allow thousands of agents to develop on **separate task-owned branches, forks or isolated worktrees** concurrently.
- Do NOT give thousands of agents concurrent direct write access to `main` or to a shared feature branch.
- Separate read/discovery credentials from write/merge credentials.
- Agents contributing to the **same logical task** should default to separate candidate branches or one elected branch writer; other agents submit patches/artifacts/PR reviews, not competing writes.
- Temporary shared-branch collaboration requires an explicit owner/lease and a compare-and-set gate; no direct unrestricted push.
- Never use unconditional `--force` on shared branches; `--force-with-lease=<ref>:<expected-old-oid>` is a conditional safety mechanism, **not a substitute for protecting mainline**, and should remain disallowed on protected refs.
- Even a conditional ref update only addresses Git-level history loss. It cannot validate semantics or prove acceptance.

**Naming illustration (not a reserved implementation convention):** `work/FOR-101/<attempt-id>`, `candidate/FOR-101/<candidate-id>`, `integration/<batch-id>`. Ensure sanitization and uniqueness across users/orgs; branch names are not security identities.

## 3. Core immutable/provenance IDs

- `task_id` and `task_revision`: what completion means at the time of execution.
- `attempt_id`: one worker execution, retry or handoff; never re-used.
- `actor_id`, `organization_id`, `auth_grant_id`: who can do what; verify independently of model self-description.
- `lease_epoch` / fencing token, `lease_expires_at`: exclusive write authority; monotonic epoch under authoritative coordinator.
- `workspace_id`, `repository_id`, `branch_ref`: local candidate workspace; explicit ref ownership.
- `expected_branch_head`, `candidate_head_sha`: conditional update input/output; do not assume latest state after a previous read.
- `expected_main_sha`, `proposed_merge_sha`, `actual_integrated_sha`: **distinct** points of source, admission and final-result verification.
- `dependency_set_digest`: versions of dependency contracts used to evaluate the candidate.
- `acceptance_contract_digest`, `evidence_bundle_digest`: bind claims to exact requirements and observed tests.
- `admission_decision_id`: independently attributable gate verdict, not an agent claim.
- `release_decision_id`: distinct authority from integration.

These fields are a *contract proposal*, not an implemented schema.

## 4. Conditional branch write protocol

A coordinator allocates a private write workspace / ref to a task attempt (or gives no repo write authority, allowing artifact submission instead). A lease is not a Git lock; it is enforced by a trusted ref writer or GitHub App with appropriate permissions. If agents retain direct unrestricted write credentials, the lease policy is **advisory and ineffective**.

Before each write:
1. Validate credential, allowed repository/ref, current lease epoch and task revision.
2. Fetch remote ref HEAD. Compare to the previously registered `expected_branch_head`.
3. Prepare a commit whose parent includes the remote head (or handle a conflict explicitly).
4. Perform only a fast-forward, or a narrowly scoped atomic compare-and-set operation where supported by the chosen backend.
5. If ref advanced, **reject and return a conflict event**. Refresh, reconcile and rerun validation. Do not force overwrite.
6. Record resulting ref SHA, actor and task attempt in the authoritative ledger. On ambiguous network responses, query the remote ref before deciding whether to retry.
7. Ref writes, CI run submissions and ledger events must be idempotent or reconcilable; Git and the DB are not one distributed transaction.

**Important limitation:** A simple `git push` fast-forward check is necessary but not sufficient for strict compare-and-set on arbitrary branch state. Design/test exact expected-OID semantics using the selected Git server API or a single trusted branch writer. Do not assume ordinary GitHub REST update-reference with `force=false` implements full expected-head CAS in one operation; it only enforces fast-forward safety.

## 5. Provider-neutral Convergence Candidate envelope (conceptual example)

```json
{
  "contract": "foromni.convergence.v0.1-draft",
  "candidate_id": "cand-example-001",
  "project_id": "foromni",
  "task": {"id": "FOR-101", "revision": 3, "acceptance_digest": "sha256:example"},
  "attempt": {"id": "attempt-001", "actor_id": "org/agent-12", "lease_epoch": 7},
  "source": {
    "repo": "Foromni-Network/forOmni",
    "branch_ref": "refs/heads/work/FOR-101/attempt-001",
    "expected_branch_head": "full-40-character-Git-OID-required",
    "candidate_head_sha": "full-40-character-Git-OID-required",
    "base_main_sha": "full-40-character-Git-OID-required"
  },
  "dependencies": {"contract_digest": "sha256:example", "candidate_ids": []},
  "evidence": {
    "bundle_digest": "sha256:example",
    "required_check_ids": ["build", "unit", "integration"],
    "source_check_status": "unverified",
    "merge_result_check_status": "unverified"
  },
  "admission": {
    "decision": "pending_independent_qa",
    "decision_actor": null,
    "proposed_merge_sha": null,
    "actual_integrated_sha": null
  },
  "release": {"approved": false}
}
```

Placeholders above deliberately do not masquerade as real Git SHAs/evidence. A later JSON Schema must prohibit these placeholders in executable submissions, validate hash algorithm/length, check strict required fields, and use version negotiation.

Model brand, prompt stack, inference host and runtime may be included as optional execution provenance but may **not** determine admissibility in place of outcome evidence.

## 6. Admission is a serialized decision, not serialized development

Only the **protected mainline publication step** must be globally coordinated per target ref. Development and much of testing can remain massively parallel.

- Candidates undergo preliminary testing independently.
- A dependency-aware queue admits eligible candidates or coherent batches.
- The queue constructs a prospective merge group against **the latest current main** and relevant predecessor candidates.
- Independently trusted checks execute against the **merge-group result**.
- Admission must be bound to that verified group and target base; a new main SHA, changed dependency or changed candidate source invalidates affected checks.
- A protected merge controller / repository ruleset serializes actual publication or relies on verified native merge-queue guarantees.
- Post-merge integration verification confirms actual `main` SHA and sandbox behavior before recording `integrated`.
- Production deployment, feature enablement and release completion remain distinct approvals.

For GitHub Actions and native merge queue, required workflows must handle `merge_group` triggers. GitHub merge queues can test speculative merge groups that contain the latest base and queued changes. See https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue .

**Batch rule:** batch by dependency compatibility and check cost, not the time agents submitted work. If a group fails, isolate offending candidates (e.g. queue bisect/retry) without falsely advancing unrelated tasks.

## 7. Authority matrix

| Operation | Worker | Task coordinator | Independent QA | Protected integration controller | Release approver |
|---|---:|---:|---:|---:|---:|
| Read permitted tasks/source | scoped | yes | scoped | yes | yes |
| Claim task/renew lease | request | issue/revoke | observe | observe | observe |
| Submit artifact/patch/own branch | scoped | provision | test only | ingest | no |
| Update authoritative task admission status | no | rule-bound projection | submit verdict | postmerge event | release event |
| Publish independent check verdict | no self-approval | no | yes | check gate | no |
| Write protected mainline | no | no | no | authorized gated action | no |
| Change production/release state | no | no | no unless separately approved | only gated deploy mechanics | approve |

This is conceptual authority, not a statement that existing GitHub settings enforce it. Identity should be independently authenticated, grants scoped per repo/ref/resource, and revocations effective at action time.

## 8. GitHub-specific operational options

**Small scale:** one agent/attempt branch, PR, required reviews and status checks, automatic sync/rebase on stale candidates via coordinated service; default deny force pushes. A dedicated merger owns `main`.

**Higher scale:** GitHub merge queue (where plan/repo supports it), required `merge_group` CI, a dependency-aware admission scheduler, protected checks from specified trusted GitHub Apps, bounded queue concurrency, and a reconciler for webhook delivery/CI failures.

**Cross-organization:** fork-based contribution with explicit repository permissions; GitHub App installation tokens rather than sharing personal access tokens; provider-neutral task and evidence manifests can come from external organizations. Contributors may submit candidate bundles without write access.

**If GitHub alone is insufficient:** maintain a Foromni-owned event ledger for task leases/fencing/idempotency and independent QA decisions, while Git remains authoritative for actual commit/ref state. Avoid distributed transactions across the two; reconcile after partial failures.

**Do not build a custom Git host or merge queue initially.** Research existing controls and measure the gap first.

## 9. Safe worker pseudocode (non-executable model)

```text
claim(task, task_revision):
  coordinator verifies capabilities, access and dependency readiness
  issue unique attempt, workspace/ref, bounded lease_epoch and token

prepare(attempt):
  read main SHA, current branch SHA and dependency versions
  create candidate commit(s) in isolated workspace
  run local preliminary checks
  submit source artifact + evidence, never self-admit

write_candidate(attempt, expected_ref, new_commit):
  trusted ref-writer verifies current lease epoch and permitted branch
  if current remote ref != expected_ref: reject STALE_HEAD
  if new_commit not valid descendant of remote ref: reject NON_FAST_FORWARD
  attempt conditional ref update; on any race: reject/reconcile
  read back the ref; record successful authoritative SHA

admit(candidate):
  independent QA verifies task spec, artifact, tests, authorization
  queue coordinator computes dependency-compatible position
  synthesize merge result against latest main and queued candidates
  execute required checks on synthesized merge result
  if main/base/source/dependencies changed: invalidate/requeue
  if failed: return to repair with precise logs
  if fully passed: protected controller publishes to main and records actual SHA
  run post-merge integration verification; emit integrated event or repair event
```

Agent-to-agent messaging (A2A or otherwise) and tool invocation (MCP or otherwise) are adapters; they cannot bypass the authority boundaries above.

## 10. Synchronization and recovery invariants

1. A **fetch is safe** alongside remote pushes; local snapshots must be treated as potentially stale.
2. Every shared ref mutation must enforce fast-forward/non-overwrite behavior, expected state where supported, authorization and current fencing token.
3. No two agents have unrestricted write authority to the same shared branch.
4. No untrusted worker can force push or directly merge main.
5. Each execution attempt and artifact is immutable/recoverable even after rejection.
6. Duplicated webhooks and retries cannot duplicate acceptance or protected merges.
7. A worker that loses the lease can submit a **new proposal**, not authoritative updates.
8. QA is bound to exact task revision, source revision, dependency digest, merge-result revision, validator version and environment.
9. Every new change to these inputs invalidates the applicable evidence; the policy determines which checks must rerun.
10. Mainline commits are associated with a unique admission decision and evidence.
11. If the ledger and GitHub diverge, reconcile from actual Git refs/CI and log discrepancies. Never invent success.
12. The system may reject, split, defer or abandon incompatible candidates without destroying their contributions.
13. Worker concurrency is elastic; merge publication is coordinated per target ref, avoiding unnecessary global lock across unrelated repositories.
14. With delayed webhooks or partial network partitions, fail closed for protected transitions; continue permitted isolated work.

## 11. Adversarial tabletop test plan (not yet executed)

| Scenario | Expected result |
|---|---|
| Two workers read same branch A, one pushes B | Second divergent push rejected; candidate retained; safe reconcile path |
| Agent pulls while another pushes | Fetch completes; stale read detected at subsequent write/admission gate |
| Force push attempted on protected ref | Denied by permissions/ruleset |
| Compromised worker bypasses coordinator with leaked credentials | Ref ACL denies; revoke affected credentials and audit |
| Lease expires after candidate creation | Old token cannot mutate authoritative ref; candidate may be resubmitted under new attempt |
| Repo ref moves after pre-write read | Conditional write fails rather than clobbering newer state |
| Two non-conflicting Git patches alter incompatible API contracts | Semantic/contract check fails merge-group integration |
| CI success on SHA S, source changes to S2 | Requalification mandatory; no stale approval |
| Main advances while queue tests earlier base | Queue regeneration or requalification required |
| Two admission controllers attempt merge | Protected serialized admission or one CAS success only |
| Ledger write fails after successful merge | Reconciler discovers actual integrated SHA, idempotent completion event |
| Duplicate CI/webhook events | No duplicated status, branch write or approval |
| Contributor switches cloud ↔ legacy self-hosted model | Same task contract; separate attempt evidence as appropriate |
| 10,000 candidate submissions | Backpressure, task prioritization and bounded test spend; no bypass |
| Failed release after successful merge | Integrated remains historically true; incident/rollback is recorded separately |

## 12. Immediate research outputs (do not build yet)

- Formal JSON Schemas: Task, Attempt, Candidate, Evidence, Admission Decision, Branch Write Request.
- State-transition table showing who can transition each state and what exact evidence is required.
- Conflict resolver decision tree for stale branch, semantic conflict, dependency conflict, revoked lease, and stale QA.
- Synthetic event log for two concurrent writers plus a stale QA result, and expected projections.
- Comparison of GitHub protected refs / merge queue to a dedicated transactional coordinator, including limits and costs.
- Human/workforce coordination policy for task ownership and conflict escalation.
- Operational metrics: branch update conflicts, rebase churn, candidate freshness, queue age, accepted throughput, cost per valid integration.

## 13. Implementation decision gate

Research approval does **not** authorize branch-rule edits, a hosted controller, new GitHub App privileges, paid services, merging PRs or cross-project work.

Proceed to a technical spike only when contract invariants, authority matrix, exact-SHA QA rule and adversarial tests have been reviewed. Then test with synthetic tasks and disposable branches before giving real agents shared write authority.

**Founder's problem statement:** Thousands of independently operated agents may work at once. Their contributions must converge into one reliable product *without competing for the same branch, overwriting history, accepting stale tests, or conflating passing work with integrated work*.

**Foromni's foundational product:** A safe, open, evidence-driven synchronization and convergence protocol—not a globally shared mutable branch.
