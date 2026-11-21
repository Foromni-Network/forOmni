# Persistent Agent Identity vs Shared GitHub Credentials — Agent Registry Research v0.1

**Status:** Foromni-only research design, not implemented, tested, merged or deployed.  
**Date:** 2026-11-21. **Purpose:** Extend end-to-end full-stack workforce evaluation with the *minimum* durable agent identity and evidence attribution needed for orchestration. Comprehensive communication protocol research remains queued.

## Founder insight

The human managing an AI workforce often operates through one GitHub account or one orchestrator connection, so all commits and comments can appear under that same identity. Giving each agent its own GitHub key might create traceability, but the deeper goal is an **agent registry that reliably knows which worker actually did which job, what it owns, where its expertise lies, and which other worker should contact it**.

The registry—not a proliferation of API keys—is the essential organizational memory layer.

## 1. Five identifiers that must not be collapsed

| Identifier | Purpose | Trust source |
|---|---|---|
| **Agent ID** | Persistent logical worker (e.g. UI steward); survives sessions and model changes | Trusted registry |
| **Agent incarnation/session ID** | Specific active process/model/runtime running as that agent | Authenticated worker enrollment / executor |
| **Task + attempt ID** | Specific assignment and bounded execution; retries are separate attempts | Accepted task registry + dispatcher |
| **Provider key/service account** | Access to inference service, costs and provider limits | AI provider/credential broker; may be shared via gateway |
| **GitHub principal/token** | API authorization and recorded forge actor; bot may represent multiple workers | GitHub App installation or scoped principal |

Commit author string and a self-proclaimed `agent_id` in a PR description are **not identity proofs**. GitHub App installation requests are attributed to the app, not automatically to the internal worker. If human user-to-server tokens are used, GitHub may show the user as actor; this still does not authenticate a specific AI subprocess.

## 2. Shared API key is compatible with unique persistent agent IDs

Two separate decisions:

**Shared provider connection, broker-mediated:** one project/organization manages inference billing and outbound model API calls. A trusted gateway tags authenticated `agent_id`, `session_id`, `task_id` and `attempt_id` before invoking the provider, meters tokens/costs, and enforces allowed models/data regions/budgets. Workers do not receive the raw provider key. This can support per-agent cost attribution *internally*, provided all inference traffic is forced through the gateway and usage telemetry is complete.

**Shared GitHub App credential, broker-mediated:** one authorized GitHub App installation can submit isolated branches and PRs on behalf of multiple registered AI workers. A trusted write broker verifies signed session/agent identity and effective task grant, scans the exact submitted diff/path/source revision and performs the GitHub write. The GitHub actor remains the App bot; the internal registry records the authenticated agent, task, attempt, action, source SHA and GitHub request/result identifiers. The public GitHub UI may require a bot-authored PR with signed/verified metadata references to show agent provenance; do not claim per-agent native GitHub authorship.

**Caveat:** Merely distributing the same bearer token to eight agents and asking each to label its commits is NOT equivalent. An agent that directly holds an unrestricted key can impersonate another label or bypass broker policy. When trusted per-agent authentication and exclusive routing cannot be enforced, the ledger's attribution is only an unverified claim.

## 3. Proposed agent registry model (research schema)

Conceptual entities (not database tables created yet):

- `AgentDefinition(agent_id, stable_name, capability_tags, declared_roles, owner_organization, policy_scope, lifecycle)`
- `AgentIncarnation(session_id, agent_id, authenticated_principal, model_version, runtime_provider, attestation_level, started_at, retired_at)`
- `AgentAssignment(task_id, task_revision, attempt_id, agent_id, session_id, effective_grant_ref, owned_paths_or_contracts, dependency_refs, lease_epoch)`
- `AgentContribution(contribution_id, attempt_id, source_commit_oid, pull_request_ref, affected_contracts, accepted_qa_ref, integrated_commit_oid?, status)`
- `RelationshipEdge(from_agent_or_task, to_agent_or_task, relation_type, contract_revision, observed_by, effective_from, expires_at?)`
- `RoutingEvidence(agent_id, task_family, accepted_outcomes, failures_and_censoring, total_cost, human_interventions, uncertainty, evaluator_version)`
- `InteractionEvent(event_id, authenticated_sender, intended_receiver, subject_task, purpose, artifact_refs, required_ack, outcome, timestamp)`

Agent IDs are persistent identifiers, not permanent personalities or guaranteed expertise. A new model version/incarnation can have different capabilities; routing must be calibrated to recent verified performance and avoid pretending historical results transfer unchanged.

### Minimal verified contribution event

```json
{
  "schema": "foromni.agent-contribution.v0.1-research",
  "agent_id": "ag-frontend-01",
  "session_id": "sess-demo-003",
  "task_id": "task-demo-12",
  "task_revision": 2,
  "attempt_id": "attempt-demo-05",
  "submission_id": "sub-demo-08",
  "requested_action": "submit_candidate_patch",
  "candidate_source_sha": "REAL_SHA_REQUIRED_WHEN_IMPLEMENTED",
  "authenticated_identity": "BROKER_MUST_VERIFY",
  "github_actor": "foromni-app[bot]",
  "broker_decision_id": "decision-demo-09",
  "independent_qa_verdict": "NOT_YET_ASSESSED",
  "integrated_source_sha": null,
  "status": "SUBMITTED_NOT_ACCEPTED"
}
```

This illustrative JSON confers no rights and is not a real GitHub record. Actual authority requires trusted identity, cryptographically authenticated transport, immutable-enough evidence storage, receipt/ref reconciliation and independently observed GitHub result. Keep candidate SHA and actual integrated SHA separate.

## 4. Registry relationships should answer real coordination queries

