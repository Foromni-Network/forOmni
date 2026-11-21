# Cross-Domain Convergence Contract v0.2 — Outcome, Authority and Evidence

**Status:** RESEARCH DRAFT; not adopted, implemented, validated in production, or authorized for deployment  
**Date:** 2026-11-21  
**Scope:** Foromni only; no Internet Embassy changes, mergers, shared code or cross-project dependencies  
**Build discipline:** Research and tabletop exercises first. Use existing standards and platforms whenever appropriate.

## Executive decision proposal

The Foromni Convergence Contract should be **an outcome-oriented protocol**, not a Git-only merge protocol or universal task board. Its invariant core is the same for software, education, research, professional and community efforts:

> An independently operated worker may propose a contribution, but only the project-defined authorized decision process can accept that contribution toward a particular versioned outcome, using evidence appropriate to the domain.

Accepting a contribution, integrating it into a canonical result, publishing it, and verifying that it benefited intended stakeholders are **separate events**. A signed attestation may prove *who asserted something* and *which artifact was referenced*; it does not by itself prove that the assertion is correct or useful.

The earlier Convergence Contract v0.1 remains the **Git and agent-concurrency specialization**. v0.2 extends its authority/evidence model to non-code endeavors; it does not supersede its Git safety checks.

## 1. Minimum portable conceptual objects

| Object | Durable key | Required semantics |
|---|---|---|
| Collective | `collective_id` | Independent steward, jurisdiction/locale where needed, governance policy revision, privacy/ownership boundaries |
| Outcome | `outcome_id`, `outcome_revision` | Intended beneficiary, agreed success criteria, scope, limits, accountable acceptance authority |
| Task | `task_id`, `task_revision` | Bounded commitment contributing to an outcome, dependencies, assigned rights, definition of submitted vs accepted |
| Attempt | `attempt_id` | Actor/worker and execution context, lease or consent if relevant, artifact submissions, partial progress and interruptions |
| Artifact | `artifact_id`, `artifact_digest` | Content/reference, provenance, version, visibility/licensing and rights |
| Claim/evidence | `claim_id`, `evidence_id` | Typed assertion, asserted-by principal, reference, provenance, verification method, target revision, limitations |
| Decision | `decision_id` | Independently authenticated authorized reviewer/decision process, applied policy version, verdict, reasons, conflicts, appeal path |
| Convergence | `convergence_id` | Canonical accepted result/version and constituent contributions; integration validation for target domain |
| Publication | `publication_id` | Exposure, delivery or release approval and scope |
| Effect/outcome review | `effect_review_id` | Separate evidence of real-world or stakeholder result; may remain unverified even when artifact delivered |

**Actor != model.** Actors may be humans, organizations, services or agents, with independently established authority. Model/provider/version remains optional attempt provenance; it cannot create authority by itself.

**Public != unrestricted re-use.** Artifact permissions are separate from visibility and provenance. Private evidence must support verification through access-controlled references, not compulsory public upload.

## 2. Minimal draft wire envelope

The following is an **illustrative document**, not a validated JSON Schema, implementation, actual attestation, or authenticated signature.

```json
{
  "contract_version": "foromni.convergence.v0.2-draft",
  "collective": {
    "id": "example-collective",
    "policy_revision": "policy-r3",
    "authority_registry_ref": "access-controlled-policy-reference"
  },
  "outcome": {
    "id": "example-outcome",
    "revision": 2,
    "beneficiary_class": "participants",
    "criteria": [
      {"id": "OC-1", "description": "Publish a reviewed, accessible learning resource",
       "evidence_policy": "learning-publication-v1"}
    ]
  },
  "task": {
    "id": "example-task",
    "revision": 4,
    "outcome_id": "example-outcome",
    "dependencies": []
  },
  "attempt": {
    "id": "example-attempt",
    "actor_id": "org/worker-17",
    "worker_kind": "self_hosted_model",
    "lease_epoch": 6
  },
  "artifact": {
    "id": "example-artifact",
    "digest": "sha256:PLACEHOLDER_NOT_VALID",
    "visibility": "restricted",
    "rights_ref": "license-or-permission-policy"
  },
  "claims": [
    {
      "id": "example-claim",
      "criterion_id": "OC-1",
      "kind": "authored_resource",
      "evidence_ids": ["example-evidence"],
      "confidence": "unverified"
    }
  ],
  "evidence": [
    {
      "id": "example-evidence",
      "kind": "source_review",
      "asserted_by": "org/worker-17",
      "artifact_digest": "sha256:PLACEHOLDER_NOT_VALID",
      "verification_state": "submitted",
      "limitations": ["Independent source review not completed"]
    }
  ],
  "decisions": [],
  "convergence": {"state": "not_admitted"},
  "publication": {"state": "not_authorized"},
  "effect": {"state": "unknown"}
}
```

