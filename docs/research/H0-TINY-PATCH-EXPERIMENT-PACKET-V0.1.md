# H0 — Tiny Patch Experiment Packet v0.1 (Proposed; Not Executed)

**Status:** Research-only protocol for later independent review and explicit trial authorization. No app, test runner, model, container or credential has been used.  
**Date:** 2026-11-21. **Scope:** Foromni only.  
**Parent:** HYBRID-AINO-BOTTOM-UP-EXPERIMENTAL-LADDER-V0.1.md and ADR-E0A-002-INDEPENDENT-REVIEWER-CUSTODY-AND-PATCH-ONLY-TRIAL.md.

## Purpose

Test only the **minimum evidence kernel** before involving any external agent framework: can an independent observer reproduce a candidate from a patch against fixed source, and can an independent evaluator accept correct behavior while rejecting incorrect behavior? This is H0, not full-stack E0a, and does not establish multi-agent or AINO superiority.

## 1. Candidate task: deterministic slug normalization

Public specification for a pure Python function named `normalize_slug(value: str) -> str`:

1. Accept only a Python `str`; any other type raises `TypeError`.
2. Supported input characters: ASCII letters A-Z/a-z, ASCII digits 0-9, ASCII space U+0020 and ASCII hyphen U+002D only. Any other code point raises `ValueError`, so Unicode handling is deliberately **not** inferred from this simplistic H0.
3. ASCII uppercase letters lower-case; digits are unchanged.
4. Treat each consecutive run of spaces and hyphens as **one hyphen**; trim leading/trailing hyphen from normalized output.
5. Empty or separator-only input produces the empty string.
6. Function is pure: no network, file I/O, environment secrets, clock, nondeterminism, or external dependencies.

**Public examples** (not a complete grader):

| Input | Expected |
|---|---|
| `"Hello World"` | `"hello-world"` |
| `" --- A  B--- "` | `"a-b"` |
| `"123"` | `"123"` |
| `""` | `""` |
| `"a_b"` | raises ValueError |
| `12` | raises TypeError |

**Worker-facing stub design (not an executed code artifact):**
```python
def normalize_slug(value: str) -> str:
    raise NotImplementedError("H0 worker implementation required")
```

The worker is to modify **only** a local candidate module file supplied in a disposable starter repository. No repository hosting token or evaluator test suite is in the worker runtime. Reviewers may choose a different tiny function before freezing H0; this proposal is not yet an authorized task.

## 2. Separate, mutually exclusive roles

- H: approves objective and allowed resource/time/cost.
- W: implementer, receives public spec and starter source; can output only a patch/diff and usage log.
- S: independently checks the patch against frozen base SHA and creates a clean candidate Git SHA; never trusts a SHA provided by W.
- Q: has separate tests, credentials and evidence store; receives only S's clean candidate source; runs tests and records true processes and exit values.
- P: restricts worker runtime, external API usage, resource limits and actions.

A no-model, hand-coded demonstration can check artifact plumbing once separately authorized, but **cannot** measure an AI worker's competence.

## 3. Pre-registration decisions needed

| Decision | Recommended value | Status |
|---|---|---|
| Public source | Minimal Python function stub, pinned exact Git SHA | NOT PINNED |
| Source control | Local disposable Git repo; worker writes patch only | PROPOSED |
| Interpreter | One pinned Python 3 minor version and environment digest | NOT SELECTED |
| Evaluation | Q-owned Python built-in unittest suite in separate directory | PROPOSED, NOT WRITTEN |
| Public cases | Examples in this document | SPECIFIED |
| Hidden cases | Q authors before worker sees assignment; must use only public behavior | NOT CREATED |
| Independent grader | Separate authenticated principal/process and logs | NOT ESTABLISHED |
| Required negative grader challenge | Deliberately incorrect candidate must NOT receive PASS | SPECIFIED, NOT RUN |
| Limits | Max time, attempts, tool calls, memory/CPU and model cost | NOT APPROVED |
| Data and egress | Synthetic only, no Foromni/IE production data, restricted network | PROPOSED |
| Trial authorization | Written scoped founder consent before any code execution/testing | NOT GIVEN |

