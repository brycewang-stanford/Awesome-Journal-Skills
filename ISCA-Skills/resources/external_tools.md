# External Tools - ISCA

Access date: 2026-07-08

Surfaces to open, and author-side checks to run, around an ISCA submission.
Every URL below is per-edition or rotating: substitute the target year and
reopen before acting. The verification gateway blocked direct fetches of
several of these hosts on the access date (see the note in
[`official-source-map.md`](official-source-map.md)); from an ordinary network
they open normally.

## Official surfaces

- Conference site hub (per edition): https://iscaconf.org/ →
  `iscaconf.org/isca<year>/`
- ISCA 2026 Call for Papers: https://iscaconf.org/isca2026/submit/callforpapers.php
- ISCA 2026 submission guidelines (page rule, template, blinding):
  https://iscaconf.org/isca2026/submit/guidelines.php
- ISCA 2026 artifact evaluation: https://iscaconf.org/isca2026/submit/artifactevaluation.php
- HotCRP portal (per edition): `isca<year>.hotcrp.com` (2026: https://isca2026.hotcrp.com/)
- Sponsor postings — cross-checks when the site is slow to update:
  https://www.sigarch.org/call-contributions/ and https://ieeetcca.org/
- Proceedings records: https://dblp.org/db/conf/isca/ (publisher-neutral spine),
  plus ACM DL (https://dl.acm.org/conference/isca) and IEEE Xplore depending on
  the edition's publisher.
- Award lineage for exemplars:
  https://www.sigarch.org/benefit/awards/acm-sigarchieee-cs-tcca-influential-isca-paper-award/

## Author-side verification passes

Run each pass against the live pages, in this order, before upload:

1. **Calendar pass** — abstract date, paper date, AoE convention, industry-track
   dates if relevant, rebuttal/revision window. The 2026 pattern (Nov 10/17 →
   Feb 16-Mar 6 → late-June conference) is a template, not a promise.
2. **Format pass** — current page count and what it excludes (2026: 11 pages of
   text, references uncounted), the edition's template (IEEE-flavored in 2026;
   the publisher alternates), printable-PDF requirement.
3. **Blinding pass** — the three 2026-verified rules (no names outside the form;
   clean PDF metadata; fully anonymized artifact links) plus the counter-rule
   (references never anonymized). Mechanical sweeps live in
   [`../skills/isca-submission/SKILL.md`](../skills/isca-submission/SKILL.md).
4. **Portal pass** — HotCRP account, all form fields, complete per-author
   conflicts, topics chosen deliberately, status = submitted (not saved).
5. **Post-acceptance pass** — camera-ready page and its publisher workflow, AE
   calendar and badge set, registration/attendance obligations. All three vary
   by edition and none was verifiable for 2027 at the access date.

## Do not infer

- Do not project ISCA 2026 dates onto ISCA 2027; at the access date no 2027 CFP
  existed. "Mid-November" is an expectation to verify, nothing more.
- Do not assume the publisher, template, camera-ready allowance, badge set, or
  attendance policy carries over between editions — the ACM/IEEE alternation
  makes carry-over assumptions worse at ISCA than at single-sponsor venues.
- Do not quote acceptance rates, notification dates, or chair rosters from
  memory or third-party aggregators; if it matters, find it on an official page
  and record URL + date in the source map.
- When official pages conflict, prefer the conference site over sponsor
  cross-posts, and direct chair email over both; record the conflict.
