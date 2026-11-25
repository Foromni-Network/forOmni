# Foromni — AI Security Engineering Career and Research Portfolio Track v0.1

**Research proposal | 2026-11-25 | Foromni only.** Inspired by founder-supplied AI cybersecurity career transcription, commentary and the founder's preference to pursue CompTIA A+, Security+ and CySA+. This is a research and learning plan; not a claim of certification, employment, executed tests, accredited training, or authorization to probe systems.

## Strategic position

Use **foundations + formal credentials + safe hands-on engineering + public reproducible evidence**. The six-month framing is a stretch goal, not a promise of job-readiness. Actual hiring outcomes depend on prior knowledge, experience, market conditions and demonstrable ability. Avoid claiming credentials guarantee employment or that a portfolio replaces hiring requirements.

The technical opportunity for Foromni is to make its agent communication, credential isolation, evidence custody, license-safe update exchange and supply-chain boundaries a series of independently reproducible **defensive security engineering studies**, not self-rated security badges.

## Parallel pathways

| Credential/study | Core purpose | Practical Foromni artifact | Relationship |
|---|---|---|---|
| CompTIA A+ | Systems, OS, troubleshooting, networks, device/process administration | Linux process, users, file-descriptor and network lab; show permitted/denied behavior | Foundation; useful where needed for role screening |
| CompTIA Security+ | Security concepts, identity, secure architecture, incident response, basic cryptography, risk | Risk register, least-privilege grant matrix, security event map, mock detection rule | Foundational security credential |
| CompTIA CySA+ | Detection, threat/vulnerability analysis, SIEM/incident handling | Structured gateway denial logs, detections with false positive/negative evaluation and incident evidence timeline | Applied analyst/defensive qualification |
| OWASP LLM and Agentic Security | Prompt injection, tool misuse, excessive agency, data disclosure, unsafe output | Isolated synthetic agent tool-call injection evaluation, before/after security fixes | AI-specific engineering specialty |
| OWASP MCP Security | Tool poisoning, untrusted descriptions and response content, server/connector trust, overprivileged operations | MCP broker/capability tests with mandatory mediation and separate credential custody | Agent integration specialty |
| AI supply chain and secure DevOps | Dependencies, source provenance, SBOM, release signing, confidential data handling | Signed source-bound update manifest; package dependency/SBOM and license checks | Bridges cybersecurity and AINO licensing R&D |
| Automated incident response and threat hunting | Logs, behavioral detection, triage, recovery, red-team regression | Synthetic attack/defense corpus, alerts, containment, audit receipts | Applied portfolio evidence |
| Optional advanced theory | Privacy-preserving computation, adversarial ML, model evaluation, reverse engineering | Carefully bounded research notes and synthetic experiments | After core operational controls |

**Credential order:** A+ → Security+ → CySA+ is a reasonable preference but does not have to be rigid. Validate current CompTIA exam series, objectives, costs and prerequisite recommendations on official CompTIA sites before enrollment: https://www.comptia.org/en-us/certifications/a/ ; https://www.comptia.org/en-us/certifications/security/ ; https://www.comptia.org/en-us/certifications/cybersecurity-analyst/ . This document does **not** assert specific current exam codes or prices.

## Six-month illustrative plan (flexible, not a guaranteed outcome)

1. **Month 1:** Linux/process/network basics; A+ objectives where needed; capture traffic on owned lab; explain socket vs proxy; run EXP-12/13 evidence reproducibly.
2. **Month 2:** Security+ fundamentals: permissions, cryptography, IAM, web auth, OWASP LLM risk mapping; write and test a small deny-by-default tool gateway.
3. **Month 3:** MCP / connectors and service identities: distinct Unix principals, access grants, issuer trust, credential storage, inter-process messaging; reproduce EXP-9/10/11 limits without claiming full sandbox security.
4. **Month 4:** Detection/SIEM and CySA+ content: build durable audit records, alert logic, false-positive checks, response runbooks and after-action reports from adversarial synthetic events.
5. **Month 5:** Agent security and AI supply chain: inert prompt-injection/tool-poisoning fixtures with actual LLM behavior only in approved contained labs; secure dependency provenance, signed release metadata, license/SBOM scans; no real IE code or secrets.
6. **Month 6:** Capstone: end-to-end worker → broker → mock provider → independent evaluator → signed release/rollback. Publish verified non-sensitive write-up, exact version/commands, mitigations and disclosed limits. Consider responsible disclosure only for real in-scope findings after maintainer coordination.

## Distinguish what has been observed

Research reports EXP-7–EXP-17 describe repeated local synthetic experiments and documented negative cases. **Do not turn their test pass counts into independent security assurance.** Important gaps remain: truly independent QA, provider secret custody, cross-host network egress confinement, live MCP semantics, revocation during external effects, input provenance, real signing authority and actual legal code-contribution permissions.

## Portfolio quality gate (publishable case studies)

Each item should include:
- Threat model and legitimate task; explicit authorization scope and owned environment.
- Reproducible baseline including code, exact version/source hash, local commands, logs and actual observed outcomes.
- A demonstrated negative control (vulnerability) and secure modification, followed by independently reproducible regression tests.
- Source/evaluator boundary and who has signing/credential authority.
- Distinction between application-layer guard and mandatory host-enforced boundary.
- Limits, remaining risks, impact level and no unverified claims of industry credential, production security or CVE.
- Sanitized mock data with no production credentials, identifying user data or raw malicious payload shared irresponsibly.

## Candidate portfolio projects, ordered by current research leverage

**SEC-PORT-01** Credential isolation and confined worker: combine safe synthetic known failures from EXP-10–15; prove explicit Unix resource mediation; document inherited FD and public Unix proxy holes.

**SEC-PORT-02** Durable idempotent orchestration: webhook, cron, SQLite task ledger, provider post-effect crash ambiguity; show duplicate-effect negative control, then restore safe idempotency/review.

**SEC-PORT-03** Agent / MCP tool poisoning: mock tool metadata and simulated tool outputs with inert malicious requests; compare authority checks before/after defensive mediation; don't conflate string rejection with evaluated LLM resistance.

**SEC-PORT-04** AI security logging and detection: collect denied tool calls, invalid grants, replay, high-cost anomalies and cross-project attempts into structured events; test detection true/false positive counts and triage.

**SEC-PORT-05** Source supply chain and update exchange: license provenance, source-bound release, private AINO module separation, dependency/SBOM/secret scanning, explicit import authorization and rollback; no actual IE import until approved.

**SEC-PORT-06** Capstone end-to-end agency release: independent reviewer verifies source and QA before human approval; real bounded task with measured cost. No protected-main merge without authorization.

## What to measure

- Unauthorized provider **effects** (not just rejected request count).
- False approvals, successful replay after crash/restart and zero-cost bypass attempts.
- Detection precision/recall on held-out attack/normal synthetic cases.
- Legitimate tasks accepted end-to-end and time-to-recovery.
- Full true costs (API, tests, retries, human review), not just token charges.
- Evidence quality score: exact SHA, reproduction, independent observer and clear limitation.

## Curriculum sources to consult

- OWASP LLM Top 10: https://owasp.org/projects/top-10-for-large-language-model-applications
- OWASP MCP Top 10: https://owasp.org/projects/mcp-top-10
- OWASP Agentic Application Top 10 and GenAI security: https://genai.owasp.org/
- CompTIA official certification pages as above.
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework

**Next step:** preserve this as a new research and career development track; run a small pre-registered SEC-PORT-04 detection experiment on previously captured *synthetic* broker events. No broad attack tooling, external probing, credential purchase or production integration is authorized by this note.
