# Collective Lab Benchmark — API and Fixture Freeze Proposal v0.3

**Status:** Proposed detailed behavioral contract for review, NOT an accepted implementation contract and NOT a running benchmark.  
**Date:** 2026-11-21 · Scope: Foromni only; Internet Embassy untouched.
**Based on:** FULL-STACK-REFERENCE-APP-CONFORMANCE-V0.2.md, E0-RESEARCH-EXIT-AUDIT-AND-THREAT-MODEL.md, FULL-STACK-CONVERGENCE-TRIAL-PREREGISTRATION-V0.1.md.

## Why this pass matters

An end-to-end experiment is uninterpretable if each autonomous team can silently choose different paging, identity, invitations, concurrency or error semantics. This document provides **candidate decisions** that an independent reviewer must accept/freeze before any trial. It is deliberately technology-neutral for Next.js + local Supabase/Postgres and Next.js + Auth.js/Postgres alternatives.

## Candidate decisions and test oracle

| Topic | Proposed v0.3 behavior | Negative case required |
|---|---|---|
| User identity | Authenticated opaque server-minted `userId`; current identity read via `GET /api/me` | Reject body or header claims to be arbitrary another user |
| Sessions | HttpOnly, Secure (except explicitly approved local development), SameSite=Lax cookie where cookie sessions used; server checks every private request | Expired/invalid session denied; logout invalidates future protected use |
| Project visibility | `private` default, `public` displays minimal metadata only; tasks/activity stay members-only | Nonmember cannot access private project or public project's private task list |
| Role semantics | Existing v0.2 matrix: owner controls membership/visibility, manager edits project/task, member edits assigned task, viewer reads | Cy viewer write denied, Bao visibility change denied, Dee cross-project access denied |
| List paging | Page size default 20, maximum 50; stable ordering by `createdAt DESC, id DESC`; opaque cursor bound to filters and viewer scope | Cursor from different filter/user denied or safely reset; no leakage of inaccessible rows |
| Identifiers | Opaque stable IDs issued by server, not user-controlled foreign keys | Body-supplied `ownerId`, `actorId`, `role`, `projectId` cannot override scope |
| Task title/description | Title trimmed 1–160 Unicode code points; description 0–4000 Unicode code points; reject invalid types and excessive size before DB write | Oversize/blank title rejected without mutation |
| Task statuses | `todo | in_progress | done`; server stores only declared values | Unknown status rejected; no partial mutation |
| Concurrency | Entity version integer begins at 1; writes send `If-Match` compatible expected version; stale version is HTTP 409 | Concurrent updates cannot silently clobber prior commit |
| Invitation | Owner creates synthetic-target invite, single use, 24h TTL, recipient-bound; token high entropy, hashed at rest; no real mail | Wrong user, replay, revoked and expired token denied |
| Error body | `{"error":{"code":"CODE","message":"...","requestId":"..."}}` consistent; no internal secrets | Invalid route/role never exposes private entity or credentials |
| Audit | Successful create/update/membership change emits server-derived actor, time, object ID; denied requests do not appear as successful business events | Forged actor field cannot influence attribution |
| Restart | Seeded DB persists project/member/task/activity through application process restart | DB data not silently replaced with in-memory state |
| DB migration | Ordered transactional DDL when possible, forward-compatibility plan and clean reset; externally destructive migrations need trusted approval | Schema mismatch causes clear failure, not silent app success |
| Accessibility | Keyboard-only essential path, visible focus, labeled errors, narrow viewport, loading/empty states | Modal or form inaccessible to keyboard test fails |

The above version and TTL values are **benchmark design choices, not general product guidance**. Auth cookie settings require review against the exact auth mechanism, threat model and transport; backend-managed auth may use a different session implementation with the same observed security behavior. `If-Match` syntax must be formalized for integer versions, e.g., a quoted strong entity tag `"v3"`; don't mix weak tags and opaque database ints. Invitation expiry must use a controlled clock in synthetic fixtures.

## Example response contracts

`GET /api/me` when authenticated:

```json
{"id":"usr_ada","displayName":"Ada"}
```

`GET /api/projects?limit=20` for a synthetic member:

```json
{
  "items":[
    {"id":"prj_A","title":"Research Workspace","description":"Synthetic data only","visibility":"private","version":1}
  ],
  "nextCursor":null
}
```

`POST /api/projects` body:

```json
{"title":"New Project","description":"Synthetic only"}
```

Server records authenticated actor as owner and defaults to `private`. Clients must not be allowed to assign another owner by submitting additional fields. Private project not found or inaccessible should not disclose existence.

`PATCH /api/projects/prj_A/tasks/task_1`:

```text
If-Match: "v3"
Content-Type: application/json

{"status":"in_progress"}
```

The server rejects a stale version with a structured `409`; successful response returns updated version and an ETag consistent with representation.

## Deterministic seed and held-out variants

**Public fixture identities:** Ada (A owner), Bao (A manager), Cy (A viewer), Eli (A member), Dee (B owner), anonymous visitor.

**Fixed setup:** A private and B public; at least one assigned task in A for Eli; one task assigned to another member; B private task metadata not visible merely because B is published. All IDs are synthetic. Fixture timestamps should derive from a reproducible clock, not wall time.

**Reviewer-held-out cases:** foreign-project task ID mixed with a valid A URL; invitation accepted twice in concurrent requests; deactivated membership during session; cursor scopes changed; stale task update; body actor forgery; API `displayName` mismatch; generated code logging synthetic tokens. An evaluator may hold these variants confidential from implementers while still sharing all corresponding behavioral requirements and test-class descriptions.

## Deployment-stage prompt injection requirement

Independent security evaluation must verify that a malicious synthetic project title, PR comment, README, or tool log cannot change task acceptance, source/QA provenance, effective tool grants or deployment authority. Actual authorization is enforced outside the model; a test scanner is defense-in-depth. Future `SEC-PI-GATE` requirements are described in PROMPT-INJECTION-PIPELINE-SECURITY-GATE-RESEARCH.md. No PI checks have been run.

## Reviewer decision list before a 'frozen' experiment

1. Approve or revise pagination scheme, entity tag representation, invite TTL and access behavior.
2. Select exact authentication/session test harness while preserving cross-stack behavioral equivalence.
3. Resolve ambiguous public project details, explicit unauthorized error status and membership deletion.
4. Approve deterministic seed/time model and independent hidden negative test ownership.
5. Verify resource limits, database reset isolation and permitted network calls.
6. Version the accepted spec and pin trial starter source, packages and test suite.
7. Request separate founder authorization for bounded execution; none assumed by this research document.

**No executable code, tests, databases, projects or service accounts were created.** This is a proposal for independent review, not a validated frozen contract.

*Build today, so others can enjoy tomorrow.*
