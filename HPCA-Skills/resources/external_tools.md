# External Tools - HPCA

Access date: 2026-07-09

Surfaces to open, and author-side checks to run, around an HPCA submission. Every
URL below is per-edition or rotating: substitute the target year and reopen before
acting. The verification gateway blocked direct fetches of several of these hosts on
the access date (see the note in
[`official-source-map.md`](official-source-map.md)); from an ordinary network they
open normally.

## Official surfaces

- Series landing page: https://hpca-conf.org/ → per edition `20XX.hpca-conf.org/`
- HPCA 2027 Call for Papers: https://2027.hpca-conf.org/call-for-papers/
- HPCA 2027 important dates (researchr mirror):
  https://conf.researchr.org/dates/hpca-2027
- HPCA 2025 Call for Papers (format and blinding wording still useful):
  https://hpca-conf.org/2025/call-for-papers/
- HotCRP submission portal (per edition): `hpca<year>.hotcrp.com`
  (2026: https://hpca2026.hotcrp.com/)
- Artifact-evaluation portal (per edition, separate site):
  `hpca<year>ae.hotcrp.com` (2026: https://hpca2026ae.hotcrp.com/)
- Sponsor / awards — cross-checks and exemplar lineage:
  https://ieeetcca.org/ and https://ieeetcca.org/awards/hpca-test-of-time-award/
- Proceedings records: https://dblp.org/db/conf/hpca/ (publisher-neutral spine)
  and IEEE Xplore for the edition's published volume.

## Author-side verification passes

Run each pass against the live pages, in this order, before upload:

1. **Calendar pass** — abstract-and-conflict registration date, paper date, the AoE
   convention, industry-track dates if relevant, and the rebuttal/revision window.
   The recent pattern (late-July registration/paper → autumn notification →
   February/March conference) is a template, not a promise.
2. **Format pass** — the current page count and what it excludes (recent cycles:
   11 pages of text, references uncounted), the minimum-font and leading rules, the
   IEEE template, and the printable-PDF requirement.
3. **Blinding pass** — names only in the form; scrubbed PDF metadata; anonymized
   artifact links; plus the counter-rule that references are never anonymized and
   **each reference must list all authors**. The AI-use disclosure belongs in the
   acknowledgments (which is de-anonymized only at camera-ready). Mechanical sweeps
   live in [`../skills/hpca-submission/SKILL.md`](../skills/hpca-submission/SKILL.md).
4. **Portal pass** — HotCRP account, every form field, complete per-author
   conflicts finalized by the registration step, topics chosen deliberately, and
   status = submitted (not merely saved).
5. **Post-acceptance pass** — camera-ready page and the IEEE rights workflow, the AE
   calendar and badge set on the separate AE HotCRP, and registration/attendance
   obligations. All vary by edition; none was verifiable for 2027 at the access date.

## Do not infer

- Do not project HPCA 2026 dates onto HPCA 2027 beyond the verified July 24, 2026
  paper deadline; the rebuttal window and exact conference dates were unconfirmed.
- Do not assume the 2027 page limit equals 11 pages until the 2027 guidelines say
  so, and do not assume the camera-ready allowance, badge set, or attendance policy
  carries over between editions.
- Do not import ACM habits: HPCA uses **IEEE reproducibility badging**, an IEEE
  template, and IEEE rights forms — not the ACM Artifact Review and Badging policy
  or ACM DL conventions used at ISCA/MICRO/ASPLOS.
- Do not quote acceptance rates, notification dates, or chair rosters from memory or
  third-party aggregators; if it matters, find it on an official page and record URL
  + date in the source map.
- When official pages conflict, prefer the current conference site over the
  researchr mirror or sponsor cross-posts, and direct chair email over all; record
  the conflict.
