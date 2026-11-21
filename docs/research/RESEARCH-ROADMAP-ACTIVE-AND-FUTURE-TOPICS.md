# Foromni Research Roadmap — Active Questions and Future R&D Parking Lot

**Status:** Research roadmap working index, proposed priorities; **not** the canonical task registry or an approved implementation roadmap.  
**Date:** 2026-11-21. **Repository scope:** Foromni only. No Internet Embassy changes.  
**Reference:** Foundational ROADMAP.md and draft `roadmap/tasks.json` remain in their separately reviewed branches. This document must be reconciled by maintainers before any task identifiers/statuses are incorporated into the canonical roadmap. No existing FOR-001..FOR-006 task is duplicated or changed here.

## Purpose

Keep research focus disciplined while preserving promising future investigations. Research **must not** be confused with a development authorization, a scheduled experiment or an obligation to build a new platform. First prove a safe, portable, economically viable convergence system; other ideas stay discoverable and deliberately deferred.

## Now — active research priorities

| Priority | Research theme | Current questions | Next evidence deliverable |
|---|---|---|---|
| P0-A | Convergence-first autonomous development | How can AI workers receive authoritative, integration-aware packets before writing? | Work-packet schema, readiness/permission distinction, stale-version decision oracle |
| P0-B | Controller and protected mainline | Can parallel agents contribute without race/lost updates/false QA? | Actual merge queue/source-level enforcement mapping; synthetic replay and adversarial tests |
| P0-C | Cross-domain Convergence Contract | Can one portable contract support software, research, learning and collectively accepted outcomes? | Typed authority/evidence schemas, domain adapter boundaries |
| P0-D | AI workforce authority + human oversight | How much execution, repair and orchestration can be autonomous safely? | Delegation event schema, identity/grant proof, action-time controls |
| P0-E | End-to-end full-stack agent study | Does solo, small, studio, or adaptive AI workforce ship more verified product per full cost? | Preregistered matched benchmark method and independent QA rubric |
| P0-F | Evidence-driven improvement | Can agents learn from bugs, queues, releases and costs without gaming the metrics? | Replayable learning/decision traces and rollback policy |
| P0-G | Experiments → GitHub evidence → evergreen education | Can public reproducible research attract valuable contributions while preserving accuracy and rights? | Experiment Publication Contract and revision-linked claim/content ledgers |

**Priority ordering:** Reliability and authorization invariants first; full-stack team sizing and research-publishing systems are complementary research that should not delay essential convergence validation. All remain research-only unless separately approved.

## Later — Future Topics / Points of Research

These are **parking-lot research opportunities**. Entry here is not a task assignment, implementation permission, funding approval, active initiative or guarantee of demand.

| Parking ID | Topic | Key questions to explore later | Trigger to revisit | Status |
|---|---|---|---|---|
| FUT-RD-CYBER-001 | **AI-native cybersecurity and collective security operations** | Can permissioned AI workers assist with asset discovery, defensive telemetry, SIEM/SOAR integration, anomaly triage, vulnerability prioritization, secure-by-design development, incident response and evidence-bound human escalation? How do we avoid hallucinated incidents, surveillance creep, private-data leakage and agent privilege escalation? | Foundational task/authority/evidence model reviewed; separate threat model, consent/privacy and research scope approved | **Deferred — no investigation or build authorized** |
| FUT-RD-IDENTITY-002 | Portable identity and capability attestations | How can contributors prove appropriate capabilities while retaining pseudonymity, privacy and revocation? | Cross-domain identity/rights requirements and threat review complete | Deferred |
| FUT-RD-FEDERATION-003 | Federated independent collective coordination | Can independently governed communities exchange tasks/results without centralized ownership? | Contract semantics and cross-boundary permissions proven | Deferred |
| FUT-RD-ECONOMICS-004 | Fair contribution incentives and sustainability | How should labor, attribution, maintainer support, compute costs and value distribution be governed without speculative token incentives? | Genuine participation needs and legal/ownership research | Deferred |
| FUT-RD-ACCESS-005 | Inclusive offline and low-bandwidth AINO | Can older models, inexpensive hardware and unreliable connectivity join safely? | Worker handoff and fencing demonstrations designed | Deferred |
| FUT-RD-EDU-006 | Multilingual collective learning and edutainment | How can open knowledge be translated, locally reviewed and made reusable with factual corrections? | Research provenance and publication controls defined | Deferred |
| FUT-RD-RESILIENCE-007 | Supply-chain and service resilience | How can AINOs keep operating during provider, network, or dependency outages without false completion? | Service recovery and scoped authority evaluation | Deferred |

### Cybersecurity parking-lot boundaries

**Intent:** defensive AI-native security research potentially spanning developer supply-chain checks, secure integration, audit, SIEM data intake and alert analysis, human-authorized containment, tenant privacy and community cyber hygiene. The existing convergence security gates **remain active non-negotiable safeguards**; deferring this *separate expanded cybersecurity R&D track* does not defer baseline safety, identity/permission checks or threat modeling for the convergence system.

**When revisited, begin with:**
1. What security needs are actually shared by independently operated collectives rather than a single business?
2. Which mature open-source tools, standards and managed services already solve portions of defensive telemetry, analysis and response?
3. What information may cross project boundaries, and how can raw alerts/PII remain protected?
4. Which AI judgments are only recommendations; which incident actions require deterministic enforcement/human approval?
5. How are true/false positives, time to detect/respond, reviewer workload and privacy failures independently evaluated?
6. What safe, synthetic test fixtures establish competence without using real credentials, live targets or unauthorized scanning?

**Do not start research spikes, integrate IE cybersecurity ideas, create real security collectors, access live security data, scan targets, or commit to vendors under this parking-lot item.** No claim of current Foromni security-service capabilities is made.

## Adding future ideas without derailing current priorities

Every new proposed topic should have: a unique provisional parking ID, one-sentence beneficiary/problem, 3–6 research questions, scope exclusions, dependency/trigger, evidence needed to graduate, and current **deferred** state. A human/maintainer must approve promotion to active research and reconcile it with the canonical task registry.

**Graduation:** deferred → proposed study → scoped/approved study → sourced review → experiment design → separately authorized experiment → independently assessed findings → possible implementation proposal. No topic graduates merely because it is exciting, or because a related organization is building it.

**Avoid duplicate work:** Before promoting any entry, compare it with the current mainline roadmap and all pending roadmap PRs. The existing draft `roadmap/tasks.json` includes FOR-001 through FOR-006; no new canonical task is created by this index.

## Next specific research action

Complete the **Convergence Packet Freshness & Decision Rules** study and a formal machine-readable contract that separates:
- facts observed from Git and issue tracking,
- scoped grant/revocation/lease authority,
- agent-proposed remedies,
- independent QA verdict,
- protected mainline integration,
- downstream release/outcome evidence.

Then choose the smallest honest synthetic trial to test whether the convergence-first packet reduces integration rework relative to ordinary task prompts. **No pilot has been authorized or run.**

*Build today, so others can enjoy tomorrow.*
