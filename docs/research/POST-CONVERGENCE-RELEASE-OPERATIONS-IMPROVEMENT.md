# Post-Convergence: AI-Operated Validation, Release, Operations, and Improvement

**Status:** Research proposal, NOT implemented / authorized for a live pipeline.  
**Date:** 2026-11-21. **Scope:** Foromni only. No Internet Embassy access, modifications, integration, or deployment.  
**Companions:** CONVERGENCE-CONTRACT-V0.1.md; CROSS-DOMAIN-CONVERGENCE-CONTRACT-V0.2.md; AI-OPERATED-AINO-OVERSIGHT-MODEL.md; AI-FULL-STACK-END-TO-END-WORKED-TRACE.md; SCALING-THE-CONVERGENCE-CONTROLLER.md.

## Executive research recommendation

Treat convergence as **verified source integration**, not software release or proof of real-world value. After a protected mainline updates, a separate chain should construct an immutable artifact, validate it in an isolated environment, seek authorized release approval, deliver progressively when appropriate, observe effects, recover from failures, and feed learnings back into existing roadmap and incident records.

**Key separation:** `source_integrated` ≠ `artifact_built` ≠ `staging_verified` ≠ `release_authorized` ≠ `released` ≠ `healthy` ≠ `beneficiary_outcome_verified`.

AI-operated workers may perform most routine activity inside bounded permissions. A deterministic policy gate, independent verification, and human approval for consequential operations prevent an agent's persuasive declaration from being treated as authority.

## 1. A proposed pipeline — logical stages, not Git branch names

```
Independent feature branches
      → protected merge queue / exact-SHA QA
      → canonical main commit
      → immutable, provenance-bound build artifact
      → disposable staging / end-to-end / security / compatibility gates
      → release candidate / approval request
      → authorized progressive rollout
      → telemetry + user/stakeholder feedback
      → repair / rollback / next roadmap iteration
```

Do **not** assume a branch for staging, QA or production is required. Favor immutable artifact promotion: the same digest that passed staging should be the artifact deployed to the intended target, with environment-specific configuration outside that artifact. Optional short-lived `release/*` branches are for stabilization or supported-version patching and must reconcile with `main`; they must not create an undetected parallel product history.

### Chain of custody

At minimum record:
- `main_commit_oid` and task/candidate provenance links;
- dependency-lock and build-system revisions;
- build/run attestation (who, where, tooling version, inputs);
- `artifact_digest`, signature/attestation if available;
- SBOM/dependency and license policy if applicable;
- staging environment, test version, synthetic data and observed results;
- `release_decision_id` with accountable authority and policy revision;
- deployment environment, rollout stage, actual running artifact digest;
- monitoring/effect observations and any incident or remediation IDs.

If a rebuilt artifact has a different digest, it requires its own provenance and necessary validation; do not reuse the old pass blindly.

## 2. Autonomous workforce roles after convergence

| Role | AI-operable bounded activities | Trusted / human-controlled boundary |
|---|---|---|
| Build/reproducibility worker | Compile, package, create artifact manifests, scan dependencies in sandbox | Cannot promote modified artifact by claiming equivalence |
| Independent staging QA | Browser/API/database tests, accessibility and security probes, reproducibility | Credential isolation, distinct reviewer authority, exact artifact check |
| Release readiness agent | Summarize evidence, rollout risk, rollback strategy, ask for approval | Cannot grant approval to itself or invent effective permissions |
| Rollout controller | Execute **only** explicitly permitted release plan, traffic steps and configured stop conditions | Infrastructure policy, authorized environment grant, fail-closed on uncertainty |
| SRE/operations agent | Examine allowed telemetry, classify incidents, run read-only diagnostics, propose repair PRs | No unrestricted access to production secrets/customer data |
| Incident response worker | Trigger pre-approved safe containment actions, prepare rollback recommendation and incident timeline | Critical effects and emergency overrides under accountable policy |
| Feedback/roadmap agent | Correlate errors, tasks, consented user feedback; propose prioritized tasks | Cannot falsify results or unilaterally expand mission/privacy scope |
| Human owner / steward | Set objectives, acceptable risk and spending, approve material release decisions | Remains ultimately accountable; not routine manual coding requirement |

