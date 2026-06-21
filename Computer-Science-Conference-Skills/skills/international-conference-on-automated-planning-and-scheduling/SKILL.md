---
name: international-conference-on-automated-planning-and-scheduling
description: Use when targeting International Conference on Automated Planning and Scheduling (ICAPS) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for planning and scheduling.
---

# International Conference on Automated Planning and Scheduling (ICAPS)

## Conference positioning

International Conference on Automated Planning and Scheduling (ICAPS) is a top computer-science conference venue for automated planning, scheduling, search, temporal reasoning, and decision processes. It rewards a planning paper with formal problem structure and empirical or theoretical planner evidence. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names ICAPS / International Conference on Automated Planning and Scheduling as the target venue.
- A manuscript in automated planning needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: automated planning, scheduling, search, temporal reasoning, and decision processes.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to ICAPS's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat ICAPS as automated planning and scheduling: search spaces, temporal/resource constraints, planners, heuristics, and benchmark domains are central. It is not a generic AI venue for any algorithmic paper.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: automated planning, scheduling, search, temporal reasoning, and decision processes.
- Distinctive fingerprint for reviewer calibration: automated, planning, scheduling, search, temporal, reasoning, decision, processes, venue-specific, contribution, icaps-conference.
- Official anchor domain: icaps-conference.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in planning and
  scheduling and the author can say why ICAPS reviewers are the primary audience, not merely a
  convenient deadline.
- Closest roster neighbors to compare before final routing: `international-semantic-web-
  conference` (ISWC), `international-conference-on-knowledge-capture` (K-CAP), `international-
  conference-on-principles-of-knowledge-representation-and-reasoning` (KR), `international-
  conference-on-autonomous-agents-and-multiagent-systems` (AAMAS). Break ties by contribution
  type, evidence shape, reviewer community, and the current official CFP from icaps-
  conference.org.

## ICAPS-specific routing detail

- Prefer ICAPS when the reusable contribution is a planner, scheduler, search heuristic, temporal/resource model, benchmark domain, or decision-process formulation, and the evidence shows planning/scheduling behavior rather than generic predictive accuracy.
- Use KDD only when the discovery or data-mining contribution is primary; a planner evaluated on large operational data still belongs at ICAPS if the algorithmic insight is about search, constraints, schedules, or temporal plans.
- Compare with CPAIOR for hybrid AI/OR optimization, AAMAS for multi-agent planning, KR for representation/reasoning depth, and AAAI/IJCAI when the planning contribution is part of a broader AI method.

## Method & evidence bar

- Compare against current strong baselines and explain exactly what changes in the algorithm, objective, data, or inference procedure.
- Report ablations that isolate the claimed mechanism; do not rely on aggregate benchmark wins alone.
- Document data, compute, hyperparameters, model selection, and failure cases so the result can be reviewed as science rather than demo output.
- For ICAPS, the evidence must support the venue-specific signature: a planning paper with formal problem structure and empirical or theoretical planner evidence.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Frame the contribution as a reusable idea: method, theory, benchmark, dataset, system, or socio-technical finding.
- Separate main claims from exploratory results; reviewers at top AI venues punish overclaiming and hidden cherry-picking.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://icaps-conference.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at ICAPS, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle planning and scheduling papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Leaderboard-only novelty with weak explanation of why the method works.
- Unclear data contamination, missing baselines, or evaluation that cannot be reproduced.
- Claims about safety, fairness, health, or society without matching evidence and limitations.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving ICAPS reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses ICAPS's bar, compare against `neural-information-processing-systems` / `international-conference-on-machine-learning` / `international-conference-on-learning-representations` / `aaai-conference-on-artificial-intelligence`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] International Conference on Automated Planning and Scheduling (ICAPS)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
