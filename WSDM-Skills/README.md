# WSDM Skills

Twelve agent skills for papers targeting **WSDM - the ACM International Conference
on Web Search and Data Mining** (pronounced "wisdom"), the small, highly selective,
traditionally single-track winter venue for search and data mining on the Web and
the Social Web, jointly sponsored by ACM SIGIR, SIGKDD, SIGMOD, and SIGWEB. The
pack is organized around the four structural facts that make WSDM strategy unlike
its bigger siblings:

1. **One deadline a year, and no rebuttal.** Papers go in each August (via
   EasyChair in recent editions) and decisions arrive about ten weeks later with
   no author-response phase in between - a practice documented at this venue since
   at least 2017. The submitted PDF is the entire case, so this pack treats
   "preemptive rebuttal" as a writing discipline, not a metaphor.
2. **Appendices live inside the page cap.** The 2026 rule was 9 pages including
   diagrams, tables, *and appendices*, with uncounted space only for references
   and a required ethical-considerations section (2025: 8 pages + 2 shared by
   references and ethics). There is no unlimited appendix and no verified
   supplementary upload - the cited anonymous repository is the only overflow.
3. **Hybrid blinding with an experimental rationale.** Reviewing is double-blind
   at the PC/senior-PC level while Associate Chairs see authorship metadata for
   conflict checking - a design shaped by the controlled single-blind vs
   double-blind experiment run at WSDM 2017 and published in PNAS.
4. **A "practical yet principled" evidence culture.** The PC blends academic IR/
   mining researchers with industry search/recommendation/ads scientists;
   winning papers pair behavioral grounding and bias-aware evaluation with
   deployment realism, at roughly one-in-six selectivity (2025: >100 accepted of
   >600 submissions).

Official basis checked on **2026-07-08**: the WSDM 2026 site and long/short-paper
CFPs (19th edition, Boise, Idaho, February 22-26, 2026), the WSDM 2025 CFP and
SIGWEB conference report (18th, Hannover), the live WSDM 2027 site (20th, Hong
Kong, February 15-19, 2027), ACM Digital Library proceedings records, dblp, and
the conference's official announcements. Direct fetches of several official
domains were gateway-blocked at check time; the exact verification method, every
source URL, and all 待核实 items are in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Verified anchors

| Fact | Verified value | Volatility |
|---|---|---|
| Editions | 2025: 18th, Hannover, Mar 10-14 · 2026: 19th, Boise, Feb 22-26 · 2027: 20th, Hong Kong, Feb 15-19 | Per edition |
| 2026 deadlines | Abstract 2025-08-07, paper 2025-08-14 (AoE), EasyChair; notification listed 2025-10-23 | Per edition |
| 2026 page budget | ≤9 pages incl. appendices; references + ethics section uncounted | Per edition |
| Format | ACM `acmart`; 2025 CFP documented `[sigconf,anonymous,review]` | Per edition |
| Blinding | Anonymized PDFs; double-blind to PC/SPC; ACs see metadata for COI | Per edition |
| Review load | ≥3 PC reviews + senior PC per paper; no rebuttal historically | Per edition |
| Ethics section | Required, uncounted, societal-impact + mitigations | Per edition |
| Short papers | New track in 2026, September deadlines, 10-submission cap | Per edition |
| Selectivity | 2025: >100 of >600 (~16-17%) | Per edition |
| Proceedings | ACM DL (WSDM '26 DOI 10.1145/3773966); sponsors SIGIR/SIGKDD/SIGMOD/SIGWEB | Stable-ish |

WSDM 2027 CFP deadlines, camera-ready rules, fees, and chair names could not be
verified at check time and are flagged 待核实 in the source map, never guessed.

## Skills

Routing and planning:

- [`wsdm-topic-selection`](skills/wsdm-topic-selection/SKILL.md) - the two-gate
  test (web/social data as the object of study; practical *and* principled),
  2026-CFP scope areas including "Search with Foundation Models," and routing
  against SIGIR, KDD, WWW, CIKM, RecSys, and ICWSM.
- [`wsdm-workflow`](skills/wsdm-workflow/SKILL.md) - the single annual cycle:
  backward milestones from the August deadline, the September short-paper
  pressure valve, alternate entrances (demo, WSDM Cup, doctoral consortium,
  Industry Day), and the sibling-venue rejection chain.

Building the paper:

- [`wsdm-writing-style`](skills/wsdm-writing-style/SKILL.md) - behavior-first
  openings, the self-containment voice for a no-rebuttal review, WSDM-specific
  sentence tells, ethics-section craft, and single-track-audience clarity.
- [`wsdm-related-work`](skills/wsdm-related-work/SKILL.md) - joining a WSDM
  lineage (click models, unbiased LTR, sequential recommendation, off-policy RL
  for rec, community detection), mechanism-level contrast sentences, and
  dblp-verified venue attribution.
- [`wsdm-experiments`](skills/wsdm-experiments/SKILL.md) - the four evidence
  quadrants, temporal splits and candidate-set regimes, baseline recency and
  tuning parity, mechanism-isolating ablations, and attested online evidence.
- [`wsdm-reproducibility`](skills/wsdm-reproducibility/SKILL.md) - behavioral-
  data provenance, split manifests, named bias models, seed/variance discipline,
  and the rerunnable/rebuildable/attested honesty ladder for log-driven work.

Packaging and submitting:

- [`wsdm-artifact-evaluation`](skills/wsdm-artifact-evaluation/SKILL.md) - the
  ten-minute reviewer-facing repository, the proprietary-log release ladder,
  public-benchmark mirrors, WSDM Cup datasets, and foundation-model pinning.
- [`wsdm-supplementary`](skills/wsdm-supplementary/SKILL.md) - triage across the
  9-page-inclusive body, uncounted references/ethics, and the cited repository;
  compression tactics and the budget worksheet.
- [`wsdm-submission`](skills/wsdm-submission/SKILL.md) - the abstract-then-paper
  week, page-budget arithmetic, anonymization under hybrid blinding, and the
  desk-level exposure table.

Review phase and after:

- [`wsdm-review-process`](skills/wsdm-review-process/SKILL.md) - the pipeline
  from bidding to October notification, who sees what and why (the 2017 PNAS
  experiment), reviewer-pool reading, and selectivity arithmetic.
- [`wsdm-author-response`](skills/wsdm-author-response/SKILL.md) - author
  communication at a venue with no rebuttal: the objection-inventory method,
  narrow legitimate chair contacts, and the post-decision fork.
- [`wsdm-camera-ready`](skills/wsdm-camera-ready/SKILL.md) - ACM e-rights before
  editing, TAPS-style production, CCS concepts, de-anonymization as an editing
  pass, and February presentation logistics.

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) - all
  eleven sources with access dates, the access-method disclosure for blocked
  domains, verified-facts list, and the 待核实 register.
