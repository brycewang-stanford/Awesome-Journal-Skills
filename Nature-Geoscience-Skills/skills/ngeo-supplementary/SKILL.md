---
name: ngeo-supplementary
description: Use when partitioning content between the Nature Geoscience main text and its Supplementary Information, ensuring the Article stands alone while extended data, model output, and derivations live in the SI. Organizes the SI; does not write the main text.
---

# Nature Geoscience Supplementary Information (ngeo-supplementary)

## When to trigger

- The Article is over 3,000 words and detail must move out of the main text
- A reader cannot follow the main text without consulting the Supplementary Information
- You have extended maps, full model ensembles, derivations, or additional proxies with no home
- You are unsure what is allowed in SI versus what must stay in the main text or online Methods
- Referees of a prior version asked for material that would bloat the main text

## The stand-alone rule (non-negotiable)

The main text must be **fully understandable on its own**. The Supplementary Information *supports* the Article; it must never be *load-bearing* for the headline advance. A reader who never opens the SI should still grasp the result, the core evidence for it, its uncertainty, and why it matters.

- The headline advance, its decisive evidence, and the headline uncertainty live in the **main text**.
- The **online Methods** holds the reproducible protocol (instruments, model setup, statistics).
- The **SI** holds the exhaustive backup a skeptical referee or replicator wants: extended datasets, full ensembles, sensitivity tests, additional figures and tables.

If removing the SI breaks the argument, the partition is wrong — pull the essential piece back into the main text (and trim elsewhere via `ngeo-length-management`).

## Methods vs. SI (a common confusion)

Nature Geoscience has *both* an online Methods section and Supplementary Information; they are not the same:

| Content                                              | Home           |
|------------------------------------------------------|----------------|
| Reproducible protocol (instrument, model config, statistics) | online Methods |
| Full uncertainty budget / error propagation           | online Methods |
| Extended data figures, additional maps/sections       | SI             |
| Full model ensemble members, sensitivity sweeps        | SI             |
| Supporting derivations / lengthy algebra               | SI             |
| Secondary proxies, additional sites, robustness checks | SI             |
| Large data tables                                      | SI             |
| The headline advance and its decisive evidence          | main text      |
| The headline uncertainty                                | main text      |

## SI organization

- Mirror the Article's logic: order SI sections to match the order they are cited in the main text and Methods.
- Give SI sections clear headings and self-contained captions; label figures/tables **Fig. Sn / Table Sn / Supplementary Note n**.
- Every SI item is **cited from the main text or Methods** at the point it is relevant; nothing goes uncited.
- Keep notation, units, and symbol definitions consistent with the main text and Methods.
- Keep the SI honest: it is peer-reviewed alongside the Article, not a place to bury weak results, unvalidated model runs, or claims the referees did not vet.

## Checklist

- [ ] The main text is understandable without ever opening the SI
- [ ] No headline-advance evidence is *only* in the SI
- [ ] Reproducible protocol is in online Methods, not scattered in SI
- [ ] Every SI item is cited from the main text or Methods at the relevant point
- [ ] SI sections ordered to match their citation order
- [ ] SI figures/tables labeled Fig. Sn / Table Sn distinctly
- [ ] Extended data, full ensembles, and derivations live in SI
- [ ] Notation and units consistent across main text, Methods, and SI

## Anti-patterns

- A main text that silently depends on the SI to be understood
- Burying the decisive evidence or headline uncertainty in the SI
- Confusing SI with online Methods (protocol scattered instead of consolidated)
- An SI that is a disorganized dump rather than a structured appendix
- SI items referenced out of order or never cited
- Notation/unit drift between main text, Methods, and SI
- Using SI to smuggle in unvalidated model runs or claims reviewers did not see

## Output format

```
【Main text stands alone】yes / fix (pull back: ...)
【Methods vs. SI split correct】yes / fix
【SI sections】S1: ... / S2: ... (cited from main text/Methods?)
【Headline evidence only in SI?】none / move back: ...
【SI labels】Fig. Sn / Table Sn?  yes / fix
【Notation consistent across all three】yes / fix
【Next】ngeo-writing-style or ngeo-length-management
```

> SI scope, labeling, and the Methods/SI boundary evolve — verify on the official Nature Geoscience author pages (Checked: 2026-07-16).
