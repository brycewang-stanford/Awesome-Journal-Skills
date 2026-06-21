---
name: ieee-international-conference-on-robotics-and-automation
description: Use when targeting IEEE International Conference on Robotics and Automation (ICRA) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for robotics flagship.
---

# IEEE International Conference on Robotics and Automation (ICRA)

## Conference positioning

IEEE International Conference on Robotics and Automation (ICRA) is a top computer-science conference venue for robotics, automation, manipulation, perception, planning, control, and embodied AI systems. It rewards a robotics paper with hardware/simulation evidence, clear task definition, and real-world constraints. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names ICRA / IEEE International Conference on Robotics and Automation as the target venue.
- A manuscript in robotics needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: robotics, automation, manipulation, perception, planning, control, and embodied AI systems.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to ICRA's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Read reviewers as embodied-systems researchers. Hardware, simulation, task distributions, and failure rates matter more than a clean curve alone.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: robotics, automation, manipulation, perception, planning, control, and embodied AI systems.
- Distinctive fingerprint for reviewer calibration: robotics, automation, manipulation, perception, planning, control, embodied, venue-specific, contribution, flagship, ieee-ras.
- Official anchor domain: www.ieee-ras.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in robotics
  flagship and the author can say why ICRA reviewers are the primary audience, not merely a
  convenient deadline.
- Closest roster neighbors to compare before final routing: `ieee-rsj-international-conference-
  on-intelligent-robots-and-systems` (IROS), `robotics-science-and-systems` (RSS). Break ties
  by contribution type, evidence shape, reviewer community, and the current official CFP from
  www.ieee-ras.org.

## What distinguishes this venue from its closest siblings

- **Sponsorship & cadence.** Sole flagship of the **IEEE Robotics & Automation Society (RAS)**, held annually — distinct from **IROS**, which is **co-sponsored by IEEE RAS and the Robotics Society of Japan (RSJ)** (the "IEEE/RSJ" in its name).
- **Center of gravity.** Broad automation / manipulation / planning / control across the full robotics stack; the single most prestige-dense robotics deadline.
- **vs RSS.** RSS is single-track and foundations/algorithmic-model forward; route model-and-theory results there and integrated hardware/system results here. Confirm the current cycle on www.ieee-ras.org.

## ICRA-specific routing detail

- Prefer ICRA when the contribution is broad robotics and automation: manipulation, locomotion, perception, control, planning, field robots, industrial robotics, or integrated robot systems.
- Route intelligent-robot systems and community/cycle fit to IROS, experimental-method depth to ISER, and robotics research vision to ISRR.
- ICRA evidence should include robot platform, task setup, trials, baselines, failure analysis, and whether results transfer beyond a single demonstration.

## Method & evidence bar

- Report hardware, simulation, environment, task distribution, reset procedure, and failure cases; embodied evidence must be inspectable.
- Compare against meaningful robot-learning, planning, or control baselines under matched assumptions.
- Separate simulation gains from real-world transfer and quantify reliability, not only best-case success.
- For ICRA, the evidence must support the venue-specific signature: a robotics paper with hardware/simulation evidence, clear task definition, and real-world constraints.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the robot task and system constraint before the algorithmic component.
- Use video or supplementary material only as allowed by the current anonymous-review policy.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at ICRA, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle robotics flagship papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Simulation-only evidence for a claim about real robots.
- No clear task distribution, few trials, or missing failure analysis.
- A learning curve without robot-specific insight or system integration.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving ICRA reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses ICRA's bar, compare against `ieee-rsj-international-conference-on-intelligent-robots-and-systems` / `robotics-science-and-systems` / `conference-on-robot-learning` / `acm-ieee-international-conference-on-human-robot-interaction`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE International Conference on Robotics and Automation (ICRA)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
