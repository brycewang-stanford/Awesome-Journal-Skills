---
name: acm-sigplan-conference-on-object-oriented-programming-systems-languages-and-applications
description: Use when targeting ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications (OOPSLA) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for programming languages.
---

# ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications (OOPSLA)

## Conference positioning

ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications (OOPSLA) is a top computer-science conference venue for programming languages, software systems, language design, tools, types, verification, and empirical PL. It rewards a PL/systems paper with language or tool contribution and convincing semantic or empirical support. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names OOPSLA / ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications as the target venue.
- A manuscript in programming languages needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: programming languages, software systems, language design, tools, types, verification, and empirical PL.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to OOPSLA's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat OOPSLA as a programming languages venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: programming languages, software systems, language design, tools, types, verification, and empirical PL.
- Distinctive fingerprint for reviewer calibration: programming, languages, software, language, design, tools, types, verification, empirical, venue-specific, contribution, conf, researchr.
- Official anchor domain: conf.researchr.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in programming
  languages and the author can say why OOPSLA reviewers are the primary audience, not merely a
  convenient deadline.
- Closest roster neighbors to compare before final routing: `acm-sigplan-conference-on-
  programming-language-design-and-implementation` (PLDI), `acm-sigplan-symposium-on-
  principles-of-programming-languages` (POPL). Break ties by contribution type, evidence
  shape, reviewer community, and the current official CFP from conf.researchr.org.

## OOPSLA-specific routing detail

- Prefer OOPSLA when the contribution is programming languages and software systems: language design, type systems, semantics, program analysis, runtime systems, or developer-facing PL abstractions.
- Route language resources and computational linguistics to LREC-COLING, functional-programming-specific work to ICFP, and PL implementation/performance to PLDI when that community is primary.
- OOPSLA evidence should include formal or empirical support, implementation, examples, evaluation on programs, and clarity about language or system usability.

## Method & evidence bar

- Use task-appropriate baselines, multiple datasets or languages when the claim is broad, and error analysis that explains model behavior.
- For LLM work, control for data leakage, prompt sensitivity, evaluation contamination, and human-evaluation reliability.
- For resources, document annotation, licensing, demographics, quality control, and intended use.
- For OOPSLA, the evidence must support the venue-specific signature: a PL/systems paper with language or tool contribution and convincing semantic or empirical support.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- State the language phenomenon, task, or system behavior before the model name.
- Connect examples to measured errors; reviewers dislike anecdotal examples presented as evidence.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://conf.researchr.org/series/splash
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at OOPSLA, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle programming languages papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Evaluation that is only a prompt table or cherry-picked generation examples.
- Missing dataset documentation, licensing, or annotation reliability.
- Claims of general language understanding from narrow English-only benchmarks.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving OOPSLA reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses OOPSLA's bar, compare against `annual-meeting-of-the-association-for-computational-linguistics` / `conference-on-empirical-methods-in-natural-language-processing` / `north-american-chapter-of-the-association-for-computational-linguistics` / `european-chapter-of-the-association-for-computational-linguistics`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications (OOPSLA)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
