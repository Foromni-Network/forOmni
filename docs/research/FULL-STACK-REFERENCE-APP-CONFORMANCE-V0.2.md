# Collective Lab Full-Stack Reference App — API, Rights and Acceptance Contract v0.2

**Status:** Research specification, not built or tested.  
**Date:** 2026-11-21 · **Scope:** Foromni only; IE remains separate.  
**Companions:** FULL-STACK-REFERENCE-APP-BENCHMARK-V0.1.md and END-TO-END-AINO-EXPERIMENT-READINESS-AND-EVIDENCE-PLAN.md.

## Intent and experimental control

This v0.2 freezes a *candidate* canonical behavioral contract for a fictional multi-project collaboration app. Every future agent-team cohort must implement identical requirements, including negative cases, rather than selecting the easiest interpretation. An authorized owner and independent reviewer must approve/freeze the specification before trials. No implementation or executable tests exist today.

### Personas and tenancy

Synthetic identities: Ada (A owner), Bao (A manager), Cy (A viewer), Dee (B owner, outside A), Eli (A member) and anonymous visitor. Project A is private, Project B can be made public by B's owner. Membership is project-scoped, not global. IDs are server-assigned opaque identifiers. Session user cannot select an arbitrary actor by request body.

## Canonical roles and permissions

| Action | Anonymous | Viewer | Member | Manager | Owner |
|---|---:|---:|---:|---:|---:|
| Read published project metadata | Yes | Yes | Yes | Yes | Yes |
| Read private project details | No | If project member | If project member | If project member | If project member |
| Read project tasks/activity | No | Yes, own project | Yes, own project | Yes, own project | Yes, own project |
| Create project | No | Yes as authenticated user | Yes as authenticated user | Yes as authenticated user | Yes as authenticated user |
| Create project task | No | No | Yes | Yes | Yes |
| Edit own assigned task title/status | No | No | Yes, when assigned | Yes | Yes |
| Assign/reassign any project task | No | No | No | Yes | Yes |
| Edit project title/description | No | No | No | Yes | Yes |
| Change project visibility | No | No | No | No | Yes |
| Invite/remove member or change role | No | No | No | No | Yes |
| Delete project | No | No | No | No | Yes |

**Scope:** Each role is evaluated relative to the *target project*, never the user's role elsewhere. Project owner is immutable except through a separately specified authorized ownership-transfer workflow (out of scope for this benchmark). An authenticated user may create their own new project regardless of any role in another project.

**Task updates:** Managers and owners may update any task. A member may change a task's title/status only if `assignee_user_id` is their own user ID; members cannot change assignee, project ID, role or activity actor. Viewers may not mutate. Audit records of successful mutations must attribute the authenticated actor.

## Proposed request/response contracts

A successful `GET /api/me` returns `{ "id": "usr_ada", "displayName": "Ada" }`. No private profile or membership lists are exposed to unauthenticated visitors.

A project response includes `{ "id", "title", "description", "visibility", "version" }` with `visibility` = `public | private`. For authorized members, responses may additionally include `myRole` and member count; public visitor responses omit private fields and membership lists. A task response includes `{ "id", "projectId", "title", "status", "assigneeUserId", "version" }`. Status = `todo | in_progress | done`.

Routes:
- `GET /api/projects`: return public projects plus requesting user's member projects; unauthorized private projects never appear; filter by `visibility` only with server-side permission.
- `POST /api/projects`: authenticated; body `{title, description?, visibility?}`; server sets owner and defaults visibility private.
- `GET /api/projects/:projectId`: owner/member can see private; any visitor can see published basic details.
- `PATCH /api/projects/:projectId`: managers may edit only title/description; only owner may change visibility; require `If-Match` or equivalent expected version.
- `GET /api/projects/:projectId/tasks`: project members only, including when the project is public; public metadata does not expose tasks.
- `POST /api/projects/:projectId/tasks`: member/manager/owner can create, but only manager/owner can specify non-null assignee other than self. Member-created task defaults assignee to self.
- `PATCH /api/projects/:projectId/tasks/:taskId`: allowed by role matrix; require expected version; target task must belong to given project.
- `GET /api/projects/:projectId/activity`: members only. Activity records append server-computed actor/action/timestamp.
- `POST /api/projects/:projectId/invitations`: owner only; creates **synthetic in-app invitation token** usable by a synthetic test identity. No outbound email/SMS.
- `POST /api/invitations/:token/accept`: authenticated; accept only an unexpired, unconsumed invitation addressed to same synthetic identity; server validates one-time use and intended role.
- `DELETE /api/projects/:projectId/members/:userId`: owner only; removing owner is forbidden.

