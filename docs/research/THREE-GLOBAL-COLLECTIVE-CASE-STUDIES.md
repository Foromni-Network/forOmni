# Three Global Collective Case Studies: Nepal, Barcelona, e-NABLE

**Research status:** First documented source-based comparative study; not fieldwork, an endorsement, or experimental validation of Foromni.  
**As-of:** 2026-11-21. **Scope:** Foromni research branch only; no IE updates, no deployments, no contact with case organizations.  
**Companion:** GLOBAL-COLLECTIVE-RESEARCH-STANDARD.md; COLLECTIVE-FIRST-STRATEGY-AND-CONVERGENCE.md; CONVERGENCE-CONTRACT-V0.1.md.

## Study method

Three documented public cases were selected to deliberately vary **region and domain**: (1) 2015 Nepal earthquake humanitarian mapping, (2) 2020–23 Barcelona, Spain participatory budgeting, (3) the international volunteer-maker e-NABLE assistive-device network, with its original collaborators in different countries. This is not a representative global sample. I read originating community/operator materials and available external research. Where public reports contain self-reported counts, figures remain attributed rather than independently audited. No interviews, consented participant testimony, production trials, or independent reproduction occurred.

For each case separate **documented observations**, **limits/contradictions**, **design inferences**, and **proposed adversarial tests**.

---

## Case FOR-CASE-001: Nepal earthquake / remote-humanitarian mapping (2015)

**Origin/discipline:** Nepal and remote contributors globally; humanitarian geospatial data.  
**Case status:** Sourced from community firsthand documentation and secondary/academic sources; *not independently field-verified*.

### What primary sources report

The OpenStreetMap community's contemporaneous Nepal response page states that **more than 7,500 worldwide contributors** participated between April 25 and June 8, 2015. HOT's Tasking Manager organized digitization work, while Nepal-based Kathmandu Living Labs and international HOT volunteers connected mapping needs with responders. Documentation names on-the-ground and overseas coordinators in different time zones; describes mapping roads, buildings and settlements; and explains that map data supported response organizations.

**Primary/community documentation:**
- https://wiki.openstreetmap.org/wiki/2015_Nepal_earthquake (sections: Response; Coordination; volunteers)
- https://wiki.openstreetmap.org/wiki/Humanitarian_OSM_Team/Working_groups/Activation/meeting_2015-05-12

**Cross-check/critical perspective:**
- https://ieeexplore.ieee.org/abstract/document/7427206 — academic study title: “Potential of Collaborative Mapping for Disaster Relief: A Case Study of OpenStreetMap in the Nepal Earthquake 2015”; search abstract describes local-to-remote coordination to improve map accuracy; full text was not available through research access.
- https://media.odi.org/documents/12042.pdf — humanitarian evidence study discusses caution about distinguishing pre-existing damage from earthquake damage in crowdsourced imagery, and limitations of fragmented needs assessments; PDF content was accessible in parsed web form, but screenshot retrieval returned cache miss. Treat this as a caveat pending visual-source verification.

**Limits:** A reported volunteer count is not a verified count of *correct* map edits or of lives saved. Mapping and actual relief outcomes have different evidence standards; the quality of remote data can vary and local contextual review matters. Do not present all crowd-sourced annotations as ground truth.

### Transferable lessons

1. Decompose large, time-critical collective needs into bounded work packages.
2. Local stakeholders must influence requirements and validate whether remote outputs are useful.
3. Diverse and asynchronous contributors need handoffs and explicit responsibility.
4. Contributor quantity and task closure are not equivalent to verified real-world impact.

### Proposed Foromni requirements

- `task.local_context_owner` and authorized external evidence reviewer separate from `attempt.worker`.
- Geo/source metadata and `provenance` required for factual mapping artifacts.
- Independent verification levels: uploaded → reviewed → locally confirmed (only when actually observed).
- An evidence warning when an output's source (e.g. satellite imagery) cannot support its claimed conclusion (e.g. exact earthquake causation).

