# Research: Provider-Agnostic and Self-Hosted Agent Participation

**Status:** Research proposal; not an accepted architecture or implementation authorization  
**Updated:** 2026-11-20  
**Scope:** Foromni only, with no IE development, task, data, or integration changes  
**Related:** [Global Agent Roadmap Execution](GLOBAL-AGENT-ROADMAP-EXECUTION.md), [Many Branches to Mainline](MASSIVE-PARALLEL-TO-ONE-MAINLINE.md)

## Core proposition

Foromni's roadmap execution and convergence system should work with **any suitably authorized participant capable of producing a verifiable result**. This includes commercial model APIs, privately hosted contemporary open-weight models, **older/dated models**, small quantized models on consumer hardware, deterministic scripts, purpose-built expert systems, and humans.

**Model or provider brand must never be an intrinsic admission requirement.** The approval gate evaluates task-bound outcomes and verifiable provenance. An older model may be highly valuable for bounded extraction, formatting, low-risk test generation or classification—even if it cannot safely execute privileged code changes. Conversely, a powerful new model does not get automatic permission to merge.

**Separation of concerns:** Agent identity and rights belong to a verified actor/organization; model identity and capability are metadata about one worker attempt. A model is neither a legal principal nor independent evidence that work is correct.

## 1. Evidence from current ecosystem

- **A2A** specifies agent identity/capability cards, tasks, messages and artifacts between independent opaque systems. Its protocol/task states are communication constructs, not roadmap acceptance verdicts. Different protocol versions exist, so pin negotiated profiles rather than assuming every agent supports the same wire contract.
- **MCP** standardizes tool access and defines authorization for remote HTTP tool servers. It does not grant an agent blanket authorization or guarantee task completion. Negotiate version and limit tools per task.
- **vLLM** offers an OpenAI-compatible serving API for self-hosted inference. "Compatible" does not guarantee identical tool calling, structured output or multimodal behavior across arbitrary models.
- **llama.cpp server** supports OpenAI-compatible chat/completions endpoints, enabling small and older local GGUF models; individual model, chat-template, context length and tool-use support vary.
- **LiteLLM** provides examples of routing, rate limiting, budget tracking, failover and model grouping. If evaluated, it would be an optional adapter/gateway, not the mandated Foromni control plane. Its fallback semantics and spending controls must be tested; a free-to-paid fallback is not acceptable without task-budget authorization.
- **OpenTelemetry** provides vendor-neutral telemetry patterns, including GenAI usage attributes/metrics; traces and token counts are operations evidence, never task acceptance proof.

Sources (official/upstream pages inspected 2026-11-20):

1. A2A official spec: https://a2a-protocol.org/dev/specification/
2. MCP specification and authorization: https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization
3. vLLM serving guide: https://docs.vllm.ai/en/latest/serving/openai_compatible_server/
4. llama.cpp serving guide: https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
5. LiteLLM reliability: https://docs.litellm.ai/docs/router/learn/reliability
6. LiteLLM budget docs: https://docs.litellm.ai/docs/proxy/users
7. OpenTelemetry GenAI conventions: https://opentelemetry.io/docs/specs/semconv/gen-ai/

**Research caveat:** These documents describe tool capabilities; they do not establish that a particular vintage/quantization of model passes Foromni tasks, or that all API-compatible servers behave identically.

## 2. Strict four-layer compatibility boundary

**Layer 1: Foromni canonical work contract.** Versioned task spec, acceptance criteria, dependency IDs, risk, required permission scope, artifacts, expiry, completion evidence and reviewer decisions. Must not encode one model vendor's prompts or response format.

**Layer 2: Worker participation contract.** Actor identity, accountable organization, runtime/adapter ID, supported contract versions, capability claims, tool permissions, confidentiality class, resource limits, operational window, and contact/handoff endpoint. A2A may carry task messages; another compatible transport may also work.

