---
name: hlr-submission
description: Use when running the final pre-submission preflight for the Harvard Law Review (HLR) via HLR's own electronic submission system — manuscript readiness, anonymization, length limits, Bluebook 22nd-edition footnotes, expedite setup, and season timing. Final upload checks; it does not plan the placement strategy (hlr-placement-strategy) or draft content.
---

# Submission Preflight (hlr-submission)

The last check before uploading through **HLR's own electronic submission system**
(harvardlawreview.org). HLR does **not** intake through Scholastica — Scholastica/ExpressO are the
*general-market* platforms you use to multi-submit and expedite at **peer** journals
(see `hlr-placement-strategy`); HLR itself takes the manuscript on its own portal. Unlike a
peer-reviewed science journal, HLR receives a **near-final, fully footnoted** article — there is no
"revise the methods later." The most common avoidable failures are an over-length manuscript, an
incomplete footnote apparatus, skipped anonymization, and mistimed submission.

## When to trigger

- "Submitting this week" — last pass before upload
- Unsure what HLR's submission system expects in the package
- Confirming the manuscript is genuinely near-final, anonymized, and pull-ready

## Process facts (live-check only the items marked 待核实)

- **Owner / publisher:** the **Harvard Law Review Association** — an independent, student-run
  organization (editorially independent of Harvard Law School).
- **Portal:** HLR's **own electronic submission system** (Microsoft **Word** documents encouraged;
  mailing the Articles Office is a fallback). Not Scholastica. (检索于 2026-06；以官网为准 for any
  additional channel.)
- **Review model:** **student-edited**, reviewed **anonymously**; each piece is read by **≥ 3
  editors** and many proceed through an Articles Committee vote, a **preemption check**, a
  **faculty peer-review** stage, and a full-body vote. ("Student-edited" — but a faculty peer-review
  stage does exist; do not tell authors there is zero peer review.)
- **Length** (count **includes text, footnotes, and appendices**): Articles preferred **≤ 25,000
  words**; over **30,000** weighs against selection; unconditional acceptance over **37,500** is
  rare. Essays (Print/Forum) **12,000–17,500**; Forum Responses **8,000**; Commentaries **6,000**;
  Book Review proposals a few pages.
- **Anonymization (required):** keep name, affiliation, bio, and acknowledgments on a **separate
  cover page**; put the **title on the first text page**; **anonymize self-citations**.
- **Citations:** **The Bluebook, 22nd edition** (HLR co-compiles it) — footnoted, pincited,
  signal-correct.
- **Expedite:** request via the unique link in your confirmation email; HLR honors requests where
  it can but **does not omit review stages**; a **≥ 7-day** offer-decision window is committed.
- **What HLR publishes:** **Articles, Essays, Book Reviews** by outside authors; **Notes** and case/
  legislation comments by **student editors** (student writing is unsigned); the annual **Supreme
  Court issue** (November) with the **Foreword**, and a **Developments in the Law** issue (April).
- **Leadership / no fee:** HLR is led by an **annually-elected student President** (the law-review
  analogue of an editor-in-chief) — **Volume 139 (2025–2026)** is led by **G. Terrell Seabrooks ('26)**;
  the masthead **rotates ANNUALLY each volume** (Volume 140's President, Alex Zhao, was elected Feb 2026),
  so **re-check the current masthead** before naming anyone (verified 2026-06-22). Article selection is by
  **student editors**, and HLR charges **no submission fee / no APC** — Scholastica/ExpressO fees, if any,
  belong to the *peer-journal* market, not HLR's own portal.
- **Season:** submit in the **Feb-Mar** main window or the smaller **Aug** window; earlier is
  stronger. Current intake **volume/season status**: 待核实 on the live page.

## Preflight checklist

### Manuscript readiness
- [ ] Genuinely near-final — argument complete, not a draft to finish in editing
- [ ] **Length within limits**: Article ≤ 25k (over 30k weighs against; over 37.5k rarely accepted),
      counting footnotes and appendices — cut before submitting if over
- [ ] Introduction front-loads the claim and contribution (see `hlr-writing-style`)
- [ ] Doctrine → theory → prescription arc intact (see `hlr-argument-structure`)

### Anonymization & footnotes (the make-or-break)
- [ ] **Anonymized**: separate cover page; title on first text page; self-citations neutralized
- [ ] Every proposition pincited to the strongest authority (see `hlr-sources-and-bluebook`)
- [ ] **Bluebook 22nd-edition** formatting, signals, and short forms consistent
- [ ] Every source kept and **pull-ready** for the source-pull (see `hlr-footnotes-and-cite-check`)
- [ ] Originality confirmed and re-checked near submission (see `hlr-preemption-check`)

### Package & metadata (HLR submission system)
- [ ] Word manuscript (with footnotes) prepared; abstract written
- [ ] **Anonymized cover page** separate from the manuscript body
- [ ] CV / author info ready as the portal requires
- [ ] Submission set tiered and timed (see `hlr-placement-strategy`)
- [ ] Expedite mechanics understood (only with an offer in hand)

### Timing & compliance
- [ ] Submitting early in a season, not mid-window into a crowded topic
- [ ] If you prefer HLR, submit it **≥ 2 weeks before** sending to other journals
- [ ] Original, unpublished work; no overlapping commitment
- [ ] Current intake volume/season status confirmed on the live page (待核实) — note HLR charges
      **no submission fee / no APC**; re-check the current masthead (student President rotates annually)

## Anti-patterns

- Submitting "through Scholastica" — that is the peer-journal market platform; **HLR uses its own
  system**
- An over-length manuscript (over 30k weighs against; over 37.5k rarely accepted) — and forgetting
  footnotes count toward the limit
- Skipping anonymization (cover page / self-citations) on an anonymously-reviewed submission
- Uploading a draft you "plan to finish in editing" — HLR expects near-final
- An incomplete or inconsistent footnote apparatus (it will not survive the source-pull)
- Single-submitting and forgoing expedite leverage (see `hlr-placement-strategy`)

## Output format

```
【Portal】HLR's own electronic submission system (NOT Scholastica)
【Length】word count incl. footnotes vs ≤25k / 30k / 37.5k thresholds — within? [Y/N]
【Anonymized】cover page + self-citations neutralized? [Y/N]
【Footnotes】pincited, Bluebook 22nd, pull-ready? [Y/N]
【Originality】preemption re-checked near submission? [Y/N]
【Timing】early in Feb-Mar / Aug season; ≥2 wks before other journals if HLR-first? [Y/N]
【Next】await offers → hlr-placement-strategy (expedite) → hlr-student-editor-review (on acceptance)
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — printable pre-submission checklist
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official HLR submissions facts with 待核实 markers
