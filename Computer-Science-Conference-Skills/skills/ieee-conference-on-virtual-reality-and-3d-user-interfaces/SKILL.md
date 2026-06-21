---
name: ieee-conference-on-virtual-reality-and-3d-user-interfaces
description: Use when targeting IEEE Conference on Virtual Reality and 3D User Interfaces (IEEE VR) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for virtual reality.
---

# IEEE Conference on Virtual Reality and 3D User Interfaces (IEEE VR)

## Conference positioning

IEEE Conference on Virtual Reality and 3D User Interfaces (IEEE VR) is a top computer-science conference venue for VR systems, 3D interaction, immersive analytics, perception, haptics, and user studies. It rewards a VR paper that connects technical novelty to measured immersive user experience. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names IEEE VR / IEEE Conference on Virtual Reality and 3D User Interfaces as the target venue.
- A manuscript in VR systems needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: VR systems, 3D interaction, immersive analytics, perception, haptics, and user studies.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to IEEE VR's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat IEEE VR as a virtual reality venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: VR systems, 3D interaction, immersive analytics, perception, haptics, and user studies.
- Distinctive fingerprint for reviewer calibration: interaction, immersive, analytics, perception, haptics, user, studies, venue-specific, contribution, virtual, reality, ieeevr.
- Official anchor domain: ieeevr.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Route to IEEE VR when the contribution is virtual reality, 3D user interfaces, immersive
  interaction, perception in VR, or VR system evaluation.
- Compare ISMAR for mixed/augmented reality, I3D/SIGGRAPH for graphics, CHI/UIST for interaction
  techniques, and HRI/robotics venues for embodied agents.

## What distinguishes this venue from its closest siblings

- **What IEEE VR is.** The IEEE Conference on **Virtual Reality and 3D User Interfaces** — VR/AR, perception, interaction, and 3D UIs (papers in IEEE TVCG).
- **vs I3D.** I3D (ACM SIGGRAPH) is **real-time rendering / interactive 3D graphics**; IEEE VR is VR/3DUI-centered.
- **vs SIGGRAPH.** SIGGRAPH is the broad graphics flagship; IEEE VR is the VR/3DUI specialist.

## IEEE VR-specific routing detail

- Prefer IEEE VR when the research object is virtual, augmented, or mixed reality: immersion, presence, 3D user interfaces, perception, interaction techniques, tracking, or embodied evaluation.
- Route real-time graphics algorithms without VR/AR interaction claims to I3D, and route broad HCI studies to CHI/UIST when immersive technology is not central.
- IEEE VR evidence should include headset/device context, user-study protocol, perceptual or interaction measures, latency/sickness considerations, and immersive-task realism.

## Method & evidence bar

- Use current vision baselines, strong ablations, dataset-specific protocols, and qualitative examples that reveal failure modes.
- Keep the anonymous submission self-contained; external material should follow the current-cycle policy exactly.
- For generated or foundation-model outputs, show robustness, data provenance, and evaluation beyond cherry-picked visuals.
- For IEEE VR, the evidence must support the venue-specific signature: a VR paper that connects technical novelty to measured immersive user experience.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the visual problem and the technical insight; then prove it across datasets, metrics, and ablations.
- Make figures do work: pipeline, qualitative wins/failures, and compact quantitative comparisons.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://ieeevr.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at IEEE VR, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle virtual reality papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- A thin architecture tweak with marginal gains and no analysis.
- Using non-comparable baselines, private data splits, or hidden external links that violate review policy.
- Ethics, consent, or biometric/medical claims handled as boilerplate rather than as real constraints.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving IEEE VR reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses IEEE VR's bar, compare against `computer-vision-and-pattern-recognition` / `international-conference-on-computer-vision` / `european-conference-on-computer-vision` / `winter-conference-on-applications-of-computer-vision`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Conference on Virtual Reality and 3D User Interfaces (IEEE VR)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
