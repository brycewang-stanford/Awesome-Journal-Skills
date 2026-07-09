---
name: pods-supplementary
description: Use when deciding what belongs in an ACM PODS paper body versus its at-submission appendix, covering the acmsmall 15-page budget, the rule that PODS forbids online/external appendices so all proofs ship with the submission, the body/appendix split for a theory paper, and double-anonymous supplementary hygiene.
---

# PODS Supplementary

Use this when assembling PODS supplementary material. The governing rule is specific to PODS: the
**appendix is incorporated with the submission and there are no online or external appendices**, so
"supplementary" means the appendix inside the same PDF — nothing lives off-paper. The body must be
readable as a self-contained mathematical narrative, and the appendix must contain every proof the
body defers.

## What goes where

| Content | Body (within 15-page budget) | Appendix (same PDF, unlimited) |
|---|---|---|
| Model, definitions, problem statement | Yes | — |
| Main theorem statements | Yes | — |
| Key proof ideas / the crux of each argument | Yes | Full details |
| Full proofs of main theorems | If they fit | Otherwise here, complete |
| Long reductions, gadget constructions | A description + the idea | The full construction and correctness proof |
| Corollaries and secondary results | Statement | Full proofs |
| Extended examples, tables of cases | The illustrative one | The exhaustive set |
| References | Yes (unlimited, not in page count) | — |

If a reviewer would have to trust an unproved step to accept the paper, it is mis-partitioned — the
full proof must be in the appendix, because at PODS the appendix ships with the submission and is
expected to be checked.

## The acmsmall page-budget discipline

PODS 2026's budget is **15 pages excluding references** in `\documentclass[acmsmall,review,anonymous]{acmart}`,
plus **unlimited references** and the **at-submission appendix of unlimited length**. Consequences:

- The **body** must stand alone: a reader should understand the model, the results, and *why* they
  hold from the 15 pages, with the appendix supplying verification detail.
- **Proofs that do not fit** go to the appendix behind explicit forward references ("full proof in
  Appendix B") — never dropped or deferred to an external document.
- **Do not smuggle a result into the appendix** that the body needs to make its case: the body carries
  the argument; the appendix carries the verification. Reviewers read the body in full and consult the
  appendix to check.
- References are unlimited and outside the page count, so there is no reason to trim the bibliography
  to save space.

## No external appendix — the PODS-specific rule

```text
[One PDF]        body + references + appendix in a single submitted file; no separate archive, no URL
[No online host]  a link to proofs "on a website" is not allowed and breaks anonymity — do not use one
[Complete]        every deferred proof is present in the appendix, self-contained and cite-correct
[Reviewer path]   the body forward-references each appendix proof so a reviewer can find it fast
```

## Double-anonymous supplementary hygiene

```text
[No identity]   no authors, affiliations, acknowledgements, funding, or a named system anywhere in the
                body or the appendix
[Third person]  self-citations phrased in the third person, in the body and the appendix alike
[No revealing link] no arXiv/homepage/repository link that discloses authorship; withhold or anonymize
[Clean PDF]     scrub PDF metadata (author/producer) before upload
```

## Appendix architecture

- Order appendix sections to mirror the body's theorem order; reviewers navigate by theorem number,
  not page.
- Keep each appendix proof referenced from the body at least once — an orphaned proof is invisible.
- Make each appendix proof self-contained: restate the theorem, state assumptions, and cite the exact
  prior lemmas used, so a reviewer can check it without reconstructing context.

## Vignette: splitting a two-bound paper

A paper with an upper-bound algorithm and a lower-bound reduction: the body keeps the model, both
theorem statements, the algorithm with its invariant and complexity accounting, and the crux of the
reduction; the appendix holds the full correctness proof, the complete gadget construction, and the
secondary corollaries — each forward-referenced from the body, all inside the one submitted PDF, with
no external link and no identity leak.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] any unproved decision-critical step? <none / move full proof to appendix: what>
[Single-PDF check] all proofs in the submitted file? no external/online appendix? yes/no
[Page budget] body within 15 pp (excl. refs)? appendix forward-referenced? yes/no
[Anonymity] body + appendix clean of identity + metadata? passed/issues
```
