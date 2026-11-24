---
name: joap-submission
description: Use when running the final pre-submission preflight for the Journal of Applied Psychology (JAP) via Editorial Manager — APA 7th-edition style, the APA submission/masking checklist, anonymization for masked review, the structured abstract, the data-availability/TOP statement, and persistent identifiers for data/materials/code. Final checks; it does not draft content.
---

# Submission Preflight (joap-submission)

The last check before submitting through **Editorial Manager** (`editorialmanager.com/apl`). Three
things sink JAP submissions most often: **a missing or weak theoretical contribution surfacing late**,
**broken masking**, and **incomplete open-science compliance**. Verify volatile specifics (length caps,
abstract limit, checklist contents, current editor) on the official APA page first.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure what the masking and open-science requirements demand
- Confirming the abstract, anonymization, data-availability statement, and deposits are in order

## Process facts (re-verified 2026-11-24 on the APA submission-guidelines page)

- **Owner / publisher:** American Psychological Association (APA). ISSN 0021-9010 / e-ISSN 1939-1854.
- **Portal:** **Editorial Manager**, `editorialmanager.com/apl`.
- **Review:** **masked review only** — "The journal will accept submissions in masked review format only";
  names and affiliations go in the cover letter, and unmasked manuscripts are returned before review.
- **Submission checklist:** completing the **APA-published submission/masking checklist** is required at
  upload and signifies you have read and will follow the guidelines.
- **Style:** **APA 7th edition** throughout.
- **Article types:** Feature Article (length commensurate with contribution); **Research Report ≤ 19
  manuscript pages** excluding title page, abstract, references, tables and figures (25 lines of 12-pt
  text, 1-inch margins = one page; request it in the cover letter); **Integrative Conceptual Review**
  (starts with a 10-page prospectus); occasional Monographs and Commentaries; replications.
- **Abstract:** **≤ 250 words** on a separate page, then **up to five keywords**; content-bearing.
- **Open science (TOP):** a one-paragraph Method subsection titled **"Transparency and openness"**.
  Levels: Citation **L2**; Data, Code, Materials transparency **L1 (disclosure)**; Design & Analysis
  **L2** (follow the JAP methods checklist + JARS); Study and Analysis-plan preregistration **L2**
  (state whether preregistered; masked copy available at submission). Non-empirical papers state why
  TOP data/code/preregistration items do not apply.
- **Data transparency appendix:** last page of the manuscript, detailing every prior, concurrent or
  planned use of the data (original-use policy); identifying details go in the cover letter.
- **Files:** Word (.docx) or a LaTeX ZIP with a PDF; the APA submission checklist is completed at upload.
- **Fee:** submission is free; an APC applies only to gold open access.
- **Current Editor:** Mo Wang (University of Florida) — listed as "Incoming (2027) editor (handling all new submissions in 2026)"; Lillian T. Eby is outgoing editor handling invited revisions only in 2026 (APA editorial-board page, re-verified 2026-11-24).

## Preflight checklist

### Style & format
- [ ] APA 7th edition throughout (headings, statistics with ES + CI, references)
- [ ] Article type chosen; length appropriate (Research Report ≤ 19 manuscript pages excl. title page, abstract, refs, tables, figures)
- [ ] Abstract ≤ 250 words + up to five keywords; states contribution, design, samples, result
- [ ] Tables/figures APA 7th; Table 1 has reliabilities; path tables/figures carry CIs and fit indices

### Masking (for anonymized review)
- [ ] No author names/affiliations anywhere in the manuscript
- [ ] Self-citations neutralized ("as we showed in…" removed)
- [ ] Repository / preregistration links **anonymized** (e.g., OSF anonymized view)
- [ ] Identifying file metadata stripped (document properties, tracked-change authors)
- [ ] Separate, non-anonymous title page prepared as a distinct file

