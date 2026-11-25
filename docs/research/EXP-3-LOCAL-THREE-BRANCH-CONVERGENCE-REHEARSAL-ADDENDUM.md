# EXP-3 Addendum — Actual Local Three-Branch Convergence Rehearsal (Executed)

**Date:** 2026-11-22. **Follows:** [EXP-3 scientific run report](EXP-3-THREE-TASK-SYNTHETIC-CONVERGENCE-SCIENTIFIC-RUN-2026-11-22.md). **Scope:** local, disposable Git repository only. No Foromni protected main/shared branch merge, remote PR, CI, production operations, real agent collaboration, or paid service. This addendum extends the first report; it does not retroactively change the earlier experiment's initial limits.

## New experiment actually performed

1. Initialized fresh isolated local Git repository and configured a synthetic research author.
2. Froze integration contract `converge.py` and `tests/test_experiment.py` on base commit `a240f8052a0207159f0722ee39a16407e978ce55`.
3. Created **three separate local development branches from the same frozen base**, each containing just its source slice:
   - `exp3/task-A` evidence receipt validator @ `984e9dc6c04e64ae2c132f7a3659b0aabeee7670`
   - `exp3/task-B` project/task/epoch permission predicate @ `1ae8a68ec638ee5c68b25e4474057705786d6537`
   - `exp3/task-C` Wilson confidence ranking @ `b1247ff5404596d04a13b83e18e6356f2f43a62b`
4. Created local integration branch `exp3/integration` from same base, then cherry-picked the three commits in A→B→C order; all applied without conflict.
5. Independently re-invoked test command in **the resulting integration branch**: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v`.
6. Observed **10/10 tests PASS**, 0 failures/errors, source inventory of all five files present, and **clean Git working tree**. Local integrated Git commit `8a21b06be7473ad9ae096f1491adcf9274171f60`.
7. Compared exact resulting source blobs against files published to Foromni research branch; source paths `research/exp3_three_task_convergence/` match verified blob IDs in initial report.

## Results vs limits

| Measured claim | Actual evidence |
|---|---|
| Three separate development histories created from one frozen integration contract | YES — task A/B/C local branch SHAs above |
| Three contributions converged into exactly one integration branch | YES — cherry-picks A,B,C without conflict |
| Integrated code remains executable | YES — local Python interpreter and ten unittest checks passed |
| Source preserved on Foromni research branch | YES — exact five Git blobs verified |
| Protected-main convergence or remote PR accepted | NO — not attempted |
| True autonomous agents and authenticated task leases | NO — same author generated all three slices and commits |
| Independent evaluator principal, signed receipts, actual model task performance | NO — synthetic evaluation fixture only |
| Economic metrics or model comparison significance | NO — no paid API and single deterministic fixture |

**Important qualification:** These are actual local branches and cherry-picks in a disposable rehearsal. The 3 local branch refs are not pushed to GitHub as separate remote branches; only identical source files and test suite reside on Foromni's existing research branch. The local Git SHA provenance is reproducible by using a supplied local bundle but should not be presented as GitHub branch history.

## AAR for this additional gate

- **Promising:** simple shared interface and file ownership allowed three independent source slices to converge with no code conflict.
- **Still unverified:** asynchronous agent coordination, contribution ownership/authentication, integration controller concurrency, automatic issue/PR flow, source attested QA, exact per-task receipts, or protected-ref enforcement.
- **Next discriminating experiment:** three agents/worktrees with independent QA and source-bound attestations against a real trusted policy boundary; design under existing FOR-007 and FOR-011 without giving agents broad Git rights.

**Verdict:** `LOCAL_BRANCH_CONVERGENCE_PASS`, `SYNTHETIC_UNIT_INTEGRATION_PASS`, `PRODUCTION_CONVERGENCE_UNVERIFIED`. No authority escalation.
