# Global Collective Research Standard: Examples, Lessons, and Verified Facts

**Status:** Research proposal, not a binding policy or completed field study  
**Date:** 2026-11-21  
**Scope:** Foromni research only; no IE task, repository, integration, publication or outreach changes  
**Guiding motto:** *Build today, so others can enjoy tomorrow.*

## Purpose

Foromni should develop its research and engineering knowledge from **many independent geographies, languages, professional backgrounds, disciplines, communities and lived experiences**, rather than treating one technology company, country, sector, or AI provider as universal. Global diversity is not a quota to fill with token anecdotes. Each contribution must be accurately represented, context-aware, permissioned, checkable where factual, and genuinely useful to the wider collective.

The goal is an **evidence-to-learning-to-design feedback loop**: global observations → verified cases → competing explanations → lessons → testable design hypotheses → evaluated implementations → published results → corrections and continued learning.

## Requirements for any published research case

1. **Origin and context:** country/region and language when relevant and voluntarily public; type of participant/collective; environment and constraints. Do not infer personal demographic attributes.
2. **Primary account:** original publication, participant-authorized interview, public project artifact, dataset, repo, or official document. Preserve author, date, license, provenance, stable URL and retrieval date where available.
3. **Claim decomposition:** distinguish directly observed facts, self-reported experiences, interpretations, hypotheses, recommendations and unresolved disputes.
4. **Independent corroboration:** consult authoritative complementary sources when feasible; indicate when a single source or firsthand account is all that exists. Do not label a claim verified merely because several articles repeat the same source.
5. **Local validity:** explain cultural, legal, economic, language, technical and infrastructure context; never assume a successful pattern generalizes worldwide.
6. **Participant agency:** obtain explicit permission before publishing private testimony or identifiable case detail; provide correction/withdrawal processes where appropriate. An open URL does not automatically license copying text/media.
7. **Limitations and counterexamples:** record conditions where the lesson may fail, uncertainty and alternative explanations.
8. **Reproducible teaching:** create a clear practical lesson with a hypothetical exercise or a demonstrable, appropriately sourced real example.
9. **Revision and correction:** version the case; date changes; disclose what was corrected; connect design decisions to exact research revisions.
10. **Benefit and reciprocity:** credit sources, identify who might benefit or bear costs, invite appropriate review without implying partnership.

## Coverage dimensions: diversify methods, not just geography

Review evidence for meaningful breadth across:
- Language and translation, including non-English primary sources;
- Global North and South without treating either as a monolith;
- Rural and urban, low-bandwidth and high-bandwidth settings;
- Older devices, self-hosted hardware, intermittent connectivity and commercial hosted services;
- Individual contributors, cooperatives, open-source maintainers, businesses, public-interest projects, educational communities and professional associations;
- Different disciplines: software engineering, research, education, health-adjacent administration (not patient data), agriculture, accessibility, creative work, logistics and community coordination;
- Successful and failed initiatives, including dissenting perspectives and abandoned attempts;
- People participating as volunteers, paid professionals, learners, maintainers and decision makers.

This is a **sampling framework**, not permission to collect sensitive individual-level attributes or a requirement to represent every population before publishing a bounded finding.

## Why this matters for the Convergence Contract

The same coordination machinery must handle different social/technical realities:

| Research lens | Scenario to study (hypothetical until sourced) | Convergence question |
|---|---|---|
| Open-source contributor across continents | Async patch and review between different time zones | Can task handoff survive long delays and revoked leases? |
| Low-connectivity rural community | Worker completes an offline task and reconnects days later | Can useful contributions be retained without stale authoritative writes? |
| Multilingual learning collective | Contributors translate and revise a shared resource | Who verifies translation quality and authorizes publication? |
| Distributed professional team | Several independent specialists fulfill one client outcome | How are scope, consent, cost and client acceptance documented? |
| Community/governance network | Conflicting proposals have legitimate minority views | How are dissent, authority, appeals and decisions preserved? |
| Global knowledge synthesis | Experts reach different interpretations of the same source | How can the result preserve uncertainty instead of false consensus? |
| Small self-hosted AINO | Dated local model handles bounded tasks; humans review | Can capability be measured without provider, age or wealth bias? |

