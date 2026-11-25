# Hybrid AINO Engineering Stack: Adopt / Extend / Reject Decision Framework

**Status:** Research proposal; no platform selection, implementation, integration or deployment authorized.  
**Date:** 2026-11-21. **Repository:** Foromni-Network/forOmni. **Project isolation:** No Internet Embassy code, tasks, infrastructure, or repo modifications.

## Thesis

Foromni's durable competitive contribution should be a **portable convergence contract** joining mature external systems—not rebuilding every roadmap, forge, agent runner, CI service or deployment pipeline. Assemble only after independent evidence establishes which components satisfy the contract, and preserve export/migration paths so any chosen vendor can be replaced.

**Value proposition:** Many independently operated agents (including self-hosted, old and new models, humans and deterministic workers) can safely contribute useful work, see why a task is blocked, repair failures, and reach verifiable completion. The unit of output is an accepted integrated result, not a PR, prompt, task count or model call.

## Four layers and their initial candidate families

| Layer | Consider adopting | Foromni-owned missing contract | Avoid building initially |
|---|---|---|---|
| Roadmap view/intake | It's a Plan, Plane, OpenProject, GitHub Projects | Portable versioned task IDs, acceptance contracts, authority/events | Another Kanban UI |
| Worker connectivity | A2A, MCP, external CLI runners, OpenHands SDK | Worker attestations, task leases, expiration/fencing, handoff, provenance | A proprietary agent runtime |
| Evidence and integration | GitHub checks/protected refs/merge queue; Zuul; Prow/Tide | Task-bound independent acceptance; consistency between task, source SHA, merge result and actual integrated SHA | New Git host, CI engine, merge queue |
| Operations and learning | Existing telemetry, CI and event exports | Cross-provider acceptance yield, queue aging, cost per verified result, failure taxonomy | A broad AI analytics suite |

**Trust boundary:** A task board and worker runner may help, but neither grants protected merge/release authority. The integration controller verifies current source and prospective merge state independently. A self-hosted model is still untrusted for self-certification.

## Source-based findings to carry forward

