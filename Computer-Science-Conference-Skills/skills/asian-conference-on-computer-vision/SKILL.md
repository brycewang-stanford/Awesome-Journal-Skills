---
name: asian-conference-on-computer-vision
description: Use when targeting Asian Conference on Computer Vision (ACCV) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for computer vision regional flagship.
---

# Asian Conference on Computer Vision (ACCV)

## Conference positioning

Asian Conference on Computer Vision (ACCV) is a top computer-science conference venue for computer vision methods and applications with strong Asia-Pacific community visibility. It rewards a CV paper seeking rigorous review in a focused international venue. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names ACCV / Asian Conference on Computer Vision as the target venue.
- A manuscript in computer vision methods and applications with strong Asia-Pacific community visibility needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: computer vision methods and applications with strong Asia-Pacific community visibility.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to ACCV's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat ACCV as a computer vision regional flagship venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: computer vision methods and applications with strong Asia-Pacific community visibility.
- Distinctive fingerprint for reviewer calibration: vision, methods, applications, strong, asia-pacific, community, visibility, venue-specific, contribution, regional, flagship, accv-conf.
- Official anchor domain: accv-conf.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in computer
  vision regional flagship and the author can say why ACCV reviewers are the primary audience,
  not merely a convenient deadline.
- Closest roster neighbors to compare before final routing: `european-conference-on-computer-
  vision` (ECCV), `winter-conference-on-applications-of-computer-vision` (WACV), `british-
  machine-vision-conference` (BMVC), `international-conference-on-3d-vision` (3DV). Break ties
  by contribution type, evidence shape, reviewer community, and the current official CFP from
  accv-conf.org.

## What distinguishes this venue from its closest siblings

- **What ACCV is.** The **Asian Conference on Computer Vision** (Asian Federation of Computer Vision) — the regional vision venue, biennial, anchored in the Asia-Pacific community.
- **vs WACV.** WACV (IEEE/CVF) is **applications-forward and held in winter**; route applied-systems vision there and regional general-vision work here.
- **vs CVPR/ICCV/ECCV.** The flagships set the global bar; ACCV is the regional complement, not a fallback by prestige.

## ACCV-specific routing detail

- Prefer ACCV when the paper is computer vision and the Asian vision community/cycle is the natural fit, especially for recognition, geometry, video, 3D, or vision-language work.
- Route application-forward winter-cycle vision work to WACV, flagship global vision work to CVPR/ICCV/ECCV, and biomedical imaging to ISBI/MICCAI when domain validation is central.
- ACCV evidence should include vision baselines, dataset protocol, ablations, qualitative failure cases, and clear positioning against current vision literature.

## Method & evidence bar

- Use current vision baselines, strong ablations, dataset-specific protocols, and qualitative examples that reveal failure modes.
- Keep the anonymous submission self-contained; external material should follow the current-cycle policy exactly.
- For generated or foundation-model outputs, show robustness, data provenance, and evaluation beyond cherry-picked visuals.
- For ACCV, the evidence must support the venue-specific signature: a CV paper seeking rigorous review in a focused international venue.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the visual problem and the technical insight; then prove it across datasets, metrics, and ablations.
- Make figures do work: pipeline, qualitative wins/failures, and compact quantitative comparisons.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://accv-conf.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: the current CVF/ECCV/CMT/OpenReview author kit and anonymity policy.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at ACCV, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle computer vision regional flagship papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- A thin architecture tweak with marginal gains and no analysis.
- Using non-comparable baselines, private data splits, or hidden external links that violate review policy.
- Ethics, consent, or biometric/medical claims handled as boilerplate rather than as real constraints.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving ACCV reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses ACCV's bar, compare against `computer-vision-and-pattern-recognition` / `international-conference-on-computer-vision` / `european-conference-on-computer-vision` / `winter-conference-on-applications-of-computer-vision`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Asian Conference on Computer Vision (ACCV)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
