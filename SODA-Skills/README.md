# SODA Skills

Twelve agent skills for papers targeting **SODA — the ACM-SIAM Symposium on
Discrete Algorithms**, the venue jointly sponsored by the SIAM Activity Group on
Discrete Mathematics and ACM SIGACT where the algorithms community moves its
quantitative frontiers: running times, approximation ratios, data-structure
bounds, and the discrete mathematics behind them. The pack covers the full arc:
deciding whether a result is SODA-shaped, building an uncapped full-version
submission for HotCRP, surviving lightweight double-blind review and the
three-day September rebuttal, and converting an October acceptance into a SIAM
proceedings entry and a January talk.

Official basis checked on **2026-07-08**: the SIAM SODA 2027 conference and
submissions pages, the `soda27.hotcrp.com` site, the SIAM ALENEX 2027 and SOSA
2027 pages, SIAM epubs proceedings volumes (2021-2026), dblp series records, and
institutional best-paper announcements. Direct fetches of `siam.org`,
`hotcrp.com`, and `dblp.org` were blocked in the verification environment, so
official pages were read via search-engine renderings of the exact URLs and
cross-checked across independent surfaces; the full trail, including every item
still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## The mechanics that make SODA its own venue

These verified 2027-cycle facts drive most of the advice — and most of the
mistakes made by authors arriving with other venues' habits:

- **No page limit; the full version is the submission.** The CFP encourages
  submitting the complete paper: title page with a one-to-two-paragraph
  abstract, then everything, proofs included. "Details deferred to the full
  version" is a phrase from somewhere else.
- **A July deadline for a January conference.** SODA 2027: papers due July 9,
  2026 (AoE), conference January 24-27, 2027, Philadelphia. SODA holds the
  summer seat in the theory calendar, between STOC's November deadline and
  FOCS's April one.
- **Lightweight double-blind.** No names or affiliations on the PDF — but arXiv
  posting and talks stay explicitly permitted, and important references
  (including your own) must not be omitted or anonymized.
- **A short rebuttal exists.** Reviews reach authors by September 1, 2026;
  responses are due September 4. Three days — preparation is an August
  activity, not a September one.
- **SIAM's publication machinery.** Proceedings appear in the SIAM Publications
  Library under `10.1137/1.978...` DOIs; final-version instructions arrive with
  October's acceptance email.
- **Satellites with their own mandates.** ALENEX (experimental algorithmics,
  papers due July 20, 2026, with formal artifact evaluation) and SOSA
  (simplicity in algorithms, due August 6, 2026) share the Philadelphia venue —
  and absorb the papers SODA reviewing would undervalue.

## Skills

