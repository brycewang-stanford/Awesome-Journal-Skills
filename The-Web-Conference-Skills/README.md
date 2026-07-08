# The Web Conference Skills

Twelve agent skills for papers targeting **The ACM Web Conference (WWW)** — the
flagship venue for research on the Web itself: its graphs, platforms, markets,
search systems, users, and societal effects, running annually since WWW1 at CERN in
1994. The pack is organized around the five structural facts that make Web
Conference strategy unlike its ML and mining siblings:

1. **Review happens inside topical tracks.** The 2026 edition fielded ten research
   tracks, each with its own chairs and reviewer pool; track choice decides who
   judges the paper and by which evidence bar — a routing decision as consequential
   as the venue decision.
2. **The author list freezes at the abstract deadline**, a week before the paper is
   due: no additions, removals, or reordering afterward, and each author is capped
   at seven research-track submissions.
3. **One PDF, three zones.** In 2026: 8 pages of main paper that must be
   self-contained (reviewers need not read further), then references and an
   optional appendix sharing the remainder of a 12-page ceiling — no separate
   supplementary upload.
4. **The web-nativeness bar.** The venue's signature rejection is "unclear why this
   is a WWW paper"; contributions must depend on link structure, platform
   mechanics, live user behavior, or web-scale constraints — not merely evaluate on
   web data.
5. **ACM production with an availability badge.** Accepted papers flow through ACM
   e-rights and TAPS into the Digital Library, uniformly budgeted at 12 pages (8
   content), with an "Artifacts Available" badge earned by an archival,
   DOI-bearing deposit filed with the camera-ready.

Official basis checked on **2026-07-08**: the WWW 2026 site (35th edition, Dubai —
postponed mid-cycle from April to June 29 - July 3, 2026), the research-tracks CFP,
important-dates page, short-papers and Web4Good calls, the artifact-badging call,
ACM DL proceedings records for 2025-2026, SIGWEB venue announcements, and IW3C2
series history. Direct fetches of the conference domains were blocked in the build
environment, so contents were verified through search renderings of the exact
official URLs and cross-checked against ACM DL and dblp — the full method note,
source list, and every fact left 待核实 are in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Verified 2026-edition anchors

| Fact | 2026 value | Volatility |
|---|---|---|
| Edition | 35th, Dubai, UAE; postponed to June 29 - July 3, 2026 | Per edition |
| Research tracks | Ten, from graph algorithms to responsible Web | Re-cut most editions |
| Deadlines | Abstract 2025-09-30; paper 2025-10-07; rebuttal Nov 24 - Dec 1; notify 2026-01-13; camera-ready 2026-01-25 (AoE, strict) | Per edition |
| Format | `\documentclass[sigconf, anonymous, review]{acmart}`; 8-page main + refs + appendix ≤ 12 pages, first 8 self-contained | Per edition |
| Author rules | List frozen at abstract deadline; ≤ 7 submissions/author; LLMs cannot be authors | Per edition |
| Platform | EasyChair for 2026 research tracks (OpenReview in 2024-25; Industry 2026 on OpenReview) | Per track, per edition |
| Preprints | Anonymized arXiv/SSRN copies tolerated, uncited | Per edition |
| Later lanes | Short papers (4 pp incl. refs, Nov deadlines) and Web4Good (Nov deadlines), both into main proceedings | Per edition |
| Publication | ACM DL; 12 pages/8 content for all accepted papers; Artifacts Available badging at camera-ready | Per edition |
| Governance | ACM/SIGWEB + steering committee since 2022; IW3C2 ran 1994-2022; renamed The Web Conference in 2018 | Historical |

Chair rosters beyond the general co-chairs, rebuttal mechanics, fees, acceptance
rates, and ACM Open amounts could not be verified and are flagged 待核实 in the
source map rather than guessed.

## Skills

Routing and planning:

- [`webconf-topic-selection`](skills/webconf-topic-selection/SKILL.md) — the
  web-nativeness test, track fit across the ten 2026 tracks, lane choice
  (full/short/Web4Good/industry/workshop), and rerouting to WSDM, SIGIR, CIKM,
  KDD, ICWSM, or WebSci.
- [`webconf-workflow`](skills/webconf-workflow/SKILL.md) — the autumn-to-summer
  calendar, backward planning from the abstract deadline, the intra-edition
  fallback tree, and the 2026 postponement's travel-slack lesson.

Building the paper:

- [`webconf-writing-style`](skills/webconf-writing-style/SKILL.md) — the page-one
  web-native mechanism, writing for mixed computing/social-science panels,
  attaching numbers to adjectives, and 8-page compression by re-homing.
