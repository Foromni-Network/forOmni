# AI Provider Connections vs Per-Agent GitHub Authority — Orchestration Research v0.1

**Status:** Foromni research architecture, not deployed, tested or authorized for operational integration.  
**Date:** 2026-11-21 · **Scope:** Foromni only. No Internet Embassy modification or cross-project connection.
**Context:** End-to-end full-stack experiment research; deeper inter-agent protocol work remains queued.
**Research companions:** AI-WORKFORCE-HOSTING-AND-SYNERGY-ARCHITECTURE.md; CONVERGENCE-WORK-PACKET-TYPED-CONTRACT-V0.2.md; FULL-STACK-CONVERGENCE-TRIAL-PREREGISTRATION-V0.1.md; PROMPT-INJECTION-PIPELINE-SECURITY-GATE-RESEARCH.md.

## Central decision

When Rerun or another orchestration platform runs multiple coding agents using ChatGPT/OpenAI or other AI providers, should every agent share one connection or hold separate credentials for GitHub?

**Answer to study:** Separate *identity*, *model inference access*, *repository write authority*, and *integration authority*. Sharing a model provider subscription/key has no inherent relationship to who is authorized to modify GitHub. A per-agent provider key does not automatically become an independently attributable GitHub identity.

Recommended hypothesis for a small AINO: **one trusted credential broker plus per-attempt agent identities and bounded policy leases; workload-scoped provider service accounts/keys as needed; narrowly scoped short-lived GitHub App installation tokens for authorized branch actions; independent QA and protected merger credentials held separately.**

Agents can still share one **billing organization/project** and a common task ledger, but should not share long-lived broad GitHub credentials in their contexts. Conversely, creating a separate GitHub personal access token for every agent is not sufficient: tokens must be tied to correctly enforced permissions, repository selection, credential custody, and an authoritative task-to-action mapping.

## 1. Four distinct identity/credential layers

| Layer | Example identifier | Purpose | Caution |
|---|---|---|---|
| AINO actor | `agent_id`, `attempt_id`, `work_packet_revision` | Operational attribution, ownership, scheduling, reason codes | A string in a prompt is not cryptographic authentication |
| AI model provider | OpenAI project service account/API key or workload federation where supported | Inference requests, usage attribution, budget and model access | Not a GitHub credential or authorized PR writer |
| Git forge | Short-lived GitHub App installation access token; scoped repo permissions | Read repository, create/update allowed source, submit PR | GitHub App permissions are generally repo/resource-level, not a native per-agent path ownership/branch lease system |
| Protected authority | Separate QA/check principal, protected merge service, release principal | Independent verification, merge/admission, deployment | Never expose to ordinary coding agent |

**Credential design warning:** A GitHub installation token is limited by the installed App's permission envelope and can be further narrowed by repositories and permissions at issuance. An individual fine-grained token may still offer broad write authority *within* a permitted repository. Restrict which refs it can affect with actual GitHub rules, a policy-enforcing broker, isolated fork/branch topology or write mediation. A label saying "frontend-only token" does not magically enforce frontend-only paths.

## 2. Compare three implementation patterns

| Pattern | Pros | Weaknesses | Research decision |
|---|---|---|---|
| Shared provider connection and shared GitHub PAT/token across every agent | Minimal setup; cheap for disposable prototypes | Weak actor attribution and revocation, one compromise reaches all permitted repos/refs; high prompt-injection impact | Reject for serious parallel automation |
| Unique AI provider key + unique GitHub PAT per agent | Stronger provider metering/rotation and GitHub actor differentiation if actually distinct principals | Credential explosion; static secrets; broad repo permissions possible; key does not establish task ownership | Possible controlled short-term fallback, not first choice |
| **Central credential broker; independently authenticated agent attempts; short-lived narrowly scoped GitHub App tokens or mediated writes; separate protected merge authority** | Fewer persistent secrets, policy checks, managed rotation, distinct task/attempt audit and revocation | Broker becomes security-critical; need robust identity binding, leases, Git ref checks, and revocation/reconciliation | **Preferred research architecture** |

One GitHub App may perform all branch writes on GitHub as the same bot identity. **Do not claim GitHub's own commit/API audit uniquely identifies the individual AI agent.** The broker must maintain attributable signed/immutable-enough internal actor/action/attempt events and branch/PR labels, preferably correlate them with GitHub webhook delivery IDs and commit SHAs. Commit author strings can be spoofed and are not identity proof.

## 3. Proposed minimal end-to-end flow (not implemented)