- [`resources/external_tools.md`](resources/external_tools.md) - official sites,
  EasyChair note, ACM DL/dblp links, and the per-cycle re-check list.
- [`resources/exemplars/library.md`](resources/exemplars/library.md) - five
  DOI-verified WSDM papers (Craswell 2008, Yang & Leskovec 2013, Joachims 2017,
  Tang & Wang 2018, Chen 2019) plus a misattribution guard list.
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  - a fictional before/after rewrite into the WSDM register, ending with the
  no-rebuttal move: the strongest objection becomes Section 3.
- [`resources/code/README.md`](resources/code/README.md) - adapter to the shared
  ML-conference reproducibility kit with WSDM-specific caveats.

## Suggested sequence

1. **Route**: `wsdm-topic-selection`, then `wsdm-workflow` to lay the annual
   clock and the rejection chain.
2. **Build**: `wsdm-experiments` + `wsdm-reproducibility` for evidence;
   `wsdm-writing-style` + `wsdm-related-work` for the text.
3. **Package**: `wsdm-artifact-evaluation` and `wsdm-supplementary` well before
   deadline week; `wsdm-submission` as the final audit.
4. **Wait wisely**: `wsdm-review-process` to model what is happening;
   `wsdm-author-response` beforehand, since its work happens pre-deadline here.
5. **Publish**: `wsdm-camera-ready` on acceptance; on rejection, execute the
   pre-mapped chain from `wsdm-workflow`.

## Installation

The pack ships as a Claude Code plugin. From this repository:

```bash
claude plugin marketplace add ./WSDM-Skills
claude plugin install wsdm-skills
```

Individual `skills/wsdm-*/SKILL.md` files also work standalone - each declares
its trigger scope in frontmatter and ends with a structured output block so
results compose.

## Scope and disclaimers

- This pack advises on strategy, evidence, and writing for WSDM submissions. It
  is not the CFP; where anything here conflicts with the current edition's
  official instructions, the official instructions win.
- Every dated fact is an edition anchor checked on 2026-07-08, not a rule. Items
  that could not be verified are marked 待核实 in the source map rather than
  asserted.
- The worked example is fictional and the exemplar library records positioning
  patterns; neither contains prose to paste into a manuscript.

## Maintenance notes

- Re-verify before each August: deadlines, page budget and what counts inside
  it, the EasyChair instance, ethics-section wording, and any new short-paper or
  AI-policy rules - all changed at least once between 2025 and 2026.
- The 2027 cycle was live but unreadable through the verification gateway at
  check time; its CFP pages are the first thing to re-open.
- Add two recent-edition exemplars (with DOIs) to the library each year.
- 中文版见 [`README.zh-CN.md`](README.zh-CN.md); keep both READMEs in sync when
  facts change.
