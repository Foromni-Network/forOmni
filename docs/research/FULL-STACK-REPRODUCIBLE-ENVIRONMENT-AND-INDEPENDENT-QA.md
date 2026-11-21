# Reproducible Full-Stack Experiment Environment and Independent QA — v0.1

**Status:** RESEARCH SPECIFICATION, not deployed, executed, or authorized as an experiment.  
**Date:** 2026-11-21 · **Scope:** Foromni only; Internet Embassy remains separate and untouched.  
**Companions:** FULL-STACK-MANAGED-VS-SELFHOSTED-ARCHITECTURE-COMPARISON.md, FULL-STACK-REFERENCE-APP-CONFORMANCE-V0.2.md, FULL-STACK-CONVERGENCE-TRIAL-PREREGISTRATION-V0.1.md, CONVERGENCE-WORK-PACKET-TYPED-CONTRACT-V0.2.md.

## Decision to research next

Before choosing a managed or self-hosted benchmark winner, establish a host-independent experiment envelope and independently enforceable acceptance path. The goal is **a comparable fully integrated application**, not a contest in who can make a green badge quickest.

Avoid combining three variables into one trial: app backend architecture (Supabase vs Auth.js/Postgres), agent hosting (local vs ephemeral cloud), and tasking style (ordinary vs convergence-aware). Fix all but one for each first comparison, or comparisons become uninterpretable.

## 1. The minimum reproducibility envelope

| Layer | Fixed research input | Evidence a future authorized trial must emit |
|---|---|---|
| Source | Frozen starter commit and benchmark specification revision | Git commit OID, dependency lock digest, diff and candidate provenance |
| Toolchain | Exact Node.js/package-manager/browser/CLI/database image versions | Manifest of resolved versions and content digests |
| Agent | Model/provider ID, temperature/tools, retries, effective instructions, scoped authority | Redacted attempt log, token/cost measurements, work packet revision |
| Runtime | CPU, RAM, filesystem/disk quotas, network egress rules, process timeout | Provisioning record and observed resource consumption |
| Database | Disposable database per run, migration history and fixed seed | Reset/replay evidence, schema digest, migration failures |
| Auth | Synthetic personas, identity/session mechanism, role matrix | Independent positive/negative permission checks |
| QA | Immutable test corpus version, authorized reviewer principal, browser list | Test event IDs, exact tested source/artifact SHA, failures and trace references |
| Git | Isolated worker branches and protected integration destination | PR/candidate source SHA, prospective merge-group SHA, actual merged SHA |
| Cost | Inference, hosting, storage, CI/QA, review, orchestration and failed attempts | Timestamped ledger with units/currency and missing-data flags |
| Outcomes | Observable fixed vertical-slice acceptance and safety requirements | Signed/attributed independent acceptance or explicit unknown/failure |

Do not rely on unstated defaults. Use documented base images and verified immutable image digests where possible. Dependency lockfiles and image tags alone are not a cryptographic provenance system.

## 2. Isolation and hosting

**Local disposable baseline:** Containerized app, database and test harness may run on a developer lab machine, but no real personal files, host Docker socket or production cloud credentials should be accessible to untrusted agents. For stronger isolation, prefer dedicated disposable VMs/sandboxes rather than assuming a container is a complete security boundary.

**Ephemeral cloud comparison:** A fresh worker sandbox per task/attempt with resource and network caps, separately managed trial database, short-lived credentials, and teardown evidence. A persistent central task ledger may observe experiments but must not give worker sandboxes credentials to alter protected mainline or the independent evaluation suite.

**Managed backend path:** A local Supabase CLI development stack is suitable as a candidate **only when reset commands are guaranteed local**. Official docs warn that remote/linked reset flags can destroy remote schemas and replay migrations. No experiment worker should be able to target a linked production project.

**Self-hosted backend path:** Disposable PostgreSQL plus app-owned auth; one isolated database/namespace per trial; separately protected database superuser/setup credentials. Compare auth/RLS outcomes, not only service start time.

