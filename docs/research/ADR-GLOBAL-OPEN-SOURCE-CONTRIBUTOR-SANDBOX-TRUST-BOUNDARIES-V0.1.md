# Foromni ADR — Open-Source Global Contributor Sandboxes and Community Trust Boundaries v0.1

**Status:** Proposed research amendment, NOT implemented or independently security reviewed. **Date:** 2026-11-21. **Scope:** Foromni only. No IE systems, contributor accounts, runner installs, deployments or Git configuration changes.
**Supersedes no existing policy.** Companion to `H0-SBX-P0-MINIMUM-ENFORCEABLE-SANDBOX-POLICY-V0.1.md`, `H0-SBX-R1-BUBBLEWRAP-NSJAIL-PAIRED-ADMISSION-MATRIX-V0.1.md` and `HYBRID-AINO-BOTTOM-UP-EXPERIMENTAL-LADDER-V0.1.md`.

## The corrected organizational premise

Foromni is intended to be an **open-source AI-native organization** that welcomes members and contributors around the world. People may bring agents, code, connectors, models, goals, workflows and experiments. Their participation must not create implied trust in their identity, supplied source, prompts, runtime or credentials. A founder's single isolated local shell is only a research seed, **not the future global deployment model**.

The architecture must support community collaboration and experimentation while refusing to let one contributor's sandbox, branch, model or agent cross into another contributor's data or the organization-wide control plane without a specific, time-bounded grant.

**Core architectural invariant:** *Anyone can propose; no one can self-authorize acceptance or production effects.* Participation is open, privileges are scoped, and evidence is independently evaluated.

## Identity and trust dimensions — not one opaque "trust score"

- `human_member_id`: authenticated person or approved organization, distinct from GitHub username and pseudonym; privacy-preserving public identity can be separate.
- `agent_definition_id` and `agent_incarnation_id`: logical persistent agent and particular session/runtime; many agents may share a provider connection without sharing identity.
- `workspace_id`, `tenant_id` and `project_id`: explicitly scoped access and data boundary. Workspace membership does not imply Foromni administrative access.
- `task_id` and `lease_id`: signed/validated assignment, allowed source paths, current revision, constraints and expiry.
- `sandbox_id`: disposable isolated execution environment; not a persistent identity or authority.
- `source_sha`, `candidate_sha`, `evidence_id`: observed exact code and independent outcome records.

Trust is multidimensional: **identity proof, code provenance, capability entitlement, observed reliability, security posture and review accountability** must remain separate. Past success may inform routing but cannot grant new operational privileges automatically.

## Global contribution lifecycle (proposal)

```text
Public docs/specs + accessible participation rules
        |
Member proposes task / agent adapter / experiment / issue / PR
        |
Provenance + license + contribution/admission checks
        |
Task maintainer triage + permission/budget approval
        |
Per-attempt sandbox, scoped artifact/source access
        |
Untrusted patch/artifact + separately collected receipts
        |
Trusted observer pins exact source and dependencies
        |
Independent reviewer/QA and mandatory negative tests
        |
Community review and transparent decision history
        |
Maintainer-approved protected integration (later)
        |
Release authorized separately; learn from real outcomes
```

**No promise of guaranteed free compute for public users.** Foromni may support bring-your-own-compute, community-provided runners and metered hosted pools, but all must use equivalent evidence contracts with distinct authenticity and isolation classifications.

## Three execution/trust tiers, not three security claims

| Tier | Who runs code | Starting trust stance | Artifact acceptance rule |
|---|---|---|---|
| **C0 External contributor** | Person/agent on their own computer; may submit patches and logs | Source and self-reported tests untrusted; no host grants | Maintainer-controlled independent rebuild/test mandatory |
| **C1 Community sandbox** | Approved remote worker in a disposable project-scoped runner with constrained grants | Isolation assumed **unverified until independently tested** for that runner/host | Trusted source observer and evaluator must remain outside contributor's writable scope |
| **C2 Protected organization execution** | Trusted operator-controlled worker on explicitly isolated infrastructure | Higher operational responsibility, but no implicit release authority | Independent source/QA plus protected integration and separately approved release |

