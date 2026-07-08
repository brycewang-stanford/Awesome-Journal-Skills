# VLDB Skills

Twelve agent skills for research papers at the International Conference on Very Large
Data Bases (VLDB) and its publication vehicle, PVLDB (Proceedings of the VLDB
Endowment). VLDB is one of the two flagship database venues, and it is structurally
unlike almost every other CS conference: there is no annual deadline. Research papers
are submitted to a PVLDB volume on a **rolling monthly calendar** — a deadline on the
1st of every month, twelve chances a year — with journal-style **accept / revise /
reject** outcomes, a one-shot revision with a three-month window, and publication in
monthly issues months before the conference itself convenes.

Official basis checked on **2026-07-08**: the PVLDB Volume 20 submission guidelines,
the VLDB 2027 research-track call, the PVLDB Volume 19 guidelines and VLDB 2026
research-track call, the VLDB 2026/2027 conference sites, the pVLDB reproducibility
pages, and VLDB Endowment award records used for exemplar verification. Exact URLs,
dated facts, and the 待核实 ledger live in
[`resources/official-source-map.md`](resources/official-source-map.md). Note the
access-method caveat recorded there: `vldb.org`, `dl.acm.org`, and `dblp.org` refused
direct automated fetches, so page contents were verified through search renderings of
the exact URLs and cross-checked across independent official and institutional pages.

## The PVLDB model in one paragraph

You register an abstract by the **25th** of a month, submit the paper by the **1st**
of the next month at **5:00 PM Pacific Time** (not AoE — mind the conversion), and
receive reviews with a verdict around the **15th** of the month after that. A *revise*
verdict grants up to **three months** for exactly **one** revision, re-judged by the
same reviewers against their explicit required-changes list. Accepted papers publish
in the volume's monthly issues, and papers accepted by the volume's cutoff (June 15,
2026 for Vol 19) present at the matching conference. On the build date the live volume
is **Vol 20** (first deadline April 1, 2026; final deadline March 1, 2027), feeding
**VLDB 2027 in Athens, August 23-27, 2027**; VLDB 2026 meets in **Boston, August 31 -
September 4, 2026** on Vol 19's papers.

## Where this pack spends its depth

- **Month-picking as arithmetic.** With twelve deadlines a year, the strategic skill
  is computing the right month backward — from the conference cutoff, the review
  latency, and the three-month revision runway — instead of submitting whatever
  exists on the nearest 1st. `vldb-workflow` teaches the computation.
- **The revision as the author-response genre.** PVLDB has no rebuttal: reviews and
  verdict arrive together, so your one conversation with reviewers is the revision
  package. `vldb-author-response` builds the requirement ledger and change document.
- **Single-blind candor.** Author names stay on the paper, extended technical reports
  go on arXiv under your name, and self-citation is direct — the inverse of the
  double-anonymous venues nearby (reconfirm on the live guidelines; see 待核实).
- **Reproducibility with teeth.** Artifact availability earns an ACM badge, the pVLDB
  Reproducibility Evaluation reruns experiments, EA&B papers *must* participate, and
  a Best Reproducible Paper Award exists. Two skills cover the engineering and the
  packaging sides.
- **Scalable-systems evidence culture.** Throughput and tail latency with declared
  variance, scale curves rather than single points, tuned competitors, and a
  mandatory loss map — the evaluation bar `vldb-experiments` enforces.

## Skills

- `vldb-submission` - audit a monthly cycle: the 25th abstract gate, CMT window,
  5:00 PM PT cutoff, category budgets, single-blind cover page, author caps.
- `vldb-author-response` - turn a revise verdict into a requirement ledger, a
  three-month plan, and a change document the same reviewers accept.
- `vldb-camera-ready` - produce the PVLDB issue version: volume template, PDF/A and
  font embedding, availability paragraph, naming/copyright steps, conference leg.
- `vldb-artifact-evaluation` - package the four artifact surfaces for the pVLDB
  Reproducibility Evaluation and position for badge and award.
- `vldb-reproducibility` - engineer disclosure into the paper: hardware/software/
  data/workload floors, systems-variance protocol, competitor fairness ledger,
  figure-to-raw-data traceability.
- `vldb-supplementary` - manage what lives outside the page budget, where appendices
  count against the limit: the extended TR, the tagged repository, self-containment.
- `vldb-review-process` - model the rolling pipeline: six-week turnaround, the
  three-outcome space, one-shot revision odds, the standing review board.
