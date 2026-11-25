# Full-Stack E0 Pilot Architecture Decision — Research ADR-001

**Status:** Proposed for independent review. NOT adopted, implemented, benchmarked, or approved for execution.
**Date:** 2026-11-21. **Project:** Foromni only; IE remains untouched.
**Inputs:** FULL-STACK-REFERENCE-APP-CONFORMANCE-V0.2.md, FULL-STACK-MANAGED-VS-SELFHOSTED-ARCHITECTURE-COMPARISON.md, FULL-STACK-REPRODUCIBLE-ENVIRONMENT-AND-INDEPENDENT-QA.md, ECONOMETRICS-OF-CONVERGENCE-AND-COORDINATION-VARIANCE.md.

## Decision to make

For the **first** future E0 experiment, fix a single application and hosting configuration before comparing ordinary AI tasking to convergence-first packets. The research needs a credible baseline that makes end-to-end auth, server permission checks, UI, database, errors, migration, independent QA and Git integration observable without extensive infrastructure work.

**Provisional recommendation:** Next.js + TypeScript + PostgreSQL through a local disposable Supabase stack (including Supabase Auth), with explicit RLS policies and backend authorization tests. Use Playwright plus isolated API/database testing, GitHub-hosted independent CI and native protected merge behavior where supported. Keep Auth.js + standalone PostgreSQL as the *second-stage* portability comparison. This is a research preference, not a chosen production stack.

This baseline is selected to minimize first-trial setup variables, **not** because Supabase is proven safer, universally cheaper, easier for AI, or more interoperable. If a local CLI service cannot meet isolation, repeatability, test-data safety or resource limits, revisit and switch before the experiment is frozen.

## Competing alternatives and why not first

| Candidate | Potential advantage | Major complication for E0 | Selection |
|---|---|---|---|
| Next.js + local Supabase Auth/Postgres + RLS | Repeatable integrated auth/DB and a clear security oracle | Multiple local services, difficult RLS correctness and service-key isolation | Provisional E0 candidate |
| Next.js + Auth.js + vanilla Postgres/Drizzle | Portable standalone DB and app-owned auth | More auth/session setup, app-layer tenant authorization implementation | Stage E2 architecture comparison |
| Next.js + hosted managed backend | Fast real hosted setup | Service quotas, provider versions, network/billing, nonlocal reset risk | Not preferred for first disposable E0 |
| Custom complete microservice stack | Flexible and distributed | Adds unrelated service/ops variables and scope creep | Reject for E0 |
| Kubernetes worker and app cluster | Scalable future operations | Operational complexity confounds small-sample pilot | Defer until measurable need |

## Freeze a reproducible fixture, not vendor lock-in

The **behavioral contract** remains independent of any stack: same routes/field names, exact permission matrix, seeded synthetic users, migrations, data persistence, error handling, mobile and accessibility checks. The alternative architecture must satisfy this same acceptance oracle; changing expectations between arms invalidates the comparison.

Use a public, safely licensed toolchain and record tested resolved package versions **at trial authorization time**. Do not assert November 2026 versions, support status or monthly costs without verifying them. Pin lockfile and container digests, supported runtimes, browser versions and an environment manifest. Treat managed/local differences as a research factor; they are not identical merely because both use PostgreSQL.

## Target executable shape for a future trial (not created here)

```text
synthetic experiment workspace
  web/                 # Next.js app (UI + server API)
  db/migrations/       # schema and RLS / access policy migrations
  fixtures/            # synthetic identities/projects/tasks, seeded deterministically
  acceptance/          # independently maintained API, browser and security oracle
  protocol/            # preregistered cohort/strategy allocation and metrics
  evidence/            # local run manifest and redacted artifacts only
  docs/                # study method and discrepancy/correction register
```

The controller/worker implementation must **not** be in the same permission domain as the authoritative acceptance oracle. The proposal is a workspace outline, not an actual created directory or repository.

## Effective trust boundary

- An AI implementer receives an isolated repo clone/worktree and **synthetic-only** test data.
- A trusted fixture/setup principal provisions/tears down each disposable database. No remote-linked Supabase reset access.
- No service-role, root, Docker-host socket, deployment or protected-branch credentials are accessible to untrusted coding agents.
- The QA principal owns held-out negative tests, controls its evidence and cannot be impersonated by a coding worker.
- The protected merger checks the **current combined result**, not stale green branch self-reports. Its access is separate from the planner.
- Release/public publishing requires separate accountable authorization; E0 can stop after source integration or authorized disposable staging.
- If a trial's self-hosted runner cannot be isolated from malicious code, use a trustworthy provider-hosted ephemeral evaluator instead and document the trust assumptions.

## Authority vs user-facing task completion

Task accepted for development != code generated != candidate accepted != integrated source != staging ready != published/beneficial. Report all stages separately to avoid goal substitution.

### Stop/go for architecture choice

**Go to trial-authorization review only if:**
1. Local service boot/reset is reproducible without real cloud linkage.
2. Auth+RLS deny cases are independently specified, including bypass risks.
3. Schema/migrations, test identities and API field shapes are frozen.
4. An independent evaluator can test combined source under actual Git protections.
5. Per-run cost/resource limits and teardown are enforceable.
6. Reviewer/maintainer approves the architecture ADR and a fixed E0 protocol.

**Otherwise:** keep studying the blocker or choose a simpler safe baseline. No architecture score can override an unverified security gate.

## Research source references

- Supabase local development: https://supabase.com/docs/guides/local-development
- Supabase RLS concepts and roles: https://supabase.com/docs/guides/database/postgres/row-level-security
- Next.js deployment/self-hosting: https://nextjs.org/docs/app/guides/self-hosting
- GitHub merge queue: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue
- Playwright traces: https://playwright.dev/docs/trace-viewer-intro

**Not done:** no repository configuration audit, no source-level security review, no cost quotation, no sandbox benchmark and no approved pilot. A future research review must confirm the citations and exact current versions.

*Build today, so others can enjoy tomorrow.*
