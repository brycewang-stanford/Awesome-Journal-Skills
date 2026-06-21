---
name: acm-ieee-international-conference-on-model-driven-engineering-languages-and-systems
description: Use when targeting ACM/IEEE International Conference on Model Driven Engineering Languages and Systems (MODELS) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for model-driven engineering.
---

# ACM/IEEE International Conference on Model Driven Engineering Languages and Systems (MODELS)

## Conference positioning

ACM/IEEE International Conference on Model Driven Engineering Languages and Systems (MODELS) is a top computer-science conference venue for model-driven engineering, modeling languages, transformations, DSLs, and software/system models. It rewards a modeling paper where language semantics, tooling, and engineering use case are all credible. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names MODELS / ACM/IEEE International Conference on Model Driven Engineering Languages and Systems as the target venue.
- A manuscript in model-driven engineering needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: model-driven engineering, modeling languages, transformations, DSLs, and software/system models.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to MODELS's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat MODELS as a model-driven engineering venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: model-driven engineering, modeling languages, transformations, DSLs, and software/system models.
- Distinctive fingerprint for reviewer calibration: model-driven, engineering, modeling, languages, transformations, dsls, software, system, models, venue-specific, contribution, conf, researchr.
- Official anchor domain: conf.researchr.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in model-driven
  engineering and the author can say why MODELS reviewers are the primary audience, not merely
  a convenient deadline.
- Closest roster neighbors to compare before final routing: `international-symposium-on-
  research-in-attacks-intrusions-and-defenses` (RAID), `ieee-international-requirements-
  engineering-conference` (RE), `ieee-international-conference-on-data-engineering` (ICDE).
  Break ties by contribution type, evidence shape, reviewer community, and the current
  official CFP from conf.researchr.org.

## What distinguishes this venue from its closest siblings

- **What MODELS is.** The **ACM/IEEE** conference on **Model-Driven Engineering Languages and Systems** — modeling languages, transformations, MDE.
- **Real neighbors.** ICSE / FSE / ASE (software engineering) and SLE (language engineering) — not data-mining venues.
- **Routing.** MDE/modeling here; general SE to ICSE/FSE.

## MODELS-specific routing detail

- Prefer MODELS when the contribution is a modeling language, metamodel, transformation, DSL, model analysis, code generation, or model-based engineering workflow with credible semantics and tooling.
- Route web-scale search, mining, recommendation, ranking, or user/platform data papers to WSDM/SIGIR/KDD; route general software-engineering studies to ICSE/FSE/ASE.
- The paper should show that models are the engineering abstraction under study, not merely diagrams used to explain a data-mining method.

## Method & evidence bar

- Compare against current strong baselines and explain exactly what changes in the algorithm, objective, data, or inference procedure.
- Report ablations that isolate the claimed mechanism; do not rely on aggregate benchmark wins alone.
- Document data, compute, hyperparameters, model selection, and failure cases so the result can be reviewed as science rather than demo output.
- For MODELS, the evidence must support the venue-specific signature: a modeling paper where language semantics, tooling, and engineering use case are all credible.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Frame the contribution as a reusable idea: method, theory, benchmark, dataset, system, or socio-technical finding.
- Separate main claims from exploratory results; reviewers at top AI venues punish overclaiming and hidden cherry-picking.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://conf.researchr.org/series/models
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at MODELS, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle model-driven engineering papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Leaderboard-only novelty with weak explanation of why the method works.
- Unclear data contamination, missing baselines, or evaluation that cannot be reproduced.
- Claims about safety, fairness, health, or society without matching evidence and limitations.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving MODELS reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses MODELS's bar, compare against `neural-information-processing-systems` / `international-conference-on-machine-learning` / `international-conference-on-learning-representations` / `aaai-conference-on-artificial-intelligence`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] ACM/IEEE International Conference on Model Driven Engineering Languages and Systems (MODELS)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
