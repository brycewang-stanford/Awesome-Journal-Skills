# SIGMOD Skills

Twelve agent skills for research papers at the ACM SIGMOD International Conference on
Management of Data — the ACM flagship for database systems and data management. The pack
is built around what makes SIGMOD structurally unusual among CS conferences: research
papers are **journal submissions to PACMMOD** (Proceedings of the ACM on Management of
Data), reviewed in **four rounds per year** with genuine major/minor **revision verdicts**,
a **12-month embargo** after rejection, and a flagship artifact program — the
**Availability & Reproducibility Initiative (ARI)** — whose badges are embedded into the
published PDF.

Official basis checked on **2026-07-08**: the SIGMOD 2027 Call for Research Papers and
important-dates calendar, the PACMMOD author guidelines, the ARI pages at
`reproducibility.sigmod.org`, the SIGMOD 2026 conference site, and the sigmod.org awards
pages used for exemplar verification. Exact URLs, verified facts, and the 待核实 ledger
live in [`resources/official-source-map.md`](resources/official-source-map.md). Note the
access caveat recorded there: several official hosts reject automated fetches, so facts
were verified through search renderings of the exact URLs and cross-checked across
independent official pages.

## Why SIGMOD needs its own pack

- **Round-hopping replaces the annual deadline.** SIGMOD 2027 takes papers on
  Jan 17 / Apr 17 / Jul 17 / Oct 17, 2026 (abstract + conflict declarations one week
  earlier, all 11:59 PM AoE), each round feeding its own PACMMOD issue. Choosing the
  round — and pricing the embargo if you lose it — is a strategic skill in itself.
- **Revision is a first-class outcome.** A major/minor-revision verdict grants one extra
  content page and one month, and demands a four-page letter with per-reviewer color
  highlighting. That genre barely exists at other CS venues.
- **Reviewing is double-anonymous for months**, spanning feedback phases and revisions,
  which changes how artifacts, preprints, and repositories must be handled.
- **Reproducibility is institutionalized.** PACMMOD expects code, data, scripts, and
  notebooks to be shared; ARI evaluates artifacts post-acceptance for the Artifacts
  Available / Artifacts Evaluated / Results Reproduced badge ladder, and confers a Best
  Artifact award.
- **The neighborhood is dense.** PVLDB accepts monthly on a rolling basis, PODS takes the
  theory, ICDE the broader engineering, KDD the mining, TODS the journal-length
  extensions. Routing among them is a recurring decision this pack teaches explicitly.

## Skills

| Skill | What it does |
| --- | --- |
| `sigmod-submission` | Audits a round submission: abstract+COI pre-deadline, CMT, 12-page ACM template, anonymity, the 10-paper cap, embargo-aware round choice. |
| `sigmod-author-response` | Drafts both author turns: the mid-round feedback reply and the four-page revision letter with per-reviewer highlighting. |
| `sigmod-camera-ready` | Runs the PACMMOD-format port, de-anonymization, per-round issue placement, ACM DL metadata, and conference-presentation logistics. |
| `sigmod-artifact-evaluation` | Prepares ARI participation: HotCRP registration, the badge ladder, evaluator criteria, hardware honesty, Best Artifact positioning. |
| `sigmod-reproducibility` | Engineers provenance into the paper: config/data/workload/hardware pinning, variance floors, baseline fairness, the repro-debt ledger. |
| `sigmod-supplementary` | Manages what lives outside the 12 pages: extended reports, anonymous frozen repositories, multi-round hosting hygiene. |
| `sigmod-review-process` | Models the round pipeline: feedback phase, three-valued verdicts, the one-month revision, the embargo, and how a builder-heavy PC reads. |
| `sigmod-writing-style` | Enforces the page-one contract, the running-example device, scoped systems claims, and the 12-page budget. |
| `sigmod-related-work` | Covers the five literature lines, deep-history diligence against reinvention, rolling-venue concurrency, and overlap rules. |
| `sigmod-experiments` | Sets the evaluation bar: workload realism ladder, tuned baselines, curves over points, mechanism-isolating ablations, loss disclosure. |
| `sigmod-workflow` | Plans the round as a five-act unit: backward planning, revision bandwidth, portfolio constraints, the pre-agreed reject plan. |
| `sigmod-topic-selection` | Routes projects: research vs. industrial track, SIGMOD vs. PVLDB/PODS/ICDE/KDD/CIDR/TODS, the data-management-primitive test. |

## Resources

Beyond the skills, [`resources/`](resources/README.md) carries:

- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —
  a fictional storage-engine opening rewritten before → after against the pack's rules.
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — award-anchored real
  SIGMOD papers (Selinger 1979; Online Aggregation, ToT 2007; PrivBayes, ToT 2024;
  k-Shape, ToT 2025; PolarDB-MP, 2024 industry best paper) plus a documented list of famous
  papers that are *not* SIGMOD papers.
- [`resources/official-source-map.md`](resources/official-source-map.md) — every verified
  fact with its URL and access date, the access-method note, and the 待核实 ledger.
- [`resources/external_tools.md`](resources/external_tools.md) — live official surfaces and
  do-not-infer rules.
- [`resources/code/README.md`](resources/code/README.md) — the shared artifact smoke-check
  kit, translated into data-systems terms.

## Quick-start scenarios

- **"We have a working system and want the July round."** Start with
  `sigmod-workflow` (backward plan, bandwidth check), then `sigmod-experiments` and
  `sigmod-reproducibility` to close evaluation debt, then `sigmod-submission` in the final
  two weeks.
- **"Reviews arrived and one reviewer misread Figure 7."** `sigmod-author-response`,
  feedback-phase mode — correct facts with pointers, no promises.
- **"We got a major revision with six requirements."** `sigmod-author-response`,
  revision-letter mode, plus `sigmod-experiments` for any demanded runs; check the
  one-month feasibility honestly before committing.
- **"Accepted — now what?"** `sigmod-camera-ready` for the PACMMOD port and
  de-anonymization, then `sigmod-artifact-evaluation` for the ARI badge push.
- **"Is this even a SIGMOD paper?"** `sigmod-topic-selection` first, always; half of
  review pain is routing error.
- **"We were rejected in Round 2."** The embargo closes the track for about three rounds:
  `sigmod-topic-selection`'s venue-race table (PVLDB's monthly gate, ICDE, TODS) plus
  `sigmod-review-process` to convert the reviews into the rework plan.

## Verification snapshot (2026-07-08)

| Fact | Value | Source |
| --- | --- | --- |
| Publication vehicle | PACMMOD issues, one per round | 2027 CFP, PACMMOD pages |
| SIGMOD 2027 round deadlines | Jan 17 / Apr 17 / Jul 17 / Oct 17, 2026 (AoE) | 2027 important dates |
| Page budget | 12 pages + unlimited references, ACM template | 2027 CFP |
| Platform | Microsoft CMT | 2027 CFP |
| Revision terms | +1 page, ≤4-page letter, per-reviewer colors | 2027 CFP |
| Rejection embargo | 12 months (late withdrawal counts) | 2027 CFP |
| Author cap | 10 research submissions per cycle | 2027 CFP |
| ARI badges | Available / Evaluated / Results Reproduced | reproducibility.sigmod.org |
| SIGMOD 2026 | Bengaluru, May 31 - June 5, 2026 | 2026.sigmod.org |
| SIGMOD 2027 | Huntington Beach, June 13-19, 2027 | 2027.sigmod.org |

## Installation

As a Claude Code plugin (marketplace metadata is included):

```bash
/plugin marketplace add brycewang-stanford/awesome-journal-skills
/plugin install sigmod-skills
```

Or copy the pack directly into a project:

```bash
cp -r SIGMOD-Skills/skills/* your-project/.claude/skills/
```

## Layout

```text
SIGMOD-Skills/
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
    └── sigmod-*/SKILL.md    # 12 skills
```

## Fact discipline

Every deadline, page count, and policy statement in this pack carries one of two labels:
verified against a named official URL on 2026-07-08, or explicitly marked 待核实. Items
known to be unverifiable at build time — the SIGMOD 2027 industrial-track calendar, the
current CMT site URL, ARI 2027 logistics, PACMMOD fee mechanics, in-PDF appendix
permission — are listed in the source map's 待核实 section rather than guessed.

## Maintenance notes

- The SIGMOD 2027 round calendar quoted throughout is a dated observation; future cycles
  republish dates, and only the quarterly pattern should be assumed durable.
- Revision mechanics (extra page, letter length, highlighting rules), the author cap, and
  embargo wording are re-declared each cycle — reopen the live CFP before advising.
- ARI edition logistics (registration site, dates, hardware support) change yearly.
- If official pages conflict, prefer the newest statement, record the conflict, and treat
  chair communication as controlling.
- When updating exemplars, follow the library's verification protocol: award citation or
  ACM DL record, two independent confirmations, exclude on any disagreement.
