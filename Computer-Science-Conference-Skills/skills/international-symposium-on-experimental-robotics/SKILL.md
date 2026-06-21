---
name: international-symposium-on-experimental-robotics
description: Use when targeting International Symposium on Experimental Robotics (ISER) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for experimental robotics.
---

# International Symposium on Experimental Robotics (ISER)

## Conference positioning

International Symposium on Experimental Robotics (ISER) is a top computer-science conference venue for experimental robotics, field robots, manipulation, navigation, embodied learning, and real-world validation. It rewards a robotics paper where experimental evidence and real-world performance are the contribution. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names ISER / International Symposium on Experimental Robotics as the target venue.
- A manuscript in experimental robotics needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: experimental robotics, field robots, manipulation, navigation, embodied learning, and real-world validation.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to ISER's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat ISER as a experimental robotics venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: experimental robotics, field robots, manipulation, navigation, embodied learning, and real-world validation.
- Distinctive fingerprint for reviewer calibration: experimental, robotics, field, robots, manipulation, navigation, embodied, learning, real-world, validation, venue-specific, contribution, iser-robotics.
- Official anchor domain: www.iser-robotics.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Route to ISER when the evidence is the contribution: real robot experiments, field trials,
  hardware constraints, repeatability, failures, and performance under physical-world
  conditions.
- Do not confuse ISER with ISRR. ISRR should read as agenda-setting robotics research; CoRL as
  robot learning; ICRA/IROS as broader robotics conference targets.

## What distinguishes this venue from its closest siblings

- **What ISER is.** The **International Symposium on Experimental Robotics** — single-track, **experiment-validated** robotics results.
- **vs ISRR.** ISRR (International Symposium on Robotics Research) is the **foundational/forward-looking** robotics symposium; ISER emphasizes experimental validation.
- **vs ICRA/IROS.** The IEEE flagships are larger and multi-track; ISER/ISRR are selective single-track symposia — route by format and emphasis.

## ISER-specific routing detail

- Prefer ISER when the contribution is experimentally grounded robotics: real-robot protocols, embodied system behavior, controlled experimental design, or empirical comparison of robotic methods.
- Route broad robotics theory and long-horizon research vision to ISRR, flagship robot systems to RSS/ICRA/IROS, and human-interaction claims to HRI/RO-MAN when people are central.
- ISER evidence should make robot platform, task distribution, number of trials, reset policy, failure modes, and sim-to-real boundaries inspectable.

## Method & evidence bar

- Report hardware, simulation, environment, task distribution, reset procedure, and failure cases; embodied evidence must be inspectable.
- Compare against meaningful robot-learning, planning, or control baselines under matched assumptions.
- Separate simulation gains from real-world transfer and quantify reliability, not only best-case success.
- For ISER, the evidence must support the venue-specific signature: a robotics paper where experimental evidence and real-world performance are the contribution.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the robot task and system constraint before the algorithmic component.
- Use video or supplementary material only as allowed by the current anonymous-review policy.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.iser-robotics.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at ISER, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle experimental robotics papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Simulation-only evidence for a claim about real robots.
- No clear task distribution, few trials, or missing failure analysis.
- A learning curve without robot-specific insight or system integration.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving ISER reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses ISER's bar, compare against `ieee-international-conference-on-robotics-and-automation` / `ieee-rsj-international-conference-on-intelligent-robots-and-systems` / `robotics-science-and-systems` / `conference-on-robot-learning`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] International Symposium on Experimental Robotics (ISER)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
