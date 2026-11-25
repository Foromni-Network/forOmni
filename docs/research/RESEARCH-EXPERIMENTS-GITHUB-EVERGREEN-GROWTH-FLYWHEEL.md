# From Open Research to Evergreen Education and Collective Growth

**Status:** Foromni strategy / editorial system research, NOT an approved social-media campaign, publication schedule, or integration with IE.  
**Date:** 2026-11-21  
**Scope:** Foromni collective-first. External publication, contributor outreach, subscriptions, paid promotions, and any IE operations require separate authorization.  
**Companions:** GLOBAL-COLLECTIVE-RESEARCH-STANDARD.md; EDUTAINMENT-WHY-CONVERGENCE-CONTRACTS-MATTER.md; REPLAYABLE-LEARNING-FAILURE-TO-IMPROVEMENT-TRACE.md; AI-WORKFORCE-CONTINUOUS-LEARNING-AND-EXPERIMENTS.md.

## Strategic thesis: evidence drives the growth flywheel

```
Real question from the collective
  → research + independent verification
  → reproducible experiment (when authorized)
  → versioned GitHub evidence package (including negative results)
  → genuinely helpful evergreen lesson
  → short/long educational content with source link and clear caveats
  → interested learners, testers, builders and community contributors
  → sourced feedback + new research questions
  → revised experiments, corrections, next verified outcomes
```

The audience is not merely an acquisition funnel; members can also be critics, fact-checkers, local-context reviewers, independent developers, educators, and maintainers. Keep individual agency and project ownership visible; no public commitment, scraping or forced conversion.

The core promise must be **"show your work"**, not "AI solved it" when evidence is incomplete.

## 1. GitHub as a research record, not only code storage

Proposed documentation package per completed experiment:
- `experiments/EXP-ID/README.md`: research question, authors, status and links;
- `protocol.md`: preregistered hypothesis, baseline/treatment, frozen acceptance rubric and stop criteria;
- `environment.md`: exact model/tool/runtime versions, hardware/host class, privacy constraints and cost accounting;
- `run-manifest.json`: machine-readable run IDs, sanitized artifact refs, source commit, dependency/version digests, independent judge;
- `results.md`: including failures, negative/inconclusive outcomes, confidence limitations, human interventions and cost;
- `reproduction.md`: what can be repeated safely without leaking secrets or real participant data;
- `lessons.md`: what is established, inferred, still unknown, and generalization caveats;
- `content-ledger.md`: approved claims mapped to results, figures, permits/licenses and publishing assets;
- `corrections.md`: transparent revisions/withdrawals after publication.

These are **proposed conventions**, not files created for actual experiment results. Never commit private keys, identifiable participant data, raw user transcripts, or restricted evaluation sets to a public repository. A citation is not a license; check redistribution rights.

Consider `CITATION.cff` when appropriate for a versioned research artifact; GitHub supports citation metadata on default branches. GitHub Releases can tag stable snapshot versions when actual publication is approved.

## 2. Evidence-based publication gates

- **RESEARCH_DRAFT:** hypothesis, source review, simulation; allowed narrative only when unmistakably labeled.
- **METHODOLOGY_REVIEWED:** independent methodological check, no results necessarily.
- **EXPERIMENT_RECORDED:** executed data, complete run and cost logs, immutable evidence refs, adverse outcomes.
- **INDEPENDENTLY_REVIEWED:** evaluator verifies claims against the permitted artifacts.
- **PUBLICATION_APPROVED:** content accuracy, participant rights, attribution, copyright, legal/privacy and scope approval.
- **PUBLISHED:** known URL and version linked back to source; comments and disputes monitored.
- **CORRECTED / RETRACTED:** edits preserve correction notices and avoid leaving misleading scheduled posts active.

Agents may draft and recommend; an editorial authority decides external publication. Draft/test stage should not be described as empirical demonstration.

## 3. Evergreen content pillars

