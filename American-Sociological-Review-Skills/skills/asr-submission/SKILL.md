---
name: asr-submission
description: Use when running the final pre-submission preflight for the American Sociological Review (ASR) via Sage Track — masked-manuscript preparation, the separate title page, word/abstract caps, ASA Style Guide formatting, the $25 processing fee, and ethics declarations. Final checks; it does not draft content.
---

# Submission Preflight (asr-submission)

The last check before submitting through **Sage Track** (ScholarOne Manuscript Central). ASR is
**masked**, so the most common avoidable failure is an under-anonymized manuscript or a missing
separate title page. Verify volatile specifics (fee, caps, editors) on the official page first.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure what files Sage Track expects (masked manuscript + title page)
- Confirming the caps are met, the manuscript is masked, and the fee is handled

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** American Sociological Association (ASA) / SAGE.
- **Portal:** **Sage Track** (ScholarOne Manuscript Central), `mc.manuscriptcentral.com/asr`.
- **Review model:** **masked (anonymous)** — anonymous manuscript **without a title page** + a
  **separate title page** (institutional affiliations, acknowledgments, word count, corresponding-
  author contact). You **may cite your own work** but not in identifying wording.
- **Scope / fit filter:** ASR evaluates **general-interest sociology** with strong research
  designs/methods, **broad sociological appeal**, and **theory development that transcends
  subfields** — a fit mismatch is a desk-reject risk before review.
- **Previously rejected:** ASR **does not consider papers previously rejected at ASR** — do not
  resubmit a rejected manuscript.
- **Length:** **Articles ≤ 15,000 words** including text, references, and footnotes (tables and
  figures excluded); **Comments/Replies ≤ 3,000 words** (uploaded directly in Sage Track).
- **Abstract:** **200 words or fewer** (the manuscript-prep section describes 150-200 words; use the
  stricter **200-word ceiling** for the check), no identifying information.
- **Format:** **double-spaced** text, notes, and references; **Times New Roman 12 pt, ≥1-inch
  margins**; **ASA Style Guide (7th ed., 2022)** with author-year in-text citations for references.
- **Fee:** **$25.00 non-refundable** manuscript processing fee via Sage Track, **waived for ASA
  student members** (verified 2026-06-22; re-check the amount before paying).

## Preflight checklist

### Type & length
- [ ] Article (≤ 15,000 words incl. text + references + footnotes) or Comment/Reply (≤ 3,000)
- [ ] Word count recorded on the **separate title page**
- [ ] Abstract ≤ 200 words (150-200 target), non-identifying
- [ ] Not previously rejected at ASR (rejected papers are not reconsidered)

### Masking (anonymous review)
- [ ] Manuscript has **no title page**, no author names/affiliations/acknowledgments
- [ ] Self-citations neutralized ("in a prior study," not "in our prior study")
- [ ] Identifying **file metadata stripped** (document properties)
- [ ] **Separate title page** prepared: affiliations, acknowledgments, word count, contact

### Format & files
- [ ] Double-spaced, Times New Roman 12 pt, ≥1-inch margins
- [ ] ASA Style Guide (7th ed., 2022) references; consistent author-date
- [ ] Tables/figures self-contained (see `asr-tables-figures`)

### Fee, ethics & data
- [ ] **$25 processing fee** ready (or ASA student-member waiver applies)
- [ ] Not under review at any other journal; prior appearances disclosed
- [ ] Data documentation prepared per the ASA data-sharing norm (see `asr-data-and-transparency`)

## Avoidable returns at the ASR desk

The ASA's flagship returns or delays papers most often for masking and length-accounting errors, not
for science — all within your control. Confirm any volatile figure against the current guidelines first.

| Trip-wire | Consequence | Fix before upload |
|-----------|-------------|-------------------|
| Title page in the manuscript | masking broken | strip it; use the separate title-page file |
| "in our prior study" wording | de-anonymizes the author | neutralize to "in a prior study" |
| References left out of word count | over the 15,000 cap on recount | count text + references + footnotes |
| Live document metadata | author name in file properties | clear properties before export |
| Resubmitting an ASR-rejected paper | not reconsidered | do not resubmit; ASR rejects are final |

## Worked micro-example (illustrative)

An author preps a quantitative inequality paper for Sage Track upload.

```
Body + references + footnotes: 14,920 words → under 15,000, OK
Abstract: 178 words, no institutions named → under the 200-word ceiling
Files: (1) masked manuscript, no title page; (2) separate title page with affiliations + word count
Masking sweep: 3 self-citations reworded; properties cleared; acknowledgments on title page only
Fee: $25 processing fee ready (verified 2026-06-22; ASA-student waiver applies)
```

Two files, caps verified on a recount including references, and a clean masking sweep — the most
common avoidable rejections pre-empted before upload.

## Editor pushback → ASR-specific fix

- *"Over length."* → Recount with references and footnotes; prune citation strings rather than cutting
  argument (hand to `asr-writing-style`).
- *"We could identify the authors."* → Re-run the masking sweep on wording, acknowledgments, and
  metadata; the separate title page is the only place identifiers belong.

## Calibration anchors

- **Masking is the highest-frequency failure.** At a masked flagship, an under-anonymized file is the
  most common avoidable cause of a return.
- **References are not free.** ASR's cap is unusual in counting the reference list — budget for it
  early.
- **Treat volatile specifics as provisional.** Fee, caps, and editor handling can change; verify
  live.

## Anti-patterns

- Leaving a title page or author identifiers in the manuscript (breaks masking)
- Forgetting the **separate title page** Sage Track expects
- Treating references as outside the word count — they count toward 15,000
- Abstract over the 200-word ceiling
- Resubmitting a paper ASR previously rejected (not reconsidered)
- Forgetting the $25 fee, or submitting elsewhere while under ASR review

## Output format

```
【Type】Article (≤15,000) / Comment-Reply (≤3,000) — cap met? [Y/N]
【Masked】no title page + self-refs neutralized + metadata clean? [Y/N]
【Separate title page】prepared? [Y/N]
【Abstract】word count (≤200), non-identifying?
【Format】double-spaced TNR 12pt + ASA Style Guide (7th ed., 2022)? [Y/N]
【Fee】$25 ready or ASA-student waiver? [Y/N]
【Next】await decision → asr-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, masking, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official ASR URLs behind every fact in this pack
