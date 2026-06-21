---
name: international-natural-language-generation-conference
description: Use when targeting International Natural Language Generation Conference (INLG) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for language generation.
---

# International Natural Language Generation Conference (INLG)

## Conference positioning

International Natural Language Generation Conference (INLG) is a top computer-science conference venue for natural language generation, evaluation, controllability, data-to-text, dialogue, and LLM generation. It rewards a generation paper with rigorous human or automatic evaluation and clear generation task framing. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names INLG / International Natural Language Generation Conference as the target venue.
- A manuscript in natural language generation needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: natural language generation, evaluation, controllability, data-to-text, dialogue, and LLM generation.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to INLG's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat INLG as a language generation venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: natural language generation, evaluation, controllability, data-to-text, dialogue, and LLM generation.
- Distinctive fingerprint for reviewer calibration: natural, language, generation, evaluation, controllability, data-to-text, dialogue, venue-specific, contribution, inlgmeeting, github.
- Official anchor domain: inlgmeeting.github.io. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in language
  generation and the author can say why INLG reviewers are the primary audience, not merely a
  convenient deadline.
- Closest roster neighbors to compare before final routing: `north-american-chapter-of-the-
  association-for-computational-linguistics` (NAACL), `european-chapter-of-the-association-
  for-computational-linguistics` (EACL), `sigdial-conference-on-discourse-and-dialogue`
  (SIGDIAL), `joint-international-conference-on-computational-linguistics-language-resources-
  and-evaluation` (LREC-COLING). Break ties by contribution type, evidence shape, reviewer
  community, and the current official CFP from inlgmeeting.github.io.

## What distinguishes this venue from its closest siblings

- **What INLG is.** The **International Natural Language Generation Conference** (ACL **SIGGEN**) — natural language **generation** specifically: data-to-text, surface realization, planning, and generation evaluation.
- **vs *SEM.** *SEM is about **semantics/meaning representation**, a different SIG community; route generation work here, meaning-analysis work there.
- **vs ACL/EMNLP.** The big ACL-family meetings absorb generation too; pick INLG when the NLG community is the primary audience.

## INLG-specific routing detail

- Prefer INLG when the paper studies text generation itself: planning, realization, controllability, data-to-text, generation evaluation, factuality, style, or human assessment of generated language.
- Route meaning representation, semantic parsing, lexical semantics, and entailment analysis to *SEM unless the main contribution is producing language.
- INLG evidence should make the generation task, evaluation protocol, human-rating reliability, prompt/model controls, and example-to-metric connection explicit.

## Method & evidence bar

- Use task-appropriate baselines, multiple datasets or languages when the claim is broad, and error analysis that explains model behavior.
- For LLM work, control for data leakage, prompt sensitivity, evaluation contamination, and human-evaluation reliability.
- For resources, document annotation, licensing, demographics, quality control, and intended use.
- For INLG, the evidence must support the venue-specific signature: a generation paper with rigorous human or automatic evaluation and clear generation task framing.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- State the language phenomenon, task, or system behavior before the model name.
- Connect examples to measured errors; reviewers dislike anecdotal examples presented as evidence.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://inlgmeeting.github.io/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: ARR/START/ACL Rolling Review or the current ACL-family submission portal, plus ACLPUB formatting when applicable.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at INLG, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle language generation papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Evaluation that is only a prompt table or cherry-picked generation examples.
- Missing dataset documentation, licensing, or annotation reliability.
- Claims of general language understanding from narrow English-only benchmarks.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving INLG reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses INLG's bar, compare against `annual-meeting-of-the-association-for-computational-linguistics` / `conference-on-empirical-methods-in-natural-language-processing` / `north-american-chapter-of-the-association-for-computational-linguistics` / `european-chapter-of-the-association-for-computational-linguistics`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] International Natural Language Generation Conference (INLG)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
