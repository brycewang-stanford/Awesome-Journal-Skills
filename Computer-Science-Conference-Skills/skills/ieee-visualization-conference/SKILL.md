---
name: ieee-visualization-conference
description: Use when targeting IEEE Visualization Conference (IEEE VIS) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for visualization flagship.
---

# IEEE Visualization Conference (IEEE VIS)

## Conference positioning

IEEE Visualization Conference (IEEE VIS) is a top computer-science conference venue for information visualization, scientific visualization, visual analytics, and visualization systems/evaluation. It rewards a visualization paper with a precise task, visual encoding rationale, and evaluation appropriate to contribution type. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names IEEE VIS / IEEE Visualization Conference as the target venue.
- A manuscript in information visualization needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: information visualization, scientific visualization, visual analytics, and visualization systems/evaluation.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to IEEE VIS's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat IEEE VIS as a visualization flagship venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: information visualization, scientific visualization, visual analytics, and visualization systems/evaluation.
- Distinctive fingerprint for reviewer calibration: information, visualization, scientific, visual, analytics, evaluation, venue-specific, contribution, flagship, ieeevis.
- Official anchor domain: ieeevis.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Route to IEEE VIS when the central contribution is visualization: visual encoding, visual
  analytics, scientific visualization, visualization systems, or evaluation matched to the
  visualization claim.
- Do not submit generic HCI or graphics papers here. Compare EuroVis for specialist
  visualization, CHI/UIST for interaction/UI systems, and graphics venues for rendering or
  geometry.

## What distinguishes this venue from its closest siblings

- **What IEEE VIS is.** The **IEEE** visualization flagship (VIS), with papers in **IEEE TVCG** — scientific viz, information viz, and visual analytics.
- **vs EuroVis.** EuroVis (Eurographics) is the European counterpart publishing in **CGF**; differentiate by organizing community and cycle.
- **Routing.** Same scientific scope as EuroVis; pick by audience, journal pipeline (TVCG vs CGF), and timing.

## IEEE VIS-specific routing detail

- Prefer IEEE VIS when the contribution is flagship visualization research: visual analytics, information/scientific visualization, perception, evaluation, or visualization systems.
- Route European visualization community/cycle work to EuroVis, advanced visual interface techniques to AVI, and graphics algorithms to SIGGRAPH/Eurographics-family venues.
- IEEE VIS evidence should connect data abstraction, task analysis, visual encoding, evaluation, domain insight, and design rationale.

## Method & evidence bar

- Match the contribution type to the evidence: controlled study, field deployment, design inquiry, technical system, dataset, or theory.
- Report participants, recruitment, analysis method, consent/ethics, and limitations with enough detail for HCI review.
- For AI-infused interfaces, evaluate both model behavior and user experience; either alone is usually insufficient.
- For IEEE VIS, the evidence must support the venue-specific signature: a visualization paper with a precise task, visual encoding rationale, and evaluation appropriate to contribution type.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Explain who benefits, what interaction changes, and what design knowledge the paper contributes.
- Avoid treating users as a decoration for a technical system; the human evidence has to shape the claim.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://ieeevis.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at IEEE VIS, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle visualization flagship papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Underpowered or poorly matched user study for an ambitious design claim.
- Novel interface demo without contribution to interaction knowledge.
- Ethics, accessibility, or community context handled superficially.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving IEEE VIS reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses IEEE VIS's bar, compare against `acm-chi-conference-on-human-factors-in-computing-systems` / `acm-symposium-on-user-interface-software-and-technology` / `acm-conference-on-computer-supported-cooperative-work-and-social-computing` / `acm-conference-on-intelligent-user-interfaces`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Visualization Conference (IEEE VIS)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
