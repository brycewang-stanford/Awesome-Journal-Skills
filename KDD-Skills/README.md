# KDD Skills

Twelve agent skills for papers targeting **KDD — the ACM SIGKDD Conference on
Knowledge Discovery and Data Mining** — the flagship venue for data mining, applied
data science, and knowledge discovery at scale. The pack is built around the four
structural facts that make KDD strategy different from single-deadline ML venues:

1. **Two tracks with different evidence bars.** The Research Track wants a named
   mechanism with ablations and scale evidence; the Applied Data Science (ADS) Track
   wants deployed systems with **quantified post-launch performance** — and the 2026
   ADS CFP desk-rejects submissions that lack that quantification.
2. **Two submission cycles per year.** Each cycle pairs an abstract deadline with a
   paper deadline about a week later, and the decision space includes **Resubmit**,
   which feeds a paper from one cycle into the next with a mandatory change summary.
3. **A no-hyperlink rebuttal.** Author responses cannot carry links, so the
   repository cited inside the submitted PDF is the only artifact reviewers will ever
   see — artifact work must finish *before* the deadline, not after reviews.
4. **ACM production.** Accepted papers flow through ACM e-rights and TAPS into the
   Digital Library under the ACM Open model, with a uniform 12-page proceedings
   budget (9 content pages; references + appendix within 3).

Official basis checked on **2026-07-08**: the KDD 2026 site (32nd SIGKDD conference,
August 9-13, 2026, ICC Jeju, Korea), the Research Track and ADS Track CFPs, the
Datasets & Benchmarks and AI for Sciences track CFPs, the per-track-per-cycle
OpenReview groups, and the ACM Digital Library proceedings record. The exact source
map, including every fact left 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Verified 2026-cycle anchors

| Fact | 2026 value | Volatility |
|---|---|---|
| Edition | 32nd ACM SIGKDD Conference, Aug 9-13, 2026, ICC Jeju, Korea | Per edition |
| Cycles | Cycle 1: abstract 2025-07-24, paper 2025-07-31; Cycle 2: abstract 2026-02-01, paper 2026-02-08 (AoE) | Per cycle |
| Submission format | ACM double-column, `\documentclass[sigconf,anonymous,review]{acmart}`, 8 content pages + refs + optional appendix, double-blind | Per cycle |
| Proceedings budget | 12 pages total: 9 content + up to 3 for references and appendix | Per cycle |
| ADS gate | Quantified post-launch performance required; absence = desk reject | Per cycle |
| Rebuttal | Response per review; **no hyperlinks**; ACs recommend, PC chairs decide | Per cycle |
| Resubmit path | Prior forum id declared + one-page change summary as PDF page 1 | Per cycle |
| Platform | OpenReview, complete profiles for all authors (5-year affiliations, DBLP, ORCID, ...) | Per cycle |
| Publication | ACM DL; ACM Open APC exposure for non-member institutions, 65% ACM subsidy announced for 2026 | Per year |

Notification/camera-ready dates, chair names, fee amounts, and other unverifiable
items are explicitly flagged 待核实 in the source map rather than guessed.

## Skills

Routing and planning:

- [`kdd-topic-selection`](skills/kdd-topic-selection/SKILL.md) — the two-stage
  routing decision: is the work KDD-shaped, and which track (Research vs ADS vs
  Datasets & Benchmarks vs AI for Sciences) matches the strongest honest evidence;
  neighbor routing to ICDM, SDM, WSDM, WWW, VLDB, and the ML flagships.
- [`kdd-workflow`](skills/kdd-workflow/SKILL.md) — the dual-cycle pipeline: cycle
  choice, milestone offsets, rebuttal capacity, the Resubmit loop as a tracked
  contract, and ACM money checks.

Building the paper:

- [`kdd-writing-style`](skills/kdd-writing-style/SKILL.md) — the KDD register:
  data-regime-first framing, mechanism-attached adjectives, dataset-size discipline,
  assertive contribution bullets, ADS lessons-learned voice, 8-page compression.
- [`kdd-related-work`](skills/kdd-related-work/SKILL.md) — lineage positioning
  against prior KDD volumes and sibling venues, venue-misattribution traps, the
  mechanism-contrast novelty sentence, and cross-cycle overlap declarations.
- [`kdd-experiments`](skills/kdd-experiments/SKILL.md) — the four-axis evidence plan
  (quality, scale, efficiency, mechanism), temporal-leakage-safe splits, tuning
  symmetry, ablation matrices, and ADS post-launch measurement design.
