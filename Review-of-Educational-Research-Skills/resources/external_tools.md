# External Tools & Resources for the Review of Educational Research (RER)

Tools, databases, and services useful when preparing a *Review of Educational
Research* (RER) **systematic review, meta-analysis, or critical integrative
synthesis**. RER is AERA's review journal of record: a typical article **synthesizes
a body of research bearing on education**, so the toolchain is built for **systematic
literature discovery, screening, coding, evidence synthesis, meta-analysis, and
transparent reporting** — not for running original primary data collection. (RER
publishes no original empirical research of the author's own; the data of an RER
article is its documented search, coding, and synthesis — see
`official-source-map.md`.) Verify volatile process specifics on the official
SAGE/AERA RER pages.

## 1. Literature discovery & indexing

| Source | Provider | Typical use in a review |
|--------|----------|--------------------------|
| ERIC | U.S. Dept. of Education / IES | The education index; search by descriptor + keyword |
| PsycINFO / APA PsycNet | American Psychological Association | Learning, cognition, motivation literature bearing on education |
| Education Source / Education Full Text | EBSCO | Broad education coverage incl. practitioner journals |
| Web of Science / Scopus | Clarivate / Elsevier | Cross-disciplinary coverage + **forward citation** for snowballing |
| ProQuest Dissertations & Theses | ProQuest | **Grey literature** — null/small-sample results that reduce publication bias |
| What Works Clearinghouse / IES | U.S. Dept. of Education | Vetted intervention evidence and reports |
| EconLit / NBER | AEA / NBER | Education-economics work indexed outside education databases |
| Google Scholar | Google | Forward-citation snowballing to saturation (not a sole source) |

> Coverage discipline (see `revedres-literature-synthesis`): map constructs to each
> field's vocabulary, sweep multiple databases + grey literature, then snowball
> backward and forward to **saturation**, logging every count for the PRISMA flow.

## 2. Screening, coding & reference management

- **Reference managers:** Zotero, Mendeley, EndNote, BibTeX/BibLaTeX — an RER review
  has a very large reference set; keep it curated and de-duplicated.
- **Systematic-review screening:** **Covidence**, **Rayyan**, **DistillerSR**,
  **EPPI-Reviewer** — dual independent screening, conflict tracking, and PRISMA-count
  export.
- **Coding / extraction:** a structured codebook in a spreadsheet or a tool above;
  capture design, sample/context, measure, effect size + variance, moderators, and
  risk-of-bias per study (see `revedres-literature-synthesis`).
- **Inter-rater reliability:** compute Cohen's/Fleiss' κ (categorical) or ICC
  (continuous) and **report the value** (R `irr`/`psych`; Stata `kap`/`icc`).

## 3. Reporting standards & registration

- **PRISMA** (`prisma-statement.org`) — checklist + flow diagram; RER directs
  systematic-review/meta-analysis authors here.
- **APA "Reporting Standards for Research in Psychology" (JARS / MARS)** —
  RER's guidance cites the *American Psychologist* article for meta-analyses.
- **PRISMA-P** — protocol-reporting checklist; **PROSPERO** / **OSF** — protocol
  registration so the search is demonstrably a-priori (see
  `revedres-proposal-and-commissioning`).

## 4. Meta-analysis software (only where estimates are commensurable)

If the review pools effect sizes, treat it as a meta-analysis with its assumptions:
- **R:** `metafor` (the workhorse — multilevel/robust variance, moderators, bias
  diagnostics), `meta`, `robumeta`, `dmetar`; **Stata:** the `meta` suite, `robumeta`;
  **Python:** `PythonMeta`, `statsmodels`; **CMA** (Comprehensive Meta-Analysis) GUI.
- Report effect-size metric, model (fixed/random/multilevel/robust variance),
  heterogeneity (I²/τ²), moderators, **dependent-effects handling**, and
  publication-bias diagnostics (funnel, Egger, trim-and-fill, p-curve/selection
  models). Pool only where the literature genuinely supports it — otherwise a
  qualitative evidence-map table is more honest (see `revedres-tables-figures`).

## 5. Writing & typesetting
- **Microsoft Word** is required by RER (the system converts it; do not upload PDF).
- **APA 7th edition** throughout — citations, references, headings, tables, figures,
  and bias-free language. Reference managers can apply APA 7 automatically; verify
  output.

## 6. Process & portal (verify on the official SAGE/AERA RER pages — 检索于 2026-06)
| Item | Note |
|------|------|
| Submission portal | **Manuscript Central / ScholarOne** (`mc.manuscriptcentral.com/rer`) |
| Artefact | Comprehensive, critical, integrative review (no original empirical research) |
| Style | **APA 7th**; abstract **≤ 150 words** + keywords; **Word** (not PDF) |
| Files | Unblinded title page + blinded manuscript + Author Bios; masked review |
| Reporting standards | PRISMA + APA Reporting Standards (MARS) for systematic reviews/meta-analyses |
| Fee / editors / length / timeline | **待核实 / volatile** — re-confirm on the SAGE/AERA RER pages |

## 7. Cautions
1. **Verify volatile specifics** (editors, fee, length, formatting) on the official
   SAGE/AERA RER pages — they change.
2. **A review appraises, it does not re-collect** — your tools are for discovery,
   screening, coding, synthesis, and reporting, not original data collection.
3. **Comprehensiveness is provable** — document the search so a reviewer cannot name
   an omitted study or database.
4. **Pool only commensurable estimates** — a spurious meta-analytic number is worse
   than an honest qualitative evidence map.
5. **The `10.3102/` DOI stem is shared across AERA journals** — it confirms AERA, not
   RER specifically; check the journal name before attributing a piece to RER (see
   `exemplars/library.md`).