- `vldb-writing-style` - enforce the page-one contract, scoped performance claims,
  trade-off candor, and terminology discipline across 12 pages.
- `vldb-related-work` - run the reinvention audit across the deep canon, the venue
  ring, and shipping systems; handle rolling-calendar concurrency and overlap.
- `vldb-experiments` - carry the four evidence burdens: problem exists, mechanism
  causes the gain, gain survives scale, cost is known.
- `vldb-workflow` - compute the submission month, plan one cycle backward from the
  1st, schedule revision bandwidth, manage group caps.
- `vldb-topic-selection` - apply the data-management-primitive test, choose among
  Regular/EA&B/Scalable Data Science/Vision, route against SIGMOD, PODS, ICDE, CIDR,
  EDBT, KDD, systems venues, and The VLDB Journal.

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — every
  verified fact with URL and access date, the access-method note, and the 待核实
  ledger.
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — four
  award-anchored real papers: the Test-of-Time 2025 query-optimizer study (Leis et
  al., PVLDB 2015), C-Store (VLDB 2005), Hadoop-GIS (ToT 2024), and TiDB (PVLDB
  2020) — plus the famous papers that are *not* VLDB papers.
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  — a fictional LSM-store paper's first page rewritten before → after.
- [`resources/external_tools.md`](resources/external_tools.md) — live official
  surfaces and do-not-infer rules.
- [`resources/code/README.md`](resources/code/README.md) — the shared artifact
  smoke-check kit, read with systems eyes.

## Typical entry points

- **"Which month do we submit?"** → `vldb-workflow`. If you want Athens 2027 with a
  revision-proof path, the arithmetic starts about six months before the cutoff.
- **"Is this a VLDB paper or a SIGMOD paper?"** → `vldb-topic-selection`; the scopes
  overlap almost entirely, so the answer is usually calendar geometry and category
  fit, not topic.
- **"We got a revise with five required changes."** → `vldb-author-response`, then
  `vldb-experiments` for the demanded runs. Check three-month feasibility before
  celebrating.
- **"The abstract deadline is the 25th — are we ready?"** → `vldb-submission`'s
  audit sequence, two weeks out.
- **"Accepted — what breaks now?"** → `vldb-camera-ready` (PDF/A bites late), then
  `vldb-artifact-evaluation` before the artifact URL freezes.
- **"Reviewers will ask why we didn't compare against X."** → `vldb-related-work`'s
  reinvention audit and `vldb-experiments`' baseline fairness protocol, pre-emptively.

## Installation

As a Claude Code plugin (marketplace metadata included):

```bash
/plugin marketplace add brycewang-stanford/awesome-journal-skills
/plugin install vldb-skills
```

Or copy the skills straight into a project:

```bash
cp -r VLDB-Skills/skills/* your-project/.claude/skills/
```

## Layout

```text
VLDB-Skills/
├── .claude-plugin/          # plugin.json + marketplace.json (12 skills registered)
├── assets/cover.svg
├── resources/
│   ├── README.md
│   ├── official-source-map.md
│   ├── external_tools.md
│   ├── exemplars/library.md
│   ├── worked-examples/01-introduction.md
│   └── code/README.md
└── skills/
    └── vldb-*/SKILL.md      # 12 skills
```

## Fact discipline

Every date, page count, cap, and policy in this pack is either tied to a named URL
checked on 2026-07-08 or explicitly marked 待核实. The deliberately-unguessed items —
the exact single-blind wording on the live Vol 20 page, any post-rejection embargo,
Vol 20 camera-ready mechanics, demo/tutorial budgets, the Vol 20 conference cutoff
date, officer names on the official page — are listed in the source map's 待核实
section.

## Maintenance notes

- PVLDB republishes everything per volume: deadlines, caps, categories, budgets,
  template, and officers reset annually. Only the rolling monthly pattern itself is
  a safe prior, and even it deserves an annual re-read.
- The 5:00 PM Pacific clock is this venue's sharpest recurring trap for non-US
  authors; keep the conversion warning wherever dates are quoted.
- When VLDB 2027 concludes, re-anchor the pack on Vol 21 and refresh the exemplars
  against the newest Test-of-Time citations using the library's two-source rule.
- If official pages disagree, prefer the newer volume's statement, record the
  conflict, and treat word from the PVLDB Editors-in-Chief as controlling.
