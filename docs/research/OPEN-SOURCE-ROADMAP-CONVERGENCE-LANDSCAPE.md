# Open-Source Engineering Roadmap and Convergence Stack — Comparative Research

**Research-only** · 2026-11-21 · **Project:** Foromni only · **No IE changes**  
**Status:** Candidate scan; desk research from upstream repositories and documentation, not a deployed or benchmarked evaluation.  
**Companion:** [Convergence Contract v0.1](CONVERGENCE-CONTRACT-V0.1.md)

## Executive finding

There are credible open-source systems for **different layers** of the problem, but no evaluated project in this scan has demonstrated the entire Foromni goal: thousands of heterogeneous, independently operated agents discovering and claiming roadmap work, safely maintaining concurrent attempts, proving acceptance with independent evidence, and merging dependency-compatible work into a trustworthy mainline while remaining provider-neutral.

**Do not build a roadmap UI, task tracker, CI server or merge queue from scratch yet.** Research integration of existing components through the versioned Convergence Contract. Best candidates to investigate in depth:

- **It's a Plan (itsaplan):** especially close to Foromni's *agent-enabled issue/workflow* surface: self-hosted tracker, REST/OpenAPI, MCP, webhooks, external runners and multi-forge PR integrations. Evaluate agent claim fencing, task event provenance, permissions, reliability, licensing and current maturity. Agent integration is not proof of independent admission or mainline correctness.
- **Plane** and **OpenProject:** comparatively established open-source roadmap/work-package interfaces, with work-item organization and planning. Check which dependency, workflow, API, self-hosted and access-control features actually exist in the intended free/open distribution. Neither should be assumed to provide agent leases or protected merge admission.
- **Zuul:** high-priority study for speculative, dependency-aware pre-merge testing of *future combined repository states*. Its dependent pipeline directly tackles the convergence bottleneck.
- **Kubernetes Prow/Tide:** high-priority study for GitHub-native large-scale PR pooling, up-to-date tests and batch merge automation; actual Kubernetes-scale deployment examples are useful, but operations and privileged tokens add substantial overhead.
- **Gerrit:** mature review/submit requirements and large-scale change submission with separate verification controls; adopting its alternative review workflow would be a major forge/process change.
- **GitHub native protected branches/merge queue** (not open-source software itself): preferred baseline for a GitHub-hosted Foromni prototype; compare to Zuul/Prow rather than rebuilding features already available.
- **OpenHands SDK / resolver:** possible execution worker adapter, **not** an acceptance ledger, roadmap authority, or merge gate.
- **Backstage:** developer portal/catalog and software templates, not a core task acceptance/merge engine.
- **Forgejo + external merge queue solutions:** possible fully self-hosted repository layer, but do not migrate for ideology; evaluate actual integration, permission, maintenance and reliability constraints.

## 1. Shortlist with clear division of responsibilities

