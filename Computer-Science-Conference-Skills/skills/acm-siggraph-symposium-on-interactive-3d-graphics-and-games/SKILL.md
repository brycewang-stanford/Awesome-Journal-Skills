---
name: acm-siggraph-symposium-on-interactive-3d-graphics-and-games
description: Use when targeting ACM SIGGRAPH Symposium on Interactive 3D Graphics and Games (I3D) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for interactive graphics.
---

# ACM SIGGRAPH Symposium on Interactive 3D Graphics and Games (I3D)

## Conference positioning

ACM SIGGRAPH Symposium on Interactive 3D Graphics and Games (I3D) is a top computer-science conference venue for real-time rendering, games, interactive 3D systems, GPU algorithms, and visual simulation. It rewards an interactive graphics paper where real-time performance and visual quality both matter. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names I3D / ACM SIGGRAPH Symposium on Interactive 3D Graphics and Games as the target venue.
- A manuscript in real-time rendering needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: real-time rendering, games, interactive 3D systems, GPU algorithms, and visual simulation.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to I3D's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat I3D as a interactive graphics venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: real-time rendering, games, interactive 3D systems, GPU algorithms, and visual simulation.
- Distinctive fingerprint for reviewer calibration: real-time, rendering, games, interactive, algorithms, visual, simulation, venue-specific, contribution, graphics, i3dsymposium.
- Official anchor domain: i3dsymposium.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Route to I3D when the contribution is interactive 3D graphics, real-time rendering, game
  graphics, geometry processing, or graphics systems for interactivity.
- Compare SIGGRAPH/SIGGRAPH Asia for broad graphics, SCA for animation, IEEE VR/ISMAR for
  immersive systems, and VIS venues for visualization knowledge.

## What distinguishes this venue from its closest siblings

- **What I3D is.** The **ACM SIGGRAPH** Symposium on **Interactive 3D Graphics and Games** — real-time rendering and interactive 3D.
- **vs IEEE VR.** IEEE VR is **virtual reality and 3D user interfaces** (perception, interaction, displays); I3D is real-time-rendering/graphics-systems-centered.
- **vs SIGGRAPH.** SIGGRAPH (ACM TOG) is the broad graphics flagship; I3D is the focused real-time/interactive venue.

## I3D-specific routing detail

- Prefer I3D when the contribution is interactive 3D graphics, real-time rendering, game graphics, simulation for interactive scenes, or systems that must run under interactive latency.
- Route VR/AR user-interface, perception, presence, or immersive-experience studies to IEEE VR; route full flagship graphics papers to SIGGRAPH/SIGGRAPH Asia when the bar and cycle fit.
- I3D evidence should show frame-time or latency constraints, interactive visual quality, scene complexity, implementation details, and comparisons relevant to real-time graphics.

## Method & evidence bar

- Use current vision baselines, strong ablations, dataset-specific protocols, and qualitative examples that reveal failure modes.
- Keep the anonymous submission self-contained; external material should follow the current-cycle policy exactly.
- For generated or foundation-model outputs, show robustness, data provenance, and evaluation beyond cherry-picked visuals.
- For I3D, the evidence must support the venue-specific signature: an interactive graphics paper where real-time performance and visual quality both matter.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the visual problem and the technical insight; then prove it across datasets, metrics, and ablations.
- Make figures do work: pipeline, qualitative wins/failures, and compact quantitative comparisons.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://i3dsymposium.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at I3D, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle interactive graphics papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- A thin architecture tweak with marginal gains and no analysis.
- Using non-comparable baselines, private data splits, or hidden external links that violate review policy.
- Ethics, consent, or biometric/medical claims handled as boilerplate rather than as real constraints.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving I3D reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses I3D's bar, compare against `computer-vision-and-pattern-recognition` / `international-conference-on-computer-vision` / `european-conference-on-computer-vision` / `winter-conference-on-applications-of-computer-vision`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] ACM SIGGRAPH Symposium on Interactive 3D Graphics and Games (I3D)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