A future actual schema must prohibit placeholders, enforce identifiers and digests, define canonical serialization, authenticate the submitter, validate all references, check policy versions, and expose safe rejection codes. No assumption that one central authority operates all collectives.

## 3. Domain-independent state axes

A universal *single enumerated status* is misleading. Keep **orthogonal dimensions**:

- **Planning:** proposed → scoped → ready, or declined/withdrawn.
- **Execution attempt:** offered → claimed → running → submitted | interrupted | failed | expired | cancelled.
- **Evidence:** asserted → received → authenticated → independently_checked → supported | disputed | rejected | inconclusive.
- **Admission:** pending → accepted | rejected | conditional | superseded; all require policy-bound decision record.
- **Integration/collective convergence:** pending → reconciled → integrated | blocked | failed, using domain-specific checks.
- **Publication/exposure:** not_requested → proposed → approved → published | revoked.
- **Real-world benefit:** not_assessed → in_progress → observed | unconfirmed | contested, with assessment scope.

Transitions require actor authority, applicable policy revision, exact object revisions and evidence. Failures append events rather than overwriting history. Policies may forbid stages entirely for certain projects.

An approved software patch can remain unreleased; a voted proposal can remain unimplemented; a printed artifact can remain unsuitable for its intended recipient.

## 4. Domain adapters: same core, different independent proof

| Domain | What may be submitted | Independent acceptance authority | Evidence and distinct final outcome |
|---|---|---|---|
| Software | Patch, PR, build artifact | Appointed maintainer/QA + protected integration controller | Exact task SHA, CI/test results on synthetic merge and actual integrated revision; separate release evidence |
| Research | Dataset, synthesis, translation, method | Qualified designated reviewer or review panel | Sources, methods, replication/critique, uncertainty and provenance; publication ≠ confirmed real-world impact |
| Learning | Student work, curriculum, tutorial | Learner/mentor or accredited assessor as applicable | Consent-aware assessment, clear rubric, demonstrated competency; no universal score or compulsory public portfolio |
| Professional services | Agreed deliverable or milestone | Contractually entitled client/project authority | Scope/rights, delivery acknowledgement, acceptance, dispute resolution; payment authorization separate |
| Community/governance | Proposal, record, shared decision | Project-specific legitimate decision process, stakeholder rules | Eligibility, deliberation, decision, dissent and audit trail; selected ≠ implemented ≠ impact |
| Maker/assistive device | Design, fabricated artifact | Recipient and relevant qualified safety/professional parties | Design version, suitability/safety assessment, recipient consent; no AI substitution for clinical judgment |

**Universal validity:** independent *authority* and *evidence* are necessary for the relevant acceptance claim, but different legitimate processes (human votes, client approval, reproducible tests) cannot be collapsed into one algorithmic 'pass' score.

## 5. Authority, sovereignty and disagreement

- The collective defines its own permitted decisions and stakeholders under a versioned governance policy, constrained by applicable laws and baseline safety/consent rules.
- Each contribution has a recorded origin, grant, data handling class, and revocation/reuse policy.
- No outside agent receives authority to vote, consent on behalf of a person, sign a professional acceptance, or merge protected work merely for completing an assigned task.
- Preserve dissent, minority objections, appeals, withdrawn consent, disputed facts and superseding decisions rather than flattening them into consensus.
- Avoid publishing private audit data to show transparency; support privacy-respecting metadata, redaction policies and authorized access.
- An affected individual's request to restrict personal information may require deletion or redaction rather than immutable public retention; keep narrowly scoped audit metadata only where lawful/necessary.
- Peer review independence should be evaluated by conflict of interest and organizational control, not just distinct agent usernames.

**Important:** The coordinator cannot assume ownership of participants' work, identity, original project systems, credentials, or data.

## 6. Evidence technologies — adopt selectively, do not conflate meaning

**W3C PROV-O** models provenance among entities, activities, and agents. Reuse its conceptual graph for origin and derivation where suitable rather than inventing vague attribution fields.
https://www.w3.org/TR/prov-o/

**in-toto** describes verified software supply-chain steps and signed links. Appropriate inspiration for code/build/deploy evidence, without claiming it verifies stakeholder benefit.
https://in-toto.io/docs/getting-started/

**C2PA Content Credentials** support media provenance/authenticity checks; their own specification explicitly distinguishes validating assertions and bindings from judging underlying truth. Optional for content artifacts; not a universal truth engine.
https://spec.c2pa.org/specifications/specifications/2.5/specs/C2PA_Specification.html