| Product/repository | Best demonstrated role | Relevant published capabilities | Key gap to verify before adoption |
|---|---|---|---|
| [It's a Plan](https://github.com/croffasia/itsaplan) | Roadmap + agent participation | Self-hosted issue planning, MCP, REST, webhook, local external agent runner; integrations with several Git forges | Lease fencing under actual races, audit/evidence authority, independent acceptance, integration result checks, maturity |
| [Plane](https://github.com/makeplane/plane) | Product planning | Issues/work items, cycles, modules, roadmap/project views, self-hosted community edition | Whether needed dependencies, granular approvals, agent participation and workflows are present in chosen edition |
| [OpenProject](https://github.com/opf/openproject) | Structured large-team planning | Work packages, configurable workflows, dependencies, API and GitHub integration | Agent-native claims/leases, exact-SHA QA, merge queue |
| [Zuul](https://github.com/zuul/zuul) | Speculative integration gating | Dependent pipeline tests proposed change combinations in parallel to protect mainline | Deployment/operations complexity; independent roadmap acceptance |
| [Prow](https://github.com/kubernetes-sigs/prow) / Tide | GitHub PR aggregation and merges | Label/policy eligibility, up-to-date pre-merge tests, batching, dozens of org/repo pools | Kubernetes infrastructure/permissions, task semantics, security boundaries of untrusted code |
| [Gerrit](https://gerrit.googlesource.com/gerrit/) | Controlled code review | Submit requirements, review labels, approval policies | New code review paradigm; no general roadmap/orchestration semantics |
| [Backstage](https://github.com/backstage/backstage) | Developer portal & software catalog | Catalog, plugin ecosystem, standardized templates | No native end-to-end agent convergence guarantee |
| [OpenHands SDK](https://github.com/OpenHands/software-agent-sdk) | Swappable coding-worker adapter | Python/TS/REST agent SDK and software-development runtime | Human/agent completion claims still need external independent verification |
| [Forgejo](https://codeberg.org/forgejo/forgejo) | Self-hosted forge | Git hosting, PRs, issues, Actions, webhooks, permissions | Distinct merge-queue/agent orchestration needed; migration and operations costs |

**Not an endorsement:** Features can be edition-restricted, unstable, missing, or non-equivalent between hosted and self-hosted distributions. All candidates need current code/release, licensing, permission, and adversarial validation before production use.

## 2. Most relevant *combinations*

### Candidate A — Minimal GitHub-first research pilot
- GitHub Issues/Projects as visible roadmap and human work intake.
- Foromni-owned task/attempt/evidence/admission contract and projection.
- GitHub App with narrowly scoped branch/PR access and protected main.
- GitHub Actions/merge queue as initial build-and-combination verification.
- Pluggable worker adapters (OpenHands SDK, external CLIs, small self-hosted models or scripts).

**Advantages:** Fits current repository; lowest new operational footprint. **Limits:** Some GitHub protections/queues may depend on repository plan, configuration, or permissions; GitHub is not a transactional lease/actor ledger; vendor-dependent forge.

### Candidate B — Itsaplan + GitHub merge queue or Zuul
- Use itsaplan for human/agent task assignments and operational view.
- Add Convergence Contract adapter and independent verification ledger.
- Let GitHub/Zuul own actual Git ref/merge-result checks.
- Keep provider and worker runtimes fully interchangeable.

**Advantages:** Existing agent-friendly UI/runner could save significant development. **Risks:** Ownership/version reconciliation between task board and GitHub, license network obligations, maturity, security, and overlap with Foromni's native authority.

### Candidate C — Plane or OpenProject + Prow/Zuul
- Mature planning/work-package surface.
- Convergence/agent layer implemented as a small independent adapter.
- Prow/Tide or Zuul protects the integration mainline.
- Optional Backstage catalog for many products/repositories.

**Advantages:** May suit large human/agent organizations. **Risks:** Higher integration/ops complexity and extensive mapping of task statuses, approvals and cross-system permissions.

### Candidate D — Fully self-hosted Forgejo + roadmap + gate
- Forgejo as self-hosted Git forge; Plane/OpenProject/itsaplan as planner.
- Evaluate Prow/Zuul/third-party queue compatibility rather than assume.
- Vendor-neutral Convergence Contract and independent gate still required.

**Advantages:** Infrastructural sovereignty. **Risks:** Patch/security operations and the burden of reproducing GitHub's ecosystem; defer until a proven need.

**Recommendation:** Benchmark A and B first with *synthetic* tasks; research Zuul and Prow deeply as established examples of convergence control. Avoid deploying a complex suite solely for a documentation/research phase.

## 3. Feature verification matrix

Scale: **D** = described in upstream docs, **?** = not established in this desk review. These symbols are *not test results*.

| Requirement | Itsaplan | Plane/OpenProject | Zuul | Prow/Tide | GitHub |
|---|---|---|---|---|---|
| Human roadmap / work-item UX | D | D | ? | ? | D |
| External heterogeneous agents | D (runner) | ? | Worker jobs (not general agents) | Worker jobs (not general agents) | API adapters |
| Self-hosting | D | D | D | D | No, GitHub SaaS |
| Dependency-aware integration testing | ? | ? | D | D (batch) | D (merge queue; availability varies) |
| Explicit task lease/fencing and offline recovery | Verify | ? | Not general purpose | Not general purpose | Not native |
| Independently attested exact-task-version acceptance | Not demonstrated | Not demonstrated | CI gate, not task acceptance | CI gate, not task acceptance | Checks/reviews, not full task proof |
| Protected mainline merge checks | Via forge | Via forge | D | D | D |
| Cross-provider model independence | Runner lists multiple CLIs | Adapter needed | Runner-neutral tests | Runner-neutral tests | Adapter needed |
| End-to-end verified roadmap-to-release | **Not demonstrated** | **Not demonstrated** | **Not demonstrated** | **Not demonstrated** | **Not demonstrated** |

**Never interpret '?' as 'no'.** Conduct targeted source/doc inspection and tests for unresolved rows.

## 4. Underappreciated lessons

1. **Do not confuse roadmap software with the integration controller.** A polished task UI does not prevent competing write ownership, stale CI, invalid source SHAs or false-green statuses.
2. **Zuul and Tide are directly relevant to the hard problem.** They converge changes after verifying prospective combined states; study their queues, invalidation behavior, resource quotas and fallback paths.
3. **The right unit of concurrency is not a branch name.** It is the versioned task attempt plus its exclusive authorized ref-write lease and evidence bundle.
4. **Do not grant agents broad repository credentials just to connect a tracker.** Use separate scopes for intake, read-only discovery, candidate writes, independent QA and protected merges.
5. **Agent-friendly features can increase risk without durable attempts.** A tool that starts 100 simultaneous coding jobs is counterproductive unless it bounds ownership, revisions, retries, costs and admission.
6. **Forks/branching scale contribution; coordinated mainline gates scale trust.**
7. **Plan to migrate away from any UI.** Convergence Contract events and artifacts should export/import independently so an AINO is not locked to its first issue tracker.

## 5. Experimental comparison protocol — before adoption

Use the same synthetic workload across viable candidate combinations:

- 30 tasks with dependencies (including a critical path and circular-dependency rejection).
- 12 agent workers: 4 cloud model runtimes, 4 local/self-hosted or older model runtimes, 4 deterministic/human test participants.
- 5 overlapping patch sets to one API, 2 incompatible migrations, 1 stale branch, 1 expired worker lease, duplicate webhook delivery, 1 forged CI URL, 1 late QA verdict, 1 controller crash and one protected release approval.
- Tests execute in a disposable sandbox, with separate accounts/permissions and no IE resources.
- Measure accepted/mainline-integrated outputs per hour, queue latency percentiles, stale-ref write rejections, lost/overwritten accepted commits, independent false-green admissions (target 0), recovery rate, resource cost per accepted change and operational complexity.
- Verify all access/authorization assertions with a real adversarial test; no vendor marketing comparison alone is adequate.
- Compare cost/licensing, self-hosting maintenance burden, API coverage, extensibility, accessibility and worker portability.

**Do not run these tests or deploy infrastructure under current research-only authorization.**

## 6. Targeted repository studies to perform next

**Highest priority (inspect source, not just README):**
1. [Itsaplan](https://github.com/croffasia/itsaplan): runner claims and fencing, expired attempts, webhook handling, PR integration and ability to use a custom task/evidence protocol. Inspect changelog and open PRs—some improvements may be *proposed*, not merged.
2. [Zuul](https://zuul-ci.org/docs/zuul/latest/gating.html): speculative execution graph, dependent pipeline, queue invalidation/reconfiguration, multi-repo dependency ordering.
3. [Prow Tide](https://docs.prow.k8s.io/docs/components/core/tide/): query/eligibility, batch test, merge behavior and required trust/permissions; review [scaling guidance](https://docs.prow.k8s.io/docs/scaling/).

**Second priority:**
4. [Plane](https://github.com/makeplane/plane) vs [OpenProject](https://www.openproject.org/docs/): self-hosted roadmap and dependency workflows with actual API surface.
5. GitHub native merge queue and branch protection vs independent gate; document plan limits and `merge_group` CI triggers.
6. [Gerrit](https://gerrit-review.googlesource.com/Documentation/config-submit-requirements.html), [Forgejo](https://forgejo.org/), [Backstage](https://backstage.io/) as alternatives for future scale/sovereignty rather than prerequisites.

## 7. Required decisions before selecting a stack

- Is Foromni's canonical roadmap ledger independent of any UI, with UI as replaceable projection?
- Which task event fields and gate decisions are normative vs informative?
- Which evidence forms count as independently reproduced acceptance for code and *non-code* tasks?
- Can multiple distinct organizations operate workers without sharing credentials or centralizing private data?
- Which stack handles optimistic concurrency, leases/fencing, idempotency and durable handoff?
- Which integration gate can prove changes as combined on the latest actual mainline, including dependency-linked changes?
- What is the minimum practical deployment that permits controlled tests before building more Foromni features?
- What are each candidate's actual licenses (including AGPL or commercial restrictions) and obligations for hosting/adaptation?

## 8. Source list (official upstream or canonical source)

- https://github.com/croffasia/itsaplan
- https://github.com/croffasia/itsaplan/blob/main/README.md
- https://github.com/croffasia/itsaplan/blob/main/CHANGELOG.md
- https://github.com/makeplane/plane
- https://plane.so/open-source
- https://github.com/opf/openproject
- https://www.openproject.org/docs/api/endpoints/work-packages/
- https://www.openproject.org/docs/system-admin-guide/integrations/github-integration/
- https://zuul-ci.org/docs/zuul/latest/gating.html
- https://zuul-ci.org/docs/zuul/latest/config/pipeline.html
- https://github.com/kubernetes-sigs/prow
- https://docs.prow.k8s.io/docs/components/core/tide/
- https://docs.prow.k8s.io/docs/scaling/
- https://gerrit-review.googlesource.com/Documentation/config-submit-requirements.html
- https://backstage.io/plugins/
- https://github.com/OpenHands/software-agent-sdk
- https://forgejo.org/

## Conclusion

**Buy/adopt/extend the existing planning, agent, CI and merge systems where they are good; let Foromni own the missing cross-system convergence semantics.** The value is a portable, evidence-backed work contract linking those tools, not a competing clone of each one.

The next action is a **deep technical feasibility and adversarial-readiness review** of It's a Plan, Zuul and Prow, documenting exactly which contract invariants each can enforce and what minimal adapter would be needed. No claim of working integration is made.
