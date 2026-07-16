# Molecular Cell Manuscript Template

> Skeleton for a Molecular Cell (Cell Press) Research Article. Replace every [bracket]; delete guidance notes.
> Confirm all limits against the current
> [Molecular Cell information for authors](https://www.cell.com/molecular-cell/information-for-authors).
> Molecular Cell uses **STAR Methods**, a **Key Resources Table**, and **Cell Press numbered references**.

---

## Title
**[Declarative title naming the molecular actor and molecular action — e.g., "PROTEIN X unwinds DNA by a single-subunit ATP ratchet"].**
> Avoid "Towards", "Characterization of", "Role of", "Novel". Name the mechanism, not just the system.

## Authors & affiliations
[Author One^1], [Author Two^2], … [Corresponding/Lead Contact^1,*]
1. [Affiliation]
2. [Affiliation]
\* Lead Contact: [name, email]  ·  ORCIDs: [...]

## Highlights (3–4 bullets, each ≤ 85 characters incl. spaces)
- [Actor does molecular action on substrate]            (__ chars)
- [Mechanism: residue/interface/step drives process]    (__ chars)
- [Point mutant uncouples activity from outcome]        (__ chars)
- [Physiological consequence for the process]           (__ chars)

## eTOC / In Brief blurb (~50 words, third person)
> [Author et al.] show that [plain-language molecular finding]. [One sentence of mechanism in accessible
> terms.] [One sentence on why it matters for the process or for disease.] Never "we".

## Graphical Abstract
> Single panel; left→right or top→bottom cause → mechanism → effect; minimal text; RGB; colorblind-safe.
> Describe here for the designer: [top state] → [mechanism icon] → [outcome].

## Summary (single unstructured paragraph, ~150 words; no citations, no subheadings)
[Molecular context/stakes.] [Gap/question.] [What we did + the mechanism, named at the molecular level,
with ≥1 quantified result and the orthogonal evidence.] [Physiological consequence for a molecular-biology
readership.]

---

## Introduction (~3 short paragraphs)
> ¶1 the molecular problem and the specific step not understood. ¶2 the gap/hypothesis. ¶3 what we found,
> ending on the physiological consequence — the reader knows the mechanism before Results.

## Results
> Descriptive, molecular-claim subheadings; each block: claim → evidence (figure + numbers + stats) →
> inference and the alternative excluded. Order by the proof of mechanism, not by chronology.

### [Subheading = molecular claim 1: establish the phenomenon / pose the question] (Figure 1)
[...]

### [Subheading = molecular claim 2: define the mechanism — structure/biochemistry/reconstitution] (Figures 2–3)
[...]

### [Subheading = molecular claim 3: separation-of-function ties mechanism to phenotype] (Figure 4)
[...]

### [Subheading = molecular claim 4: physiological relevance in cells / in vivo] (Figures 5–6)
[...]

## Discussion
> Interpret, don't recap. State the molecular model, exclude the main alternative, state limitations,
> end on the mechanistic significance / open molecular question.

---

## STAR Methods

### Key Resources Table
| REAGENT or RESOURCE | SOURCE | IDENTIFIER |
|---------------------|--------|------------|
| **Antibodies** | | |
| Anti-[X] ([clone, host]) | [Vendor] | Cat# ____; RRID:AB______ |
| **Chemicals, Peptides, Recombinant Proteins** | | |
| Purified [PROTEIN X] (residues a–b, tag) | This paper | N/A |
| **Critical Commercial Assays** | | |
| **Deposited Data** | | |
| [ChIP/RNA-seq], this paper | This paper | GEO: GSE______ |
| [Cryo-EM map + model], this paper | This paper | EMDB: EMD-____ ; PDB: ____ |
| [Mass spec], this paper | This paper | PRIDE: PXD______ |
| **Experimental Models: Cell Lines / Organisms** | | |
| **Oligonucleotides** | | |
| [sgRNA/primer/probe sequence] | This paper | N/A |
| **Recombinant DNA** | | Addgene #______ |
| **Software and Algorithms** | | RRID:SCR______ / DOI |

### Resource Availability
- **Lead Contact:** [Name, email]. Requests for resources/reagents go to the Lead Contact.
- **Materials Availability:** [How unique reagents are shared — Addgene/MTA — or "did not generate new unique reagents."]
- **Data and Code Availability:**
  - [DATA] [...] deposited at [GEO/PDB+EMDB/PRIDE]; accession numbers in the Key Resources Table.
  - [CODE] All original code deposited at [Zenodo/Mendeley Data]; DOIs in the Key Resources Table. / No original code.
  - [ADDITIONAL] Any additional information is available from the Lead Contact upon request.

### Experimental Model and Subject Details
[Organisms/strains/cell lines: sex, age, source, passage, authentication, mycoplasma; expression hosts;
participants + ethics (IRB/IACUC, consent, protocol numbers).]

### Method Details
[Protein expression and purification (constructs, tags, columns); reconstitution; in-vitro assays;
cryo-EM/crystallography collection and processing; genomics library prep and pipelines; single-molecule
setups — reference reagents by their KRT entries.]

### Quantification and Statistical Analysis
[Per result: statistical test, definition of n and what it represents, dispersion (SD/SEM/CI), thresholds,
software; structure resolution/refinement/validation; genomics normalization; kinetics/single-molecule
fitting. Must match figure legends.]

---

## Figure legends
> Each: title sentence (mechanistic claim) + per-panel (A, B, C…) + statistics (test, exact n, replicate
> type, error-bar definition, P values) + structure/genomics metadata. Stand-alone.

## References
> Cell Press numbered style: superscript numbers in order of first appearance; list numbered by appearance;
> full author lists; abbreviated journal names; single merged list incl. STAR Methods citations.
1. [Author, A.B., Author, C.D., and Author, E.F. (Year). Title. Abbrev. Journal Vol, pages.]

## Supplemental Information
[Supplemental figures/tables/videos + captions; orthogonal confirmations and controls moved here.]

---

## Cover letter scaffold (separate file at submission; ~250–400 words, one page)

[Date]

Dear Dr. [Editor Name],

We submit our manuscript, **"[Declarative title],"** for consideration as an **Article** in *Molecular Cell*.

**[Mechanistic advance.]** We show that [molecular actor] [molecular action] by [mechanistic detail],
resolving how [process] is controlled and why [physiological outcome] depends on it. [One sentence
quantifying the headline result — a rate, affinity, resolution, or fold-change.]

**[Why this is proven, not proposed.]** The mechanism is supported by orthogonal approaches — [e.g.,
structure, reconstitution from defined components, and separation-of-function genetics] — and we tie it to
the phenotype with point mutants that break only the proposed step. The in-vitro mechanism is validated
in [cells / in vivo].

**[Why Molecular Cell.]** This advance addresses the mechanism-focused readership of *Molecular Cell* in
[gene expression / chromatin / RNA biology / replication-repair / signaling / proteostasis / structure],
and is timely because [why-now: a method makes the step visible / a controversy is now decidable].

**[Vs. prior and concurrent work.]** Unlike [closest prior work], which [limitation — e.g., localized the
factor without the molecular step], our study [decisive distinction]. [Concurrent work, if any, and how we
differ.]

This work is original, not published, and not under consideration elsewhere. All authors approved the
submission and declare [no competing interests / the interests listed]. Lead Contact: [Name, email].

[Optional: suggested/opposed reviewers.]

Sincerely,
[Corresponding author, on behalf of all authors]
[Affiliation] · [email] · [ORCID]