## 4. H0 test inventory — expected *types* of checks

| ID | Public behavioral class | Positive / negative |
|---|---|---|
| H0-T01 | Ordinary capitalization and separator runs | Positive |
| H0-T02 | Digits and empty string | Positive |
| H0-T03 | Leading and trailing separators | Positive |
| H0-T04 | Non-string input raises TypeError | Negative |
| H0-T05 | Unsupported underscore, tab and non-ASCII raise ValueError | Negative |
| H0-S01 | Source observer reconstructs candidate against pinned base | Integrity |
| H0-S02 | Altered base or patch cannot inherit previous green verdict | Integrity-negative |
| H0-E01 | Zero-test or forged PASS string rejected | Evaluator-negative |
| H0-E02 | Intentionally faulty candidate rejected with actual test evidence | Evaluator-negative |
| H0-P01 | Worker cannot access Q's holdouts or GitHub main token | Policy-negative |
| H0-C01 | Total time/tool/QA/human/provider cost and retries recorded | Economics |

Hidden fixtures should vary inputs but must not silently add new behavior requirements. No source-level exposure of Q's cases to W. Python built-in unittest can minimize dependency scope; this is a proposal, not proof.

## 5. Expected artifacts and classification

At each authorized attempt, capture:
`trial_id`, public contract revision and SHA, base SHA, patch digest, candidate SHA verified by S, Q evaluator identity, environment/suite digest, expected/executed cases, observed exit code, pass/fail per case, security incidents and full cost (worker + QA + human). Use the existing proposed E0 evidence schema as a starting shape, but H0 should have its own versioned profile to avoid falsely requiring Collective Lab endpoints.

Primary outcomes:
- `VERIFIED_ACCEPTED_FOR_CANDIDATE` only if all required positive and negative H0 tests genuinely run/pass and S/Q source binding is correct;
- `VERIFIED_REJECTED` for actual behavioral failures;
- `NO_TEST_EXECUTION`, `STALE_EVIDENCE`, `INVALID_PATCH`, `INFRA_ERROR`, `UNKNOWN_OR_AMBIGUOUS`, `SECURITY_BLOCKED`, `INCOMPLETE` as appropriate; retain all incidental reason tags.

## 6. Bottleneck ledger format

| Field | Meaning |
|---|---|
| `bottleneck_id` | Stable research defect identifier, not new product feature ID |
| `phase` | H0/H1/… and versioned comparison baseline |
| `failure_class` | SOURCE, GRADING, AUTHORITY, COST, etc. |
| `observed_evidence_ref` | Independent actual evidence URI/hash |
| `minimal_reproduction` | Smallest input+source+environment that showed issue |
| `cost_of_failure` | Lost worker/QA/reviewer time and direct money |
| `candidate_fix` | One changed mechanism only |
| `counterfactual_baseline` | What same task did under simpler system |
| `disposition` | KEEP, REWORK, DEFER or REMOVE after independent results |

We should not create “bottlenecks” from imagined failures. Rows enter the observed ledger only when actual authorized experiments produce evidence.

## 7. Progression

**H0 -> H1 only when:** (a) source can be independently reproduced and checked by actual SHA, (b) true positive and negative test execution observed, (c) deliberately faulty candidate is rejected, (d) evaluator and worker access boundaries verified, (e) costs and incomplete attempts recorded, and (f) reviewer accepts limitations.

If H0 fails: fix the minimal evidence path first; **do not introduce** an agent framework, durable workflow engine, multi-agent group or OpenTelemetry collector to mask the failure.

**Current: SPECIFICATION ONLY; no code built or run, no trial authorized.**

*Build today, so others can enjoy tomorrow.* ❤️🐂
