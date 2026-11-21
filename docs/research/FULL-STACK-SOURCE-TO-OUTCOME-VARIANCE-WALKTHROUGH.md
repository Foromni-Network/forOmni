# Full-Stack Source-to-Outcome Walkthrough: Coordination Loss Accounting

**Status:** Hypothetical Foromni research case. No code, tests, real agents or releases were run. Date: 2026-11-21.
**Scope:** Foromni only; Internet Embassy is independent and untouched.
**Related:** FULL-STACK-REFERENCE-APP-CONFORMANCE-V0.2.md; ECONOMETRICS-OF-CONVERGENCE-AND-COORDINATION-VARIANCE.md; CONVERGENCE-WORK-PACKET-TYPED-CONTRACT-V0.2.md; POST-CONVERGENCE-RELEASE-OPERATIONS-IMPROVEMENT.md.

## Founder objective and fixed required outcome

Using the fictional Collective Lab app, build accessible authenticated project/task UI with API and PostgreSQL persistence. Verify that project A owner Ada can assign tasks, project A viewer Cy cannot mutate, and unrelated project B owner Dee cannot read private A data. All synthetic identities; no live outreach/real-world user data.

Acceptance is one complete functioning vertical slice under independent testing and a separately authorized release boundary. An agent claiming it wrote a component is not an accepted outcome.

## The end-to-end chain (illustrative events only)

| Phase | Decision / actor | Data relation preserved | Independent acceptance / variance measurement |
|---|---|---|---|
| 01 Objective | Owner approves project behavior and restrictions | objective ID, revision, acceptance | Unclear needs become rework only if unrecognized |
| 02 Architecture | AI architect proposes Next.js + one approved PostgreSQL/auth backend | schema/API decisions linked to spec | Compare setup overhead, avoid architectural drift |
| 03 Roadmap | AI coordinator decomposes V0 shell, V1 auth, V2 projects, V3 tasks | task IDs, DAG, task revision and owner | Duplicate/missing scopes tracked |
| 04 Relationships | Workers accept shared membership/API/data contracts | API digest, task dependencies, reviewer principal | Detect frontend/backend mismatch before implementation |
| 05 Synchronization | Trusted planner reads current main and grants isolated scoped attempts | source commit, branch, lease epoch and budget | Old assumptions invalidated only where relevant |
| 06 Coding | UI and API/data AI workers implement and self-check | source SHA, tool/model/runtime/cost | Self-report counts as attempt, not accepted deliverable |
| 07 Handoff | Candidates reference unchanged acceptance and source evidence | PR/candidate IDs, test run inputs | Rework due to stale handoff is recorded |
| 08 Independent QA | Separate reviewer tests access, browser, database | exact candidate SHA, isolated principal | Reject incorrect RBAC and API fields |
| 09 Protected convergence | Merge gate checks combined current revision | actual merge-group SHA, protected authority | False-green branches cannot bypass integration |
| 10 Build/staging | Trusted pipeline produces immutable artifact and synthetic staging | artifact digest, exact source mapping | Build/provision failure recorded |
| 11 Release boundary | Accountable owner may authorize future public release | scoped approval identity and expiry | For this research, no publication authorized |
| 12 Operations | If deployed in an authorized later experiment, track errors and impact | event provenance and repair task | Release != healthy != beneficial |
| 13 Learning | Analysts compare candidate strategies and failed attempts | full cost/failed runs and method versions | No cherry-picked winning example |
| 14 Evidence publication | Claim review attaches actual run data and limitations | published study/claim revision and rights | No empirical claims from this tabletop |

## An example of the suspected econometric mechanism

A frontend worker expects member.displayName, while the backend returns member.name. Without early contract agreement, each candidate could pass isolated checks, causing failed combined tests and repair. With preflight, a versioned API agreement may expose the mismatch before code is authored. That may shift some work to planning and lower downstream rework—but the net effect requires measured costs and repeated trials.

### Cost ledger for both experimental arms

- Requirement interpretation/planning and agent model usage
- Source generation and local self-checks
- Dependency negotiation and conflict reconciliation
- Candidate review and independent QA compute/human attention
- CI invalidation/retries and source admission delays
- Build and staging resources
- Failure, abandoned attempts and timeouts
- Oversight and meaningful policy approvals

Never omit treatment planning expense or discard failed control attempts. Report completed and incomplete outcomes by the authorized horizon.

## Causal diagnostic map

Input complexity and dependency density -> roadmap alignment -> interface relationships -> source/revision synchronization -> candidate QA/integration repair -> accepted functionality -> release/real-world outcomes.

Potential confounders: task complexity, agent-model capability, context length, hosting characteristics, evaluator independence, developer familiarity and QA capacity. Randomize or block where possible; do not infer cause from correlation between coordinator activity and deliverables.

## Remaining end-to-end research blockers before a real experiment

1. Select and pin the test runtime and exact approved auth/DB architecture; include versions and support policies.
2. Freeze role matrix, API response fields, accessible UX fixtures and migration semantics.
3. Verify available protected Git admission and independent CI capabilities in the isolated experiment repo.
4. Decide the actual sandbox and environment teardown/secret restrictions.
5. Design resource and evidence ledger with zero unaccounted costs; establish right-censored treatment of unfinished work.
6. Independently review safety cases, code/test separation and controlled experiment allocation.
7. Seek explicit founder authorization for a bounded disposable application build and trial; no existing authorization is assumed.

Broader agent-to-agent protocols remain queued after the end-to-end research; cybersecurity beyond baseline experiment safeguards remains deferred.

*Build today, so others can enjoy tomorrow.*