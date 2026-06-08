# JACS Resources

Action-oriented resources for the **Journal of the American Chemical Society
(JACS)** skill pack. The `skills/` give advice; this directory lets an agent
**act** — model a JACS-style abstract/opening, benchmark against verified
exemplars, and find the right external tools and deposition services. Pair these
with the relevant `skills/jacs-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper **abstract + opening** in JACS house style — concise significance, the problem → advance → number → significance arc, the TOC-graphic convention, and the Communication vs Article choice. Illustrative **fictional** paper; no invented policy. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified JACS papers** (DOIs `10.1021/ja...` / `10.1021/jacs...`) organized by subfield × method. Design positioning only — no fabricated yields/ee. Includes a sibling-confusion guard (JACS is not *Angew. Chem.*, *Nature Chem.*, *Chem. Sci.*, or other ACS titles). |
| [`official-source-map.md`](external_tools.md) | **JACS-specific policy & facts** — ACS Paragon Plus submission, TOC-graphic and SI rules, CIF/CCDC deposition, characterization/data requirements, scope, and a do-not-misattribute list. The authoritative pack source for venue policy. *(Authoritative policy index for the pack; populate/verify against the official ACS JACS author page before relying on it.)* |
| [`external_tools.md`](external_tools.md) | Databases, characterization platforms, deposition services (CCDC/CSD, PDB, BMRB, ICSD), and software referenced by the pack across organic, inorganic, materials, physical, analytical, and biological chemistry. |

## Scope note — no econometrics/empirical code kit (chemistry venue)

Unlike the economics packs in this repo, **JACS does not vendor a statistical /
causal-inference code kit** (no Stata/Python DID–IV–RDD–DML pipeline). JACS is a
broad-scope **chemistry** journal; reproducibility here means full
**characterization and crystallographic deposition** (NMR/HRMS/IR, CIF + CCDC
numbers, computational coordinates), not regression code. The relevant tools are
indexed in [`external_tools.md`](external_tools.md). There are intentionally **no
`../../shared-resources/` links** from this pack — its resources are self-contained
and discipline-appropriate.

## Suggested workflow

1. **Test fit and pick a format** with
   [`../skills/jacs-scope-fit/SKILL.md`](../skills/jacs-scope-fit/SKILL.md)
   (advance test + breadth test; Communication vs Article).
2. **Frame the advance** with
   [`../skills/jacs-results-framing/SKILL.md`](../skills/jacs-results-framing/SKILL.md)
   and model your abstract/opening on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
3. **Polish to ACS house style** with
   [`../skills/jacs-writing-style/SKILL.md`](../skills/jacs-writing-style/SKILL.md)
   and build ACS-style schemes/TOC with
   [`../skills/jacs-figures/SKILL.md`](../skills/jacs-figures/SKILL.md).
4. **Benchmark** your subfield × method against verified papers in
   [`exemplars/library.md`](exemplars/library.md).
5. **Gather tools and deposit data** via
   [`external_tools.md`](external_tools.md), then run the pre-submission gate with
   [`../skills/jacs-submission/SKILL.md`](../skills/jacs-submission/SKILL.md) and
   confirm current policy in
   [`official-source-map.md`](external_tools.md).
