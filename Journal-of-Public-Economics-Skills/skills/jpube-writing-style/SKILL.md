---
name: jpube-writing-style
description: Use to polish prose for a Journal of Public Economics (JPubE) manuscript — a 250-word abstract stating purpose, results, and policy conclusion; an intro that lands the government-role question; author-date references; and clear translation of estimates into welfare terms. Late-stage polish; it does not change the analysis.
---

# Writing Style (jpube-writing-style)

## When to trigger

- The abstract exceeds 250 words or buries the policy finding
- The intro recites results before stating the public-economics question
- Estimates are reported without translation into welfare / revenue terms
- References are not in author-date format

## JPubE house style

JPubE is an Elsevier field journal read by public-finance specialists internationally, and its conventions are concrete. Match them:

- **Abstract: 250 words maximum.** Write a concise, factual abstract stating the purpose, the principal results (with the key number), and the major policy conclusion. No literature, no equations.
- **References: author-date (name-and-year)** in-text, per Elsevier's economics formatting; reference list alphabetical by surname. Numbered/footnote citation styles read as off-template.
- **Source files.** Supply editable files: Word in **single-column** layout, or LaTeX (`.tex`) — double-column is permitted only for LaTeX submissions. Keep the manuscript in an editable format, not a flattened PDF only.
- **AI disclosure.** If generative AI assisted manuscript preparation, it must be **declared at submission**; AI may support but not substitute for your critical thinking and analysis.

## Prose moves specific to public economics

- **Lead with the policy question, then the answer.** The first paragraph should name the government policy, the behavioral margin, and the welfare stake.
- **Translate every headline estimate.** Convert elasticities into deadweight loss, revenue, MVPF, or distributional language a policy economist reads instantly.
- **State the design in plain words** before the equations — JPubE referees reward transparent identification described verbally.
- **Be precise about scope.** Say which population and policy the estimate identifies; avoid implying a universal optimal rate from a local design.
- **Discipline the claims.** The conclusion must not exceed what the design and welfare assumptions support.

## Checklist

- [ ] Abstract ≤ 250 words; states purpose, key result (with a number), policy conclusion
- [ ] Intro leads with the government-role question, then the answer
- [ ] Every headline estimate translated into welfare / revenue / distributional terms
- [ ] References in author-date format, list alphabetical by surname
- [ ] Editable source files ready (Word single-column or LaTeX `.tex`)
- [ ] Generative-AI use declared if applicable
- [ ] No over-claiming beyond the design and welfare assumptions

## Anti-patterns

- A 300-word abstract crammed with caveats and no headline number
- Reporting elasticities the reader must convert to welfare themselves
- Numbered or footnote references instead of author-date
- A PDF-only submission with no editable Word/LaTeX source
- Undeclared AI assistance in manuscript preparation

## Output format

```
【Abstract】≤250 words, states result + policy conclusion? [Y/N]
【Intro】leads with policy question then answer? [Y/N]
【Estimate translation】welfare / revenue / distributional? [Y/N]
【References】author-date, alphabetical? [Y/N]
【Source files】Word single-column / LaTeX .tex ready? [Y/N]
【AI declaration】prepared if applicable? [Y/N]
【Next step】jpube-replication-and-data-policy
```
