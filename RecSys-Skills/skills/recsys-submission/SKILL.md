---
name: recsys-submission
description: Use when auditing an ACM RecSys submission before the deadline — routing between the Main, Reproducibility, Industry and Resource tracks, the ACM two-column content-page budgets with appendices counted inside, double-blind anonymization for recommender papers, the anonymous-repository expectation, and desk-reject triage.
---

# RecSys Submission

Run this audit before anything is uploaded to the RecSys submission system. RecSys is a
single-community but multi-track venue: the same manuscript can be legal in one track and
desk-rejectable in another, so the audit begins with "which track is this PDF for?" and only
then checks format. Reopen the current edition's Call for Contributions — every number below
is a 2026-cycle anchor (verified 2026-07-09), not a permanent rule.

## Pick the track before the format

For 2026 RecSys reorganized its lineup: it **dropped the Late-Breaking Results (LBR)** poster
track and added **Research & Practice (R&P) Notes**. Route the contribution first.

| Track | 2026 budget | What belongs here |
|---|---|---|
| Main - long paper | 8 content pages | A rounded recommendation contribution with offline (and ideally online) evidence |
| Main - short paper | 4 content pages | One focused, complete finding |
| Main - Past, Present & Future | 4 content pages | Reflective/forward-looking position on a recommendation topic |
| Reproducibility | see current CFP | Repeating, refuting, or re-scoping prior results; datasets/frameworks for future reproduction |
| Industry | see current CFP | Deployed systems, production constraints, live A/B evidence |
| Resource / Dataset | see current CFP | A community dataset or software resource with build methodology |
| R&P Notes (posters) | see current CFP | Short findings/experiences; replaces LBR for 2026 |

References are **excluded** from the page count; **appendices count inside** it. Use the ACM
two-column template unmodified — no margin, font, or spacing surgery.

## Anonymization for recommender papers specifically

Generic double-blind advice misses the leaks recommender papers actually carry:

- **Proprietary logs and platform.** "Interaction logs from our video platform in region X"
  can name the company. Keep the statistics, genericize the source.
- **Deployed system names.** If the ranker already runs in production under a public name, the
  name de-anonymizes; rename for review or argue from the current policy on preprints.
- **The anonymous repository.** RecSys expects a code/data link **inside the paper** rather than
  a supplement upload — mirror it to an anonymized host and strip the owner, commit authors, and
  cluster paths from history.
- **Self-citations** in third person; **acknowledgements and funding** removed; **PDF metadata**
  stripped.

## Blocking risks

- Wrong track for the contribution (a deployed-system paper squeezed into a Main long paper, or
  a reproduction study submitted as a novel-method paper).
- Over budget once appendices are counted inside the limit.
- Identity leak via logs, platform, deployed system name, or repository owner.
- Untuned baselines or a random split on sequential data — not a format desk reject, but the
  fastest route to a low score (see `recsys-experiments`).
- Parallel submission of the same work to another venue.

## Desk-reject and triage table

| Trigger | Severity at RecSys | Repair window |
|---|---|---|
| Over budget (appendix counted in) | Desk reject | None after the deadline |
| Template tampering | Desk reject or chair flag | None |
| Identity leak in PDF, logs, or repository | Desk reject | None |
| Wrong track's submission form | Desk reject or forced move | Usually none |
| Parallel/dual submission | Desk reject at any time | None |
| Baselines untuned; random split on session data | Review-stage damage | Only before the deadline |

## Final-week sequence for an offline-evaluation paper

1. Freeze the split: regenerate every ranking table from the versioned dataset and a **temporal**
   split so the PDF and the anonymous repository agree.
2. Re-run baseline tuning last under an **equal budget**; a stale, under-tuned baseline is the
   classic reviewer catch when the numbers move.
3. Compress into the content-page budget by demoting per-dataset analyses to the appendix or
   repository, never by shrinking floats.
4. Anonymity sweep: PDF metadata, acknowledgements, log provenance, deployed-system name,
   repository owner.
5. Confirm the submission-form abstract matches the PDF abstract and the track is correct.

```bash
# Pre-upload checks that catch the silent killers
pdfinfo paper.pdf | grep -iE "author|creator"                 # metadata identity leak
grep -inE "acknowledg|our (platform|service|company)" *.tex   # textual / platform leaks
pdftotext paper.pdf - | grep -icE "tuned|grid search|equal budget"  # baseline tuning stated?
pdftotext paper.pdf - | grep -icE "temporal split|leave-one-last"   # leakage-aware split?
```

## Format anchors

- RecSys uses the ACM **two-column** proceedings template; dense ranking tables and multi-panel
  offline/online figures overflow columns fast, so compress early rather than on deadline night.
- The page counts above describe the 2026 cycle; treat every number as provisional and recheck
  the current Call for Contributions before relying on it.

## Output format

```text
[RecSys readiness] Ready / Needs fixes / Wrong track / Not ready
[Track] main-long / main-short / past-present-future / reproducibility / industry / resource / R&P-note
[Budget check] <pages used>/<budget>, appendix-inside-budget confirmed yes-no
[Anonymity risks] <logs / platform / deployed name / repository owner / metadata>
[Evidence risk] <baseline tuning / split leakage / offline-only claim>
[Fix order] <ordered blocking fixes>
```
