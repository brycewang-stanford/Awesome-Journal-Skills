# Validation set — `ahr-submission`

Held-out researcher queries (the skill text does not contain these) plus the
verified ground-truth fact sheet the judge scores against. Ground truth is drawn
from `American-Historical-Review-Skills/resources/official-source-map.md`
(OUP Author Guidelines, accessed 2026-06).

## Held-out queries

**Q1 (review process + timeline).**
> "I'm about to submit to the AHR. How many reviewers will see my article, what
> share of submissions actually get sent out for review, and how long until I get
> a decision?"

**Q2 (odds + fees).**
> "What are my realistic chances of acceptance at the AHR, and is there any
> submission or publication fee?"

**Q3 (notes budget + citation style).**
> "My article runs about 7,500 words of text. Roughly how many words of notes is
> normal for the AHR, and what citation style do they require?"

## Ground-truth fact sheet

- **Reviewers / filter.** Every article published in the AHR has been reviewed by
  **at least six scholars**; roughly **a quarter** of submissions are sent out for
  full review. → Q1.
- **Decision timeline.** Targeted within about **six to eight months**. → Q1.
- **Acceptance.** The AHR publishes roughly **8–10% of the ~360 manuscripts** it
  receives per year. → Q2.
- **Fees.** **No author processing fees**; a **50% discount on up to 10 print
  copies**. → Q2.
- **Length / notes.** Ideally **≤ 8,000 words of text** excluding notes, tables,
  charts; **2:1 text-to-notes** guideline; a typical 8,000-word article carries
  **4,500–5,500 words of notes** — so ~7,500 words of text normally carries on the
  order of **~4,200–5,200 words of notes**, materially more than a naive "half the
  text ≈ 3,750". → Q3. (The baseline skill produced the naive 3,750 figure; the
  judge flags it as a wrong fact.)
- **Citations.** Chicago Manual of Style notes (foot/endnotes); **no bibliography**,
  **no in-text parenthetical**. → Q3.
- **Portal.** ScholarOne / Manuscript Central (`mc.manuscriptcentral.com/ahrev`),
  Microsoft Word; email submissions not accepted. Double-blind / anonymous.

## Volatile — defer to a live check (rubric §5)

- Current **editor** name and term (secondary sources: Mark Philip Bradley — 需复核).
- Exact **CMOS edition** and any AHR house departures.
- Whether a separate **abstract** is required at submission.
- Any optional **OA/APC** option via OUP after acceptance.
