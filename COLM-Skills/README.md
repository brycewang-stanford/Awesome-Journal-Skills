# COLM Skills

Twelve agent skills for papers targeting **COLM — the Conference on Language
Modeling**, the young venue (announced October 2023, first edition 2024) built
specifically for research where the language model is the object of study:
training, data, evaluation, inference, interpretability, and safety of LM
technology. The pack covers the whole arc — deciding whether a project is
COLM-shaped at all, building contamination-aware and version-pinned evidence,
surviving the OpenReview rebuttal, and turning a July acceptance into an August
camera-ready and an October talk.

Official basis checked on **2026-07-08**: the COLM 2026 homepage, key-dates page,
Call for Papers, submission instructions, author guide, FAQ, the COLM 2026
OpenReview group, the 2024/2025 accepted-paper lists, and independent coverage of
the Outstanding Paper Awards. Direct fetches of `colmweb.org` were blocked by the
network gateway used for verification, so official pages were read through
search-engine renderings of the exact URLs and cross-checked against OpenReview and
institutional sources; the full trail, including every item still marked 待核实, is
in [`resources/official-source-map.md`](resources/official-source-map.md).

## Where the 2026 cycle stands (as of 2026-07-08)

This pack was built on **COLM 2026 decision day**. The March deadlines (abstract
March 26, paper March 31) and the rebuttal window (May 22 - June 8) are history;
**decision notifications land July 8**; camera-ready is due **August 7**; the
conference runs **October 6-9 at the Hilton Union Square, San Francisco** (main
program October 6-8, workshops October 9). Practically:

- **Accepted today?** Start at [`colm-camera-ready`](skills/colm-camera-ready/SKILL.md)
  — you have one month, and the artifact release should ship in the same pass.
- **Rejected today?** The reject branch of
  [`colm-review-process`](skills/colm-review-process/SKILL.md) maps the
  ICLR/NeurIPS/COLM-2027 resubmission calendar.
- **Planning new work?** You are planning **COLM 2027** — dates unannounced
  (待核实; late March is the working assumption), so the planning skills teach the
  cycle shape from the verified 2026 calendar.

## What makes COLM different from its neighbors

- **The LM is the subject, not the tool.** COLM's founding premise is that LM
  technology raises research questions that sat awkwardly at ACL/EMNLP (task- and
  language-centered), ICLR/NeurIPS/ICML (generality-centered), and systems venues.
  The routing test lives in [`colm-topic-selection`](skills/colm-topic-selection/SKILL.md).
- **An award lineage that prizes measurement.** Five of the eight Outstanding
  Papers across 2024-2025 are analysis, measurement, or evaluation-critique work —
  a strong prior about what reviewers value
  ([`resources/exemplars/library.md`](resources/exemplars/library.md)).
- **LM-specific rigor is the review bar:** contamination handling, matched-budget
  baselines, pinned checkpoints and API version strings with query dates, decoding
  disclosure, and compute reporting — the core of
  [`colm-experiments`](skills/colm-experiments/SKILL.md) and
  [`colm-reproducibility`](skills/colm-reproducibility/SKILL.md).
- **Compact modern mechanics:** OpenReview end-to-end with papers published
  openly there (no PMLR volume, no ACL Anthology); a strict 9-page main text with
  unlimited citation pages; double-blind rules that explicitly ban acknowledgments
  and identity-revealing links; a Code of Ethics every author must acknowledge; an
  LLM-usage policy (adopted from ICLR 2026, relaxed for minor assistance); and
  reciprocal-reviewing requirements that draft authors with 4+ submissions into
  the reviewer pool.
- **Young-venue variance.** Three editions in (2024 Philadelphia, 2025 Montreal,
  2026 San Francisco), norms and policies move every year — which is why every
  skill separates verified 2026 facts from 待核实 items.

## Skills