Examples:
- **Who owns this API contract?** Query accepted contract ownership, not the worker that last mentioned the API.
- **Who can resolve this failing migration?** Query verified outcomes on relevant task families, active capacity, current grant, model/runtime availability and uncertainty.
- **Whom should frontend contact?** Query dependency owner for current task/schema version; route a typed question with task/contract ref and required acknowledgement.
- **Which workers clash?** Compute overlapping effective ownership, shared critical dependency or file-modification risk, not merely same team name.
- **Which agent is best at this?** Estimate accepted outputs and total cost/risk conditional on task difficulty; avoid using completed task count alone.
- **Who caused this failure?** Link authenticated attempt -> source diff -> exact QA evidence -> merge and release effect, without assuming individual blame from a correlated incident.

Store relationships as **versioned, queryable evidence**, not merely an LLM-generated summary or a huge shared memory thread. Summaries help the planner but cannot be authoritative if stale or unsupported.

## 5. Task routing algorithm research: objective, constraints, learning

When assigning task t, choose agent a among *eligible* agents by:
1. Enforce security/rights, dependencies, workspace and capability restrictions.
2. Identify current owner of related interface/modules and downstream consumers.
3. Forecast probability of independently accepted completion, cost and latency with uncertainty calibrated to task type and current agent/model/runtime versions.
4. Model collaboration/review cost when the task involves shared dependencies.
5. Choose a reasonable assignment under budget, workload/QA bottlenecks and conflict risk; preserve deliberate exploration for uncertain agent skills.
6. After independently verified outcome, update calibrated routing evidence, including failures, timeouts and intervention cost.
7. Do not let an AI worker alter its own verified success score, role eligibility, QA requirements or grant.

Illustrative scoring function (not learned or tested):

```text
candidate_score =
  expected_verified_value
  - lambda_cost * expected_total_cost
  - lambda_delay * expected_critical_path_delay
  - lambda_collision * expected_coordination_loss
  - lambda_risk * bounded_failure_risk
  + exploration_bonus_if_policy_allows
```

A high-performing agent on easy work is not necessarily the right agent for a hard migration. Blocking noncompletion from the dataset would bias the registry. Estimates should reflect sample size, task mix and model drift.

## 6. Practical graduated architecture

**Small AINO (first baseline):**
- One human-managed GitHub organization and one registered coding agent with persistent agent ID.
- One tightly scoped GitHub App or controlled branch-write service; no protected merge authority in the worker.
- One common AI provider project/key held only by trusted runtime/gateway, or permitted dedicated service account. Internal ledger captures authenticated run/task attribution.
- Separate QA identity and immutable acceptance evidence.

**Three to eight agents:**
- Same GitHub App can represent multiple workers; authenticated distinct agent/session identities and separate task attempts.
- Isolated workspaces, effective leases and constrained Git writes through broker.
- Agent registry tracks API/module ownership and whom to contact.
- Separate inference keys may improve cost observability or blast radius but should be introduced based on actual provider controls/risk, not as the identity mechanism.

**Larger distributed AINO:**
- Federation of independently governed registries via permissioned identity/contract adapters where authorized.
- Separate credential domains for tenants/organizations; short-lived trusted workload identities, auditable delegation and revocation.
- Specialized providers/runtimes and adaptive routing with explicit uncertainty, not one global secret.

## 7. Experiment questions and evidence gates

Propose (after E0 full-stack reproducibility):
- **Identity continuity:** Can agent A restart or switch model without losing ownership/history, while old incarnations cannot keep writing?
- **Attribution:** If multiple workers share one GitHub App token, can a trusted observer identify agent/attempt/actual SHA without trusting self-labelled commits?
- **Routing:** Does registry-based dependency/expertise lookup reduce rework or improve verified outcome per total cost versus simple task-owner lookup?
- **Contact precision:** Can the controller route a schema question to the verified contract owner, and recover if owner is offline?
- **Revocation:** Does deactivating an agent/grant block stale writes while preserving prior evidence?
- **Cost:** Are shared inference credentials plus broker telemetry sufficiently complete for per-agent costs? If not, when do separate provider service accounts help?
- **Security:** Can untrusted README/PR text forge an agent identity or induce branch writes outside scope? Must fail at trusted policy boundary.

Keep identity/provenance experiments separate from provider-key count so the study estimates the effect of registry intelligence rather than secret topology.

## 8. Important limitations and authoritative references

- GitHub App **installation** requests are attributed to the app (not the internal sub-agent): https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation
- GitHub App **user-to-server** requests are attributed to the authorizing human user, with app usage indicated: https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-with-a-github-app-on-behalf-of-a-user
- GitHub Git commit author fields are editable metadata and should not be used alone as verified action attribution: https://docs.github.com/en/rest/git/commits
- OpenAI project service accounts and workload keys allow provider-level access organization; provider usage totals do not always identify which internal agent sent each request: https://developers.openai.com/api/docs/guides/api-keys ; https://help.openai.com/en/articles/10478918-reviewing-api-usage-and-costs
- Separate API keys/projects can improve revocation and security isolation even if a shared broker preserves internal attribution: https://help.openai.com/en/articles/5008148-can-i-share-my-api-key-with-my-teammatecoworker

**Conclusion:** Agent identity is not a key. The *agent registry is the source of persistent organizational identity and learning*, while actual signed/authenticated worker sessions and enforced Git/provider credentials determine what can be done. A common GitHub connection is compatible with individually attributable contributions **only when workers cannot bypass trusted attribution and permission boundaries**.

**No agent registry, credential broker, or Rerun connection was configured.** This is a research proposal within current end-to-end full-stack scope.

*Build today, so others can enjoy tomorrow.*
