# EXP-3 — Three Isolated Engineering Tasks Converge into One Recommendation: Scientific Run Report v0.1

**Executed:** 2026-11-22 (local container, Python 3.13.5). **Repo:** Foromni-Network/forOmni; branch `research/global-agent-roadmap-execution`. **Status:** SYNTHETIC EXPERIMENT EXECUTED; local unit/integration acceptance checks passed; no remote CI, independent external reviewer, deployment, merge to protected main, actual provider agents or real policy authority.

## Research question and hypothesis

Can three independently specified, separately implemented *software slices*—(A) source-bound synthetic evidence filtering, (B) scoped synthetic authorization screening, and (C) uncertainty-aware agent selection—be assembled into one callable pipeline that produces a defensible **non-authoritative** assignment suggestion while preserving negative-case behavior?

**Exploratory hypothesis:** a combined pipeline will select a well-supported candidate from eligible synthetic agents and abstain/deny on invalid synthetic evidence and grants; a naive unadjusted historical-rate control will favor a 2/2 over a 35/40 candidate. **Scientific caution:** the first 8 tests were implemented and run before the additional 2 control/authority assertions were appended. This is an exploratory study followed by a replicated expanded suite, *not* a preregistered randomized trial. The fixtures and implementation were built by the same assistant; no blinded independent experimenter audited them.

## Frozen local synthetic task descriptions / acceptance

- **A / evidence:** `slices/evidence.py` extracts **accepted counts** from synthetic `Receipt` objects bound to expected source SHA, suite ID, independent evaluator *name* (different from worker), verdict `ACCEPT`. Duplicate or empty receipt IDs fail closed. Acceptance: reject stale, failed, self-attributed and duplicate examples. **Limitation:** an evaluator ID is only a string, not signed/verified identity; receipts and recorded source SHA are caller-supplied, and this is a fixture-level check.
- **B / policy:** `slices/policy.py` screens synthetic `AgentGrant` fields by project ID, task ID, capability, action, epoch and revoked/suspended flags; accepts only `draft_isolated` as a synthetic eligible operation. Acceptance: deny wrong project, wrong task, wrong epoch, revoked, suspended and protected-merge request. **Limitation:** no authenticated identity or trusted grant database; the check does not issue or enforce operating-system credentials.
- **C / ranking:** `slices/ranking.py` chooses from eligible evidence-bearing candidates with the Wilson 95% lower-bound heuristic. Acceptance: 35/40 ranks ahead of 2/2; no evaluated opportunities leads to no recommendation. **Limitation:** no workload, provenance, task-difficulty, spend or calibration adjustments.
- **Convergence:** `converge.py` composes A → B → C for one `TaskRequest`, emits one suggested agent, only eligible agent IDs and explicit `authority: NONE`, `integration_status: RESEARCH_ONLY`. No runtime grant or protected integration.

**Isolation notion:** three separately owned source modules with a frozen simple API shape, converged into a single local Python module, not three distinct Git branches, three running agents or externally authenticated team members. Never claim those capabilities were exercised.

## Exact reproducible code and test

Source snapshot (all files were confirmed identical to the local tested files using Git blob SHA checks after GitHub upload):

| Artifact | Git blob SHA |
|---|---|
| `slices/evidence.py` | `e9cced9b23844772e61af5b49b37b8d6cc20b492` |
| `slices/policy.py` | `12427ef1bf33b6d773070d1f1284bf5339adf3cc` |
| `slices/ranking.py` | `3ac895ae8f201f2ac721167f97e19f3e9be8531f` |
| `converge.py` | `841d57f26f89d95f6bdf51b290b879a465577afe` |
| `tests/test_experiment.py` | `01722596ca21430924b7a13be01e1514b35c25d6` |

**Source tree:** [research/exp3_three_task_convergence](../../research/exp3_three_task_convergence).

Run from repository root with a standard library interpreter (Python 3.10+ for the syntax used):

```bash
cd research/exp3_three_task_convergence
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v
```

No external packages, network services, secret API keys or cloud budget are needed.

## Actual observed execution

**Initial run:** 8 test cases, 8 passed, 0 failures or errors.

**Expanded replication after adding control and no-authority assertions:** 10 cases, 10 passed, 0 failures/errors; Python reported `Ran 10 tests in 0.002s` (not a benchmark-quality latency measurement).

