# ICDT Skills

Twelve agent skills for papers targeting **ICDT — the International Conference on Database Theory**,
the European foundations-of-data-management venue held jointly with **EDBT** and published **open
access in LIPIcs** (Schloss Dagstuhl). The pack covers the full arc of an ICDT campaign: deciding
whether a project is ICDT-shaped or belongs at **PODS**, the co-located EDBT systems track, a
pure-TCS venue, or a journal; writing a theorem-proof paper with matching bounds; packaging the
**anonymous** submission in the **`lipics-v2021`** 15-page format with a complete-proofs appendix;
navigating the **two-submission-cycle** calendar and its **first-cycle revision**; and delivering the
LIPIcs camera-ready plus an archived full version.

Official basis checked on **2026-07-09**: the ICDT 2026 and ICDT 2027 calls at databasetheory.org,
the EDBT/ICDT 2026 (Tampere) and 2027 (Lille) event sites, the DROPS/LIPIcs series and the ICDT 2026
proceedings volume, the `lipics-v2021` author instructions, the Microsoft CMT submission portal, and
the ICDT awards pages. Direct fetches of `databasetheory.org`, `drops.dagstuhl.de`, and the event
sites failed/returned 403 in the verification environment, so official pages were read via
search-engine renderings of the exact URLs and cross-checked against dblp, the DROPS volume pages,
the CMT/EasyChair CfP listings, and mailing-list archives; the full trail, including everything still
marked 待核实, is in [`resources/official-source-map.md`](resources/official-source-map.md).

> Name-collision warning: the SID *International Conference on Display Technology* (`sidicdt.org`)
> and IARIA's *International Conference on Digital Telecommunications* also abbreviate to "ICDT" and
> are **not** this venue. No fact in this pack derives from them.

## What makes ICDT different from its siblings

These venue mechanics, verified for the 2026/2027 cycles, drive most of the advice in the skills —
and most of the mistakes made by authors arriving from PODS, from a systems venue, or from pure TCS:

- **Open-access LIPIcs, not ACM/IEEE.** ICDT papers publish in **LIPIcs (Leibniz International
  Proceedings in Informatics)**, Schloss Dagstuhl, under **CC-BY 4.0** with a DOI on **DROPS** and no
  author-facing APC. The camera-ready is a **LaTeX-only `lipics-v2021`** document — this is the concrete
  publishing difference from **PODS**, whose research papers now appear in ACM **PACMMOD**.
- **Co-located with EDBT.** ICDT runs inside the joint **EDBT/ICDT** event (Tampere 2026, Lille 2027),
  sharing a week and a venue with the EDBT systems track — same building, different reviewer culture:
  ICDT wants a proof, EDBT wants a system.
- **Two submission cycles per year.** ICDT posts **two annual deadlines** (ICDT 2027: papers 10 Mar
  2026 and 10 Sep 2026, AoE). The **first cycle carries a revision option**; a paper **rejected** in
  Cycle 1 **cannot be resubmitted to Cycle 2 unless the reviewers invite it**.
- **Anonymous review since 2024.** Regular-track submissions carry no author names, affiliations, or
  acknowledgments. (The short **Database Theory in Action** track is *not* anonymous.)
