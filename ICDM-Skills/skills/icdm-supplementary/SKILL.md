---
name: icdm-supplementary
description: Use when organizing supplementary and appendix material for an ICDM (IEEE International Conference on Data Mining) paper - deciding what belongs in the body, in an appendix that counts inside the single 10-page IEEE cap, or in an external anonymized repository, plus planning the compression if the paper is accepted as a short paper.
---

# ICDM Supplementary

Decide where each piece of evidence lives under ICDM's unusual constraint: the appendix is
**not** free space. At ICDM the 10-page IEEE two-column cap **includes the bibliography and
any appendices**, so an appendix competes with the body for the same pages. Anything that will
not fit belongs in the **external anonymized repository**, cited in the PDF.

## The three containers

| Container | Counts toward 10 pages? | What belongs there |
|---|---|---|
| Body | Yes | The mining task, mechanism, main results, the argument's spine |
| In-cap appendix | **Yes** | Short proofs, a key ablation table, protocol detail the body references |
| External anonymized repo | No | Code, full logs, extra datasets, long proofs, overflow tables |

The mistake ICDM punishes is treating the appendix like a KDD/CIKM "extra pages after
references" allowance. There is no such allowance here — every appendix line is a body line you
chose not to write.

## Allocation rules

- The body must be **self-contained**: a reviewer should grasp the contribution and judge
  correctness without opening the repository, because there is traditionally no rebuttal to
  clarify later.
- Put in the in-cap appendix only what genuinely earns its space against the body — the one
  proof or ablation a skeptical reviewer needs on the page.
- Push bulk to the repository: full hyperparameter grids, additional datasets, extended tables,
  and code. Cite it precisely so reviewers can find the specific artifact.

## Keep every container triple-blind (Research Track)

- The in-cap appendix is part of the anonymized PDF: no names, acknowledgements, or grant
  numbers hiding at the end.
- The external repository must be history-scrubbed and free of institutional paths and internal
  dataset names (see `icdm-artifact-evaluation`).

```text
Allocation worked example (10-page all-inclusive budget):
  body            ~7.5 pages  (task, mechanism, main experiments, discovery-validity)
  references      ~1.0 page   (pruned to the mechanism-contrast set)
  in-cap appendix ~1.5 pages  (one proof sketch + the key ablation table)
  repository      unbounded   (code, full logs, extra datasets, long proofs)
  -------------------------------------------------------------------
  PDF total       10.0 pages  <- hard cap; over 10 = rejected without review
```

## Plan the short-paper compression now

Because ICDM may accept a full submission **as a short paper**, keep a compression map ready:
which body sections collapse to a paragraph, which figures merge, and which detail moves
entirely to the repository, while the mechanism and its single strongest result stay in the
(shorter) body. Deciding this before the notification saves the camera-ready week (see
`icdm-camera-ready`).

## Vignette: the appendix that cost a reject

A team wrote a complete 10-page body, then appended three pages of proofs — reading ICDM's cap
as body-only. The 13-page PDF was rejected without review. Rebuilt correctly, one proof sketch
stayed in a 1.5-page in-cap appendix, the full proofs and extended tables moved to the cited
anonymized repository, and the related-work prose was trimmed to hold the total at 10. Same
science, but now inside the only budget ICDM allows.

## Output format

```text
[Body self-contained] yes / no (fix if no)
[Appendix in-cap] fits inside 10 pages: yes / over budget
[Repo offload] code + overflow moved out and cited: yes / no
[Anonymity] appendix + repo triple-blind clean: yes / leaks found
[Short-paper map] compression plan ready: yes / no
[Reallocation] <what to move body -> appendix -> repo to hit 10 pages>
```
