---
name: advmat-supplementary
description: Use when partitioning content between an Advanced Materials main text and its Supporting Information, ensuring the paper stands alone while extended data, full experimental detail, and secondary characterization live in the SI. Organizes the Supporting Information; does not write the main text.
---

# Advanced Materials Supporting Information (advmat-supplementary)

## When to trigger

- The manuscript is over the Communication/Article format and detail must move out of the body
- A reader cannot judge the material without opening the SI
- You have extended datasets, full recipes, or control experiments with no home
- You are unsure what belongs in the SI versus what must stay in the main text
- Reviewers of a prior version asked for data that would bloat the body

## The stand-alone rule (non-negotiable)

The main text must be **fully understandable and convincing on its own**. The Supporting Information *supports* the paper; it must never be *load-bearing* for the central advance. A reader who never opens the SI should still grasp the material, the decisive evidence that it is what you claim, the property, and the benchmarked function.

- The central advance, the decisive characterization, and the headline benchmarked metric live in the **main text**.
- The SI holds the exhaustive backup a skeptical referee or a group trying to reproduce the work will want.
- Every SI item is **cited from the main text** at the point it becomes relevant.

If removing the SI collapses the argument, the partition is wrong — pull the essential piece back into the main text (and trim elsewhere via `advmat-length-management`).

## What belongs in Supporting Information

| Content                                             | Home       |
|-----------------------------------------------------|------------|
| Full synthesis recipes, optimization sweeps          | SI         |
| Extended characterization (more samples, techniques) | SI         |
| Full device fabrication protocols, control devices   | SI         |
| Complete benchmarking table with all references      | SI         |
| Per-sample statistics, histograms, batch data        | SI         |
| Additional figures, movies, large data tables        | SI         |
| DFT/computational details, input files               | SI         |
| The central advance and its decisive evidence        | Main text  |
| The property mechanism linking structure to function | Main text  |
| The headline benchmarked metric with n and spread    | Main text  |

## SI organization

- Mirror the main text's logic: order SI sections to match the order they are cited.
- Give SI sections clear headings and self-contained captions; label SI figures/tables distinctly (Figure S1, Table S1).
- Include an SI Experimental Section detailed enough to reproduce the material if the main-text version is condensed.
- Keep the SI honest: it is peer-reviewed alongside the paper — not a place to bury weak or contradictory data.
- Provide computational and raw-data availability per current Wiley policy (repository + DOI where required).

## Checklist

- [ ] The main text is convincing without ever opening the SI
- [ ] No decisive evidence for the advance lives *only* in the SI
- [ ] Every SI item is cited from the main text at the relevant point
- [ ] SI sections ordered to match their citation order
- [ ] SI figures/tables labeled S1, S2, ... distinctly from main-text items
- [ ] The full reproducible recipe/protocol is in the SI if condensed in the body
- [ ] Nomenclature and units are consistent between main text and SI
- [ ] Data/computational availability handled per current Wiley policy

## Anti-patterns

- A paper that silently depends on the SI to be believed
- Burying the decisive characterization or the benchmarking in the SI
- An SI that is a disorganized data dump rather than a structured appendix
- SI figures referenced out of order or never cited from the body
- Nomenclature/unit drift between main text and SI
- Using the SI to smuggle in claims the referees did not scrutinize

## Output format

```
【Main text stands alone】yes / fix (pull back: ...)
【SI sections】S1: ... / S2: ... (cited from body?)
【Decisive evidence only in SI?】none / move back: ...
【SI figure/table labels】S-prefixed?  yes / fix
【Reproducible recipe present】yes / fix
【Nomenclature consistent body↔SI】yes / fix
【Next】advmat-writing-style or advmat-length-management
```

> SI scope, file formats, and data-deposition rules are set by Wiley and evolve — verify on the official Advanced Materials author page.