Specify offset/cursor pagination and input size limits in a follow-up implementation ADR; until chosen, acceptance cases must cover bounded lists and stable ordering without selecting a cohort-favorable shortcut. Error envelope: `{"error":{"code":"FORBIDDEN","message":"...","requestId":"..."}}`; no secret/internal stack traces.

### Status and error semantics

- `401` absent/expired authentication for private endpoints; `403` authenticated without permission where object existence is already knowable; `404` for inaccessible private resource where disclosure of existence is not authorized.
- `400` invalid syntax, `422` semantically invalid fields, `409` stale entity version, `429` synthetic throttling if included by fixed fixture.
- Consistent UI handling: pending, empty, failure, retry and success states; no optimistic "success" until server commits or state is reconciled.

## Data correctness and privacy invariants

1. Every task, membership, invitation and activity row references a project/subject with database constraints.
2. Private-project authorization must be enforced on the server/data layer, not only in UI navigation.
3. Foreign-project identifiers supplied by a client must not bypass scoping.
4. Project membership and project visibility changes must be atomic with relevant audit events where practicable.
5. Invite tokens should be opaque, hashed/secured at rest, expiring and single-use; test identities only.
6. Task `version` increments on mutation; stale expected version returns conflict rather than overwriting silently.
7. User-visible activity logs are sanitized; don't expose access tokens, raw prompts or private audit details.
8. Public project list must not leak private project names/counts through error messages or timing-sensitive metadata when practical.
9. Schema migrations need a reproducible setup path and reversible/forward-compatible plan; irreversible migrations require separate review.
10. No API accepts a user-supplied owner/actor/role field as authoritative.

## Independent acceptance IDs

| ID | Test fixture | Expected result |
|---|---|---|
| ID-01 | Anonymous GET public project | 200 minimal project metadata |
| ID-02 | Anonymous GET private project A | 404, no project details |
| ID-03 | Dee requests A task list | 404 or non-disclosing forbidden behavior, no tasks |
| ID-04 | Ada manages A and attempts B mutation | A allowed; B denied |
| ID-05 | Cy attempts task POST/PATCH | Denied; no activity mutation |
| ID-06 | Eli updates own assigned task, another's task, and assignee | Own title/status allowed; others/assignment denied |
| ID-07 | Bao updates task and project title, attempts visibility/membership changes | Task/title allowed; visibility/membership denied |
| ID-08 | Ada invites test identity and accepts once as recipient | First accepted, replay or wrong identity denied |
| ID-09 | Client forges actor/owner role on POST | Server ignores/rejects; no privilege gain |
| API-01 | UI expects `displayName`; backend sends `name` | Consumer/provider or E2E test must fail |
| API-02 | Invalid and unknown update fields | No unintended mutation; standardized error |
| DATA-01 | Restart database after synthetic data create | Data and attribution retained |
| DATA-02 | Two writes share stale version | Conflict prevents lost update |
| QA-01 | UI desktop/mobile, keyboard-only and loading/error | Independently observed accessible behavior |
| INT-01 | Isolated green tests but latest merge-group incompatibility | Protected integration denied |
| OPS-01 | Build artifact and proposed release authorization | Integrated != deployed; without approval, no public release |

**These tests are specified but not implemented or executed.** An independent reviewer should own hidden variants and verify exact source/artifact revisions.

## Handoff needs strictly in scope

Task identity, source/base SHA, dependency/API contract revision, scoped grant, isolated branch ownership, test evidence refs and candidate SHA. Do **not** expand this benchmark into a general inter-agent communication platform before evaluating full-stack needs.

## Remaining decisions before freeze

- Choose session/auth approach and enforceable isolation boundary for disposable synthetic accounts.
- Define rate, pagination, field length, invite expiration and exact conflict response.
- Select one reproducible database and web/API runtime or supply equivalent conformance rules.
- Author exact independent browser/API/database check fixtures with held-out failures.
- Approve a matched compute/hosting envelope and external service restrictions.

**Scope note:** This document is a candidate experiment oracle; it does not authorize using Foromni or IE production data.

*Build today, so others can enjoy tomorrow.*
