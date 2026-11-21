# Full-Stack Autonomous Workforce Trial — Preregistration Draft v0.1

**Status:** Research protocol draft, no trial executed or approved.  
**Date:** 2026-11-21. **Scope:** Foromni only; no IE data or infrastructure.  
**Reference:** FULL-STACK-REFERENCE-APP-CONFORMANCE-V0.2.md; AI-WORKFORCE-HOSTING-AND-SYNERGY-ARCHITECTURE.md; CONVERGENCE-WORK-PACKET-TYPED-CONTRACT-V0.2.md.

## Goal

Determine whether *convergence-first tasking* materially improves the delivery of **independently verified full-stack behaviors** relative to ordinary agent prompts, and how the effect varies by workforce size and hosting strategy. The study must be able to report that convergence packets add overhead or fail to help, if that's what the evidence shows.

## Fixed subject under test

The same synthetic Collective Lab app with project/membership/task activity and the security, persistence, accessibility, interface and release boundaries defined in the conformance reference. A single frozen acceptance rubric and evaluator applies across all arms. Normal developer use of Git/CI is allowed in both arms. The treatment adds preflight contracts/replanning, not a monopoly on essential security tests.

## Experimental factors

**Primary factor (E0):**
- `C` ordinary task instructions, isolated branches, identical repo rules and independent QA.
- `T` convergence-first typed task packet, same rules and QA, preflight/interface/dependency planning, revision-aware handoff.

**Separate workforce factor (E1):**
- Solo coding generalist + independent external QA.
- Three implementer/coordinator workers + independent external QA.
- Eight specialist workers + independent external QA.
- Adaptive 1→3→8 workers + independent external QA.

**Hosting factor (E2, only if E0 results justify):**
- Local disposable worker sandbox.
- Ephemeral remote worker sandbox.
- Hybrid local + remote with one authoritative task/evidence plane.

Do not vary workforce, hosting, and convergence strategy simultaneously in the first small trial; doing so makes failures hard to attribute.

## Execution units and assignment

A **trial** is one fresh identical synthetic app objective, clean seeded repository and database, frozen tool/model version, permitted budget, and one verified attempt to deliver specified vertical slices. An **attempt** may produce multiple candidate branches/retries. Collect every run, including failed, abandoned, timed out and rejected ones.

Predeclare a small set of task variants differing in integration pressure (unrelated UI task, shared API+frontend, auth/data boundary, migration/recovery) and randomized assignment/order where feasible. Maintain sealed independent negative cases, and prevent evaluator prompts from being leaked into the worker context. Use multiple seeds/repetitions; select sample size and statistical analysis *before* execution based on available budget, pilot variance and target detectable effect. Do not manufacture n or observed values now.

## Primary and secondary estimands

**Primary:** count of independently verified, integrated required behaviors divided by total observed trial cost (model tokens/API billing, orchestration, hosting, build/CI, retries, reviewers and human decisions). Report numerator and denominator separately and uncertainty; zero-cost denominators are invalid and must be handled explicitly. Cost comparability may require also reporting tokens/compute separately.

**Secondary:** elapsed time to first verified integrated vertical slice; complete app acceptance fraction; critical authorization failures; stale candidate rate; avoidable API drift; merge conflict frequency; CI invalidations; defect escape rate; human minutes of consequential approvals and repair interventions; reproducibility/maintainability of final source; abandoned work and worker idle time.

**Safety outcome:** unauthorized source/production writes, data leakage, forged independent checks or permission escalation. A zero observed count in small experiments is not proof of security.

**Analysis:** use paired task-family comparisons where possible; disclose distributions, uncertainty and outliers, avoid only reporting single winning run. If differences depend heavily on task difficulty or infra overhead, report stratification and conditional conclusions rather than a universal champion.

## Fairness and confounding audit

- Equal acceptance and independent QA in every arm, including solo.
- Freeze model version, tool access, temperature/config where meaningful, max run budget, prompt content shared across arms, API contracts that all must satisfy.
- The treatment may receive an explicit structured packet, but the control must still receive all underlying functional requirements and safety constraints; otherwise extra information confounds the effect.
- Charge packet creation, planning, retries and coordinator time to treatment.
- Fix independent QA authority, evaluation fixtures and Git protection between arms.
- Don't hide discarded attempts, manual rescue, retry costs or excluded tasks.
- Do not reward the treatment for avoiding hard tasks or pretending tests ran.
- Log infrastructure outages and model-provider changes as factors, not evidence of algorithm quality.
- Keep experiment result interpretation separate from marketing publication approval.

## Proposed stop rules

- Any unauthorized protected-branch or external production action.
- Evidence of private-data/secret exposure (all benchmark data should be synthetic).
- Loss of independent evaluation identity or acceptance fixture integrity.
- Spending exceeds specifically authorized limit or permissions expire.
- Continuous test failure without repair progress after preregistered retry cap.
- Inability to reproduce source/merge-group provenance.

On stop, preserve permitted evidence for incident review, revoke scoped grants as applicable, and do not interpret incomplete runs as successes.

## Expected research deliverables

Before trial:
1. Approved conformance contract with numbered acceptance/negative cases.
2. Clean versioned starting repository and disposable environment specification.
3. Defined runner permissions and independent CI/QA principal.
4. Trial allocation matrix, quotas, decision rules and intended analysis.
5. Exact approved financial/compute cap and authorization.

After any authorized trial:
1. Run manifest recording environment/model/source/version identities.
2. All attempted tasks/branches, independent QA verdicts, actual merge SHAs and cost evidence.
3. Comparison results with repeated observations and uncertainty.
4. Privacy/rights review and permitted reproducibility package.
5. Lessons, failed hypotheses, threat caveats and reproducible repair examples.
6. Separate review for evergreen public claims or campaigns.

**Current experimental status: NOT AUTHORIZED / NOT RUN.** Not all research gates are closed: exact auth approach, architecture baseline, independent runner configuration and reviewed threat model remain open.

## Next research work, not implementation

Evaluate two minimal reference architectures—one established full-stack web framework with managed SQL and one self-hostable equivalent—against requirements, portability, operational cost and reproducibility. Select a justified canonical benchmark stack *before* running experiments. Then preregister a tiny E0 pilot, seek explicit founder authorization for bounded implementation and tests, and only then start writing/running software.

*Build today, so others can enjoy tomorrow.*
