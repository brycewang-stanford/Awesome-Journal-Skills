# External Tools - ICSE

Access date: 2026-07-08

Open the current edition's pages before using any workflow below; every date,
page budget, and policy in this pack is a 2027-cycle snapshot, and ICSE has
recently changed even its cycle *count* between editions. If the live pages
and this pack disagree, the live pages win.

## Official workflow surfaces

- ICSE conference series index: https://www.icse-conferences.org/
- ICSE 2027 site: https://conf.researchr.org/home/icse-2027
- ICSE 2027 Research Track call: https://conf.researchr.org/track/icse-2027/icse-2027-research-track
- ICSE 2027 important dates: https://conf.researchr.org/dates/icse-2027
- ICSE 2027 research-track HotCRP: https://icse2027.hotcrp.com/
- ICSE 2027 NIER track: https://conf.researchr.org/track/icse-2027/icse-2027-new-ideas-and-emerging-results--nier-
- ICSE 2027 Journal-first track: https://conf.researchr.org/track/icse-2027/icse-2027-journal-first-papers
- ICSE 2027 Artifact Evaluation: https://conf.researchr.org/track/icse-2027/icse-2027-artifact-evaluation
- ACM artifact review and badging policy: https://www.acm.org/publications/policies/artifact-review-and-badging-current
- Archival indexes: https://dl.acm.org/ · https://ieeexplore.ieee.org/ · https://dblp.org/
- SIGSOFT award pages (MIP lineage): https://www.sigsoft.org/awards/icseMIPAward.html

## Author-side verification passes

Run these against the live pages, in order, before committing to a plan:

1. **Structure pass** — how many submission cycles this edition runs, and
   which decision categories exist; everything downstream depends on this.
2. **Calendar pass** — abstract (mandatory?) and paper deadlines with AoE
   conversion; response window; notification; revision and final-decision
   dates; artifact and camera-ready windows.
3. **Format pass** — page budget for main text vs references, template and
   class options, desk-reject wording, camera-ready page allowance.
4. **Policy pass** — double-anonymous wording, open-science requirements and
   availability-statement placement, dual submission, any AI-use disclosure
   added since 2027.
5. **Track-fit pass** — current calls for NIER, SEIP, SEIS, Demonstrations,
   and journal-first windows, in case routing (see `icse-topic-selection`)
   changed while you were writing.

## Useful non-official tooling

- `pdfinfo` / `pdftotext` (poppler) for metadata and identity-leak scans of
  the submission PDF.
- `git archive` for history-free anonymized replication packages.
- Container tooling (Docker/Podman) for freezing artifact environments the
  week of acceptance, before January bit-rot.
- dblp BibTeX export for reference hygiene — SE venue names mutate across
  years (ESEC/FSE naming, ICSE companion volumes) and dblp normalizes them.
- The shared reproducibility kit in this repository (see `code/README.md`)
  for package smoke checks.

## Do not infer

- Do not project the 2027 single cycle, the 10+2 page budget, the IEEE
  template choice, or the September/October/November/December pipeline onto
  any other edition — 2025/2026 already differed on the biggest of these.
- Do not treat ICSE norms as interchangeable with FSE/ASE/ISSTA mechanics;
  the venues share a community but not calendars, page models, or badging
  schedules.
- Do not assume the absence of an AI-use policy persists, and do not assume
  supplementary material is guaranteed reviewer reading.
- When pages conflict, prefer the newest dated official announcement, then
  the HotCRP site's own instructions, then direct chair communication — and
  record what conflicted in your notes.
