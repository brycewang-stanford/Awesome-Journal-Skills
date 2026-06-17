---
name: conference-on-learning-theory
description: Use when targeting Conference on Learning Theory (COLT) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for learning theory.
---

# Conference on Learning Theory (COLT)

## Conference positioning

Conference on Learning Theory (COLT) is a top computer-science conference venue for formal learning theory, statistical learning, online learning, bandits, optimization theory, and lower bounds. It rewards a theorem-first paper whose contribution is a sharp result, proof technique, or formal separation. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names COLT / Conference on Learning Theory as the target venue.
- A manuscript in formal learning theory needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: formal learning theory, statistical learning, online learning, bandits, optimization theory, and lower bounds.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to COLT's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Read reviewers as theorem-first. Definitions, proof novelty, rates, lower bounds, or separations must carry the paper.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: formal learning theory, statistical learning, online learning, bandits, optimization theory, and lower bounds.
- Distinctive fingerprint for reviewer calibration: formal, learning, theory, statistical, online, bandits, optimization, lower, bounds, venue-specific, contribution, learningtheory.
- Official anchor domain: learningtheory.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in learning
  theory and the author can say why COLT reviewers are the primary audience, not merely a
  convenient deadline.
- Closest roster neighbors to compare before final routing: `artificial-intelligence-and-
  statistics` (AISTATS), `uncertainty-in-artificial-intelligence` (UAI), `conference-on-
  machine-learning-and-systems` (MLSys), `conference-on-lifelong-learning-agents` (CoLLAs).
  Break ties by contribution type, evidence shape, reviewer community, and the current
  official CFP from learningtheory.org.

## Method & evidence bar

- For systems/data papers, use realistic workloads, data sizes, and baselines; for theory papers, give exact statements and complete proofs.
- Explain the data model, assumptions, complexity, and implementation details at the level reviewers can audit.
- Connect the result to a durable database, algorithmic, or theoretical problem rather than a one-off benchmark.
- For COLT, the evidence must support the venue-specific signature: a theorem-first paper whose contribution is a sharp result, proof technique, or formal separation.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the formal or systems problem and the new capability the paper creates.
- Use figures or examples to make the model clear before dense proof or system detail.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://learningtheory.org/colt2026/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at COLT, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle learning theory papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Benchmark gains with no explanation of why the method generalizes.
- Theory result whose significance is unclear outside a narrow variant.
- Missing implementation details or proof gaps in the central claim.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving COLT reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses COLT's bar, compare against `acm-sigmod-international-conference-on-management-of-data` / `international-conference-on-very-large-data-bases` / `ieee-international-conference-on-data-engineering` / `acm-symposium-on-theory-of-computing`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Conference on Learning Theory (COLT)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