### Synthetic test FOR-TEST-001

Remote agent marks 100 map tiles finished; two tiles contain incorrect interpretation of damage. Local reviewer rejects those tiles, accepts the remainder, and the ledger must retain original submissions and reasoned rejection. A donor-facing dashboard must not report “100 tiles validated” or “100 communities served.”

---

## Case FOR-CASE-002: Barcelona participatory budgeting (2020–2023)

**Origin/discipline:** Barcelona, Catalonia, Spain; public decision-making and participatory governance.  
**Case status:** Operator-published case study, plus academic/municipal research; local outcomes not independently audited in this study.

### What sources report

Decidim's case study describes **€30 million** available for participatory projects. It describes a staged process: residents submit ideas; municipal technical teams evaluate legal, technical and economic feasibility and explain rejections; residents support/prioritize eligible projects; staff refine scope/budgets; census-based verification and voting select projects for implementation. The case page reports **1,982 submitted proposals**, **823 passing technical viability**, **204 prioritized**, **76 selected in final voting**, and **64,571 participants**. The case page's summary labels/phase descriptions are not perfectly uniform: its header associates some numbers with different stages than its narrative, so the phase narrative and counts should be preserved with attribution rather than recast as independent measurements.

**Operator source:** https://decidim.org/case-studies/barcelona-budgeting  
**Additional study:** https://www.institutmetropoli.cat/en/estudi/digital-citizen-participation-in-the-province-of-barcelona-digital-platforms-and-participatory-budgeting/  
**Academic context:** https://ejpr.onlinelibrary.wiley.com/doi/full/10.1111/1475-6765.12421

**Limits:** “Selected for implementation” and “completed with positive public impact” are distinct. An official source presenting project success should not be treated as an independent outcome audit. Participation was not perfectly digital-only; the hybrid online/in-person design was important. Feasibility gates and voting legitimacy are social and institutional, not executable Git/CI tests.

### Transferable lessons

1. Distinguish *anyone may propose* from *the relevant authority may approve*.
2. Publish process rules before decisions and the reason for acceptance/rejection afterward.
3. Keep feasibility, prioritization, selection, implementation, and verified completion separate.
4. Digital participation should not erase people who engage via other channels.

### Proposed Foromni requirements

- Project-specific authority matrix for proposal → feasibility → deliberation → legitimate decision → implementation → evidence of real completion.
- Stakeholder/eligibility checks must be authorized and privacy-preserving.
- Recorded reason codes, appeal/review channels and public/private evidence classification.
- Support non-code collective outcome adapters; Git SHAs should not be mandatory for governance tasks.

### Synthetic test FOR-TEST-002

One thousand suggestions are submitted; only eligible proposals can advance. An agent may summarize public suggestions but cannot simulate eligibility verification or cast votes. A budgeted outcome remains `selected` until a separately authorized completion verifier confirms implementation.

---

## Case FOR-CASE-003: Global e-NABLE volunteer makers and assistive devices

**Origin/discipline:** Transnational volunteer maker network with collaborative roots across countries; open designs, 3D printing, recipient support.  
**Case status:** Sourced from operator/community pages, not an independent clinical evaluation.

### What operator/community sources report

e-NABLE describes itself as a global volunteer network creating free 3D-printed hands and other assistive devices, with designs shared and improved by volunteers. Its involvement page distinguishes recipient requests from volunteers, says certified makers can review requests, and documents multiple roles (printing, assembly, sizing review, chapters, tutorials, R&D, design improvements). Its guidance expressly warns that 3D-printed devices **are not appropriate for everyone**, are not a replacement for professional prosthetic care, and volunteers are not necessarily medical professionals.

**Organization pages:**
- https://enable-site.vercel.app/get-involved
- https://enable-site.vercel.app/about/history
- https://enablingthefuture.org/about/
- https://www.enablewebcentral.com/

**Limits:** Community-reported device and volunteer counts are not independently verified here. Neither a completed print nor a shipment proves recipient suitability, fit, long-term outcomes, or clinical efficacy. No personal recipient details should be harvested from case pages without permission; do not infer patient data or recommend these devices as medical treatment.

