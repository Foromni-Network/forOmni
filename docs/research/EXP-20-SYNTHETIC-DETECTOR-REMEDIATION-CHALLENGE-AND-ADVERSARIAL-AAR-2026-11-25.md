# EXP-20 — Structured Agency Detector Remediation and Prospective Synthetic Challenge (Executed AAR)

**Date:** 2026-11-25. **Project:** Foromni-only research, branch `research/global-agent-roadmap-execution`. **Status:** 17/17 executable local tests PASS; 32 previous synthetic EXP-19 scenarios and a separately frozen, *same-author* 24-case challenge evaluated. No deployment, real MCP/server, live logs, owner credentials, protected merge, paid service, public vulnerability disclosures, or changes to frozen FOR-007.

## Research question and design

After EXP-19 exposed nine misses and two disputed false positives in the frozen EXP-18 detector, can a **revised structured rule detector** improve coverage of missing grants, unknown principals, unknown MCP tool operations and provider-effect mismatches while preserving a reproducible baseline?

**Controls:** `detector_exp18.py` copied byte-for-byte from EXP-19, SHA-256 `d766627d86c2efc7def1865b595a09f70cd1cb414c71065b5897083aa6508ee7`. Original EXP-19 corpus copied unchanged. A new 24-case challenge `challenge.py` was authored and SHA-256 frozen at `feab8c8517ff7d442b4ffa9a25d92c94818d547689fbf5ad9e83cc3c99795366` **before implementing the revised detector**. The same assistant designed both challenge and candidate; this is prospective synthetic fixture construction, **not independent blind QA**.

## Revised rule design

`detector_v2.py` adds a *synthetic* known-principal registry and MCP action allowlist, recognizes missing/revoked/expired/stale grants on mutating actions, alerts on mismatches between nominal read-only action and `privileged_effect=true`, detects cross-project effects despite public labels, accounts for replay with effects, and adds a low-severity advisory heuristic for a narrow malicious imperative text pattern.

**Important:** `principal`, `privileged_effect`, `grant_state`, `resource_project` and event type are caller-controlled dataclass fields. Neither authenticity nor the reality of the effect is established by these rules. They are **detections, not enforcement**. Tool descriptions do not bestow authority.

## Actual observed results

```sh
cd foromni_exp20_detector
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest discover -v
PYTHONDONTWRITEBYTECODE=1 python evaluate.py
```

Final local verification: **Ran 17 tests in 0.004s; OK**, zero final failures/warnings. The verification includes three deliberately passing negative controls that demonstrate vulnerabilities rather than protection.

| Suite | Original EXP-18 detector | Revised detector |
|---|---|---|
| EXP-19 development corpus, 32 cases (19 positives, 13 negatives) | TP 10, FP 2, TN 11, FN 9; precision .8333, recall .5263, F1 .6452 | **TP 19, FP 2, TN 11, FN 0**; precision .9048, recall 1.0, F1 .95 |
| EXP-20 new challenge, 24 cases (14 positives, 10 negatives) | TP 4, FP 0, TN 10, FN 10; precision 1.0, recall .2857, F1 .4444 | **TP 14, FP 0, TN 10, FN 0**; precision 1.0, recall 1.0, F1 1.0 |

**Do not interpret a 100% rate on 24 researcher-authored scenarios as external accuracy.** The threat and benign classes were selected and labeled by the author, who also wrote the revised rules. Sample is tiny, repeated/related themes, no independent labeling, and no natural traffic base rate.

The two EXP-19 false alarms `O07` (sanctioned high-volume batch) and `O12` (unsigned sandbox diagnostic webhook) remain unresolved because existing `Event` fields do not carry independently authenticated exemptions or environment metadata. Simply hiding those alerts would be unjustified; a qualified reviewer must adjudicate and specify signed exception semantics.

## Failures deliberately demonstrated

1. **Telemetry forgery:** an attacker able to rewrite all caller-provided security fields can convert a suspicious event into an alert-free event.
2. **Unknown prompt wording:** alternate instruction text evades the simplistic content heuristic. No language model was tested.
3. **Provider bypass:** a nominally safe event yields no alert, but that does not prove an authorized provider action or prevent direct out-of-band invocation. The detector is not an authorization boundary.

All three negative-control test assertions PASS because they successfully demonstrate these limitations.

## Exact reproducible evidence

Executable Python source/tests/cases, JSON results, unittest log and `SHA256SUMS` are in the conversation artifact **`foromni_exp20_detector_evidence.zip`**, with archive SHA-256 `2638e3c9c7e3ad257c80a1f05020d56dc72ca3a628075ec6e6e9a24d8052211d`.

| Executed artifact | SHA-256 |
|---|---|
| `detector_exp18.py` | `d766627d86c2efc7def1865b595a09f70cd1cb414c71065b5897083aa6508ee7` |
| `holdout.py` | `1f6c9c07f8f92ec7250e4859f29cad446e984e1b2515e3d1ba4f4870ec7abd33` |
| `challenge.py` | `feab8c8517ff7d442b4ffa9a25d92c94818d547689fbf5ad9e83cc3c99795366` |
| `detector_v2.py` | `956c43f88af4fc51e93b2c575820d4f7ea04c64147f4c5fb2a1193acefb91d99` |
| `evaluate.py` | `448566724ebb974ebe337f1eb42180abba2d93cea217096c6757a3b5febec331` |
| `test_experiment.py` | `ab8a255583c2304671f8eacd11e19437219ec4a3a7d96ab86ab257f48e0136ea` |
| `results.json` | `c927f3b1a8d93d032504ba66d3ae26e5ab99c8e669c424860c855990b202f93d` |
| `test_output.txt` | `f6ac78f0d9bddf9ebc35866da1deb22e42b11902288a6be2344bd8d6aa147a94` |

**Source location:** local artifact archive only; this GitHub report does not mean that the executable source was pushed into the Foromni repository or independently passed GitHub CI.

## AAR / actionable next decision

- **Next gate is provenance, not more keyword rules.** Normalize authenticated producer/source, trusted project/agent/task lease, structured actual provider-effect evidence and signed policy-exemption claims. An alerting function that trusts caller-supplied identity can be bypassed even if its fixture scores are perfect.
- Record rate-policy exemptions as separately granted and verifiable: environment, tenant, task/batch owner, window, signed authorization and expiry. Do not blanket-suppress invalid-signature webhooks merely because their payload says 'sandbox'.
- Continue to separate *security alert* from *denied authorization*: trusted gateway must block invalid action; detector independently reports what occurred.
- Have a different qualified reviewer own labels and unseen cases, and hold them until rules are frozen. Evaluate full precision/recall plus per-rule false-alarm rate on genuine event telemetry (with authorization/privacy safeguards).
- For public security research and future services, publish **baseline failure, modification, exact tests, residual bypasses**, and do not claim certified protection, independent QA or client readiness.

**Verdict:** `EXP20_LOCAL_17_OF_17_TESTS_PASS`, `EXP20_RESEARCH_FIXTURE_RECALL_IMPROVED`, `EXP20_INDEPENDENT_ACCURACY_UNPROVEN`, `EXP20_TELEMETRY_FORGERY_AND_DETECTION_BYPASS_OPEN`, `FOR007_UNCHANGED`.
