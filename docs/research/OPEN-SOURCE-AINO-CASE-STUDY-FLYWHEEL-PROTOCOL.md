# Foromni Open-Source Case Study Flywheel — Research Protocol v0.1

**Status:** Proposed repeatable research method, not an automated scanner or authorization for outreach.  
**Date:** 2026-11-21. **Foromni only.** Existing Foromni research process remains separate from other projects.
**Initial examples:** EXTERNAL-CASE-STUDY-RERUN-BUILD-OPEN-SOURCE-AND-COLLABORATION.md; EXTERNAL-CASE-STUDY-OPENHANDS-AGENT-CANVAS-OWNERSHIP-AND-CONVERGENCE.md.

## Intent

Transform each unresolved AINO design question into an evidence-backed study of an existing open-source project. Produce a useful learning artifact first, map how its maintainers actually solve related problems, identify unanswered details without alleging product deficiencies, and only later suggest a specific, respectful contribution.

**Knowledge is the primary output.** Search visibility/backlinks and potential partnership are secondary effects, never the reason to manufacture superficial case studies or create spammy issues.

## 1. Standard case study sequence

1. **Choose one live research question:** e.g. persistent agent IDs; ownership; event provenance; branch-only Git writes; durable retries; independent QA; multi-agent communication; objective/resource optimization.
2. **Discover candidate OSS systems** through their official repositories, check product identity, current ownership and repo moves, licensing, current health/maintenance; do not assume the first famous project is the best.
3. **Select a case based on mechanism fit** rather than popularity. Prefer direct source evidence addressing a disputed architectural choice.
4. **Read current canonical docs and code**: README, contributor rules, architecture, modules, contracts, tests, CI and security policy. Pin a source SHA or explain when a link is moving.
5. **Describe precisely what exists**, distinguish documented intention from verified code paths, actual tests, runtime observations and independently reproduced proof.
6. **Crosswalk to Foromni:** what can be adopted as a concept, what is complementary, what remains uncertain, what fails Foromni's required trust boundary.
7. **Identify minimal useful outputs:** clarity about a contract; maintained docs/test fixtures; small issue reproduction; portability proposal or experimental benchmark.
8. **Document external contribution etiquette:** maintainer-directed issue/PR process, security disclosure, license/trademark boundaries, no implied endorsement.
9. **Commit the study in Foromni research branch**, cross-link previous studies and accurately label unverified claims.
10. **Only after authorization**, open a narrow discussion/contribution or run a controlled external-system experiment; track real outcome and community feedback without assuming collaboration.

## 2. Candidate project discovery map

| AINO question | Candidate open-source project | What to verify first |
|---|---|---|
| Persistent AI coworkers and model connections | [Rerun](https://github.com/rerun-build/rerun) | Actual runtime identity, per-coworker connection rights and shared workspace behavior |
| Coding workers and multi-backend execution | [OpenHands](https://github.com/OpenHands/OpenHands) and [Software Agent SDK](https://github.com/OpenHands/software-agent-sdk) | Current repo ownership, agent server contracts, sandbox and independent QA |
| Durable orchestration and checkpoint/replay | [LangGraph](https://github.com/langchain-ai/langgraph) | Thread/checkpoint semantics, interrupts and protected side effects |
| Durable workflow service with retries | [Temporal](https://github.com/temporalio/temporal) | Activity idempotency, durable history and workflow determinism |
| Provider-independent multi-agent messaging | [AutoGen](https://github.com/microsoft/autogen) | Current maintenance direction, agent messaging protocol, active branch and ecosystem |
| Git host admission/integration | [GitHub merge queue documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue) / other CI OSS | Required checks on prospective merge-group, exact SHA/source and policy enforcement |
| Code agent evaluation | [SWE-bench](https://github.com/SWE-bench/SWE-bench) | Task split validity, ground-truth acceptance, repository contamination and metric caveats |
| Agent telemetry | [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-specification) | Identity/provenance and cost events without personal secrets |
| Agent context and tools | [Model Context Protocol](https://github.com/modelcontextprotocol/specification) | Tool identity, consent, permissions and protocol version compatibility |

This is a **curated question-to-repository map**, not a claim that each project solves the problem end-to-end or is open to collaboration. Verify current branch, license, source and maintainer priorities before writing each case.

## 3. AINO knowledge registry (conceptual; not built)

Each study should record:
- `study_id`, `research_question`, `project_name`, `canonical_repo_url`, `source_revision`, `observation_date`;
- `observed_mechanism`, `evidence_paths`, `confidence_level` (docs-described / code-inspected / test-executed / independent-reproduced);
- `foromni_mapping` (objective, roadmap, relationships, agent registry, work authorization, QA, merge, release, learning);
- `tradeoffs`, `threat_boundaries`, `licensing_concerns`, `open_questions`;
- `candidate_contribution`, `maintainer_guidance`, `interaction_status`, `human_approval`;
- `insight_status` (hypothesis, supported design pattern, experimentally verified) and `links_to_other_studies`.

Each change should preserve the source observation and update the finding rather than rewrite history to appear correct from the start. Avoid scoring OSS organizations as better/worse from incomplete evidence.

## 4. Discovery priorities after Rerun and OpenHands

**Next highest information gain:** LangGraph checkpoint/replay or Temporal execution durability. The research gap is how an interrupted agent resumes without duplicating protected side effects, while the state of the Git repo and task grants may have changed. An investigation should distinguish a runtime-replayed task from an *authorized* external write and introduce no redundant orchestration framework without evidence.

**Second:** SWE-bench/agent benchmark methodology to better freeze Foromni's independently evaluated full-stack task set and prevent reward hacking.

**Third:** OpenTelemetry or an agent observability implementation to align cost, source commit, task identity, completed behavior, human intervention and failure attribution.

**Fourth:** existing agent interoperability standards (MCP, ACP and others) to inform the dedicated communication-protocol phase only **after** the current end-to-end research exit conditions are met. Narrow protocol handoff notes remain in-tandem.

## 5. Research contribution ethics

- Credit maintainers and link canonical, version-pinned source; avoid copied brand assets and trademark confusion.
- Make the write-up useful to the studied community, not keyword-stuffed "backlink" content.
- Do not post unsolicited external PRs/issues/blog comments or seek endorsement without explicit approval.
- Treat possible vulnerabilities responsibly; use `SECURITY.md` and private disclosure when warranted.
- Respect AGPL, MIT, Apache and multi-license boundaries; inspect exact files before any code reuse.
- Prefer a small practical contribution over an unsolicited proposal to re-architect an existing product.
- When the real implementation contradicts our theory, **update our theory**, not selectively present favorable evidence.

## 6. Quality and outcome tracking

A useful case study needs **(a) a concrete research question, (b) pinned credible source, (c) correct mechanism, (d) actionable new knowledge, (e) limitations, and (f) a possible nonintrusive next step**. Backlink count and PR count are not substitutes for understanding.

Track whether the study changed an actual design decision, prevented redundant development, revealed a source-level invariant, improved benchmark validity or led to an accepted contribution. Only record collaboration when it occurs.

## What was and was not done

This is a repeatable research procedure and question-driven list. No scheduled crawl, social promotion, external contribution, partnership or integration has been executed or authorized. Case studies may be pursued within approved Foromni research; experiments and external interactions require their own approval.

*Build today, so others can enjoy tomorrow.* ❤️🐂
