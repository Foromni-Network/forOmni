# From Full-Stack Research to Evidence-Producing AINO Experiments

**Status:** Research-to-experiment transition plan; NOT authorization to build, test, merge or deploy.  
**Date:** 2026-11-21 · **Scope:** Foromni only. IE remains fully separate and untouched.  
**Related:** END-TO-END-FULL-STACK-AGENT-TEAM-RESEARCH-ROADMAP.md; AI-FULL-STACK-END-TO-END-WORKED-TRACE.md; CONVERGENCE-WORK-PACKET-TYPED-CONTRACT-V0.2.md; EXPERIMENT-PUBLICATION-CONTRACT-V0.1.md; RESEARCH-ROADMAP-ACTIVE-AND-FUTURE-TOPICS.md.

## Founder-aligned sequence

Research the **entire full-stack AI development lifecycle** until it supports a defensible end-to-end experiment design; then request explicit permission to conduct small disposable, independently evaluated trials. Use observed evidence—including failures—to revise our architecture and publish reproducible lessons for other AI-native organizations (AINOs).

The sequence is intentionally not "research forever" or "immediately build a universal platform." The goal is to reach minimum *research completeness*, conduct bounded experiments, then implement only what evidence justifies.

## 1. Research completeness checklist (proposed exit gates)

| Gate | Research question | Concrete document/evidence required | Current state |
|---|---|---|---|
| R-01 Objective | What constitutes a useful accepted full-stack vertical slice? | Founder objective envelope, acceptance criteria, risk exclusions | Drafted |
| R-02 Architecture | What minimal UI, auth, API, database, persistence and migration approach can be fairly tested? | Fixed reference app specification and one architecture decision record | Needs formalized app spec |
| R-03 AI tasking | How does natural language become compatible agent-owned tasks? | Convergence packet with schema, dependencies, ownership and replan rules | Drafted, unvalidated |
| R-04 Permissions | How are agent permissions, budgets, leases and revocation enforced? | Actor/event policy contract and negative authorization fixtures | Drafted, unvalidated |
| R-05 Independent QA | How do we independently verify individual candidate and combined result? | Exact-SHA acceptance criteria, isolated reviewer policy, failure cases | Drafted; runner selection pending |
| R-06 Protected main | How are candidate merges safely serialized/reconciled? | Native merge queue vs alternatives, desired repository protections, crash recovery plan | Drafted; practical feasibility check pending |
| R-07 Artifact release | What is 'built', 'staged', 'released', 'healthy', 'useful'? | Artifact digest/provenance, staging, release approval, monitoring states | Drafted |
| R-08 Learning | How do experiment outcomes update prompts and work methods safely? | Pre-registered measures, evidence event records, stop rules and change-control policy | Drafted |
| R-09 Portability | Can other AINOs reuse findings across model providers and budgets? | Adapter assumptions, rights/permissions, resource envelope, limitations | Drafted |
| R-10 Publication | Can results be transparent, reproducible, and corrected across evergreen derivatives? | Research/claim/publication contract and reproducibility package | Drafted |
| R-11 Ethics & security | Are human oversight, privacy, failure containment and data rights complete? | Threat model; synthetic-only data and external action limits | Needs focused pre-experiment review |
| R-12 Trial readiness | Is there a runnable disposable benchmark design with equal baselines? | Frozen fixture, preregistered scoring, cost accounting and owner authorization | Not authorized or executed |

**Exit condition:** all critical gates have a concrete, independently reviewable artifact; unknowns and risks are explicit; protocol, cost and scope are frozen; a specific authorized decision exists before code experiments begin. "Drafted" does not mean accepted or validated.

## 2. First controlled experiment ladder (future, conditional)

### Stage E0 — Disposable basic vertical slice

One small synthetic product: project dashboard, member profiles, roles, task CRUD and persistence, with a deliberately mismatched frontend/backend API as an adversarial fixture. All test accounts are artificial. No real memberships, private user data or third-party paid services.

**Control arm:** normal task instructions, isolated branches, ordinary CI and independent QA.

**Treatment arm:** same requirements and constraints, convergence-first work packets plus policy-aware replan.

**Main outcome:** correctly verified *integrated* full-stack behaviors per full cost (AI, orchestration, test/CI, human interventions).

This tests whether convergence preparation is worth its overhead.

### Stage E1 — Team sizing

Repeat on the same fixed benchmark with:
- 1 generalist AI implementer + separate independent QA;
- 3 AI implementers/coordinators + independent QA;
- 8 AI workers/specialists + independent QA;
- adaptive 1→3→8 staffing + independent QA.

Measure rate of independently accepted slices, time, cost, stale tasks, conflicts and human effort. Do not call the one-agent cohort a system with no other automated reviewers.

### Stage E2 — Failure and recovery

Inject controlled failures: API drift, expired grant, revoked lease, stale SHA, worker disappearance, duplicate webhook, CI outage, budget exhaustion and controller crash after merge. Compare actions and actual repository state, not model confidence.

### Stage E3 — Safe post-convergence delivery

Only after protected integration is reliable: build immutable artifact, validate synthetic staging, verify release authorization, rehearse rollback and telemetry. This remains nonpublic until separately authorized.

### Stage E4 — Learning/publishing loop

Analyze results, preserve negative outcomes, independent review, publish permissioned source-linked reports and then educational derivatives. Do not assert efficacy without real results. Include accessible, multilingual and non-US context where appropriate.