- [It's a Plan changelog](https://itsaplan.dev/changelog/v1.10.0) describes agent workflows and MCP-triggered runs (Nov. 5, 2026). This is a strong **agent-workflow candidate**, not proof of atomic leases, independent QA or merge-result checks.
- [Zuul project gating](https://zuul-ci.org/docs/zuul/latest/gating.html) documents speculative dependent pipelines: jobs test proposed cumulative changes as if gated sequentially, while running in parallel.
- [Prow Tide](https://docs.prow.k8s.io/docs/components/core/tide/) automatically retests eligible PRs and merges those with current passing checks; [scaling guidance](https://docs.prow.k8s.io/docs/scaling/) describes batching and safe handling of untrusted PR tests.
- [OpenProject GitHub integration](https://www.openproject.org/docs/system-admin-guide/integrations/github-integration/) links work packages to source control and supports branch/PR workflows; [API docs](https://www.openproject.org/docs/api/) note that API coverage is evolving.
- [Plane self-hosted](https://plane.so/self-hosted) offers self-hosting, but free/community versus paid-feature details, license terms and available agent capabilities must be verified for the *exact version/edition* before choosing.

No product above has been installed, tested, or endorsed for Foromni.

## Adoption scorecard (score against verified evidence, not marketing)

Each requirement is graded 0=unsupported, 1=claimed/unclear, 2=demonstrated in reproducible tabletop or sandbox, 3=adversarially validated with measurable results. **Unverified is not zero**; label it unknown until tested.

1. **Concurrency correctness:** conditional writes, lease/fencing enforcement, idempotency, duplicate event handling, conflict recovery.
2. **Admission integrity:** exact task acceptance revision, source SHA, prospective merge SHA, independent QA, protected merge control, post-merge proof.
3. **Interoperability:** open APIs, export/import, adapters for models and humans, neutral protocol, clear versioning.
4. **Self-hosting and sovereignty:** deployment footprint, backups, auth, data residency, offline support, no required hosted inference.
5. **Security/trust:** least privilege, permission revocation, untrusted execution isolation, secret handling, vulnerable dependency response.
6. **Operating economics:** total cost to operate, CI throughput, cost per independently accepted task, staff maintenance, tail latency.
7. **Product utility:** roadmap usability, dependency visibility, ownership, recovery, creator/maintainer experience.
8. **Licensing/maintenance:** actual licenses and terms, contributor provenance, community health, support and update frequency.

**Gates:** Any failure of core safety invariants (unsupported protected write checks, fabricated QA acceptance, task version drift, leakage of restricted information) disqualifies direct use in the protected integration path regardless of total score. An adapter or gated augmentation can still be considered.

## Proposed decision process

1. Inventory the actual Foromni needs and risk levels; define a small, public synthetic task suite.
2. Read upstream architecture, docs, API schemas, releases, tests and open incidents for each candidate; record snapshot/version/license.
3. **Adopt** features proven to meet acceptance and nonfunctional requirements.
4. **Extend via adapter** where the upstream project provides a sound core but lacks a neutral task/evidence/authority contract.
5. **Contribute upstream** generic fixes when permission and licensing permit, rather than maintaining a permanent fork.
6. **Reject or defer** features that add unnecessary operational dependencies, excessive privilege, poor migration paths or unproven guarantees.
7. Benchmark two minimum viable combinations before selecting a deployment architecture.
8. Record an architecture decision for every accepted component with version, source, license, maintainer, integration boundaries, replacement plan and evidence.
9. Make major platform changes contingent on explicit Founder authorization.

## Initial candidate experiments to design (not run)

**A. GitHub-first + neutral contract:** 10 synthetic tasks, 3 independent worker adapters, one safe task claim/retry, exact-SHA tests, PR merge admission, deliberately stale source and duplicate webhook.

**B. It's a Plan + neutral contract + GitHub merge gate:** Same task specification and expected evidence, but use the agent-friendly tracker. Verify whether ownership/leases are really enforced or just advisory.

**C. Plane/OpenProject + Zuul/Prow:** Later study if genuine large-team scheduling, multi-repository dependencies, and high-throughput batch admission require the additional infrastructure.

**Selection standard:** The best candidate is the *simplest viable combination that survives adversarial tests*, not the option with the longest feature list.

## Why the hybrid approach matters at 1,000+ agents

Without limits, the arrival rate of candidate features can overwhelm testing and merging capacity. The system must dynamically:

- Limit work-in-progress by dependency and integration capacity.
- Route workers toward incomplete/rejected/blocked tasks before speculative new features.
- Reserve exclusive writes narrowly; allow unrestricted authorized reads and isolated drafts.
- Preserve rejected work and failure evidence for recovery, avoiding repeated agent churn.
- Divide large features into individually verifiable, backward-compatible increments.
- Track real queue age and throughput instead of PR volume.
- Expose learning signals: recurring conflicts, missing contracts, stale SHAs, repeated failures and costs.

## Research/documentation-only deliverables needed next

- Detailed source-code reviews of It's a Plan claim/runner logic; Zuul dependency pipelines; Prow Tide batching/merge policies.
- A capability-by-capability comparison of **tested** versions and licenses, with documented unknowns.
- Formal Convergence Contract JSON Schemas, authority-transition table and threat model.
- A runnable **synthetic** integration acceptance test plan (without deployment).
- A global AINO case study translating software convergence into research, operations and non-code contribution acceptance.

## IE educational relationship — strictly documentation, not integration

The ideas can inspire educational content for IE Growth, Learn and Entrepreneur pillar teams **if the Founder separately authorizes content use**. Do not create IE tasks, publish content, copy Foromni code into IE, or assert a completed cross-project relationship. Keep origin/provenance attribution and label experimental concepts honestly.

**Founder principle:** Borrow what works, extend what is missing, reject what adds fragility, and keep the AINO's truth layer independent of any single vendor.
