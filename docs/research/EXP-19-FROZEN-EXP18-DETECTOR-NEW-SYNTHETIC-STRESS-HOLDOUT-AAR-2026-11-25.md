# EXP-19 — Frozen EXP-18 Detector vs New Synthetic Stress Cases: Executed AAR

**Date:** 2026-11-25. **Project:** Foromni research only; branch `research/global-agent-roadmap-execution`. **Status:** executed Python standard-library local evaluation, **8/8 verification checks PASS**. No real users, MCP services, webhook providers, production SIEM, credential access, protected merge or external security probes. **The executed source, fixtures, output and hashes are in `foromni_exp19_holdout_evidence.zip`**, attached to the research conversation; this report is the GitHub artifact, not a CI run or source-tree integration.

## Question and hypothesis

Can a **byte-for-byte frozen** EXP-18 structured detector generalize from its own 100 repeated matching fixtures to **32 newly authored scenario specifications** spanning deceptive benign content, missing grants and principals, unrecognized tool names, risky side effects masked as status reads, and event-signature anomalies? Compare to the EXP-18 keyword baseline.

**Hypothesis:** the structured detector will surpass the keyword baseline but lose some recall and precision relative to its original 100%-on-its-own-fixture result. This is a researcher's manually labeled holdout-*style* stress set, not an externally independently labeled dataset or a pre-registered clinical/statistical experiment. The author saw the EXP-18 detector before constructing these cases; adversarial stress design is intentional. Do **not** call these data independently blind.

## Frozen implementation and method

The unmodified EXP-18 `detector.py` was copied to `detector_exp18.py` and SHA-256 locked at `d766627d86c2efc7def1865b595a09f70cd1cb414c71065b5897083aa6508ee7`. `holdout.py` specifies 32 individually labeled synthetic scenarios (19 positive, 13 negative), `evaluate.py` runs both detectors without modifying either, and `test_holdout.py` independently checks dimensions, source hash, confusion matrices and exact error-case IDs. These are synthetic source records: fields like `privileged_effect` and `principal` are caller assertions, not authenticated evidence.

```sh
cd foromni_exp19_holdout
PYTHONDONTWRITEBYTECODE=1 python -W error::ResourceWarning -m unittest -v
PYTHONDONTWRITEBYTECODE=1 python evaluate.py
```

**Observed:** `Ran 8 tests in 0.002s, OK`, 0 warnings/errors. Scores from real local execution:

| Metric | Naive keyword | EXP-18 structured |
|---|---:|---:|
| Scenarios | 32 | 32 |
| Threat-labeled cases | 19 | 19 |
| True positive | 1 | 10 |
| False positive | 3 | 2 |
| True negative | 10 | 11 |
| False negative | 18 | 9 |
| Precision | 0.2500 | 0.8333 |
| Recall | 0.0526 | 0.5263 |
| F1 | 0.0870 | 0.6452 |
| False positive rate | 0.2308 | 0.1538 |

Compare EXP-18's original internally aligned dataset (55 TP, 0 FP, 45 TN, 0 FN): that was a designed fixture, not evidence of a generalizable real detection rate. **This stress test challenges that overconfident interpretation**, not a statistical estimate of live performance.

## Concrete failure classes

**9 false negatives**:
- `O23`: missing grant on write.
- `O24`: unknown principal/agent, absent trusted identity registry.
- `O25`: unexpected unknown connector tool with benign-looking name.
- `O26`: untrusted tool text with instruction to export private records (the detector rightly ignores text as policy, but does not detect suspicious content).
- `O27`: privileged effect underneath a nominal `status_read`.
- `O28`: unauthenticated `system` write.
- `O29`: cross-tenant effect mislabeled `view_public`.
- `O30`: high-volume status_read with privileged effect.
- `O31`: replayed effect disguised as a status_read.

**2 false positives:** `O07` sanctioned high-volume internal batch was labeled benign but flagged `RATE_ABUSE`; `O12` a deliberately unsigned sandbox diagnostic webhook was labeled benign but flagged invalid signature.

**Label adjudication required:** A real detector may appropriately flag an unsigned webhook even when it claims to be sandbox diagnostic; conversely a large sanctioned batch may need an allowlisted signed exception. These labels are *policy-dependent*. The simplistic Event schema cannot encode authenticated exception authority or side-effect evidence. A security SME should re-adjudicate before any efficacy claim.

## Reproducibility

| Executed artifact | SHA-256 |
|---|---|
| Frozen EXP-18 detector | `d766627d86c2efc7def1865b595a09f70cd1cb414c71065b5897083aa6508ee7` |
| `holdout.py` | `1f6c9c07f8f92ec7250e4859f29cad446e984e1b2515e3d1ba4f4870ec7abd33` |
| `evaluate.py` | `502e2500c4a9f7491f9f323a4ad2ebca9ebca09d8d08f84de532cac7fa07b750` |
| `test_holdout.py` | `7a7cd248ed37cdb1b6623ef7fd437e72fa91b08c8ce4266aa5d59aba3a6f122a` |
| `results.json` | `e7afc3e95c8ce0e042d2b4dc006f81ffe39d2a16660055d463c8aaf6b7798c83` |
| `test_output.txt` | `0c619f81cc8079c464c1d56a6b1adbc0a1b58c8bd545cfd60c9c4cad9624d856` |
| ZIP `foromni_exp19_holdout_evidence.zip` | `687a7d85b48f1b377bd10fecf3ccbc798dbdb9d69b4117de5be6ffd41a4a2b6d` |

## Defensive design recommendations (not yet implemented)

- **Authenticated event provenance:** record trusted source, independently verified principal/project/action and actual provider effect/side-effect receipts rather than accepting client-supplied `kind`, `resource_project`, `privileged_effect` fields.
- **Default deny in the broker:** the enforcement plane, not the detector, must refuse unknown tool IDs, missing grants and unauthenticated principals.
- **Content inspection distinct from authority:** separately detect likely prompt-injection text and suspicious tool outputs *without treating them as instructions or granting privileges*. Use safe inert fixture strings for evaluation.
- **Real policy semantics:** signed batch exemptions, explicitly permitted diagnostics, rate policy per task/provider/tenant, and whether status read can ever mutate resources.
- **Independent held-out validation:** obtain new scenarios and adjudication from another reviewer *before* modifying the detector; freeze that set and measure alert fatigue, precision/recall by threat class and missing telemetry.
- **Portfolio and future services:** publish these *negative findings* as an honest case study; never use the old internally aligned 100% score as customer-facing product accuracy.

## Gate and conclusion

`EXP19_FROZEN_DETECTOR_STRESS_8_TESTS_PASS`; `EXP19_STRUCTURED_RECALL_10_OF_19`; `EXP19_INDEPENDENT_HOLDOUT_NOT_PROVEN`; `REAL_WORLD_DETECTION_EFFICACY_NOT_PROVEN`. FOR-007 untouched; no outreach/service launched. The next valuable experiment is a **separately authored, source-bound label adjudication and revised rule evaluation**, ideally with a qualified security engineer as reviewer.
