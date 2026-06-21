---
name: international-conference-on-principles-of-knowledge-representation-and-reasoning
description: Use when targeting International Conference on Principles of Knowledge Representation and Reasoning (KR) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for knowledge representation.
---

# International Conference on Principles of Knowledge Representation and Reasoning (KR)

## Conference positioning

International Conference on Principles of Knowledge Representation and Reasoning (KR) is a top computer-science conference venue for logic, reasoning, ontologies, nonmonotonic reasoning, argumentation, and explainable symbolic AI. It rewards a reasoning paper where representational commitments and formal semantics are central. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names KR / International Conference on Principles of Knowledge Representation and Reasoning as the target venue.
- A manuscript in logic needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: logic, reasoning, ontologies, nonmonotonic reasoning, argumentation, and explainable symbolic AI.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to KR's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat KR as a knowledge representation venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: logic, reasoning, ontologies, nonmonotonic reasoning, argumentation, and explainable symbolic AI.
- Distinctive fingerprint for reviewer calibration: logic, reasoning, ontologies, nonmonotonic, argumentation, explainable, symbolic, venue-specific, contribution, knowledge, representation.
- Official anchor domain: kr.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Route to KR when the paper is about formal knowledge representation, reasoning, logics,
  ontologies, constraints, argumentation, or planning-relevant representation principles.
- Compare SAT/CP for satisfiability or constraint solving, ISWC/K-CAP for semantic-web or
  knowledge-capture systems, and AAAI/IJCAI for broader AI.

## What distinguishes this venue from its closest siblings

- **What KR is.** The conference on **Principles of Knowledge Representation and Reasoning** — logics, ontologies, nonmonotonic and epistemic reasoning.
- **vs CP / SAT.** CP is constraint solving and SAT is Boolean satisfiability; KR is about **representation and reasoning formalisms**, not solver engineering.
- **vs AAAI/IJCAI.** The generalist AI flagships also take KR work; choose KR when the formal-reasoning community is the primary audience.

## KR-specific routing detail

- Prefer KR when the contribution is about representation and reasoning formalisms: logics, ontologies, argumentation, belief change, nonmonotonic reasoning, constraints, planning knowledge, or explainable reasoning.
- Route intrusion detection, attacks, defenses, and security measurement to RAID/security venues; route satisfiability-specific solving to SAT and semantic-web deployment to ISWC.
- KR evidence should make formal semantics, reasoning properties, expressiveness/complexity, examples, and solver or empirical support explicit.

## Method & evidence bar

- Compare against current strong baselines and explain exactly what changes in the algorithm, objective, data, or inference procedure.
- Report ablations that isolate the claimed mechanism; do not rely on aggregate benchmark wins alone.
- Document data, compute, hyperparameters, model selection, and failure cases so the result can be reviewed as science rather than demo output.
- For KR, the evidence must support the venue-specific signature: a reasoning paper where representational commitments and formal semantics are central.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Frame the contribution as a reusable idea: method, theory, benchmark, dataset, system, or socio-technical finding.
- Separate main claims from exploratory results; reviewers at top AI venues punish overclaiming and hidden cherry-picking.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://kr.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at KR, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle knowledge representation papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Leaderboard-only novelty with weak explanation of why the method works.
- Unclear data contamination, missing baselines, or evaluation that cannot be reproduced.
- Claims about safety, fairness, health, or society without matching evidence and limitations.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving KR reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses KR's bar, compare against `neural-information-processing-systems` / `international-conference-on-machine-learning` / `international-conference-on-learning-representations` / `aaai-conference-on-artificial-intelligence`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] International Conference on Principles of Knowledge Representation and Reasoning (KR)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
