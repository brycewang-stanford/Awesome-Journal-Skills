# ICDM Skills

Twelve agent skills for papers targeting **ICDM — the IEEE International Conference on
Data Mining** — the IEEE-sponsored flagship for data-mining algorithms, graph and
pattern mining, anomaly detection, and applied analytics. The pack is built around the
four structural facts that make ICDM strategy different from its ACM and SIAM siblings:

1. **Triple-blind review, not double-blind.** Since 2011 ICDM's Research Track hides
   both author *and* referee identities; names are known only to the PC Co-Chairs, and
   author names are disclosed only after ranking and acceptance are finalized. Identity
   must be concealed **throughout the whole paper**, not just the first page.
2. **A single all-inclusive page cap.** Submissions are IEEE two-column, **10 pages
   maximum including the bibliography and any appendices** — everything counts inside
   the 10 pages, and over-length papers are **rejected without review**. There is no
   separate reference or appendix budget.
3. **A regular-to-short acceptance mechanic.** Every paper is submitted in full-paper
   format; based on quality and reviews, **some are accepted as short papers**.
   Acceptance-as-short is a distinct outcome authors must plan a camera-ready for.
4. **A new two-track split in 2026.** For the first time the edition runs an **Applied
   Track (single-blind)** and a CCC-sponsored **Blue Sky Track** alongside the
   triple-blind Research Track — so the anonymity regime now depends on the track.

Official basis checked on **2026-07-09**: the ICDM 2026 site (26th edition, Nov 12-15,
2026, Northeastern University, Shenyang, China), the Research and Applied Track calls,
the CCC Blue Sky Track call, the IEEE ICDM awards roster, IEEE Xplore proceedings, and
dblp. The host domain returns 403 to automated fetches, so facts were verified through
search renderings and cross-checked against dblp and the awards site. The exact source
map, the access-method note, and every fact left 待核实, are in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Verified 2026-edition anchors

| Fact | 2026 value | Volatility |
|---|---|---|
| Edition | 26th IEEE ICDM, Nov 12-15 2026, NEU, Shenyang, China | Per edition |
| Deadlines | Abstract 2026-05-30; full paper 2026-06-06 (AoE); notification 2026-08-16 | Per edition |
| Cycle model | **Single deadline** (no KDD-style cycles) | Stable-ish |
| Format | IEEE two-column, **10 pages incl. references + appendices**; over-length = no-review reject | Per edition |
| Research Track review | **Triple-blind** since 2011 (authors + referees hidden; PC Co-Chairs only) | Per edition |
| Applied Track review | **Single-blind** (new track in 2026) | Per edition |
| Short-paper mechanic | All submit as full papers; some accepted as **short papers** | Per edition |
| Rebuttal | Historically **none**; any response window is 待核实 for 2026 | Per edition |
| Publication | IEEE proceedings, indexed on IEEE Xplore and dblp; in-person presentation required | Per year |

Camera-ready dates, chair names, fees, short-paper camera-ready length, and any rebuttal
mechanics are flagged 待核实 in the source map rather than guessed.

## Skills

Routing and planning:

- [`icdm-topic-selection`](skills/icdm-topic-selection/SKILL.md) — the venue-fit read
  plus the track fork (Research vs Applied vs Blue Sky), and neighbor routing to KDD,
  SDM, CIKM, WSDM, WWW, and the ML flagships from ICDM's June-deadline seat.
- [`icdm-workflow`](skills/icdm-workflow/SKILL.md) — the single-deadline pipeline:
  abstract-then-paper offsets, the long summer wait to the August notification, and the
  branch for a short-paper acceptance.

Building the paper:

- [`icdm-writing-style`](skills/icdm-writing-style/SKILL.md) — the ICDM register:
  data-regime-first framing, named-mechanism discipline, measured-scale language,
  discovery-validity sentences, and triple-blind-safe self-reference.
- [`icdm-related-work`](skills/icdm-related-work/SKILL.md) — lineage against prior ICDM
  editions and IEEE data-mining neighbors, the KDD/SDM/CIKM misattribution traps, and
  anonymized comparison to your own prior work.
- [`icdm-experiments`](skills/icdm-experiments/SKILL.md) — the mining-evidence plan:
  task definition, baselines, ablations that isolate the mechanism, scalability curves,
  and discovery-validity checks against evaluation artifacts.
- [`icdm-reproducibility`](skills/icdm-reproducibility/SKILL.md) — reproducibility inside
  the triple-blind regime: seeds, configs, compute, and an anonymized artifact that
  leaks no identity.