**Network**: No real invitations, payments or unsolicited external messages; synthetic identities only. Prefer deny-by-default outbound access with allowlisted model-provider endpoints and approved package registries, including dependency-cache strategies where practical.

## 3. Independent QA architecture

Three different judgments must never be conflated:

1. **Agent local self-check:** allowed unit/type checks and summary; useful for repair but not authoritative.
2. **Independent candidate QA:** actual test runs under a separate principal, with acceptance oracle the worker cannot alter; exact candidate SHA and immutable report.
3. **Integration-group QA:** tests the *combined prospective target* on the current mainline / eligible queued changes; the tested source must match what receives protected admission.

**Tooling candidate:** Playwright supports multiple browser projects and traces for reproducible UI failure diagnosis. A browser trace can contain screenshots, network details or sensitive state; in future tests retain synthetic-only data, redaction and controlled access.

**Git host candidate:** If GitHub merge queue is selected, any required GitHub Actions checks must handle the `merge_group` event; old green branch checks alone are not a substitute for relevant group verification. Do not assume these features are active in Foromni's repository.

**Evaluator independence:** Distinct model invocation is insufficient if its credentials/reports/fixtures can be controlled by the implementer. Independent reviewer should use a separately permissioned identity and sealed tests; it can still produce mistakes, so preserve raw outcomes and human challenge pathways.

## 4. Proposed minimal acceptance fixture matrix

| Gate | Test family | Example failure to catch |
|---|---|---|
| BUILD | deterministic install/typecheck/production build | Hidden undeclared dependency or missing env |
| API | schema compatibility, validation, response contract | UI expects `displayName`; API responds `name` |
| AUTH | impersonation and session expiration | Synthetic user accesses another project |
| RBAC | member/viewer/manager/owner matrix | Viewer mutates task or manager changes membership |
| DATA | migration, seed/reset, restart persistence | Task lost on restart; cross-project leakage |
| CONCURRENCY | entity version conflict | Stale mutation silently overwrites newer task |
| ACCESSIBILITY | keyboard navigation, labels, focus, basic narrow viewport | Modal traps keyboard, form errors inaccessible |
| RECOVERY | intentional worker/provider interruption | Duplicate task result accepted after retry |
| INTEGRATION | latest merge-group exact source and API | Independently green branches fail together |
| RELEASE | staging artifact provenance, explicit approval | Unapproved public deployment occurs |

The tests here are specifications. **No passing or failing run exists** as of this document.

## 5. Reset and teardown requirements

Each attempt begins with a clean, attributable state:
- pristine starter repo / isolated task branch;
- fresh synthetic seeded database and storage;
- fixed clock-sensitive fixture behavior where possible (expiry, session, retry);
- distinct worker and reviewer credentials, with least-privilege scope;
- no connected real user, production system or sensitive secrets;
- cleanup that verifies worker credential revocation and removal of disposable resources.

Never let an experiment agent directly run generic "reset database" instructions against production or arbitrary remote destinations. Prove the intended target with environment identity and a privileged trusted setup executor before executing destructive actions. Save permitted test failure artifacts without retaining private data.

## 6. Cost and resource measurement

Do **not** invent an hourly price or promise a cost threshold without dated provider quotes. Before experimental authorization, budget:
- per-worker tokens/inference and API calls;
- agent hosting boot and running time;
- managed backend resources / self-hosted database time;
- CI runner and browser testing workload;
- result artifacts and log retention;
- orchestration/dispatcher and human reviewer time;
- retries, bad candidates, resource teardown and idle capacity.

Resource controls must enforce actual ceilings in the provider/billing/runtime path; a JSON limit in a prompt is informational only. Record missing data rather than filling in guessed costs. If a trial aborts, count consumed resources.

The first comparison should prioritize **end-to-end reproducibility and security**, then optimize cost after data exists.

## 7. Threat/authority boundary

