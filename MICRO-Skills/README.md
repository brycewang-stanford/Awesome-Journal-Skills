# MICRO Skills

Twelve agent skills for papers targeting **MICRO — the IEEE/ACM International
Symposium on Microarchitecture**, the flagship venue of the microarchitecture
community and, via its 1968 microprogramming-workshop lineage, the oldest of
computer architecture's top conferences. The pack covers the whole campaign:
testing whether a mechanism truly lives inside the machine, building
simulator-grade evidence with honest cost accounting, fitting an argument into 11
appendix-free pages, spending the two-week rebuttal/revision window on runs rather
than rhetoric, and converting acceptance into a badged, artifact-backed entry in
the ACM DL and IEEE Xplore.

Official basis checked on **2026-07-08**: the MICRO 2026 (59th edition) hub, Call
for Papers, and submission guidelines at `microarch.org/micro59/`, the
`micro2026.hotcrp.com` site, the inaugural Industry Track CFP, the MICRO 2025
artifact-evaluation pages, the SIGMICRO Test of Time and Hall of Fame pages, and
ACM DL / IEEE Xplore / dblp proceedings records. Direct fetches of `microarch.org`
and related hosts returned 403 in the verification environment, so official pages
were read through search-engine renderings of the exact URLs and cross-checked
against the digital libraries and SIGARCH/TCCA CFP mirrors; the full trail and
every item still marked 待核实 live in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Where the 2026 cycle stands (as of the check date)

MICRO 2026 notifications went out **July 7, 2026** — the day before this pack's
verification date. The live work this pack lands in the middle of:

- **Accepted papers** face the September 11 camera-ready with artifact evaluation
  running in parallel, then Athens (October 31 – November 4).
- **Rejected papers** have a quarterly fallback lattice: HPCA 2027 closes
  **July 24, 2026** (17 days after notification), ASPLOS 2027's second deadline is
  September 9, ISCA 2027 papers are due November 17, and MICRO 2027 returns to the
  early-April slot (date 待核实).
- **New projects** should be building their evaluation stack now — in this field
  the simulator, baselines, and sweep queue are the schedule; prose is cheap.

## The venue mechanics that drive this pack's advice

Verified for the 2026 cycle and taught throughout the skills:

- **Deadlines run on US Eastern time, not AoE** — abstracts March 31, papers
  April 7, both 11:59 PM EDT, with the abstract acting as a hard registration
  gate a week before the paper.
- **11 content pages, unlimited references, and no appendix at all.** There is no
  supplementary PDF tier; material either earns body space, moves to an anonymized
  artifact repository, or gets cut.
- **Format enforcement is dual:** visual plus automated inspection, with rejection
  possible even after the HotCRP checker passes. Minimum 9pt everywhere, page
  numbers required, template geometry untouchable.
- **Every reference names every author** — "et al." in an entry is a format
  violation, and the rule survives into the camera-ready.
- **A two-week combined rebuttal/revision window** (June 3–17 in 2026), long
  enough to run reviewer-requested experiments, with double-blind obligations and
  a professional-conduct rule that explicitly covers rebuttal language.
- **Post-acceptance artifact evaluation with ACM badges** (2025 pattern:
  Available requires an archival deposit; passing earns a free two-page artifact
  appendix), feeding badges into the ACM DL record.
- **An inaugural Industry Track** with a review process tailored to
  production-scale evidence.

## Skills