Packaging and submitting:

- [`icdm-artifact-evaluation`](skills/icdm-artifact-evaluation/SKILL.md) — building the
  anonymized, history-scrubbed repository for a triple-blind Research Track submission,
  and how the Applied Track's single-blind regime changes what may be revealed.
- [`icdm-supplementary`](skills/icdm-supplementary/SKILL.md) — living within one
  10-page all-inclusive cap: what belongs in the body vs an in-cap appendix vs an
  external anonymized repo, and the short-paper compression plan.
- [`icdm-submission`](skills/icdm-submission/SKILL.md) — the pre-deadline audit: track
  and anonymity regime, the 10-page all-inclusive check, triple-blind sweep, and the
  final-week sequence against the AoE cutoff.

Review phase and after:

- [`icdm-review-process`](skills/icdm-review-process/SKILL.md) — the triple-blind
  machinery, the Accept / **Accept-as-Short** / Reject outcome space, the mixed
  data-mining reviewer pool, and the no-rebuttal posture.
- [`icdm-author-response`](skills/icdm-author-response/SKILL.md) — how to prepare for a
  venue that may offer no rebuttal at all, and how to answer tightly if a response
  window exists — without breaking anonymity.
- [`icdm-camera-ready`](skills/icdm-camera-ready/SKILL.md) — IEEE camera-ready, eCopyright,
  de-anonymization, in-person presentation, and the compression path if the paper was
  accepted as a short paper.

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — every official
  URL with access date, the access-method note, the verified-facts list, and the 待核实
  register.
- [`resources/external_tools.md`](resources/external_tools.md) — track calls, IEEE Xplore,
  the awards site, dblp, and per-edition author checks.
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — award-verified ICDM
  exemplars (Isolation Forest, Fast RWR, implicit-feedback CF, PEGASUS, SLIM, DTW
  averaging) plus the KDD/CIKM/WSDM/SDM misattribution guard.
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  — a fictional before/after rewrite into the ICDM first-page arc: data regime →
  mechanism → baseline + scale → discovery validity.
- [`resources/code/README.md`](resources/code/README.md) — adapter to the shared
  ML-conference reproducibility kit, with the triple-blind artifact caution.

## Suggested sequence

1. **Route**: `icdm-topic-selection` (venue fit + track fork), then `icdm-workflow` (the
   single-deadline calendar and the long wait to August).
2. **Build**: `icdm-experiments` + `icdm-reproducibility` while writing with
   `icdm-writing-style` and `icdm-related-work`.
3. **Package**: `icdm-artifact-evaluation` and `icdm-supplementary` *before* deadline
   week; then the `icdm-submission` audit against the 10-page all-inclusive cap.
4. **Wait and read**: `icdm-review-process` for the packet; `icdm-author-response` only
   if the edition offers a response window.
5. **Publish**: `icdm-camera-ready` on acceptance, with the short-paper branch ready.

## Installation

The pack ships as a Claude Code plugin. From this repository:

```bash
# add the marketplace rooted at this directory, then install the plugin
claude plugin marketplace add ./ICDM-Skills
claude plugin install icdm-skills
```

Or point an agent directly at individual `skills/icdm-*/SKILL.md` files — each skill is
self-contained, states its scope in the frontmatter description, and ends with a
structured output format so results compose across skills.

## Scope and disclaimers

- This pack advises on **strategy, structure, and evidence** for ICDM submissions. It is
  not the CFP: where any statement here conflicts with the current edition's official
  instructions, the official instructions win, always.
- Facts are dated. Everything specific was checked on 2026-07-09 against the sources in
  the source map; unstable items (deadlines, fees, chairs, rebuttal mechanics) are phrased
  as edition-volatile or 待核实 rather than asserted.
- No text here should be pasted into a paper. The worked example is fictional by design,
  and the exemplar library records positioning patterns, not reusable prose.

## Maintenance notes

- Every dated fact above is a **2026-edition anchor, not a rule**. ICDM re-sets tracks
  (the Applied and Blue Sky tracks were new in 2026), review model per track, page
  handling, short-paper mechanics, and any response policy between editions.
- Before deadline-sensitive advice, reopen the **track-specific** call — Research and
  Applied now differ on anonymity, so "the ICDM CFP" is ambiguous at this venue.
- Facts marked 待核实 (rebuttal window, short-paper camera-ready length, chairs, fees)
  must be verified live before being stated to an author as fact.
- If a call page and an IEEE Xplore or committee page disagree, prefer the newer official
  instruction and record the conflict.
