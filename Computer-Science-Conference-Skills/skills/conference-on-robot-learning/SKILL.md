---
name: conference-on-robot-learning
description: Use when targeting Conference on Robot Learning (CoRL) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for robot learning.
---

# Conference on Robot Learning (CoRL)

## Conference positioning

Conference on Robot Learning (CoRL) is a top computer-science conference venue for robot learning, imitation, reinforcement learning, dexterous manipulation, sim-to-real, and embodied foundation models. It rewards a robot-learning paper where learning contributes to robust embodied behavior, not only simulated reward curves. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names CoRL / Conference on Robot Learning as the target venue.
- A manuscript in robot learning needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: robot learning, imitation, reinforcement learning, dexterous manipulation, sim-to-real, and embodied foundation models.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to CoRL's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat CoRL as a robot learning venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: robot learning, imitation, reinforcement learning, dexterous manipulation, sim-to-real, and embodied foundation models.
- Distinctive fingerprint for reviewer calibration: robot, learning, imitation, reinforcement, dexterous, manipulation, sim-to-real, embodied, foundation, models, venue-specific, contribution, corl.
- Official anchor domain: www.corl.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in robot
  learning and the author can say why CoRL reviewers are the primary audience, not merely a
  convenient deadline.
- Closest roster neighbors to compare before final routing: `robotics-science-and-systems`
  (RSS), `ieee-international-conference-on-robotics-and-automation` (ICRA), `ieee-rsj-
  international-conference-on-intelligent-robots-and-systems` (IROS), and `acm-ieee-
  international-conference-on-human-robot-interaction` (HRI). Break ties by contribution
  type, embodied-evidence shape, reviewer community, and the current official CFP from
  www.corl.org.

## What distinguishes CoRL from its closest siblings

- **CoRL vs HRI:** choose CoRL when the paper's main novelty is the learning algorithm,
  policy representation, data regime, sim-to-real strategy, or embodied foundation-model
  behavior; choose HRI when the decisive evidence is human interaction quality, trust,
  collaboration, or user-study design.
- **CoRL vs RSS:** choose CoRL for learning-centric claims with strong robot evidence; choose
  RSS when the contribution is broader robotics science, planning, perception, mechanics, or
  systems integration where learning is only one component.
- **CoRL vs ICRA/IROS:** choose CoRL when reviewers must evaluate learning generalization,
  imitation/RL baselines, data scaling, or policy robustness; route to ICRA/IROS when the paper
  is a robotics application, system, hardware, or control result with a wider robotics audience.

## Method & evidence bar

- Report hardware, simulation, environment, task distribution, reset procedure, and failure cases; embodied evidence must be inspectable.
- Compare against meaningful robot-learning, planning, or control baselines under matched assumptions.
- Separate simulation gains from real-world transfer and quantify reliability, not only best-case success.
- For CoRL, the evidence must support the venue-specific signature: a robot-learning paper where learning contributes to robust embodied behavior, not only simulated reward curves.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the robot task and system constraint before the algorithmic component.
- Use video or supplementary material only as allowed by the current anonymous-review policy.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.corl.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at CoRL, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle robot learning papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Simulation-only evidence for a claim about real robots.
- No clear task distribution, few trials, or missing failure analysis.
- A learning curve without robot-specific insight or system integration.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving CoRL reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses CoRL's bar, compare against `ieee-international-conference-on-robotics-and-automation` / `ieee-rsj-international-conference-on-intelligent-robots-and-systems` / `robotics-science-and-systems` / `acm-ieee-international-conference-on-human-robot-interaction`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Conference on Robot Learning (CoRL)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
