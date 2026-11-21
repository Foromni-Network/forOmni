# Full-Stack Benchmark: Managed vs Self-Hosted Architecture Decision Study v0.1

**Status:** Foromni research only — no deployment, account configuration, CI runs, authorization or stack selection.  
**Date:** 2026-11-21. **Boundary:** Foromni only; no Internet Embassy code, credentials, infrastructure or integration.  
**Companions:** FULL-STACK-REFERENCE-APP-CONFORMANCE-V0.2.md, FULL-STACK-CONVERGENCE-TRIAL-PREREGISTRATION-V0.1.md, AI-WORKFORCE-HOSTING-AND-SYNERGY-ARCHITECTURE.md.

## Research question

For an identical synthetic full-stack collaboration app built by autonomous AI workers, which baseline architecture offers the most reproducible, independently verifiable result with controlled risk and total cost? Separate **application stack selection** from **AI worker hosting** so trial conclusions are not confounded.

We compare two grounded, technically plausible stacks with shared Next.js frontend and PostgreSQL relational semantics. This reduces unrelated frontend differences while exposing the managed-vs-self-managed authentication and data-policy tradeoffs. Not a universal benchmark of all modern web stacks.

## A. Managed integrated backend

**Candidate:** Next.js App Router frontend and server integration + Supabase Postgres/Auth (managed for eventual hosted trials, or local CLI stack for disposable runs) + SQL migrations + PostgreSQL RLS.

### Advantages to test
- Local Supabase CLI stack includes Postgres/Auth, enabling seeded synthetic fixtures and restart/reset exercises.
- Row Level Security combined with Supabase Auth can express project/member access boundaries in database policies.
- Less need to build a login/session subsystem for a small app; managed backend may lower setup effort.
- Webapp remains portable within Next.js hosting choices, though Supabase-specific APIs and auth/RLS coupling reduce backend interchangeability.

### Risks and evidence requirements
- RLS is **not automatic security**: every relevant table/policy and operation requires negative cross-project verification.
- Service-role or other privileged keys can bypass ordinary RLS expectations; keep them out of untrusted workers and browser runtime.
- Local CLI starts multiple services (often via Docker), potentially increasing CPU/memory and cold-start costs for eight parallel workers.
- Reset/migration commands can be destructive if run against a linked remote project; make destructive operations impossible for experiment workers.
- Need to prove session/claims propagation, auth state transitions, invitation handling and server-side enforcement.
- Managed service price, limits and regions should be compared on trial date; no invented quotes or guarantees.

**Primary sources:**  
https://supabase.com/docs/guides/local-development  
https://supabase.com/docs/guides/local-development/cli/getting-started  
https://supabase.com/docs/guides/database/postgres/row-level-security

## B. Self-managed application/auth/database

**Candidate:** Next.js App Router + Auth.js for login/session handling + PostgreSQL database + Drizzle ORM/migrations, packaged with disposable Docker Compose services and self-hostable Next.js standalone output.

### Advantages to test
- Independent, explicit app-owned authorization logic can be inspected for every API route; SQL policy layer may also be added but should not be claimed present automatically.
- Postgres and app containers provide portable isolated environment for local, VM and ephemeral remote worker evaluation.
- Fewer proprietary backend interfaces may ease migration and alternate hosting.
- Drizzle provides typed PostgreSQL integration and migration tooling; Auth.js has Next.js integration and database adapters.

### Risks and evidence requirements
- Auth.js authenticates users but does **not** automatically implement tenant/project permission checks; server-side permission matrix needs bespoke design and independent negative testing.
- Session secret handling, adapter schema, migrations, invitation tokens, cookie/security headers, connection pooling, backups and recovery impose additional operational work.
- A shared database container with eight independent workers is a data and collision hazard; provision a disposable database per trial or use demonstrably separated schemas with strict grants.
- The current Auth.js Next.js package/reference may have release/beta nuances: pin and review exact version and security updates before experiment; avoid assuming API stability.
- Self-hosting requires operational hardening, reverse proxy/HTTPS and health/recovery controls for any future exposed service.

**Primary sources:**  
https://authjs.dev/getting-started  
https://authjs.dev/reference/nextjs  
https://orm.drizzle.team/docs/get-started-postgresql  
https://orm.drizzle.team/docs/migrations  
https://nextjs.org/docs/app/getting-started/deploying  
https://nextjs.org/docs/app/guides/self-hosting

## Fair comparison dimensions

