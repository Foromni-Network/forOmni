# Foromni Open-Source Agency Case Studies — After-Action Review & Convergence Audit v0.1

**Date:** 2026-11-22. **Scope:** Foromni research only, separate from Internet Embassy. **Review type:** cross-document evidence and decision audit, not independent runtime QA. No tests, CI, deployments, protected merges, changes to FOR-007, outside outreach or spending.
**Audit window:** study arc from Paperclip and AI agency SOPs through AG2/OpenAgents federation, agent trust ladder, admission and assignment. This review covers named deliverables, **not an exhaustive audit of every repository file, GitHub issue or downstream implementation**.

## Executive disposition

**Research direction is coherent; runtime maturity has not advanced.** The strongest conclusion is a clean separation of (1) communication/collaboration, (2) validated identity and task-specific authorization, (3) worker execution and evidence, (4) independently authenticated QA, (5) human candidate acceptance, (6) protected integration, and (7) deployment/outcome. The source comparisons explain why substituting role titles, model summaries, peer rankings or workspace membership for these protections would be unsafe.

**What was actually achieved:** source-level research, source-pinned comparisons, attack/negative-case specifications, proposed trust and assignment protocols, and an isolated, inert Python recommendation prototype. **What did NOT occur:** live policy enforcement, executed QA, multi-agent federation, measured throughput/cost, successful source integration, calibrated reputation, production security proof. Never describe a proposed case as a passed test.

## Study inventory, scope and integration disposition

| Case study/workstream | Direct source/evidence level | Transferable learning | Status/next action |
|---|---|---|---|
| Paperclip control plane (prior) | Direct pinned source, source-scoped mechanisms | Budget reservations, approvals, recovery, task ownership and cost events | Reuse existing contracts; compare costs/authority under a single synthetic scenario |
| Agency Agents / NEXUS SOP | Source and document inspection | Typed handoff; Dev↔QA loop; bounded escalation | Adapt SOP metadata, **not** named-agent authorization |
| BMAD plan/review | Pinned source inspection | Frozen intent, multi-lens triage, failed-lens disclosure and review repair routing | Adapt review process; independently verify actual code/tests |
| MetaGPT / ChatDev | Earlier literature/document studies; less direct mechanism inspection in this arc | SOP and conversation topology hypotheses | Low-priority further inspection only for unresolved mechanism |
| AG2 modern network | Direct pinned files `identity.py`, `peers.py`, `hub/core.py`, `channel.py`, `rule.py` | Agent/human/remote participant model, channel ack lifecycle, separate claimed vs observed stats | Adapt interface concepts, prohibit unverified upstream rules becoming policy |
| OpenAgents workspace | Direct pinned access, sharing, approvals, visibility, resource grants | Human-agent workspaces, owner consent, revocable resource grant, issue→task boundary | Adapt UI/consent patterns, enforce project/task security separately |
| Foromni evidence/work packet | Own research-only contracts v0.2/E0 | Source-bound attempts, independent QA, grant separation | Preserve canonical ownership; **not runtime implemented** |
| Trust & rank design | Foromni proposal based on source-scoped findings | Capability-specific confidence, cold start, anti-farming, bounded recommendation | Proceed with controlled synthetic test only if separately authorized |