| Skill | What it does |
| --- | --- |
| [`soda-topic-selection`](skills/soda-topic-selection/SKILL.md) | Apply the three-question fit test — problem with a bound? expert-legible? discrete technique? — and route between SODA, STOC/FOCS, ITCS, ESA/ICALP, SOSA, ALENEX, SoCG, and journals. |
| [`soda-workflow`](skills/soda-workflow/SKILL.md) | Run the July-to-January campaign: backward plan to July 9, the quiet refereeing months, the September sprint, the October fork, and satellite choreography. |
| [`soda-writing-style`](skills/soda-writing-style/SKILL.md) | Engineer the quotable headline bound, the bidding-surface abstract, the first-ten-pages overview contract, and the prior-bound table. |
| [`soda-related-work`](skills/soda-related-work/SKILL.md) | Sweep the five literature lanes, verify bound lineages via dblp and journal versions, and handle arXiv-first priority and self-citation under lightweight double-blind. |
| [`soda-experiments`](skills/soda-experiments/SKILL.md) | Decide whether numerics belong at all, label their claim class honestly, and route implementation-led work to ALENEX or SEA. |
| [`soda-reproducibility`](skills/soda-reproducibility/SKILL.md) | Build the claims ledger, run blind proof-checks, audit imported theorems and probability budgets, and certify machine-checked steps. |
| [`soda-supplementary`](skills/soda-supplementary/SKILL.md) | Architect the single uncapped PDF — front/back matter contract, dependency-ordered appendices, restated theorems — since no supplement channel exists. |
| [`soda-artifact-evaluation`](skills/soda-artifact-evaluation/SKILL.md) | Package computer-assisted proof evidence with certificates, keep archives anonymity-safe, and use ALENEX's AE pipeline when the artifact is the point. |
| [`soda-submission`](skills/soda-submission/SKILL.md) | Final audit: format floor, lightweight double-blind sweep, completeness check, HotCRP record hygiene, and the summary-rejection triggers. |
| [`soda-review-process`](skills/soda-review-process/SKILL.md) | Model the pipeline — bidding, subreviewers, rebuttal, PC deliberation, October decisions — and what actually moves a borderline paper. |
| [`soda-author-response`](skills/soda-author-response/SKILL.md) | Fight the three-day rebuttal well: August preparation, F/L/S/C review triage, theorem-anchored numbered replies, clean concessions. |
| [`soda-camera-ready`](skills/soda-camera-ready/SKILL.md) | Condense the full version into the SIAM proceedings entry, restore identity, sync arXiv, and prepare the Philadelphia talk. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten primary sources plus award sources, with URLs and access dates; verified 2027-cycle facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces and the five author-side verification passes to run before upload. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Four attribution-verified best-paper-level SODA exemplars (2021-2025) across four problem lanes, each with a self-check question, plus the venue-verification recipe. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional dynamic-data-structure abstract and overview opening rebuilt before → after for SODA's two readers. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared packaging smoke-checker, plus the four SODA-specific checks no script performs. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./SODA-Skills
claude plugin install soda-skills
```

Or use the files directly: each `skills/soda-*/SKILL.md` is a standalone
instruction file whose frontmatter `description` tells an agent when to trigger
it. Typical invocations:

- "Is this min-cut improvement a SODA paper or should it wait for STOC?" → `soda-topic-selection`
- "Audit my draft against the SODA format and double-blind rules" → `soda-submission`
- "Reviews arrive September 1 — set up the rebuttal plan" → `soda-author-response`
- "My proof uses an exhaustive computer search — how do I ship it?" → `soda-artifact-evaluation`

## Pack structure

```text
SODA-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── soda-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # packaging-check adapter
```

## 2027-cycle anchor facts (snapshot, not permanent rules)

- SODA 2027: **Philadelphia, January 24-27, 2027**; by edition count the 38th
  (2025 = 36th, 2026 = 37th, both verified; 2027 derived).
- Papers due **July 9, 2026, anywhere on Earth**, via `soda27.hotcrp.com`.
- Reviews to authors by **September 1, 2026**; responses due **September 4**;
  decisions and final-version instructions **October 2026**.
- Format: **no page limit** (full version encouraged); title page with 1-2
  paragraph abstract; 11-point+ single-column, 1-inch margins, letter paper;
  deviations risk summary rejection.
- Review model: fairly **lightweight double-blind**; arXiv/talks free;
  important references never omitted or anonymized.
- Co-located: **ALENEX 2027** (Jan 24-25; papers July 20, 2026; artifacts
  Sept 11; AE results by Oct 16) and **SOSA 2027** (Jan 25-26; papers
  Aug 6, 2026). ANALCO, the former third satellite, last appears in dblp
  for 2019.
- Recent proceedings DOI anchors on epubs.siam.org: `10.1137/1.9781611976465`
  (2021), `...977912` (2024), `...978322` (2025), `...978971` (2026).

## Fact discipline

Three classes of statement, kept distinguishable throughout the skills:

1. **Verified 2027-cycle facts** — carry dates and trace to a numbered source in
   the source map (the July 9 deadline, the format floor, the rebuttal window).
2. **Reported facts** — from credible secondary sources and labeled as such
   (e.g., the 2026 PC chair's record-submission announcement).
3. **Unverifiable-at-check-time items** — marked 待核实 and phrased as questions
   (2027 PC chairs, camera-ready mechanics, registration duties, proceedings
   access terms).

Any statement presenting class 2 or 3 as class 1 is a bug; fix it against the
live SIAM pages.

## Maintenance notes

- Every date above is a **2027-cycle snapshot**. SODA's PC — and therefore its
  policy — is reappointed annually; reopen
  `siam.org/conferences-events/siam-conferences/soda<yy>/` before any
  deadline-sensitive advice.
- The rebuttal is recent house practice (institutionalized by 2026), not ancient
  tradition: confirm its dates and mechanics each cycle rather than assuming.
- Camera-ready page allowances, SIAM macros, and registration rules ship with
  acceptance emails and remain 待核实 here — never invent them.
- When adding exemplars, follow the recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md): dblp plus
  the epubs DOI, because the SODA/STOC/FOCS boundary is where memory
  misattributes.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
