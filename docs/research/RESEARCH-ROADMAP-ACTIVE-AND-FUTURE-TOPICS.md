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

## Sequencing decision — full-stack first, handoff protocol next (2026-11-21)

**Current focus:** Finish the end-to-end full-stack development research and the fixed benchmark design before opening a separate agent-to-agent communication/orchestration research workstream. This includes objective → specifications → frontend/backend/auth/database → independent QA → convergence → staging/release boundaries → evidence and costs.

**Study in tandem, narrowly:** Identify only the **minimum handoff and synchronization fields necessary to make the current full-stack reference workflow technically coherent** (task ID/revision, dependency/interface version, source SHA, authenticated worker/grant, candidate/evidence references, and stale-packet recovery). Record unknowns as research questions, not as permission to design or deploy a complete communication platform.

**Next dedicated topic after the full-stack research exit gates:** `NEXT-RD-AGENT-HANDOFF-001` — **Agent-to-agent communication, durable memory, delegation, worker replacement, and synchronization protocol.** Compare portable standards and existing orchestration systems only after the full-stack benchmark identifies the actual handoff failures and functional needs. Research should first determine whether a thin adapter to existing queues/events is sufficient; avoid designing a new universal protocol by assumption.

**Promotion trigger:** The reference app, acceptance oracle, risk/authority boundaries, dependency/revision decisions, hosting comparisons, and fair 1/3/8/adaptive experiment protocol are independently reviewable, with known gaps and a defensible proposed experimental authorization scope. Later implementation/experimentation still needs separate authorization.

**Prioritization rule:** The next-topic record is neither an active independent study nor a canonical task registry entry; it is a sequencing marker. Do not redirect effort from current convergence/full-stack questions, and do not treat any Internet Embassy work as Foromni authorization or shared implementation.

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

### Future subtopic: deployment-stage prompt-injection security gate

**Parking ID:** `FUT-RD-CYBER-PI-002` — *AI prompt-injection defenses and deployment acceptance*. This is a **deferred focused investigation under** `FUT-RD-CYBER-001`, not a duplicate canonical task and not an active security product initiative.

When the separate cybersecurity track is authorized, evaluate direct and indirect prompt-injection threat models for autonomous agents consuming repository files, PR comments, tickets, logs, web content, retrieved knowledge, tool responses and inter-agent messages. Research a dedicated **predeployment security admission gate** that assesses untrusted-content boundaries, action-time tool permissions, provenance and delegated authority, data exfiltration controls, and adversarial evaluation. Include deployment-blocking conditions, evaluator independence, regression tests and continuous post-release monitoring.

**Current P0 overlap (narrow and necessary):** The ongoing full-stack experiment pipeline must treat untrusted instructions as data and prevent them from becoming grants, instructions for a privileged worker, QA approvals or release authority. Document a minimal planned security gate and synthetic negative fixtures; do not launch dedicated cybersecurity R&D, real red-team operations or a live deployment under this item.

**Research sources to review on future promotion:** OWASP LLM01:2025 (https://genai.owasp.org/llmrisk/llm01-prompt-injection/), OWASP LLM Prompt Injection Prevention Cheat Sheet (https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html), NIST AI 100-2e2025 (https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf). No mitigation is complete on its own; prompt-based instructions and model-based scanners are not authorization boundaries.

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
