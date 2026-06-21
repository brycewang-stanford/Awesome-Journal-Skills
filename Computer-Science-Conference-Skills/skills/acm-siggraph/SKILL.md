---
name: acm-siggraph
description: Use when targeting ACM SIGGRAPH (SIGGRAPH) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for computer graphics flagship.
---

# ACM SIGGRAPH (SIGGRAPH)

## Conference positioning

ACM SIGGRAPH (SIGGRAPH) is a top computer-science conference venue for computer graphics, rendering, animation, simulation, geometry, interaction, and visual computing. It rewards a graphics paper with a clear technical advance plus visual, mathematical, or system evidence. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names SIGGRAPH / ACM SIGGRAPH as the target venue.
- A manuscript in computer graphics needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: computer graphics, rendering, animation, simulation, geometry, interaction, and visual computing.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to SIGGRAPH's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat ACM SIGGRAPH as the flagship North American ACM graphics gathering: technical papers historically connect to the ACM Transactions on Graphics culture, and the broader venue mixes research with production, real-time demos, art, animation, rendering craft, and emerging technology showcases. A SIGGRAPH submission should feel like a definitive graphics result with visual evidence and production-aware technical polish.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: computer graphics, rendering, animation, simulation, geometry, interaction, and visual computing.
- Distinctive fingerprint for reviewer calibration: graphics, rendering, animation, simulation, geometry, interaction, visual, computing, venue-specific, contribution, flagship, siggraph.
- Official anchor domain: www.siggraph.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in computer
  graphics flagship and the author can say why SIGGRAPH reviewers are the primary audience,
  not merely a convenient deadline.
- Closest roster neighbors to compare before final routing: `acm-international-conference-on-
  multimedia` (ACM MM), `acm-international-conference-on-multimedia-retrieval` (ICMR), `acm-
  siggraph-asia` (SIGGRAPH Asia), `eurographics` (Eurographics). Break ties by contribution
  type, evidence shape, reviewer community, and the current official CFP from
  www.siggraph.org.

## What distinguishes this venue from its closest siblings

- **Publication model.** Technical papers are published as a **special summer issue of *ACM Transactions on Graphics* (TOG)**; the meeting is **ACM**-run and held in **North America**, with a Journal (TOG) track plus a Conference track.
- **vs SIGGRAPH Asia.** The Asian counterpart runs late in the year across rotating Asian host cities at the same bar — choose by **region and submission window**, never prestige.
- **Scope.** Rendering, geometry processing, animation, physical simulation, imaging, and graphics systems.

## SIGGRAPH-specific routing detail

- Prefer SIGGRAPH when the result fits the summer North American SIGGRAPH/TOG rhythm and needs the flagship graphics audience around rendering, geometry, animation, simulation, imaging, or graphics systems.
- Route to SIGGRAPH Asia when the same bar and community fit but the late-year Asia-Pacific cycle is strategically better; route to CVPR/ICCV/ECCV when recognition/vision benchmarks dominate.
- A SIGGRAPH paper should make visual quality, technical novelty, reproducibility, and production-aware evaluation visible in the main figures.

## Method & evidence bar

- Use current vision baselines, strong ablations, dataset-specific protocols, and qualitative examples that reveal failure modes.
- Keep the anonymous submission self-contained; external material should follow the current-cycle policy exactly.
- For generated or foundation-model outputs, show robustness, data provenance, and evaluation beyond cherry-picked visuals.
- For SIGGRAPH, the evidence must support the venue-specific signature: a graphics paper with a clear technical advance plus visual, mathematical, or system evidence.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the visual problem and the technical insight; then prove it across datasets, metrics, and ablations.
- Make figures do work: pipeline, qualitative wins/failures, and compact quantitative comparisons.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.siggraph.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at SIGGRAPH, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle computer graphics flagship papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- A thin architecture tweak with marginal gains and no analysis.
- Using non-comparable baselines, private data splits, or hidden external links that violate review policy.
- Ethics, consent, or biometric/medical claims handled as boilerplate rather than as real constraints.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving SIGGRAPH reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses SIGGRAPH's bar, compare against `computer-vision-and-pattern-recognition` / `international-conference-on-computer-vision` / `european-conference-on-computer-vision` / `winter-conference-on-applications-of-computer-vision`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] ACM SIGGRAPH (SIGGRAPH)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