| Pillar | Repeatable question | Suggested audience | Evidence/source |
|---|---|---|---|
| Agent engineering fundamentals | Why can 100 AI workers finish tasks without shipping a product? | Builders/founders | Convergence research; simulation labeled |
| Autonomous workforce operations | How do AI workers hand off, recover and stay within permissions? | Agent teams | Event and authority contracts |
| Open-source adoption | What should we adopt, extend or reject? | Technologists/maintainers | Upstream licensing and source-level assessments |
| Verified experimentation | Can 1 vs 3 vs 8 agents make a better full-stack app? | Builders/educators | Actual future experiments once run |
| Global collective lessons | How do different communities coordinate and validate outcomes? | Worldwide learners, researchers | Locally grounded public cases |
| Human oversight and autonomy | Where do humans remain accountable? | Owners/collectives | Security, privacy and policy research |
| Failure and repair | Why did a supposedly green change break when integrated? | Engineers/learners | Hypothetical case now, real postmortem only with permission |
| Real-world usefulness | Why is merged ≠ released ≠ beneficial? | Founders and public | Cross-domain outcomes contract |

**Avoid single-region bias:** feature translations, non-English primary sources, low-connectivity perspectives, different cultures/disciplines and respectful local context. Do not manufacture community endorsements.

## 4. Evergreen content atom template

Each reusable content unit should include:
- `content_id`, title/hook, intended audience, knowledge level and language;
- primary research artifact + exact revision;
- factual claims and source links; simulated/observed/tested labels;
- memorable demonstration or animation concept;
- one actionable practice/worksheet/quiz;
- a neutral call-to-action (read methods, challenge a claim, reproduce a fixture, suggest a local case);
- rights, credit, media license and accessibility requirements (captions, transcript, descriptive alt text);
- visual/story versions: 20–45s short, 60–90s explainer, 4–8 min deep dive, written article and source repository;
- approved publication owner and `last_fact_checked_at`;
- reevaluation triggers: upstream software release, new experiments, correction, changed standards or safety discovery;
- opt-in audience feedback and consent handling; no inferred personal traits for targeting.

Evergreen ≠ publish once and leave forever. Preserve stable conceptual teaching while refreshing evidence, library versions and dated screenshots.

## 5. Research-to-content sample campaign: "A Hundred Green Branches"

**Campaign status:** DRAFT CONTENT SYSTEM; no channels connected, posts scheduled or content published.

**Hub / flagship:** evidence-backed evergreen article and reproducible hypothetical UI/API mismatch exercise on GitHub. Headline: "Why 100 AI Developers Can All Be Green—and Still Break the App." Accuracy note: Git does merge without a formal Foromni contract; the issue is *reliability and scale*.

**Short 1 — Hook:** "100 AI agents. 100 green checks. Zero working product. What happened?" Explain an API contract mismatch; CTA to GitHub exercise; label simulation.

**Short 2 — Git myth:** "Merge isn't copy-paste." Show simplified branch and merge graph; link Git docs.

**Short 3 — Broken green:** "Your test passed—on yesterday's code." Bind evidence to actual source/merge group SHA.

**Short 4 — Who gets to merge?:** Human/AI authors vs protected deterministic gate; independent QA and approvals.

**Short 5 — After main:** "Merged isn't released." Show staging/rollout/feedback separation.

**Short 6 — The scientific method for AI teams:** "Our model suggested an improvement. We didn't immediately trust it." Explain controlled baseline/treatment; do not imply a trial ran.

**Deep dive:** One fictional software product delivered by solo vs 3 vs 8 agents; what would be measured, when additional agents backfire, why results are TBD.

**Evergreen worksheet:** `What is a convergence contract?` with task specification, API contract, evidence, authority, revision, release, and beneficiary outcome checks.

**Community prompt:** "What's the hardest integration failure you've personally documented? Share a non-sensitive sanitized example or reproducible public repo." Do not ask contributors to leak customer data, private repos or credentials.

**Attribution:** Credit source projects Git, GitHub, Zuul, Pact etc as technical references, not partners.

## 6. Proposed distribution system (not activated)

**Hub-and-spoke:** The canonical method/results page should be the source of truth; short-form content on video/social channels points back to it for context and corrections. Avoid posting unsupported stand-alone statistics.

