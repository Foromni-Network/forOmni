# Research Roadmap: Can One Agent or a Team Deliver Full-Stack Software End to End?

**Status:** R&D BACKLOG / EXPERIMENT DESIGN ONLY; no platform build or model spending authorized.  
**Date:** 2026-11-21. **Project:** Foromni, independent of Internet Embassy.  
**Priority:** Proposed R&D track after foundational convergence/QA invariants are documented.  
**Related:** GLOBAL-AGENT-ROADMAP-EXECUTION.md; SYNTHETIC-TEN-WORKER-CONVERGENCE-TRACE.md; PROVIDER-AGNOSTIC-AGENT-EXECUTION.md; CROSS-DOMAIN-CONVERGENCE-CONTRACT-V0.2.md.

## Core question

**Can one AI worker—or a team of independent agents—turn a loosely framed product need into an actually usable, secure, maintainable full-stack application, from discovery through deployment, monitoring and postrelease support?**

Do not assume more agents or more specialized prompts improve net outcome. Coordination, redundant work and integration can erase apparent generation advantages. Evaluate *single focused worker*, *small specialist group*, and *large "studio" team* on the same product specification, with independent acceptance.

## Why this must be evaluated against reality

Public software-agent benchmarks are not the same as end-to-end product delivery: patching an existing repository with predefined tests is different from gathering requirements, designing contracts, building a database/backend/frontend, authenticating users, deploying and supporting them.

- SWE-bench Pro introduced longer-horizon, more realistic software engineering tasks than earlier benchmarks; its measured outcomes depend on model, scaffold, task version and test conditions. https://arxiv.org/abs/2509.16941
- OpenAI reported in February 2026 that SWE-bench Verified is no longer a reliable frontier evaluation target because of data contamination and test/assessment problems; this reinforces avoiding leaderboard-only procurement decisions. https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- SWE-bench Pro V2 and verified variants continue evolving; pin benchmark dataset versions and avoid comparing unlike scores. https://arxiv.org/abs/2610.24206
- OpenHands' SDK provides agent/tool/workspace building blocks, but possessing an agent runtime is not proof of full-stack delivery. https://github.com/OpenHands/software-agent-sdk
- GitHub merge queue and Zuul speculative gating support safe integration, but do not determine whether the deployed product satisfies its actual users. https://zuul-ci.org/docs/zuul/latest/gating.html

## Research tracks

### Track A — One focused full-stack agent

A single worker has scoped access to read requirements, propose architecture, edit isolated code, write tests and infrastructure config, and submit one or more independent PRs. A **separate** QA/verifier is still required for protected acceptance; "one agent developed it" is not "one agent self-approved it."

Questions: Can a single agent preserve context through weeks of iteration? How much prompt scaffolding helps? Does giving it a long-lived memory make stale assumptions worse? When should it stop and request a human architectural decision?

### Track B — Small specialized team (3–5)

Potential roles: product/specification, architecture/contracts, backend/data/auth, frontend/UX, independent test/security. One coordinator owns the dependency graph. Exact role composition should be an experimental variable, not a permanent org chart.

Questions: Are branch handoffs worth their cost? Does a shared schema/API contract reduce conflict? Can the integrator reliably distinguish completion from a PR claim? How much duplication emerges?

### Track C — Larger studio (8–15+)

Roles may include design system, accessibility, data, backend, integrations, security, test automation, performance, docs, SRE, release and repair. Expand only if the product has enough independently parallelizable work and the convergence gate scales.

Questions: What is the coordination overhead? How many independent verification lanes are needed? Is a single planning model bottlenecking delegation? What are queue stability and accepted throughput at 8, 15, 50 workers?

### Track D — Hybrid changing-size team

Begin with one generalist and a human stakeholder; recruit specialist agents **only when objective checkpoints show expertise or parallelism is needed**. Shrink the team after integration or during bug triage. This is the likely cost-effective hypothesis but must be measured.

### Track E — Provider and hardware independence

Repeat a subset with hosted contemporary models, self-hosted modern open weights, a dated/quantized local model, deterministic tools and human intervention. Use task-family capability gates; older models can do meaningful bounded work without being granted sensitive permissions.

## Standard end-to-end product specification

All experimental cohorts must receive an identical, versioned, bounded product brief, for example a non-sensitive collaborative project board with:
1. public landing + responsive accessible interface;
2. sign-in and role-based access with a tenant boundary;
3. create/read/update/delete projects and tasks in persistent storage;
4. server-side authorization and input validation;
5. task assignment, dependencies and activity log;
6. tests for permissions, persistence, key user flows, error states, mobile accessibility;
7. reproducible local setup, migrations and seed data;
8. build, staging deployment artifact, runtime health checks and rollback plan;
9. observability and a repair process for at least one deliberately injected defect;
10. independent acceptance against hidden adversarial scenarios.

Use synthetic accounts and data only. No real users, production secrets, infrastructure charges or public deployments during research.

## Controlled variables to measure

