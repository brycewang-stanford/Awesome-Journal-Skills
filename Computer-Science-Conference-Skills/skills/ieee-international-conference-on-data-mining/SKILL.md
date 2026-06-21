---
name: ieee-international-conference-on-data-mining
description: Use when targeting IEEE International Conference on Data Mining (ICDM) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for data mining.
---

# IEEE International Conference on Data Mining (ICDM)

## Conference positioning

IEEE International Conference on Data Mining (ICDM) is a top computer-science conference venue for data mining algorithms, pattern discovery, graph mining, anomaly detection, and applied analytics. It rewards a data-mining methods paper with careful baselines and defensible discovery claims. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names ICDM / IEEE International Conference on Data Mining as the target venue.
- A manuscript in data mining algorithms needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: data mining algorithms, pattern discovery, graph mining, anomaly detection, and applied analytics.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to ICDM's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Read reviewers as data-centric ML and discovery specialists. Novelty should appear in mining method, scale, discovery validity, or applied impact.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: data mining algorithms, pattern discovery, graph mining, anomaly detection, and applied analytics.
- Distinctive fingerprint for reviewer calibration: data, mining, algorithms, pattern, discovery, graph, anomaly, detection, applied, analytics, venue-specific, contribution.
- Official anchor domain: www.computer.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Route to ICDM when the paper is a data-mining method, pattern-discovery result, or applied
  mining study suited to a broad IEEE data-mining audience.
- Compare KDD for larger data-mining impact and applied discovery, SDM for
  mathematical/statistical rigor, CIKM for information/knowledge management, and
  SIGMOD/VLDB/ICDE for database systems.

## What distinguishes this venue from its closest siblings

- **Sponsorship.** **IEEE**-sponsored data-mining flagship; distinguish from **SDM** (**SIAM**-sponsored) and **KDD** (**ACM**).
- **Routing.** Topic scope across ICDM/SDM/KDD overlaps heavily; route by **community, cycle, and paper format** rather than prestige.
- **Center of gravity.** Algorithmic data-mining contributions with strong empirical evaluation; applied/industrial tracks fit KDD's applied-data-science lane.

## ICDM-specific routing detail

- Prefer ICDM when the paper is data-mining research with algorithmic, applied, or scalable mining contribution across structured, graph, temporal, text, or heterogeneous data.
- Route mathematically focused data-mining methods to SDM, database-system contributions to ICDE/SIGMOD/VLDB, and broad ML method papers to ICML/NeurIPS/ICLR.
- ICDM evidence should show mining task definition, baselines, scalability, dataset realism, ablations, and interpretability or application relevance.

## Method & evidence bar

- Compare against current strong baselines and explain exactly what changes in the algorithm, objective, data, or inference procedure.
- Report ablations that isolate the claimed mechanism; do not rely on aggregate benchmark wins alone.
- Document data, compute, hyperparameters, model selection, and failure cases so the result can be reviewed as science rather than demo output.
- For ICDM, the evidence must support the venue-specific signature: a data-mining methods paper with careful baselines and defensible discovery claims.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Frame the contribution as a reusable idea: method, theory, benchmark, dataset, system, or socio-technical finding.
- Separate main claims from exploratory results; reviewers at top AI venues punish overclaiming and hidden cherry-picking.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.computer.org/csdl/proceedings/icdm
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at ICDM, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle data mining papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Leaderboard-only novelty with weak explanation of why the method works.
- Unclear data contamination, missing baselines, or evaluation that cannot be reproduced.
- Claims about safety, fairness, health, or society without matching evidence and limitations.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving ICDM reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses ICDM's bar, compare against `neural-information-processing-systems` / `international-conference-on-machine-learning` / `international-conference-on-learning-representations` / `aaai-conference-on-artificial-intelligence`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE International Conference on Data Mining (ICDM)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