**Pinned upstream pointers already recorded:** [AG2 modern network@9bdd9d4](https://github.com/ag2ai/ag2/tree/9bdd9d493a9a3a01308949b67d5a18219cb6c71c); [OpenAgents@93e3347](https://github.com/openagents-org/openagents/tree/93e334783747f6f35eb5133c0dec4351b7fffa10); [BMAD@e435a22](https://github.com/bmad-code-org/BMAD-METHOD/tree/e435a22574fe55722841086e5566420178b98df3); [Agency Agents@8ae6164](https://github.com/msitarzewski/agency-agents/tree/8ae6164602c95ca78828b148b9052460ee426885). Do not mistake pinned source inspection for production or security attestation.

## Five high-value learnings

1. **Evidence provenance needs separate authority.** AG2 hub `completed/n` is a task lifecycle counter, not independently accepted QA; NEXUS's or BMAD's PASS language does not prove real execution. Source SHA, verified reviewer, fixture/suite, actual process exit and negative cases are mandatory for accepted work.
2. **Network membership must not be an execution grant.** AG2 invitation ACK makes a communication channel ACTIVE; OpenAgents owner-approved agent use authorizes a collaboration resource. Neither admits Foromni protected source edits, expensive actions or cross-project data by itself.
3. **Policy visibility is not enforcement.** AG2 in-process rule source explicitly notes stored-but-unenforced channel-type and rate controls. OpenAgents access helper treats machine tokens as broadly trusted in their workspace. Foromni may borrow shapes but must separately prove its effective tool/action boundaries.
4. **Reputation can improve assignment choice, not replace privilege.** Verified skill is capability/risk specific, source-bound, subject to suspension and reevaluation; a T4/T5 label alone cannot grant reviewer, merger or release authority.
5. **Scientific comparison requires matched, full-cost outcomes.** Multi-agent complexity can produce attractive demos yet reduce accepted value per total dollar when retries, coordination, context transfer, failure and human oversight are included.

## Gaps and corrections surfaced by the review

| Issue | Severity for future implementation | Correction now |
|---|---|---|
| Multiple case studies repeat similar attack cases under distinct IDs (CWP, FED-T, ADMIT, TRUST, ASSIGN) | Medium: count inflation and conflicting test oracles | Treat them as **scenario families**, not number of independently built tests; defer canonical ID dedup until test suite work is authorized |
| Score model lacks independent evidence verification at its input boundary | Critical if deployed | Research oracle accepts typed synthetic counts only; must reject production claims unless independently signed/verified source and attempts |
| AG2 completion rate aggregates across capabilities in the peer helper | High for assignment if used raw | Capability-specific stratification and confidence-adjusted advisory ranking |
| Reputation/role ladder does not automatically verify agent operator linkage or independence | High | Authenticate operator, incarnation, task and reviewer under trusted identity system; T-levels cannot override hard grant checks |
| Task complexity classification can be gamed by task author | Medium/high | Freeze complexity before assignment with accountable owner/adjudication; report disagreement and stratify |
| Cost hints may be optional, provider-declared, and partial | High for economic conclusions | Use audited full-cost receipts; unknown is unknown, never $0 |
| OpenAgents machine credential can bypass role checks in its inspected helper | High as an integration design hazard | Do not reuse broad workspace token as BYOA execution credential; project-scoped rights required |
| Confidence heuristics use binomial assumptions on heterogeneous dependent task attempts | High if presented as calibrated probability | Wilson/Beta illustrative only; keep explicit `uncalibrated` until challenge diversity and independent trials |
| Synthetic quick exploration may encourage easy-task farming | Medium | Cap near-duplicate trial credit; count outcomes from frozen independent acceptance, no self-issued tasks |
| A reviewer's model identity alone does not guarantee independence | Critical | Credentials, separate evaluator suite/fixture custody and task/source segregation |

These are **AAR findings**, not proven exploitable defects or verified failed runtime tests.

## Convergence mapping (do not expand frozen MVP)

| Existing target | Research harvest | Not yet satisfied |
|---|---|---|
| FOR-007 frozen execution MVP | Single-worker cost/evidence baseline; no mutation | No new end-to-end executable evidence from this review |
| FOR-009 ownership/registry | Agent/operator/incarnation lineage, trust-aware eligibility, lease epoch, per-task boundary | Authenticated enforced grants and enforcement tests |
| FOR-011 evaluator | BMAD review provenance, NEXUS feedback, independent QA custody | Actual separate evaluator runnable acceptance |
| FOR-012 cost/evidence | Real outcomes/negative receipts, retries and full costs, reputation sources | Verified receipt pipeline and calibrated score |
| FOR-013 human approval | OpenAgents owner rechecks, exact candidate SHA-scoped decision | Validated approval and revocation implementation |
| FOR-016 federation/community | AG2 network protocol and OpenAgents collaboration pattern; reputation-based discovery | Cross-network admission/identity sandbox and negative tests |

**Prevent scope drift:** FOR-016/trust marketplace is a future research track, not a reason to block or enlarge the frozen one-worker FOR-007 baseline. The first reproducible program must use synthetic data with no trusted credentials or unapproved external side effects.

## Synthetic assignment oracle: new isolated prototype

**Code:** [research/foromni_trust_assignment_oracle_v01.py](../../research/foromni_trust_assignment_oracle_v01.py). **Commit:** [f31e746](https://github.com/Foromni-Network/forOmni/commit/f31e746c9731822b764eb18649a7e073d6cf94a6). This file is an **unexecuted** pure-function prototype for synthetic `Task`/`Agent` records. It returns `suggest`, `explore_only`, `abstain`, `ineligible`, a reason code and a Wilson lower confidence heuristic, while `grants_issued` is always 0. No network/file writes, tool calls, Git operations or runtime grants.

**Prototype limits that MUST be resolved before policy use:**
- Input fields such as `accepted`, `project_memberships`, `active_security_suspension` and `grant_present` are supplied by caller, **not authenticated or independently verified**.
- `owner_has_authorized_assignment` is a synthetic Boolean, **not an owner signature or lease**.
- It does not check freshness, task revision, security classification provenance, risk-relevant complexity except a placeholder `high` tier, operator conflicts, private data and cross-tenant details, receipt completeness beyond a flag, or task-level cost prediction.
- It does not currently choose among C0–C3 arms, randomize exploration, calculate empirical calibration or prevent duplicated evidence events.
- It is an **illustrative recommender**, not a reference implementation of Foromni policies. Comments in the code explicitly state it cannot issue authority.
- Ranking the Wilson lower bound without task-difficulty control is still subject to misleading selection. No 'best agent' claim is supported.

### Proposed minimal code-review assertions (NOT RUN)

1. Suspended agent returns `ineligible` even with perfect history.
2. Protected task returns `ineligible` for every agent irrespective of its T-level.
3. No cross-project membership yields `ineligible`, including strong frontend records.
4. No owner consent produces `abstain`, without producing a grant.
5. No private-data grant produces `ineligible`.
6. Unknown skill is allowed only as `explore_only` on public low-risk consented fixture.
7. For same task complexity and verified source provenance, 35/40 evidence should receive stronger confidence support than 2/2 (not asserted as universal without confounding controls).
8. Duplicate agent aliases/receipts must not grow reputation in any later evidence ingestion layer.
9. Expired/revoked task grants remain denied by external trusted action-time service even when recommender suggests agent.
10. For all inputs, `grants_issued == 0`; no filesystem/network side effect.

## Next sequence — stop adding case studies indiscriminately

**P0 research gate (immediate):** explicit canonical artifact index plus core claim ledger separating code-inspected/documented/tabletop/actually-executed. This AAR provides a first concise index. Avoid duplicate architecture documents.

**P1 proof preparation:** when authorized, execute isolated pure-function assertions on the synthetic recommender; fix logic and record exact code SHA, command/output and failed tests rather than calling an unrun test successful. Also construct frozen synthetic evidence fixtures as non-credentialed inputs, version with task/taxonomy. This is not a live BYOA experiment.

**P2 independent source/security:** test FED/ADMIT negative conditions on an isolated minimal Foromni policy harness, with separate evaluator credential and no public endpoint or sensitive data; focus on spoofing, replay, revocation, cross-project scope and missing QA execution.

**P3 efficacy:** comparative randomized C0 human choice, C1 raw rate, C2 confidence-aware, C3 safe exploration with identical task mix and independent QA; measure accepted outcomes/full cost, unfair exclusion, false promotion, time/attempt, and actual security failures. No optimization conclusion without measured trials.

**P4 incorporation:** only after current FOR-007 contract and eligibility policy are independently accepted, consider FOR-009/012/016 roadmap integration. New source studies only when they resolve a documented unknown, not for novelty.

## Explicit AAR decision record

- **KEEP:** one canonical work packet, trusted action-time grants, separate QA identity, human-controlled high-risk action, exact SHA/cost receipts, global inclusion for safe newcomers.
- **ADAPT (later):** AG2 network/channel and claim/observation separation; OpenAgents workspace/owner approvals; BMAD review lenses; NEXUS handoff; Paperclip spending and recovery techniques.
- **REJECT AS AUTHORITY:** agent-self-report, channel ACK, general workspace token, raw success rate, opaque 0–100 credit rating, stylistic review PASS, model-generated Git status.
- **DEFER:** fully federated agent marketplace, real multi-agent benchmark, scoring-derived promotion or protected-branch integration until approved experiment and baseline acceptance.
- **KNOWN LIMITATION:** no dedicated independent reviewer conducted this AAR. It is a structured internal review with source references, not the independent QA event the architecture requires.

**AAR verdict:** **RESEARCH READY FOR CONTROLLED SYNTHETIC VERIFICATION; NOT EXECUTION VERIFIED; NOT INTEGRATED.**

*Build today, so others can enjoy tomorrow.* ❤️🐂