**Layer 3: Inference adapter.** Provider-specific request/response conversion, tokenizer/context handling, tools, structured output, model sampling settings, error taxonomy, rate limits and metrics. Adapters explicitly advertise supported features; never fabricate capabilities.

**Layer 4: Evidence / admission authority.** Reproduces or independently verifies relevant outputs using trusted source systems, exact artifact digests, CI and integration test results. Outside workers have no authority to certify their own outputs.

**Critical rule:** Universal participation does not imply universal permissions, tool availability, task suitability or quality.

## 3. Proposed provider-neutral worker manifest

Illustrative **conceptual** fields (not an implemented schema):

```json
{
  "schema_version": "foromni.worker.v0-proposal",
  "actor_id": "orgA/worker-17",
  "organization_id": "orgA",
  "runtime": {
    "kind": "self_hosted",
    "adapter": "llama-cpp",
    "adapter_version": "pinned-version",
    "endpoint_visibility": "private"
  },
  "model": {
    "publisher": "declared-vendor-or-community",
    "identifier": "pinned-model-artifact",
    "revision_or_digest": "content-addressed-digest",
    "release_or_training_cutoff": "unknown",
    "quantization": "declared-or-none",
    "context_window_verified": 4096,
    "capability_attestations": ["text_generation", "json_with_validation"]
  },
  "trust": {
    "level": "untrusted_contributor",
    "permissions": ["read_public_task", "submit_candidate_artifact"],
    "data_classes": ["public"]
  },
  "resources": {
    "max_parallel_tasks": 1,
    "available_compute": "cpu",
    "max_estimated_cost_usd_per_task": 0.05
  },
  "interoperability": {
    "task_contract_versions": ["foromni.task.v0-proposal"],
    "transport_profiles": ["async_handoff_v0-proposal"],
    "structured_output": "postvalidated_only",
    "tool_use": "none"
  }
}
```

All capability data above is **self-declared until verified**. A model's training cutoff is useful task metadata, not an admission criterion; unknown should be allowed but freshness-sensitive assignments require retrieval and an independent source check. Do not publish private endpoint URLs, secrets or hardware fingerprint details unnecessarily.

## 4. Older models are first-class participants

Do not treat "old" as synonymous with "unusable". Evaluate tasks by observable capability and risk.

| Task class | Potential older/self-hosted role | Required safeguards |
|---|---|---|
| Reformatting and deterministic transformation | Often viable | Golden fixtures, schema validation, source preservation |
| Code indexing / file classification | Viable with targeted testing | Precision/recall spot checks; do not execute untrusted suggestions |
| Draft documentation / translations | Viable with review | Factual grounding, human/independent reviewer for publication |
| Unit-test suggestions | Viable as candidate generator | Tests must actually run and be checked for meaningful assertions |
| Bounded bug-reproduction research | Conditional | Read-only scope and reproducible observation |
| Code patches | Conditional and risk-tiered | Isolated branch, independent CI/security/functional review |
| Security or permission changes | No default authority from any model | Scoped authorization and specialist independent review |
| Protected merges / production deployments | Never delegated solely based on model pedigree | Explicit founder/maintainer gate and protected controller |
| Time-sensitive facts, dependency versions or live APIs | Model memory insufficient regardless of age | Authoritative current retrieval and linked verification evidence |

**Proposed competence registry:** Record benchmark results per **task family and versioned test suite**, not a universal model ranking. Confidence decays when inputs, dependencies or task expectations change. Revocation and re-evaluation should be routine. No capability or permission may be inferred from model parameter count, recency, vendor reputation or an unverifiable self-report.

## 5. Execution and routing policy

Start with **user/maintainer-assigned workers and deterministic routing**, not unconstrained autonomous model selection.

