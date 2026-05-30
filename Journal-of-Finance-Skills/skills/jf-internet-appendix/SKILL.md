---
name: jf-internet-appendix
description: Use when deciding what belongs in the journal-hosted Internet Appendix vs. the main text of a The Journal of Finance (JF) manuscript. Allocates content and structures the appendix; it does not generate the results.
---

# Internet Appendix (jf-internet-appendix)

## When to trigger

- The main text is bloated with proofs, secondary robustness tables, or data-construction detail
- A referee will ask for more checks but the article is already long
- You are unsure what JF expects to live in the journal-hosted Internet Appendix
- The main result is buried on page 40 behind diagnostics

## Why JF has an Internet Appendix

JF favors **accessible, somewhat shorter** articles. The journal hosts an online **Internet Appendix** so technical depth does not crowd the printed paper. The main text carries the question, the design, the headline results, and the decisive robustness; everything else moves online. This is a JF hallmark — use it deliberately, not as a dumping ground.

## What goes where

| Content                                                        | Main text | Internet Appendix |
|----------------------------------------------------------------|:---------:|:-----------------:|
| The question, design, headline result, economic magnitude      |     X     |                   |
| The 3–6 decisive robustness checks                             |     X     |                   |
| Full proofs / derivations of propositions                      |           |         X         |
| Secondary / exhaustive robustness tables                       |           |         X         |
| Detailed variable construction, data filters, sample steps     |   brief   |     full detail   |
| Alternative measures / extra subsamples / extra factor models  |           |         X         |
| Monte Carlo / simulation evidence                              |           |         X         |
| Additional figures, summary-stat breakdowns                    |           |         X         |
| Replication notes (code/data availability statement)           |   brief   |     pointer       |

## Structuring the Internet Appendix

- Mirror the main-text section order; label tables `IA.I`, `IA.II`, … and figures `IA.1`, `IA.2`, ….
- Every appendix item must be **referenced from the main text** ("see Internet Appendix Table IA.IV") — orphan tables read as padding.
- Keep each appendix table self-contained, same note conventions as the main exhibits (`jf-tables-figures`).
- Proofs: state the proposition, then the proof, in the same numbering as the main text.
- Do not introduce a *new* main result only in the appendix — the appendix supports, it does not surprise.

## Checklist

- [ ] Main text keeps only question, design, headline results, decisive robustness, and economic magnitude
- [ ] All proofs/derivations are in the Internet Appendix, not interleaved in the body
- [ ] Every Internet Appendix item is cited from the main text
- [ ] Appendix tables/figures use the journal's IA numbering and the same note conventions
- [ ] Data-construction detail is brief in the body, full in the appendix
- [ ] No genuinely new headline finding appears only in the appendix
- [ ] Code/data availability statement points to where the replication package lives

## Anti-patterns

- Treating the Internet Appendix as a junk drawer of uncited tables
- Leaving long proofs in the main text "so referees see the rigor" — move them online
- A 70-page main article with the key table deep inside it
- Numbering appendix exhibits inconsistently with the main text
- Hiding a result that should be in the paper inside the appendix to dodge a length limit

## Output format

```
【Main-text length OK?】yes / no
【Proofs relocated?】yes / no
【All IA items cited from body?】yes / no
【Orphan appendix tables】[...]
【New result hidden in appendix?】yes / no
【Next step】jf-writing-style
```
