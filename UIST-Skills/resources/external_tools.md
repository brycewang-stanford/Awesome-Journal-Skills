# External Tools - UIST

Access date: 2026-07-08 (direct fetches of `uist.acm.org` returned 403; URLs were
verified through search renderings and ACM DL/dblp cross-checks — open them directly
before acting on anything time-sensitive).

## Live official surfaces

- UIST 2026 home (venue, dates, announcements): https://uist.acm.org/2026/
- UIST 2026 Call for Participation (all tracks, all deadlines): https://uist.acm.org/2026/cfp/
- UIST 2026 Author Guide (template, page limits, video specs, anonymization, TAPS):
  https://uist.acm.org/2026/author-guide/
- UIST 2026 organizers (rotating chairs, track contacts): https://uist.acm.org/2026/organizers/
- PCS submission system (SIGCHI → UIST 2026 → track): https://new.precisionconference.com/
- ACM DL conference hub (main + adjunct proceedings): https://dl.acm.org/conference/uist
- dblp series index (edition and paper verification): https://dblp.org/db/conf/uist/index.html
- ACM TAPS author workflow (camera-ready production): https://www.acm.org/publications/taps/
- SIGCHI (sponsor-level policies and announcements): https://sigchi.org/

## Author-side verification passes

Run each pass against the live pages above, not against this pack's snapshot.

1. **Track and calendar pass** — confirm which track (Papers, Demos, Posters,
   Doctoral Symposium, SIC, Workshops) you are actually inside, its current
   deadline, and its notification date. The Papers deadline for 2026 (March 31) has
   passed; adjunct-track deadlines were not verifiable on 2026-07-08 and must be read
   from the CFP directly.
2. **Format pass** — recompile with the current `acmart` options named in the Author
   Guide, count body pages against the 10/5-page limits, and confirm references and
   appendices are the only overflow.
3. **Video pass** — check duration (≤ 3 min), resolution (1080p/4K), container and
   codec (MP4/H.264), caption track, and that neither frames nor audio identify an
   author, lab, or building.
4. **Anonymity pass** — PDF metadata, acknowledgements, grant strings, repository
   URLs, third-person self-citation phrasing, and the anonymized copy of any
   overlapping prior submission.
5. **Camera-ready pass** (live phase for accepted 2026 papers) — TAPS source upload,
   alt text on every figure/subfigure/table, the rebuttal-promised changes actually
   made, the 10% growth allowance not exceeded, and the final video figure with
   captions.

## Do not infer

- Do not project the 2026 dates onto 2027; UIST re-publishes its full calendar every
  edition and has changed length rules across recent cycles.
- Do not assume the adjunct tracks share the Papers track's rules — Demos and Posters
  have their own chairs, formats, and archival home (the adjunct proceedings).
- Do not assume an artifact-evaluation committee, badge system, registration rule, or
  AI-use policy exists or persists without reading the current pages; where this pack
  could not verify an item it is marked 待核实 in
  [`official-source-map.md`](official-source-map.md).
- If pages disagree, the newest dated announcement on `uist.acm.org/2026/` or direct
  mail from the chairs (program2026@uist.org) controls; record the conflict.
