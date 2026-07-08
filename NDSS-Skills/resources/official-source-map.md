# Official Source Map - NDSS

Access date: 2026-07-08

This map records the official sources behind every NDSS-specific fact used in this pack.
NDSS policy is re-issued per symposium and per submission cycle; reopen the current Call for
Papers, the live HotCRP cycle site, the Call for Artifacts, and the symposium logistics pages
before giving deadline-sensitive advice.

## How these sources were accessed

Direct HTTPS requests to `www.ndss-symposium.org` and `dblp.org` returned HTTP 403 in the
verification environment (proxy-level denial), so the pages could not be fetched raw.
Every fact below was instead read through search-engine renderings of the exact official
URLs and then cross-checked across at least two independent surfaces: the NDSS 2027 pages,
the live `ndss27-summer.hotcrp.com` site, Internet Society announcements and blog posts, dblp
record links, and secondary trackers. Where a fact could be found on only one surface, it is
marked 待核实 below rather than stated in the skills.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.ndss-symposium.org/ndss2027/ | NDSS 2027 identity: the symposium and its co-located workshops take place in Seoul, Republic of Korea, 22-26 March 2027. | 2026-07-08 |
| 2 | https://www.ndss-symposium.org/ndss2027/submissions/call-for-papers/ | Two review cycles (summer and fall); summer paper deadline May 6, 2026 and fall paper deadline August 19, 2026, both 11:59 PM AoE (UTC-12); two-round review per cycle; early-reject notification with Round-1 reviews; rebuttal and interactive discussion in Round 2; decision categories including Accept, Minor Revision, and Major Revision with reviewer-specified revision tasks; at most one major revision; major overlap between a summer-rejected paper and a fall submission disallowed; 13-page limit excluding the Ethics Considerations section, references, and appendices; NDSS templates; double-blind review; per-author cap of six submissions per cycle (twelve per year); Ethics Review Board drawn from the TPC; Menlo Report guidance; responsible-disclosure expectations; camera-ready January 6, 2027. | 2026-07-08 |
| 3 | https://www.ndss-symposium.org/ndss2027/submissions/call-for-artifacts/ | NDSS 2027 artifact evaluation: authors of (conditionally) accepted papers may opt in shortly after notification; evaluated papers add a 2-page artifact appendix and carry badges on the first page. | 2026-07-08 |
| 4 | https://ndss27-summer.hotcrp.com/ | The NDSS 2027 summer-cycle HotCRP submission site exists and is the review portal for that cycle (its PC listing is at `/users/pc`). | 2026-07-08 |
| 5 | https://www.internetsociety.org/blog/2026/06/ndss-symposium-2027-heads-to-seoul-expanding-global-collaboration-in-cybersecurity-research/ | Internet Society announcement (June 2026) that NDSS 2027 moves to Seoul, 22-26 March 2027 — the first break from the fixed San Diego/February pattern — with registration opening October 2026 and Asia-Pacific participation up more than 60% over three years. | 2026-07-08 |
| 6 | https://www.ndss-symposium.org/ndss2026/ | Historical anchor: NDSS 2026 was held 23-27 February 2026 in San Diego, CA, continuing the long-standing San Diego February identity through 2026. | 2026-07-08 |
| 7 | https://www.ndss-symposium.org/ndss2026/co-located-events/ | NDSS 2026 co-located workshops, including BAR (Binary Analysis Research), USEC (Usable Security and Privacy), and MADWeb (Measurements, Attacks, and Defenses for the Web). | 2026-07-08 |
| 8 | https://www.ndss-symposium.org/ndss2025/submissions/call-for-papers/ | NDSS's open-publication model: proceedings and presentation videos are freely available; noncommercial reproduction permitted with the Internet Society notice; authors may post camera-ready versions on personal and institutional pages. | 2026-07-08 |
| 9 | https://secartifacts.github.io/ndss2026/call | NDSS artifact evaluation mechanics as run for 2026 on the secartifacts platform: badge options are Available, Functional, and Reproduced, added to the camera-ready first page via `ndssbadges.sty`. | 2026-07-08 |
| 10 | https://www.ndss-symposium.org/ndss-test-of-time-award/ | The NDSS Test of Time Award: recognizes NDSS papers at least ten years old with lasting research or industrial impact. | 2026-07-08 |
| 11 | https://dblp.org/db/conf/ndss/index.html | The dblp proceedings stream `conf/ndss`, used to cross-check exemplar papers and edition numbering (e.g., NDSS 2018 = 25th edition, San Diego, February 18-21, 2018). | 2026-07-08 |

## Verified cycle facts used in the skills

All verified 2026-07-08 against the sources above; every one is a cycle snapshot, not a rule.

