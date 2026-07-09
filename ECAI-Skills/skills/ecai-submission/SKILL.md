---
name: ecai-submission
description: Use when auditing an ECAI submission for readiness — the abstract-then-full-paper two-deadline flow, the tight 7-page body budget, double-blind anonymity, the correct template/publisher regime (ecai.cls/FAIA for a standalone ECAI vs ijcai.sty/IJCAI proceedings for the joint IJCAI-ECAI 2026), the per-author submission cap, the ethics statement, and desk-reject triage before the AoE cutoff.
---

# ECAI Submission

Run this audit before uploading to the ECAI submission site. **First settle which regime the target
edition is in**, because it changes the template, the publisher, and the page budget:

- **A standalone ECAI** (e.g. ECAI 2023/2024) publishes in **IOS Press FAIA** (Frontiers in
  Artificial Intelligence and Applications), uses the **`ecai.cls`** template, and allows
  **7 pages of body + 1 page of references**.
- **ECAI 2026 is the joint IJCAI-ECAI 2026** (Bremen, 15-21 Aug 2026). It follows **IJCAI**:
  the **`ijcai.sty`** template, **7 pages body + 2 pages references** plus an optional ethics
  statement, and **IJCAI's own open-access proceedings** — not FAIA this cycle.

Every number below was read from the IJCAI-ECAI 2026 and ECAI 2024 calls on 2026-07-09 via search
renderings (see `resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen
the live call first.

## The two-deadline flow

ECAI separates an **abstract/registration** deadline from the **paper** deadline, and both are AoE:

- **Abstract** locks in title, abstract text, authors, and topics about a week early
  (IJCAI-ECAI 2026: **12 January 2026**; ECAI 2024: registration **19 April 2024**). Miss it and
  the system will not accept the PDF later.
- **Paper** uploads the anonymized PDF (IJCAI-ECAI 2026: **19 January 2026**; ECAI 2024:
  **25 April 2024**).

Register with the *real* title and abstract (plain text, ~100-300 words), not a placeholder — the
abstract drives reviewer bidding and area-chair assignment, and a registered abstract that diverges
from the final paper quietly worsens your match.

## Format and page budget

- **Template:** `ijcai.sty` for IJCAI-ECAI 2026; `ecai.cls` for a standalone ECAI. This is **not**
  the ACM `acmart` path, **not** IEEE `IEEEtran`, and **not** LNCS — do not carry a sibling-venue
  habit over.
- **Page budget (verify per cycle):** **7 pages of body** for all text and figures. References
  are the only overflow — **1 page** (standalone ECAI) or **2 pages** (IJCAI-ECAI 2026). There is
  no unlimited appendix inside the paper; anything a reviewer must read to judge the paper lives in
  the 7-page body.
- **Ethics statement (2026):** optional, may sit in the body or the reference pages; recommended
  for sensitive data or tasks.
- Margins, font, and spacing are fixed by the template; editorial compression, not template
  tampering, is how you recover space.

## Double-blind sweep

ECAI review is **double-blind**. Because AI papers lean on code, datasets, and named systems, the
leak surface is wide:

```bash
# Mechanical pass on the submission PDF and any anonymized supplement
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|gitlab|zenodo\.org/record|acknowledg|grant|funded by' | head
unzip -l supplement.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/' | head
grep -rni 'university\|@[a-z0-9.]*\.edu\|our (system|group|lab)' supplement/ --include='*.md' | head
```

The AI-specific leaks: a method named after your group, a dataset or benchmark you are known for,
an acknowledgements/funding line left in, a repository owner in a supplement, and self-citations
phrased as "in our prior work [X]" instead of neutrally. Anonymize the supplement archive before
upload.

## Per-author cap and topics

- **Submission cap:** IJCAI-ECAI 2026 limits each author to **no more than 8 submissions** to the
  main track (verify per cycle). Count every paper on which a person is an author across your group.
- **Topics/keywords:** select the areas that match your evidence so the paper routes to the right
  area chair and reviewer pool — the single largest lever you control before reviews.
- **Track choice:** a *deployed application* paper may belong in **PAIS** (standalone editions) or
  an applied special track rather than the main track — decide before the abstract deadline
  (`ecai-topic-selection`).

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Body over 7 pages | Desk-reject-grade | Cut or move to the supplement; reference pages do not absorb body text |
| Wrong template (`acmart`/`IEEEtran`/LNCS) or altered margins | Named desk-reject ground | Recompile in `ijcai.sty`/`ecai.cls`, recover space editorially |
| Identity leak in PDF, supplement, or method name | Anonymity violation | Re-anonymize and re-host; scrub PDF metadata |
| Abstract not registered by the earlier date | No submission slot exists | Nothing fixes this post-AoE — calendar it now |
| Author over the per-author submission cap | Submissions may be dropped | Prioritize and withdraw the weakest before the cutoff |
| Same work under review elsewhere | Dual-submission violation | Withdraw one venue; check the current concurrent-submission wording |

## Final-week order of operations

1. Freeze the 7-page body early; references can churn, the argument cannot.
2. Register title/abstract/authors/topics before the abstract cutoff.
3. Build the anonymized supplement (proofs, extra tables, code) and reference it from the body.
4. Run the mechanical double-blind checks on the *final* PDF and the *final* archive.
5. Confirm the template regime (`ijcai.sty` vs `ecai.cls`) and the exact page budget for THIS
   edition — do not assume 7+1 in a joint year.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- Whether the edition is standalone (FAIA/`ecai.cls`, 7+1, PAIS) or joint with IJCAI
  (IJCAI proceedings/`ijcai.sty`, 7+2) — this flips template, publisher, and budget.
- All dates and AoE cutoffs; the per-author submission cap; the ethics-statement and
  generative-AI policy wording.
- Supplementary-material rules and whether an appendix is allowed.

## Output format

```text
[ECAI submission status] ready / blocked / needs work
[Regime] standalone ECAI (FAIA/ecai.cls) / joint IJCAI-ECAI (IJCAI/ijcai.sty)
[Abstract step] title/abstract/authors/topics locked by the earlier deadline? yes/no
[Format] pages used (body/refs), template compliance
[Anonymity] clean / leaks: <where>
[Caps & tracks] within per-author cap? correct track (main/PAIS)?
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
