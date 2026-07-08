# FOCS Skills

Twelve agent skills for papers targeting **FOCS — the IEEE Symposium on
Foundations of Computer Science**, the autumn flagship of theoretical computer
science, sponsored by the IEEE Computer Society's Technical Committee on
Mathematical Foundations of Computing (TCMF). The pack follows a theory paper
through the whole April-anchored cycle: testing foundations-level
significance, writing a full-version submission whose first ten pages carry
the case, clearing the HotCRP audit, waiting out a no-rebuttal summer review,
and converting acceptance into an IEEE Xplore proceedings entry plus the
public arXiv/ECCC full version that the community treats as the real record.

Official basis checked on **2026-07-08**: the FOCS 2026 conference site and
Call for Papers at `focs.computer.org/2026/`, the FOCS 2026 HotCRP portal,
the call for workshops, IEEE TCMF award pages, IEEE Xplore / IEEE CS Digital
Library proceedings records, dblp entries, and university announcements of
recent Machtey Awards. Direct fetches of the official domains were blocked in
the verification environment, so pages were verified via search-engine
renderings of the exact URLs and cross-checked across TCMF, IEEE Xplore,
dblp, and community blogs; the full trail — including everything still marked
待核实 — is in [`resources/official-source-map.md`](resources/official-source-map.md).

## Where the 2026 cycle stands (as of the check date)

FOCS 2026 (67th edition, New York, November 8–11, 2026) closed submissions on
**April 1, 2026, 5 PM EDT** — so this pack teaches the *live* post-submission
phases of the current cycle (the summer review wait, the July 31 workshop-
proposal deadline, camera-ready preparation once dates publish) alongside
backward planning for a FOCS 2027 attempt, whose CFP did not yet exist at the
check date. Every 2026 fact is labeled a cycle snapshot, not a permanent rule.

## The venue mechanics that drive this pack

- **Ten pages, plus your bibliography.** No length cap, but the committee
  guarantees attention only to the abstract, the **references**, and the
  first ten pages. FOCS names the reference list as always-read material —
  your bibliography is a reviewed object.
- **You submit the paper, not a teaser.** The CFP encourages the full
  version, complete proofs included, as the submission itself; there is no
  separate supplement channel at all.
- **Double-blind veteran.** FOCS has required anonymized submissions since at
  least the 2023 cycle — years ahead of its ACM sibling — with purpose
  language aimed at unbiased first judgment, not undiscoverable authorship.
- **An IEEE venue running SIGACT rules.** Sponsorship is IEEE TCMF, but the
  prior/simultaneous-publication policy is SIGACT's, and proceedings land in
  IEEE Xplore — a seam that trips authors who read only one society's rules.
- **No rebuttal.** Nothing between the April upload and the decision; your
  submission is your entire side of the conversation.
- **The spring beat of a two-flagship year.** FOCS takes April submissions
  for a fall conference; STOC takes November submissions for a June one. The
  pair forms theory's natural resubmission loop, and this pack plans from
  the FOCS seat.
- **Award lineage as a quality compass.** The Machtey Award (best student
  paper) and the TCMF-administered Test of Time Award (10/20/30-year
  lookback) define, in the venue's own voice, what durable FOCS work looks
  like — the exemplars library is built from them.

## Skills