One agent may fill multiple low-risk operational roles, but independent acceptance and privileged publication must be separated by enforceable policy, not just separate prompts.

## 3. Release gate and graduated autonomy

**R0: Source:** Integrator observes actual main commit and required postmerge checks.

**R1: Artifact:** Builder produces reproducible or appropriately attested artifact with stable digest and minimal rights.

**R2: Staging:** Independent environment-specific tests confirm critical user flows, data isolation, migrations and rollback readiness. Credentials, tenancy, external network and secrets are sandbox scoped.

**R3: Release authorization:** Project-defined accountable approver reviews evidence and risk. No automatic public deployment from `main` unless an explicit advance release policy was separately approved for a bounded low-risk class. Release approval is a durable, time-limited, target-specific authorization event.

**R4: Progressive delivery:** Release service applies the authorized plan, observes health thresholds, stops and rolls back on defined conditions; never improvises expansion of blast radius.

**R5: Operations:** Observe runtime health, latency, errors, saturation, accessibility feedback, security events and customer-impact signals with consent/data minimization.

**R6: Improvement:** Link issues and verified outcomes to originating artifact and source; create repair requests with task contracts and independent evidence; re-enter worker/integration flow.

### Changes with special caution

Schema migrations, destructive data operations, irreversible configuration changes, authentication/permission changes, payment/external communications, secrets changes and legal-sensitive workflows may not be safely undone by rolling back application code. Require explicit migration/backward-compatibility and recovery plans, relevant stakeholders, and separate consent/authorization before acting.

## 4. Adopt instead of rebuild: upstream candidates

- **GitHub Actions environments** support required deployment reviewers, branch/tag constraints, environment-scoped secrets and custom protection rules. Availability varies by GitHub plan and repository visibility; check the actual project's permissions and edition before relying on them.  
  https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments
- **Argo Rollouts** is a Kubernetes-oriented controller supporting canary/blue-green releases, analysis and abort/rollback behaviors. Its infrastructure footprint may be unjustified for simpler application hosting.  
  https://argoproj.github.io/argo-rollouts/features/analysis/  
  https://argoproj.github.io/argo-rollouts/features/rollback/
- **Flagger** implements progressive delivery informed by telemetry with supported service-mesh/ingress and GitOps integrations; evaluate against actual hosting, not abstract popularity.  
  https://flagger.app/
- **Google SRE Workbook** describes canary releases as a way to reduce failure blast radius through partial exposure and measurement.  
  https://sre.google/workbook/canarying-releases/
- **OpenTelemetry** offers vendor-neutral APIs/SDKs for traces, metrics and logs. Instrumentation is not a sufficient outcome/impact metric by itself.  
  https://opentelemetry.io/docs/concepts/observability-primer/
- **DORA** tracks software-delivery performance and stability; use metrics carefully and avoid optimizing deployment frequency alone while neglecting quality. The current DORA model has evolved beyond its original four metrics.  
  https://dora.dev/guides/dora-metrics/

All are research candidates. No vendor selected, configured or deployed.

## 5. Hypothetical release event example

```json
{
  "schema": "foromni.release-event.v0.1-PROPOSAL",
  "objective_id": "OBJ-DEMO",
  "source_main_sha": "PLACEHOLDER_SHA",
  "artifact": {"digest": "sha256:PLACEHOLDER", "build_attestation_ref": "example-build"},
  "staging": {"status": "INDEPENDENT_TESTS_PENDING", "test_run_refs": []},
  "release": {
    "environment": "demo-production",
    "authorization": "NOT_GRANTED",
    "plan_revision": 1,
    "rollout": "NOT_STARTED",
    "rollback_reference": "previous-known-good-artifact"
  },
  "operations": {
    "observability_state": "NOT_DEPLOYED",
    "beneficiary_outcome": "UNKNOWN"
  }
}
```

This object is illustrative, not a validated JSON Schema or evidence. Production writes must verify actual signed/authorized principals, source and artifact digests, policy revisions, lease state, user rights and action-specific scopes.

## 6. Operations feedback: close the loop responsibly

