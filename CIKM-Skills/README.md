# CIKM Skills

Twelve agent skills for papers targeting **CIKM — the ACM International Conference on
Information and Knowledge Management** — the venue where information retrieval, data
mining, and knowledge management/databases share one program. The pack is built
around four structural facts that make CIKM strategy its own subject rather than
recycled SIGIR or KDD advice:

1. **A tri-community reviewer pool.** CIKM is co-sponsored by ACM SIGIR (since 1993)
   and SIGWEB (since 2006), and a submission is typically read across three lanes at
   once — IR evaluation culture, mining mechanism culture, and KM/database data-reality
   culture. The pack's core teaching is when that breadth is an asset (two- and
   three-lane papers) and when a specialist venue serves better.
2. **Five tracks, appendices inside every budget.** CIKM 2026 fields Full Research
   (≤10 pages *including* appendices, +2 reference pages), Short (≤4), Applied
   Research (≤7, deployment evidence required), Resource (≤4), and Demonstration (≤4)
   tracks — so "move it to the appendix" saves nothing, and track routing is a
   first-class decision.
3. **An EasyChair form with teeth.** Every track requires nominating an author as a
   reviewer (a stated desk reject if skipped), a declaration of any public
   non-anonymized version (silent arXiv copies risk desk rejection), and a mandatory
   **GenAI Usage Disclosure section** in the PDF covering research, code, data, and
   writing — with automated compliance checks reserved.
4. **The fall slot in the information family's calendar.** May abstract/paper gates,
   August 7 notification, August 20 camera-ready, November conference — which makes
   CIKM the natural next stop for work maturing after SIGIR's January or KDD's
   February gates, and gives accepted authors a thirteen-day ACM
   e-rights/TAPS sprint.

Official basis checked on **2026-07-08**: the CIKM 2026 host site (35th edition,
November 7-11, 2026, Rome, Italy — hosted under a Sapienza University of Rome
domain), its five per-track calls, important-dates and submission-policies pages, the
ACM DL proceedings record for CIKM '25 (DOI 10.1145/3746252), dblp's CIKM index, and
the SIGIR/SIGWEB sponsorship pages. Several official domains were reachable only
through search renderings (gateway-blocked direct fetches); the access-method note,
the full source list, and every fact left 待核实 are in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Verified 2026-cycle anchors

