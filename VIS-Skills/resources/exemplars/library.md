# IEEE VIS Exemplars Library (contribution type × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and **IEEE Xplore / TVCG** to confirm it appeared at an **IEEE Visualization Conference
> track (InfoVis / VAST / SciVis, now unified IEEE VIS) and published in IEEE TVCG** — matching
> title, author list, year, and venue string. Papers that could not be cleanly confirmed as an IEEE
> VIS/TVCG placement (as opposed to EuroVis/CGF, CHI, SIGGRAPH, or a non-VIS journal) were
> **omitted and documented below**. It is deliberately a short, verified list (5 verified > 15
> guessed).
>
> **Sibling-confusion guard:** IEEE VIS is **not** EuroVis (Computer Graphics Forum), **not** CHI,
> and **not** SIGGRAPH. Several canonical visualization ideas were introduced at those venues
> instead; a famous author or a familiar system name does **not** prove an IEEE VIS placement. Each
> row was checked to be an IEEE VIS / TVCG edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, effect sizes, or table numbers — read the original on IEEE Xplore
> before citing anything. For VIS-specific policy, the six-area model, and the two-phase cycle, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution type × method** is closest to yours, then study how that paper
grounds a **data-and-task problem**, justifies its **visual encoding and interaction**, and backs
its claim with **evidence matched to the contribution type** — the VIS bar (see
[`../../skills/vis-writing-style/SKILL.md`](../../skills/vis-writing-style/SKILL.md),
[`../../skills/vis-topic-selection/SKILL.md`](../../skills/vis-topic-selection/SKILL.md), and
[`../../skills/vis-experiments/SKILL.md`](../../skills/vis-experiments/SKILL.md)). For each, ask the
self-check question before claiming your paper is "VIS-shaped."

Several rows are IEEE VIS **Test-of-Time** honorees, so they also model what "influence a decade
later" looks like at this venue.

---

## By contribution type

### System / toolkit — visualization infrastructure

- **Bostock, Ogievetsky & Heer, "D³ Data-Driven Documents," IEEE InfoVis 2011** (IEEE TVCG
  17(12):2301-2309, DOI 10.1109/TVCG.2011.185). Verified: IEEE Xplore / dblp; IEEE VIS
  Test-of-Time honoree. Introduced a representation-transparent approach binding data to web-document
  elements.
  - **Why it is an exemplar:** it reframes web visualization around directly manipulating the
    document, delivering a **toolkit others build on** rather than a one-off system — the classic VIS
    "infrastructure contribution" evaluated by expressiveness and adoption.
  - **Self-check:** is your system a reusable capability a third party could build with, evaluated on
    real use, rather than a feature list?

### Encoding / interaction technique — set visualization

- **Lex, Gehlenborg, Strobelt, Vuillemot & Pfister, "UpSet: Visualization of Intersecting Sets,"
  IEEE InfoVis 2014** (IEEE TVCG 20(12):1983-1992). Verified: IEEE Xplore / dblp; IEEE VIS
  Test-of-Time honoree (2024). A tabular technique for sets, their intersections, and aggregates,
  with coordinated interaction.
  - **Why it is an exemplar:** a **named technique** that solves a task (analyzing many intersecting
    sets) prior encodings handled poorly at scale, justified by task and adopted widely across
    fields.
  - **Self-check:** does your encoding serve a specific task that conventional charts fail at, and is
    that failure demonstrated rather than asserted?

### Perceptual / empirical study — what people remember

- **Borkin, Vo, Bylinskii, Isola, Sunkavalli, Oliva & Pfister, "What Makes a Visualization
  Memorable?", IEEE InfoVis 2013** (IEEE TVCG 19(12):2306-2315). Verified: IEEE Xplore / dblp. A
  large study of memorability across thousands of real visualizations.
  - **Why it is an exemplar:** it turns a design folk-belief into a **controlled empirical result**
    on real stimuli, changing what the community believes about "chart junk" — evidence matched to a
    perceptual claim.
  - **Self-check:** does your study change design practice with stimuli, a task, and statistics a
    reviewer could scrutinize, rather than author intuition?

