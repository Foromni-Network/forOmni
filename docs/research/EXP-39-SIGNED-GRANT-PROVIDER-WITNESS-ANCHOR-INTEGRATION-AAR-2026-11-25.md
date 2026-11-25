# EXP-39 — Task Grants, Provider-Signed Effects, Witness Checkpoints, and Anchored Head Reconciliation (Executed AAR)

**Date:** 2026-11-25. **Project:** Foromni-Network/forOmni, branch `research/global-agent-roadmap-execution`. **Status:** 25/25 local Python unittest checks passed in one run, `Ran 25 tests in 0.611s; OK`, ResourceWarnings treated as errors. No frozen FOR-007 changes, Internet Embassy modifications, protected-branch merge, production deployment, customer security testing or actual API effects.

## Hypothesis and scope

EXP-38 verified separately running provider/witness/observer identities but its mock provider mutation path had no task-scoped grant and checkpoint completeness was not independently anchored. Can the **protocol-level contracts**—signed mutation grant, provider-signed receipt, witness exact-ID checkpoint, and a separately persisted signed anchor head—be exercised together such that omitted effects, withheld witness entries, stale checkpoint heads, altered signatures and false claims remain unconfirmed or rejected?

**Scope qualification:** This is a **single-process integration regression fixture** with three separate local SQLite files, distinct Ed25519 keys generated/held by one experimenter, and in-process method calls. It is NOT a combined multi-UID/multi-host runtime, independent anchoring, independently secured key custody or actual provider API. The previous experiments' OS separation was *not carried forward* in this study.

## Architecture and observed result

- `Authority`: creates a signed narrowly typed `draft.create` grant, binding task, project, effect, action, expiry and nonce. The provider independently checks the signature and exact matching parameters before SQLite effect creation.
- `Provider`: its own SQLite effect ledger, one effect per ID, conflict denial and Ed25519-signed exact effect receipt. Same operator controls the provider key and ledger.
- `Witness`: its own SQLite checkpoint ledger with signed exact sorted effect-ID list, monotonically increasing sequence and a fork rejection rule.
- `Anchor`: separate SQLite signed expected checkpoint-head ledger, verifying witness signatures and requiring consecutive sequence. It can expose rollback, a withheld latest checkpoint or an inconsistent witness head *if the anchor itself remains trusted*.
- `Observer`: verifies anchor and witness signatures, checks exact checkpoint digest against anchored head, compares effect-ID sets with provider ledger and checks provider receipt signatures. Returns explicit `UNCONFIRMED_NO_ANCHOR`, `MISSING_WITNESS`, `WITNESS_ROLLBACK_OR_FORK`, `UNCONFIRMED_PROVIDER`, `PROVIDER_MISMATCH`, `INVALID_PROVIDER_RECEIPT`, and `CORROBORATED`.

## Execution

```bash
cd foromni_exp39
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v test_experiment.py
```

**Actually observed:** `Ran 25 tests in 0.611s; OK`.

Twenty-five checks include: authorized execution; missing/incorrect/expired/tampered grants; same-effect duplicate and task collision; full corroboration; signed fabricated witness claim; provider effect omitted from witness; anchored checkpoint with no witness entry; no anchor; tampered witness/anchor; anchor replay/fork; witness fork; old witness record under newer anchored head; changed signed provider receipt; unavailable provider; and three passing intentionally insecure negative controls (fixture key-holder can mint false signed work, provider may attest to wrong physical truth, and a single operator controls all keys).

**Passing negative controls reproduce weaknesses; they are not security wins.**

## Exact artifact hashes

Runnable experiment, tests, README, output and SHA256SUMS reside in the conversation artifact `foromni_exp39_integrated_evidence.zip`, SHA-256 `c5b3dd1ad322f3cf96250168e81a4c1ac9d628b5b650c428126da54ecc7a940d`.

| File | SHA-256 |
|---|---|
| `protocol.py` | `eb5b7404e4064198bb350a9bd5b614a9e8d7aa649fbf68d71d963c78c5d2c233` |
| `test_experiment.py` | `0d5a560abcf9e193dfa64d32af39d3d1845b28070848071a958d11dbdc3fd6b7` |
| `README.md` | `710386d61ed4838ad01a611feefdc0fff96d9c8dde07a102c788994a87de1c57` |
| `test_output.txt` | `68faf555007fdc23a3fac12dfb3173b1b7ab7345708a65003a83fc8ae49651d1` |

**This GitHub commit stores the scientific report only**; executable code and test output remain in the linked downloadable evidence archive, not an integrated Foromni application source branch or GitHub CI.

## Critical limitations

1. **Not distributed independence:** all signing keys, trust roots and databases are owned by one Python process/operator; separate DB files cannot resist a privileged common attacker or an issuer/provider lying in concert.
2. **Not complete event history:** an anchored list is only a signed declared set. Missing events *before anchoring* remain invisible, and a colluding issuer/provider/anchor can fabricate consistency. No authenticated external watermark, independent organization, third-party transparency log or real write-once system.
3. **Not provider-honest readback:** the observer calls the provider object's methods directly; no peer authentication, private key compartment or separate trust custodian. An attacker that controls the mock provider can falsify both SQLite state and signed receipt.
4. **Not full execution governance:** no grant revocation/epoch, cost budgets, historical read permission, race/concurrency, true crash-after-remote-effect ambiguity or actual MCP/third-party API. Those remain in separate prior experiments, not all together.
5. **Not independent evaluation:** developer authored and labeled all tests; no externally held challenge dataset, reviewer, signed source-bound QA or commercial readiness established.

## Next discriminating gate

**EXP-40:** rebuild this protocol with actual separately administered (or at least isolated Linux UID) authority, provider, witness, anchor and observer service boundaries; only accept provider effect records through authenticated IPC, and test malicious common-operator changes, missing-tail anchoring, signed-but-false provider claims, crash recovery and historical read grants. Freeze a reviewer-authored dataset and avoid production claims unless controls demonstrably survive compromised-component simulations.

**Verdict:** `EXP39_PROTOCOL_INTEGRATION_25_OF_25_PASS`; `SIGNED_GRANT_EFFECT_AND_ANCHOR_CONSISTENCY_REPRODUCED`; `INDEPENDENT_TRUST_AND_REAL_EFFECT_TRUTH_UNPROVEN`; `FOR007_UNCHANGED`.