| Skill | What it does |
| --- | --- |
| [`focs-topic-selection`](skills/focs-topic-selection/SKILL.md) | Run the consequence/obstacle/durability significance test, use the broaden-the-reach lane safely, and route among FOCS, STOC, SODA, CCC, ITCS, CRYPTO, QIP, COLT, and journals. |
| [`focs-workflow`](skills/focs-workflow/SKILL.md) | Manage the live 2026 post-submission phases and backward-plan a 2027 attempt against the April rhythm, with owner assignments and the STOC beat integrated. |
| [`focs-writing-style`](skills/focs-writing-style/SKILL.md) | Budget the guaranteed pages, pair informal and formal statements via `thm-restate`, write the obstacle paragraph, and keep prose double-blind-safe. |
| [`focs-related-work`](skills/focs-related-work/SKILL.md) | Build lineage tables, pin arXiv/ECCC versions, verify `conf/focs/` vs `conf/stoc/` attributions, and handle concurrent preprints generously. |
| [`focs-experiments`](skills/focs-experiments/SKILL.md) | Scope computation by the referee question it triggers — proof-bearing case checks, discovered objects, honest illustrations — and re-route benchmark evidence. |
| [`focs-reproducibility`](skills/focs-reproducibility/SKILL.md) | Engineer checkability: hypothesis ledgers, hash-enforced statement freezes across versions, imported-theorem audits, certificates for computed steps. |
| [`focs-supplementary`](skills/focs-supplementary/SKILL.md) | Architect pages eleven onward at a venue with no supplement channel — the two-reader contract, body organization, pointer discipline, length judgment. |
| [`focs-artifact-evaluation`](skills/focs-artifact-evaluation/SKILL.md) | Manage the evidence inventory without an artifact track: the public full version as object of record, certificate packaging, version ledgers, calibrated formalization claims. |
| [`focs-submission`](skills/focs-submission/SKILL.md) | Final HotCRP audit: the EDT deadline clock, the ten-page window, the format floor, the PDF-encryption ban, the blind sweep, and the IEEE/SIGACT policy seam. |
| [`focs-review-process`](skills/focs-review-process/SKILL.md) | Model the TCMF-sponsored PC, subreferee delegation, the three committee questions, FOCS's double-blind history, and what each outcome actually means. |
| [`focs-author-response`](skills/focs-author-response/SKILL.md) | Operate a no-rebuttal venue: pre-emptive objection discharge, the narrow legitimate uses of chair contact, and the disciplined autumn resubmission memo. |
| [`focs-camera-ready`](skills/focs-camera-ready/SKILL.md) | Deliver the IEEE proceedings version and the public full version in sync, reverse the anonymization completely, and prepare the New York talk and award-eligibility file. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Thirteen sources with URLs and access dates, the verified 2026-cycle fact list, the access-method note, and the 待核实 register. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus six author-side checks keyed to the skills. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Award-anchored exemplars (Test of Time + Machtey lineages) with self-checks and a FOCS/STOC misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional expander-decomposition opening resequenced from journal pacing to the ten-page window. |
| [`resources/code/README.md`](resources/code/README.md) | The narrow slice of shared tooling that applies here, plus FOCS-native PDF, statement-freeze, and certificate checks. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its
own marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./FOCS-Skills
claude plugin install focs-skills
```

Or use the files directly: each `skills/focs-*/SKILL.md` is a standalone
instruction file whose frontmatter `description` tells an agent when to
trigger it. Typical invocations:

- "Is this hardness result FOCS-worthy or a CCC paper?" → `focs-topic-selection`
- "We submitted April 1 — what should we be doing right now?" → `focs-workflow`
- "Audit my PDF before the HotCRP upload" → `focs-submission`
- "A lemma depends on an exhaustive search — how do I make it citable?" → `focs-experiments`
- "We got in; how do the IEEE version and the arXiv version stay in sync?" → `focs-camera-ready`

## Pack structure

```text
FOCS-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── focs-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # checkability tooling notes
```

## 2026 anchor facts (cycle snapshot, not permanent rules)

- FOCS 2026 is the **67th** edition: New York, NY, USA, **November 8–11,
  2026**, sponsored by the IEEE Computer Society TCMF.
- Submissions were due **April 1, 2026, 5:00 PM EDT (21:00 UTC)** on HotCRP
  (`focs26.hotcrp.com`); notification and camera-ready dates were unpublished
  at the check date (待核实).
- Format: no length bound; full version encouraged; abstract + references +
  first **ten pages** guaranteed reading; 11-point-plus single-column,
  1-inch margins, letter paper; PDF free of copy/print security restrictions.
- **Double-blind** reviewing (FOCS practice since at least 2023); SIGACT
  prior/simultaneous-publication policy; full papers with proofs expected
  public (arXiv/ECCC) by camera-ready.
- PC chair: Sanjeev Khanna (one-cycle fact). Workshops Sunday November 8;
  proposals due July 31, 2026 AoE to workshop chairs Dakshita Khurana and
  Sam Hopkins; decisions August 14, 2026.
- Sibling beat: STOC 2026 was due November 4, 2025 and met June 22–26, 2026.

## Fact discipline

The pack keeps three kinds of statement separable:

1. **Verified cycle facts** — dated, and traceable to a numbered row in the
   source map (the April 1 deadline, the ten-page window).
2. **Community customs** — how the venue is observed to behave (subreferee
   delegation, arXiv-first posting norms), labeled as customs.
3. **待核实 items** — explicitly listed in the source map and phrased as
   questions in the skills (notification date, camera-ready format,
   attendance duties, everything about FOCS 2027).

A statement presenting class 2 or 3 as class 1 is a bug; fix it against the
live pages.

## Maintenance notes

- Every number above is a **2026-cycle snapshot**. Deadlines, the window
  size, anonymity wording, and award mechanics can all move; reopen
  `focs.computer.org/<year>/` before advising on a live deadline.
- **FOCS 2027 was entirely 待核实 at 2026-07-08**: no CFP, venue, or dates.
  The April-deadline/autumn-conference rhythm is a pattern, not a promise.
- PC chairs and committees are per-edition appointments; every personal name
  in this pack expires with its cycle.
- When adding exemplars, use the award-anchored recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md), and
  never attribute a paper between FOCS and STOC from memory.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
