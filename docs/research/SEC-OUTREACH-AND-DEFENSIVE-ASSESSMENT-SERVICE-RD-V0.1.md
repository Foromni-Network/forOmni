# Foromni Security Research → Collaboration and Authorized Services R&D v0.1

**Date:** 2026-11-25. **Status:** future research/market validation, not an active paid offer, certification, customer contract, authorized scan, operating claim, or license selection. Foromni only. No IE import or outreach sent.

## Opportunity hypothesis

Publish reproducible, scoped *defensive* case studies (synthetic experiments first; real findings only through responsible disclosure) to attract engineering collaborators, open-source contributors, educational partners, and potentially clients for authorized security assessments. Separate the public trust-building research program from any future commercial service obligations.

### Collaboration funnel (research proposal)

Research evidence → non-sensitive public case study → repo issue/discussion or opt-in technical workshop → joint lab reproduction → upstream fix or improvement with proper licensing → public credited contributor outcome → optional separately contracted service.

Outreach must be opt-in, technically relevant, accurate and never claim that another organization is vulnerable based on a synthetic fixture. No unsolicited testing, no leak of targets/secrets, no fake endorsements, and no security guarantee.

### Potential service packages to evaluate, not pricing offers

| Candidate service | Deliverable | Exclusions / required contract |
|---|---|---|
| Agent and MCP architecture review | tool inventory, trust diagram, machine principal/capability matrix, prioritized remediation | read-only review first; no vulnerability exploitation without explicit written scope |
| Scoped agent/tool security assessment | authorization, request replay, provider effect and tool poisoning laboratory cases | only owned/client-authorized systems; approved rate limits, hours and incident contact |
| Automation resilience review | webhook and cron replay tests, failure recovery design and idempotency gap analysis | no production write tests or billable third-party effects by default |
| AI security logging and detections | structured events, detection hypotheses, labeled evaluation and tuning suggestions | explicit log access, retention and privacy plan; no claims of efficacy without held-out evaluation |
| Secure AINO component exchange readiness | provenance manifest, software license inventory, CI/rollback workflow design | no legal opinion; license and contributor policy requires counsel review |

## Three-way value split

- **Public commons:** generic defensive tests and securely shareable abstractions remain available under a valid chosen license; avoid private customer artifacts in open Git.
- **Partner outcomes:** partner retains private configurations, secrets and ownership; authorized upstream contributions occur only with validated rights and explicit consent.
- **Commercial services (possible):** payment for scoped analysis, implementation, training, support, monitoring, verification and customized integration. The scope and any source-license obligations must be documented before making an offer.

## Evidence maturity labels

RESEARCH_ONLY → LOCALLY_REPRODUCED → INDEPENDENTLY_REVIEWED → AUTHORIZED_CLIENT_PILOT → PUBLIC_CLAIM_APPROVED. Never treat a test suite's `15/15` as a real-world detection rate or a product certification.

## Authorization and service operations checklist

Written statement of work; approved asset/tenant list; permitted test actions; prohibited effects; test accounts; NDA and data retention; defined escalation and stop button; liability/insurance/legal review as appropriate; accurate report/limitations; remediation window; authorized publication and responsible disclosure process; separate billing and security obligations; explicit no warranty of perfect safety.

**Go/no-go gates:** legal licensing of Foromni's core and contributed files, maintainer agreement on public materials, qualified security reviewer, adequate technical isolation, pre-sale service delivery capacity, scope documents and privacy controls. Service business model is hypothetical until validated.

## Initial outreach experiment (not executed)

Create three concise public research summaries, all with source and failure limits, aimed separately at: (1) MCP maintainers and OSS developer communities, (2) AINO operators building secured tool integrations, (3) security educators/defensive engineers. Observe voluntary engagement, reproducible external feedback, accepted upstream contributions, and qualified opt-in calls. Do not scrape contacts, send messages or promise external validation. Compare outcomes per effort, not vanity impression counts.

## Adjacent portfolio research

EXP-18 structured agency threat-event detector (synthetic fixture, no real-world efficacy); future held-out evaluation and incident triage; EXP-7 replay; EXP-10–15 isolation; EXP-16/17 update provenance; PMI-CPMAI goal/outcome management and A+/Security+/CySA+ learning track.

**Decision:** preserve as a potential growth and monetization avenue, *not* launch or solicit customers until explicit founder approval and accurate scope/proof.