### Transferable lessons

1. A shared project can benefit from many contribution types, not just software engineering.
2. Designs need versions and provenance, while local makers bring situational knowledge.
3. Recipient needs and consent define the outcome, not the contributor's artifact alone.
4. Some outcomes require certified competence, specialized safety controls and limits on automated acceptance.

### Proposed Foromni requirements

- Support role- and competency-scoped participation, including self-declared vs verified capabilities.
- Preserve design versions, licensing and attribution through handoff.
- Distinguish design submission, making, inspection, delivery and recipient-appropriate acceptance.
- Critical safety domains require human/professional decision owners; an AI agent's self-reported success must never substitute.

### Synthetic test FOR-TEST-003

Three contributors submit different design variants; one 3D-print artifact passes file-format validation but fails fit/safety review for the intended person. Status stays `rejected_for_use` or `needs_revision` for that purpose, with design contribution retained and recipient information kept private.

---

## Cross-case synthesis: Convergence is larger than merging code

| Dimension | Nepal | Barcelona | e-NABLE | Core Foromni abstraction |
|---|---|---|---|---|
| Coordination | Remote + local mapping | Public + technical + institutional stages | Recipient + maker + design contributor | Bounded tasks and handoffs |
| Authority | Humanitarian mapping requirements / local review | Rules, feasibility review, legitimate vote | Recipient needs, maker qualifications, safety guidance | Explicit domain-specific decision rights |
| Evidence | Provenance, map validation, local feedback | Eligibility and recorded outcomes | Design/version, production review, suitability | Typed evidence and independent review |
| Failure | Misinterpreted imagery / bad data | Ineligible proposal or unimplemented selection | Unsuitable device despite finished print | Honest repair states |
| Benefit | Better information for response | Legitimate public project decisions | Practical assistive-device support | Stakeholder-defined accepted outcome |
| Rights | Contributor attribution; responsible data use | Participation and privacy | Recipient privacy and design rights | Consent, provenance, portability |

**Provisional generalization, not experimentally proven:** the common unit is an authorized, versioned *commitment to an outcome*, with contribution evidence, a domain-specific acceptance rule, and an explicit beneficiary/decision owner. A software branch/merge is only one adapter.

## Three changes proposed for the Convergence Contract

1. **Outcome contract separate from execution artifact.** Give every task a definition of benefit and an authorized acceptance authority. A passing file check is not completed service, map validation is not relief delivered, and a city vote is not implemented infrastructure.
2. **Local-context and stakeholder-validation hooks.** Relevant communities can reject technically valid but contextually unsuitable contributions. Make such decisions explicit, reviewable, consent-aware and not silently overridden by a remote agent.
3. **Evidence typing plus independent-gate separation.** For each stage record `claim_type`, `evidence_type`, `source`, `revision`, `reviewer`, `authority_basis`, `confidence_limits` and `decision`. Different domains supply different required evidence. No global one-size-fits-all pass badge.

## Follow-on research questions

- Can contributors and beneficiaries agree on a minimal, portable `outcome_contract` without exposing sensitive personal information?
- How should an appeal, public dissent, or withdrawal be expressed in an append-only event ledger?
- Can local reviewers prevent dominant outside contributors from claiming authority over community needs?
- When does global collaboration actually reduce the time to a safe accepted outcome, including reviewer workload?
- Which data can be exported or publicly attributed under each case's actual licenses and consent terms?

## Evidence and publication caution

These are **three sourced desk-research cases**, not three field-validated case studies. Source counts are attributed. Interpretations and Foromni test fixtures are hypotheses. No direct source organization was contacted, no software was built, and no tasks were imported into Internet Embassy.

The next responsible step is a source-to-claim ledger with independent checks of each assertion and a follow-up case from a different region/field where local primary sources are accessible. Avoid global representativeness claims from three cases.

*Build today, so others can enjoy tomorrow.*
