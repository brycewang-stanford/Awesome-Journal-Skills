---
name: aaai-acm-conference-on-ai-ethics-and-society
description: Use when targeting AAAI/ACM Conference on AI, Ethics, and Society (AIES) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for AI ethics and society.
---

# AAAI/ACM Conference on AI, Ethics, and Society (AIES)

## Conference positioning

AAAI/ACM Conference on AI, Ethics, and Society (AIES) is a top computer-science conference venue for AI ethics, governance, accountability, safety, social impacts, and socio-technical methods. It rewards a socio-technical AI paper that combines technical detail with normative or empirical social analysis. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names AIES / AAAI/ACM Conference on AI, Ethics, and Society as the target venue.
- A manuscript in AI ethics needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: AI ethics, governance, accountability, safety, social impacts, and socio-technical methods.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to AIES's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat AIES as a AI ethics and society venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: AI ethics, governance, accountability, safety, social impacts, and socio-technical methods.
- Distinctive fingerprint for reviewer calibration: ethics, governance, accountability, safety, social, impacts, socio-technical, methods, venue-specific, contribution, society, aies-conference.
- Official anchor domain: www.aies-conference.com. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in AI ethics and
  society and the author can say why AIES reviewers are the primary audience, not merely a
  convenient deadline.
- Closest roster neighbors to compare before final routing: `international-conference-on-
  principles-and-practice-of-constraint-programming` (CP), `integration-of-constraint-
  programming-artificial-intelligence-and-operations-research` (CPAIOR), `acm-conference-on-
  fairness-accountability-and-transparency` (FAccT), `european-conference-on-artificial-
  intelligence` (ECAI). Break ties by contribution type, evidence shape, reviewer community,
  and the current official CFP from www.aies-conference.com.

## What distinguishes this venue from its closest siblings

- **What AIES is.** The **AAAI/ACM** Conference on **AI, Ethics, and Society** — interdisciplinary AI ethics (philosophy, policy, technical).
- **vs FAccT.** FAccT (ACM Fairness, Accountability, and Transparency) is **algorithmic fairness/accountability**-centered and more technical-methods-forward; AIES is broader ethics/society.
- **Routing.** Pure ML-method fairness work may fit NeurIPS/ICML tracks; route normative/interdisciplinary work to AIES, fairness-systems work to FAccT.

## AIES-specific routing detail

- Prefer AIES when the contribution is AI ethics and society: governance, normative analysis, sociotechnical harms, policy, responsible AI, empirical audits, or human impacts of AI systems.
- Route fairness/accountability technical governance to FAccT, broad social computing to CSCW, and general AI methods to AAAI/IJCAI/ML venues when ethics is not the core.
- AIES evidence should connect technical claims to social context, affected stakeholders, normative assumptions, governance implications, and limits of the evidence.

## Method & evidence bar

- Compare against current strong baselines and explain exactly what changes in the algorithm, objective, data, or inference procedure.
- Report ablations that isolate the claimed mechanism; do not rely on aggregate benchmark wins alone.
- Document data, compute, hyperparameters, model selection, and failure cases so the result can be reviewed as science rather than demo output.
- For AIES, the evidence must support the venue-specific signature: a socio-technical AI paper that combines technical detail with normative or empirical social analysis.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Frame the contribution as a reusable idea: method, theory, benchmark, dataset, system, or socio-technical finding.
- Separate main claims from exploratory results; reviewers at top AI venues punish overclaiming and hidden cherry-picking.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.aies-conference.com/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at AIES, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle AI ethics and society papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Leaderboard-only novelty with weak explanation of why the method works.
- Unclear data contamination, missing baselines, or evaluation that cannot be reproduced.
- Claims about safety, fairness, health, or society without matching evidence and limitations.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving AIES reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses AIES's bar, compare against `neural-information-processing-systems` / `international-conference-on-machine-learning` / `international-conference-on-learning-representations` / `aaai-conference-on-artificial-intelligence`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] AAAI/ACM Conference on AI, Ethics, and Society (AIES)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