Every observation should distinguish:
- **Signal:** latency, crash, security alert, broken user flow, consented customer complaint, engagement or usage observation.
- **Interpretation:** AI-generated hypothesis, never automatically treated as fact.
- **Corroboration:** independently reproduced bug, known release change, domain expert assessment or controlled experiment.
- **Action:** bounded remediation proposal, pre-approved mitigation under a policy, or human escalation.
- **Verification:** health and beneficiary impact observation after remediation, with limitations.
- **Learning:** versioned incident/postmortem and a new or updated roadmap task; do not duplicate task IDs.

The operation agent may triage and draft PRs, but it must not write unrestricted production data, silently move monetary resources, or roll forward a failed change outside granted policy.

## 7. Twelve post-convergence failure exercises (not executed)

1. Main merge succeeded but ledger ACK was lost; read Git truth before rebuilding/promoting twice.
2. Source main SHA differs from artifact build source; deny promotion.
3. Staging tests pass on artifact A, release references artifact B; deny.
4. Tests pass with fixtures, but real permission isolation fails in staging; hold release and return to repair.
5. Human approves release plan for environment X, agent requests Y; deny.
6. Release authorization expires; deny even if old green checks remain.
7. Canary shows elevated error rate; halt and perform only policy-approved rollback/mitigation.
8. Database migration is destructive; app rollback alone is insufficient; require separate recovery authorization.
9. Agent attempts to fetch private user content into a public cloud LLM for triage; deny or require redaction/new authorization.
10. External provider outage; safe degraded mode and human communication if appropriate, with scoped authority.
11. Deploy succeeded but telemetry is unavailable; mark health UNKNOWN, stop automatic expansion rather than declare healthy.
12. Metrics return green but user-reported essential workflow remains broken; task remains open for outcome verification.

## 8. AI autonomy and human oversight experiment

**Question:** How far can agents autonomously drive routine delivery after the code is merged without increasing failures, unauthorized actions or human alert fatigue?

Compare:
- Manual release operator with ordinary CI baseline.
- AI-assisted readiness and triage; humans approve release.
- AI-operated staging/release prep with deterministic deployment controller, human approval of consequential action.
- Preapproved narrowly bounded low-risk automated rollouts with telemetry-driven abort and human escalation.

Hold artifact/version, test suite, risk class and environment fixed. Record human intervention counts, time-to-detect, time-to-recover, false alarms, change failure rate, escaped defects, cost per healthy verified release, and downstream stakeholder outcomes. Do not claim any configuration proven until tested.

**Stop/go criteria:** Zero unauthorized deployments/data transfers, exact artifact evidence, independent QA integrity, successful bounded recovery, and transparent uncertainty. A failed run never becomes accepted by changing its status label.

## 9. Research backlog (not canonical task registry entries)

**FOR-RD-RELEASE-001:** Define post-convergence artifact promotion and immutable release evidence.  
**FOR-RD-OPS-002:** Compare telemetry + incident-response adapters with privacy controls.  
**FOR-RD-RELEASE-003:** Design progressive-rollout/rollback policy and human decision events.  
**FOR-RD-LEARN-004:** Map production errors and consented feedback to repairs and roadmap provenance.  
**FOR-RD-EVAL-005:** Design repeated synthetic end-to-end trials and reliability evaluation.

Each remains **proposed**, not an approved Supabase/GitHub roadmap task. Reconcile IDs and ownership before creating canonical registry items.

## 10. Future edutainment opportunity

Episode: **"Your Code Merged. Your App Still Isn't Ready."**  
Hook: Eight AI coders celebrate a green mainline. The staging robot discovers an auth bug. The rollout robot won't deploy without authority. The SRE robot finds a regression during a fictional canary. The founder sees one accurate decision request—not 50 vague task-complete messages.

Lesson: integrate ≠ validate ≠ release ≠ healthy ≠ actually useful. A full loop produces trustworthy learning.

Label demonstrations and metrics hypothetical; link primary source standards, and never imply Foromni has implemented these capabilities.

## Conclusion

The protected `main` is not the finish line. **The finish line is a verified outcome for the intended collective**, with human-governed consequences, AI-operated execution, and durable evidence from one iteration to the next.

*Build today, so others can enjoy tomorrow.*
