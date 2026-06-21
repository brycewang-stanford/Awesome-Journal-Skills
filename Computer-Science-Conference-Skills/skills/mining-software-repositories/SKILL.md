---
name: mining-software-repositories
description: Use when targeting Mining Software Repositories (MSR) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for software analytics.
---

# Mining Software Repositories (MSR)

## Conference positioning

Mining Software Repositories (MSR) is a top computer-science conference venue for software repository mining, developer behavior, empirical methods, datasets, and mining tools. It rewards an MSR paper with careful dataset construction, validity threats, and reproducible mining workflow. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names MSR / Mining Software Repositories as the target venue.
- A manuscript in software repository mining needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: software repository mining, developer behavior, empirical methods, datasets, and mining tools.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to MSR's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat MSR as a software analytics venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: software repository mining, developer behavior, empirical methods, datasets, and mining tools.
- Distinctive fingerprint for reviewer calibration: software, repository, mining, developer, behavior, empirical, methods, datasets, tools, venue-specific, contribution, analytics, msrconf.
- Official anchor domain: www.msrconf.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in software
  analytics and the author can say why MSR reviewers are the primary audience, not merely a
  convenient deadline.
- Closest roster neighbors to compare before final routing: `ieee-acm-international-conference-
  on-automated-software-engineering` (ASE), `acm-sigsoft-international-symposium-on-software-
  testing-and-analysis` (ISSTA), `ieee-international-conference-on-software-analysis-
  evolution-and-reengineering` (SANER), `international-symposium-on-empirical-software-
  engineering-and-measurement` (ESEM). Break ties by contribution type, evidence shape,
  reviewer community, and the current official CFP from www.msrconf.org.

## What distinguishes this venue from its closest siblings

- **What MSR is.** The conference on **Mining Software Repositories** — empirical SE from version-control, issue-tracker, and code data.
- **vs ICSE / FSE.** ICSE/FSE are the SE flagships; MSR is the data-mining-of-software-artifacts venue (often co-located with ICSE).
- **vs SANER / ICSME.** Those are analysis/maintenance; MSR centers repository-data empirical studies.

## MSR-specific routing detail

- Prefer MSR when the contribution mines software repositories: commits, issues, pull requests, CI logs, dependencies, developer behavior, or repository-derived datasets.
- Route logic/foundations to LICS, software maintenance/evolution claims to ICSME/SANER when mining is only evidence, and testing/analysis tools to ISSTA.
- MSR evidence should show repository sampling, data cleaning, construct validity, replication package, developer relevance, and limits of observational inference.

## Method & evidence bar

- Use real programs, benchmarks, proofs, developer studies, or artifacts matched to the contribution type.
- For tools, report usability, scalability, false positives/negatives, and reproducible artifact details.
- For theory, provide precise definitions and complete proofs; for empirical SE, foreground validity threats.
- For MSR, the evidence must support the venue-specific signature: an MSR paper with careful dataset construction, validity threats, and reproducible mining workflow.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- State the software-engineering or language problem in terms of developer, program, proof, or runtime consequence.
- Keep examples small but nontrivial, then scale evidence to realistic code or formal benchmarks.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.msrconf.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at MSR, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle software analytics papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Toy examples with no evidence on real programs or benchmarks.
- Tool paper without artifact clarity or comparison to current systems.
- Empirical claims without validity analysis or reproducible data pipeline.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving MSR reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses MSR's bar, compare against `international-conference-on-software-engineering` / `acm-international-conference-on-the-foundations-of-software-engineering` / `ieee-acm-international-conference-on-automated-software-engineering` / `acm-sigplan-conference-on-programming-language-design-and-implementation`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Mining Software Repositories (MSR)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
