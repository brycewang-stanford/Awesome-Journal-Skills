---
name: eurographics
description: Use when targeting Eurographics Annual Conference (Eurographics) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for computer graphics.
---

# Eurographics Annual Conference (Eurographics)

## Conference positioning

Eurographics Annual Conference (Eurographics) is a top computer-science conference venue for European graphics research, rendering, geometry processing, visualization, simulation, and interaction. It rewards a graphics paper with strong specialist contribution and polished visual demonstrations. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names Eurographics / Eurographics Annual Conference as the target venue.
- A manuscript in European graphics research needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: European graphics research, rendering, geometry processing, visualization, simulation, and interaction.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to Eurographics's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat Eurographics as the European graphics research venue: the audience rewards careful geometric, rendering, visualization, simulation, or visual-computing scholarship and clear specialist positioning. Avoid writing it as a generic SIGGRAPH-lite submission; explain the research contribution to the graphics community directly.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: European graphics research, rendering, geometry processing, visualization, simulation, and interaction.
- Distinctive fingerprint for reviewer calibration: european, graphics, rendering, geometry, processing, visualization, simulation, interaction, venue-specific, contribution.
- Official anchor domain: www.eg.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in computer
  graphics and the author can say why Eurographics reviewers are the primary audience, not
  merely a convenient deadline.
- Closest roster neighbors to compare before final routing: `acm-siggraph` (SIGGRAPH), `acm-
  siggraph-asia` (SIGGRAPH Asia), `pacific-graphics` (Pacific Graphics), `acm-siggraph-
  symposium-on-interactive-3d-graphics-and-games` (I3D). Break ties by contribution type,
  evidence shape, reviewer community, and the current official CFP from www.eg.org.

## What distinguishes this venue from its closest siblings

- **What Eurographics is.** The annual conference of the **European Association for Computer Graphics (EG)**; archival papers appear in **Computer Graphics Forum (CGF)**.
- **vs Pacific Graphics.** PG is the **Asia-Pacific** graphics conference (also CGF); route by region and cycle, same CGF pipeline.
- **vs SIGGRAPH/SIGGRAPH Asia.** Those publish in ACM TOG; Eurographics is the European CGF-track flagship.

## Eurographics-specific routing detail

- Prefer Eurographics when the paper targets the European graphics community with a CGF-track graphics contribution in rendering, geometry, simulation, visualization, or visual computing.
- Route to Pacific Graphics when the same CGF-style contribution fits an Asia-Pacific cycle/community better; route to SIGGRAPH/SIGGRAPH Asia for ACM TOG flagship positioning.
- Eurographics evidence should emphasize specialist graphics novelty, comparative visuals, mathematical or system grounding, and clear positioning against recent CGF/EG work.

## Method & evidence bar

- Use current vision baselines, strong ablations, dataset-specific protocols, and qualitative examples that reveal failure modes.
- Keep the anonymous submission self-contained; external material should follow the current-cycle policy exactly.
- For generated or foundation-model outputs, show robustness, data provenance, and evaluation beyond cherry-picked visuals.
- For Eurographics, the evidence must support the venue-specific signature: a graphics paper with strong specialist contribution and polished visual demonstrations.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the visual problem and the technical insight; then prove it across datasets, metrics, and ablations.
- Make figures do work: pipeline, qualitative wins/failures, and compact quantitative comparisons.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.eg.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at Eurographics, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle computer graphics papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- A thin architecture tweak with marginal gains and no analysis.
- Using non-comparable baselines, private data splits, or hidden external links that violate review policy.
- Ethics, consent, or biometric/medical claims handled as boilerplate rather than as real constraints.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving Eurographics reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses Eurographics's bar, compare against `computer-vision-and-pattern-recognition` / `international-conference-on-computer-vision` / `european-conference-on-computer-vision` / `winter-conference-on-applications-of-computer-vision`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Eurographics Annual Conference (Eurographics)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
