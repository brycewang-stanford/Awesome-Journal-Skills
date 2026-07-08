# External Tools - FOCS

Access date: 2026-07-08

Official surfaces for the FOCS author workflow, plus the author-side checks
this venue actually rewards. FOCS rules are re-issued each edition; open the
live cycle's pages before relying on anything here. (At the access date the
official domains answered only via search renderings in this environment —
see the access-method note in `official-source-map.md`.)

## Official surfaces

- Current-cycle site: https://focs.computer.org/2026/ (pattern:
  `focs.computer.org/<year>/`)
- Call for papers: https://focs.computer.org/2026/call-for-papers-2/
- Submission portal: https://focs26.hotcrp.com/ (pattern: `focs<yy>.hotcrp.com`)
- Workshop call: https://focs.computer.org/2026/call-for-workshops/
- Series page: https://ieee-focs.org/
- Sponsor: https://tc.computer.org/tcmf/ (IEEE CS Technical Committee on
  Mathematical Foundations of Computing — CFP reposts, Test of Time Award
  calls and citations)
- Proceedings: https://ieeexplore.ieee.org/xpl/conhome/1000292/all-proceedings
  and https://www.computer.org/csdl/proceedings/1000292
- Full-version hosts: https://arxiv.org/ and https://eccc.weizmann.ac.il/
- Bibliographic ground truth: https://dblp.org/db/conf/focs/
- The other flagship's calendar (for the two-beat year): https://acm-stoc.org/

## Author-side checks keyed to the skills

1. **Significance dossier** (`focs-topic-selection`) — the written
   consequence/obstacle/durability answers, reviewed by a co-author before
   any formatting work begins.
2. **Window walkthrough** (`focs-writing-style`, `focs-supplementary`) — a
   colleague outside your subarea reads only the abstract, references, and
   pages 1-10 and must be able to state every claimed result and its novelty.
3. **Mechanical PDF pass** (`focs-submission`) — page size and count,
   `qpdf --show-encryption` (the CFP bans copy/print restrictions), metadata
   and self-reference sweep for double-blind.
4. **Statement-freeze hash** (`focs-reproducibility`, `focs-camera-ready`) —
   extract and hash all theorem/lemma environments in the submission source
   and the arXiv source; hashes must match at every publication event.
5. **Import audit** (`focs-related-work`) — every cited external theorem
   located by number and version; every dblp key checked `conf/focs/` vs
   `conf/stoc/`.
6. **Certificate re-run** (`focs-experiments`, `focs-artifact-evaluation`) —
   any machine-checked step re-verified from a clean clone by a non-author
   using only the packaged checker and README.

## Do not infer

- Do not project FOCS 2026 dates onto FOCS 2027; the next cycle's CFP is the
  only source for its deadline, venue, and policies.
- Do not assume notification or camera-ready dates from history; the 2026
  ones were unpublished at the access date (待核实).
- Do not carry STOC's format numbers (twelve-page window, ToC rule) into
  FOCS advice: the FOCS 2026 guaranteed set is abstract + references + ten
  pages, and the two venues' CFPs differ in exactly such details.
- If official pages conflict, the newest CFP or direct PC-chair
  communication controls; record the conflict in the source map.
