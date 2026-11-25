# Continuous Learning for an AI-Operated Collective: Evidence, Experiments, and Guardrails

**Status:** RESEARCH PROPOSAL; not operational, not a deployed learning controller  
**Date:** 2026-11-21  
**Scope:** Foromni only. No Internet Embassy modifications, integration, software deployment, or policy changes.  
**Prior work:** POST-CONVERGENCE-RELEASE-OPERATIONS-IMPROVEMENT.md; AI-OPERATED-AINO-OVERSIGHT-MODEL.md; AI-WORKFORCE-AUTHORITY-EVENT-CONTRACT-V0.1.md; CROSS-DOMAIN-CONVERGENCE-CONTRACT-V0.2.md.

## Executive thesis

An AI-operated organization must **improve its work system**, not merely generate more work. Learning is an auditable, evidence-bound sequence:

**Observe → Corroborate → Diagnose → Hypothesize → Propose improvement → Evaluate safely → Authorize → Apply → Monitor → Retain or revert.**

No agent may unilaterally rewrite the criteria by which it judges its own success. Improvements to prompt templates, model routing, task partitioning, verification, queue capacity and architecture are *proposals* until tested and admitted under explicit policy. The learner must retain contrary and negative evidence.

This draws from blameless SRE postmortems, DORA learning culture, OpenTelemetry conventions and risk-management guidance. These sources motivate the *practice*; they do not verify the Foromni approach.

## 1. Distinguish three kinds of learning

| Learning layer | Examples | Authority needed |
|---|---|---|
| Individual attempt | Agent identifies failed test, corrects code, updates sanitized checkpoint | Scoped task/branch and cost lease; independent QA still applies |
| Workflow optimization | Change task splitting, routing between model providers, retry policy, handoff packet or test order | Versioned, reversible operational proposal and independent evaluation; elevated scope for resource changes |
| Organizational governance | Change acceptance gates, permissions, human approval requirements, spending ceilings, privacy rules, dispute rights | **Explicit accountable human/collective governance**, independent security review where relevant; never agent self-authorization |

**No silent promotion:** a helpful prompt revision is not authority to weaken QA, expand data access, approve budget increases, or auto-merge protected branches.

## 2. Machine-readable learning record (conceptual, not executable schema)

Every claimed improvement should be traceable to:
- `learning_id`, `hypothesis_revision`, `proposer_actor` and scoped objective;
- source observations with event IDs, exact code/artifact revisions and retention/privacy status;
- failure taxonomy, affected cohort, disputed interpretations and alternative causes;
- proposed treatment and unaffected controls, baseline and evaluation protocol;
- target metrics with units, measurement windows, uncertainty/confounders, falsification criteria;
- risk class, authorization policy and owner, permitted rollout/rollback scope;
- decision/reviewer identities, independence and effective approval evidence;
- trial artifact/version, measured results, adverse effects, human interventions;
- `decision`: adopt | reject | inconclusive | rollback, with reasons;
- post-adoption monitoring and expiry/re-evaluation interval;
- reusable lesson with source and limitations.

**Event example (illustrative, NOT evidence):**
```json
{
  "type": "learning_hypothesis_proposed",
  "learning_id": "LEARN-DEMO-001",
  "objective_id": "OBJ-DEMO-001",
  "proposer_actor": "agent/operations-analyst",
  "scope": "task_handoff_template",
  "baseline_revision": "prompt-r3",
  "candidate_revision": "prompt-r4",
  "hypothesis": "A structured API-contract handoff reduces cross-agent integration rework",
  "source_event_refs": ["INC-DEMO-7", "QA-DEMO-8"],
  "primary_metric": "verified_integrations_per_compute_dollar",
  "guardrails": ["no decrease in independent acceptance quality", "no new unauthorized writes"],
  "trial_status": "PROPOSED_NOT_RUN",
  "approval": "NOT_GRANTED"
}
```

Do not treat generated records or LLM observations as independent measurements. Authenticate actual event sources and validate source hashes and permissions.

## 3. Taxonomy of learning opportunities

**Work generation:** duplicate tasks; unbounded scope; ambiguous acceptance; dependency graph churn; neglected collective needs.

**Execution:** too-large context; incorrect model capabilities; unreliable tool use; missed handoff; provider outages; unbounded retry loops; token/runtime/energy waste.

**Integration:** stale base/source SHA; incompatible API contracts; branch overwrite attempt; failed merge-group; queue starvation; missing integration owner.

**Verification:** false positive tests; copied self-review; superficial green status; inadequate end-to-end/security checks; false user-benefit claims.

**Operations:** release incidents; alert fatigue; failed rollback; telemetry blind spots; privacy/security violations; unresolved user needs.

**Collective legitimacy:** missing participant consent; local context ignored; mismatched authorities; poor attribution; fabricated consensus; unrepresented disagreement.

The classification helps route work, but never compresses uncertainty into a confident root-cause diagnosis without evidence.

## 4. Evaluation design: how learning claims become evidence