| Skill | What it does |
| --- | --- |
| [`colm-topic-selection`](skills/colm-topic-selection/SKILL.md) | Apply the object-of-study test and route between COLM, ACL/EMNLP, ICLR, NeurIPS/ICML, systems venues, and workshops — including the young-venue calculus. |
| [`colm-workflow`](skills/colm-workflow/SKILL.md) | Run the one-shot year backward from the March deadline: compute booking, claims ledger, reciprocal-reviewing map, decision-tree memo, multi-venue rotation. |
| [`colm-writing-style`](skills/colm-writing-style/SKILL.md) | Lead with a finding about LMs, scope every claim to tested models and scales, pin versions in prose, keep the 9 pages self-sufficient. |
| [`colm-related-work`](skills/colm-related-work/SKILL.md) | Cover the five literature lanes, handle arXiv-heavy and concurrent work honestly, verify references resolve, keep self-citation double-blind. |
| [`colm-experiments`](skills/colm-experiments/SKILL.md) | Survive the four LM-specific attacks: contamination, baseline fairness, version drift, decoding sensitivity — with matched budgets and real uncertainty. |
| [`colm-reproducibility`](skills/colm-reproducibility/SKILL.md) | Layer the repro story (exact / budgeted / drifting), pin four hashes, cache API responses, disclose compute, write itemized availability statements. |
| [`colm-supplementary`](skills/colm-supplementary/SKILL.md) | Split content between the strict 9-page body and the audit-trail appendix: verbatim prompts, tried-ledgers, contamination analyses, anonymized packages. |
| [`colm-artifact-evaluation`](skills/colm-artifact-evaluation/SKILL.md) | Package weights, data, prompts, and cached outputs for review and release — licensing gates, ToS limits, one-command reproduction, verify-from-cache. |
| [`colm-submission`](skills/colm-submission/SKILL.md) | Final OpenReview audit: 9-page cap, anonymity sweep for LM-specific leaks, ethics acknowledgment, LLM disclosure, reciprocal-reviewer assignment. |
| [`colm-review-process`](skills/colm-review-process/SKILL.md) | Model the March-to-July pipeline, the reciprocal reviewer pool, young-venue score variance, reviewer LLM-use rules, and the reject branch. |
| [`colm-author-response`](skills/colm-author-response/SKILL.md) | Budget the ~18-day rebuttal, answer the four standard objections with cache-based evidence, concede in the open, write for the AC. |
| [`colm-camera-ready`](skills/colm-camera-ready/SKILL.md) | Convert acceptance into the public OpenReview record: de-anonymize in both directions, honor the rebuttal ledger, ship artifacts, plan San Francisco. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Twelve dated sources, the access-method caveat, verified 2026 facts, reported-only items, and the explicit 待核实 list. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | The eight Outstanding Papers of COLM 2024-2025 with positioning notes, self-check questions, and venue-attribution guards. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional leaderboard-style first page rebuilt into COLM shape: phenomenon first, contamination on page one, pinned models, scoped claims. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference repro kit, plus the five LM-specific checks the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./COLM-Skills
claude plugin install colm-skills
```

Or use the files directly — each `skills/colm-*/SKILL.md` is a standalone
instruction file whose frontmatter `description` tells an agent when to fire.
Typical invocations:

- "Is this a COLM paper or an EMNLP paper?" → `colm-topic-selection`
- "Red-team my evaluation before we train anything" → `colm-experiments`
- "Reviews drop May 22 — set up the rebuttal plan" → `colm-author-response`
- "We got in! What has to happen before August 7?" → `colm-camera-ready`

## Pack structure

```text
COLM-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── colm-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 2026 anchor facts (one cycle's snapshot, not permanent rules)

- COLM 2026 is the **third edition**: Hilton Union Square, San Francisco,
  **October 6-9, 2026** (main conference Oct 6-8, workshops Oct 9).
- Timeline: abstract **March 26** · paper **March 31** · reviews **May 22** ·
  rebuttal **May 22 - June 8** · decisions **July 8** · camera-ready **August 7**.
- Format: **strict 9-page main text**, unlimited citation pages, optional ≤ 1-page
  acknowledgments outside the limit (camera-ready only — submissions are
  double-blind with no acknowledgments and no identity-revealing links).
- Platform: OpenReview (`colmweb.org/COLM/2026/Conference`), opened February 2026;
  papers published openly on OpenReview.
- Policy: Code of Ethics acknowledgment required from all authors; LLM-usage
  disclosure per the 2026 policy; per-submission and per-reviewer reciprocal
  reviewing, with automatic pool entry at 4+ submissions.
- Editions: 2024 Philadelphia (UPenn) · 2025 Montreal · 2026 San Francisco; four
  Outstanding Paper Awards in each of the first two editions.

## Fact discipline

Three statement classes run through the pack, kept deliberately distinguishable:

1. **Verified 2026 facts** — dated and traceable to a numbered source in the
   source map (the 9-page cap, the March 26 / March 31 / May 22 / June 8 /
   July 8 / August 7 chain, the LLM policy).
2. **Reported facts** — found only in secondary renderings and labeled as such
   (the 2026 committee names, the 2025 venue building).
3. **待核实 items** — camera-ready page allowance, registration and attendance
   rules, acceptance rates, artifact-track existence, all 2027 dates — phrased as
   questions to resolve, never as facts.

If any skill statement presents class 2 or 3 material as class 1, treat it as a bug
and fix it against the live pages.

## Maintenance notes

- COLM is young enough that *everything* above is cycle-volatile — the venue moved
  continents twice and adjusted policy in each of its first three editions. Reopen
  `colmweb.org` and the current OpenReview group before deadline-sensitive advice.
- The dblp record for COLM could not be fetched at build time; cross-check
  `dblp.org/db/conf/colm/` when adding bibliography guidance.
- When adding exemplars, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — an arXiv
  "Published at COLM" banner is a claim, not a proof.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