1. Resolve task risk, acceptance spec, privacy classification, freshness demand, necessary tools and budget.
2. Filter workers by organizational authorization, verified support for required capabilities, data locality and task contract compatibility.
3. Prefer least-privilege / lowest expected cost among qualified workers—not the newest model.
4. Attach immutable `task_revision`, `attempt_id`, `worker_id`, `model_digest` where available, `adapter_version`, `tool_policy`, `max_cost`, `deadline`, `base_sha` and input provenance.
5. Enforce task lease/fencing token. Execute in an appropriately isolated environment.
6. Normalize artifact packaging, **not** assertions of correctness.
7. Run deterministic validators, then trusted independent QA and authorized integration gates.
8. On failure, capture exact issue and allow repair, alternate model/human escalation or declined task.
9. If a fallback changes model/provider/data jurisdiction, **re-authorize** where policy requires. Never silently route confidential input from private self-hosted to public paid API.
10. Record observed outcome, monetary and compute/energy cost, handoffs, model category and provenance.

A fallback is a **new execution attempt** whenever its provenance, authorization scope, trust boundary, or validation semantics differ. Preserve both attempts.

## 6. Privacy, sovereignty and offline operation

- **Self-hosted does not mean trusted**: compromise, logs, insecure endpoints, supply-chain issues and unsafe tool execution remain possible.
- Self-hosted nodes should initiate an outbound secure connection or use an authorized private gateway; avoid broad public exposure of local model endpoints.
- Support on-premises, disconnected and intermittently connected agents with signed/canonical task envelopes, expiring grants and idempotent result upload after reconnect.
- While offline, a worker may continue safe local computation but **cannot assume its lease remains exclusive** after expiry. Late submissions become candidate artifacts requiring reconciliation, never direct state mutations or merges.
- Apply data minimization: public, internal, confidential, regulated/sensitive and restricted operational classifications; authorize each flow explicitly. Legal/regional constraints need separate review.
- Encrypt and authenticate channels, store secrets in scoped secret managers, minimize telemetry payloads; never include hidden chain-of-thought or unneeded personal information in shared trace logs.
- Never use external agent outputs, model cards or protocol messages as executable instructions without policy and schema checks.

## 7. Reproducibility and version pinning

An evidence record should identify: task/acceptance revision, original inputs or their approved digest, source revisions, runtime/container checksum, adapter version, model weight digest or hosted model snapshot identifier where provider exposes one, prompt/template version, decoding settings, tool manifest, data retrieval timestamp/source, test runner/CI run ID, outcome and reviewer.

For hosted services, exact weight digests may be unavailable. Mark `model_weight_digest=not_exposed` instead of pretending deterministic replay. Record other reproducibility boundaries.

Temperature zero is not a guarantee of deterministic inference across providers, hardware, batching, quantization or kernel versions. **Outcome-level conformance and independent checks** matter more than bit-identical generated text.

## 8. Capability conformance and vendor-lock-in tests

A provider adapter is admitted to a task class only after passing that task class's versioned conformance suite. Suggested checks:

- Can it read the task envelope and reject unsupported versions/required fields?
- Can it return the correct artifact manifest and error taxonomy?
- Does a minimal older CPU-hosted model successfully complete a deterministic task with no privileged tools?
- Does tool calling accurately obey allowlists where offered? A model lacking reliable tool calls must use an external deterministic runner or remain no-tools.
- Does malformed JSON fail validation rather than getting a green status?
- Does hallucinated CI success fail independent verification?
- Can a task be handed from cloud model to local model to a human, preserving artifacts and ownership without shared private prompts?
- Can disconnected devices reconnect without stale-lease writes?
- Does a prohibited confidential-to-cloud fallback fail closed?
- Are budgets enforced across retries/fallbacks?
- Does revoking an agent stop further submissions that would change authoritative task state?
- Can providers/models be switched while the **same task contract and independent acceptance rules** remain unchanged?

Success means different workers achieve the same verifiable *task outcome*, not that their outputs or internal plans are identical.

## 9. Test matrix for controlled research

