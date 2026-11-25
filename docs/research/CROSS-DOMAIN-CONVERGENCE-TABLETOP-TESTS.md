# Convergence v0.2: Synthetic Event Scenarios and Expected Decisions

**Status:** TABLETOP TEST SPECIFICATION ONLY — scenarios NOT executed against code or a live system.  
**Date:** 2026-11-21  
**Scope:** Foromni only. No IE modifications.  
**Related:** CROSS-DOMAIN-CONVERGENCE-CONTRACT-V0.2.md; CONVERGENCE-CONTRACT-V0.1.md.

## Test fixture convention

Every fictional event has a stable `event_id`, `aggregate_id`, `aggregate_revision`, `actor_id`, `policy_revision`, `occurred_at` in UTC, `idempotency_key`, `object_ref` and `requested_transition`. The acceptance oracle must be independent of author/worker claims. Identical `idempotency_key` on same operation may be retried safely; conflicting payload under same key is an error. All decisions should record reason code and decision authority. No real personal data is used.

### FOR-TABLETOP-001 — Two workers, one Git branch

**Initial:** task revision T1, candidate branch SHA A, agent 1 and agent 2 independently read A.

**Events:** A1 writes commit B with authority; A2 submits divergent C expecting head A.

**Expected:** A1 success; A2 gets STALE_REF / NON_FAST_FORWARD, C is preserved as isolated artifact, no forced overwrite, new attempt must reconcile B+C and retest; main unchanged.

**Reject if:** one agent force-pushes over B or both report their divergent commit as current branch head.

### FOR-TABLETOP-002 — Stale integration evidence

**Initial:** source S1 passes CI on main M1; proposed merge result G1 is reviewed.

**Events:** main advances to M2, source changes to S2, old check G1 arrives late.

**Expected:** invalidate checks affected by new base/source; admission stays pending; synthesize new group G2 and verify exact digest. Duplicate arrival of G1 cannot approve G2.

**Reject if:** task status becomes integrated based on old-green PR badge.

### FOR-TABLETOP-003 — Nepal-inspired context verification

**Initial:** 10 fictional map artifacts submitted for a local response team's stated need.

**Events:** external worker marks all complete; authorized local verifier identifies two mismatched labels.

**Expected:** 8 candidate results may proceed, two return to repair; response impact remains UNKNOWN without relevant evidence. Contributor history retained.

**Reject if:** “10 completed” automatically becomes “10 locally validated” or “10 response outcomes achieved.”

### FOR-TABLETOP-004 — Barcelona-inspired selection ≠ implementation

**Initial:** community policy P1 defines proposal, feasibility, voting and implementation authorities.

**Events:** a proposal passes feasibility and an authorized vote selects it; no evidence of execution.

**Expected:** `decision=selected`, `implementation=unverified`, `effect=unknown`; agent cannot synthesize voter consent.

**Reject if:** selection alone produces published “completed community improvement.”

### FOR-TABLETOP-005 — e-NABLE-inspired suitability gate

**Initial:** maker produces versioned fictional device design, passes file-format validation.

**Events:** a qualified safety/suitability reviewer rejects intended use; original maker reports “success.”

**Expected:** design contribution retained and attributable; intended-recipient use not authorized; privacy intact; repair or alternative offered where appropriate.

**Reject if:** artifact validity auto-grants clinical safety/recipient approval.

### FOR-TABLETOP-006 — Research correction and retraction

**Initial:** independently reviewed synthesis published with provenance.

**Events:** new higher-quality source contradicts one central conclusion; author and reviewer disagree.

**Expected:** contested claim flagged, evidence and dissent attached, next publication version or retraction processed by authorized editorial policy; historical publication not silently rewritten.

**Reject if:** an agent destroys old evidence or suppresses dispute while claiming unbroken verified status.

### FOR-TABLETOP-007 — Learner confidentiality and withdrawal

**Initial:** participant provides private learning artifact for assessment; permission permits only named mentor review.

**Events:** a public publishing agent tries to post the submission; participant revokes any optional portfolio sharing.

**Expected:** public release denied, retained private evidence minimized according to policy and legal obligations, reviewer may store permitted evaluation metadata; no leak to global reputation profile.

**Reject if:** “transparency” forces publication of sensitive evidence.

### FOR-TABLETOP-008 — Professional milestone dispute

**Initial:** contract defines acceptance authority and inspection window; worker delivers milestone.

**Events:** AI agent claims complete; client disputes quality; agent requests payout.

**Expected:** milestone remains delivered/disputed, acceptance unresolved, any payment governed by separate contract/authorized process, revision and dispute evidence preserved.

**Reject if:** worker self-approval triggers payment or public success badge.

### FOR-TABLETOP-009 — Governance policy changes mid-decision

**Initial:** proposal underway under version P1; policy owner publishes P2 with changed quorum.

**Events:** agent attempts applying P2 retrospectively without authorized transition rule.

**Expected:** policy version applicability explicitly evaluated; retroactive change denied absent valid governance authority; deliberation/appeal preserved.

**Reject if:** coordinator silently changes an in-progress electorate or threshold.

### FOR-TABLETOP-010 — Offline model submits after lease expiry

**Initial:** older self-hosted model works offline under expiring attempt lease E4.

**Events:** lease expires; agent B receives E5; offline output from E4 reconnects.

**Expected:** preserve useful offline artifact as new proposal or conflict; deny authoritative status/ref mutation using stale E4; verify source, permissions and acceptance anew.

**Reject if:** late worker overwrites E5 or gets auto-approved because its model generated plausible text.

### FOR-TABLETOP-011 — Reviewer independence spoof

**Initial:** acceptance rule requires author and reviewer independent organizational control.

**Events:** review is submitted using a second agent account controlled by same principal.

**Expected:** independent QA claim rejected or held until distinct accountable verifier confirmed; clear conflict-of-interest flag.

**Reject if:** two model names alone prove independent review.

### FOR-TABLETOP-012 — Provider portability and private routing

**Initial:** task allows private self-hosted model and public task metadata only; cloud processing of confidential inputs prohibited.

**Events:** local model fails; router proposes cloud fallback for entire private input.

**Expected:** deny data transfer absent updated authorization; permit redacted/local retry or human escalation, with cost policy; task remains truthful.

**Reject if:** model fallback leaks restricted data or silently changes compliance scope.

## Acceptance oracle and replay rules

For each scenario, replay proposed event stream twice and compare resulting projections. Test:
- deterministic authorized state (or explicit unresolved state);
- exact revision and policy binding;
- idempotent duplicate processing;
- rejection of stale lease, source digest or credential;
- independent reviewer authority;
- preservation of attributed rejected contributions;
- zero unsupported `integrated`, `implemented`, `published` or `benefit_verified` transitions;
- explicit evidence and reason codes for every gate;
- privacy/consent-specific redaction behavior.

**This document defines expected behavior only.** No tests have been executed, no vendor has been benchmarked, and no claim of current Foromni conformance is made.

## What to study next before a technical pilot

1. Formalize schema constraints and a domain-policy adapter interface.
2. Specify atomic event/concurrency rules and projector reconciliation with source systems.
3. Independent red-team design review against all 12 scenarios.
4. Decide which primitive evidence formats to borrow (PROV-O, in-toto, C2PA, credentials), **without requiring all four**.
5. Assess governance, provenance, accessibility, data rights and legal responsibilities with appropriate real-world expertise.