```text
Founder approves benchmark objective / scope / maximum cost
                            |
                      Task ledger
          accepted task -> versioned work packet
                            |
                Trusted dispatcher/broker
                  |          |          |
          AI provider    agent auth    GitHub App
          project /      + scoped      token service
          usage meter    work lease    (private key held here)
                  |          |          |
               Isolated per-attempt AI worker
               (Rerun or external sandbox)
                            |
                Request scoped Git operation
            task + attempt + branch + base SHA
                            |
              Broker checks current task/grant,
                repo/ref, budget, lease epoch
                            |
               Short-lived token OR trusted
                 narrowly mediated write
                            |
                   Isolated feature branch
                            |
                    Pull request/candidate
                            |
        INDEPENDENT QA (different authority)
                            |
          Protected merge queue / trusted merger
                            |
             Actual Git main SHA + evidence
                            |
          Staging, release, monitor separately
```

Important distinction: *GitHub App token issuance* can narrow repository and API permissions but typically cannot enforce a file-level lease by itself. A worker that receives `contents:write` can try to touch other files or branches to the extent allowed by repository rules. For truly exclusive path/branch boundaries, have workers produce patches in isolated sandboxes and let a trusted server validate base SHA, diff paths, task scope and branch then perform the write (or host-side ref restrictions plus trusted checks). Still defend against race conditions and semantics beyond path diffs.

## 4. What Rerun appears to provide, and what must be verified

Rerun's own published materials describe agents/coworkers, delegation, shared memory, retry/approval features, AI-provider BYO connections and a per-workspace cloud computer. This is vendor-reported capability rather than an audited guarantee about specific enterprise security behavior.

**Unverified questions before selecting Rerun as the experiment worker:**
1. Do different Rerun coworkers support independent tool credentials and connection ACLs, or does every coworker inherit workspace-wide connector access?
2. Can an agent be denied access to sibling agents' credentials, prompts, memory or browser state in the same workspace?
3. Can Rerun supply stable external agent identity (signed JWT / workload identity / webhook signing) suitable for a credential broker, rather than a user-controlled `agent_id` in a webhook body?
4. Is a per-coworker model provider key actually supported? Is accounting available per coworker, run and task, including retries?
5. Can each coding coworker run in an isolated workspace/repo branch or does a shared cloud computer permit cross-agent filesystem interference?
6. Are external Git operations mediated via separately granted MCP/tool connectors and an approval gate, or is there a single powerful GitHub connection?
7. Are webhook retries signed and idempotent? Can a caller verify the latest state rather than treating a callback as final truth?
8. What are audit log retention, administrative revocation, and data region/deletion controls? Can privileged secrets be hidden from model-visible context?
9. Can an independent evaluator run under a separate authority that coding coworkers cannot control?
10. Does the selected Rerun plan/workspace support necessary caps/permissions, and what are actual total usage costs?

**Do not assert per-agent GitHub authority is natively guaranteed by Rerun until its exact connectors/tool configuration is inspected.** If only a workspace-wide GitHub connection exists, use read-only connection to workers; route candidate writes through the trusted broker, or do not use that platform for privileged writes in the trial.

## 5. AI inference connectivity options

**One model provider organization/project, multiple workload service accounts:** Usually simpler billing and access governance. Separate production vs research and tenant data as required by policy; allow per-worker/role service accounts when practical, or a trusted inference gateway that tags each invocation with authenticated agent/task IDs. Multiple model keys need not imply separate billing entities.

**Per-agent provider API key:** useful for isolation, revocation and provider-level telemetry where supported. But per-key permissions may not encode a specific Git branch/task, and every extra secret increases operational burden. Usage charged to a key is not proof that a particular agent created a specific commit.

**Workload identity federation where available:** preferable to long-lived API keys for supported provider/identity combinations; verify provider support and infrastructure requirements. For a product called "ChatGPT" subscription, distinguish account/plan connector integration from **OpenAI API** project/service account credentials; they are not automatically the same authentication/billing path.

**Common inference gateway:** possible to choose models dynamically, centralize cost/rate/PII rules and record task tags, while giving each attempt an authenticated runtime identity and scoped model permissions. The gateway must not become a source of fabricated agent identity or silently route restricted data to a disallowed provider.

## 6. Specific GitHub permission map (proposal)

| Role | Repository read | Isolated source write | PR submit/comment | CI/QA verdict | Protected merge | Deploy |
|---|---|---|---|---|---|---|
| Planner | Scoped read | No | Draft plan only | No | No | No |
| Frontend/backend coder | Scoped read | Via broker on assigned candidate branch, validated diff | Submit candidate via broker | No | No | No |
| QA evaluator | Candidate read | No, except its separately owned test repo/ref | Record authentic check via trusted CI | Yes under independent principal | No | No |
| Integration lead | Target + candidates read | Integration-only via protected trusted actor | Review/queue | Verify independent evidence | Conditional protected authority | No |
| Release steward | Approved artifact and staging read | No source authoring | Release record | Review existing evidence | No | Separate human-authorized scope |

