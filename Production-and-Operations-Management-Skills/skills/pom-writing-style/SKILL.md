---
name: pom-writing-style
description: Use when revising the prose of a Production and Operations Management (POM) manuscript — front-loading the operations problem, balancing theory with practice relevance, applying author-year citations, and enforcing the 32-page cap with an e-companion split. Polishes prose; it does not build the model (pom-theory-development) or design exhibits (pom-tables-figures).
---

# Writing Style (pom-writing-style)

## When to trigger

- The prose buries the operations problem or the managerial takeaway
- The main document is over the 32-page cap
- Method exposition crowds out the OM insight
- Citations are not in POM's author-year style

## Write for a broad OM audience and for practicing managers

POM reviewers span method specialists and broad operations scholars, and the **practice-relevance gate** means the writing must convince both. Lead with the operations problem, setting, and decision; keep the method visible but **subordinate to the OM insight**. Pair theory and practice throughout: every theoretical claim should imply an operational consequence a manager can act on.

## POM house conventions

- **Citations:** author-year (name-year) parenthetical in-text (e.g., Hayes & Pisano 1996 style) with an alphabetical reference list. Configure your reference manager accordingly.
- **Abstract:** maximum **350 words**, with **no formulas, references, or abbreviations**. Write it for a Department Editor: problem, method family, key result, theory contribution, practice implication.
- **Title:** concise and descriptive, **≤ 25 words**; supply 1–6 keywords.
- **LaTeX:** a journal-specific POM LaTeX template is provided/recommended for math-heavy papers; any software is acceptable.

## Enforce the 32-page discipline

The main document is capped at **32 pages** (1.5 spacing, 11-pt, one-inch margins) including abstract, tables, figures, appendices, and references. When over budget, move proofs, lengthy derivations, and extended robustness to the **unlimited online e-companion** rather than compressing the argument. Do not let method machinery consume pages the contribution needs.

## Revision targets

- **First page:** decision, setting, mechanism, contribution — fast.
- **Literature review:** focused contrast that positions the paper, not a catalogue.
- **Model/empirics:** assumptions and validity stated in operational language.
- **Discussion:** actionable practice implications with boundary conditions.

## Checklist

- [ ] Operations problem and managerial takeaway front-loaded
- [ ] Theory-practice balance maintained, not method-dominated
- [ ] Author-year citations; alphabetical reference list
- [ ] Abstract ≤ 350 words, no formulas/references/abbreviations; title ≤ 25 words; 1–6 keywords
- [ ] Main document within 32 pages; overflow moved to the e-companion


## Style execution pass for Production and Operations Management

Treat this skill as an executable review pass, not a prose hint. First lock the operational decision, the performance metric, and the implementable lever; then judge whether the current manuscript answers the venue's real reader: POM reviewers who want operational insight tied to production, service, supply-chain, or platform decisions.

- **Do the pass:** Rewrite the first two pages so each paragraph starts from the venue-level claim, not from chronology or method inventory; preserve exact source-map limits and move technical overflow to appendix or supplement.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Management Science for broader OR/MS theory, Operations Research for method-first optimization, MSOM for manufacturing/service operations depth; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【POM fit sentence】one sentence (problem + insight + practice)
【Main readability issue】<problem>
【Theory-practice balance】theory-heavy / practice-heavy / balanced
【Format flags】abstract words / title length / citation style / page count
【e-companion move】content to relocate
【Next step】pom-submission
```