- [`webconf-related-work`](skills/webconf-related-work/SKILL.md) — lineage
  waypoints through three decades of WWW proceedings, sibling-circuit contrast
  sentences, venue-attribution hygiene, and the own-preprint non-citation rule.
- [`webconf-experiments`](skills/webconf-experiments/SKILL.md) — the
  claim-to-evidence contract, dataset provenance and freshness, temporal/
  popularity/duplication leakage, symmetric baseline tuning, and when live or
  user evidence is mandatory.
- [`webconf-reproducibility`](skills/webconf-reproducibility/SKILL.md) — the
  frozen/decaying/unreplayable regime model for web data, snapshot pinning,
  determinism audits, and temporal-split honesty.

Packaging and submitting:

- [`webconf-supplementary`](skills/webconf-supplementary/SKILL.md) — the
  three-container model (8 pages / shared PDF tail / external artifact), the
  references-vs-appendix zero-sum, and anonymized linking.
- [`webconf-artifact-evaluation`](skills/webconf-artifact-evaluation/SKILL.md) —
  the Artifacts Available badge bar, archival deposits with DOIs, sharing tiers
  for encumbered web data, and takedown-resilient packaging.
- [`webconf-submission`](skills/webconf-submission/SKILL.md) — the pre-deadline
  audit: author-list freeze, track declaration, the 7-submission cap, page-zone
  arithmetic, EasyChair profiles, and the anonymity sweep.

Review phase and after:

- [`webconf-review-process`](skills/webconf-review-process/SKILL.md) — track-scoped
  double-blind review, the four recurring decision questions, pipeline dates, and
  reading rejection packets for routing signal.
- [`webconf-author-response`](skills/webconf-author-response/SKILL.md) — the
  one-week rebuttal: classifying reviewer stances, answering the web-fit skeptic,
  small honest evidence, and camera-ready promises that fit 8 content pages.
- [`webconf-camera-ready`](skills/webconf-camera-ready/SKILL.md) — the 12-day
  window: de-anonymization sweeps, e-rights and TAPS, ACM Open checks,
  registration, and the artifact rider.

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — every
  source URL with access date, the verified-fact list, the access-method note, and
  the 待核实 register.
- [`resources/external_tools.md`](resources/external_tools.md) — official venue,
  proceedings, and platform links with per-edition author checks.
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — five
  proceedings-verified WWW papers (LINE, NCF, VAE-CF, HAN, the Twitter
  measurement study) plus the KDD/SIGIR/UAI misattribution guard.
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  — a fictional before/after rewrite into the web-native first-page arc.
- [`resources/code/README.md`](resources/code/README.md) — adapter to the shared
  ML-conference reproducibility kit plus crawl-manifest and decay-accounting
  additions.

## Suggested sequence

1. **Route**: `webconf-topic-selection` (web-nativeness, then track), calendar via
   `webconf-workflow`.
2. **Build**: `webconf-experiments` and `webconf-reproducibility` alongside
   `webconf-writing-style` and `webconf-related-work`.
3. **Package**: `webconf-supplementary` and `webconf-artifact-evaluation`, then the
   `webconf-submission` audit — author list and profiles settled *before* the
   abstract deadline.
4. **Respond**: `webconf-review-process` to read the packet, `webconf-author-response`
   for the rebuttal week.
5. **Publish**: `webconf-camera-ready`, with the artifact badge riding along.

## Installation

```bash
# from this repository root
claude plugin marketplace add ./The-Web-Conference-Skills
claude plugin install the-web-conference-skills
```

Each `skills/webconf-*/SKILL.md` is also directly usable as a standalone
instruction file; every skill declares its scope in the frontmatter and ends with
a structured output block so results compose.

## Scope and disclaimers

- This pack advises on **strategy, structure, and evidence** for Web Conference
  submissions. It is not the CFP; where anything here conflicts with the current
  edition's official pages, the official pages win without exception.
- All specific numbers are **2026-edition anchors** verified on 2026-07-08, and
  the 2026 edition itself demonstrated in-cycle volatility by moving its own
  dates. Reopen the live site before acting on any deadline, page count, or fee.
- No prose here is paper text. The worked example is fictional by design; the
  exemplar library records positioning patterns, not quotable results.

## Maintenance notes

- Re-verify the track list every edition — it is re-cut most years, and special
  tracks (Web4Good in 2026) come and go.
- Re-verify the submission platform per track: the series switched research
  tracks from OpenReview to EasyChair between 2025 and 2026.
- Items marked 待核实 in the source map (chairs, fees, rebuttal mechanics,
  acceptance rates, ACM Open terms) must be confirmed live before being stated to
  an author as fact.
- When sources conflict, the newest official edition page or direct chair
  communication controls; record the conflict and the access date in the source map.