- [`kdd-reproducibility`](skills/kdd-reproducibility/SKILL.md) — reproducibility as
  a scored decision factor: the rerunnable/rebuildable/attested tier model, pipeline
  pins, config-as-artifact manifests, and attested-results protocol for production
  numbers.

Packaging and submitting:

- [`kdd-artifact-evaluation`](skills/kdd-artifact-evaluation/SKILL.md) — building
  the anonymized repository that must be cited in the PDF (the no-links rebuttal
  makes it the only reviewer-reachable artifact), scale-claim harnesses, and ADS
  evidence that ships without production data.
- [`kdd-supplementary`](skills/kdd-supplementary/SKILL.md) — the three-container
  split (8 content pages / appendix after references / cited repository), the
  camera-ready 3-page cap trap, and the resubmission change-summary page.
- [`kdd-submission`](skills/kdd-submission/SKILL.md) — the pre-deadline audit:
  track and cycle declaration, all-author OpenReview profile completeness, sigconf
  format, anonymity, ADS desk-check exposure, and the final-week sequence.

Review phase and after:

- [`kdd-review-process`](skills/kdd-review-process/SKILL.md) — the decision
  machinery (reviewers → AC recommendation → PC-chair decision), the
  Accept/Resubmit/Reject outcome game, the mixed academic-practitioner reviewer
  pool, and generative-AI review rules.
- [`kdd-author-response`](skills/kdd-author-response/SKILL.md) — rebuttal under the
  link ban: coordinate-based evidence anchoring, per-reviewer triage bins, and
  playing a lost cycle for a strong Resubmit.
- [`kdd-camera-ready`](skills/kdd-camera-ready/SKILL.md) — page arithmetic
  (9 + 3 within 12), e-rights, TAPS source processing, de-anonymization, ACM Open
  APC status, and Digital Library metadata.

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — every
  official URL with access date, the verified-facts list, and the 待核实 register.
- [`resources/external_tools.md`](resources/external_tools.md) — track CFPs,
  OpenReview groups, ACM DL links, and per-cycle author checks.
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — DOI-verified
  KDD exemplars (XGBoost, node2vec, DeepWalk, metapath2vec, Ad Click Prediction)
  plus the ICDM/NeurIPS/RecSys misattribution guard list.
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  — a fictional before/after rewrite into the KDD first-page arc: data regime →
  mechanism → scale evidence → availability.
- [`resources/code/README.md`](resources/code/README.md) — adapter to the shared
  ML-conference reproducibility kit, with KDD-specific packaging notes.

## Suggested sequence

1. **Route**: `kdd-topic-selection` (track fork first), then `kdd-workflow` (cycle).
2. **Build**: `kdd-experiments` + `kdd-reproducibility` while writing with
   `kdd-writing-style` and `kdd-related-work`.
3. **Package**: `kdd-artifact-evaluation` and `kdd-supplementary` *before* the
   deadline week; then the `kdd-submission` audit.
4. **Respond**: `kdd-review-process` to read the packet, `kdd-author-response` to
   answer it.
5. **Publish or loop**: `kdd-camera-ready` on acceptance; on Resubmit, back to
   `kdd-workflow` with the review contract.

## Installation

The pack ships as a Claude Code plugin. From this repository:

```bash
# add the marketplace rooted at this directory, then install the plugin
claude plugin marketplace add ./KDD-Skills
claude plugin install kdd-skills
```

Or point an agent directly at individual `skills/kdd-*/SKILL.md` files — each skill
is self-contained, states its own scope in the frontmatter description, and ends
with a structured output format so results compose across skills.

## Scope and disclaimers

- This pack advises on **strategy, structure, and evidence** for KDD submissions.
  It is not the CFP: where any statement here conflicts with the current cycle's
  official instructions, the official instructions win, always.
- Facts are dated. Everything specific was checked on 2026-07-08 against the
  sources in the source map; the pack deliberately phrases unstable items
  (deadlines, fees, chairs) as cycle-volatile or 待核实 rather than asserting them.
- No text here should be pasted into a paper. The worked example is fictional by
  design, and the exemplar library records positioning patterns, not reusable prose.

## Maintenance notes

- Every dated fact above is a **2026-cycle anchor, not a rule**. KDD changes cycle
  counts, page budgets, track lineups (two tracks were new in 2026), rebuttal
  mechanics, and ACM Open terms between cycles.
- Before deadline-sensitive advice, reopen the **track-specific** CFP for the
  **named cycle** — "the KDD CFP" is ambiguous at this venue by construction.
- Facts marked 待核实 in the source map (notification dates, chairs, fees) must be
  verified live before being stated to an author as fact.
- If a CFP page and an OpenReview announcement disagree, prefer the newer OpenReview
  instruction or direct chair communication, and record the conflict.