| Fact | 2026 value | Volatility |
|---|---|---|
| Edition | 35th CIKM, November 7-11, 2026, Rome, Italy | Per edition |
| Full Research | ≤10 pages incl. figures/tables/**appendices** + ≤2 pages references; double-blind | Per cycle |
| Short Research | ≤4 pages incl. appendix | Per cycle |
| Applied Research | ≤7 pages; launch/data-release evidence required | Per cycle |
| Resource / Demo | ≤4 pages each; demos enter main proceedings | Per cycle |
| Dates | Full: abstract May 16, paper May 23; short/resource/demo: May 30 / June 6; notify Aug 7; camera-ready Aug 20 (all AoE) | Per cycle |
| Platform | EasyChair, one named track selection per paper | Per cycle |
| Form obligations | Author-reviewer nomination (desk reject if missing); arXiv-version declaration | Per cycle |
| GenAI policy | Mandatory uncounted "GenAI Usage Disclosure" section; ACM AI policy; no AI-written reviews | Per cycle |
| Dual submission | Concurrent submission to any conference/journal prohibited; authorship frozen at abstract gate | Per cycle |
| Publication | ACM Digital Library via e-rights + TAPS | Per year |

As of the check date every 2026 submission gate has passed — the pack teaches the
**live post-submission phases** (review wait, notification, the 13-day camera-ready
window, Rome logistics) plus CIKM 2027 planning. A possible 2026 rebuttal phase,
chair names, camera-ready page allowances, fees, and 2027 facts could not be
verified and are flagged 待核实 rather than asserted.

## Skills

Routing and planning:

- [`cikm-topic-selection`](skills/cikm-topic-selection/SKILL.md) — the lane-count
  test (how many of IR/mining/KM the paper truly occupies), honest fall-venue
  positioning vs. SIGIR/KDD/WSDM/TheWebConf/SIGMOD/ISWC, and the five-track fork.
- [`cikm-workflow`](skills/cikm-workflow/SKILL.md) — the May→November year, the two
  live modes (under-review wait vs. next-edition build), the abstract-gate
  authorship freeze, multi-track coordination, and the fallback ring.

Building the paper:

- [`cikm-writing-style`](skills/cikm-writing-style/SKILL.md) — the tri-lane first
  page (problem → boundary → named mechanism → calibrated evidence), cross-lane
  vocabulary pinning, and appendix-inclusive compression.
- [`cikm-related-work`](skills/cikm-related-work/SKILL.md) — three-front coverage,
  the boundary-work paragraph, CIKM back-catalog fluency, and the misattribution
  guard (DeepWalk/SASRec/NGCF/Conv-KNRM/TransE are *not* CIKM papers).
- [`cikm-experiments`](skills/cikm-experiments/SKILL.md) — the claim-lane-evidence
  contract, datasets that satisfy a blended panel, mechanism-isolating ablations,
  and the Applied-track deployment-evidence bar.
- [`cikm-reproducibility`](skills/cikm-reproducibility/SKILL.md) — the
  divergence map for chained pipelines (index/KG/model/eval), unreleasable-data
  honesty patterns, and GenAI disclosure as a methods record.

Submitting:

- [`cikm-submission`](skills/cikm-submission/SKILL.md) — the per-track budget card,
  the three EasyChair form gates, the GenAI-disclosure section, anonymity sweep,
  and the desk-reject ledger.
- [`cikm-supplementary`](skills/cikm-supplementary/SKILL.md) — the three-container
  split (costed appendix vs. anonymous artifact vs. cut) under budgets with no
  appendix escape, and what the uncounted sections may not carry.
- [`cikm-artifact-evaluation`](skills/cikm-artifact-evaluation/SKILL.md) — artifact
  roles per track, the Resource-track adoption bar, KG snapshot packaging, demo
  survival kits, and anonymous-to-public staging.

Review to publication:

- [`cikm-review-process`](skills/cikm-review-process/SKILL.md) — the blended-pool
  effect, per-track criteria shifts, what moves borderlines, and timeline realism
  for the live cycle.
- [`cikm-author-response`](skills/cikm-author-response/SKILL.md) — the four
  author-side writing situations (window/no-window × accept/reject), tri-lane reply
  structure, and the concern → edit ledger.
- [`cikm-camera-ready`](skills/cikm-camera-ready/SKILL.md) — the thirteen-day
  sequence through e-rights and TAPS, de-anonymization beyond adding names, CCS/dblp
  metadata care, GenAI-section retention, and the parallel Rome logistics strand.

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — every
  verified fact with URL + access date; every gap marked 待核实.
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — six
  dblp-verified CIKM landmarks (TAGME 2010 → BERT4Rec 2019) covering all lane
  combinations, plus the checked sibling-venue traps.
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  — a fictional before → after rewrite into the tri-lane register.
- [`resources/external_tools.md`](resources/external_tools.md) — live official
  surfaces and what to re-check on each.
- [`resources/code/README.md`](resources/code/README.md) — the shared
  ML-conference reproducibility kit, with CIKM-specific checks the kit lacks.

## How to use the pack

Typical entry points by situation:

| You are... | Start with | Then |
|---|---|---|
| Deciding where a boundary paper goes | `cikm-topic-selection` | `cikm-workflow` for the calendar math |
| Holding a CIKM 2026 submission (live cycle) | `cikm-workflow` Mode A | `cikm-camera-ready` prep + `cikm-author-response` ledger |
| Drafting for the next edition | `cikm-writing-style` + worked example | `cikm-experiments`, `cikm-related-work` |
| One week from a deadline | `cikm-submission` | `cikm-supplementary` for the split decisions |
| Building a resource or demo | `cikm-artifact-evaluation` | `cikm-submission` for that track's budget card |
| Just rejected | `cikm-author-response` (resubmission brief) | `cikm-workflow` fallback ring |

Each skill ends with an output format block so agent runs produce comparable,
decision-ready summaries rather than open-ended prose.

## Repository layout

```text
CIKM-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skill paths)
├── assets/cover.svg
├── resources/
│   ├── official-source-map.md    # verified facts + 待核实 ledger
│   ├── external_tools.md         # live official surfaces
│   ├── exemplars/library.md      # six dblp-verified CIKM landmarks
│   ├── worked-examples/01-introduction.md
│   └── code/README.md            # shared reproducibility kit pointer
└── skills/cikm-*/SKILL.md        # the twelve skills
```

## Maintenance notes

- CIKM's site moves to a new host domain every year; never trust last year's URLs
  or rules. Start from the series page or a fresh search for the current edition.
- Everything in the anchors table is one host-committee decision from changing:
  track lineup, budgets, platform (EasyChair today), disclosure wording, and the
  nomination rule.
- The 2026 facts in this pack are dated anchors for reasoning, not standing policy.
  When an official page and this pack disagree, the page wins — update the source
  map with a new access date.