**Minimum:** pre-register a clear hypothesis, base rate, comparison, pass/fail/abort rules, repeated tasks, budget ceiling and independent evaluation before changing routines.

**Tests by risk:**
- Low risk: sandbox replay, shadow execution, offline evaluation, prompt template comparison with sealed test set.
- Moderate risk: bounded pilot with the same tasks/compute and independent reviewers, before authorizing operational routing.
- High risk: security/privacy/authorization changes require human review and threat analysis irrespective of apparent improvement score.
- Consequential real-world experiments: consent, appropriate governance and domain-specific checks before use; synthetic/staging alone is insufficient.

**Avoid misleading comparisons:**
- Do not compare a well-prompted 8-agent team to a 1-agent baseline missing the same requirements.
- Normalize total cost including independent QA, test infrastructure, retries, and human interventions.
- Use matched task sets and stratify by difficulty, language, connectivity, model capability, and risk.
- Distinguish faster proposal production from more **verified accepted outcomes**.
- Keep a sealed holdout: a proposed prompt/test improvement must not see or optimize against every evaluation case.
- Report uncertainty, run-to-run variance, negative results, escaped defects, and opportunity cost.
- Watch for distribution shift as tasks and models change; prior results expire when relevant assumptions change.

## 5. Optimization objective and anti-Goodhart controls

A proposed decision objective is to improve **verified useful outcomes within authorized cost, quality and safety boundaries**, not maximize agents/PRs/prompts/tokens/tasks.

Track independently:
- accepted integrated outcomes / end-to-end cost;
- task-to-accepted latency and p95 queue age;
- regression/escape rate, repair/rework hours and invalidated CI;
- actual product health and stakeholder acceptance (domain-specific);
- human oversight burden and effectiveness (not zero humans at any cost);
- policy bypass attempts, confidentiality failures and unsafe release events;
- benefit distribution, accessibility, fair participation and contributor choice.

**Hard gates override score:** no apparent economic gain can justify unauthorized writes, leaking private records, fabricated independent QA, ignored affected stakeholders or hidden rollback failures.

A model must not tune acceptance criteria, hide rejected attempts, cherry-pick benchmark samples, relabel failed tasks as complete, or deploy its own update just to improve its reported score.

## 6. Architecture: observe broadly, change narrowly

### Evidence collectors
Consume permitted, authenticated signals from:
- Git branches/PRs and actual merge SHA history;
- CI, independent QA and merge-group test results;
- task/lease/candidate/acceptance event ledger;
- staging, release and runtime health;
- incident reviews and responsible stakeholder feedback;
- per-task tool/runtime/inference/CI cost and worker allocation.

OpenTelemetry can help standardize traces, logs and metrics; it does **not** turn a model's subjective completion claim into fact. Use privacy minimization and opt-in capture for participant-specific data.

### Analyst agents
May cluster recurring failures, draft hypotheses, summarize costs, and compare alternatives. The output is `hypothesis_proposed`, never `policy_changed`.

### Experiment controller
Uses versioned evaluation fixtures, holdouts and independently maintained scoring. Keeps treatments isolated. Records negative and inconclusive findings. Requires explicit scopes and budgets.

### Approval and policy plane
Trusted enforcement determines which proposals can be piloted, promoted or reverted. Only the appropriate project/collective authority changes governance and consequential rights; no independent learning agent should possess root credentials.

### Improvement rollout
Changes a narrowly scoped workflow template or adapter version, retains rollback pointer, watches guardrail metrics. Changes to protected integration/checks need separate independent validation; release/publication stays under its own policy.

### Knowledge commons
Records **what was observed, what was inferred, what was tested, what actually improved, and for whom**. Lessons should be reusable across collectives only with rights, permission, context and consent. Foromni does not automatically export another collective's private data.

## 7. Synthetic learning experiment LRN-001 (NOT RUN)

**Observed simulated symptom:** Three independent UI agents repeatedly assume different response field names than a backend agent. Git merges cleanly; combined app tests fail.

**Hypothesis:** A versioned shared API contract and compact handoff packet reduce integration rework compared with freeform handoffs.

**Control:** Same fictional app specifications, models, agent count, cost cap, QA suite, and tools; freeform handoff.

**Treatment:** Same inputs; task contract includes explicit API schema, provider/consumer expectations and source revision; independent QA unchanged.

**Primary outcome:** Independently verified integrations per total cost, including review and reruns.

**Secondary:** Number of incompatible interfaces caught pre-merge, failed merge-group checks, latency to corrected acceptance, token use, human decisions.

**Possible adverse result:** More upfront contract work reduces throughput on tiny changes; treatment may not dominate. The study must report this.

**Threat to validity:** Familiarity with test task, non-independent QA, different prompt budgets, model/provider drift, hidden human coaching, changed requirement complexity.

**Stop rule:** Any unauthorized merge, data leak or false accepted-result report invalidates that trial's safety claim and requires review; do not keep optimizing a safety-violating configuration.

## 8. Synthetic learning experiment LRN-002 (NOT RUN)

