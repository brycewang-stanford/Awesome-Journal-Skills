# EuroSys Skills

Twelve agent skills for papers targeting **EuroSys — the European Conference on Computer
Systems**, the flagship conference of the European Chapter of ACM SIGOPS and one of the
handful of top-tier general systems venues. The pack covers the whole EuroSys arc:
deciding whether a project is EuroSys-shaped, running the distinctive **two-deadline
calendar** toward one April conference, surviving double-blind HotCRP review with its
three-way **accept / revise-and-resubmit (one-shot revision) / reject** outcomes, and converting acceptance
into an ACM camera-ready plus a badge-earning **sysartifacts** artifact.

Official basis **re-verified on 2026-11-24** by direct fetch: the EuroSys 2027 home page, Call
for Papers and Organizing Committee, the sysartifacts EuroSys 2027 artifact pages, the EuroSys
2026 home page, and the `eurosys.org` chapter and Test-of-Time pages. The original 2026-07-08
pass (also covering the ACM DL EuroSys proceedings and dblp) read the `*.eurosys.org` pages via
search-engine renderings because they were then blocked; the full trail, including everything
still marked 待核实, is in [`resources/official-source-map.md`](resources/official-source-map.md).

## What makes EuroSys different from its siblings

These verified mechanics drive most of the advice in the skills — and most of the
mistakes made by authors arriving from SOSP, OSDI, or NSDI habits:

- **Two juries, one April conference.** Each edition accepts papers through two
  independent rounds (for 2027: spring, papers May 14, 2026; fall, papers
  September 24, 2026), both publishing in the same proceedings and presenting in Rabat
  in April 2027. Both 2027 rounds are closed; the EuroSys 2028 call is not yet out.
- **A short author response.** Each round releases reviews a few days before an optional
  response (2027 fall: reviews January 6, responses January 8, 2027), limited to factual
  corrections and answers to reviewer questions, no new experiments, ideally 500 words.
- **Three-way outcomes.** A submission is accepted (tentatively, until a PC shepherd
  approves the revision), rejected, or offered **revise-and-resubmit** to the following
  cycle with a list of specific concerns — no guarantee of acceptance.
- **A one-year price for rejection.** A paper rejected at a round may not return until
  the *same round of the next edition* — premature submission costs a season plus a year.
- **12 technical pages, free references.** The SIGPLAN template the CFP encourages
  (`acmart[sigplan,twocolumn,review,anonymous]` in LaTeX), a 178 x 229 mm text block,
  ≥10-point type, an optional separate supplementary file, and at most three submissions
  per author per round.
- **Disclose AI use; ACM open access.** ACM's authorship policy requires any AI-tool use to
  be fully disclosed in the submission; authors outside ACM Open institutions pay an APC
  (2027 subsidized: $500 ACM/SIG members, $750 non-members).
- **sysartifacts artifact evaluation.** Optional, post-notification, three badges
  (Available / Functional / Reproduced, in three allowed combinations), and a
  Distinguished Artifact award (named the Gilles Muller Best Artifact Award at earlier
  editions).
- **A community with institutions.** The European SIGOPS chapter runs a Test-of-Time
  Award, the Roger Needham PhD Award, the Jochen Liedtke Young Researcher Award, and a
  Shadow PC that trains the reviewers who will eventually read your paper.

## Skills

