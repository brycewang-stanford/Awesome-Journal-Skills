---
name: ecai-camera-ready
description: Use when preparing the ECAI camera-ready — de-anonymizing, fitting the final version into the page budget, and meeting the publisher's production requirements, which differ by regime: IOS Press FAIA (ecai.cls, open-access book volume, copyright/consent-to-publish forms) for a standalone ECAI, versus IJCAI's own open-access proceedings (ijcai.sty) for the joint IJCAI-ECAI 2026.
---

# ECAI Camera-Ready

The camera-ready turns an accepted paper into an archival, open-access publication. **The single
biggest decision is which publisher regime the edition is in**, because it sets the template, the
metadata, and the forms:

- **Standalone ECAI** → published in **IOS Press FAIA** (Frontiers in Artificial Intelligence and
  Applications), an **open-access book series**. Template **`ecai.cls`**; a **consent-to-publish /
  copyright form** to IOS Press; the paper becomes a numbered chapter in a FAIA volume
  (ECAI 2024 = Vol. 392).
- **IJCAI-ECAI 2026** → published in **IJCAI's own open-access, online-only proceedings**.
  Template **`ijcai.sty`**; IJCAI's license/consent process; the paper indexes under the IJCAI
  proceedings, not FAIA, this cycle.

Confirm the regime, the exact production instructions, and every deadline on the current author kit
before starting — the details below are a 2026-07-09 snapshot.

## De-anonymize systematically

The reviewed PDF was double-blind; the camera-ready is not. Reverse every anonymization:

- Restore **author names, affiliations, and ORCIDs** in the template's author block.
- Restore **acknowledgements and funding** statements (removed for review).
- Convert anonymized "prior work [X]" back to proper self-citations.
- Replace anonymized supplement/repository links with the **permanent** ones.

```bash
# Catch leftover anonymization scaffolding
grep -nEi 'anonymous|anonymi|blinded|redacted|\[REDACTED\]|XX+|placeholder' paper.tex | head
grep -nEi 'our prior work \[|removed for (review|blind)' paper.tex | head
```

## Fit the final version into the page budget

Camera-ready is **not** a chance to expand: the body stays at **7 pages** (references overflow only:
1 page standalone, 2 pages in IJCAI-ECAI 2026). Adding author blocks and acknowledgements can push
you over — recover space editorially, not by shrinking the font or margins (the template forbids it
and production will reject it).

- Fold rebuttal-promised clarifications in *minimally* (an assumption list, one surfaced number) —
  camera-ready edits are minor, not a new version.
- Move any overflow to the **supplement**, not the reference pages.

## Template and production checks

**FAIA / `ecai.cls` (standalone):**
- Use the exact `ecai.cls` and the FAIA metadata macros; do not restyle headings or bibliography.
- Embed and subset all fonts (Type 1 / TrueType), no Type 3 fonts; figures at print resolution.
- Provide the paper title, authors, and abstract exactly as they must appear in the IOS Press
  volume front matter and the DOI record.
- Submit the **consent-to-publish / copyright transfer** form IOS Press requires; the volume is
  open access, but the form is still mandatory.

**IJCAI / `ijcai.sty` (IJCAI-ECAI 2026):**
- Use the current `ijcai.sty`; keep the ethics statement placement (body or reference pages) as
  submitted, updated only minimally.
- Follow IJCAI's PDF/font requirements and the license/consent step in its author kit.
- Metadata (title/authors/abstract) must match what is entered in the submission system for the
  proceedings index.

```bash
# PDF production sanity (both regimes)
pdffonts paper.pdf | grep -i 'Type 3' && echo "FAIL: Type 3 fonts present"
pdfinfo paper.pdf | grep -Ei 'page size|pages'   # confirm A4/Letter per the kit and page count
```

## Open-access specifics

- ECAI proceedings are **open access with no article-processing charge**; the cost model is
  registration and at least one author presenting. Do not expect (or pay) an APC.
- Because the paper is openly readable on publication, the **permanent** links you place (dataset,
  code, proofs) are the version the whole community will use — pin them now
  (`ecai-reproducibility`).
- Register/confirm the **DOI** (FAIA chapters carry DOIs; IJCAI proceedings entries have stable
  URLs). Use the canonical citation string the publisher issues.

## Registration and presentation gate

At least one author must **register** and **present** for the paper to appear. Missing this can
pull an accepted paper from the proceedings — verify the registration deadline and the
presentation format (talk/poster) on the current program page.

## Final checklist

```text
[Regime] FAIA/ecai.cls (standalone) or IJCAI/ijcai.sty (IJCAI-ECAI 2026) confirmed
[De-anonymize] authors, affiliations, ORCIDs, acknowledgements, funding, self-cites, links restored
[Budget] body still 7 pages; overflow in supplement, not reference pages
[Template] correct .cls/.sty; no margin/font tampering; fonts embedded, no Type 3
[Forms] IOS Press consent-to-publish OR IJCAI license/consent submitted
[Metadata] title/authors/abstract match the volume/proceedings record; DOI/citation confirmed
[Presentation] a registered author committed to present by the deadline
```

## Reverify each cycle

- The publisher/template regime (FAIA vs IJCAI proceedings) and its exact production instructions.
- Page size (A4/Letter), font rules, and the copyright/consent form and deadline.
- Whether the ethics statement, supplement, or any AI-disclosure note must be finalized here.