Do not present these scenarios as observed real-world examples until sourced.

## Proposed structured case-study record

```yaml
case_id: FOR-CASE-0001
status: proposed # proposed, sourced, independently_reviewed, published, corrected, withdrawn
title: "Descriptive—not promotional—title"
origin:
  region: "voluntarily-public scope or unknown"
  language: "source language or unknown"
  domain: "software | research | learning | professional | community | other"
source_records:
  - url: "primary source URL"
    author_or_org: "as publicly attributed"
    published_on: "YYYY-MM-DD or unknown"
    accessed_on: "YYYY-MM-DD"
    license_or_permission: "verified terms or unknown"
claims:
  - claim_id: "claim-01"
    text: "Atomic claim"
    type: "observed | reported | inferred | hypothesis"
    source_ids: ["source-01"]
    corroboration: "independent | single_source | unresolved"
    confidence_basis: "Why the classification is justified"
perspectives:
  alternative_explanations: []
  limitations: []
  affected_stakeholders: []
lessons:
  transferable_pattern: "Claimed useful practice"
  applicability_conditions: []
  contraindications: []
design_implications:
  convergence_contract_questions: []
  suggested_test_fixture: "No real confidential data"
review:
  subject_matter_reviewer: null
  local_context_reviewer: null
  conflict_disclosure: null
  consent_and_privacy_review: "pending"
  verification_evidence: []
revision: 1
```

This is an **illustrative draft data shape**, not a committed runtime schema. URL examples are placeholders, not source evidence.

## Editorial ladder

Each case should support multiple honest levels of communication:
1. **Fact card:** what happened, where, when, from which source, with caveats.
2. **Story:** human or collective problem, context, decision, observable outcome, disagreement.
3. **Lesson:** what can reasonably be generalized, what cannot.
4. **Practice exercise:** a safe simulation that helps members try the principle.
5. **Design test:** measurable acceptance case for an AINO or Foromni contract.
6. **Research update:** what later evidence changed, including explicit corrections.

Avoid replacing a community's voice with AI paraphrase when direct, permitted attribution is available. Seek multilingual/local-context review for consequential interpretations.

## Research quality gates

A case must **not** be advertised as independently verified unless it has source traceability and a reviewer distinct from the original author/collector. Anonymized consent-based testimony may be valuable but should be labeled testimony, not externally corroborated fact. Research claims about entire countries/cultures require appropriately representative data; anecdotes do not suffice.

For technical studies, retain exact repo/revision, environment, commands, artifacts, known failures and independent results. For nontechnical cases, preserve original goals, authorization, outcome evidence and dissent/appeal processes.

Use an inclusion check periodically: Which voices, languages, disciplines or infrastructure contexts are absent? Are omitted cases systematically unsuccessful or inconvenient? Correct selection bias rather than manufacturing balance.

## Initial research-only backlog

- Compare research practices from open-source communities, participatory-governance networks, global learning communities, and multilingual knowledge initiatives.
- Select three **documented public case studies** from different regions/disciplines and verify their primary sources, legal reuse, and local limitations.
- Design a translation/local-context review protocol and consent/correction workflow.
- Map each case to one distinct Convergence Contract stress test.
- Build an editorial source ledger for later factual educational content, with verification states and revisions.
- Document non-code acceptance and fair contributor attribution without pretending a Git check can certify human outcomes.

**Open decision:** Whether a future collective research library should be public by default, federated, or participant-managed with opt-in shared records. Default to privacy and portability until reviewed.

## Boundaries

No interviews, outreach, external commitments, publication, personal-data collection, cross-project integration, or live development were authorized by this document. Foromni remains independent of Internet Embassy; future reuse of facts/lessons in any other organization needs a separate scope and normal attribution/permission checks.

**North Star:** Our research should reflect what the world actually knows, including uncertainty and disagreement. Our engineering should turn those lessons into tools that help other people create lasting value.

*Build today, so others can enjoy tomorrow.*
