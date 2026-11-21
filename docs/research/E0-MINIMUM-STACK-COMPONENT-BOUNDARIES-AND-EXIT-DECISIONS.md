# E0 Component Boundaries and Minimum-Stack Decision Record — Research v0.1

**Status:** Proposed decision record and research-exit checklist; no permission to execute tests, create infrastructure, merge, deploy or contact any external party.  
**Date:** 2026-11-21 · **Scope:** Foromni only.
**Parent:** AINO-END-TO-END-OPEN-SOURCE-CONVERGENCE-REFERENCE-ARCHITECTURE-V0.1.md.  
**Existing audits:** E0-RESEARCH-EXIT-AUDIT-AND-THREAT-MODEL.md; FULL-STACK-REFERENCE-APP-API-FIXTURE-FREEZE-PROPOSAL-V0.3.md; E0-INDEPENDENT-ACCEPTANCE-EVIDENCE-AND-GRADE-DECISION-TABLE.md.

## Context: avoid a distributed-system-shaped research trap

The five OSS case studies are complementary. **Adopting all of them simultaneously would confound a first controlled trial and add needless risk/cost.** E0 must prove that one independent coding worker can build a small full-stack app and that an independent reviewer can determine whether the result actually works, using exact source and fixed requirements. Only later should Foromni compare convergence-first orchestration with simpler task assignment and evaluate scaling with more agents.

A "complete AINO reference architecture" is a map of boundaries; **not** a demand to implement every layer in a minimal pilot.

## 1. Minimum E0 implementation boundary (only if separately authorized)

| Component / concern | Research selection for a bounded synthetic E0 | Owner / trusted authority | Excluded until justified |
|---|---|---|---|
| Objective and roadmap | Reviewed, frozen Collective Lab goal/requirements revision | Founder/reviewer | General-purpose portfolio planning platform |
| Agent identity | One stable registry `agent_id` plus session, task and attempt IDs in a small trusted ledger | Authorized dispatcher | Autonomous agent-hiring/competency marketplace |
| Task graph | Fixed finite dependencies and accepted interface contract | Research reviewer | Live adaptive multi-tenant relationship knowledge graph |
| Coding worker | One isolated disposable agent/runtime under approved provider | Executor limited to synthetic project | Rerun/OpenHands product integration solely for brand parity |
| Model credential | Trusted gateway or scoped service account outside model context; usage records | Operator/runtime | New key per agent unless actual isolation needs demand it |
| Repo write | Isolated candidate patch submitted via trusted reviewer/broker; source SHA/read-back recorded | Trusted Git principal | Permanent GitHub App broker service unless needed to verify scoped actions |
| Database/auth | Proposed local disposable Next.js + PostgreSQL/Auth provider, deterministic synthetic fixtures; final choice pending | Approved environment owner | Cloud-linked production Supabase or real users |
| Independent acceptance | Separate principal and frozen positive/negative test oracle, exact-source checks | Evaluator owner | Production CI or public benchmark score claim |
| Security | Worker isolation, action-time grants, no secrets/egress by default, PI synthetic denies, review | Independent policy owner | Full SIEM and adversarial testing platform |
| Recovery | Minimal operation intent/read-back ledger, UNKNOWN handling, no blind retry | Trusted operator | Mandatory LangGraph + Temporal simultaneously |
| Observability | Local redacted run/attempt/operation logs; optional OTel spans if naturally supported | Runtime plus separate ledger | Full collector cluster + paid backend |
| Integration/release | Document protected Git path/prospective merge semantics; no main merge/release in research-only phase | Human owner + Git policy | Live staging/public deployment without separate permission |
| Outcome/econometrics | Accepted behaviors, all attempted runs, full costs and failure classes | Independent analyst | Long-term adaptive routing claims from 1 case |

**Important:** This table is still provisional. The operational trial must specify exact authenticated principals, environment, secrets and Git rules and be approved separately.

## 2. Boundary decisions — what Foromni owns

