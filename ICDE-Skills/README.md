# ICDE Skills

Twelve agent skills for research papers at the **IEEE International Conference on Data
Engineering (ICDE)** — the IEEE Computer Society's flagship for data engineering, and the third
corner of the database field's top triangle alongside ACM SIGMOD and VLDB. The pack is built
around what makes ICDE structurally distinct among that triangle: research papers are submitted
in **two fixed rounds per edition** (not SIGMOD's four quarterly rounds, not PVLDB's twelve
monthly ones), reviewed **single-blind** through **Microsoft CMT**, coordinated by an **area
chair** over **at least three reviewers** — in ICDE 2027 with a rebuttal and a straight
**Accept/Reject** decision (the ICDE 2026 **Revise & Resubmit** phase was dropped) — and published as classic conference proceedings in **IEEE Xplore** rather
than in a conference-owned journal.

Official basis checked on **2026-07-09** and **re-verified 2026-11-24**: the ICDE 2027 Call for
Research Papers, its Important Dates page, Submission Guidelines and officers page (read
directly on the live site in November); the ICDE 2026 research call and important-dates page
(history: the two-phase Revise & Resubmit model); the IEEE TCDE Influential Paper Award records
used for exemplar verification; and the IEEE TKDE relationship pages. Exact URLs, dated facts,
the edition status (no ICDE 2028 site or call yet), and the 待核实 ledger live in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Why ICDE needs its own pack

- **Two rounds, and only two.** ICDE 2027 took research papers in Round 1 (June 11, 2026) and
  Round 2 (November 11, 2026; rebuttal January 8-15, notification February 10, 2027), both at
  5:00 PM Pacific Time. A paper rejected in Round 1 is **not** eligible for Round 2 — it waits
  a whole edition (1-year rule). Choosing the
  round is therefore a genuine commitment, not a convenience, and this pack teaches the
  arithmetic.
- **Single-blind, not double-anonymous.** Author names stay on the paper. Every anonymity reflex
  imported from a double-blind venue — scrubbing self-citations, anonymizing the repository — is
  wrong here, and doing it can even confuse a single-blind reviewer.
- **Rebuttal, then a binary verdict.** ICDE 2027 gives each round an author rebuttal and then
  Accept or Reject — "There will be no revisions." ICDE 2026 had run a Revise & Resubmit phase
  with a ~4-week window; the pack keeps that genre as history, because editions change it.
  The evidence has to be complete at submission time.
- **IEEE mechanics, not ACM.** The final paper goes through IEEE eCopyright and PDF-eXpress into
  IEEE Xplore; the format is the IEEE double-column template, 12 pages plus references, no
  appendix (ICDE 2027).
- **The neighborhood is dense.** SIGMOD accepts quarterly into PACMMOD, PVLDB monthly on a rolling
  calendar, EDBT serves the European community, and IEEE TKDE takes journal-length extensions of
  the best ICDE papers. Routing among them, from ICDE's seat, is a recurring decision this pack
  teaches explicitly.

## Skills

| Skill | What it does |
| --- | --- |
| `icde-submission` | Audits a round submission: round eligibility, CMT profiles and conflicts, IEEE 12-page format, single-blind requirements, supplemental-material availability. |
| `icde-author-response` | Drafts the rebuttal (the only response genre in ICDE 2027) and, for editions that offer one, the revise-and-resubmit change document with a per-reviewer requirement ledger. |
| `icde-camera-ready` | Runs the IEEE eCopyright/PDF-eXpress port into Xplore, integrates required changes, final artifact release, registration, and the TKDE extension path. |
| `icde-artifact-evaluation` | Packages code, generators, and logs as availability-scored supplemental material a builder-heavy committee can re-run in minutes. |
| `icde-reproducibility` | Engineers disclosure into the paper: hardware/device/version pinning, seeded generators, variance protocol, baseline-tuning fairness, figure-to-log traceability. |
| `icde-supplementary` | Manages what lives outside the 12 pages: the runnable artifact package, extended sweeps, and single-blind packaging that keeps the body self-contained. |
| `icde-review-process` | Models the two-round pipeline: area-chair coordination, the rebuttal and Accept/Reject decision (R&R in 2026 only), single-blind dynamics, and how builders read an evaluation. |
| `icde-writing-style` | Enforces the first-page data-engineering contract, a reconstructable mechanism, the running-example device, and 12-page IEEE compression. |
| `icde-related-work` | Runs the reinvention audit across the deep DB canon, the venue ring (SIGMOD/VLDB/EDBT), journals, and shipping systems; handles two-round concurrency. |
| `icde-experiments` | Sets the evaluation bar: workload realism, tuned baselines, curves over points, throughput/tail latency with variance, mechanism-isolating ablations, loss disclosure. |
| `icde-workflow` | Plans an edition as a two-round unit: round choice, backward planning, revision-bandwidth reserve, and the price of a Round 1 reject. |
| `icde-topic-selection` | Routes projects: the data-management-primitive test, research vs. industry track, and ICDE vs. SIGMOD/PVLDB/EDBT/TKDE from ICDE's seat. |

## Resources

Beyond the skills, [`resources/`](resources/README.md) carries:

- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —
  a fictional write-optimized-index opening rewritten before → after against the pack's rules.
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — award-anchored real ICDE
  papers (SpatialHadoop, 10-Year award 2025; the Bw-Tree, Ten-Year award 2023; Alibaba PolarDB,
  2024 industry best paper) plus a documented list of famous papers that are *not* ICDE papers.
