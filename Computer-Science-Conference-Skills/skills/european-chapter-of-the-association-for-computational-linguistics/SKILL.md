---
name: european-chapter-of-the-association-for-computational-linguistics
description: Use when targeting Conference of the European Chapter of the Association for Computational Linguistics (EACL) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for NLP regional flagship.
---

# Conference of the European Chapter of the Association for Computational Linguistics (EACL)

## Conference positioning

Conference of the European Chapter of the Association for Computational Linguistics (EACL) is a top computer-science conference venue for NLP and computational linguistics with European ACL community focus. It rewards a language paper suited to the EACL cycle and computational-linguistics readership. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names EACL / Conference of the European Chapter of the Association for Computational Linguistics as the target venue.
- A manuscript in NLP and computational linguistics with European ACL community focus needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: NLP and computational linguistics with European ACL community focus.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to EACL's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat EACL as an ACL-family venue with a European chapter identity and strong multilingual/computational-linguistics traditions. Emphasize language coverage, linguistic clarity, and ACL-family evaluation discipline rather than generic NLP speed.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: NLP and computational linguistics with European ACL community focus.
- Distinctive fingerprint for reviewer calibration: computational, linguistics, european, community, focus, venue-specific, contribution, regional, flagship, eacl.
- Official anchor domain: eacl.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Route to EACL when the paper is an NLP contribution and the European ACL chapter
  cycle/community is the right fit for timing, topic, or audience.
- Do not treat EACL as a generic fallback from ACL/EMNLP. Resource-heavy papers may fit LREC-
  COLING; dialogue, semantics, or generation may fit SIGDIAL, *SEM, or INLG.

## What distinguishes this venue from its closest siblings

- **Which ACL chapter.** EACL is the ACL's **European** chapter; its community, host locations, and program rhythm are anchored in Europe.
- **Same review pipeline.** It draws on the **ACL Rolling Review (ARR)** commitment model shared with ACL and NAACL, so the bar and topic scope are common — the real choice is *which chapter's cycle and audience* you want.
- **Do not route by prestige.** Pick EACL for fit with the European cycle/community; ACL is the international meeting and NAACL the North American one.

## Method & evidence bar

- Use task-appropriate baselines, multiple datasets or languages when the claim is broad, and error analysis that explains model behavior.
- For LLM work, control for data leakage, prompt sensitivity, evaluation contamination, and human-evaluation reliability.
- For resources, document annotation, licensing, demographics, quality control, and intended use.
- For EACL, the evidence must support the venue-specific signature: a language paper suited to the EACL cycle and computational-linguistics readership.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- State the language phenomenon, task, or system behavior before the model name.
- Connect examples to measured errors; reviewers dislike anecdotal examples presented as evidence.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://eacl.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: ARR/START/ACL Rolling Review or the current ACL-family submission portal, plus ACLPUB formatting when applicable.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at EACL, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle NLP regional flagship papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Evaluation that is only a prompt table or cherry-picked generation examples.
- Missing dataset documentation, licensing, or annotation reliability.
- Claims of general language understanding from narrow English-only benchmarks.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving EACL reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses EACL's bar, compare against `annual-meeting-of-the-association-for-computational-linguistics` / `conference-on-empirical-methods-in-natural-language-processing` / `north-american-chapter-of-the-association-for-computational-linguistics` / `interspeech`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Conference of the European Chapter of the Association for Computational Linguistics (EACL)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
