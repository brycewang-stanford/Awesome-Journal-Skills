---
name: jae-writing-style
description: Use when polishing the prose of a Journal of Accounting and Economics (JAE) manuscript — economics-paper conventions (precise, hypothesis-driven, restrained), Elsevier author-date (Harvard) referencing, numbered sections, and the mandatory Highlights/keywords/JEL packaging — so the writing matches the positive-accounting tradition.
---

# Writing Style for JAE (jae-writing-style)

## When to trigger

- Prose is verbose, hedged, or buries the prediction and result
- The intro does not state the economic question, prediction, and finding early
- References are not in Elsevier author-date (Harvard) style
- Highlights, keywords, or JEL codes are missing or off-spec

## Write like an economics paper, not an essay

JAE prose follows the **economics/positive-accounting** register: precise, restrained, and hypothesis-driven. The introduction should, within the first pages, state the **research question, the economic friction, the prediction, the identification, the data, and the headline result** — reviewers should know what you find before the methods section. Use the present tense for established results and active, direct sentences. Avoid normative language ("firms should"), promotional adjectives, and behavioral speculation; let the economic argument and evidence carry the paper.

## Structure and sections

Use **numbered sections** (1. Introduction, 2. Background/Hypotheses, 3. Data and research design, 4. Results, 5. Robustness, 6. Conclusion) with numbered subsections (1.1, 1.1.1). Each hypothesis stated in the development section should map cleanly onto a table in results. Tie every empirical claim to a specific exhibit. Keep the conclusion to what the evidence supports — restate mechanism, magnitude, and boundaries.

## Elsevier referencing and packaging

- **References**: Elsevier author-date (Harvard) — in-text by author name and year; reference list alphabetical then chronological, with a/b/c suffixes for same-author/same-year works. Use the `[dataset]` tag for cited data.
- **LaTeX**: the Elsevier `elsarticle.cls` class with BibTeX is recommended; single-column native format.
- **Highlights** (mandatory): 2-5 bullet points, **max 125 characters each**, summarizing the contribution.
- **Keywords**: up to **6**, American spelling.
- **JEL codes**: up to **6** — required, signaling the economics-discipline orientation.

## Precision over hedging

Economics referees punish vague causal verbs. Say "is associated with" for correlational evidence and reserve "causes/leads to" for designs that identify it. Define every construct on first use; do not let a proxy (e.g., "disclosure quality") drift in meaning across the paper.

## Checklist

- [ ] Intro states question, friction, prediction, design, data, and result early
- [ ] Active voice, present tense for findings; no normative/promotional language
- [ ] Numbered sections and subsections; hypotheses map to tables
- [ ] Elsevier author-date (Harvard) references; alphabetical-then-chronological
- [ ] Highlights (2-5 bullets, ≤125 chars), ≤6 keywords, ≤6 JEL codes present
- [ ] Causal verbs matched to identification; constructs defined consistently

## Anti-patterns

- **Burying the result** until after the methods.
- **Normative or promotional prose** ("this important problem...").
- **Causal language** unsupported by the design.
- **Wrong reference style** (numbered/Vancouver instead of author-date).
- **Missing Highlights/JEL codes** at submission.


## Style execution pass for Journal of Accounting and Economics

Use this as a second-pass capability check. First lock the economic mechanism, accounting setting, identification or model, and market/contracting consequence; then test whether the manuscript addresses accounting-economics reviewers who expect economics discipline, identification, and market or contracting implications.

- **Primary move:** Rewrite the opening and transitions so the venue-level claim, evidence object, and contribution are visible before technical detail.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JAR for accounting research breadth, TAR for accounting flagship breadth, Review of Accounting Studies for archival/accounting focus; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Intro】question + friction + prediction + design + result stated early? Y/N
【Voice/tense】active, present-for-findings; normative language removed
【Sections】numbered; hypotheses ↔ tables aligned
【References】Elsevier author-date (Harvard) verified
【Packaging】Highlights ≤125 chars ×(2-5); keywords ≤6; JEL ≤6
【Causal verbs】matched to identification
【Next step】jae-submission
```
