---
name: pacific-graphics
description: Use when targeting Pacific Graphics (Pacific Graphics) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for computer graphics.
---

# Pacific Graphics (Pacific Graphics)

## Conference positioning

Pacific Graphics (Pacific Graphics) is a top computer-science conference venue for graphics, visualization, geometric computing, rendering, animation, and Asia-Pacific visual computing. It rewards a visual computing paper with specialist novelty and clear comparative demonstrations. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names Pacific Graphics / Pacific Graphics as the target venue.
- A manuscript in graphics needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: graphics, visualization, geometric computing, rendering, animation, and Asia-Pacific visual computing.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to Pacific Graphics's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat Pacific Graphics as a focused Asia-Pacific visual computing venue. A good submission foregrounds graphics technique, comparative visuals, and regional/international visual-computing relevance, not only broad multimedia or HCI claims.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: graphics, visualization, geometric computing, rendering, animation, and Asia-Pacific visual computing.
- Distinctive fingerprint for reviewer calibration: graphics, visualization, geometric, computing, rendering, animation, asia-pacific, visual, venue-specific, contribution, pg2026, nccu.
- Official anchor domain: pg2026.nccu.edu.tw. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in computer
  graphics and the author can say why Pacific Graphics reviewers are the primary audience, not
  merely a convenient deadline.
- Closest roster neighbors to compare before final routing: `acm-siggraph-asia` (SIGGRAPH Asia),
  `eurographics` (Eurographics), `acm-siggraph-symposium-on-interactive-3d-graphics-and-games`
  (I3D), `international-conference-on-advanced-visual-interfaces` (AVI). Break ties by
  contribution type, evidence shape, reviewer community, and the current official CFP from
  pg2026.nccu.edu.tw.

## What distinguishes this venue from its closest siblings

- **What Pacific Graphics is.** The **Pacific Conference on Computer Graphics and Applications** — the **Asia-Pacific** graphics venue; archival papers in **Computer Graphics Forum (CGF)**.
- **vs Eurographics.** Eurographics is the **European** CGF conference; same journal pipeline, different region and cycle.
- **vs SIGGRAPH Asia.** SIGGRAPH Asia publishes in ACM TOG and is larger; PG is the CGF-track Asia-Pacific venue.

## Pacific Graphics-specific routing detail

- Prefer Pacific Graphics when the manuscript is a focused Asia-Pacific visual-computing contribution with CGF-style evidence in graphics, rendering, geometry, visualization, or animation.
- Route to Eurographics for the European CGF community, to SIGGRAPH Asia for the ACM TOG flagship Asia-Pacific cycle, and to vision venues when recognition benchmarks dominate.
- Pacific Graphics evidence should make the visual-computing technique, comparative demonstrations, and regional/community fit explicit without framing the venue as fallback.

## Method & evidence bar

- Use current vision baselines, strong ablations, dataset-specific protocols, and qualitative examples that reveal failure modes.
- Keep the anonymous submission self-contained; external material should follow the current-cycle policy exactly.
- For generated or foundation-model outputs, show robustness, data provenance, and evaluation beyond cherry-picked visuals.
- For Pacific Graphics, the evidence must support the venue-specific signature: a visual computing paper with specialist novelty and clear comparative demonstrations.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the visual problem and the technical insight; then prove it across datasets, metrics, and ablations.
- Make figures do work: pipeline, qualitative wins/failures, and compact quantitative comparisons.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://pg2026.nccu.edu.tw/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at Pacific Graphics, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle computer graphics papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- A thin architecture tweak with marginal gains and no analysis.
- Using non-comparable baselines, private data splits, or hidden external links that violate review policy.
- Ethics, consent, or biometric/medical claims handled as boilerplate rather than as real constraints.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving Pacific Graphics reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses Pacific Graphics's bar, compare against `computer-vision-and-pattern-recognition` / `international-conference-on-computer-vision` / `european-conference-on-computer-vision` / `winter-conference-on-applications-of-computer-vision`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Pacific Graphics (Pacific Graphics)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