- **Complete proofs expected.** ICDT is a proof venue: the 15-page body (excluding references) states
  the results and ideas, a **clearly marked appendix** (read at the PC's discretion) holds the full
  proofs, **online appendices are not allowed**, and an arXiv **full version** carries all proofs after
  publication.
- **A tight-bounds, precise-model culture.** Matching upper and lower bounds, an explicit data /
  combined / query complexity measure, and a fixed data and query model are community norms the
  database-theory referee pool enforces even where no rule states them.

## Skills

| Skill | What it does |
| --- | --- |
| [`icdt-topic-selection`](skills/icdt-topic-selection/SKILL.md) | Route between ICDT and its siblings (PODS, the co-located EDBT, LICS/ICALP/STACS, and journals like TODS/LMCS/TheoretiCS) by contribution shape, calendar, and the open-access-LIPIcs vs PACMMOD choice. |
| [`icdt-workflow`](skills/icdt-workflow/SKILL.md) | Run the two-cycle year backward from a chosen deadline through abstract registration, the Cycle-1 revision, LIPIcs camera-ready, and the EDBT/ICDT talk. |
| [`icdt-writing-style`](skills/icdt-writing-style/SKILL.md) | Build the theorem-proof skeleton: fix the data and computation model, state the result early, sketch-in-body-proofs-in-appendix within 15 pages. |
| [`icdt-related-work`](skills/icdt-related-work/SKILL.md) | Cover the database-theory lanes, write delta-first positioning against the nearest prior bound, and keep self-citations anonymous. |
| [`icdt-experiments`](skills/icdt-experiments/SKILL.md) | Match evidence to claim: matching bounds and constructions as the primary evidence, with a proportional experiment only for the rare algorithmic paper. |
| [`icdt-reproducibility`](skills/icdt-reproducibility/SKILL.md) | The theory-venue analogue of reproducibility: complete self-contained proofs, pinned models, matching bounds, and paper/full-version consistency. |
| [`icdt-supplementary`](skills/icdt-supplementary/SKILL.md) | Split content between the 15-page body and the marked appendix, given that online appendices are forbidden and the reviewed object is one PDF. |
| [`icdt-submission`](skills/icdt-submission/SKILL.md) | Final CMT audit: pick the cycle, the two-step abstract+paper deadline, `lipics-v2021` and the page budget, the anonymity sweep, complete-proofs check, desk-risk triage. |
| [`icdt-review-process`](skills/icdt-review-process/SKILL.md) | Model the pipeline — two cycles, anonymous review, Accept/Revise/Reject, the cross-cycle carry rule, proof-correctness scrutiny — and where author leverage exists. |
| [`icdt-author-response`](skills/icdt-author-response/SKILL.md) | Write the Cycle-1 revision: close each named proof gap, document the change, keep the revised paper anonymous. |
| [`icdt-artifact-evaluation`](skills/icdt-artifact-evaluation/SKILL.md) | Understand that ICDT has no code-artifact track: make the proof-artifact (marked appendix + arXiv full version) airtight instead of chasing ACM badges. |
| [`icdt-camera-ready`](skills/icdt-camera-ready/SKILL.md) | De-anonymize, complete the LIPIcs metadata (CCS, keywords, ORCID), link the full version, pass the Dagstuhl/DROPS production checks under CC-BY. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026/2027 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Four archival-verified ICDT Test-of-Time papers across four contribution shapes, with self-check questions and sibling-venue guards. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional consistent-query-answering result's abstract and introduction rebuilt to the ICDT arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Why ICDT has no code artifact, plus the proof-artifact checklist the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ICDT-Skills
claude plugin install icdt-skills
```

Or use the files directly: each `skills/icdt-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an ICDT paper or should it go to PODS/EDBT?" → `icdt-topic-selection`
- "Audit my draft against the ICDT regular-track rules" → `icdt-submission`
- "We got a Cycle-1 revise — plan the revision" → `icdt-author-response`
- "Prepare the LIPIcs camera-ready" → `icdt-camera-ready`

## Pack structure

```text
ICDT-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── icdt-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # proof-artifact adapter (no code track)
```

## Suggested use

1. **Before writing** — run `icdt-topic-selection`; ICDT and PODS overlap almost completely, so
   choosing by calendar and publisher matters. Skim the exemplars library to see what decade-influential
   ICDT contributions look like.
2. **While proving** — keep `icdt-experiments` and `icdt-reproducibility` beside the result; matching
   bounds and self-contained proofs cannot be retrofitted at deadline time.
3. **While writing** — `icdt-writing-style` for the theorem-proof body against the worked example,
   `icdt-supplementary` for the body/appendix split, `icdt-related-work` for delta-first positioning.
4. **Deadline weeks** — register the abstract before the earlier deadline in the chosen cycle, then
   `icdt-submission` end to end on the final PDF.
5. **After submission** — `icdt-review-process` to calibrate, `icdt-author-response` for a Cycle-1
   revision, then `icdt-camera-ready` — or the routing table in `icdt-topic-selection` if the decision
   goes the other way.

## 2026/2027-cycle anchor facts (historical snapshot, not permanent rules)

- ICDT 2026 is the **29th** edition, within **EDBT/ICDT 2026**, Tampere, Finland; proceedings are
  **LIPIcs Volume 365**. Review chair: **Balder ten Cate** (ILLC, University of Amsterdam). Event dates
  differ between renderings (24-27 March vs 9-14 March 2026) and are **待核实**.
- ICDT 2027 is the **30th** edition, within **EDBT/ICDT 2027**, **Lille, France, 6-9 April 2027**; PC
  chair **Stijn Vansummeren** (Hasselt University). **Two cycles:** papers **10 Mar 2026** (Cycle 1,
  notification 1 Jun 2026) and **10 Sep 2026** (Cycle 2, notification 1 Dec 2026), AoE. As of 2026-07-09
  **Cycle 2 is the immediate live target.**
- Publication: **LIPIcs**, open access, **CC-BY 4.0**, DOI on DROPS, no author APC. Review:
  **anonymous** (regular track), **two cycles** with a **Cycle-1 revision**. Format: **`lipics-v2021`,
  15 pages excl. references**, marked appendix, no online appendices. Portal: **Microsoft CMT**.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026/2027 facts** — carry dates/limits and trace to a numbered source in the source map
   (e.g., the LIPIcs publication, the 15-page `lipics-v2021` format, the two-cycle calendar, anonymous
   review since 2024).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., exact ICDT
   session dates within the EDBT/ICDT event).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the ICDT 2026 date
   discrepancy, full PC rosters, any generative-AI disclosure policy, whether a short rebuilt/rebuttal
   phase runs).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it against
the live official pages.

## Maintenance notes

- Every date and limit above is a **cycle snapshot**. ICDT re-decides its structure per edition —
  including which cycles run and their dates — so verify the cadence before anything else each year.
- ICDT has no standing editor-in-chief and no author APC; the PC chair rotates per edition. Treat
  continuity assumptions about people as errors.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar result is not proof
  of an ICDT placement (many are PODS or journal papers).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