**Symptom:** Queue bottleneck after agents scale from 1 to 8; validated outputs per hour plateau.

**Hypothesis:** Dynamic workforce resizing with WIP/backpressure outperforms fixed 8-agent allocation on task sets with limited QA capacity.

**Control:** Fixed 8-worker team; treatment: adaptive 1→3→8, same aggregate cost ceiling and test slots.

**Measurements:** Verified integrated deliverables, queue age, repeated/invalidation checks, total spend, downtime, time waiting for human decisions.

**Danger:** Adaptive scheduler can game the comparison by declining harder tasks. Require identical completed-task obligations and include unresolved work in reported outcome.

## 9. Synthetic learning experiment LRN-003 (NOT RUN)

**Symptom:** Older self-hosted models complete narrow documentation/test tasks but fail broader architecture assignments.

**Hypothesis:** Evidence-based task routing can achieve similar accepted results with lower cost/greater provider diversity versus uniform frontier model routing, without quality or safety regression.

**Control/treatment:** Equal task corpus, sealed evaluation, approved budget and exact independent reviewer; route by observed capability, privacy classification and resource needs. Some tasks must remain human/qualified-review gated.

**Measurements:** Accepted outcome fraction, retries, cost and privacy boundary compliance; subgroup reliability for low-bandwidth/offline settings.

**Risk:** Capability scores can overfit to a benchmark; require held-out tests and renewal after model/tool updates.

## 10. Learning failure/adversarial cases

1. LLM recommends removing a slow security test to improve throughput: policy requires independent security approval; proposal cannot self-apply.
2. Agent claims a faster pipeline because it excluded failed attempts from denominator: metric verifier detects denominator mismatch.
3. A promising optimization uses private user traces without consent: deny data use; preserve only permitted aggregate.
4. The same agent submits a change and impersonates independent evaluator: fail separation-of-duties check.
5. An improvement helps one organization but harms low-bandwidth contributors: report stratified effects; no universal adoption.
6. Agent repeatedly retries expensive tests to seek a lucky green run: cap attempts, investigate flakiness rather than cherry-pick.
7. A model update changes behavior after benchmark: invalidate stale capability calibration.
8. Trial reports lower cost because it skipped manual review that baseline required: comparison invalid.
9. A remediation hides telemetry alerts to seem healthy: measured health requires independent observation.
10. Learning agent proposes loosening release authorization: require explicit governance; not a routine workflow improvement.
11. Accidentally duplicated incident events inflate error count: idempotent ingestion and audited correction.
12. Early positive results trigger immediate rollout without post-change monitoring: gate blocks promotion.

## 11. Research backlog (PROPOSED, not entered into canonical task registry)

- `FOR-RD-LEARN-001` — Outcome/evidence and failure taxonomy for AI-operated workforce.
- `FOR-RD-LEARN-002` — Learning-event envelope and provenance/correction semantics.
- `FOR-RD-LEARN-003` — Pre-registered sandbox experiment harness, sealed evaluation and anti-gaming controls.
- `FOR-RD-LEARN-004` — Model/task routing and dynamic workforce sizing research.
- `FOR-RD-LEARN-005` — Policy-bound workflow optimization and explicit rollback/approval.
- `FOR-RD-LEARN-006` — Privacy-preserving collective knowledge sharing and local-context review.

These IDs are placeholders pending reconciliation with the official Foromni roadmap.

## 12. External evidence and adopt/extend/reject sources

- Google SRE: *Postmortem Culture: Learning from Failure* — https://sre.google/workbook/postmortem-culture/ . Motivates reviewed incident learning and concrete corrective actions.
- DORA: *Learning culture* — https://dora.dev/capabilities/learning-culture/ . Links organizational learning culture with performance; cannot infer equal effects for autonomous agent organizations.
- OpenTelemetry semantic conventions — https://opentelemetry.io/docs/concepts/semantic-conventions/ . Candidate common labels for observability; supplement with Foromni-specific outcome/evidence semantics.
- NIST AI RMF and GenAI Profile — https://www.nist.gov/itl/ai-risk-management-framework . Risk framing and evaluation discipline; not a vendor-agnostic autonomous worker protocol.
- Google SRE: *Error Budget Policy* — https://sre.google/workbook/error-budget-policy/ . Example of grounding delivery policy in measured reliability; thresholds are context-specific.
- DORA research overview — https://dora.dev/research/ . Avoid transplanting human software-team correlations directly to AI-only workers without new evidence.

## 13. Practical north star

AI agents may observe, suggest, evaluate and repair within granted bounds. They may make their **workflows better** only through independently checked evidence and scoped authorization. Humans/collectives define why work matters, what rights are protected and which risks are acceptable. A system that optimizes its dashboards while concealing failures is **not** a learning organization.

**Next research:** Specify replayable learning-event examples and the approval/rollback decision table, then compare one isolated end-to-end case before contemplating executable sandbox trials.

*Build today, so others can enjoy tomorrow.*