**W3C Verifiable Credentials Data Model 2.0** provides privacy-aware, verifiable credential representation. Useful to study for issuer-authorized capabilities or qualifications, but verification of cryptographic proof does not establish the truth of the claimed skill or authorize actions outside the collective's policy.
https://www.w3.org/TR/vc-data-model-2.0/

**Decidim's accountability component** tracks results and their execution, reinforcing the distinctness of democratic selection, execution and real-world accountability.
https://docs.decidim.org/en/develop/admin/components/accountability.html

Standards may be combined only after validating versions, extension compatibility, threat models and participant consent. They are **candidate interoperable primitives**, not selected dependencies.

## 7. Lessons transformed from the first three Foromni case studies

**Nepal 2015 remote/local mapping:** Remote workers can produce useful candidate data, but meaningful validation should include relevant local context. A 'mapped' task must not automatically mean a humanitarian outcome was achieved.

**Barcelona participatory budgeting:** Legitimate selection follows project-specific eligibility, feasibility and public participation rules; selected projects may remain unimplemented. Distinguish proposal, decision, execution and outcome evidence.

**Global e-NABLE making:** A fabricated design is not proof of recipient suitability or safe use. Accept technical/design contributions without granting an agent professional or individual consent authority.

These are design inferences from sourced desk research, not field-tested requirements.

## 8. Threat and failure model

1. A provider reports task success with a plausible but fake artifact URI.
2. A reviewer cryptographically verifies an attestation, then wrongly labels its real-world claim true.
3. Two independent agents submit revisions to the same draft simultaneously.
4. Local stakeholder veto/consent is omitted from an otherwise technically passing workflow.
5. An old outcome specification is silently used to accept a newer project goal.
6. An agent impersonates a project decision-maker or reuses revoked permissions.
7. A participant submits sensitive personal data in a public evidence bundle.
8. A collective changes voting policy halfway through a process without a recorded transition.
9. Two different reviewers are in fact controlled by the same operator when separation is required.
10. A legally protected deletion conflicts with an indiscriminately append-only public audit log.
11. A selected project or delivered artifact is incorrectly reported as beneficiary impact.
12. A purportedly 'neutral' model router exfiltrates restricted data to external inference.
13. A self-hosted offline contributor submits after its authorization/lease expires.
14. A published resource proves false later; correction/retraction must remain visible.
15. An external group has a valid contribution but no obligation to accept a Foromni-controlled result.

All need defined rejection, repair, escalation and appeal paths. **Fail closed on privileged/irreversible actions**, while allowing low-risk isolated contributions and corrections to continue.

## 9. Research acceptance criteria for v0.2

- Every candidate links a versioned outcome, task, actor, artifact, claim, evidence, authority and disposition, or explicitly records why a concept is not applicable.
- For every domain, one **accepted contribution** and one **unaccepted but preserved contribution** are expressible without a Git SHA.
- No case is marked 'real-world benefit verified' solely because the task artifact passed a technical check.
- The same contract can encode human, cloud AI, self-hosted/older-model and deterministic-script participation.
- Conditional/revoked consent and private evidence remain representable.
- Independent reviewer decisions reference policy version and evidence—not provider status.
- Existing Git concurrency semantics remain intact: protected ref writes, lease fencing, exact merge-result checks and post-integration verification for software.
- An independent observer can replay event histories and obtain the same authorized state projection, with contested events retained.
- All tabletop failures are rejected, escalated or safely deferred without inventing evidence.

These are **design acceptance targets**, not achieved software test results.

## 10. Research sequence before implementation

**R0 (now):** Review this model with the original three case studies and add edge cases/authority conflicts.

**R1:** Produce event schemas, decision matrix and privacy-preserving evidence-reference definitions; distinguish stable canonical fields from domain extensions.

**R2:** Author synthetic event sequences spanning: two concurrent software writers, a research correction, a learner privacy withdrawal, a community vote under changing rules, and a professional milestone dispute.

**R3:** Compare how Zuul/Prow/GitHub, Decidim, W3C PROV, in-toto and C2PA align to the core; record which validations can actually be delegated to each.

**R4:** Independent review and formal v0.x revision, explicitly recording rejected alternatives.

**R5:** Founder-authorized disposable technical proof only after the contract consistently explains all five domains and its safety assumptions are reviewable.

## Final principle

Foromni should not become one global decision-maker. It should provide interoperable coordination rules so **independent collectives can converge contributions into outcomes they legitimately choose and verify**, without being forced to surrender their autonomy.

**Build today, so others can enjoy tomorrow.**
