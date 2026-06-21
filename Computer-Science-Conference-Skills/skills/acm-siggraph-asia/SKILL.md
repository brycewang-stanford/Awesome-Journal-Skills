---
name: acm-siggraph-asia
description: Use when targeting ACM SIGGRAPH Asia (SIGGRAPH Asia) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for computer graphics flagship.
---

# ACM SIGGRAPH Asia (SIGGRAPH Asia)

## Conference positioning

ACM SIGGRAPH Asia (SIGGRAPH Asia) is a top computer-science conference venue for graphics, animation, rendering, geometry, simulation, and visual computing in the Asia-Pacific SIGGRAPH venue. It rewards a graphics paper with flagship-level novelty and reproducible visual evidence. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names SIGGRAPH Asia / ACM SIGGRAPH Asia as the target venue.
- A manuscript in graphics needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: graphics, animation, rendering, geometry, simulation, and visual computing in the Asia-Pacific SIGGRAPH venue.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to SIGGRAPH Asia's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat SIGGRAPH Asia as the Asia-Pacific counterpart with the same high graphics bar but a distinct regional community, production ecosystem, and program rhythm. Emphasize how the result travels across animation, rendering, XR, geometry, or visual computing communities rather than framing it as a fallback for the North American event.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: graphics, animation, rendering, geometry, simulation, and visual computing in the Asia-Pacific SIGGRAPH venue.
- Distinctive fingerprint for reviewer calibration: graphics, animation, rendering, geometry, simulation, visual, computing, asia-pacific, siggraph, venue-specific, contribution, flagship, asia.
- Official anchor domain: asia.siggraph.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in computer
  graphics flagship and the author can say why SIGGRAPH Asia reviewers are the primary
  audience, not merely a convenient deadline.
- Closest roster neighbors to compare before final routing: `acm-international-conference-on-
  multimedia-retrieval` (ICMR), `acm-siggraph` (SIGGRAPH), `eurographics` (Eurographics),
  `pacific-graphics` (Pacific Graphics). Break ties by contribution type, evidence shape,
  reviewer community, and the current official CFP from asia.siggraph.org.

## What distinguishes this venue from its closest siblings

- **Host rotation.** Held **across rotating Asian cities** in **November/December** under **ACM SIGGRAPH**.
- **Publication model.** Accepted technical papers become a **special late-year issue of *ACM Transactions on Graphics* (TOG)**, mirroring the summer SIGGRAPH issue; Journal + Conference tracks.
- **vs SIGGRAPH (North America).** Same family and acceptance bar, different hemisphere and season — route by **where and when**, not prestige.

## SIGGRAPH Asia-specific routing detail

- Prefer SIGGRAPH Asia when the manuscript targets the same flagship graphics/TOG standard but benefits from the late-year Asia-Pacific cycle, regional program rhythm, or local graphics production ecosystem.
- Route to SIGGRAPH for the summer North American cycle, to Eurographics/Pacific Graphics for regional graphics community fit, and to vision venues when recognition metrics are the main contribution.
- A SIGGRAPH Asia paper should avoid fallback framing; make the graphics advance, evidence package, and cycle-specific submission plan explicit.

## Method & evidence bar

- Use current vision baselines, strong ablations, dataset-specific protocols, and qualitative examples that reveal failure modes.
- Keep the anonymous submission self-contained; external material should follow the current-cycle policy exactly.
- For generated or foundation-model outputs, show robustness, data provenance, and evaluation beyond cherry-picked visuals.
- For SIGGRAPH Asia, the evidence must support the venue-specific signature: a graphics paper with flagship-level novelty and reproducible visual evidence.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the visual problem and the technical insight; then prove it across datasets, metrics, and ablations.
- Make figures do work: pipeline, qualitative wins/failures, and compact quantitative comparisons.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://asia.siggraph.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at SIGGRAPH Asia, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle computer graphics flagship papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- A thin architecture tweak with marginal gains and no analysis.
- Using non-comparable baselines, private data splits, or hidden external links that violate review policy.
- Ethics, consent, or biometric/medical claims handled as boilerplate rather than as real constraints.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving SIGGRAPH Asia reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses SIGGRAPH Asia's bar, compare against `computer-vision-and-pattern-recognition` / `international-conference-on-computer-vision` / `european-conference-on-computer-vision` / `winter-conference-on-applications-of-computer-vision`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] ACM SIGGRAPH Asia (SIGGRAPH Asia)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
