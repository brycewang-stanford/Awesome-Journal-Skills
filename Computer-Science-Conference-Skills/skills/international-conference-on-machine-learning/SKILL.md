---
name: international-conference-on-machine-learning
description: Use when targeting International Conference on Machine Learning (ICML) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for AI/ML flagship.
---

# International Conference on Machine Learning (ICML)

## Conference positioning

International Conference on Machine Learning (ICML) is a top computer-science conference venue for core machine learning methods, theory, applications, and responsible deployment. It rewards a technically rigorous ML contribution with clean experiments, clear limitations, and current-cycle formatting discipline. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names ICML / International Conference on Machine Learning as the target venue.
- A manuscript in core machine learning methods needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: core machine learning methods, theory, applications, and responsible deployment.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to ICML's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Read reviewers as cross-area AI specialists. The paper needs a clear ML or AI research contribution, strong baselines, honest limitations, and enough breadth to matter outside one lab benchmark.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: core machine learning methods, theory, applications, and responsible deployment.
- Distinctive fingerprint for reviewer calibration: core, machine, learning, methods, theory, applications, responsible, deployment, venue-specific, contribution, flagship, icml.
- Official anchor domain: icml.cc. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Route to ICML when the contribution is a machine-learning method, theory, evaluation protocol,
  or empirical result with rigorous ML baselines and ablations.
- Compare ICLR for representation/deep-learning framing, NeurIPS for broad ML/AI impact,
  AISTATS/UAI/COLT for statistical or theoretical claims, and MLSys for systems bottlenecks.

## What distinguishes this venue from its closest siblings

- **What ICML is.** The **International Conference on Machine Learning** (IMLS) — the broad ML flagship spanning theory and applications.
- **vs ICLR / NeurIPS.** ICLR is deep-learning-forward (OpenReview) and NeurIPS is the broad ML/neuro flagship; the three overlap heavily — route by cycle and community.
- **Routing.** Learning theory → COLT; vision → CVPR/ICCV/ECCV; NLP → ACL-family.

## ICML-specific routing detail

- Prefer ICML when the paper is a broad machine-learning contribution: algorithms, theory-informed methods, optimization, probabilistic learning, evaluation, or generalization across tasks.
- Route representation-learning framing to ICLR, broader AI/society/systems mix to NeurIPS, statistical inference to AISTATS, and ML systems to MLSys.
- ICML evidence should include strong baselines, ablations, theoretical or empirical justification, compute/reporting transparency, and task diversity matching the claim.

## Method & evidence bar

- Compare against current strong baselines and explain exactly what changes in the algorithm, objective, data, or inference procedure.
- Report ablations that isolate the claimed mechanism; do not rely on aggregate benchmark wins alone.
- Document data, compute, hyperparameters, model selection, and failure cases so the result can be reviewed as science rather than demo output.
- For ICML, the evidence must support the venue-specific signature: a technically rigorous ML contribution with clean experiments, clear limitations, and current-cycle formatting discipline.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Frame the contribution as a reusable idea: method, theory, benchmark, dataset, system, or socio-technical finding.
- Separate main claims from exploratory results; reviewers at top AI venues punish overclaiming and hidden cherry-picking.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://icml.cc/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview and the current-year official author guide.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at ICML, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle AI/ML flagship papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Leaderboard-only novelty with weak explanation of why the method works.
- Unclear data contamination, missing baselines, or evaluation that cannot be reproduced.
- Claims about safety, fairness, health, or society without matching evidence and limitations.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving ICML reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses ICML's bar, compare against `neural-information-processing-systems` / `international-conference-on-learning-representations` / `aaai-conference-on-artificial-intelligence` / `international-joint-conference-on-artificial-intelligence`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] International Conference on Machine Learning (ICML)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
