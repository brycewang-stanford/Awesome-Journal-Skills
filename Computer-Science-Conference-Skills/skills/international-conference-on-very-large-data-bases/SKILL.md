---
name: international-conference-on-very-large-data-bases
description: Use when targeting International Conference on Very Large Data Bases (VLDB) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for database flagship.
---

# International Conference on Very Large Data Bases (VLDB)

## Conference positioning

International Conference on Very Large Data Bases (VLDB) is a top computer-science conference venue for database systems, data management, analytics, transactions, distributed data, and data-intensive applications. It rewards a database paper with archival systems depth and large-scale empirical credibility. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names VLDB / International Conference on Very Large Data Bases as the target venue.
- A manuscript in database systems needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: database systems, data management, analytics, transactions, distributed data, and data-intensive applications.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to VLDB's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Read reviewers as data-management specialists. Query processing, transactions, storage, workload realism, and system architecture must be clear.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: database systems, data management, analytics, transactions, distributed data, and data-intensive applications.
- Distinctive fingerprint for reviewer calibration: database, data, management, analytics, transactions, distributed, data-intensive, applications, venue-specific, contribution, flagship, vldb.
- Official anchor domain: www.vldb.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Route to VLDB/PVLDB when the paper is database research with substantial data-management
  contribution and fits the VLDB community and submission model.
- Compare SIGMOD for database systems conference fit, ICDE for IEEE data engineering,
  KDD/ICDM/SDM for mining, and CIKM for information and knowledge management.

## What distinguishes this venue from its closest siblings

- **What VLDB is.** The **Very Large Data Bases** conference, publishing through **PVLDB (Proceedings of the VLDB Endowment)** on a **rolling monthly** submission model.
- **vs SIGMOD.** SIGMOD (ACM) is the cycle-deadline DB flagship; VLDB's rolling PVLDB pipeline is the practical routing difference.
- **Routing.** Both are top database systems venues; theory fits PODS, mining fits KDD/ICDM.

## VLDB-specific routing detail

- Prefer VLDB when the contribution is data-management research at large scale: database systems, query processing, transactions, storage, data integration, streams, or analytics infrastructure.
- Route SIGMOD when the ACM flagship cycle/community is the better fit, ICDE for data-engineering breadth, and data-mining papers to KDD/ICDM/SDM.
- VLDB evidence should include scale, workloads, system design, reproducibility, correctness tradeoffs, and practical data-management implications.

## Method & evidence bar

- For systems/data papers, use realistic workloads, data sizes, and baselines; for theory papers, give exact statements and complete proofs.
- Explain the data model, assumptions, complexity, and implementation details at the level reviewers can audit.
- Connect the result to a durable database, algorithmic, or theoretical problem rather than a one-off benchmark.
- For VLDB, the evidence must support the venue-specific signature: a database paper with archival systems depth and large-scale empirical credibility.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the formal or systems problem and the new capability the paper creates.
- Use figures or examples to make the model clear before dense proof or system detail.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.vldb.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at VLDB, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle database flagship papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Benchmark gains with no explanation of why the method generalizes.
- Theory result whose significance is unclear outside a narrow variant.
- Missing implementation details or proof gaps in the central claim.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving VLDB reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses VLDB's bar, compare against `acm-sigmod-international-conference-on-management-of-data` / `ieee-international-conference-on-data-engineering` / `acm-symposium-on-theory-of-computing` / `ieee-symposium-on-foundations-of-computer-science`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] International Conference on Very Large Data Bases (VLDB)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
