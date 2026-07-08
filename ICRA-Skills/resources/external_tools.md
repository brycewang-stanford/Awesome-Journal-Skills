# External Tools - ICRA

Access date: 2026-07-08

Live official surfaces for the ICRA pipeline, plus the author-side verification
passes to run before upload. Note the access caveat in
[`official-source-map.md`](official-source-map.md): the `*.ieee-icra.org` year-sites
blocked direct programmatic fetches at check time, so scripted link checks may 403
where a browser succeeds.

## Official surfaces

| Surface | URL | Use for |
| --- | --- | --- |
| Current year-site | https://2027.ieee-icra.org/ | CFP, dates, video windows, policies |
| Previous year-site | https://2026.ieee-icra.org/ | the most recent completed cycle's rules |
| RAS ICRA series page | https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/ | series continuity, future venues |
| PaperPlaza portal | https://ras.papercept.net/ | PIN accounts, templates, submission, PDF compliance test |
| RA-L author pages | https://www.ieee-ras.org/publications/ra-l/ | journal-pathway rules, presentation-option FAQ |
| IEEE Xplore | https://ieeexplore.ieee.org/ | proceedings ground truth, citation verification |
| IEEE author posting policy | https://www.ieee.org/publications/rights/ | preprint/self-archiving rules before updating arXiv |

## Author-side verification passes

Run these five passes before any PaperPlaza upload; each maps to a skill in this
pack.

1. **Geometry pass** (`icra-submission`): content ends by page 6; pages 7-8 hold
   references only; template class file untouched; PDF passes the PaperPlaza
   compliance test.
2. **Anonymity pass** (`icra-submission`, 2026-cycle double-anonymous rule): PDF
   author block, acknowledgements, self-citation grammar, PDF metadata, figure
   backgrounds, repository URLs, and video frames/captions/container metadata.
3. **Video pass** (`icra-supplementary`): ≤ 180 s, ≤ 20 MB, allowed container,
   speed changes labeled, trial conditions cross-referenced to paper tables,
   upload window dates confirmed for the current cycle.
4. **Evidence pass** (`icra-experiments`): claim altitude vs evidence rung; trial
   counts and success criteria printed; baselines hardware-matched; failure
   taxonomy sums to total trials.
5. **Timing pass** (`icra-workflow`): deadline converted to local time from 23:59
   **Pacific** (the 2026-cycle zone — not AoE); both video windows and the paper
   deadline in the team calendar.

## Do not infer

- Do not project ICRA 2026 numbers (page split, video specs, Pacific-time
  deadline, double-anonymity) onto ICRA 2027 without reopening the 2027 pages —
  the 2025→2026 anonymity flip proves these rules genuinely change.
- Do not apply RA-L rules (extra pages at USD 175, rolling deadlines, revision
  rounds) to the conference track or vice versa; the two systems share PaperPlaza
  but not policy.
- Do not treat aggregator sites' dates as authoritative; they lag and occasionally
  contradict the year-site. Where sources disagree, the newest first-party page or
  direct organizing-committee communication controls, and the conflict should be
  recorded in the source map.
