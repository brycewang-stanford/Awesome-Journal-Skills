# External Tools - STOC

Access date: 2026-07-08

Official surfaces for the STOC author workflow, plus the author-side verification
passes this venue actually rewards. STOC rules are re-issued per cycle; open the
live year's pages before relying on anything here. (Note: at the access date the
official domains were reachable only via search renderings in this environment —
see the access-method note in `official-source-map.md`.)

## Official workflow surfaces

- STOC series home: https://acm-stoc.org/
- Current-cycle site and CFP (2026 anchor): https://acm-stoc.org/stoc2026/ and
  https://acm-stoc.org/stoc2026/stoc2026-cfp.html
- Submission portal (2026): https://stoc26.hotcrp.com/
- SIGACT (sponsor, prizes, policies): https://sigact.org/
- ACM Digital Library proceedings series: https://dl.acm.org/ (58th proceedings:
  https://dl.acm.org/doi/proceedings/10.1145/3798129)
- Full-version hosts: https://arxiv.org/ (cs.DS, cs.CC, cs.CG, quant-ph...) and
  https://eccc.weizmann.ac.il/ (complexity-focused, community-reviewed)
- Bibliographic ground truth: https://dblp.org/db/conf/stoc/
- Sibling-cycle calendars: https://focs.computer.org/ (FOCS),
  https://www.siam.org/conferences/ (SODA), https://computationalcomplexity.org/ (CCC)

## Author-side verification passes

Run these before upload; each maps to a skill in this pack.

1. **Guaranteed-read pass** — every theorem stated within abstract + ToC + first
   twelve pages; ToC section titles narrate the argument (`stoc-submission`,
   `stoc-supplementary`).
2. **Statement-consistency pass** — extended abstract and full-version theorem
   statements are byte-identical or single-sourced (`stoc-reproducibility`).
3. **Anonymity pass** (double-blind cycles) — author block, acknowledgements,
   grant lines, first-person self-citations, and PDF metadata all clean
   (`stoc-submission`); check with `pdfinfo paper.pdf` and a grep for author
   surnames over the LaTeX sources.
4. **Policy pass** — no simultaneous submission to a proceedings-publishing
   venue or journal; prior-publication status checked against the SIGACT rule
   (`stoc-submission`).
5. **Lineage pass** — final arXiv/ECCC sweep for new bounds on your problem;
   comparison table quotes the strongest prior work (`stoc-related-work`).
6. **Certificate pass** — any computer-assisted proof step ships a deterministic
   run and an independent checker (`stoc-experiments`,
   `stoc-artifact-evaluation`).

## Do not infer

- Do not infer STOC 2027 dates, the reading-window size, or double-blind details
  from the 2026 cycle; each is CFP-controlled and has changed across cycles.
- Do not infer FOCS/SODA/CCC rules from STOC's — the venues share a community
  but not their mechanics (FOCS is IEEE-side; SODA runs through SIAM).
- Do not treat aggregator sites (wikicfp and similar) as authoritative for
  future STOC editions; at the access date they carried recycled 2026 data
  labeled as 2027.
- If official pages conflict, the newest CFP or a direct PC-chair announcement
  controls; record the conflict in the source map when updating this pack.
