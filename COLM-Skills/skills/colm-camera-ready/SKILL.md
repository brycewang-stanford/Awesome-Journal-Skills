---
name: colm-camera-ready
description: Use when converting a COLM acceptance into the final paper — the August 7 camera-ready deadline in 2026, de-anonymization and the one-page acknowledgments allowance, folding rebuttal commitments into the text, publishing on OpenReview, releasing artifacts publicly, and planning the October conference in San Francisco.
---

# COLM Camera-Ready

Decisions for COLM 2026 landed July 8 and camera-ready is due August 7 — a
one-month window. COLM publishes its papers openly on OpenReview rather than through
an external proceedings publisher, which makes the camera-ready unusually final:
what you upload is the public record, discoverable within days, forever attached to
your OpenReview forum with its reviews.

## The one-month plan

| Week (2026 dates) | Work |
|---|---|
| Jul 8-14 | Read the meta-review and decision notes; list every commitment made in rebuttal; decide which promised changes are in-scope for camera-ready |
| Jul 15-24 | Execute the text changes; de-anonymize; build the public artifact release in parallel (`colm-artifact-evaluation`) |
| Jul 25-31 | Full-paper cold read by a co-author who did not edit it; verify every link resolves to the *public*, de-anonymized artifact |
| Aug 1-7 | Format check on the final COLM template, metadata check, upload with days to spare |

## De-anonymization, done in both directions

Adding identity back is the easy half. The camera-ready pass must also *reverse*
every anonymization workaround the submission introduced:

- Restore author names, affiliations, and correspondence.
- Add acknowledgments — under the 2026 format an optional acknowledgments section
  of at most one page sits outside the 9-page limit. Fund-source and
  compute-donor acknowledgments live here; check funder-mandated wording.
- Swap anonymized repository links for the real, tagged public repo; replace
  anonymized model-hub IDs with your org's actual IDs.
- Un-contort self-citations: "the dataset of [7]" can become "our earlier dataset
  [7]" where that is clearer.
- Then sweep for stragglers — a leftover "anonymous.4open.science" link in the
  published PDF is the classic COLM-camera-ready fossil.

```bash
# Fossil hunt on the final PDF before upload
pdftotext camera-ready.pdf - | grep -niE 'anonym|blinded|redacted|placeholder|TODO|XXX' | head
pdftotext camera-ready.pdf - | grep -noE 'https?://[^ ]+' | sort -u   # every link: click each one
```

## Honoring the rebuttal ledger

Reviewers and the AC accepted a paper that includes what you promised in the
May-June discussion. Fold in: rescoped claims exactly as conceded, the R1/R2/...
tables or their summaries, corrected version strings and query dates, and the
limitations you agreed to add. Silently dropping a rebuttal commitment is visible —
the whole discussion sits on the same OpenReview page as your final PDF.

Also re-check facts that aged during review: an API model you evaluated in March
may have been deprecated by August. Do not re-run and overwrite (the paper reports
the March measurements); *do* update the availability language so readers know what
is still queryable (`colm-reproducibility`).

## Metadata and the public record

- Title, author order, and abstract in the OpenReview form must match the PDF
  exactly — this metadata is what indexers and citation managers scrape.
- The LLM-usage disclosure travels with the paper; if camera-ready edits changed
  what should be disclosed, update it.
- 待核实 items this cycle (verify on the current author guide before upload):
  whether camera-ready grants extra content pages beyond 9, the exact license
  terms of the OpenReview publication, and any required funding/COI statement
  format. None was verifiable on 2026-07-08.

## Artifact release and the arXiv decision

Ship the public artifacts in the same pass as the PDF: tagged code release, weights
and datasets with cards, the cached-outputs archive if ToS permits, and the paper's
OpenReview URL embedded in each artifact's documentation. If you also post to
arXiv, note that the OpenReview version is the version of record and keep the two
synchronized — a drifting arXiv copy generates years of confused citations.

## The forum is part of the publication

Because COLM publishes on OpenReview, your paper's public page carries the entire
review history: scores, rebuttal, AC notes. Readers *will* scroll down. Three
consequences worth acting on during camera-ready week:

- **The rebuttal is now documentation.** Numbers and clarifications that exist
  only in the discussion thread get cited by careful readers; make sure everything
  load-bearing from the thread made it into the PDF so the paper does not depend
  on its own comment section.
- **Discrepancies are visible.** If the discussion says "we will rescope claim X"
  and the final PDF still makes claim X, anyone can see it. The rebuttal ledger
  audit above is not optional politeness; it is public-record consistency.
- **The forum stays live.** Post-publication questions sometimes arrive as
  comments. Decide who on the author team watches the forum through the October
  conference and answers with the same care as the rebuttal.

## October logistics

COLM 2026 runs October 6-9 at the Hilton Union Square, San Francisco (main
conference October 6-8, workshop day October 9). Presentation format assignments,
registration requirements for accepted papers, poster specs, and any remote-
participation option were not verifiable at pack-build time — all 待核实 via the
conference's announcements before booking. What is safely plannable now: at least
one author available in San Francisco that week, a poster-design slot in late
September, and visa timelines for authors who need them, which in a July-to-October
gap are the item most often fumbled.

## Common fossils, ranked by embarrassment

From most to least visible in published COLM-style PDFs: an "Anonymous Authors"
block surviving into the final version; anonymized-repo links next to the real
ones; "we thank the anonymous reviewers" *without* the funding acknowledgments the
grant requires; rebuttal-era "R1/R2" table labels leaking into the final text;
appendix cross-references broken by post-acceptance renumbering; and an abstract
in the OpenReview form that still matches the March submission instead of the
August PDF. Each is a two-minute check; the full sweep is under an hour and is the
last hour that matters.

## Output format

```text
[Countdown] days to camera-ready: <n>
[Rebuttal ledger] commitments folded in: <k>/<total> — outstanding: <items>
[De-anon sweep] identity restored ▢  workarounds reversed ▢  fossils: <hits>
[Links] all resolve to public artifacts ▢
[待核实 checked live] extra-pages? license? attendance rules?
[October] presenter ▢  visa ▢  poster slot ▢
```
