# Foromni Network Roadmap

**Status:** Initial direction-setting roadmap. Items are proposals until scoped, prioritized, and accepted by maintainers and contributors.

## North Star

Build a global collaborative network where people, businesses, communities, developers, and intelligent systems can discover one another, share reusable knowledge and capabilities, coordinate work, and create compounding value.

## Phase 0 — Foundation and trust

- [x] Establish the public canonical repository.
- [x] Preserve the original Foromni mission and motto in a founding charter.
- [ ] Publish organization profile, contribution guidance, and security reporting process.
- [ ] Establish issue labels, proposal templates, maintainer responsibilities, and decision records.
- [ ] Document project architecture principles, privacy boundaries, and threat model.
- [ ] Inventory historical repositories and recover reusable work without rewriting their histories.
- [x] Create an evidence-based discovery register structure (external project entries still pending research).
- [x] Define a repeatable upstream contribution and relationship process (initial proposal documented; community review pending).
- [x] Document the complementary Foromni/IE product boundary and selective shared-capability flywheel (strategic proposal; licensing, ownership, and maintainership decisions remain open).

**Exit criteria:** Contributors can understand the mission, find the roadmap, propose work, report security concerns, and see how external collaboration is handled.

## Execution MVP track — verified AI-native work (FOR-007..FOR-016)

**Status:** Proposed sequence and acceptance gates; research and selected local experiments exist, but the end-to-end founder-operable MVP is **not built, integrated, released, or independently certified**. This is a **parallel, explicitly scoped execution-MVP track**, not a replacement for the Phase 1 member/profile/discovery MVP (FOR-004/005). The two product capabilities can converge later through the shared member, project, permission and contribution contracts. Their sequencing and funding require maintainer approval.

**First deliverable:** A human creates a task → a stable registered AI worker obtains a bounded lease → performs work in a verified disposable sandbox → exports a patch → a separate observer reconstructs exact source SHA → independent QA evaluates real positive/negative tests → a human accepts, rejects or requests repair → attempt outcome and full cost become persistent history.

| Gate | Existing/new task | Exit required | Status |
|---|---|---|---|
| M0 — Contract freeze | FOR-007 | Versioned minimal objects, explicit scope, independent acceptance criteria and security authority | Proposed |
| M1 — Safe sandbox | FOR-008 | One runner meets verified filesystem, network, process, secret and resource controls | Proposed |
| M2 — Organization state | FOR-009 | Persistent Agent/Task/Attempt registry; stable identity and scoped leases | Proposed |
| M3 — First coding worker | FOR-010 | One actual agent produces a bounded patch, with costs and no source-host write authority | Proposed |
| M4 — Independent evidence | FOR-011, FOR-012 | Source observer, evaluator, immutable outcome and cost history; false green denied | Proposed |
| M5 — Human operating loop | FOR-013 | Authenticated task intake, decisions and repair without agent self-approval | Proposed |
| M6 — End-to-end MVP acceptance | FOR-014 | Repeated complete vertical-slice demo with positive, negative and interruption evidence | Proposed |
| M7 — Founder release readiness | FOR-015 | Reproducible build, approved mainline protections, independent QA and founder release gate | Proposed |
| M8 — Community expansion | FOR-016 | First independently verified external contribution; portable provenance and tenant boundaries | Proposed |

### What the existing research actually establishes

- **H0-M:** 18/18 *selected local mechanical classification observations* matched in three corrected repetitions, including wrong code, forged PASS, stale source and missing tests. Not an AI-worker test.
- **H0-S:** 24/24 *selected Linux DAC file-boundary classifications* matched across three repetitions. Same operator controlled setup; does not prove independent reviewer security.
- **H0-R:** a nested user/network namespace setup succeeded 3/3 under selected local benign probes; direct net namespace setup failed. Not a complete secure sandbox.
- **Open-source case studies:** Codex, Anthropic srt, Bubblewrap, NsJail, Rerun, OpenHands, LangGraph/Temporal, SWE-bench and telemetry are architectural inputs; not installed together, benchmarked, or integrated.
- **Open blocker:** Bubblewrap/NsJail admission, independent evaluator/runtime custody, real AI worker execution, persistent application integration, independently observed positive/negative security gates, and source-host protection.
- **Governance:** Foromni main was observed without branch protection in the research audit; do not permit autonomous main merges or claim release authorization.

Read the research records in `docs/research/` on `research/global-agent-roadmap-execution`, especially `HYBRID-AINO-BOTTOM-UP-EXPERIMENTAL-LADDER-V0.1.md`, `H0-SBX-R1-BUBBLEWRAP-NSJAIL-PAIRED-ADMISSION-MATRIX-V0.1.md` and `ADR-GLOBAL-OPEN-SOURCE-CONTRIBUTOR-SANDBOX-TRUST-BOUNDARIES-V0.1.md`.