| Principal | Allowed | Denied unless separately authorized |
|---|---|---|
| AI implementer | Read approved synthetic spec; write isolated branch; run local sandbox checks | Read evaluator secrets, edit independent tests, merge protected main, deploy |
| AI planner | Propose work packets, dependency splits, repair | Grant itself permissions, override human objective |
| QA evaluator | Read permitted candidate; execute independent tests; issue evidence-bound verdict | Change worker source silently, self-approve release |
| Trusted merger | Verify current required conditions; perform approved protected operation | Ignore missing/unknown checks, fabricate outcome |
| Trial steward | Approve/revoke setup scope and budget; review incidents | Infer that a study outcome is proven without evidence |
| Publishing authority | Approve accurate, permissioned findings | Present simulations as measured experimental results |

All grants are scoped to Foromni. IE has no role or access path in this study.

## 8. Concrete experiment ordering

**Step R0 — Finish research and freeze scope:** Choose exact API/auth/database semantics, fixture, acceptance suite, reviewer independence, and known failure scenarios. Record stakeholder/maintainer authorization before any code.

**Step E0a — Reproducibility smoke trial:** Under separate later authorization, can one isolated agent build the fixed reference app in a disposable environment, and can an independent reviewer reproduce the outcome? This isolates baseline infrastructure problems.

**Step E0b — Convergence-first vs ordinary tasking:** Fix one architecture and hosting method. Compare work packets vs standard prompts with identical objectives/acceptance and full cost accounting.

**Step E1 — Agent team sizing:** With the same chosen stack, compare 1, 3, 8, adaptive; keep independent QA and cost accounting constant.

**Step E2 — Architecture/hosting comparisons:** Once a stable benchmark exists, separately compare managed vs self-hosted architecture, then local vs ephemeral cloud/hybrid worker hosting. A factorial trial can follow only if justified by adequate sample size.

**Step E3 — Failure/recovery and eventual release rehearsal:** Simulated outages, stale tasks and failed migrations, then nonpublic staged artifact with explicit authorization.

**Step E4 — Publication:** After independent review, source-link real findings and negative outcomes, then separately authorize evergreen educational content.

## 9. Remaining research uncertainties

- Which exact starter framework/runtime versions should be pinned? Need reproducibility and current security support audit.
- Authentication choice and session test fixtures in each architecture require explicit equivalence review.
- What ephemeral sandbox mechanism offers real isolation within the affordable resource envelope?
- Is Playwright plus independent API/database tests adequate to measure accessibility/security or do domain specialists need additional assessment?
- What merge protections/queue features are available under the actual Foromni repository settings?
- What queueing overhead changes results when three or eight agents share finite QA capacity?
- Can clean-room reproductions operate without exposing private prompts or API credentials?
- How much of the measurement/trace format is reusable by another AINO with a different code host?

These are **research blockers/questions**, not an authorization to build a controller.

## Primary technical references

- Next.js documented standalone output and deployability: https://nextjs.org/docs/app/api-reference/config/next-config-js/output
- Next.js App Router self-hosting considerations: https://nextjs.org/docs/app/guides/self-hosting
- Supabase local development and CLI: https://supabase.com/docs/guides/local-development/cli/getting-started
- Supabase CLI local/remote workflows and destructive reset distinction: https://supabase.com/docs/guides/local-development/cli-workflows
- GitHub protected merge queue and required `merge_group` checks: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
- Playwright projects and multi-browser coverage: https://playwright.dev/docs/test-projects
- Playwright trace viewer and debugging: https://playwright.dev/docs/trace-viewer-intro

## Research recommendation

For a first **future** trial, choose *one* reproducible stack and disposable local/ephemeral sandbox after review, then prove the clean-room acceptance procedure. Avoid scaling to eight agents or simultaneously changing app backend and host until repeatability works. The fastest way to reliable evidence is to reduce experimental variables—not produce more independent code.

*Build today, so others can enjoy tomorrow.*