| Dimension | Stack A: Next.js + Supabase | Stack B: Next.js + Auth.js + Postgres |
|---|---|---|
| Frontend/API runtime | Next.js | Next.js |
| Authentication | Supabase Auth; local service or managed project | Auth.js sessions/providers + app-controlled route authorization |
| Persistence | Supabase-hosted or local PostgreSQL | Standard disposable PostgreSQL |
| Tenant isolation | Explicit RLS policies plus server controls, tested independently | Explicit server-side authorization and SQL constraints; optional PG RLS only if preregistered |
| Environment setup | Supabase CLI stack and migrations; Docker resources | Compose app/DB and migrations; app-owned auth config |
| Data migration | SQL migration discipline and seeded resets | Drizzle migration discipline and seeded resets |
| Hosting | Next.js app host + managed or local Supabase service | Next.js standalone/container + DB host |
| Secrets risk | Elevated service keys, DB credentials, auth config | Auth/session keys and DB credentials |
| Lock-in vector | Integrated Auth/RLS/client semantics | Framework/auth/ORM conventions, infrastructure overhead |
| QA focus | RLS deny policies, claims, service key separation | Route authorization, session handling, adapter integrity |
| Worker-host portability | Requires consistent compatible local/managed service access | Docker/PG portability, host operations responsibilities |

**Security comparison caution:** DB-level RLS and app-layer authorization are not equivalent by default. Evaluate observed cross-tenant outcomes, defense-in-depth and attack surface, not the presence of a particular library or acronym.

## What remains constant across both

- Frozen Collective Lab personas/roles, URLs, API response envelope and persistence behavior.
- Exact server-side authorization fixtures (Ada, Bao, Cy, Dee, Eli and anonymous).
- Private-by-default project membership and invitation behavior.
- Mobile accessibility, errors/loading states, version-safe mutation, migration/restart proof.
- Independent QA principal and held-out negative tests.
- Git protected main/merge-group verification, source/commit provenance.
- Synthetic-only data, no real email or paid integration, no public release.
- Same agent models, compute/time budgets, task definitions and workflow arms; account for distinct setup labor.

## Trial configuration / isolation research

1. **Reference app and spec are identical**; architecture A vs B is a separate study from the convergence-first-vs-control study.
2. Build a reproducible baseline repo or two comparable scaffolded repos (not executed yet), both with an equal functional contract and the same independent test harness. Scaffold labor and any hand-optimized starter code must be disclosed.
3. Each attempt gets independent worktree/container, synthetic dataset, scoped secrets and ephemeral DB/schema; no agent holds blanket cloud account access.
4. Use a fixed, versioned application test runner with real browser/API/database checks. Avoid claiming GitHub green checks if `merge_group` workflow is not configured and executed.
5. Separate build artifact digest/source SHA and staging access from protected main and production permissions.
6. Capture full time and cost: model inference, runtime, Docker/VM provision, Supabase services or PG auth setup, CI retries, review, maintenance and recovery.
7. Rerun with different random seeds/task variants under preregistered ordering; preserve failed and inconclusive outcomes.
8. Repeat both architectures under 1 / 3 / 8 / adaptive worker cohorts only after isolated E0 study; avoid giant factorial design before sample sizes/costs are justified.

## Acceptance and negative tests to freeze before trials

- An anonymous user cannot read a private project, task or activity.
- Dee as B owner cannot access A private data or modify A projects/tasks.
- Cy as A viewer cannot mutate; Bao cannot modify A membership/visibility; Eli cannot assign others.
- Changing auth claims or request owner IDs cannot bypass project scoping.
- Invitation reuse/wrong identity/expired token fails, with no membership side effect.
- Stale entity version produces conflict without overwriting existing data.
- A frontend/backend field contract mismatch is rejected by independent verification.
- Each environment can reset from seed and reproduce equivalent test outcomes.
- No service-role/DB superuser secrets appear in worker contexts or build artifacts.
- Unrelated main advances don't permit stale integration checks to authorize a changed merge-group.
- No release/publication occurs without separately effective permission.

## Preliminary decision and next questions

**Do not choose a winner now.** A is a strong fast-start candidate if its local service footprint and RLS correctness are manageable. B is a strong portability candidate if app-owned authentication and operational overhead remain bounded. The first truly meaningful choice is between equivalent, reproducible disposable setups—not between brands.

Evaluate exact package versions, service RAM/CPU startup, authentication test strategies, provider hosting costs, migration ergonomics, worker sandbox permissions and independent QA implementation. Prefer the **simplest** baseline that meets the fixed conformance contract; use the alternative as a comparative architecture only when the trial can support the added experiment cost.

### Research exit / authorization boundary

This document is background for an eventual bounded experiment request. Still required: source-level reference starter analysis, fixture/QA independence decision, actual host class and resource cap, separate threat/privacy review and explicit authorization to create/test code. No work on actual application, live Supabase project, Vercel deployment or IE systems was performed.

*Build today, so others can enjoy tomorrow.*
