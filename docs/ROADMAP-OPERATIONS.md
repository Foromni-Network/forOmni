# Foromni repository-native roadmap operations

**Canonical code and planning repository:** `Foromni-Network/forOmni`. The separate `projectManagement` repository is historical evidence, not the authoritative roadmap.

## Two complementary roadmap layers

- `ROADMAP.md` states the product direction, phases, and high-level exit criteria.
- `roadmap/tasks.json` contains concrete, traceable implementation tasks. This is the machine-readable status source once merged into `main`.
- GitHub issues and PRs contain discussions and implementation evidence, linked from tasks. Do not confuse them with the sole task registry.

The initial seeded tasks are **planning records**, not proof that the related work has been implemented. Reconcile legacy issues before expanding the inventory. Preserve all original URLs and histories.

## Lifecycle

`proposed → ready → running → review → batch_ready → build_ready → integration_ready → integrated → completed`.

A failure goes back to `review` with defect and repair evidence; failed records are not deleted. Revalidation on a changed commit requires fresh evidence. `batch_ready` means only that a candidate has evidence sufficient to enter a founder-authorized test batch, not that it has passed the later gates. Exact-SHA checks, dependencies, independently owned QA, permission/security checks, and integration admission are separate stages.

## Changes and evidence

1. Select the existing `FOR-...` task or create a task only if the scope is genuinely new.
2. Record owner, acceptance criteria, dependencies, PR/issue references, and source revision.
3. Make changes on a working branch; put verified status and evidence updates in the same or associated reviewed PR.
4. For `batch_ready` and beyond, attach concrete evidence entries. For `build_ready` and beyond at least one evidence entry must contain a full 40-character Git commit SHA and an HTTPS evidence URL. This CI rule is a *minimum hygiene gate*, not independent approval.
5. Obtain separate independent QA and dependency/security decisions before `integration_ready`. A self-reported pass cannot satisfy independent validation.
6. Integrate into an approved sandbox and record post-integration validation before `integrated`.
7. Production release remains founder-controlled; `completed` follows release/closure policy.

Use evidence records in this form (example structure, not a real result):

```json
{"type":"ci","sha":"0000000000000000000000000000000000000000","url":"https://github.com/ORG/REPO/actions/runs/RUN_ID","result":"pass"}
```

Replace the illustrative values with actual evidence. Never use an invented SHA or test URL.

## Operating streams

- **Passing:** Verify exact SHA, ownership, dependency contracts and security; hand off to independent QA and authorized sandbox integration.
- **Failing:** Diagnose logs, repair the existing task, add regression tests, and return for validation.
- **Untested:** Run missing checks and document unknowns rather than claiming success.

IE has a separate canonical registry and remains independently deployable. Reusable capabilities cross the boundary only after provenance, license, authorization, and maintainer review. Do not copy IE customer data, credentials, or proprietary business logic into this public repository.

## CI scope and current limitations

`node scripts/validate-roadmap.mjs` checks registry syntax, unique identifiers, phase/status validity, acceptance criteria, dependencies, cycles, and minimum evidence links for advanced statuses. The workflow validates pull requests and changes to `main`.

This is **repository-native roadmap governance**, not yet a hosted multiuser roadmap UI or database-backed orchestration service. Future tasks may add issue synchronization, concurrency protection, audited status transitions, independent QA automation, and a web interface once an MVP workflow proves the need.

**Review before adoption:** This file and the task registry are proposed changes until the PR is approved and merged. No automated feature integration or production deployment is authorized by these documents.