- [`resources/official-source-map.md`](resources/official-source-map.md) — every verified fact
  with its URL and access date, the access-method note, and the 待核实 ledger.
- [`resources/external_tools.md`](resources/external_tools.md) — live official surfaces and
  do-not-infer rules.
- [`resources/code/README.md`](resources/code/README.md) — the shared artifact smoke-check kit,
  translated into data-systems terms.

## Quick-start scenarios

- **"We missed both ICDE 2027 rounds — what now?"** Start with `icde-workflow`: Round 2 closed
  on November 11, 2026 and no ICDE 2028 call exists yet (checked 2026-11-24), so either plan
  for ICDE 2028 Round 1 once its dates appear or route to SIGMOD 2028 / PVLDB.
- **"Is this an ICDE paper or a SIGMOD/VLDB paper?"** `icde-topic-selection` first, always; the
  scopes overlap almost entirely, so the answer is usually calendar geometry and house culture,
  not topic.
- **"Reviews arrived and the rebuttal window is one week."** `icde-author-response`, rebuttal
  mode (ICDE 2027 Round 2: January 8-15, 2027); there is no revision phase to defer fixes to.
- **"A reviewer says our baseline is untuned."** `icde-experiments`' baseline-fairness protocol,
  then `icde-author-response` to report the tuning budget or the re-run.
- **"Accepted — now what?"** `icde-camera-ready` for the IEEE eCopyright/PDF-eXpress port and the
  Xplore checks, then `icde-artifact-evaluation` before the artifact URL freezes.
- **"We were rejected in Round 1."** It closes the edition: `icde-topic-selection`'s venue table
  (SIGMOD's next quarterly round, PVLDB's monthly gate) plus `icde-review-process` to convert the
  reviews into the rework plan for ICDE 2028 Round 1.

## Verification snapshot (re-verified 2026-11-24)

| Fact | Value | Source |
| --- | --- | --- |
| Publication vehicle | IEEE Xplore conference proceedings | ICDE 2027 call |
| Rounds per edition | Two research rounds | ICDE 2027 important dates |
| ICDE 2027 Round 1 paper deadline | June 11, 2026 (closed) | ICDE 2027 important dates |
| ICDE 2027 Round 2 paper deadline | November 11, 2026 (closed); rebuttal January 8-15, notify February 10, 2027 | ICDE 2027 important dates |
| Deadline clock | 5:00 PM Pacific Time | ICDE 2027 important dates |
| Round 1 reject → Round 2 | Not eligible; waits for ICDE 2028 Round 1 | ICDE 2027 guidelines |
| Review model | Single-blind, area chair + ≥3 reviewers, rebuttal, Accept/Reject only | ICDE 2027 call |
| Revision | None in 2027 (2026 had Revise & Resubmit, ~4-week window) | ICDE 2027 / 2026 calls |
| Page budget | 12 pages + unlimited references, IEEE format, no appendix | ICDE 2027 call |
| Author cap | 5 research papers per author per round | ICDE 2027 call |
| Platform | Microsoft CMT (`cmt3.research.microsoft.com/ICDE2027`), conflicts author-declared | ICDE 2027 call |
| TKDE relationship | Best-paper extension invitation + TKDE Poster track | ICDE 2026 TKDE pages |
| ICDE 2026 | Montréal, Canada, May 4-8, 2026 | icde2026.github.io |
| ICDE 2027 | Copenhagen, Denmark, May 17-21, 2027 | icde2027.github.io |
| ICDE 2028 | Not announced (no site or call as of 2026-11-24) | ieee-icde.org |

## Installation

As a Claude Code plugin (marketplace metadata is included):

```bash
/plugin marketplace add brycewang-stanford/awesome-journal-skills
/plugin install icde-skills
```

Or copy the pack directly into a project:

```bash
cp -r ICDE-Skills/skills/* your-project/.claude/skills/
```

## Layout

```text
ICDE-Skills/
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
    └── icde-*/SKILL.md      # 12 skills
```

## Fact discipline

Every deadline, page count, and policy statement in this pack carries one of two labels:
verified against a named official URL (last re-check 2026-11-24), or explicitly marked 待核实.
The July build's open questions — the ICDE 2027 revision model, Round 1 dates, CMT URL, page
limit and author cap — are now confirmed on the live pages; what remains (ICDE 2028 anything,
an ICDE 2027 reproducibility/badge track, the rebuttal length) sits in the source map's 待核实
section rather than guessed.

## Maintenance notes

- ICDE stands up a new `icdeYYYY.github.io` site each edition and re-declares its round calendar,
  format, and review model; only the two-rounds-per-edition pattern, the single-blind default, the
  CMT platform, the IEEE-Xplore publication model, and the TKDE relationship are safe priors — and
  even they deserve an annual re-read.
- The revision mechanics are exactly the details that drift between editions (ICDE 2026 had
  Revise & Resubmit, ICDE 2027 has none); reopen the live call before advising on revision odds.
- The Round 1 / Round 2 asymmetry — a missed Round 1 costs five months, a Round 1 *reject* costs a
  whole edition — is the sharpest recurring trap; keep it wherever round choice is discussed.
- If the call, important-dates, and guidelines pages conflict, prefer the newest statement, record
  the conflict, and treat program-chair communication as controlling.
- When updating exemplars, follow the library's protocol: an IEEE TCDE award citation or an IEEE
  Xplore record, a second independent confirmation, and exclusion on any disagreement.
