---
name: sigmod-supplementary
description: Use when deciding what accompanies a SIGMOD submission beyond the 12 pages, covering extended technical reports, anonymized code and data links that survive multi-round review, appendix placement relative to the unlimited reference pages, and what reviewers actually open during a PACMMOD round.
---

# SIGMOD Supplementary

SIGMOD's supplementary question is shaped by two venue facts: the body is
capped at 12 pages with unlimited pages **only for references**, and the
review cycle — including a possible revision — runs for months under
double-anonymity. Everything that supports the paper from outside the PDF
must therefore stay anonymous far longer than at one-shot conferences, and
whether appendices may ride inside the PDF varies by cycle: check the current
CFP and CMT form rather than assuming.

## The three vehicles

| Vehicle | Carries | Multi-round hazard |
|---|---|---|
| In-PDF appendix (if the cycle allows) | Proofs, extra plots, tuning grids | Counting against the 12 pages by mistake |
| Anonymized extended report | Full proofs, complete evaluation | Hosting that expires or exposes authors mid-round |
| Anonymized code/data link | Implementation, workloads, scripts | Repo activity revealing identity during revision |

Decide per item, not wholesale. The default discipline: the 12 pages carry
every decision-critical argument; vehicles outside the PDF carry
verification depth, never the contribution itself.

## Anonymous hosting that survives a round

- Use a purpose-made anonymous mirror (fresh account or an anonymization
  service), not a scrubbed view of the real lab repository.
- Freeze it: pushes during the review window leak timezones, usernames in
  commit metadata, and CI badges. Snapshot once, before the deadline.
- Test from a logged-out browser and a second network; institutional
  single-sign-on redirects have unmasked authors before.
- Plan for the revision: if reviewers demand new experiments, you will need
  a *second* frozen snapshot — name the first one `v1` from the start.
- Remember late withdrawal counts as rejection; do not host anything you
  would have to take down in a hurry mid-round.

## What a database reviewer opens, in order

1. The PDF itself — if the 12 pages cannot stand alone, nothing else is
   read charitably.
2. The extended report, when a proof or algorithm detail is contested;
   mirror the paper's theorem and section numbering exactly so lookup takes
   seconds.
3. The code link, most often to check whether a suspicious number has a
   plausible harness behind it — a README naming which script produces
   which figure answers this without a checkout.
4. Raw logs or datasets, rarely; include them for the ARI future, not for
   review-time persuasion.

## Extended-report etiquette

- Give the report the same title with "(Extended Version)" and keep it
  anonymous during review — an arXiv posting under real names that the
  paper links to is an anonymity breach, not a supplement.
- Do not fork content: the report is a superset of the paper, never a
  different-numbers sibling. Divergent figures between the two versions is
  a credibility wound reviewers do report.
- If the report is cited in the submission, cite it anonymously ("Full
  proofs appear in the anonymous technical report [URL]").

## Splitting a systems paper across vehicles

Worked split for a fictional adaptive-indexing engine submission: the body
keeps the architecture, the two headline comparisons, the correctness
argument sketch, and one ablation that carries the mechanism claim. The
extended report absorbs the remaining ablations, the full proof of the
maintenance-cost bound, and per-query latency tables. The anonymous
repository holds the engine, workload generators with seeds, and per-figure
run scripts. Each vehicle references the others by stable anonymous URL, and
nothing in the report contradicts a number in the body.

```text
Body (12pp):   claim spine + headline evidence + mechanism ablation
Report:        proof detail + secondary ablations + full latency tables
Repo snapshot: engine v1 tag + generators + fig-to-script map
```

## Size and format practicalities

- Keep any uploaded archive lean: source, scripts, configs, and small
  sample data — not the 200 GB dataset, which belongs behind a fetch
  script with checksums and a stated size.
- Prefer plain tar/zip over exotic formats; a reviewer who cannot open the
  archive in ten seconds will not try twice.
- Put a one-screen INDEX file at the archive root mapping contents to paper
  sections; reviewers grant minutes, not hours.
- Whatever CMT's current size ceiling is, verify it on the live form —
  upload limits are among the least stable venue parameters.

## Pre-upload sweep

- Grep the archive for names, employers, cluster hostnames, cloud account
  IDs, and internal ticket references.
- Strip notebook execution metadata and PDF producer fields.
- Verify every URL in the PDF resolves to the anonymous mirror, not the
  canonical repo you will publish at camera-ready.

## Output format

```text
[Vehicle map] item -> body / report / repo, with rationale
[Standalone test] does the 12-page body carry the claim spine alone
[Hosting audit] anonymity, freeze status, logged-out access verified
[Numbering mirror] report matches paper theorem/section numbers yes/no
[Sweep findings] identity artifacts found and removed
[Revision reserve] plan for a v2 snapshot if a revision verdict lands
```