**Cadence experiment:** Start with a modest, sustainable review cadence only if editorial/publishing authorization is given. Test format and teaching impact rather than maximizing post count. Recut high-quality evergreen stories based on audience questions, not duplicated spam or misleading novelty.

**Quality checks:** technical fact-check, research status, local perspective where relevant, alt text/captions, source links, commercial transparency, security/privacy review and accountable human publication approval. Agents may compose, subtitle, schedule in authorized sandboxes and draft analytics; they may not publish without an effective grant.

**Feedback routing:** questions → evidence-supported answers, corrections, new research proposals, contributor documentation. Moderation and consent standards required before community channels scale.

## 7. Measurement framework

**Research quality:** protocol completeness, percentage claims with provenance, independently reproduced findings, correction latency, negative results published.

**Educational usefulness:** completion/retention on a video, worksheet usage, qualitatively accurate audience answers, accessibility and international participation; platform metrics alone are proxies.

**Community health:** opt-in contributors retained, useful bug reports, external reproductions, substantive critiques incorporated, new case studies with permission, response times and moderation burden.

**Growth:** qualified visitors to public research, repeat readers, actual relevant subscriptions or voluntarily initiated contributions; no vanity follower-count optimization at expense of trust.

**Experiment ROI:** accepted outcomes and research reliability relative to combined model, CI, human review and publication cost.

Use UTM/tagging only if approved with privacy-compliant analytics; report measurable uncertainty and avoid claims of guaranteed algorithmic growth.

## 8. Editorial principles from authoritative practices

- Google's Search Central emphasizes **helpful, reliable, people-first content**, including transparency around automation and how material was produced. Source: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- GitHub's citation metadata lets public research repositories communicate preferred citation information: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files
- GitHub's open-source community documentation covers contribution guidelines, collaboration and moderation: https://docs.github.com/en/communities
- YouTube's official guidance describes audience retention reports, useful for improving clarity of educational videos without treating attention as proof of learning: https://support.google.com/youtube/answer/9314415

These are workflow and reporting references, **not evidence that this proposed campaign will grow or that experimental results exist**.

## 9. Proposed research backlog (not registered in canonical mainline roadmap)

- `FOR-RD-EXP-PUB-001`: Reproducible experiment package template and rights/security review.
- `FOR-RD-EXP-PUB-002`: Versioned fact/claim ledger linking scientific findings to derivatives.
- `FOR-RD-EDU-003`: Multi-format evergreen learning module and mock campaign on convergence.
- `FOR-RD-GROWTH-004`: Research-to-community contribution funnel with consent/feedback safeguards.
- `FOR-RD-GROWTH-005`: Evaluation criteria for learner understanding and substantive contributions, not merely impressions.
- `FOR-RD-GLOBAL-006`: Multilingual/local-context contribution and independent case-review process.

Identifiers proposed only; resolve conflicts and gain project owner approval before adding work to canonical roadmap. No Internet Embassy tasks created.

## 10. One proposed growth flywheel experiment (not run)

**Question:** Does attaching a reproducible public learning artifact to an edutainment short produce more useful collective engagement than a short that only explains a concept?

**Control:** educational short with clear facts and neutral source link.  
**Treatment:** identical quality topic and creative effort plus a reproducible GitHub tabletop exercise with invitation for critique.  
**Primary learning value:** independently evaluated accuracy of voluntary contributions (quality review, not raw click-through).  
**Secondary:** completion/retention, verified independent issue reports, worksheet use, revisit rate and cost per useful contribution.  
**Guardrails:** no private participant capture without consent, no fake user testimonials, no deceptive claims, no unsafe autonomous publishing, no engagement bait.  
**Caveat:** platforms distribute content unevenly; a small study cannot establish universal impact.

## Final north star

Foromni can become a **public learning laboratory** where its research produces transparent experiments, those experiments generate teachable lessons, and the global collective contributes new questions, critiques and improvements. Growth follows documented value and trust, not unsupported hype.

**Build today, so others can enjoy tomorrow.**