GitHub branch protection, rulesets, merge queues, required status checks, and distinct GitHub Apps/service principals should enforce as much as possible. Do not give every Rerun coworker a GitHub PAT containing protected-merge rights. When a single GitHub App is the writer, internal actor attribution and permission enforcement must be independently auditable.

## 7. Failure cases and pre-experiment oracles

| Fixture | Condition | Expected response |
|---|---|---|
| ID-1 | Two workers share same GitHub token and claim separate identities | Identify inability to prove independent GitHub authorship; do not accept agent self-label alone |
| ID-2 | Worker asks broker to write outside assigned paths | Broker rejects exact diff even with allowed API-level repo permission |
| ID-3 | Frontend worker requests protected main merge | Deny regardless of successful self-tests |
| ID-4 | Worker with revoked/expired grant retries delayed write | Deny with grant/lease epoch check; reconcile any previously completed write |
| ID-5 | Worker spoofs sibling `agent_id` in webhook | Verify signed principal/session; cannot elevate by payload |
| ID-6 | LLM reads README instructing it to use elevated connector | Privileged operation rejected by trusted service, regardless of model behavior |
| ID-7 | QA coworker has same workspace-wide GitHub write connection as coder | Independence review fails or isolate evaluator outside workspace authority |
| ID-8 | AI provider key reused by 8 agents | Internal per-run attribution must be proved by gateway; provider billing alone cannot attribute each task |
| ID-9 | GitHub App token leaked; short TTL but write-scope broad | Incident containment, revoke/rotate, inspect writes; no claim of absolute path scoping |
| ID-10 | Broker writes commit but reply/webhook lost | Query actual ref before retry; idempotency across task/attempt/action |
| ID-11 | Provider model switched mid-task | Maintain project data-residency, budget, task and revocation rules |
| ID-12 | Rerun returns successful coworker text but no actual candidate SHA | Not accepted as source contribution without trusted Git observation |

All are *proposed* synthetic fixtures; none were executed.

## 8. Trial comparison and econometrics

Compare:
- A: one powerful shared GitHub connection across all workers (only in carefully permission-limited synthetic controlled trials, not a recommendation for production);
- B: independent per-worker tokens/identities;
- C: central broker with ephemeral scoped permissions and protected mainline.

But **do not run this three-arm auth experiment before the first full-stack reproducibility study**. For E0, use one conservative bounded authority model; then change exactly one factor in a later trial.

Measures: independently verified integrated behaviors; latency/cost of broker issuance; credential lifecycle complexity; unauthorized action opportunities; false declines of legitimate work; attribution quality; recovery time from worker revocation; host and vendor limitations. A failed malicious write is a positive safety observation, not a productivity failure; legitimate denied work is separate false-positive cost.

Avoid falsely claiming "stronger safety" from zero incidents in a few trials. Run controlled attacks and evaluate effective authorization and real Git state.

## 9. Research conclusion

A powerful coordination layer does not require all agents to share the same GitHub power. The winning hypothesis is **shared objectives/data contracts and orchestration, but distributed, individually attributable scoped execution rights**. GitHub and AI provider credentials serve different purposes. Agent IDs, tasks and grants need a trusted binding outside prompts; independently authorized reviewers/mergers release accepted work.

**Immediate P0 next questions:**
- Which GitHub host rules/roles are available in a disposable Foromni research test repo?
- Which Rerun connector and worker identity controls are actually available without privileged shared credentials?
- Can the first full-stack test use a single read-only coding worker plus patch-submission broker rather than a custom full agent protocol?
- How much operational overhead does a broker add, and can it be deferred for the 1-agent baseline without weakening privileged boundaries?

**No credentials were created, no connected apps were reconfigured, and no live GitHub source write authority was changed.**

## Dated technical references

- OpenAI project service accounts and workload identity: https://developers.openai.com/api/docs/guides/api-keys
- OpenAI API key safety: https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety
- GitHub App installation tokens and narrowing permissions/repositories: https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation
- GitHub GitHub App vs OAuth permission model: https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps
- GitHub Actions OIDC for external cloud authority: https://docs.github.com/en/actions/concepts/security/openid-connect
- Rerun public product description/pricing/connection FAQ: https://rerun.build/pricing
- Rerun public orchestration overview: https://rerun.build/blog/ai-agent-orchestration
- Rerun webhooks/approval and provider access research leads: https://rerun.build/blog/ai-agent-api

*Build today, so others can enjoy tomorrow.*
