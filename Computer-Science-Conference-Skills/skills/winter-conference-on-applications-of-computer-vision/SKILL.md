---
name: winter-conference-on-applications-of-computer-vision
description: Use when targeting IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for computer vision applications.
---

# IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)

## Conference positioning

IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) is a top computer-science conference venue for applied computer vision, datasets, systems, and methods with practical evaluation. It rewards a CV paper with solid validation and application grounding where CVPR-level breadth may be less clear. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names WACV / IEEE/CVF Winter Conference on Applications of Computer Vision as the target venue.
- A manuscript in applied computer vision needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: applied computer vision, datasets, systems, and methods with practical evaluation.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to WACV's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat WACV as a computer vision applications venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: applied computer vision, datasets, systems, and methods with practical evaluation.
- Distinctive fingerprint for reviewer calibration: applied, vision, datasets, methods, practical, evaluation, venue-specific, contribution, applications, wacv, thecvf.
- Official anchor domain: wacv.thecvf.com. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in computer
  vision applications and the author can say why WACV reviewers are the primary audience, not
  merely a convenient deadline.
- Closest roster neighbors to compare before final routing: `international-conference-on-
  computer-vision` (ICCV), `european-conference-on-computer-vision` (ECCV), `asian-conference-
  on-computer-vision` (ACCV), `british-machine-vision-conference` (BMVC). Break ties by
  contribution type, evidence shape, reviewer community, and the current official CFP from
  wacv.thecvf.com.

## What distinguishes this venue from its closest siblings

- **What WACV is.** The **IEEE/CVF Winter Conference on Applications of Computer Vision** — **applications-forward**, held in **winter**, often with distinct Applications and Algorithms tracks.
- **vs ACCV.** ACCV is a **regional (Asia-Pacific)** general-vision venue; choose WACV for applied/deployment-oriented contributions.
- **vs CVPR/ICCV/ECCV.** Same IEEE/CVF family as CVPR/ICCV; WACV rewards applied robustness and real-world systems rather than only headline novelty.

## WACV-specific routing detail

- Prefer WACV when the contribution is application-oriented computer vision with strong empirical evaluation, practical tasks, datasets, or systems.
- Route Asian community/cycle fit to ACCV, flagship vision contributions to CVPR/ICCV/ECCV, and graphics/visualization results to SIGGRAPH/EuroVis-family venues when vision is not the core.
- WACV evidence should make application setting, deployment assumptions, dataset realism, baselines, and failure analysis visible.

## Method & evidence bar

- Use current vision baselines, strong ablations, dataset-specific protocols, and qualitative examples that reveal failure modes.
- Keep the anonymous submission self-contained; external material should follow the current-cycle policy exactly.
- For generated or foundation-model outputs, show robustness, data provenance, and evaluation beyond cherry-picked visuals.
- For WACV, the evidence must support the venue-specific signature: a CV paper with solid validation and application grounding where CVPR-level breadth may be less clear.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the visual problem and the technical insight; then prove it across datasets, metrics, and ablations.
- Make figures do work: pipeline, qualitative wins/failures, and compact quantitative comparisons.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://wacv.thecvf.com/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: the current CVF/ECCV/CMT/OpenReview author kit and anonymity policy.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at WACV, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle computer vision applications papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- A thin architecture tweak with marginal gains and no analysis.
- Using non-comparable baselines, private data splits, or hidden external links that violate review policy.
- Ethics, consent, or biometric/medical claims handled as boilerplate rather than as real constraints.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving WACV reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses WACV's bar, compare against `computer-vision-and-pattern-recognition` / `international-conference-on-computer-vision` / `european-conference-on-computer-vision` / `asian-conference-on-computer-vision`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