| Cohort | Candidate configuration | Test hypothesis |
|---|---|---|
| A | Commercial hosted model | Baseline task correctness, latency, cost |
| B | Self-hosted modern open-weight model | Private execution with comparable outcome validation |
| C | Older local model with constrained context | Succeeds on suitable low-risk task classes |
| D | Small CPU-only/quantized model | Useful participation even on modest hardware |
| E | Deterministic script or rules engine | Some work does not require an LLM |
| F | Human contributor | Complete interoperability and independent-review workflow |

Use the same small synthetic tasks and pass/fail criteria; compare acceptance yield, independent reviewer time, task completion rate, recovery behavior, throughput, total resource cost, and privacy incidents (target zero). Split by task family instead of averaging across easy and hard tasks. **No tests in this matrix have yet been executed.**

## 10. Risks, tradeoffs and unresolved decisions

1. **Gateway portability vs lowest-common-denominator API:** Keep optional, separately negotiated capabilities; don't erase model-specific advantages.
2. **Open-weight vs open-source licensing:** A downloadable model is not necessarily open-source or commercially redistributable. Document licensing, permitted uses and contributor obligations per model/deployment.
3. **Evolving protocols:** Pin version/extension requirements; supply version adapters only where validated. No invisible protocol downgrades that strip security controls.
4. **Model provenance and trust:** Self-reported model names/weight hashes require deployment attestation or independent checks when risk warrants.
5. **Performance and energy:** CPU, consumer GPU, rented accelerator, local power, server maintenance and latency must be compared with paid APIs, not assumed free.
6. **Evaluation gaming:** Workers may optimize to fixtures, so rotate undisclosed acceptance cases and retain independent reviewer separation.
7. **Task assignment bias:** Track acceptance quality and failure rates, not only speed and price; protect against assigning all low-value work to small models.
8. **Version drift:** Providers retire models; community weights and runtimes change. Store versioned compatibility and requalification status.
9. **Global multi-tenancy:** Establish who is liable for bad actions, abusive workloads, privacy breaches and compute usage before open participation.
10. **Consent and agency:** Humans and organizations can revoke access without losing ownership of their artifacts or roadmap provenance.

## 11. Architecture decision: what Foromni owns

Foromni should **own and standardize**:
- Task contracts and acceptance semantics.
- Worker/organization capability attestation format.
- Attempt and lease provenance.
- Artifact/evidence envelopes and hash/revision binding.
- Independent QA, convergence/admission and release separation.
- Cost/outcome reporting and portable handoff packets.

Foromni should **not require or own**:
- The underlying model/provider.
- A particular agent framework.
- A single inference gateway or hosted GPU service.
- A particular orchestration vendor.
- Internal agent prompts and proprietary model weights.
- The contributor's infrastructure.

A2A, MCP, HTTP JSON, GitHub Actions, a self-hosted vLLM server, llama.cpp, or another runtime are **adapters**, not the source of truth.

## 12. Research-first next steps and decision gate

**N0 — Definition:** Freeze the vendor-neutral task/attempt/evidence/admission contracts as *drafts*, with explicit optional feature negotiation and backward-compatibility rules.

**N1 — Provider conformance study:** Document six cohorts above, exact fixture outcomes and trust limits; compare an older model and an offline model explicitly. Do not start hosted services or pay for models under this research directive.

**N2 — Global handoff tabletop:** Agent A (hosted) → agent B (older offline) → independent verifier (separate operator), including expired lease and rejected stale evidence.

**N3 — Security/privacy tabletop:** Simulate budget overruns, model spoofing, data exfiltration, downgrade attack, retries and unsupported tool calls.

**N4 — Decision:** Choose a minimal interoperable contract and pilot scope based on evidence. Major build work requires separate Founder authorization.

**Founder rule:** A model can be old, local, offline, inexpensive, or run by a different organization and still contribute. Only **qualified task evidence** advances roadmap state. No provider ever obtains integration or production authority merely by being the provider.

**No IE cross-project work. No runtime deployment. No production or paid compute.**
