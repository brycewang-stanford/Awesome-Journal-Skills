---
name: acm-symposium-on-theory-of-computing
description: Use when targeting ACM Symposium on Theory of Computing (STOC) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for theory flagship.
---

# ACM Symposium on Theory of Computing (STOC)

## Conference positioning

ACM Symposium on Theory of Computing (STOC) is a top computer-science conference venue for algorithms, complexity, cryptography theory, learning theory, quantum computing, and theoretical foundations. It rewards a theory paper with major theorem contribution and broad theoretical-computer-science significance. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names STOC / ACM Symposium on Theory of Computing as the target venue.
- A manuscript in algorithms needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: algorithms, complexity, cryptography theory, learning theory, quantum computing, and theoretical foundations.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to STOC's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Read reviewers as theory specialists. The result needs precise statements, proof significance, and foundations-level positioning.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: algorithms, complexity, cryptography theory, learning theory, quantum computing, and theoretical foundations.
- Distinctive fingerprint for reviewer calibration: algorithms, complexity, cryptography, theory, learning, quantum, computing, theoretical, foundations, venue-specific, contribution, flagship, acm-stoc.
- Official anchor domain: acm-stoc.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in theory
  flagship and the author can say why STOC reviewers are the primary audience, not merely a
  convenient deadline.
- Closest roster neighbors to compare before final routing: `acm-sigmod-international-
  conference-on-management-of-data` (SIGMOD), `international-conference-on-very-large-data-
  bases` (VLDB), `ieee-symposium-on-foundations-of-computer-science` (FOCS). Break ties by
  contribution type, evidence shape, reviewer community, and the current official CFP from
  acm-stoc.org.

## What distinguishes this venue from its closest siblings

- **Sponsorship & season.** **ACM SIGACT**, held each **spring**; with **FOCS** (its **IEEE**-sponsored **autumn** sister) it forms the top-two theory-of-computing pair.
- **Scope is near-identical to FOCS.** Differentiate by **deadline/cycle and program committee**, not by topic or prestige; pick whichever cycle the result is ready for.
- **vs SODA/CCC/ITCS.** Algorithms-heavy work may fit SODA; complexity-specific work CCC; conceptual/early theory ITCS — route by sub-area when STOC/FOCS breadth is not the best home.

## STOC-specific routing detail

- Prefer STOC when the paper can sell a broad theoretical-computer-science breakthrough to a cross-area SIGACT audience: the first page should make the theorem, model, and conceptual payoff legible beyond one narrow subcommunity.
- Treat FOCS as the closest peer, but use STOC for the spring-cycle version of a result whose positioning benefits from ACM SIGACT breadth, STOC plenary visibility, or a cleaner story around algorithms/complexity/crypto/theory convergence.
- Do not use STOC merely because the result is mathematical. A strongly empirical algorithms paper, a specialized complexity classification, or a cryptographic construction with protocol-specific evaluation may route better to SODA, CCC, CRYPTO, EUROCRYPT, or a domain venue.

## Method & evidence bar

- For systems/data papers, use realistic workloads, data sizes, and baselines; for theory papers, give exact statements and complete proofs.
- Explain the data model, assumptions, complexity, and implementation details at the level reviewers can audit.
- Connect the result to a durable database, algorithmic, or theoretical problem rather than a one-off benchmark.
- For STOC, the evidence must support the venue-specific signature: a theory paper with major theorem contribution and broad theoretical-computer-science significance.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Lead with the formal or systems problem and the new capability the paper creates.
- Use figures or examples to make the model clear before dense proof or system detail.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://acm-stoc.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at STOC, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle theory flagship papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Benchmark gains with no explanation of why the method generalizes.
- Theory result whose significance is unclear outside a narrow variant.
- Missing implementation details or proof gaps in the central claim.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving STOC reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses STOC's bar, compare against `acm-sigmod-international-conference-on-management-of-data` / `international-conference-on-very-large-data-bases` / `ieee-international-conference-on-data-engineering` / `ieee-symposium-on-foundations-of-computer-science`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] ACM Symposium on Theory of Computing (STOC)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