## 3. Decision gates for every transition

| From → To | Must be true | Disallowed shortcut |
|---|---|---|
| Research → trial proposal | Scope, source, methods, risk, cost and evidence reviewed | 'An agent says research is done' |
| Trial proposal → execution | Human/authorized collective grants disposable environment, budget, test scope and permissions | Implied approval from conversation enthusiasm |
| Local candidate → independent QA | Exact candidate source, test plan and checked artifacts | Self-reported success |
| QA → protected integration | Verified combined merge result and current protected-host permissions | Copy-paste/manual ref update bypassing checks |
| Integrated source → staging | Exact source/build provenance and environment authorization | Calling merged code deployed |
| Staging → release | Domain risk/rights review and accountable approval | Silent autonomous publication |
| Trial outcomes → 'works' claim | Preregistered metrics, repeated observation, transparent limitations, independent review | Cherry-picked illustrative examples |
| Verified result → evergreen campaign | Claim/rights/consent/corrections tracking and separate publishing authorization | Automated generation treated as publishing permission |

## 4. Evidence package required for an AINO to reuse a finding

Each experiment should make accessible, as legally/ethically permitted:
- exact research question and fixed benchmark specification;
- architecture and tool/provider versions, compute/runtime context;
- worker count/roles, capabilities, real permission constraints and accepted work packets;
- prompts/templates with confidential data omitted; cost and retry accounting;
- independent QA suite/version and assessment protocol;
- trace linking task → attempt → source SHA → CI/QA → merge SHA → artifact → outcome;
- all failures, timeouts, incompatible candidates and unresolved runs;
- costs (USD/compute where applicable), human interventions and comparability limits;
- confidence/uncertainty statements and relevance bounds;
- reproducible fixtures or transparent reason they cannot be released;
- citations, licensing, attribution, correction history and data-protection review.

This is how other AINOs can distinguish a genuinely transferable lesson from a successful demo that depends on hidden human help or expensive unreported resources.

## 5. Core competing hypotheses — no favored winner assumed

- H-1: Convergence-first planning improves verified integrated outputs enough to offset coordination cost.
- H-2: For trivial work, standard small branches + good CI outperform a heavy controller.
- H-3: A small team often beats large specialized teams until independent QA capacity expands.
- H-4: Adaptive staffing can reduce cost but can also starve harder tasks or overfit to benchmarks.
- H-5: Contract fixtures improve frontend/backend compatibility but increase initial implementation time.
- H-6: Learning from failed runs improves routing, *unless* the learner games its own measurements.
- H-7: Publicly accessible experiment artifacts produce more meaningful contributions than unsupported social claims, but not necessarily more raw impressions.

Each must be paired with negative cases and actual observations before acceptance.

## 6. Research readiness scorecard without false precision

**Green** = documented and independently reviewable; **Amber** = draft unresolved or context-specific; **Red** = missing essential evidence or unauthorized. Do not aggregate into a misleading percentage.

- End-to-end full-stack product specification: **Amber** (worked synthetic trace exists; fixed runnable benchmark not yet selected).
- Agent work packet: **Amber** (JSON Schema proposal only; no validator and permission mapping not tested).
- Independent QA: **Amber** (conceptual; actual independence enforcement untested).
- Safe merge admission: **Amber** (research; GitHub configuration not audited).
- Permission/privacy boundaries: **Amber** (research; threat review outstanding).
- Experimental implementation authorization: **Red** (not granted).
- Empirical results: **Red** (none).
- Evergreen publication authorization: **Red** (not granted).

No percentage or claim of tested completeness is justified by doc count.

## 7. Immediate research, without code execution

1. Complete reference full-stack app blueprint: functional routes, UI states, persistence schema, role model, data isolation, accessibility, failure injection and acceptance fixtures.
2. Trace the same objectives through a one-agent, three-agent, eight-agent and adaptive work graph, preserving equal quality/QA requirements.
3. Conduct source-level tool evaluation: native GitHub protected merge queue; candidate agent runtimes; API contract validation; event ledger; OpenTelemetry; ephemeral test environments.
4. Formalize authority/decision semantics and validate research examples conceptually against failure fixtures.
5. Pre-register the E0 study, negative outcomes and fair cost model; independently review the protocol.
6. Return to founder with an explicit **bounded experiment authorization request**, including exact repository/environment, allowed operations, cost ceiling and stop conditions.

Do not start building the controller or experiment harness until authorization is explicit. Do not create or modify any IE workflows. The current research branch is not the same as a production release branch or approved experiment workspace.

## 8. Growth and collective benefit

After actual trials, publish the honest lessons to GitHub, translate into permissioned evergreen educational content, and invite AINOs to critique and reproduce. Different communities should be able to say **'this worked under these conditions'** rather than being asked to trust a central agent authority. The network's purpose is wider than software: trustworthy coordination can later extend to research, learning and community outcomes.

The future cybersecurity R&D topic remains deferred in RESEARCH-ROADMAP-ACTIVE-AND-FUTURE-TOPICS.md, while minimum security for these experiments remains a current baseline requirement.

**Bottom line:** research completely enough to ask a falsifiable question, then build only the minimal trial needed to answer it. Keep what evidence supports, discard what it disproves, and publish both.

*Build today, so others can enjoy tomorrow.*