1. **Own accepted intent, not worker implementation:** objective/task/contract versions live in the authoritative registry; model suggestions do not become policy by being stored.
2. **Own identity mapping, not a unique AI model key:** stable registry agent ID maps onto authenticated run/session, external worker handle and provider key usage. An existing agent platform may furnish a helpful handle.
3. **Own the rights check, not broad GitHub credentials in each worker:** broker/reviewer enforces actual scope; GitHub App identity can legitimately be shared while internal actors remain verifiable.
4. **Own acceptance provenance, not a custom test framework:** use applicable maintained testing tools, but independently validate original requirements and source-bound results.
5. **Own outcomes, not an all-purpose telemetry platform:** trace model/tool calls with standard semantics when possible; cost/outcome evidence remains anchored elsewhere.
6. **Own reconciliation, not a new durable workflow engine:** an operation is not safely retried until its side effect and current permission are reconciled. Move to Temporal/LangGraph if workload evidence later warrants it.

## 3. E0 decision table and unresolved review items

| Review question | Proposed choice | Evidence currently missing |
|---|---|---|
| Which app stack? | Disposable local Next.js / Supabase Auth / Postgres RLS, pending architecture comparison | Version pinning, actual local isolation and migration validation |
| Which agent worker? | A single isolated approved coding agent, no permanent orchestrator dependency | Available model/provider runtime and permission capabilities |
| Where does candidate source go? | Disposable isolated branch or patch artifact with actual SHA recorded | Git host branch rules and safe broker/reviewer workflow |
| How are API contract differences handled? | Resolve/freeze v0.3 user roles, invitations, paging, ETags | Independent conformance review and acceptance-oracle freeze |
| What does PASS mean? | Positive+negative cases actually run; exact current SHA, separate QA, security gates | Independent evaluator, fixture identity and protected evidence storage |
| How to measure productivity? | Accepted full-stack behaviors per total cost, elapsed time, failures/censoring | Study design, trial-count/power assumptions, price/retry/human ledger |
| How to handle lost Git ACK? | Durable operation ID, read-back, compare/recheck/refuse ambiguity | Demonstrated host behavior and technical proof, not just design |
| What is a security release gate? | PI action-time enforcement and independent staged gate; E0 only synthetic | Threat review, evaluator provenance and active constraints |
| When may source be deployed? | Not during research-only work; requires additional explicit scoped approval | Authorization and real live readiness checks |

## 4. What separates E0 from convergence-first comparative proof

**E0a — Single-agent reproducibility, proposed:** One fixed reference app; one coding agent; independent acceptance and safe teardown; record all costs, failures and negative tests. Demonstrates feasible baseline, **not** an AINO-wide value proposition.

**E0b — Small controlled comparison, proposed:** Similar tasks matched/randomized, same worker/model/hosting/QA/limits. Control receives ordinary work requests; treatment receives structured convergence packets with explicit version/dependency preflight. Measure accepted functionality, task latency and full cost including planner overhead. No deployment change confound.

**Later scaling:** Add 3/8/adaptive agents, durable workflow platforms, changed host models, provider keys and sophisticated organization-learning features in isolated experiments. Avoid claiming conclusions without repeated trials and uncertainty analysis.

## 5. Handoff and study discipline

- One canonical roadmap/task identifier; research case studies are not new product tasks just because their titles exist.
- Maintain a study-to-design-decision trace (case study -> supported mechanism -> candidate interface -> accepted design decision -> tested hypothesis).
- Source refs and statuses should distinguish documented observation, code-inspected mechanism, executed unit/integration tests, and independently reproduced evidence.
- When a later source contradicts our design, revise the assumption rather than defend an earlier diagram.
- Deeper inter-agent communication/memory protocols and expanded cybersecurity/SIEM research remain deferred, with only minimal trust boundary notes active now.
- External OSS contact, issues, PRs or co-branded research needs separate founder approval and contributor consent.

## 6. Suggested next researcher action

Perform a **read-only host/permission reality audit** using Foromni's relevant disposable GitHub capabilities and inspect the exact independent evaluator proposal. The audit must not mutate repos, change rulesets or run CI. Then produce a versioned E0 trial-authorization checklist naming scope, worker, allowed tools, cost/stop limits, generated records and teardown.

### Acceptance criterion for *research exit*

An independent reviewer can explain the exact E0 objective, agent action boundary, evaluator separation, source SHA evidence, Git protections, full cost/failure denominator and rollback/teardown without inventing behavior. **Documentation clarity can make E0 research-ready; only executing authorized checks can make the implementation experimentally ready.**

*Build today, so others can enjoy tomorrow.* ❤️🐂
