---
name: mksc-submission
description: Use when preparing to submit a Marketing Science manuscript through ScholarOne — blinding for double-anonymous review, choosing the track (regular / Frontiers / Database / Practice), assembling the replication package, the cover letter, preferred AEs/reviewers, and the optional Open Option. Preflight only; it does not interpret decisions (mksc-review-process).
---

# Submission Preflight (mksc-submission)

## When to trigger

- The manuscript is finished and you are ready to submit
- You are unsure which track fits or what files ScholarOne expects
- You need to blind the manuscript and assemble the replication materials
- You are weighing the Open Option (gold OA)

## Submission system and blinding

- Submit through **ScholarOne Manuscripts at mc.manuscriptcentral.com/mksc**.
- Regular submissions use **double-anonymous review**: remove author names, institutions, and acknowledgments from the manuscript; phrase self-citations in the third person.
- The **cover letter is visible to the Editor and AE but not reviewers** — use it for context, prior-review history, and self-overlap disclosure, while keeping the manuscript itself blinded.

## Choose the right track

- **Regular (Original Article)** — authors "should strive to keep their manuscripts to 40 double-spaced pages, including all references, tables, graphs, and appendices"; online appendices do not count and can be any length; shorter is welcome.
- **Frontiers in Marketing Science** — Science-like, faster review, **strict 6,000-word total cap** (including references, tables, graphs, appendices); requires a major contribution on one primary dimension.
- **Database** — built around a novel dataset.
- **Practice Paper / Practice Prize** — requires a **500–1,000-word Impact Statement** and uses a **single-blind** process; Science-to-Practice is a related track.

## Format and front matter

- Double-spaced, single column, 11- or 12-point font, one-inch margins; Word or LaTeX (INFORMS style files), uploaded as Word or PDF.
- Abstract **≤ 200 words** on the first page (the format paragraph says "approximately 100-200 words"); text-only, no math notation; **3–6 keywords** beneath the abstract (theoretical and methodological orientation).
- INFORMS author-year citations; alphabetical reference list.
- You may suggest **2 preferred Associate Editors and 3 preferred reviewers**.
- Disclose any self-overlap with your published or under-review work and how this paper goes beyond it.
- Note any **nondisclosure agreement** covering your data in the cover letter at submission (it shapes what the replication package can contain); funding is entered in the Details & Comments step, where you also pick a preferred Senior Editor.
- **Generative AI** may be used, but authors are responsible for every fact and reference; fabricated ("hallucinated") references can be grounds for rejection on their own.

## Replication package

Although the deposit is required **on acceptance** (Replication and Disclosure Policy), assemble it now: estimation code and a master script that reproduces every table/figure/counterfactual; for licensed data (NielsenIQ, Compustat, CRSP, Census), access instructions and linking/build code rather than raw data.

## Fees / Open Option

No mandatory submission or publication fee for standard subscription publication. **Open Option** (gold OA) is optional: a one-time **US$3,000** fee charged only after acceptance, before publication; it does not affect peer review.

## Checklist

- [ ] Manuscript blinded (names, affiliations, acknowledgments, self-citations)
- [ ] Track chosen; regular paper ≤ ~40 double-spaced pages incl. references/tables/appendices (online appendix excluded); Frontiers within 6,000-word total cap; Practice has Impact Statement
- [ ] Abstract ≤ 200 words; 3–6 keywords; INFORMS author-year + alphabetical refs
- [ ] Format: double-spaced 11–12 pt, one-inch margins; Word/LaTeX → Word/PDF
- [ ] Cover letter (Editor/AE-only) with self-overlap disclosure
- [ ] 2 preferred AEs and 3 preferred reviewers suggested
- [ ] Replication package assembled (code + licensed-data access/build)
- [ ] Open Option decision noted (US$3,000, post-acceptance, optional)

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue mksc-skills   # from a clone of the AJS repository
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

- Leaving author identifiers or "our prior paper" phrasing in a double-anonymous manuscript.
- Submitting an over-length Frontiers paper.
- Treating replication as an afterthought; "code on request."
- Confusing the single-blind Practice track rules with regular double-anonymous submission.

## Replication package layout (assemble before you submit)

The deposit is required on acceptance, but reviewers increasingly probe reproducibility during review. Build the package now so the master script already reproduces every exhibit:

```text
mksc-replication/
├── README.md              # data provenance, software + versions, run order, expected runtime
├── run_all.{R,py,do}      # master script: raw → estimates → every table/figure/counterfactual
├── data/
│   ├── build/             # linking + cleaning code (NOT licensed raw data)
│   └── access.md          # how to obtain NielsenIQ / Compustat / CRSP / Census + license notes
├── estimation/            # model estimation code, starting values, solver settings
├── counterfactuals/       # policy simulations that re-solve firm optimization
└── output/
    ├── tables/            # table_1.tex ... mapped 1:1 to the manuscript
    └── figures/           # fig_1.pdf ... regenerated by run_all
```

Map each output file to its manuscript exhibit by name; a reviewer or the AE should reproduce Table 3 without emailing you. For licensed data, ship build/linking code and access instructions, never the raw proprietary extract.

## Output format

```
【Track】regular / Frontiers / Database / Practice
【Blinding】manuscript anonymized? self-cites third-person?
【Front matter】abstract ≤200w; 3–6 keywords; INFORMS format
【Handlers】2 preferred AEs + 3 reviewers; cover letter (Editor/AE-only)
【Replication】code + data access/build ready
【Fees】subscription (none) / Open Option US$3,000
【Next step】mksc-review-process
```