| Skill | What it does |
| --- | --- |
| [`eurosys-topic-selection`](skills/eurosys-topic-selection/SKILL.md) | Test the project against the substance bar (built thing, transferable idea, realistic evidence, retellable insight) and route among EuroSys, SOSP, OSDI, NSDI, ASPLOS, ATC, FAST, and SoCC. |
| [`eurosys-workflow`](skills/eurosys-workflow/SKILL.md) | Run the two-gate calendar: pick the spring or fall gate by maturity, backward-plan to the abstract week, and branch cleanly on accept / revision / reject. |
| [`eurosys-writing-style`](skills/eurosys-writing-style/SKILL.md) | Build the pain → structural gap → insight → system → scoped-numbers arc, budget the 12 pages, and write evaluation sections that answer named questions. |
| [`eurosys-related-work`](skills/eurosys-related-work/SKILL.md) | Sweep the systems circuit (including EuroSys's own 2006– back catalog on dblp), state technical deltas, and manage workshop/arXiv/prior-round lineage. |
| [`eurosys-experiments`](skills/eurosys-experiments/SKILL.md) | Design the four-layer evidence stack — end-to-end, decomposition, cost, boundary — with tuned baselines and workload realism that survives the PC's default suspicion. |
| [`eurosys-reproducibility`](skills/eurosys-reproducibility/SKILL.md) | Keep a provenance ledger per reported number, tame run-to-run variance, and write availability statements for both double-blind review and the AEC. |
| [`eurosys-supplementary`](skills/eurosys-supplementary/SKILL.md) | Decide what leaves the 12 pages — free references, anonymized artifact repo, appendix if the round allows one — without exporting decision-critical evidence. |
| [`eurosys-artifact-evaluation`](skills/eurosys-artifact-evaluation/SKILL.md) | Target the right badge set, build for an evaluator on foreign hardware, mint the archival DOI, and aim at the Distinguished Artifact award (formerly the Gilles Muller award) rather than a minimal pass. |
| [`eurosys-submission`](skills/eurosys-submission/SKILL.md) | Final HotCRP audit: abstract and paper gates, page budget, template mode, identity sweep, dual-submission and resubmission-ban checks. |
| [`eurosys-review-process`](skills/eurosys-review-process/SKILL.md) | Model the two-round decision machinery, the outcome triple, the resubmission ban, and what actually moves a systems PC discussion. |
| [`eurosys-author-response`](skills/eurosys-author-response/SKILL.md) | Sort reviews into outcome bins, write score-moving rebuttals, and convert a revision offer's condition list into an executable plan. |
| [`eurosys-camera-ready`](skills/eurosys-camera-ready/SKILL.md) | Flip the template out of anonymous mode, clear the ACM eRights/metadata pipeline, couple badges to the final PDF, and plan the Rabat presentation. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Twelve official sources with URLs and access dates, verified 2027-cycle facts, the access-method note, and the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes to run before any upload. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Award-verified exemplars from Dryad (EuroSys '07) through CacheBlend (EuroSys '25), each with a positioning lesson and self-check, plus a systems-canon misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional LSM-compaction paper's abstract and introduction rebuilt before → after into the EuroSys arc. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility kit plus the four EuroSys-specific checks (badges, hardware honesty, anonymity, provenance) that generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./EuroSys-Skills
claude plugin install eurosys-skills
```

Or use the files directly: each `skills/eurosys-*/SKILL.md` is a standalone instruction
file whose frontmatter `description` tells an agent when to trigger it. Typical
invocations:

- "Is this scheduler paper EuroSys or SOSP material?" → `eurosys-topic-selection`
- "We're aiming at the fall gate — build the plan" → `eurosys-workflow`
- "Audit the PDF before I register the abstract" → `eurosys-submission`
- "We got a revise-and-resubmit offer — now what?" → `eurosys-author-response`
- "Package the cluster experiments for the AEC" → `eurosys-artifact-evaluation`

## Pack structure

```text
EuroSys-Skills/
├── .claude-plugin/              # plugin.json + marketplace.json (12 skills declared)
├── README.md                    # this file
├── README.zh-CN.md              # 中文说明
├── LICENSE                      # MIT
├── assets/cover.svg             # pack cover
├── skills/
│   └── eurosys-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md                # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md           # adapter to the shared repro kit
```

## 2027-cycle anchor facts (snapshot, not permanent rules)

- EuroSys 2027: **Rabat, Morocco, April 2027** (the official page says both April 19—22 and
  April 19 to 23 — end date 待核实); EuroSys 2026 was the 21st edition, Edinburgh, UK, April
  27–30, 2026. EuroSys 2028: no call published on 2026-11-24.
- Spring round (closed): abstracts **May 7, 2026**, papers **May 14, 2026**, responses July
  31, notification **August 21, 2026**, camera-ready **September 25, 2026**.
- Fall round (under review): abstracts **September 17, 2026**, papers **September 24, 2026**
  (AoE), reviews January 6, responses January 8, notification **January 29, 2027**,
  camera-ready **March 5, 2027**.
- Format: **12 pages technical content + unlimited references**; SIGPLAN template
  (`acmart[sigplan,twocolumn,review,anonymous]`); 178 x 229 mm block, columns ≥ 8 mm apart;
  double-blind; three submissions per author per round.
- Outcomes: accept (shepherded) / **revise-and-resubmit** (concerns, next cycle) / reject
  (ineligible for the immediately following cycle).
- Chairs: General Chairs Rachid Guerraoui and Rafael Pires; PC Chairs Pramod Bhatotia, Lydia
  Chen and Andreas Haeberlen.
- Portals: `eurosys27-spring.hotcrp.com` / `eurosys27-fall.hotcrp.com`. Proceedings: ACM
  DL (open access). Artifacts: sysartifacts, badges Available / Functional / Reproduced.

## Fact discipline

The pack keeps three classes of statement distinguishable:

1. **Verified cycle facts** — trace to a numbered source in the source map (deadlines,
   page budget, outcome policy).
2. **Reported facts** — found only in secondary renderings and labeled as such
   (acceptance counts).
3. **待核实 items** — phrased as questions to resolve, never as facts (the 2027 end date,
   fall artifact dates, camera-ready page allowance, anything about EuroSys 2028).

If a skill statement presents class 2 or 3 material as class 1, treat it as a bug and fix
it against the live official pages.

## Maintenance notes

- Every date above is a **2027-cycle snapshot**: reopen `202N.eurosys.org` and the
  round's HotCRP instance before deadline-sensitive advice.
- EuroSys sets policy per edition *and per round*; never carry rebuttal, appendix, or
  camera-ready assumptions across rounds without rechecking.
- Chairs rotate per edition; the chapter (eurosys.org) is the stable institution, the
  conference sites are the volatile ones.
- When adding exemplars, follow the two-source verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md); the systems canon
  is full of venue misattributions.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
