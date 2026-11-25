# EXP-18 — Defensive Agency Security Event Detection: Executed Synthetic AAR

**Date:** 2026-11-25. **Project:** Foromni only. **Research branch:** research/global-agent-roadmap-execution. **Status:** local Python 3 standard-library test run PASS (15/15). No actual MCP server, real webhook, threat feed, SIEM product, third-party attack, production monitoring or deployment.

## Question

Can structured event fields outperform a naive free-text keyword detector on a deterministic, labeled synthetic agent/MCP/webhook event corpus while yielding inspectable alert rule IDs and avoiding false alarms on benign status/public reads?

## Hypothesis and method

Two predefined detection strategies: (A) naive keyword/grant heuristic, (B) explicit structured detection rules for invalid webhook signature, cross-project resource request, expired/revoked/stale grant, replay, prohibited MCP operation, and high request rate. Inputs are 20 hand-authored scenarios repeated five times, yielding 100 synthetic records with labels **selected during detector design**. These are *not* 100 independent real events and the corpus was not independently blinded. Test threshold `attempts_5m >= 20` is an illustrative constant, not calibrated to real traffic.

Measured binary alert/no alert, precision, recall, F1, and false-positive rate; separate unittest checks of expected rules and benign exemptions. No live generation, remote probing or model prompt-injection trial. Tool text is treated as data, not a source of privileges.

## Actual local execution

```bash
cd research/exp18_security_detection
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v
python -c 'from detector import *; from fixtures import build_fixture; print(metrics(build_fixture(), detect))'
```

Observed **15 tests, 15 PASS**, zero final warnings, approximately 0.003s.

| Metric | Naive baseline | Structured rules |
|---|---:|---:|
| Number of events | 100 | 100 |
| True positives | 10 | 55 |
| False positives | 10 | 0 |
| True negatives | 35 | 45 |
| False negatives | 45 | 0 |
| Precision | 0.50 | 1.00 |
| Recall | 0.1818 | 1.00 |
| F1 | 0.2667 | 1.00 |
| False-positive rate | 0.2222 | 0 |

**Not real-world detection performance.** This nearly tautological result demonstrates a functioning regression fixture and reveals the weakness of keyword-only heuristics under these authored labels. It is not an unseen holdout, randomized A/B trial, threat-hunting deployment or generalized ML evaluation.

## Final executed artifact SHA-256

| File | SHA-256 |
|---|---|
| detector.py | d766627d86c2efc7def1865b595a09f70cd1cb414c71065b5897083aa6508ee7 |
| fixtures.py | 905a87eacf4ce6ecab97eb2710fd09c579436302ba935c652751c4690dd1a35e |
| test_detector.py | 0e2e4b5c21a613d9b005bdbd30b50913ec91915561e76c6f55661515a377eef6 |
| results.json | 99ad367ec7a7bd97cf9ac394a0ee165e75a197500e6237eaed80e9a95b2ef3a8 |
| test_output.txt | b99991e1b7022e36bdfd5d95cd943e763fada9e0e54e3ed7f8dffa7e0f8ee17b |

## AAR — useful outcomes and open flaws

1. Structured and directly inspectable rules provide deterministic evidence and prevent plain tool-description strings from granting authority; **no LLM was asked to process adversarial instructions**.
2. Coverage is designed to match the same known threat scenarios; a second independently authored, secret holdout set is required to measure generalization.
3. Enforce authorization in the trusted broker; a detector is downstream observability, **not an access-control boundary**.
4. Need durable and authenticated log provenance; currently fabricated event fields could induce alerts or suppress them.
5. Need alert dedupe, suppression, escalation severity and cost budget; not implemented.
6. Need privacy/retention rules and incident response operations before real customer data is accepted.
7. For a security services business, require independent qualified assessor, written scope/authorization, repeatable report and no unsupported certification or efficacy claims.

**Next discriminating experiment:** reserve independent-authored holdout scenarios that include benign behavior resembling attacks (e.g. human incident investigations) and adversarial events disguised as normal, add event-source authentication, then compare precision/recall and alert fatigue. Only consider public portfolio/outreach after explicit approval and public source/safety review.

**Verdict:** `EXP18_LOCAL_DETECTION_FIXTURE_15_OF_15_PASS`; `EXP18_REAL_WORLD_ACCURACY_UNVERIFIED`; `FOR007_UNCHANGED`.