### Design study / methodology — how to do applied VIS

- **Sedlmair, Meyer & Munzner, "Design Study Methodology: Reflections from the Trenches and the
  Stacks," IEEE InfoVis 2012** (IEEE TVCG 18(12):2431-2440, DOI 10.1109/TVCG.2012.213). Verified:
  IEEE Xplore / dblp. A framework distilled from many design studies.
  - **Why it is an exemplar:** it interrogates **how the field does applied work**, offering
    definitions, a process, and validation guidance — a methodology contribution that improves
    everyone's practice, not one tool's score.
  - **Self-check:** does your design study reflect a **transferable lesson** validated across
    abstraction levels, or is it a single tool with no generalizable takeaway?

### Model / theory — design and validation

- **Munzner, "A Nested Model for Visualization Design and Validation," IEEE InfoVis 2009** (IEEE
  TVCG 15(6):921-928, DOI 10.1109/TVCG.2009.111). Verified: IEEE Xplore / dblp. A four-level model
  (domain, abstraction, encoding/interaction, algorithm) with level-specific validation.
  - **Why it is an exemplar:** it provides a **prescriptive framework** the field uses to reason
    about threats to validity at each design level — the "foundations" mode VIS is built on.
  - **Self-check:** does your framework give the community a reusable way to design or evaluate, with
    the levels/claims laid out explicitly?

---

## Contribution-type ↔ exemplar (verified rows)

| Contribution type | Verified IEEE VIS exemplar | Track / Year | Method |
| --- | --- | --- | --- |
| System / toolkit | Bostock, Ogievetsky & Heer, "D³" | InfoVis 2011 | Web visualization toolkit |
| Encoding / interaction technique | Lex et al., "UpSet" | InfoVis 2014 | Set visualization |
| Perceptual / empirical study | Borkin et al., "What Makes a Visualization Memorable?" | InfoVis 2013 | Controlled study |
| Design study / methodology | Sedlmair, Meyer & Munzner, "Design Study Methodology" | InfoVis 2012 | Methodology |
| Model / theory | Munzner, "A Nested Model..." | InfoVis 2009 | Design/validation model |

> Five verified papers across five VIS contribution types. Note that all pre-2021 rows carry the
> historical **InfoVis** track string; since the 2021 unification these would all be **IEEE VIS**
> full papers under the six-area model.

---

## Omitted for lack of clean IEEE VIS/TVCG verification (do not attribute without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **Cleveland & McGill, "Graphical Perception..."** — the foundational encoding-effectiveness study
  appeared in **JASA (1984)**, a statistics journal, *not* IEEE VIS. Cite it, but do not attribute it
  to VIS.
- **Heer & Bostock, "Crowdsourcing Graphical Perception..."** — verified to be **ACM CHI 2010**, not
  an IEEE VIS/TVCG paper, despite being a canonical perception study. A direct sibling-venue trap.
- **Many EuroVis / Computer Graphics Forum techniques** — EuroVis is a distinct venue publishing in
  CGF, not IEEE VIS/TVCG; confirm the venue string before attributing.
- **Wilkinson, "The Grammar of Graphics"** — a **book**, not a VIS paper; the influence is real but
  the placement is not IEEE VIS.

Before adding any paper, confirm it on **dblp** and **IEEE Xplore** by matching the venue string to
an IEEE VIS track (InfoVis / VAST / SciVis / unified VIS) and TVCG (not EuroVis/CGF, CHI, or
SIGGRAPH), then record authors, year, and DOI/pages, and update the access-date header. When in
doubt, omit. If web search is unavailable, add the row as **待核实 / TO VERIFY** with **no
attribution**.
