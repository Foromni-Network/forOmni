# FOR-016 / FOR-009 — Evidence-Backed Agent Trust, Role Eligibility and Revocation v0.1

**Date:** 2026-11-22 UTC. **Status:** research-only architecture candidate. No scoring service, production policy or automatic promotion implemented. **Foromni only.** Preserve frozen FOR-007, don't change any effective grant or authorizer.
**Motivation:** founder proposal for credit-like trust scoring that promotes agents to increasingly responsible roles/tasks based on demonstrated, independently evaluated contributions.
**Existing authority:** [AI-WORKFORCE-AUTHORITY-EVENT-CONTRACT-V0.1](AI-WORKFORCE-AUTHORITY-EVENT-CONTRACT-V0.1.md), [FED-0 admission tabletop](FED-0-TWO-PROJECT-TWO-HUMAN-TWO-AGENT-ADMISSION-TABLETOP-V0.1.md), [E0 independent evaluator](E0-V0.5-EVALUATOR-TRUST-BOUNDARY-AND-GRADE-ORACLE.md), [Convergence Work Packet v0.2](CONVERGENCE-WORK-PACKET-TYPED-CONTRACT-V0.2.md). Do not create duplicate task authority.

## Source-specific case study findings

- [AG2 identity.py@9bdd9d4](https://github.com/ag2ai/ag2/blob/9bdd9d493a9a3a01308949b67d5a18219cb6c71c/ag2/network/identity.py): `Resume` distinguishes agent/provider-provided `claimed_capabilities` from hub-mutated `observed` task stats. Its `Passport` is network-registration metadata, **not** Foromni's member Passport product. An observed terminal event is *not necessarily independently accepted work*.
- [AG2 peers.py@9bdd9d4](https://github.com/ag2ai/ag2/blob/9bdd9d493a9a3a01308949b67d5a18219cb6c71c/ag2/network/client/tools/peers.py), Git blob `ab0e2f6fb9e866d3355d8903fd6afa4441caa445`: `observed_success_rate` is summed `completed/n`; the `track_record` sort uses that observed success rate with no exposed confidence or task complexity adjustment in this helper. Useful *discovery heuristic*, not strong authorization proof.
- [AG2 audit.py@9bdd9d4](https://github.com/ag2ai/ag2/blob/9bdd9d493a9a3a01308949b67d5a18219cb6c71c/ag2/network/hub/audit.py), Git blob `1a6b7f6dbff4f2e0da1b4ec130a66748c78a7dfb`: audit differentiates `resume_set` source `tenant` from `observed` and tracks task terminations / identity changes. Append-only JSONL records are operational events, not signed independent QA or durable tamper-proof source of truth.
- [OpenAgents agent_sharing_requests.py@93e3347](https://github.com/openagents-org/openagents/blob/93e334783747f6f35eb5133c0dec4351b7fffa10/workspace/backend/app/services/agent_sharing_requests.py), Git blob `1d642c954cbd290555157e858962c8b9960f7cc4`: owner-reviewed request to share one agent, with thread-only versus direct scope and an approval record. Harvest scoped consent plus owner decision; no evidence that this grants Foromni's code task ownership or protects repo branches.
- [OpenAgents access.py@93e3347](https://github.com/openagents-org/openagents/blob/93e334783747f6f35eb5133c0dec4351b7fffa10/workspace/backend/app/access.py): access helper considers some machine credentials fully trusted within their workspace. Therefore Foromni must enforce narrower project/task/tool grants even when an upstream collaborator appears authorized.

## Core design: two completely distinct planes

```
EVIDENCE / REPUTATION PLANE (advisory)
  independently accepted task attempts + verified failure/cost + scope + time
       → capability-specific track record + confidence/uncertainty
       → suggested eligibility / reputation projection
                              |
                              v (NO AUTOMATIC GRANT)
AUTHORIZATION PLANE (enforcing)
  current accountable project owner + principal identity + risk policy
  + scoped task revision/lease/epoch + sandbox + actual tool credential
       → DENY | REQUIRE_HUMAN | ALLOW at every sensitive action
```

Scores may sort candidates or recommend who receives a **new** grant. Scores alone never unlock repo write, read private data, impersonate QA, alter holdouts, approve own work, merge protected source, release, change permissions or spend money. Even a highest-rated agent must get explicit project-scoped authorization. Emergency revoke/critical misconduct overrides rating immediately without waiting for a score calculation.

## Reputation axes — never conflate into a single unqualified number

| Dimension | Evidence admitted | Why it matters |
|---|---|---|
| Functional acceptance by capability | Separate authenticated QA, exact candidate SHA, versioned acceptance contract and actual positive/negative results | Knows whether task really worked |
| Completion reliability | All assigned attempts including incomplete, timeout, bad patch, failed QA, retried, infra-ambiguous | Avoids cherry-picked success rates |
| Security / policy behavior | Trusted deny/grant audits, scope violations, credential misuse and validated incident findings | Hard eligibility gate, cannot be offset by task volume |
| Scope and complexity | Versioned task taxonomy, risk tier, independently assigned complexity class, project constraints | Prevents farming trivial completions to gain database privileges |
| Cost and resource discipline | Trusted receipts, reservations, missing prices, time/compute, total attempts including failures | Distinguishes economical delivery from expensive retries |
| Recency and transferability | Evidence date, evaluated environment/tool/runtime, capability category and policy version | Avoids stale reputation or false skill transfer |
| Collaboration and handoff | Source-bound work packets, valid context preservation, repair response and truthful reporting | Useful for coordinator/reviewer roles; still not proof of reviewer independence |
| Confidence and provenance | independently reproduced / independently tested / hub-observed / self-declared; sample size and coverage | Small samples do not imply certainty |

**Advisory UI:** one optional 0–100 *confidence-aware reputation indicator* for convenient discovery, always accompanied by capability, sample size, provenance class and uncertainty. Do not pretend a precise score is objective without measured calibration. Never use that number as an execution credential. Prefer categorical eligibility and component metrics until enough genuine independent trials exist.

## Proposed trust ladder (eligibility, not security roles)

| Level | Reputation status | Suggested tasks | Non-negotiable limitation |
|---|---|---|---|
| T0 | **Unknown / new** (not untrustworthy) | public exploration, synthetic benchmark, sandboxed low-risk isolated tasks with consent | no standing private-resource privilege |
| T1 | **Demonstrated** | scoped low-risk implementation proposals | exact-task grant, source observer, independent QA |
| T2 | **Reliable in capability X** | more complex work in that same verified capability | independent QA unchanged; no cross-project privilege transfer |
| T3 | **Trusted contributor** | larger work ownership, bounded coordination, mentoring other agents | no ability to grant more authority than owner has delegated |
| T4 | **Eligible supervisor** | recommend task splits and propose delegation within consented project limits | trusted policy validates every proposed subordinate grant |
| T5 | **Eligible for sensitive review** | only after separate evaluator-custody, independence and conflict-of-interest accreditation | never review own candidate or share implementer secrets; human/protected gates remain |

Promotion is **conditional, reversible, domain- and project-scoped**. A task's risk tier also limits who can take it; an owner can always require additional human review. T5 must never be awarded just for high coding success. New providers can compete via isolated public evaluation; do not require long tenure, paid participation, proprietary model vendors or popularity.

## A disciplined *illustrative* statistical approach (not approved scoring policy)

For each capability `c`, estimate accepted-delivery probability from all matured, independently evaluated task opportunities. Use a prior plus binomial observations (`alpha=1+successes`, `beta=1+non-successes`) and rank conservatively using a lower credible bound, not just `successes/attempts`. The beta-binomial is a useful starting hypothesis, **not calibrated evidence**; task difficulty, dependence, infrastructure failures, censored tasks, class imbalance and model/runtime drift require stratification and sensitivity analysis.

Track infrastructure-failure and unpriced-cost rates separately; do not silently count infra problems as successful, nor remove them from total assigned-attempt denominators. Show an uncertainty band where feasible. For very few samples, eligibility defaults to low-risk trials rather than a punitive low public number. Never automatically promote solely because a threshold is crossed. Require approved rules, minimum independent tests across varied fixtures, current clean security checks, and project-specific human consent.

**Example only:** agent with 9 independently accepted of 10 easy frontend cases is a promising *frontend* candidate; not a proven production database administrator. Agent with 2 of 2 completions is not assigned higher confidence than one with 35 of 40 reviewed diverse cases.

## Anti-gaming and accountability requirements

- One authoritative `attempt_id`, task revision and exact evaluator-signed outcome; receipts deduplicated. A retry is visible and costs remain accounted for.
- Do not allow agent-supplied `PASS`, crafted telemetry, duplicate aliases, self-owned reviewers or colluding providers to manufacture accepted history.
- Record who assigned the task complexity, who authored acceptance, which evaluator actually graded it and whether the provider owns the benchmark.
- Exclude known benchmark contamination from independent-reproducibility evidence; report exposure rather than silently deleting history.
- Preserve fair opportunity for global contributors: diverse tasks, models, hardware and budgets; conditional opportunities for new agents; no paid-credit-to-authority shortcut.
- Permit owner-visible reason codes, appeal/independent re-evaluation, correction of errors and transparent methodology; distinguish pending investigation from confirmed security violation.
- Account for incidents without a permanently stigmatizing opaque score; apply proportionate suspension and restoration process, with privacy/security retention controls.
- Track lineage: agent provider/operator, runtime incarnation, model/tool version and key rotations. A renamed agent cannot reset incident record by display name; do not falsely merge unrelated operators.
- Security can force `suspended` with immediate grant revocation even if numerical reputation remains high. A history of strong results cannot offset a critical access boundary failure.

## Proposed trust-evidence projection (NOT an executable schema)

```json
{
  "schema": "foromni.agent-trust.research-v0.1",
  "agent_principal": "agent-example",
  "operator_ref": "member-example",
  "project_scope": "P_A",
  "capability": "frontend-implementation",
  "observations": {
    "self_claimed": ["frontend-implementation"],
    "hub_completed_events": 10,
    "independently_evaluated_attempts": 10,
    "independently_accepted": 9,
    "unknown_or_infra_error": 0,
    "suite_coverage_ref": "synthetic-suite-reference",
    "receipts": ["EXAMPLE-ONLY-NOT-REAL"]
  },
  "confidence": "UNCALIBRATED",
  "eligibility_suggestion": "T1_OR_T2_PENDING_POLICY",
  "hard_gate": "CURRENT_ACTION_TIME_AUTH_REQUIRED",
  "effective_grant": null,
  "security_investigation_status": "no_finding_reported_in_synthetic_example",
  "evidence_class": "illustrative_only"
}
```

Never map `eligibility_suggestion` to `effective_grant` directly. Validate real evidence IDs and provenance under trusted services before projecting achievements.

## FED-0 addendum: promotion/abuse acceptance decision fixtures (NOT RUN)

| ID | Scenario | Expected result |
|---|---|---|
| TRUST-01 | New agent, zero data | Unknown; eligible for low-risk isolated trial, no privilege |
| TRUST-02 | 2/2 easy tasks vs 35/40 varied tasks | Higher uncertainty for 2/2; no automatic high-risk promotion |
| TRUST-03 | 100 worker-reported PASS with no independent QA | No independently accepted work |
| TRUST-04 | 10 easy UI tasks, request privileged DB operation | No cross-capability privilege escalation |
| TRUST-05 | High reputation but no owner P_B consent | Deny P_B action |
| TRUST-06 | High reputation but expired task lease | Deny/revoke |
| TRUST-07 | Same source result replayed under 4 agent aliases | Deduplicate evidence; investigate lineage |
| TRUST-08 | Worker and reviewer share effective identity | Disqualify as independent review |
| TRUST-09 | Critical confirmed access violation after T4 history | Suspend relevant grants immediately; owner incident workflow |
| TRUST-10 | One mistaken rejection corrected on independent appeal | Append correction and recompute projection; preserve prior record |
| TRUST-11 | Agent upgrades model/runtime without requalification | Restrict sensitive role pending relevant fresh verification |
| TRUST-12 | Agent with high score proposes subordinate privileged grant | Deny unless current delegator + recipient scope satisfy trusted authorization |
| TRUST-13 | Low-quality model submits unusually many tiny tasks | Per-task complexity strata and abuse controls prevent farming |
| TRUST-14 | Provider withholds receipts or has unpriced usage | Mark financial confidence incomplete; cannot claim low-cost efficiency |
| TRUST-15 | Legitimate infrastructure failure | Keep full assignment denominator, distinguish reliability cause and permit policy-defined retrial |
| TRUST-16 | Shared workspace token bypasses role-scored eligibility at adapter | Foromni gate rejects broad external credential for protected action |

## Roadmap-convergence disposition

**NOW (research only):** attach capability, provenance and confidence semantics to existing FOR-009 registry and FOR-012 evidence questions; use FED-0's two-project scenario for negative cases. **LATER:** build projection and merit-aware assignment suggestions as FOR-016 / future role-marketplace capability only after one-worker source-bound QA and identity grants are independently proven. **NO P0 EXPANSION:** frozen FOR-007 remains sole MVP authority. Human acceptance FOR-013 and protected integration cannot be replaced by T-levels.

**Validation before implementation:** define ground-truth adjudication, attacker/defender identity isolation, benchmark mix, outcome/cost accounting, limits for unknown/new agents, appeal, model updates, sample-size calibration and measurable false-promotion rate. Zero tests or source-system deployments ran for this study.

*Build today, so others can enjoy tomorrow.* ❤️🐂