| Skill | What it does |
| --- | --- |
| [`micro-topic-selection`](skills/micro-topic-selection/SKILL.md) | Run the mechanism-residency test (can you state it without software actors?) and route between MICRO, ISCA, HPCA, ASPLOS, DAC/ICCAD, SC, MLSys, and the Industry Track. |
| [`micro-workflow`](skills/micro-workflow/SKILL.md) | Drive the April→Athens clock, the quarterly four-venue lattice, and the backward plan where the evaluation stack — not the writing — is the critical path. |
| [`micro-writing-style`](skills/micro-writing-style/SKILL.md) | Build the four-beat argument (characterization → insight → mechanism → accounting), budget 11 appendix-free pages, and keep simulated numbers labeled as simulated. |
| [`micro-related-work`](skills/micro-related-work/SKILL.md) | Sweep five literature lanes including industry disclosures, differentiate by structure and cost, and dblp-verify venue attribution before citing. |
| [`micro-experiments`](skills/micro-experiments/SKILL.md) | Match claims to the instrument ladder (trace model → cycle-level sim → RTL → FPGA → silicon), tune product-like baselines, and report geomeans with full overhead accounting. |
| [`micro-reproducibility`](skills/micro-reproducibility/SKILL.md) | Pin simulator commits, configs, SimPoint recipes, and power-model versions in per-run manifests that later become the AE package. |
| [`micro-supplementary`](skills/micro-supplementary/SKILL.md) | Triage content for a venue with **no appendix**: the 11 pages, the unlimited references, the anonymized repo, or the cut list. |
| [`micro-artifact-evaluation`](skills/micro-artifact-evaluation/SKILL.md) | Package simulation artifacts around evaluator time budgets (smoke/key/full tiers), handle SPEC licensing, and target the three ACM badges. |
| [`micro-submission`](skills/micro-submission/SKILL.md) | Final HotCRP audit: EDT clock, abstract gate, page and font floors, all-author references, anonymized-or-removed artifact links. |
| [`micro-review-process`](skills/micro-review-process/SKILL.md) | Model the April→July pipeline, the methodology-forensics reviewer culture, the conduct rules, and the Industry Track's separate review. |
| [`micro-author-response`](skills/micro-author-response/SKILL.md) | Treat the two-week window as a lab sprint: classify objections, run the missing experiments, and answer with manifested numbers. |
| [`micro-camera-ready`](skills/micro-camera-ready/SKILL.md) | Execute the nine-week accept path: additive de-anonymization diff, restored acknowledgments, AE-coupled artifact appendix, dual-library publication. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and 2026-07-08 access dates, verified-fact list, fact-class rules, and the explicit 待核实 register. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces, bibliographic authorities, sibling calendars, and five author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five DOI-verified MICRO papers (1991–2014), three of them Test-of-Time validated, as contribution shapes — plus the checked misattribution traps. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional dead-block-reclamation abstract and introduction rebuilt through the four-beat argument, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility kit plus six simulator/hardware checks the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./MICRO-Skills
claude plugin install micro-skills
```

Or use the files directly — each `skills/micro-*/SKILL.md` is a standalone
instruction file whose frontmatter description tells an agent when to fire.
Typical invocations:

- "Is this prefetcher paper MICRO or ASPLOS?" → `micro-topic-selection`
- "Audit the PDF before the HotCRP upload" → `micro-submission`
- "Reviews landed and the window opens Wednesday" → `micro-author-response`
- "We got in — plan camera-ready plus artifact evaluation" → `micro-camera-ready`

## Pack structure

```text
MICRO-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── micro-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to the shared repro kit
```

## 2026-cycle anchor facts (snapshot, not permanent rules)

- **MICRO 2026 = 59th edition · Athens, Greece · October 31 – November 4, 2026.**
- Abstracts March 31 / papers April 7, 2026, both 11:59 PM **EDT**, on
  `micro2026.hotcrp.com`; rebuttal/revision June 3–17; notification July 7;
  camera-ready September 11.
- Format: ≤ 11 pages excluding references; **no appendix**; unlimited references
  with all authors named; ≥ 9pt text; page numbers mandatory; MICRO template with
  no space-squeezing; dual visual/automated inspection.
- Review: double-blind end to end; artifact links anonymized or removed; no
  acknowledgments at submission; conduct rules cover rebuttals.
- Artifacts: post-acceptance AE with ACM badges (2025 pages verified; 2026
  instance 待核实); Available badge needs Zenodo/FigShare/Dryad-class archiving.
- Community fixtures: MICRO Test of Time Award (2025 winners: 3D die-stacking and
  CACTI 6.0), MICRO Hall of Fame (8+ papers), IEEE Micro Top Picks eligibility.

## Fact discipline

The pack keeps three classes of statement distinguishable:

1. **Verified 2026-cycle facts** — carry a date or cap and trace to a numbered
   source in the source map (the 11-page rule, the EDT deadlines, the June window).
2. **Derived or secondary facts** — labeled in place (the 1968 lineage is
   arithmetic from the 59th ordinal; reviewer-rubric text is a community-norm
   composite, not a quoted form).
3. **待核实 items** — phrased as questions to resolve, never as facts (2026 AE
   dates, chairs, camera-ready allowances, attendance rules, MICRO 2027 dates).

A skill stating class-2 or class-3 material as class 1 is a bug; fix it against
the live pages and update the source map.

## Maintenance notes

- Every number here is a **2026-cycle snapshot**. MICRO re-decides format, dates,
  tracks, and AE arrangements each edition — reopen `microarch.org/micro<NN>/`
  before advising on the next cycle, and note that 2026 introduced a track that
  did not exist in 2025.
- The 待核实 register in the source map is the debt list: organizers' names, AE
  calendar, Industry Track deadlines, rebuttal mechanics detail, camera-ready
  allowances, attendance rules, and any AI-authorship policy.
- Program leadership rotates per edition; nothing in this pack should be read as
  a standing editorial policy.
- New exemplars enter only through the verification recipe at the bottom of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — the DOI
  record decides, not memory.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