| Variable | Candidates |
|---|---|
| Team composition | 1 generalist; 3–5 specialists; 8–15 studio; adaptive hybrid |
| Prompt design | one brief vs role-specific instructions vs versioned task/acceptance contract |
| Task scope | vertical slices vs frontend/backend layers vs isolated feature pods |
| Agent memory | clean context, compact handoff manifest, persistent task-specific memory |
| Workspaces | one agent-owned branch per task attempt vs shared branch (shared writes only with enforced lease) |
| Planning | human-fixed task graph vs agent proposed tasks with human/independent validation |
| Integration | early micro-PRs vs delayed feature PRs; queue with exact-merge-result tests |
| Tooling | hosted CLI worker, open-source coding SDK, local model + deterministic runner |
| Review | independent QA, test-only QA, domain expert, adversarial acceptance |
| Cost policy | fixed compute budget, retry caps, model routing and escalation |
| Runtime | local/dev container, isolated hosted sandbox, temporarily disconnected local node |

Never vary all factors simultaneously and interpret the result causally. Pilot with matched tasks and repeat trials; then use a factorial or sequential design to isolate effects.

## Definition of done — not merely "generated full stack"

**Gates and evidence:**

1. Problem/acceptance contract approved by authorized stakeholder.
2. Architecture rationale, component/data boundaries, security/privacy threat review.
3. Implemented UI, API, storage, auth and migration behavior.
4. Deterministic local setup and CI with provenance and appropriate pinned dependencies.
5. Independent test of realistic end-to-end flows, including adversarial tenant/permission scenarios.
6. Integrated exact resulting SHA tested; not just individual agents' source SHAs.
7. Disposable staging artifact/reproducibility and rollback evidence.
8. Human-authorized production release only if separately requested and controlled.
9. Postrelease feedback, defect recovery, operability and maintenance responsibility.

If stage 8 has not occurred, call the result **staging-verified**, not deployed-to-users. If acceptance is only test-based, do not claim verified user benefit.

## Evaluation scorecard

- **Accepted delivery rate**, fraction of experiments independently passing all specified gates.
- **Time to first verified vertical slice** and total time to validated staged product.
- **Human effort:** hours of reviews, clarifications, and repair.
- **Full cost:** inference, CI, hosting, token/runtime overhead, failed retries, context/handoff cost.
- **Integration churn:** merge conflicts, rebases, stale CI, duplicated tasks, orphan branches.
- **Security correctness:** authorization boundary failures, secret leakage, unapproved privileged actions.
- **Maintainability:** complexity, documentation, regression test coverage, independent maintainer repair success.
- **Agent scalability:** extra accepted outputs per additional agent, not number of concurrent tasks.
- **Provider portability:** can the same contract be fulfilled by multiple agent stacks without changing authority semantics?
- **Recovery:** handoff success after one agent crashes or disappears.
- **Actual product quality:** blinded independent test and user walkthrough of defined needs.

## Suggested research phases, not implementation authorization

**FS-0:** literature/benchmark review and candidate tool inventory (OpenHands, agent coding CLIs, code-review tools, workflow engines), with version/license/source links.

**FS-1:** precise product brief, role/permission matrix and security acceptance tests.

**FS-2:** design three cohort workflows and handoff standards; pre-register metrics, ceilings and failure/stop conditions.

**FS-3:** tabletop simulation of competing agents, duplicate work, task drift and stale integration.

**FS-4:** optional founder-authorized disposable comparison: one generalist vs small team vs adaptive team; same budget and product brief.

**FS-5:** optional scaled studio experiment, only if FS-4 independently demonstrates net benefit from adding agents.

**FS-6:** publish reproducible study with caveats, failures, cost, corrections and consented contributor credits. Adapt lessons for Foromni's general convergence protocol.

## Outcome possibilities (do not assume a winner)

- One high-capability generalist plus independent QA may dominate for compact tightly coupled apps.
- A small specialist team may be better for parallel UX/backend/testing with stable interfaces.
- A large studio may win on truly modular complex products—or lose to management overhead.
- Adaptive team size may reduce wasted effort; needs demonstrated trigger rules and fair comparisons.
- Older self-hosted models may contribute strongly to narrow, repeatable tasks while weaker at cross-system design.
- Human architectural judgment and independent acceptance may remain essential.

## Roadmap registration proposal

Foromni's **strategic R&D backlog** should contain an item tentatively called:

**FOR-RD-FULLSTACK-001 — Evidence-backed end-to-end agent/software-studio evaluation**

- Status: **proposed / research only**
- Scope: comparative study of solo, small-team, studio and adaptive worker structures, including provider/self-hosting diversity.
- Dependencies: stable cross-domain Convergence Contract; exact-SHA test-gate model; synthetic concurrency trace; threat/permission and evaluation rubric.
- Acceptance: documented experiment spec, versioned product brief, security and product acceptance criteria, evaluation design, independent reviewer objections, cost/effort metric definitions.
- No claim that a full-stack app is built; no additional roadmap task entered into a canonical mainline registry until approval and reconciliation with existing task identifiers.

**Founder-level question:** How many independent agents can collaborate on a complete working application before coordination and integration overhead exceeds their added value?

*Build today, so others can enjoy tomorrow.*