- **NDSS 2027 meets in Seoul, Republic of Korea, 22-26 March 2027** (sources 1, 5). This is a
  deliberate, announced departure from the San Diego February slot that NDSS held through
  2026 (source 6). Registration opens in October 2026 (source 5).
- **Two submission cycles feed the one symposium** (source 2): summer papers were due
  May 6, 2026 (passed before this pack's check date) and fall papers are due
  **August 19, 2026, 11:59 PM AoE (UTC-12)** — about six weeks after 2026-07-08.
- **Summer-cycle timetable**: early-reject notification June 12, 2026; rebuttal
  June 24-28, 2026; final notification July 22, 2026 (source 2). On the check date the
  summer cycle was between rebuttal and final notification.
- **Fall-cycle timetable**: paper deadline August 19, 2026; early-reject notification
  September 25, 2026; rebuttal October 8-10, 2026; final notification November 4, 2026
  (source 2).
- **Review runs in two rounds per cycle**: Round 1 filters; authors receive Round-1 reviews
  at the early notification together with the early-reject-or-continue outcome; Round-2
  papers get a rebuttal plus an interactive discussion phase with reviewers (source 2).
- **Decision categories include Accept, Minor Revision, and Major Revision**; a Major
  Revision comes with an explicit list of revision tasks from the original reviewers, is
  re-reviewed against that list, and can happen at most once per paper for NDSS 2027
  (source 2).
- **A paper rejected in the summer cycle may not reappear with major overlap in the fall
  cycle** of the same symposium (source 2).
- **Format**: technical papers must not exceed 13 pages excluding the Ethics Considerations
  section, references, and appendices, in the NDSS templates, in English; an optional
  Ethics Considerations section sits immediately before the references (source 2).
- **Review is double-blind**; author names and affiliations must not appear (source 2).
- **Each author may appear on at most six submissions per cycle** — twelve across the year
  (source 2).
- **Ethics is enforced structurally**: an Ethics Review Board of TPC members examines
  flagged papers; the Menlo Report is the recommended baseline; IRB exemption alone is not
  treated as sufficient mitigation; papers reporting high-impact vulnerabilities should
  report them or discuss a responsible-disclosure plan (source 2).
- **Camera-ready is due January 6, 2027** (source 2).
- **Proceedings are fully open access** through the Internet Society: papers and talk videos
  are free to the world, no reader paywall and no author-side page charge is part of the
  model; authors keep the right to self-post camera-ready versions (source 8).
- **Artifact evaluation is opt-in after (conditional) acceptance**, produces Available /
  Functional / Reproduced badges on the first page and a 2-page artifact appendix, and has
  run for NDSS since the 2024 edition (sources 3, 9; NDSS 2024/2025 calls for artifacts
  exist on ndss-symposium.org).
- **NDSS paper DOIs use the Internet Society prefix 10.14722** (cross-checked via the
  Kitsune dblp/Semantic Scholar record, DOI `10.14722/NDSS.2018.23204`).
- **Test of Time**: "Automated Whitebox Fuzz Testing" (NDSS 2008) won the 2022 award;
  the SMART remote-attestation architecture (NDSS 2012) won the 2024 award (source 10 plus
  Internet Society and UC Irvine announcements).

## Reported facts (secondary sources only — do not present as verified)

- Hyungsub Kim serves as an NDSS 2027 Publication Chair (found on a personal academic page,
  2026-07-08; confirm on the official organizing-committee page before citing).
- NDSS 2026 Friday workshops reportedly included LAST-X and FUZZING alongside BAR, USEC, and
  MADWeb (institutional news coverage; the official co-located-events page is source 7).

## 待核实 (could not be verified live on 2026-07-08)

- The NDSS 2027 **fall-cycle HotCRP URL** (the summer site is `ndss27-summer.hotcrp.com`; a
  parallel fall site is likely but was not observed).
- The **Major Revision resubmission window** dates for each 2027 cycle.
- The full **decision-category list** verbatim (Reject wording, and whether a
  poster/short-paper track exists for 2027).
- NDSS 2027 **General Chairs and Program Chairs** (only a Publication Chair was found, and
  only on a personal page): https://www.ndss-symposium.org/ndss2027/leadership/organizing-committee/
- Any **generative-AI usage policy** for NDSS 2027 submissions.
- The **2027 co-located workshop list** for Seoul (the 2026 list is verified; 2027's is not).
- **Artifact-evaluation deadlines** for each 2027 cycle and whether the 2027 badge set is
  identical to 2026's.
- Attendance/presentation obligations for accepted papers (registration terms for Seoul).

## Still cycle-volatile

Dates, page limits, the per-author cap, revision mechanics, ethics-section wording, ERB
procedure, template versions, HotCRP URLs, badge definitions, and the host city itself (as
the 2027 Seoul move proves) can all change per symposium. The controlling source is always
the newest official CFP or a direct message from the chairs; record any conflict you find.
