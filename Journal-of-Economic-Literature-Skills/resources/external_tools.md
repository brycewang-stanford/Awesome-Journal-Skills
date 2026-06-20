# External Tools & Resources for the Journal of Economic Literature (JEL)

Tools, databases, and services useful when preparing a *Journal of Economic
Literature* (JEL) **survey/review article**. JEL is the American Economic
Association's survey-of-record journal: a typical article **synthesizes a body of
economic research**, so the toolchain is built for **systematic literature
discovery, citation management, evidence synthesis, and the JEL classification
system** — not for running original estimations. (JEL publishes no original
empirical research; where a survey contributes its own quantitative synthesis, the
AEA data/code policy applies — see `official-source-map.md`.) Verify volatile
process specifics on the official AEA JEL pages.

## 1. Literature discovery & indexing

| Source | Provider | Typical use in a survey |
|--------|----------|--------------------------|
| EconLit | American Economic Association | The field's index; search by keyword **and JEL classification code** |
| RePEc / IDEAS / EconPapers | RePEc collective | Working papers + published work; author and JEL-code browsing |
| NBER / CEPR working paper series | NBER / CEPR | The frontier — recent work a current survey must include |
| SSRN | Elsevier | Pre-prints and early drafts across economics |
| Google Scholar / Scopus / Web of Science | Google / Elsevier / Clarivate | Forward citation (who cites a seed) for snowball-to-saturation |
| JSTOR | ITHAKA | Historical/archival access to older literature |

> Coverage discipline (see `jel-literature-synthesis`): sweep by **keyword and by
> JEL code**, then snowball forward and backward to **saturation**, and log where
> searches stop yielding new must-cite work.

## 2. Reference management & synthesis

- **Reference managers:** Zotero, Mendeley, EndNote, BibTeX/BibLaTeX — a JEL survey
  has a very large reference set; keep it curated and de-duplicated.
- **Evidence synthesis:** a structured **evidence matrix** (spreadsheet or
  citation-manager notes) capturing, per study: question/estimand, method/data,
  finding (direction + magnitude), your credibility appraisal, and tensions with
  other studies (see `jel-literature-synthesis`).
- **Systematic-review aids (where a structured search helps):** PRISMA-style flow
  documentation, Covidence/Rayyan for screening, Connected Papers / Litmaps /
  Research Rabbit for citation-graph discovery. JEL surveys are usually *narrative*
  syntheses, but documenting the search strengthens the comprehensiveness claim.

## 3. The JEL classification system

- **AEA EconLit JEL Codes** (`aeaweb.org/econlit/jelCodes.php`) — the authoritative
  list, maintained by JEL. Structure: a **letter** (20 top categories), a
  **two-digit** subcategory, a **three-character** detailed code. Assign detailed
  codes top-down and verify each against the current list (see
  `jel-classification-system`).

## 4. Meta-analysis (only where estimates are commensurable)

If a survey contributes a quantitative synthesis of effect sizes, treat it as a
meta-analysis with its assumptions:
- R: `metafor`, `meta`; Stata: `meta` suite; Python: `PythonMeta`, `statsmodels`.
- Report comparability of estimands, weighting, heterogeneity, and
  publication-bias diagnostics (funnel/Egger). Use only where the literature
  genuinely supports pooling — otherwise a qualitative who-found-what table is more
  honest (see `jel-tables-figures`).

## 5. Writing & typesetting
- **LaTeX** (TeX Live / MacTeX / Overleaf) or Word, per the AEA/JEL Style Guide.
- Follow the AEA/JEL **Style Guide** for references and formatting; AEA house style
  is applied at acceptance. Keep references published, archival, or author-provided.

## 6. Process & portal (verify on the official AEA JEL pages — 检索于 2026-06)
| Item | Note |
|------|------|
| Submission portal | AEA **ScholarOne Manuscripts** |
| Intake route | **Proposal** (~10 pp excl. references: contents + reader interest + main references) **or** full paper; pre-proposal email to editor welcomed |
| Disclosure | Separate **"Disclosure Statement"** PDF per (co)author; incomplete without it |
| Data & code | AEA Data and Code Availability Policy applies to any original quantitative content |
| JEL codes | Assigned per the EconLit list; on the title page with keywords |
| Fee / editor / anonymity / length | **待核实 / volatile** — re-confirm on the AEA JEL pages |

## 7. Cautions
1. **Verify volatile specifics** (editor, fee, anonymity, length, style rules) on the
   official AEA JEL pages — they change.
2. **A survey appraises, it does not re-estimate** — your tools are for discovery,
   synthesis, and classification, not original identification or replication.
3. **Comprehensiveness is provable** — document the search so a referee cannot name
   an omitted literature.
4. **Pool only commensurable estimates** — a spurious meta-analytic number is worse
   than an honest qualitative table.