| Suite | Cases | Result |
|---|---:|---|
| Task A source-bound evidence | 2 | Passed |
| Task B project/epoch grant screening | 1 (multiple negative grant inputs) | Passed |
| Task C confidence-aware rank | 1 | Passed |
| Integrated pipeline | 4 | Passed |
| Naive raw-rate control and no-authority output | 2 | Passed |
| **Total** | **10** | **10 PASS, 0 FAIL** |

### Control vs candidate treatment (deterministic synthetic fixture)

- Agent A: 2 accepted / 2 evaluated, raw rate 100%; Wilson 95% lower heuristic **0.342372**.
- Agent B: 35 accepted / 40 evaluated, raw rate 87.5%; Wilson lower **0.738876**.
- Naive raw-rate control suggested **A**; conservative, source-filtered/scoped candidate pipeline suggested **B**.
- A third Agent C had a synthetic project B grant, and was excluded from project A.
- The selection outcome follows the implemented heuristic by design, so it cannot establish that B will outperform A in real engineering. No prospective agent runs or outcome validation occurred.
- Synthetic `source_sha = 'a'*40` is a fixture marker, **not** an actual Git commit. `qa-independent` is a fixture label, **not** a cryptographically authenticated reviewer.

### Negative path observations

- Stale source digest receipt did not add trusted accepted count (in tests).
- Self-attributed QA identity did not count as accepted work (string inequality rule).
- Duplicate evidence ID caused a ValueError rather than credit inflation.
- Revoked, suspended, wrong project/task/epoch or merge action failed the eligibility function.
- No valid eligible agent yielded null suggested agent.
- All integrated outputs returned `authority: NONE`; no grant or credential issued.

## Measurement and scientific limits

**Observed:** code passed listed deterministic unit/integration assertions in a local container, exactly matched files uploaded to research branch, and produced specified recommendation; zero external services invoked for runtime tests.  
**Not observed:** actual independently authenticated source/evaluator, real work implementation by three autonomous agents, Git isolated branches/convergence merge, approval signatures, policy enforcement at tool gateway, negative authentication against a runtime, measured costs, risk calibration, CI or production deployment.  
**Metric:** tests passed 10/10; not 10 independent attempts. These are software assertions against a synthetic fixture, **not evidence of overall Foromni security or success rate**. No statistical significance/causal inference from single scenario; Wilson bound is a heuristic, not a validated predictive model.

## After-action: biggest gaps discovered

1. **High-priority:** evidence fields `evaluator_id`, `source_sha`, and `evaluated` are currently caller-provided. An attacker can invent syntactically valid receipts; fix via independent attested QA artifacts and true trusted source checkout, not more string comparisons.
2. **High-priority:** duplicate receipt IDs are caught, but repeated evidence under *different* receipt IDs can still inflate success; add independently issued attempt IDs and uniqueness constraints backed by immutable task/evaluator records.
3. **High-priority:** policy only compares synthetic input; actual isolated sandbox credentials, revocation epochs and cross-project confidentiality remain unproven. Future tests must assert rejection at the trusted tool boundary.
4. **Medium:** lack of task difficulty strata and verified full cost means rank is a toy discovery heuristic. Need matched randomized outcome trials, not assumptions about win rate.
5. **Medium:** historical receipt `task_id` is not cross-validated against an authenticated accepted-task registry; a real trust ledger needs project/task taxonomy and owner consent.
6. **Medium:** no second implementation team/independent evaluator. The local suite was authored alongside the candidate; full FOR-011 QA requirements are not met.

## Conclusion and next gate

**Local experiment verdict: PASS FOR SYNTHETIC SOFTWARE CONVERGENCE ONLY.** The three source slices converge into one callable program and the 10 software assertions pass. **FOR-007 readiness, independent QA and real multi-agent integration remain UNVERIFIED.** No protected source was changed.

**Next separately authorized research experiment:** introduce authenticated (or isolated simulated with explicit limits) independent evaluation receipts and a source/attempt registry, then benchmark repeat-attempt aliasing and revocation across *three real isolated branches or worktrees* with reviewer-controlled test code. Keep protected Git, release and live providers out until explicitly approved.

*Build today, so others can enjoy tomorrow.* ❤️🐂
