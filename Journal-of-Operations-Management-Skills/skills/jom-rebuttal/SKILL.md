---
name: jom-rebuttal
description: Use when planning and drafting a revision and point-by-point response letter for a Journal of Operations Management (JOM) R&R — prioritizing the Department Editor/Associate Editor's decisive concerns, resolving Empirical Research Methods method-check issues, and documenting new operations analyses across multiple rounds.
---

# R&R Rebuttal for JOM (jom-rebuttal)

## When to trigger

- You received a major-revision (R&R) decision from JOM
- You must turn Department Editor, Associate Editor, and reviewer comments into a revision plan
- You need a point-by-point response letter that survives a second round
- Method-check or identification concerns must be resolved before resubmission

## Triage the letter first

JOM's decision is filtered through a Department Editor and Associate Editor on top of reviewers. Before writing:

1. **Extract the DE/AE's decisive priorities** — these set what must change for the paper to survive. They outrank individual reviewer asks when those conflict.
2. **Separate method-check issues** (sampling, measurement validity, identification/endogeneity, common-method remedies, reproducibility). Given JOM's institutionalized Empirical Research Methods gate, these usually must be **fully resolved**, not argued away.
3. **Flag contribution concerns** — "operations not central enough" or "theory contribution thin" require reframing via `jom-contribution-framing`, not just more tables.
4. **Note presentational items** — exhibits, APA style, length, clarity.

## Build the response letter

- One numbered entry per comment, quoting it, then your response, then the **exact change and location** (section/page/table).
- Lead each response with what you *did*; reserve disagreement for cases where you can defend the original with evidence, and do so respectfully.
- For new analyses (alternative identification, added robustness, a new operational measure, additional respondents/sites), report them transparently — including results that did not change the conclusion.
- Keep operations at the heart in every revision; do not let added analyses dilute the operations argument.

## Multi-round expectations

Expect more than one round; first-round acceptance is essentially unheard of. Maintain a clean changelog and a reproducible analysis pipeline so each round's edits are traceable. Re-run the similarity check (single-source <1%, overall <15%) on the revised manuscript, and update disclosures (e.g., any new prior-data use).

## Anti-patterns

- Answering reviewers while ignoring the DE/AE's decisive framing.
- Arguing away a method-check/identification concern instead of fixing it.
- Cosmetic edits where the editor asked for a substantive operations or theory change.
- Reporting only the robustness checks that worked.

## Output format

```
【DE/AE decisive priorities】...
【Method-check issues to resolve】sampling/measures/identification/reproducibility ...
【Contribution reframes needed】...
【New analyses planned】...
【Response-letter structure】numbered, change+location per comment
【Similarity re-check + disclosure updates】...
【Round】expect multiple; changelog maintained
```
