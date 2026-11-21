# E0a Go/No-Go — Independent Custody Proof Obligations v0.1

**Status:** RESEARCH PROPOSAL; no setup, trial, QA or tests have occurred. Foromni only. 2026-11-21.
**Parent:** ADR-E0A-002-INDEPENDENT-REVIEWER-CUSTODY-AND-PATCH-ONLY-TRIAL.md; E0 v0.7 canonical contract.

## Proof obligations

| Gate | Required observed evidence | Authority | Current status |
|---|---|---|---|
| G01 contract | Reviewer approves exact version/commit and six v0.7 decision bundles | Founder + independent reviewer | NOT APPROVED |
| G02 trial scope | Exact synthetic repo/runtime, provider/network, cost cap, time/retries, stop conditions, teardown | Founder | NOT AUTHORIZED |
| G03 distinct principals | Worker cannot write QA fixtures/results or impersonate reviewer | Trusted runtime/evaluator owner | UNVERIFIED |
| G04 sandbox | No host socket, production credentials, broad GitHub write token, unapproved egress or secrets | Trusted policy operator | UNVERIFIED |
| G05 source custody | Independent observer applies copied patch to frozen base, verifies clean SHA and artifact digest | Source observer | UNVERIFIED |
| G06 evaluator | Separate fixed positive/negative test suite and deterministic synthetic auth/DB/clock | QA owner | NOT IMPLEMENTED |
| G07 verdict | Actual required tests executed and tied to exact evaluated source; independent verdict | QA owner | NOT VERIFIED |
| G08 economics | Model, hosting, retries, QA, human effort and incomplete attempts accounted | Analyst | NOT FROZEN |
| G09 side effects | Worker has no GitHub main write; unknown external action reconciled before retry | Policy operator | UNVERIFIED |
| G10 claims | Candidate pass never asserted as main integration, deployment or AINO superiority | Independent reviewer | NOT VERIFIED |

Every G01–G09 must be satisfied before a bounded E0a implementation trial, and G10 before public result claims. Evidence must be separately authenticated; the worker's self-report is not proof. The reviewer must distinguish a tool-denial test from a tool simply absent.

## Exact separation for initial design

- Coding worker W: synthetic repository and disposable patch workspace; no GitHub, production database, release or evaluator secrets.
- Source observer S: frozen base plus handed-off diff; reconstructs independent candidate commit and patch digest.
- Evaluator Q: separate clean checkout at S candidate SHA, independent fixed suite, synthetic database/browser, evaluator-only result store.
- Dispatcher/policy P: independent resource and action-time limits, durable receipts and stop mechanism.
- Founder H: explicit bounded approval and ability to stop; approval is not implied by continuing research.
- The same human may operate trusted pieces with genuinely distinct effective identities, but authored self-review is not independent external evaluation.

## Unfilled authorization record

| Field | Proposed pretrial value |
|---|---|
| Approved contract and SHA | Pending independent review |
| Approved trial runtime/model | Not selected |
| Worker/principal separation | Not verified |
| Source/fixture/browser image digests | Not pinned |
| Security and egress rules | Not verified |
| Total real-spend ceiling | Not approved |
| Maximum retries and deadline | Not approved |
| Data scope | Synthetic only; no IE or Foromni production data |
| Source writes | Local patch only; no main merges |
| Tests/CI/deployment | Not authorized |
| Retention/teardown owner | Not assigned |

**No-Go:** E0a remains NOT READY FOR EXECUTION. Research commits may continue on the existing research branch. Building a worker runtime, running a benchmark, changing GitHub permissions, using credentials or creating a trial service requires separate scoped approval.

*Build today, so others can enjoy tomorrow.* ❤️🐂
