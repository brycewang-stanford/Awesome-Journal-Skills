---
name: jfe-internet-appendix
description: Use when organizing the journal-hosted Internet Appendix for a Journal of Financial Economics (JFE) manuscript — what to move off the main text, how to cross-reference it, and how to keep it self-contained. Structures the appendix; it does not decide which robustness tests to run (jfe-robustness).
---

# Internet Appendix (jfe-internet-appendix)

## When to trigger

- Robustness tables, proofs, and extra derivations are crowding the main text
- The main text exceeds a readable length and you must triage exhibits
- A referee asks for many additional tests you cannot fit in the body
- You need every main-text claim that says "untabulated" or "in the appendix" to actually land somewhere

## Why the Internet Appendix matters at JFE

JFE hosts an Internet Appendix where exhaustive robustness, proofs, additional tests, and detailed methodology live. Given JFE's robustness-heavy culture, a deep, well-organized appendix is expected — it is where the "every alternative ruled out" work is documented without making the main paper unreadable. JFE has also at times experimented with registered reports; treat that as an option to verify on the official page, not a fixed rule.

## What belongs in the Internet Appendix

- **Proofs and derivations** for any theoretical results stated in the main text.
- **Secondary robustness** — alternative measures, additional subsamples, extra cluster levels, wild bootstrap — beyond the headline checks kept in the body.
- **Variable construction details** too granular for the main text (filters, matching algorithms, data cleaning).
- **Additional results** referenced as "untabulated" or "see Internet Appendix."
- **Supplementary figures** and diagnostic plots.
- **Replication notes** that complement (not replace) the required code/data deposit.

## What stays in the main text

- The headline result and the 3–6 most decisive robustness checks.
- The identification evidence a reader needs to believe the result (parallel trends, first-stage strength).
- The core variable-definition table.

## Organization rules

- Number appendix exhibits in their own series (e.g., Table IA.1, Figure IA.1).
- Every main-text pointer ("untabulated," "Internet Appendix Table IA.3") must resolve to a real exhibit.
- The appendix should be self-contained: a reader who never opens the main paper can still read each appendix table from its title and notes.
- Mirror the main text's reporting conventions (SEs, stars, cluster level) so cross-reading is frictionless.

## Checklist

- [ ] Every "untabulated"/"see appendix" claim resolves to a real exhibit
- [ ] Proofs and granular derivations are in the appendix, not the body
- [ ] Headline robustness kept in main text; the long tail moved out
- [ ] Appendix exhibits numbered in their own IA series
- [ ] Appendix exhibits are self-contained (titles + notes)
- [ ] Reporting conventions match the main text
- [ ] Required code/data deposit prepared separately (verify current rule)

## Anti-patterns

- Main-text pointers to appendix tables that do not exist
- Treating the appendix as a dumping ground with no ordering or notes
- Moving the *identification* evidence to the appendix to shorten the body
- An appendix whose tables cannot be read without the main text
- Confusing the Internet Appendix with the mandatory code/data replication package

## Output format

```
【Main-text kept】headline result + decisive checks
【Moved to IA】proofs / robustness / construction / extra results
【Pointer audit】all "untabulated"/"see IA" claims resolve? yes/no
【IA numbering】IA series applied? yes/no
【Code/data deposit】prepared separately? (verify rule)
【Next】jfe-writing-style
```
