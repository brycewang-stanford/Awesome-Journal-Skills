---
name: ieee-international-conference-on-automation-science-and-engineering
description: Use when targeting IEEE International Conference on Automation Science and Engineering (CASE) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for automation.
---

# IEEE International Conference on Automation Science and Engineering (CASE)

## Conference positioning

IEEE International Conference on Automation Science and Engineering (CASE) is a top computer-science conference venue for automation science, manufacturing, logistics, cyber-physical systems, scheduling, and industrial robotics. It rewards an automation paper that combines algorithmic design with operations or manufacturing evidence. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names CASE / IEEE International Conference on Automation Science and Engineering as the target venue.
- A manuscript in automation science needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: automation science, manufacturing, logistics, cyber-physical systems, scheduling, and industrial robotics.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to CASE's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat CASE as a automation venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: automation science, manufacturing, logistics, cyber-physical systems, scheduling, and industrial robotics.
- Distinctive fingerprint for reviewer calibration: automation, manufacturing, logistics, cyber-physical, scheduling, industrial, robotics, venue-specific, contribution, ieee-ras.
- Official anchor domain: www.ieee-ras.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in automation
  and the author can say why CASE reviewers are the primary audience, not merely a convenient
  deadline.
- Closest roster neighbors to compare before final routing: `acm-ieee-international-conference-
  on-human-robot-interaction` (HRI), `ieee-international-conference-on-robot-and-human-
  interactive-communication` (RO-MAN), `international-symposium-on-robotics-research` (ISRR),
  `international-symposium-on-experimental-robotics` (ISER). Break ties by contribution type,
  evidence shape, reviewer community, and the current official CFP from www.ieee-ras.org.

## What distinguishes this venue from its closest siblings

- **What CASE is.** The **IEEE RAS** flagship for **automation science & engineering** — manufacturing, scheduling, logistics, planning, and automation systems with an industrial/operations slant.
- **vs RO-MAN.** RO-MAN is about **robot–human interactive communication** (social/cognitive HRI), a different reviewer community; do not route automation-systems work there.
- **vs ICRA/IROS.** Send general manipulation/perception/control to ICRA/IROS; reserve CASE for automation-systems and applied-engineering contributions.

## CASE-specific routing detail

- Prefer CASE when the core claim is automation science: manufacturing cells, logistics, scheduling, industrial cyber-physical systems, automation platforms, or operations-aware robotics.
- Route robot-human dialogue, trust, social behavior, and assistive interaction studies to RO-MAN/HRI unless automation workflow is the main object.
- CASE evidence should connect algorithms to operational constraints such as throughput, takt time, reliability, safety envelopes, resource allocation, or deployment workflow.

## Method & evidence bar

- Report hardware, simulation, environment, task distribution, reset procedure, and failure cases; embodied evidence must be inspectable.
- Compare against meaningful robot-learning, planning, or control baselines under matched assumptions.
- Separate simulation gains from real-world transfer and quantify reliability, not only best-case success.
- For CASE, the evidence must support the venue-specific signature: an automation paper that combines algorithmic design with operations or manufacturing evidence.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the robot task and system constraint before the algorithmic component.
- Use video or supplementary material only as allowed by the current anonymous-review policy.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.ieee-ras.org/conferences-workshops/fully-sponsored/case
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at CASE, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle automation papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Simulation-only evidence for a claim about real robots.
- No clear task distribution, few trials, or missing failure analysis.
- A learning curve without robot-specific insight or system integration.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving CASE reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses CASE's bar, compare against `ieee-international-conference-on-robotics-and-automation` / `ieee-rsj-international-conference-on-intelligent-robots-and-systems` / `robotics-science-and-systems` / `conference-on-robot-learning`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE International Conference on Automation Science and Engineering (CASE)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
