# Open-Source AINO Case Study 05 — OpenTelemetry, Agent Identity and Outcome Provenance

**Status:** Source-backed, read-only case study. No collector, instrumentation, backend, agent tracing, experiment or security test executed.  
**Date:** 2026-11-21. **Scope:** Foromni research only; Internet Embassy untouched. No outreach or external contribution.
**Primary snapshots:** `open-telemetry/semantic-conventions-genai@63df37263927c3d80da4668ad1541698751de7cd`; `open-telemetry/opentelemetry-collector@8e266ba207ab3ad93e3606578e3b56a5fbd47adf`. 
**Related Foromni:** PERSISTENT-AGENT-REGISTRY-IDENTITY-AND-SHARED-CREDENTIALS.md; E0-INDEPENDENT-ACCEPTANCE-EVIDENCE-AND-GRADE-DECISION-TABLE.md; EXTERNAL-CASE-STUDY-SWE-BENCH-ACCEPTANCE-EVIDENCE-AND-BENCHMARK-INTEGRITY.md; ECONOMETRICS-OF-CONVERGENCE-AND-COORDINATION-VARIANCE.md.

## Discovery: GenAI conventions moved repositories

A check of `open-telemetry/semantic-conventions/docs/gen-ai/*` found **moved** notices referring to **[open-telemetry/semantic-conventions-genai](https://github.com/open-telemetry/semantic-conventions-genai)**. This case study uses that new source. The lesson for Foromni's own research flywheel: source-verify canonical ownership at the time of study, not only the URL from an old article.

## 1. Mechanisms verified from source documentation

| Project/surface | Observed behavior or definition | Our interpretation |
|---|---|---|
| GenAI agent span conventions | `gen_ai.agent.id`, `gen_ai.agent.name`, `gen_ai.agent.version`, provider/model identifiers and create/invoke agent spans appear in maintained conventions | Traces can link *instrumented* agent operations, but a provider-assigned ID is not automatically Foromni's durable, authenticated organizational actor ID |
| Tool invocation conventions | `gen_ai.execute_tool`, `gen_ai.tool.name`, `gen_ai.tool.call.id`, optional arguments/results | Distinguish a model-supplied tool-call ID from trusted broker authorization or a GitHub-observed side effect |
| GenAI metrics | Agent/tool duration and usage/inference-call metrics are defined, with status/maturity distinctions | Valuable operational telemetry; not proof of accepted product outcomes or complete money cost |
| MCP spans | MCP client/server spans and tool-call semantic integration; cautions against double-recording execution spans | Link agent runtime/tool data and external-tool service telemetry without pretending duplicate spans are separate effects |
| Collector | Vendor-neutral receiver → processor → exporter pipeline for traces, logs and metrics; extensible components | Could export evidence to varied backends, but is *not* an authorization engine or independent source-of-truth ledger |
| Collector threat model | Explicitly separates unauthenticated traffic, authenticated telemetry and per-client context boundaries; config/components are operator-controlled trust inputs | A trace receiver can be attacked or fed false observations; authenticate inputs, isolate tenants, and don't let trace claims authorize actions |

**Pinned source:**
- [Maintained GenAI agent spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/63df37263927c3d80da4668ad1541698751de7cd/docs/gen-ai/gen-ai-agent-spans.md)
- [Tool execution spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/63df37263927c3d80da4668ad1541698751de7cd/docs/gen-ai/execute-tool.md)
- [GenAI metrics](https://github.com/open-telemetry/semantic-conventions-genai/blob/63df37263927c3d80da4668ad1541698751de7cd/docs/gen-ai/gen-ai-metrics.md)
- [MCP instrumentation](https://github.com/open-telemetry/semantic-conventions-genai/blob/63df37263927c3d80da4668ad1541698751de7cd/docs/gen-ai/mcp.md)
- [Collector README](https://github.com/open-telemetry/opentelemetry-collector/blob/8e266ba207ab3ad93e3606578e3b56a5fbd47adf/README.md)
- [Collector threat model](https://github.com/open-telemetry/opentelemetry-collector/blob/8e266ba207ab3ad93e3606578e3b56a5fbd47adf/THREAT_MODEL.md)

These are documented specifications; no claims about complete implementation of every convention in real Rerun/OpenHands workers or external provider SDKs.

## 2. Separation of traces from provenance and authority

**Traces answer:** Which operations called which tools, when, for how long, with what observed errors, provider, model and limited resource measurements?

**Authoritative ledger answers:** Who was allowed to do what *at that instant*, what real GitHub ref changed, what independent evaluator tested which SHA, what budget actually cleared, and what product/customer outcome was observed?

A worker can emit a fabricated span saying `gen_ai.agent.id=ag-qa-01` or `status=PASS`. A collector may faithfully transmit that span. This is **observability**, not identity attestation. Never treat self-authored telemetry, user-controlled span attributes, a Git commit author field or an agent's model text as effective GitHub permissions, independent QA, financial truth or outcome evidence.

**Foromni integration hypothesis:** Use OpenTelemetry conventions for causal operation traces and provider/tool performance; preserve an independent, authenticated policy and outcomes ledger that links those traces to externally verified facts.

## 3. Research architecture

```text
Founder-accepted purpose + task relationships (trusted revision)
                           |
                  Trusted task dispatcher
           authenticates worker incarnation + grant
                           |
                    Agent executes
              /             |            \
      Model inference   Tool calls      Git actions
           |                 |             |
   OTel GenAI spans/metrics and context propagation
           |                 |             |
           +--------- Collector ------------+
                           |
                  Observability store
              (signals, duration, errors,
               sample/cost estimates)
                           |
                    Join through vetted
              run/attempt/operation references
                           |
     Trusted ledger: policy decision + actual Git SHA
          + independent QA + billing evidence
                           |
           Research-grade accepted outcomes
       (with missing traces and uncertainty noted)
```

No part of this architecture was built or wired to existing Foromni infrastructure.

## 4. Suggested trace/evidence mapping, without abusing standards

| OpenTelemetry span information | Foromni-specific linkage outside/alongside spans | Trust caveat |
|---|---|---|
| Standard trace/span IDs | `run_id`, `attempt_id`, `operation_id` | Correlation, not authentication |
| `gen_ai.agent.id` | `registry_agent_id`, `incarnation_id` | Stable provider ID can differ from organizational persistent ID |
| Provider, request/response model | Account/project/ref and approved model policy revision | Record allowed provider and actual observed usage separately |
| Token usage & latency | Pricing schedule revision, retry bill, orchestration/host costs | Tokens are not money; invoices/usage APIs may lag |
| `gen_ai.tool.call.id` and tool duration | Trusted broker decision + GitHub API result/ref | Model-generated tool ID does not prove side effect occurred |
| MCP service call span | Credential/permission principal and action-time grant decision | MCP naming does not grant tool access |
| Error/exception events | Recovery attempt, failed request, uncertain acknowledgment | Failure to observe response does not prove external action failed |
| No OTel concept requiring QA acceptance | Independent evaluator identity and exact candidate/merge SHA | Acceptance must be externally verified, not inferred from traces |

For implementation, use documented standard fields where available, and a **clearly namespace-scoped Foromni research extension** for task/attempt/evidence correlation rather than inventing `gen_ai.*` standard names. Control high-cardinality labels: do not attach arbitrary task/commit IDs to every aggregated metric series. Such IDs fit tracing/log correlation, while metrics use bounded dimensions.

## 5. Why the privacy boundary is critical

GenAI tool arguments/results and model instructions may contain credentials, private content, customer data, or prompt injection. Maintained semantic conventions mark some of these as **Opt-In** and warn that their content may be sensitive. Default to **not collecting raw prompts, tool bodies, secret-bearing environment or files**; prefer redacted metadata, hashed or reference-only evidence, and minimal role-based access.

Collector logs/storage/exporters need configuration limits, retention, authentication, tenant segregation, endpoint restrictions and a recorded data-region/rights policy. Strong privacy can be compatible with complete task/operation accounting if the evidence system records the fact and result rather than the sensitive payload.

Never publish raw model conversations, connector tokens, private workspace content or third-party contributor information merely to make a public case study interesting.

## 6. Source-specific limitations

- GenAI conventions and metric names can carry **Development** or other maturity badges. Record exact schema/version alongside captures and plan migrations; do not assume universal stable semantics.
- The presence of `gen_ai.agent.id` does not mandate a universal cross-provider AINO identity service.
- Instrumentation can be incomplete, sampled, dropped, or altered by a compromised producer; missing spans are not evidence that work did not happen.
- A collector can be centrally hosted but should not be confused with a secure, immutable-enough independent audit log.
- A distributed trace describes *observed execution*, not necessarily *causal attribution* of AINO productivity improvements.
- No evidence here that Rerun, OpenHands or any given provider emits these conventions correctly in every version.

## 7. Testable questions for the first bounded Foromni experiment

1. Can an independently authenticated agent/attempt ID be reliably attached to OTel traces **without exposing credential secrets to a coding worker**?
2. Can a shared provider connection support meaningful per-agent telemetry from a trusted inference gateway?
3. What percentage of model/tool/Git operations are successfully correlated to authoritative task IDs and actual Git SHAs, and which are missing?
4. Can the independent QA observer detect fake 'green' claims in traces while preserving a valid code patch's evaluation?
5. Are provider token counts and price schedules sufficient for per-agent cost accounting? What human/hosting/CI costs are missing?
6. Does observability overhead reduce apparent productivity improvements at small agent counts?
7. Can trace content be redacted by default while maintaining recovery and failure analysis?
8. Do sample/drop/retention policies materially bias the econometric outcomes in difficult or failed trials?

**Evidence report should contain:** observed/correlated/missing operation counts, source-bounded acceptance results, total costs including telemetry, exact environment/agent/protocol revisions, and false-positive/false-negative attribution cases.

## 8. Collaboration opportunities

**First:** Credit OpenTelemetry maintainers and use their standard field names correctly in an independent, public methodology write-up.

**Second:** If Foromni discovers a reproducible *documentation* ambiguity about agent identity vs trusted actor identity, consider a minimal docs clarification after examining current OpenTelemetry issues and contribution guidelines.

**Third:** When a permitted synthetic trial exists, share example redacted spans paired with an independently verified GitHub/QA ledger; ask interested maintainers if the use case would help clarify agent-specific conventions.

**Fourth:** Explore interoperability with Rerun/OpenHands through adapters, not exclusive partnerships, only when their maintainers welcome collaboration.

No maintainers have been contacted, no PR submitted, and no conclusion that any repo is insecure or incomplete has been established.

## 9. Core AINO insight

**OpenTelemetry can help us see what a workforce does. The agent registry and independently verified evidence ledger must determine who did it, with what authority, and whether it truly contributed to the accepted objective.**

That separation strengthens Foromni's econometric hypothesis: useful routing requires trustworthy longitudinal work history rather than self-generated performance scores.

Next source-level priority: develop the minimal trace-to-authoritative-ledger correlation contract and a principled missing-telemetry rubric in Foromni's E0 research. Do not build a collector or analytics platform as an E0 prerequisite.

*Build today, so others can enjoy tomorrow.* ❤️🐂
