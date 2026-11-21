# E0a Reviewer Handoff — Evidence Schema and Freeze Gate v0.1

**Status:** Research proposal for a future reviewer. No independent approval, coding-agent execution, QA test, integration or deployment performed.  
**Date:** 2026-11-21. **Scope:** Foromni only. IE RRM and private cross-project research are entirely separate.

## New concrete deliverable

`docs/research/contracts/e0-evidence-envelope.schema.json` is a *machine-readable draft JSON Schema* for the one-agent candidate evaluation evidence envelope. It provides explicit fields and allowed grade categories for source provenance, reviewer identity, case execution, effective authorization, all-cost reporting and integration status. **This is not a validated attestation or runnable evaluator.** A JSON Schema can check structure but cannot prove that an agent, Git source, test runner, reviewer or cost value is trustworthy.

### Required trusted checks outside JSON Schema

1. **Source validity:** independent observer verifies base/candidate/evaluated SHAs on real Git objects, and source checkout is clean; `evaluated_sha === candidate_sha` for candidate verdict. A candidate SHA must not be substituted with model-generated text.
2. **Reviewer separation:** evaluator principal and its actual permission boundary differ from coding worker; hidden fixtures and report store cannot be written by worker.
3. **Execution reality:** required tests actually ran under the evaluator's runtime, not merely logged a PASS string. Case status and nonzero positive/negative expected/executed counts match independently protected test inventory.
4. **No false PASS:** only `VERIFIED_ACCEPTED_FOR_CANDIDATE` when all required positive/negative and security cases passed, no unknown critical events, trial authorization verified, source digests current and reviewer authenticated. Reject even structurally valid false claims.
5. **Financial truth:** `costs.total_amount` is computed from full retained receipts and ledger, not agent estimates; `partial`/ `unknown` results are not silently compared as zero cost.
6. **Side effects:** `integration.status=integrated_verified` requires independent observed real integration SHA and separately permitted integration. E0a should normally remain `candidate_only` and `deployment_status=not_authorized`.
7. **Retention:** evidence references are content-addressed or otherwise integrity-protected, redacted, access-controlled and retained under a versioned policy. Raw prompts, tokens and private customer data should not be embedded.

**Schema refinement required before approval:** add version-pinned formal consistency rules or deterministic reviewer-side checks for cross-field constraints and grade precedence, declare how to handle retries/multiple attempted candidates, confirm timestamps and currency, and independently validate the JSON schema itself once a test run is authorized. The source SHA pattern currently targets 40-hex Git SHA-1 IDs; if a repo uses another object format, update and re-review rather than silently truncating.

## Reviewer sign-off sequence (six gate bundles)

| Gate | Required decision | Proposed owner/authority | Current evidence |
|---|---|---|---|
| REV-A | Exact synthetic auth Mode A vs B, login/logout, cookie/Origin/CSRF/expiry test contract | Independent security reviewer + founder | Candidate v0.7 only, no approval |
| REV-B | Precisely twelve supported business routes and excluded destructive/role-change endpoints | Product requirements reviewer | Candidate v0.7 only, no approval |
| REV-C | Invitation errors, privacy and concurrent token-consumption rules | Security and contract reviewer | Candidate, one leakage decision open |
| REV-D | Cursor snapshot policy, permission revocation and entity-version semantics | API/data reviewer | Candidate, technical algorithm not pinned |
| REV-E | Test expected/executed/grade precedence, holdout source custody | Independent evaluator owner | New schema + prose, not verified |
| REV-F | One-agent E0a candidate-only trial, real host/runtime/secret constraints, cost/stop horizon | Founder/operator | No bounded execution authorization |

**Exit criterion for paper review:** each gate has a recorded reviewer identity, explicit `APPROVE|REVISE|REJECT` with rationale, full accepted contract SHA and a no-hidden-requirements statement. Do not claim self-review as independent.

## Proposed stop conditions for future E0a

Stop and record an incomplete/blocked attempt if the worker can read/modify evaluator oracle or credentials, writes to current Foromni main, touches IE/real data, bypasses source grants, changes accepted requirements, exceeds an approved budget or retry cap, or encounters an unknown critical external write. A trial requires actual approved identity/network boundaries, even when all data is synthetic.

## Why this is a meaningful next step

The schema makes it possible for a reviewer to reject a trial result that omits source provenance, execution counts, cost completeness, or reviewer identity **before** deciding whether the observed outcome is valid. It reduces discretionary interpretation while protecting the distinction between verified candidate behavior and real integration. It is a validation contract, not a new orchestration engine.

## What we can and cannot conclude today

- **Grounded:** E0 v0.7 now has a documented independent-review docket and a proposed machine-readable evidence shape.
- **Not grounded:** an independent reviewer approved the contract; the schema has been loaded by a validator; a coding agent or evaluator was run; a Git main branch was protected; E0a passed; Foromni organizational improvements have been demonstrated empirically.
- **Decision:** E0a remains `NOT READY FOR EXECUTION`. The blocker is no longer only unclear wording: it is obtaining a real reviewer, a fixed authorized runtime, a protected evidence path, and scope/budget permission.

*Build today, so others can enjoy tomorrow.* ❤️🐂
