# External Tools - ACM PODC

Access date: 2026-07-09

Use these surfaces after reopening the current PODC cycle pages. PODC mechanics — the exact dates,
the double-blind wording, whether a rebuttal phase runs, and the Brief Announcements limits — are
decided per edition, and the `podc.org` / `dl.acm.org` gateway may block direct fetches (read via
search renderings and cross-check dblp and the ACM DL proceedings). Do not confuse this venue with
**PODS** (Principles of Database Systems) or with **DISC** (the EATCS distributed-computing
symposium); see the guards in [`official-source-map.md`](official-source-map.md).

## Official workflow

- PODC series hub: https://www.podc.org/
- PODC 2026 home (Royal Holloway, Jul 6-10, 2026): https://www.podc.org/podc2026/
- PODC 2026 call for papers: https://www.podc.org/podc2026/call-for-papers/
- PODC 2026 program committee: https://www.podc.org/podc2026/program-committee/
- PODC 2026 submission site (HotCRP): https://podc26.hotcrp.com/
- Dijkstra Prize (joint PODC/DISC): https://www.podc.org/dijkstra/
- Doctoral Dissertation Award (joint PODC/DISC): https://www.podc.org/dissertation/
- Co-located SPAA 2026: https://spaa.acm.org/
- ACM Master (`acmart`) template: https://www.acm.org/publications/proceedings-template

## Cross-check surfaces (when the gateway blocks the primary page)

- dblp PODC proceedings series: https://dblp.org/db/conf/podc/ (accepted-paper and exemplar
  verification; match the venue string to a PODC edition, not DISC/SPAA/OPODIS).
- ACM DL PODC conference page: https://dl.acm.org/conference/podc (proceedings tables of contents).
- DMANET theory-announcements blog: the PODC call-for-papers postings mirror the official dates.
- wikicfp PODC entry and confsearch (deadline aggregation) for a quick cross-check of the cutoff.
- The PODC/DISC community feed (`@podc_disc@mathstodon.xyz`) for chair announcements.

## Author-side checks

- HotCRP profile, conflicts, coauthor list, and topic selection; the **abstract registration** step
  (11 Feb 2026) that precedes the full-paper deadline (16 Feb 2026).
- `acmart` two-column compliance; the **first 10 pages after the title page** carry the full merits
  case (importance, prior-work context, key technical/conceptual ideas); the full version with all
  proofs is the submission.
- **Lightweight double-blind sweep:** remove author names, affiliations, and emails from the PDF and
  its metadata; neutralize self-citations ("we build on [X]" → "[X]"); scrub acknowledgements and
  grant numbers; check that a linked arXiv/full version does not de-anonymize you at review time.
- **Regular vs. Brief Announcement** decision: is the result complete-with-proof (regular) or an
  announcement / in-progress / published-elsewhere item (≤5-page Brief Announcement)?
- Proof appendix completeness and an explicit model box (network, timing, fault, cost measure)
  before the abstract's result statement.

## Do not infer

- Do not infer the review model: PODC 2026 is **lightweight double-blind**, a change from its
  historically single-blind practice — do not carry a prior single-blind assumption forward, and do
  not over-anonymize past what the call requires.
- Do not assume a rebuttal/author-response phase exists — **待核实** for 2026; confirm on the call.
- Do not assume the page-budget wording, the Brief Announcement limits, or any AI-disclosure policy
  carry over between editions.
- Do not import an artifact-evaluation / badge workflow: PODC has **no artifact track**. The
  "evaluation" of a PODC paper is the proof and the honesty of the model/assumptions.
- If pages disagree, treat the newest call for papers, the HotCRP deadline, or a direct chair
  announcement as controlling, and record the conflict.