No automatic promotion from C0→C1→C2 based solely on model confidence, activity or reputation. Upgrades require authorization, current permission checks and auditable policy changes. C0 contributions remain welcome even without access to a hosted sandbox.

## Requirements early H0 runner research must preserve

1. **Runner portability:** define stable `create/exec/export/terminate` adapter contract, without assuming Linux kernel features available on every contributor's machine; contributor-local macOS/Windows execution cannot count as trusted Foromni runner isolation without explicit separate evaluation.
2. **Tenant/project isolation:** no shared writable checkout, model session, temp directory, artifact cache or QA suite across contributors; cache reuse requires cryptographic digest, scoping and security review.
3. **Network and software supply chain:** default deny host/prod access. Package installation and fetched dependencies become independently controlled operations later. Community-generated prompts, README files, GitHub PR descriptions and package scripts are untrusted input.
4. **Global participation:** asynchronous handoffs, UTC event timestamps, explicit locales/time zones, low-bandwidth artifact submission and resumable uploads; no requirement that all contributors use one proprietary provider.
5. **Access, affordability and fairness:** allow local BYO compute as contribution input, predictable shared resource budgets, no hidden paid-model prerequisite to participate in community QA or documentation; publish limits and allocation policies.
6. **Governance:** transparent criteria for triage, approvals, moderation, conflict of interest, security disclosures, maintainership and appeals; public roadmap/evidence but private vulnerability reports, secrets and personal details.
7. **OSS stewardship:** verify licenses and notices for each imported path, dependency and generated asset; plan contributor license policy and provenance (DCO/CLA choice requires project governance), clear contribution guidelines, security reporting and code of conduct.
8. **Privacy and jurisdiction:** minimize personal data, avoid copying private chat/tenant data into public logs, define retention/deletion and geographic hosting constraints before globally hosted services; review applicable law separately.
9. **Abuse/rate constraints:** identity and per-tenant quotas, fraud/DoS safeguards and resource spend ceilings apply at the policy controller, not by prompts alone.
10. **Independent acceptance:** authenticated reviewer and source custody required irrespective of how popular a contributor, agent or patch is. Evidence grade and permission status are not editable by worker sandboxes.

## Community-centered experiments to add AFTER H0

| Trial | Research question | Required outcome |
|---|---|---|
| **G1: remote untrusted patch** | Can an external contributor submit source without host privileges? | Maintainer rebuild, exact SHA and independent QA; no remote worker Git main rights |
| **G2: BYO vs hosted runner** | Can results from heterogeneous machines be reconciled? | Provenance and environment digests; only trusted evaluator results counted as accepted |
| **G3: tenant separation** | Can two projects run concurrently without exposing data/caches/credentials? | Independent negative access evidence and budget isolation |
| **G4: global async collaboration** | Can time-zone-separated people and agents hand off without stale contracts? | Revision-aware handoffs, duplicate/conflict detection, observed coordination cost |
| **G5: model/vendor neutrality** | Can different providers execute under the same task/evidence contract? | Matched QA oracle and total-cost reporting; no favorable self-grade |
| **G6: governance/abuse** | Can maintainers revoke member/agent grants during an in-flight task? | Current action-time revocation and no unapproved external effect |

These are future preregistration candidates, not tests already performed or authority to provision contributors.

## Consequences for the current Bubblewrap vs NsJail admission

Their immediate H0 safety requirements remain unchanged. Add **cross-tenant file visibility, cache boundaries, patch provenance, portability of artifact contracts and contributor-origin threat tests** to the eventual broader runner qualification. Do **not** overload a tiny H0 fixture with internet-wide hosting requirements; instead ensure the initial interfaces won't require breaking changes to support them.

**Decision requested of future independent reviewer:** confirm the contributor model, source contribution license/governance policy, hosted vs BYO trust classification, and minimum tenant-isolation gate before any public sandbox service.

**Current status:** Global community design requirement recorded; no assumption that Foromni is ready to accept and run anonymous remote code.

*Build today, so others can enjoy tomorrow.* ❤️🐂
