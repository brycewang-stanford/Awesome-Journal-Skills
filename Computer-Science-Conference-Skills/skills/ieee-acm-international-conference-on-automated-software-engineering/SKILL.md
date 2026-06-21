---
name: ieee-acm-international-conference-on-automated-software-engineering
description: Use when targeting IEEE/ACM International Conference on Automated Software Engineering (ASE) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for automated software engineering.
---

# IEEE/ACM International Conference on Automated Software Engineering (ASE)

## Conference positioning

IEEE/ACM International Conference on Automated Software Engineering (ASE) is a top computer-science conference venue for automated software engineering, program analysis, testing, repair, synthesis, and AI-assisted development. It rewards an automation-for-SE paper with runnable artifact and realistic software benchmarks. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names ASE / IEEE/ACM International Conference on Automated Software Engineering as the target venue.
- A manuscript in automated software engineering needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: automated software engineering, program analysis, testing, repair, synthesis, and AI-assisted development.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to ASE's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat ASE as a automated software engineering venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: automated software engineering, program analysis, testing, repair, synthesis, and AI-assisted development.
- Distinctive fingerprint for reviewer calibration: automated, software, engineering, program, analysis, testing, repair, synthesis, ai-assisted, development, venue-specific, contribution, conf, researchr.
- Official anchor domain: conf.researchr.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in automated
  software engineering and the author can say why ASE reviewers are the primary audience, not
  merely a convenient deadline.
- Closest roster neighbors to compare before final routing: `international-conference-on-
  software-engineering` (ICSE), `acm-international-conference-on-the-foundations-of-software-
  engineering` (FSE), `acm-sigsoft-international-symposium-on-software-testing-and-analysis`
  (ISSTA), `mining-software-repositories` (MSR). Break ties by contribution type, evidence
  shape, reviewer community, and the current official CFP from conf.researchr.org.

## What distinguishes this venue from its closest siblings

- **What ASE is.** The **IEEE/ACM** International Conference on **Automated Software Engineering** — automation across the SE lifecycle (analysis, testing, synthesis, repair).
- **vs RE.** RE is the **requirements-engineering**-specific conference; route requirements/elicitation/specification work there and automation/tooling work here.
- **vs ICSE/FSE.** ICSE and FSE are the broad SE flagships; choose ASE when automation is the core contribution.

## ASE-specific routing detail

- Prefer ASE when the contribution automates software engineering work: program analysis, testing, repair, synthesis, CI/tooling, mining-driven automation, or developer-assistance systems.
- Route stakeholder needs, requirements elicitation, traceability, and requirements validation to RE; route broad software-engineering studies to ICSE/FSE when automation is not the main object.
- ASE evidence should include tool behavior, benchmark or repository realism, automation precision/recall or usefulness, failure cases, and comparison to existing SE tools.

## Method & evidence bar

- Use real programs, benchmarks, proofs, developer studies, or artifacts matched to the contribution type.
- For tools, report usability, scalability, false positives/negatives, and reproducible artifact details.
- For theory, provide precise definitions and complete proofs; for empirical SE, foreground validity threats.
- For ASE, the evidence must support the venue-specific signature: an automation-for-SE paper with runnable artifact and realistic software benchmarks.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- State the software-engineering or language problem in terms of developer, program, proof, or runtime consequence.
- Keep examples small but nontrivial, then scale evidence to realistic code or formal benchmarks.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://conf.researchr.org/series/ase
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at ASE, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle automated software engineering papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Toy examples with no evidence on real programs or benchmarks.
- Tool paper without artifact clarity or comparison to current systems.
- Empirical claims without validity analysis or reproducible data pipeline.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving ASE reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses ASE's bar, compare against `international-conference-on-software-engineering` / `acm-international-conference-on-the-foundations-of-software-engineering` / `acm-sigplan-conference-on-programming-language-design-and-implementation` / `acm-sigplan-symposium-on-principles-of-programming-languages`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE/ACM International Conference on Automated Software Engineering (ASE)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
