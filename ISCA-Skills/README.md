# ISCA Skills

Twelve agent skills for papers targeting **ISCA — the ACM/IEEE International
Symposium on Computer Architecture**, the flagship venue of the computer-
architecture community, co-sponsored by ACM SIGARCH and IEEE-CS TCCA. The pack
covers the whole campaign: testing whether the machine itself is the
contribution, building simulation-grade evidence with a declared fidelity
contract, clearing the November abstract-and-paper gate on HotCRP, working the
two-round review and its combined rebuttal/revision window, and converting
acceptance into a badged, artifact-backed publication presented in late June.

Official basis checked on **2026-07-08**: the ISCA 2026 conference site
(home, Call for Papers, submission guidelines, artifact evaluation), the SIGARCH
and IEEE-TCCA postings of the 2026 call, the ISCA 2026 HotCRP portal, the
ACM DL / dblp records for the 52nd edition (Tokyo 2025), and the SIGARCH
Influential ISCA Paper Award page. The verification gateway returned 403 for
direct fetches of `iscaconf.org`, `sigarch.org`, `ieeetcca.org`, `dl.acm.org`,
and `dblp.org`, so official pages were read through search-engine renderings of
those exact URLs and cross-checked against one another; the full trail —
including everything still marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Where the cycle stands (as of 2026-07-08)

ISCA 2026, the 53rd edition, concluded on July 1, 2026 in Raleigh, North
Carolina. The live target is **ISCA 2027** — reported (via the ACM DL
conference hub) for Atlanta, GA, June 5-9, 2027, though its CFP was not yet
posted at check time. Recent cycles put the abstract deadline in mid-November
of the prior year (November 10, 2025 for ISCA 2026), so a mid-to-late November
2026 gate is the planning assumption — explicitly 待核实 until
`iscaconf.org/isca2027/` goes live.

## What makes ISCA distinctive among its siblings

Verified 2026-cycle mechanics that drive the advice in these skills:

- **Dual sponsorship, alternating publisher.** ACM SIGARCH and IEEE-CS TCCA
  jointly run ISCA; the 52nd edition's proceedings were ACM-published while the
  2026 edition carried IEEE branding and an IEEE-flavored template. Search
  across dblp (not one publisher's library), and re-identify the publisher
  workflow at every camera-ready.
- **The June flagship seat.** ISCA anchors the architecture year: November
  deadline → June conference, with MICRO (spring deadline → October), HPCA
  (summer → February), and ASPLOS (multiple gates) as retargeting seats.
- **Two deadlines a week apart.** Abstracts November 10, papers November 17
  (2025, for the 2026 edition) — the abstract step steers reviewer assignment
  and is a decisions deadline, not a formality.
- **11 pages of text, unlimited references.** Never trim the bibliography for
  space at a venue with a 50-year memory.
- **Two review rounds plus a rebuttal/revision window.** Round 1 reviews
  December, Round 2 February, then three weeks (February 16 - March 6, 2026)
  in which authors could both argue and *change the paper* — a window teams
  must staff like a sprint.
- **Double-blind with a twist.** No names outside the HotCRP form, scrubbed
  PDF metadata, fully anonymized artifact links — but references must **never**
  be anonymized or omitted.
- **Voluntary post-acceptance artifact evaluation** under the ACM Artifact
  Review and Badging policy, with badges printed on papers — the architecture
  community's adopted trust signal.
- **Simulation is the default instrument**, so methodology rigor (declared
  fidelity scope, pinned versions, sampled-region policy, validation anchors)
  is where reviews are won and lost.

## Skills

| Skill | What it does |
| --- | --- |
| [`isca-topic-selection`](skills/isca-topic-selection/SKILL.md) | Ask where the novelty's center of gravity lives (the machine, the contract, the software), route across the ISCA/MICRO/HPCA/ASPLOS year, and weigh the industry track. |
| [`isca-workflow`](skills/isca-workflow/SKILL.md) | Run the one-gate year backward from mid-November: evidence freezes, the winter wait, the staffed February window, and branch plans per outcome. |
| [`isca-writing-style`](skills/isca-writing-style/SKILL.md) | Build the paper around one mechanism-behavior insight: measured motivation, checkable mechanism description, calibrated numbers, revision slack. |
| [`isca-related-work`](skills/isca-related-work/SKILL.md) | Sweep five decades across dblp/ACM/IEEE, write lineage paragraphs with structural deltas, and blind the voice without touching the bibliography. |
| [`isca-experiments`](skills/isca-experiments/SKILL.md) | Declare the methodology contract — tool, fidelity scope, regions, anchoring — match claims to instruments, and tune baselines to win. |
| [`isca-reproducibility`](skills/isca-reproducibility/SKILL.md) | Pin the result chain (simulator commit → config → workload → region → stats), one manifest per figure, and keep the environment resurrectable for February. |
| [`isca-supplementary`](skills/isca-supplementary/SKILL.md) | Triage material across the only four destinations ISCA offers: the 11 pages, the anonymized repo, the staging shelf for the window, and post-acceptance release. |
| [`isca-artifact-evaluation`](skills/isca-artifact-evaluation/SKILL.md) | Scope Reproduce/Regenerate/Inspect tiers, package simulator-heavy workflows for cold-start evaluators, and earn ACM badges. |
| [`isca-submission`](skills/isca-submission/SKILL.md) | Final audit: the two-step gate, 11-page check, template, the three blinding rules plus the references counter-rule, and HotCRP completion. |
| [`isca-review-process`](skills/isca-review-process/SKILL.md) | Model the two-round pipeline, what the combined window means, champion dynamics at the PC meeting, and how to read each outcome. |
| [`isca-author-response`](skills/isca-author-response/SKILL.md) | Triage objections by what three weeks can fix, run at most three new experiments, write for the committee room, and revise diff-minimally. |
| [`isca-camera-ready`](skills/isca-camera-ready/SKILL.md) | Identify the edition's publisher workflow first, invert every blinding action, integrate badges and DOIs, and prepare the June talk. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten official sources with URLs and 2026-07-08 access dates; the verified 2026-cycle facts; the reported-only items (ISCA 2027 Atlanta, chair roster); the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces and five author-side verification passes (calendar, format, blinding, portal, post-acceptance). |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Six Influential-ISCA-Paper-Award winners (2020-2025 awards) as contribution shapes, each with a self-check question and an attribution guard for the dual-publisher record. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional memory-scheduling abstract and introduction rebuilt to the venue's bar, before → after, move by move. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility kit, plus five architecture-specific checks (simulator pinning, figure traceability, workload licensing, hardware state, evaluator budgets) the kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ISCA-Skills
claude plugin install isca-skills
```

Or use the files directly: each `skills/isca-*/SKILL.md` is a standalone
instruction file whose frontmatter `description` tells an agent when to trigger
it. Typical invocations:

- "Is this prefetcher paper ISCA material or a MICRO paper?" → `isca-topic-selection`
- "Audit my methodology section before the deadline" → `isca-experiments`
- "Reviews are in and the revision window opens Monday" → `isca-author-response`
- "Package the gem5 artifact for badge evaluation" → `isca-artifact-evaluation`

## Pack structure

```text
ISCA-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── isca-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to the shared repro kit
```

## Suggested use across a campaign

1. **Summer (now, for a November gate):** `isca-topic-selection` with the
   exemplars library open; if fit holds, wire in `isca-experiments` and
   `isca-reproducibility` before infrastructure hardens around bad choices.
2. **Autumn:** `isca-writing-style` against the worked example;
   `isca-related-work`'s dblp sweep; `isca-supplementary` for the repo/staging
   split.
3. **Deadline fortnight:** `isca-submission` end to end on the final build,
   twice — once at the abstract step, once at the paper step.
4. **Winter:** `isca-review-process` to set expectations; pre-build the
   objection ledger; run the environment resurrection drill in early February.
5. **The window and after:** `isca-author-response` for the three weeks, then
   `isca-camera-ready` + `isca-artifact-evaluation` on acceptance, or the
   outcome tree's retargeting branch on rejection.

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- ISCA 2026 = **53rd edition**, Raleigh Convention Center, Raleigh, NC, USA,
  **June 27 - July 1, 2026**; ISCA 2025 = 52nd, Tokyo, June 21-25, 2025
  (ACM-published proceedings).
- Main track: abstracts **November 10, 2025**; papers **November 17, 2025**;
  Round 1 reviews due December 19, 2025; Round 2 due February 13, 2026;
  **rebuttal/revision February 16 - March 6, 2026**. Industry track: abstracts
  December 5, papers December 12, 2025.
- Format: **≤ 11 pages** of single-spaced two-column text, references excluded
  and unlimited; printable PDF; ISCA 2026 IEEE LaTeX template suggested;
  submission on **HotCRP** (`isca2026.hotcrp.com`).
- Double-blind: names only in the form; clean PDF metadata; artifact links
  fully anonymized; references never anonymized.
- Artifact evaluation: voluntary, post-acceptance, ACM badging, badges printed
  on papers; no influence on decisions.

## Fact discipline

Three classes of statement, kept distinguishable throughout the pack:

1. **Verified 2026-cycle facts** — dated, and traceable to a numbered source in
   the source map (the 11-page rule, the November 10/17 deadlines).
2. **Reported facts** — found only in secondary renderings and labeled as such
   (ISCA 2027 in Atlanta; the 2026 chair roster).
3. **Unverified items** — marked 待核实 and phrased as questions to resolve
   (everything about the 2027 CFP, notification dates, camera-ready allowances,
   attendance rules, acceptance rates).

Treat any statement in the skills that presents class 2 or 3 as class 1 as a
bug; fix it against the live official pages.

## Maintenance notes

- Every date and cap here is a **2026-cycle snapshot**; reopen
  `iscaconf.org/isca<year>/` before deadline-sensitive advice. The 2027 CFP
  did not exist at check time.
- The ACM/IEEE alternation makes carry-over assumptions (template, publisher,
  rights forms, camera-ready allowance) more dangerous at ISCA than at
  single-sponsor venues — re-verify per edition.
- Chairs and committees rotate per edition; never quote a roster without
  reopening the organization page.
- When adding exemplars, follow the award-anchored recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — verify
  through dblp, not through a single publisher's search.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
