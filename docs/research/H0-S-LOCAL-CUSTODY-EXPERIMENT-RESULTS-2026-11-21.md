# H0-S — Executed Local Custody/Permission Experiment (2026-11-21)

**Status:** Local experimental evidence collected, three controlled repetitions. **Not independently attested; not a secure arbitrary-code sandbox; no AI worker run.** Foromni-only.
**Predecessor:** H0-M first local experiment (18/18 expected classifications) and H0-PATCH-LAB-REPRODUCIBLE-HANDOFF-AND-FALSE-GREEN-CHALLENGES-V0.2.md.
**Artifacts:** `foromni_H0S_experiment_bundle.zip` and `foromni_h0s/EXPERIMENT_REPORT.md` attached to the ChatGPT experiment conversation (not replicated into GitHub).

## Experiment and observations

A root-controlled local experiment created a private evaluator directory (owner root, mode 0700; synthetic hidden fixture, QA token and verdict mode 0600), and a worker-owned writable directory (UID/GID 65534, mode 0700). Worker probes executed through setpriv with dropped UID/GID and cleared supplementary groups. Each probe was confined to synthetic paths and evaluator-file SHA-256 values were rechecked before and after.

| Challenge | Expected behavior | Three repetitions |
|---|---|---|
| Read hidden fixture | Denied | 3/3 matched |
| Write hidden fixture | Denied | 3/3 matched |
| Overwrite grading verdict | Denied | 3/3 matched |
| Read synthetic QA token | Denied | 3/3 matched |
| Symlink write into evaluator verdict | Denied | 3/3 matched |
| Write own candidate source | Allowed | 3/3 matched |
| Read private result file | Denied | 3/3 matched |
| List evaluator directory | Denied | 3/3 matched |

**24/24 expected classifications matched** over 3 repetitions; evaluator file digests were unchanged. Median duration for an eight-case repetition: **5.40863 seconds**. Python 3.13.5, Linux. No external API/model/cloud spend; local compute and human time were not costed.

## Observed blocker: H0-S-B01

Attempting to create a network namespace using `unshare --net true` returned **Operation not permitted**. Network egress policy and actual deny behavior were therefore **not established**. No external request was sent. This host **must not** be represented as an isolation environment sufficient for executing arbitrary malicious or AI-generated code with production credentials or network access.

## Other open limitations

- **H0-S-B02:** Same operator/root identity prepared worker and evaluator, authored all probes, and recorded outcomes. Distinct Linux UIDs are not independently controlled reviewer identities or third-party certification.
- **H0-S-B03:** Evaluator was not asked to execute malicious candidate code; evaluator sandbox, host-process isolation, and limits remain unverified.
- No remote GitHub permission denial, privilege escalation, full egress filter, cgroup, or secret-provisioning trial was performed.
- No real AI coding worker was used. Selected-case agreement does not estimate universal security reliability.

## Interpretation and next gate

H0-S validated a **narrow Linux discretionary filesystem-permission boundary under selected synthetic probes**. It **did not pass the full custody/security gate** needed before untrusted generated-code execution. Next stage must demonstrate a runner with independently enforceable network/host restrictions, distinct authenticated evaluator custody, and safe candidate execution before H0-A begins. Preserve the raw bundle and reviewer limitations. Do not introduce multiple orchestrators as a workaround.

**No merges, deployments, CI, source-protection changes, new services, IE access, or production data reads were part of this experiment.**

*Build today, so others can enjoy tomorrow.* ❤️🐂
