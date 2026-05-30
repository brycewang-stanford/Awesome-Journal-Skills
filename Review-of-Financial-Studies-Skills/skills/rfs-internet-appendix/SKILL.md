---
name: rfs-internet-appendix
description: Use when deciding what belongs in the journal-hosted Internet Appendix vs. the main paper for a The Review of Financial Studies (RFS) manuscript, and how to structure it. Organizes supplementary material; does NOT generate the robustness content itself.
---

# Internet Appendix (rfs-internet-appendix)

## When to trigger

- The main paper is bloated with secondary tables, proofs, or derivations
- Referees will want 15–25 additional checks that cannot fit in the main text
- You have proofs, data-construction detail, or extra robustness to house
- You are unsure what RFS expects in the supplementary file vs. the article

## What the Internet Appendix is at RFS

RFS hosts an **Internet Appendix (IA)** alongside the published article. It is the standard home for material that supports the paper but would crowd the main text. Treat it as part of the submission, refereed alongside the manuscript — not a dumping ground. RFS has also run special initiatives and registered-report-style formats at various times; treat those, and the exact IA/data-and-code policy, as **options to verify on the RFS site**, not fixed rules.

### What belongs in the main paper
- The identification strategy and its core diagnostics.
- The 1–3 main results with economic magnitudes.
- The single most convincing robustness check for each main result.
- Enough to let a reader judge the contribution without the IA.

### What belongs in the Internet Appendix
- **Full robustness battery** (alternative specs, measures, subsamples, clustering) referenced from the main text.
- **Proofs and full derivations** for any model; the main text carries intuition and the key proposition.
- **Data construction details**: variable definitions, merge logic, filters, source documentation.
- **Additional figures / event-study plots** for secondary outcomes.
- **Extended tables** that are too large for the page.
- **Replication notes**: code/data availability statement consistent with current journal policy.

### Cross-referencing discipline
- Every IA table/figure is referenced by number from the main text ("see Internet Appendix Table IA.3").
- IA numbering uses an "IA" prefix to avoid confusion with main exhibits.
- The IA is self-contained: its own brief intro, consistent notation with the paper.

### What does NOT belong in the IA
- A result the paper's conclusion depends on — if a referee must read it to be convinced, it is a main result.
- Material that contradicts the main paper without reconciliation.
- A graveyard of failed specifications presented without interpretation.

### Practical workflow
1. After `rfs-robustness`, tag each table/figure as "main" or "IA".
2. Keep the single most convincing robustness check per result in the main text; send the rest to the IA.
3. Insert the IA cross-reference in the main text at the point the check supports.
4. Re-read the main paper alone and confirm the contribution still lands without the IA.

## Checklist

- [ ] Main paper stands alone: contribution judgeable without opening the IA
- [ ] Full robustness battery lives in the IA, each item referenced from the text
- [ ] Proofs/derivations in the IA; intuition + key result in the main text
- [ ] Data-construction and variable-definition detail documented in the IA
- [ ] IA tables/figures use an IA prefix and are cross-referenced by number
- [ ] Data/code availability statement matches current RFS policy (verify on site)
- [ ] IA notation and variable names match the main paper exactly

## Anti-patterns

- Burying a result the paper depends on in the IA where referees may miss it.
- An IA with no cross-references from the main text (orphan tables).
- Inconsistent variable names or notation between paper and IA.
- Assuming an old IA/data policy still holds — RFS policies evolve; verify.
- Using the IA to hide weak results instead of addressing them.

## Output format

```
【Main paper keeps】[identification, main results, top robustness each]
【IA holds】[full robustness, proofs, data construction, extra figures]
【Cross-refs】every IA item referenced from text? yes/no
【Data/code statement】drafted + checked against current policy? yes/no
【Next step】rfs-writing-style
```
