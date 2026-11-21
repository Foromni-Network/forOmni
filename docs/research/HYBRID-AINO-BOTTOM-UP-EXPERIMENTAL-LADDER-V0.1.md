# Foromni Hybrid AINO — Bottom-Up Experimental Architecture and Component Ladder v0.1

**Status:** Source-linked proposal. **No external code copied, cloned, installed, executed, tested, deployed or benchmarked.** No new projects or service accounts created.  
**Date:** 2026-11-21. **Foromni ONLY.** The Foromni × Internet Embassy study remains private within IE RRM and is not part of this work.
**Governance:** Preserves ADR-E0A-002 patch-only, independently observed source and separate QA. Current Foromni main was observed unprotected; no autonomous main writes.

## Central strategy: break it down, test it, rebuild only justified layers

Do not start with a clone of the existing Foromni app or a six-platform install. Start with a **one-task, one-worker, one-evaluator system**. Add a single research mechanism at each stage. Freeze task, model, source, environment and judge for matched comparisons, then measure overhead as well as any benefit. The research question is not “can we stitch tools together?” but “which mechanisms improve independently accepted work per full cost, with stable authority boundaries?”

**Foundational invariant:** Work history and telemetry may inform future routing; only external authentication and observed source/QA evidence can establish authorization and accepted outcomes.

## 1. Cases-to-capabilities matrix: choose mechanisms, not wholesale dependencies

