# External Open-Source Case Study: Rerun AI Coworkers and Foromni AINO Research

**Status:** Independent, read-only source review and collaboration hypothesis. **No Rerun code copied, modified, tested, forked or merged. No contact made.**
**Reviewed:** 2026-11-21. **External repository:** [rerun-build/rerun](https://github.com/rerun-build/rerun). **Snapshot reviewed:** `dev@2cf5cd6f268bac9fabdafff0b3a1c29caea6680d`; `master@24cb2da0158817977afaf214407c1e714b783905` observed on review date. Public docs/source may change rapidly; citations below pin the dev revision for reproducibility.
**Foromni scope:** Research and relationship discovery only. Internet Embassy remains separate and unchanged.
**Related Foromni studies:** AI-WORKFORCE-HOSTING-AND-SYNERGY-ARCHITECTURE.md, PERSISTENT-AGENT-REGISTRY-IDENTITY-AND-SHARED-CREDENTIALS.md, CONVERGENCE-WORK-PACKET-TYPED-CONTRACT-V0.2.md, FULL-STACK-CONVERGENCE-TRIAL-PREREGISTRATION-V0.1.md.

## 1. Why study this organization?

Rerun offers a publicly accessible AI coworker application and invites community issues, bug fixes, documentation and pull requests. Its operating model aligns with Foromni's questions about persistent agent identity, provider connections, delegation, shared memory, budgets, human approvals and multi-agent work.

**Relationship-first research hypothesis:** We can learn from the maintainers' actual implementation and may eventually offer a useful, clearly scoped contribution. Showing care means respecting their architecture, review bandwidth, licensing, commercial boundaries and product priorities—**not** proposing a partnership before establishing mutual relevance or treating their public work as Foromni's own.

**Disambiguation:** This is `rerun-build/rerun` at rerun.build, **not** `rerun-io/rerun`, the unrelated multimodal/robotics data project.

## 2. Verified source structure (repository documentation; no execution)

| Observed source feature | What the repository documents | Foromni research connection |
|---|---|---|
| Open source / licensing | Root LICENSE and package identify AGPL-3.0; README says some `ee` / cloud components carry a distinct commercial license; trademark policy excludes names/logos from general open-source grant | Evaluate an API/protocol integration first; avoid code reuse until AGPL/commercial legal review |
| Contribution route | `CONTRIBUTING.md` requests an issue for changes larger than a fix, branches from `dev`, PRs against `dev`, and checking tests/documentation; security issues go privately | Choose small maintainer-aligned contribution; ask before a large architecture proposal |
| App/engine architecture | `apps/ui` (Next.js and Supabase) and `apps/engine` (one engine per workspace), plus mobile, desktop and shared contracts | Study split control/UI and execution engine without assuming independently privileged worker isolation |
| Persistent coworker identity | Engine's agent registry/index has IDs/names/status; `agents/<id>/` has soul, config, memory, workspace, tools, run history and agent DB | Persistent IDs are **already present**; Foromni registry research can concentrate on task ownership, verified results and portable identity |
| AI provider connections | `connections/<id>` stores provider credentials and defaults; each coworker can point to a connection ID; connection can be shared | Confirms that unique agent ID does **not** require unique model API key |
| Workspace memory/collaboration | Per-agent local memory/db, `shared/` files, shared SQL DB, and `brain/` pages; `call_agent` messages persistent coworker and `delegate_tasks` spawns bounded ephemeral workers | Existing capability for handoffs and shared context; open question is authoritative task/contract graph and exact-source evidence |
| Approval / access | README describes approvals before consequential actions; API includes Vault items and agent associations; remote-computer tools offer user access requests | Verify actual policy granularity and approval paths before claiming independently enforced rights |
| Operability and testing | Documented source installation, CI checks, engine data migrations/reconciler, test commands and review expectations | Strong practical starting points for source-based comparisons and potential narrow OSS contribution |
| Shared execution limits | Engine guide explicitly says one process handles all coworker agents in a workspace and shell working directory is **not confined** to its per-coworker workspace | Per-agent file-first design should not be confused with process-level tenant isolation or GitHub file/ref authorization |

### Pinned source references

- [README](https://github.com/rerun-build/rerun/blob/2cf5cd6f268bac9fabdafff0b3a1c29caea6680d/README.md)
- [CONTRIBUTING](https://github.com/rerun-build/rerun/blob/2cf5cd6f268bac9fabdafff0b3a1c29caea6680d/CONTRIBUTING.md)
- [Engine README](https://github.com/rerun-build/rerun/blob/2cf5cd6f268bac9fabdafff0b3a1c29caea6680d/apps/engine/README.md)
- [Engine GUIDE](https://github.com/rerun-build/rerun/blob/2cf5cd6f268bac9fabdafff0b3a1c29caea6680d/apps/engine/docs/GUIDE.md)
- [Engine API](https://github.com/rerun-build/rerun/blob/2cf5cd6f268bac9fabdafff0b3a1c29caea6680d/apps/engine/docs/API.md)
- [Package manifest](https://github.com/rerun-build/rerun/blob/2cf5cd6f268bac9fabdafff0b3a1c29caea6680d/package.json)
- [Trademark policy](https://github.com/rerun-build/rerun/blob/2cf5cd6f268bac9fabdafff0b3a1c29caea6680d/TRADEMARK.md)
- [Security policy](https://github.com/rerun-build/rerun/blob/2cf5cd6f268bac9fabdafff0b3a1c29caea6680d/SECURITY.md)
- [LICENSE](https://github.com/rerun-build/rerun/blob/2cf5cd6f268bac9fabdafff0b3a1c29caea6680d/LICENSE)

The following are **source-documented claims**, not verified operational guarantees. The current assessment has not examined every implementation file, permission path or test run. Where isolation/approvals are described, do not equate a documented setting with security proof.

## 3. Convergence research crosswalk

| Foromni question | What Rerun already addresses | Gap to explore without presuming absence |
|---|---|---|
| One human account, many agent identities | Stable coworker IDs, own config/memory/run records, workspaces | Can authenticated external attempts be bound to accepted task IDs, PRs, exact Git SHAs and independent QA verdicts? |
| One API connection or key per agent? | Reusable engine-level provider connections selected per coworker; own per-agent MCP tokens and Vault associations | Do actual connector permissions enforce scoped Git write paths and worker-specific revocation? Need source-level and operational review |
| Delegation and coordination | Chief of Staff/Foreman, persistent `call_agent`, ephemeral `delegate_tasks`, team/run tools | Does the existing delegation protocol capture versioned task dependencies, authoritative ownership and stale source reassessment? |
| Shared company memory | File-first agent memories, shared file/db, brain pages and indexes | How are conflicts and authority handled in shared state? Can independent AINOs exchange *scoped* relationship evidence safely? |
| Convergence before coding | Docs/typed shared contracts, task runs, approvals and tooling | Could a lightweight external preflight packet reference task revision, API contract, source SHA and QA evidence without changing Rerun core? |
| Git mainline convergence | GitHub as an available integration; code changes flow through Rerun's own PR/CI practice | Does coworker Git operation enforce candidate branch, protected main, exact CI/QA and identity attribution? Do not assume so |
| Low-cost full-stack AINO | OSS self-hosting, BYO model connections, documented engine data and CI setup | Compare full *observed* cost and independent accepted outcomes in later authorized synthetic trial |
| Security and prompt injection | Human approval messaging, Vault and scoped coworker tools | Deep investigation needs private disclosure route for actual vulnerabilities; public study only documents architectural questions |
| Wider collective relationships | Tool integrations, experts directory and contributor program | Respect project priorities; offer research artifacts or a narrow upstream improvement that benefits Rerun users |

**Specific useful correction to our own research:** Rerun demonstrates that shared provider credentials and persistent coworkers coexist in one product. Foromni should not assume per-agent API keys are essential for identities. Focus on **authenticated action attribution, scoped Git write mediation, objective/contract ownership, source-bound evidence and outcome-based routing**.

## 4. Rerun's trust boundaries deserve careful treatment

The public engine guide says `fs_*` tools are rooted to private coworker workspaces, but the **shell is not confined to that workspace**. It also says the engine is one process for all coworkers in a workspace and provides a shared DB/file area.

These are architectural observations, **not a claim that we found an exploitable vulnerability**. Other deployment and host controls may constrain workers. We should not publicly label their implementation insecure without a verified security assessment.

For Foromni's end-to-end benchmark, evaluate:
- untrusted coding tool access and actual host/shell boundaries;
- connector token custody and whether a coworker can invoke another's privileged operations;
- trusted, unforgeable mapping of coworker/session/task to a brokered Git write;
- read-only vs branch-only vs merge authority, with current Git rules;
- independent QA controlled outside code-author principal;
- prompt-injection handling from PR comments, web and source docs;
- safe sandbox, credential revocation and forensic reconciliation.

If we ever find a reproducible vulnerability, use **Rerun's private SECURITY.md reporting process**, not a public issue or blog callout.

## 5. Licensing and commercial relationship boundaries

The public repository identifies its code as AGPL-3.0(-only) and says some `ee` components are commercially licensed. Rerun's name, logo and coworker characters are separately covered by trademark rules; Rerun Cloud may include commercial capabilities not available in the OSS build.

Before proposing code reuse or hosted modified derivatives:
1. Identify precisely which directories/packages and licenses apply; do not rely on the README alone.
2. Prefer documented APIs, contract tests, ecosystem contributions or independent research artifacts where practical.
3. If copying/modifying covered AGPL code, obtain qualified legal review of corresponding-source, network-interaction and distribution obligations.
4. Never imply Rerun endorsement, partnership, co-branding or permission to use their trademark.
5. Keep Rerun-source research notes and Foromni code/prototypes separated. No Rerun source was imported into Foromni.

## 6. Partnership ladder — earn trust before asking

**Stage 0: Study respectfully (current).** Identify maintainers' goals, published contribution guidelines and accurate overlap; document positive observations and unknowns fairly. Do not contact them yet.

**Stage 1: Be useful in public (future, separately approved).** Contribute a small, reproducible docs clarification, issue reproduction, test scenario or source-backed improvement that addresses a maintainer-valued need. Follow their issue-first guidance for nontrivial changes. Do not spam with unsolicited architecture manifestos.

**Stage 2: Share verified findings (future).** After Foromni runs authorized independent AINO trials, offer reproducible comparisons—especially negative findings and safety lessons—without implying Rerun was a participant unless it actually was.

**Stage 3: Invite collaboration, not acquisition (future).** Ask whether a narrow interoperability problem (e.g., task provenance/contract handoff) matches their priorities. Offer a co-designed study, adapter or contribution *only if maintainers welcome it*. Maintain independent ownership and licensing.

**Stage 4: Network participation (optional, mutual choice).** If there is sustained reciprocal value, explore Rerun as a voluntary ecosystem participant. No exclusivity, dependency, forced integration or premature Foromni membership assertion.

### Possible value for Rerun

- Research-backed task/source/QA attribution patterns usable by their coworker users.
- A compact, implementation-neutral "convergence preflight" checklist that can enhance safe multi-agent coding workflows.
- Accessible reproducibility/independent QA test fixtures and honest cost comparisons.
- Open-source docs/bug fixes accepted through normal maintainer channels.
- A new learning network of independent AINOs and contributors *if Rerun wants that relationship*.

### Possible value for Foromni

- Grounded reference implementation of persistent coworkers and shared provider connections.
- Real-world operational constraints to sharpen Foromni's proposed task/relationship controller.
- Existing contributor culture and tested software practices to learn from.
- Reusable patterns via standards and public APIs rather than blanket reimplementation.
- Potential long-term network relationship rooted in mutual work, not marketing.

## 7. Concrete questions to investigate next (research-only)

1. Which code paths issue and validate `call_agent` and `delegate_tasks` requests? Is recipient agent identity trusted, and how is authority bounded?
2. How are `connectionId`, Vault access, agent MCP credentials and tool switches enforced at runtime?
3. Do GitHub integration tools expose separate read, branch-write and protected-merge privileges?
4. How are tool-call events associated with agent, session, run, token usage, and accepted outcomes? Can these be exported with provenance?
5. Does Foreman coordinate dependencies via a task DAG, or primarily by prompts/sessions and team status? The answer requires code inspection, not inference from feature names.
6. Which Rerun documented APIs could accept an *external* task/attempt ID without modifying code?
7. What security/QA improvements are already on Rerun's issue tracker, and would a proposed contribution avoid duplicating current maintainer work?
8. Which small docs clarification or fixture would be genuinely helpful to Rerun's maintainers right now?

The questions are not findings of gaps. For the present, Rerun's **already shipped** coworker and connection model helps us narrow our own design scope.

## 8. An evidence-oriented next step

Without running Rerun or developing a new protocol, review targeted implementation files for coworker identity, connection selection, call/delegation permissions, Git integration and telemetry. Map each to the Foromni E0 reference application, then decide whether a **thin adapter** or simply a documented pattern is preferable to custom infrastructure. If later outreach is approved, prepare a short, respectful message proposing one concrete mutual benefit rather than asking them to "join the network."

**Research constraints remain:** no contribution PR, issue, external outreach, new Foromni Rerun integration, fork, deployment or live security test was authorized by this case study.

## 9. What this case study actually establishes

It establishes a strong **conceptual overlap** and a credible **collaboration pathway**, grounded in a verified open-source repository and published contribution process. It does **not** establish that Rerun has a missing feature, that it wants to partner, that its security controls are deficient, that Foromni is faster, or that any proposed approach has been empirically validated.

*Build today, so others can enjoy tomorrow.* ❤️🐂