### Scope discipline and rollout policy

- **Research kernel:** H0-M/S/R observations provide limited evidence, not a finished release. 
- **Founder execution MVP:** FOR-007 through FOR-015, one human, one task, one agent, one verified sandbox, one independently evaluated contribution, persistent record. CLI first is acceptable; global service hosting and polished dashboard are not prerequisites.
- **Open community pilot:** FOR-016 after the founder MVP passes; external contributors can bring their own compute and submit untrusted patches without receiving privileged organization credentials.
- **Later:** full-stack Collective Lab E0a/E0b, multi-agent comparisons, durable orchestration, brokered network permissions, agent marketplace and federated communities only when evidence/requirements justify them.
- No task advances to `batch_ready`, `build_ready`, `integration_ready`, `integrated` or `completed` without the machine-registry's evidence rules **and** actual independent gate decisions. Research commit counts and document authorship are not proof of tested functionality.
- New work is scoped to Foromni. No IE application, customer data, credentials, infrastructure or private cross-project case study is copied into this public roadmap.

**Release definition:** FOR-015 is *release-ready* only after controlled integration, independent source-bound acceptance and documented operator/safety procedures. A public deployment or release still requires its own separate authorization.

## Phase 1 — Network discovery MVP

- [ ] Define member and organization profiles with clear ownership and privacy controls.
- [ ] Define discovery and search use cases for people, projects, services, and capabilities.
- [ ] Define contribution records: what was contributed, by whom, under what license or permission, and how it can be reused.
- [ ] Design a simple onboarding and participation journey.
- [ ] Define moderation, abuse reporting, and community trust workflows.
- [x] Draft an architecture decision record for independent ownership, portability, provenance, least privilege, and interoperability (ADR-0001; proposed, not finalized).
- [x] Create a project relationship brief template covering mission, license, governance, contribution process, mutual value, and relationship status.
- [x] Draft a conceptual MVP domain model separating identity, organization, project, capability, contribution, relationship, proposal, and task (not yet a database/API schema).
- [x] Draft a capability exchange contract describing discovery, authorization, invocation, revocation, provenance, and human approval (proposed; transport and schema not finalized).

**Exit criteria:** A small pilot community can create profiles, discover relevant participants/projects, and share contributions with explicit permissions.

## Phase 2 — Collaboration and compounding contributions

- [ ] Add project spaces and lightweight collaboration workflows.
- [ ] Add proposals, roadmap participation, and transparent decision records.
- [ ] Make knowledge and reusable assets attributable, searchable, and permission-aware.
- [ ] Define integration contracts for external communities and independent platforms.
- [ ] Establish contributor recognition based on useful, verifiable contributions—not speculative financial incentives.
- [ ] Pilot reciprocal collaborations: contribute useful work upstream and invite independent contributors to participate in Foromni where mutually beneficial.

**Exit criteria:** Independent participants can collaborate across projects and reuse contributions while preserving attribution and control.

## Phase 3 — AI-native operations interoperability

- [ ] Define a capability description format for tools, agents, services, and human roles.
- [ ] Define agent identity, authorization, scoped permissions, and human approval boundaries.
- [ ] Define portable task handoffs, status, provenance, and audit events.
- [ ] Define interoperability patterns and reference integrations.
- [ ] Build a safe demonstration in which independent operations can coordinate without sharing secrets or unrestricted authority.

**Exit criteria:** Two independently operated systems can exchange a bounded task or capability through documented, permissioned interfaces with auditable outcomes.

## Phase 4 — Open ecosystem and federation

- [ ] Support independently operated communities and service providers.
- [ ] Publish stable APIs and compatibility guidance.
- [ ] Establish conformance examples and community-maintained integrations.
- [ ] Explore federated discovery and portable contribution records.
- [ ] Develop sustainable stewardship and funding options with transparent governance.

**Exit criteria:** External communities can participate without surrendering control of their own infrastructure or identity.

## Explicitly deferred

The following are not part of the initial MVP commitment:

- XRPL token reissuance or distribution.
- Recurring airdrops, inflation, token-backed voting, or treasury mechanisms.
- Financial promises, investment features, or token-based access gating.
- Unrestricted autonomous agents or cross-organization credential sharing.

Any future token or financial mechanism requires separate product justification, community governance, legal review, security review, and an explicit founder/maintainer decision.

## How roadmap work is accepted

Every implementation task should identify:

- Problem and intended users.
- Owner and collaborating contributors.
- Scope and acceptance criteria.
- Dependencies and security/privacy considerations.
- Relevant interfaces and data ownership.
- Evidence required for completion.
- Rollback or deprecation approach where relevant.

A roadmap checkbox is not evidence of implementation or validation. Mark work complete only when its acceptance criteria are met and the evidence is recorded.