| Studied OSS case | Source-observed mechanism | Small hybrid use | Initial approach | Code/license caution |
|---|---|---|---|---|
| [Rerun coworkers](https://github.com/rerun-build/rerun) | Persistent coworker identity, independent workspaces, shared provider connectors | Durable logical worker identity plus attempt/workspace mapping | **Independent compatibility interface**, not a Rerun fork | Root AGPL-3.0, distinct ee/commercial code and trademark boundaries in pinned case study; code reuse requires proper license review |
| [OpenHands ecosystem](https://github.com/OpenHands/OpenHands), [SDK](https://github.com/OpenHands/software-agent-sdk) | Agent Canvas front end split from coding SDK/automation/extensions | Optional replaceable coding-worker adapter | **No required dependency at H0**; later inspect SDK API/version/license before integration | Review each repo's actual license/dependency tree independently before copying or distributing |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Checkpointing, pending writes and interruptions | Local attempt/recovery ledger and checkpoint adapter | First record recoverable state minimally; compare real LangGraph checkpointing at H3 | Checkpoint deserialization and replay security must be assessed |
| [Temporal](https://github.com/temporalio/temporal) | Durable workflows, retryable activities and recorded event history | Optional durable scheduling and recovery under scale | **Defer**; never install Temporal plus LangGraph just to satisfy H0 | Workflow replay does not make Git/DB writes exactly once or restore expired authorization |
| [SWE-bench](https://github.com/SWE-bench/SWE-bench) | Exact patch against pinned source and independently run tests | Acceptance and no-false-green methodology | **Adapt evaluation principles**, not public benchmark contamination | Cache keys tied only to run/instance can be unsafe when candidate patch differs; use fresh evaluation identity and source SHA |
| [OpenTelemetry GenAI](https://github.com/open-telemetry/semantic-conventions-genai) | Agent/tool/model spans, token and duration observations | Correlate inference/tool traces with authoritative task evidence | Lightweight structured local log first; OTel SDK when needed | Telemetry is self-emitted and not identity/QA attestation; avoid raw prompt or secret capture |

**No compatibility, performance, license or security claim is established for a combined stack** until an authorized implementation checks exact current versions, transitive dependencies, and test results. Source snapshots are in the five existing source-pinned case studies.

## 2. Stable micro-contracts (proposed, tool-neutral)

```text
ObjectiveRevision
  objective_id, revision, accepted_requirement_digest, owner_approval_ref
TaskPacket
  task_id, objective_revision, base_sha, dependency_digest,
  allowed_paths, acceptance_case_set, budget_ref, expiry, assigned_agent_id
AgentRecord
  registry_agent_id, incarnation_id, provider_connection_ref, capabilities
Attempt
  attempt_id, task_id, incarnation_id, created_at, status, retry_of?
Candidate
  attempt_id, base_sha, patch_digest, candidate_sha_observed_by_source_reader
Evidence
  candidate_sha, evaluator_id, suite_digest, fixture_digest,
  positive_and_negative_execution, costs, grade, limitations
Operation
  operation_id, authenticated_principal, scoped_grant, requested_effect,
  observed_effect, reconciliation_state
TraceCorrelation (optional)
  trace_id, span_id, attempt_id, operation_id
```

Only trusted components mint effective grants or verified-source/evaluator records. An API token shared by several workers must not become their unique logical identity. Every external side effect needs source read-back or explicit unknown state, not blind retries.

## 3. Experimental ladder: one variable added at a time

| Phase | Candidate setup | Deliberate synthetic task | Primary uncertainty / hypothesis | Measurable blocker |
|---|---|---|---|---|
| **H0: evidence kernel** | One bounded worker and separately controlled local patch evaluator; no agent registry/orchestrator | Pure function fix (e.g. `normalize_slug` with Unicode and empty/unsafe inputs), or simple Python parser | Is candidate-source verification reproducible without false PASS? | Patch portability, correct source SHA, actual tests run, evaluation latency and human effort |
| **H1: stable identity** | H0 plus `AgentRecord` and `Attempt` journal | Two sequential tasks by same logical agent in different sessions | Can history be attributed without confusing runtime/provider keys? | Missing assignments, unbound attempts, duplicate IDs, access claims from worker |
| **H2: convergence contract** | H1 plus typed task packet, owner of interface and stale revision checks | Two-module Python library: parser producer + CLI consumer, with conflicting field-name variants | Does contract preflight reduce interface drift and repair attempts? | Contract mismatches, stale base, handoff rework time, net overhead |
| **H3: recovery** | H2 plus durable attempt checkpoint and brokered idempotent operation intent | Synthetic crash after patch handoff before acknowledgment | Does resume recover work without double effects or unauthorized retry? | Recovery latency, duplicate writes, UNKNOWN acknowledgments, lease revocation |
| **H4: observability** | H3 plus source-linked local JSON events or standards-based OTel spans if justified | Repeat task with model/tool retries and cost counters | Can trace data explain cost/latency variance **without** influencing independent grading? | Trace loss, missing cost receipts, high-cardinality fields, instrumentation overhead |
| **H5: workforce relationships** | H4 plus independent 1-agent versus 2/3-agent matched trials | Shared API/frontend or parser+CLI+data-contract integration | When do specialized agents produce more accepted integrated behavior than one worker? | Coordination variance, ownership conflicts, human-review overhead, idle time |

H0 is intentionally more rudimentary than the full-stack Collective Lab E0a: **H0 is a synthetic harness feasibility rehearsal, not a substitute for a full-stack E0a benchmark**. H0 may only be implemented or executed after a new explicit bounded authorization. Passing H0 does not mean E0a passed. After H0 proves independent evidence mechanics, return to the frozen Collective Lab contract for E0a, then compare control/treatment in E0b.

## 4. H0 smallest source code subject (design, not run)

Avoid importing external agent code at the first gate. Build a **throwaway function task** consisting of a starter implementation that intentionally rejects edge cases, a public behavioral specification and a separate reviewer-owned hidden suite. Example requirement:

```python
def normalize_slug(value: str) -> str:
    # Synthetic H0 behavior to be specified before experiment:
    # lower-case ASCII letters, preserve ASCII digits,
    # convert each run of ASCII spaces/hyphens to a single hyphen,
    # trim outer hyphens, reject unsupported input types.
    ...
```

The worker receives only the stub and public contract; its artifact is a patch. Independent reviewer owns the actual input/output oracle, verifies source SHA, runs positive and negative checks, measures time/cost and classifies every attempt. A simple deliberately wrong reference candidate can be used later to check that the evaluator actually rejects failures, **but no tests have been executed now**.

H0 must be explicitly **no external model** for an initial developer-only mechanical rehearsal if budget/authorization requires zero spend; a subsequent permitted worker trial can bring one selected coding agent. A no-model hand-built candidate checks the harness, not the AI workforce.

## 5. Baselines and attribution: prevent false gains

1. For each new phase, compare the immediately previous accepted phase (ablation) **and** a fixed H0 baseline. Use the same prompt/task variants, model/provider/runtime, allowed resources, independent oracle and time horizon wherever possible.
2. Prespecify task family and assignment; record all attempted runs including invalid patches, missing tests, infra failures, timeouts and uncaught security incidents. No cherry-picked successful cases.
3. Minimum recorded outcomes: accepted behaviors/test coverage, grade, time to independently accepted candidate, number of attempted repairs, stale-contract events, side-effect uncertainty, source integrity, model/host/QA/human full cost, evaluator failures and security incidents.
4. Report **overhead** explicitly: time/compute/effort added by identity, registry, recovery and tracing components. If overhead exceeds measurable benefit at a given workload, revert or defer.
5. Model tokens, span counts, commit count and agent chatter are not evidence of productivity. A successful H0 smoke is not a meaningful causal study and must not be described as one.

## 6. Bottleneck taxonomy and repair loop

```text
Bottleneck found -> classify root cause and confidence
 -> reproduce with minimal case and full evidence
 -> propose minimal mechanism/adapter fix
 -> rerun same frozen negative/positive oracle (after permission)
 -> compare to pre-fix + previous-phase baseline
 -> KEEP only if it improves accepted outcomes, reliability or safety
 -> otherwise ROLLBACK / DEFER
```

| Class | Example symptom | Boundary owner | Earliest relevant stage |
|---|---|---|---|
| CONTRACT | CLI expects `display_name` while producer returns `name` | Registry/contract steward | H2 |
| ATTRIBUTION | One provider key appears as three agents | Trusted identity mapping | H1 |
| AUTHORITY | Worker asks for unapproved GitHub write | Policy/operator | H0 and later |
| SOURCE | PATCH applied to stale base / dirty source | Independent observer | H0 |
| GRADING | PASS log but zero real tests | Independent evaluator | H0 |
| RECOVERY | Same external operation applied twice after timeout | Side-effect broker | H3 |
| TELEMETRY | Cost/latency missing for failed attempt | Reconciled cost ledger | H4 |
| COORDINATION | Two agents concurrently change shared contract | Task/dependency steward | H5 |
| ECONOMETRICS | More agents win only when failed runs excluded | Independent analyst | H5 |

Each issue should have a case ID, owning mechanism, evidence reference, smallest reproduction, workaround, risk and next comparison criterion. Do not turn every observation into a new roadmap feature.

## 7. Source reuse and licensing admission policy

Before *pulling code* from an external project rather than independently implementing a small compatibility adapter: inspect the target path's repo and file license and notices at a pinned SHA, dependencies and plugin terms, AGPL/GPL obligations when interacting over a network, commercial carve-outs, contributor attribution and source distribution choices; distinguish public documented API semantics from copied implementation. Record author/source and license compatibility **before import**. Default H0–H2 uses **original minimal Foromni research experiment code**; OpenHands/Rerun may be tested as adapters later only when a specific need is proven.

No inference of partnership, endorsement or rights to distribute external trademarks/artwork.

## 8. Stage advancement gates

- **Research now:** documentation, component interfaces, test hypotheses and synthetic task specs only.
- **Before H0:** scoped founder approval for disposable source, tests, worker/model (or zero-model mechanical rehearsal), safe runtime, independent evaluator, network restrictions, no-main-write, time/cost ceilings and teardown.
- **H0 -> H1:** reproducible independent source/QA evidence; no false green in a deliberately bad candidate; cost recorded.
- **H1 -> H2:** logical identity remains stable across sessions; permissions never derived from worker-provided IDs.
- **H2 -> H3:** mismatches/stale revisions are observed and refused, and acceptance is compared to simpler baseline.
- **H3 -> H4:** crash/retry cannot silently duplicate effects; missing acknowledgment remains UNKNOWN until reconciled.
- **H4 -> H5:** resource and cost coverage stable enough to compare teams without selection bias.
- **E0a/E0b:** separate full-stack reference-app gate, independent suite, full approval and no unauthorized integration.

## 9. New research decision

**Recommendation:** Adopt **H0 -> H1 -> H2 -> H3 -> H4 -> H5** as an experimental dismantle/rebuild ladder. Keep E0a as a later full-stack feasibility milestone rather than forcing the initial tiny harness to satisfy all production-like requirements. Investigate adapters based on failures observed in the immediately simpler experiment.

This is a research plan, not a request to execute unapproved tests or to expand Foromni main privileges.

*Build today, so others can enjoy tomorrow.* ❤️🐂
