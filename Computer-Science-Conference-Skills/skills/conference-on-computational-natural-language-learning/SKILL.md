---
name: conference-on-computational-natural-language-learning
description: Use when targeting Conference on Computational Natural Language Learning (CoNLL) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for NLP learning.
---

# Conference on Computational Natural Language Learning (CoNLL)

## Conference positioning

Conference on Computational Natural Language Learning (CoNLL) is a top computer-science conference venue for machine learning for language, structured prediction, shared tasks, semantics, and multilingual modeling. It rewards an NLP learning paper with method novelty and careful comparison to strong learning baselines. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names CoNLL / Conference on Computational Natural Language Learning as the target venue.
- A manuscript in machine learning for language needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: machine learning for language, structured prediction, shared tasks, semantics, and multilingual modeling.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to CoNLL's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat CoNLL as a NLP learning venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: machine learning for language, structured prediction, shared tasks, semantics, and multilingual modeling.
- Distinctive fingerprint for reviewer calibration: machine, learning, language, structured, prediction, shared, tasks, semantics, multilingual, modeling, venue-specific, contribution, CoNLL.
- Official anchor domain: conll.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in NLP learning
  and the author can say why CoNLL reviewers are the primary audience, not merely a convenient
  deadline.
- Closest roster neighbors to compare before final routing: `european-conference-on-artificial-
  intelligence` (ECAI), `medical-image-computing-and-computer-assisted-intervention` (MICCAI),
  `conference-on-robot-learning` (CoRL), `ieee-international-conference-on-software-
  maintenance-and-evolution` (ICSME). Break ties by contribution type, evidence shape,
  reviewer community, and the current official CFP from conll.org.

## CoNLL-specific routing detail

- Prefer CoNLL when the contribution is computational natural language learning: structured prediction, linguistic generalization, multilingual learning, data-efficient NLP, or learning problems tied to language structure.
- Route broad empirical NLP to EMNLP, resources/evaluation to LREC-COLING, and speech to INTERSPEECH/SLT when language-learning methodology is not central.
- CoNLL evidence should connect learning setup, linguistic phenomenon, datasets, baselines, error analysis, and generalization across languages or tasks when claimed.

## Method & evidence bar

- Use task-appropriate baselines, multiple datasets or languages when the claim is broad, and error analysis that explains model behavior.
- For LLM work, control for data leakage, prompt sensitivity, evaluation contamination, and human-evaluation reliability.
- For resources, document annotation, licensing, demographics, quality control, and intended use.
- For CoNLL, the evidence must support the venue-specific signature: an NLP learning paper with method novelty and careful comparison to strong learning baselines.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- State the language phenomenon, task, or system behavior before the model name.
- Connect examples to measured errors; reviewers dislike anecdotal examples presented as evidence.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://conll.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: ARR/START/ACL Rolling Review or the current ACL-family submission portal, plus ACLPUB formatting when applicable.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at CoNLL, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle NLP learning papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Evaluation that is only a prompt table or cherry-picked generation examples.
- Missing dataset documentation, licensing, or annotation reliability.
- Claims of general language understanding from narrow English-only benchmarks.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving CoNLL reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses CoNLL's bar, compare against `annual-meeting-of-the-association-for-computational-linguistics` / `conference-on-empirical-methods-in-natural-language-processing` / `north-american-chapter-of-the-association-for-computational-linguistics` / `european-chapter-of-the-association-for-computational-linguistics`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Conference on Computational Natural Language Learning (CoNLL)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