### Open science (TOP)
- [ ] **Data** deposited + DOI + codebook (or justified exemption)
- [ ] **Materials** (scales, manipulations, instructions) deposited + DOI
- [ ] **Analysis code** deposited; reproduces results in a fresh session
- [ ] **"Transparency and openness"** Method subsection drafted (data / code / materials availability, preregistration status, JAP methods checklist followed)
- [ ] **Data transparency appendix** as the last manuscript page (prior/concurrent/planned uses of the data)
- [ ] Preregistration linked (anonymized); confirmatory/exploratory split consistent

### Stats & rigor
- [ ] Measurement model reported (CFA fit + reliability) before structure
- [ ] Effect sizes + CIs for key paths; indirect effects with bootstrap/Monte Carlo CIs
- [ ] Nesting modeled (ICC/r_wg); CMV remedies stated
- [ ] Full disclosure of N-determination, exclusions, conditions, measures

## Worked micro-example — preflight verdict (illustrative)

Running the servant-leadership package through the gate the night before upload:

```
Style:      APA 7th throughout; abstract 241/250 words + 5 keywords → PASS*
Contribution: cross-level mechanism + boundary stated by p.3 → PASS
Masking:    no names; self-cites neutralized; OSF anonymized-view links;
            PDF metadata stripped; separate title page → PASS
Open sci:   data + materials + code each have a DOI; data-availability
            statement + prior-use note; experiment preregistration linked → PASS
Stats:      CFA fit + reliabilities reported; indirect = .13, 95% CI [.05, .23];
            multilevel model + ICC/r_wg; CMV remedies declared → PASS
Verdict:    ready to upload to Editorial Manager.
*Abstract limit (250) and Research Report cap (19 pages) re-verified 2026-11-24; re-check before upload.
```

## Last-mile failure modes that trigger a return

| Failure | Caught by | Quick fix |
|---------|-----------|-----------|
| Author name in self-citation or OSF link | masking check | neutralize self-cites; switch to anonymized view |
| Abstract over the current limit | abstract check | cut to the limit; keep contribution + design + result |
| "Data on request" instead of a DOI | open-science check | deposit and mint a persistent identifier |
| No data-availability statement | TOP check | draft it from the live DOIs |
| Table 1 missing reliabilities; paths lack CIs | exhibit check | add ω to the diagonal; add CIs + fit indices |

> Volatile specifics (length caps, abstract limit, TOP level, checklist contents, current editor) change.
> Re-confirm every item above against the journal's current submission guidelines before relying on it.
> See [`templates/checklist.md`](templates/checklist.md) for a copy-paste preflight list.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue journal-of-applied-psychology-skills   # from a clone of the AJS repository
```

It reports, with a location for each finding:

- this venue's machine-readable limits, review mode and required statements, when the venue has a
  rules block (`--list-venues`);
- citations ↔ references;
- table and figure numbering, cross-references and standard-error notes;
- abstract numbers traced to the tables;
- placeholders and tracked changes.

With the Research Toolkit pack installed, `rt-submission-readiness` runs the same check as stage 0
of the full pre-submission pipeline (scorecard → referee panel → polish → cover letter). Anything
it lists as *not checked* still needs the manual items below.

## Anti-patterns

- Submitting with the theoretical contribution buried or absent
- Broken masking (names, self-references, or identifying repository links)
- "Available on request" instead of persistent DOIs; missing data-availability statement
- Abstract over the current limit or missing the contribution/design/result
- Tables/figures without reliabilities, CIs, or fit indices

## Output format

```
【Style】APA 7th + article type + abstract ≤ 250 + ≤ 5 keywords? [Y/N]
【Contribution legible early?】[Y/N]
【Masking】manuscript + self-cites + repo links + metadata + title page? [Y/N]
【Open science】data + materials + code + DOIs + availability statement? [Y/N]
【Stats】measurement model + ES/CIs + indirect CIs + nesting + disclosure? [Y/N]
【Next】await decision → joap-rebuttal on R&R
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — copy-paste pre-submission preflight checklist
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories, DOIs, `papaja`, SEM/HLM/meta tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official APA Journal of Applied Psychology URLs behind every fact in this pack
