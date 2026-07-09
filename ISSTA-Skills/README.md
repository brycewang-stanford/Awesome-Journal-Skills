# ISSTA Skills

Twelve agent skills for papers targeting **ISSTA — the ACM SIGSOFT International
Symposium on Software Testing and Analysis**, the flagship venue whose subject is,
specifically, the *testing and analysis* of software: test generation, fuzzing,
symbolic execution, static and dynamic analysis, fault localization, program repair
evaluation, sanitizers, and the empirical study of all of them. The pack walks the full
arc of an ISSTA campaign — deciding whether a project is testing-and-analysis material
or belongs at a broader software-engineering venue, building bug-finding and analysis
evidence that survives an ISSTA reviewer's scrutiny, packaging the double-anonymous
HotCRP submission, working the major-revision cycle, and delivering the camera-ready
plus an ACM-badged, Zenodo-archived artifact.

Official basis checked on **2026-07-09**: the ISSTA 2026 Research Papers call, the
important-dates page, the artifact-evaluation track, the SPLASH/ISSTA 2026 co-location
home, and the ACM Digital Library proceedings series. Direct fetches of
`conf.researchr.org` are frequently gateway-blocked, so official pages were read through
search-engine renderings of the exact URLs and cross-checked against the ISSTA HotCRP
site, the ACM Digital Library proceedings volumes, and dblp; the full trail, including
every item still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Who this pack is for

- Authors moving to ISSTA from a **broader SE venue** (ICSE, FSE, ASE) who need to know
  what the testing/analysis specialization sharpens and what it drops.
- Authors arriving from **ML conferences** who are used to leaderboard evidence and have
  to relearn evaluation as real subjects, fair baselines, and non-parametric statistics.
- Authors arriving from **PL/verification** (PLDI, POPL, CAV) whose analysis needs an
  empirical bug-finding story to fit ISSTA rather than a soundness proof alone.
- Anyone shepherding an ISSTA paper through the **Major-Revision** path, where the second
  phase is a real second chance rather than a soft reject.

## What makes ISSTA different from its siblings

These venue mechanics, verified for the 2026 cycle, drive most of the advice below — and
most of the mistakes made by authors arriving from ML conferences, from SE journals, or
from the broader SE conferences:

- **Testing and analysis is the whole scope, not a track.** ISSTA exists for techniques
  that *find, characterize, or reason about* software behaviour and defects. A paper whose
  core is a new requirements process or a human-studies result on developer teams is an
  ICSE/FSE contribution wearing an ISSTA costume; route it early.
- **A single main deadline with a real second phase.** ISSTA 2026 opened one research-paper
  deadline (January 29, 2026, AoE); first outcomes are Accept, **Major Revision**, or Reject,
  and Major-Revision papers revise against a fixed later deadline (May 21, 2026) for a
  terminal decision (June 25, 2026). Earlier cycles ran two rolling deadlines — the model is
  cycle-volatile, so re-check.
- **Double-anonymous by construction.** LaTeX submissions use the ACM `sigconf` template with
  the `review` (line numbers) and `anonymous` options; identity may not leak through text,
  self-citation phrasing, repository ownership, or PDF metadata.
- **One generous page box, not a two-column squeeze.** ISSTA 2026 set 18 pages for everything
  except references (all sections, figures, and appendices count against it), a change from the
  older 10+2 model — desk rejection is the named penalty for exceeding it or tampering with the
  format.
- **A first-class artifact and reproducibility culture.** ISSTA runs a strong artifact
  evaluation awarding ACM badges — *Artifacts Available* (Zenodo-archived), *Artifacts
  Evaluated — Functional* and *— Reusable*, and *Results Reproduced* — and the reviewer pool
  treats a runnable tool and a shared benchmark as normal, not exceptional.
- **Bug-finding evidence has its own standard.** Claims are graded on real subject programs and
  established benchmarks (Defects4J, real-world CVEs, fuzzing corpora), on fair tool baselines,
  and on statistically defensible comparison — non-parametric tests and effect sizes, not a
  single lucky run.

## Skills

| Skill | What it does |
| --- | --- |
| [`issta-topic-selection`](skills/issta-topic-selection/SKILL.md) | Decide whether a project is ISSTA-shaped or belongs at ICSE, FSE, ASE, ICST, PLDI/CAV, or an SE journal, and name the technique-plus-property at its core. |
| [`issta-workflow`](skills/issta-workflow/SKILL.md) | Run the year backward from the January deadline through the March response, the April decision, the May Major-Revision sprint, the June final decision, artifact evaluation, and October in Oakland. |
| [`issta-writing-style`](skills/issta-writing-style/SKILL.md) | Build the testing/analysis paper skeleton: threat model, technique, evaluation contract, a real threats-to-validity section, and 18-page discipline. |
| [`issta-related-work`](skills/issta-related-work/SKILL.md) | Position delta-first against the nearest technique across ISSTA, ICSE, FSE, ASE, ICST, and PL/verification venues, keeping self-citation double-anonymous. |
| [`issta-experiments`](skills/issta-experiments/SKILL.md) | Match evidence to claim shape: real subjects, established benchmarks, fair equal-budget baselines, non-parametric tests, effect sizes, and bug-finding metrics. |
| [`issta-reproducibility`](skills/issta-reproducibility/SKILL.md) | Build the verifiability spine: pinned subjects and benchmark versions, seeds and budgets, non-determinism disclosure, and claim-to-evidence traceability. |
| [`issta-supplementary`](skills/issta-supplementary/SKILL.md) | Split content between the 18-page body and the artifact so nothing decision-critical lives only where reviewers may not look. |
| [`issta-submission`](skills/issta-submission/SKILL.md) | Audit the HotCRP record, the 18-page box, `sigconf`/`anonymous` formatting, double-anonymous integrity, and the phase-one deadline sequence. |
| [`issta-author-response`](skills/issta-author-response/SKILL.md) | Draft the rebuttal and, when the outcome is Major Revision, convert every reviewer comment into a tracked revision ledger. |
| [`issta-review-process`](skills/issta-review-process/SKILL.md) | Reason about the double-anonymous review, the Major-Revision phase, the named evaluation criteria, and how the decision is synthesized. |
| [`issta-artifact-evaluation`](skills/issta-artifact-evaluation/SKILL.md) | Package a tool, benchmark, and results for the ACM badges (Available / Functional / Reusable / Results Reproduced) with a Zenodo deposit. |
| [`issta-camera-ready`](skills/issta-camera-ready/SKILL.md) | De-anonymize, apply the final `sigconf` layout, complete the ACM rights and DOI, display the artifact badges, and prepare the ACM DL package. |

## The 2026 cycle at a glance (verify every date each edition)

| Milestone | ISSTA 2026 date | Note |
| --- | --- | --- |
| Research-paper submission | January 29, 2026 (AoE) | Single main deadline; HotCRP |
| Author response | March 24-26, 2026 | Short window; reply early and precisely |
| First notification | April 16, 2026 | Accept / Major Revision / Reject |
| Major-Revision deadline | May 21, 2026 | Resubmit with a reviewer-comment ledger |
| Final notification | June 25, 2026 | Terminal decision for revised papers |
| Symposium | October 3-9, 2026 | Oakland, California; co-located with SPLASH |

## How the twelve skills fit together

Start with `issta-topic-selection` and `issta-workflow` to route the project and lay out the
year. Build evidence with `issta-experiments` and `issta-reproducibility`, then shape the paper
with `issta-writing-style`, `issta-related-work`, and `issta-supplementary`. Package and file it
with `issta-submission` and `issta-artifact-evaluation`. When reviews land, work
`issta-review-process` and `issta-author-response` — and, on acceptance, `issta-camera-ready`.
The [`resources/`](resources/README.md) directory backs all of this with verified sources,
award-certified exemplars, and a worked first-page rewrite.

## Maintenance notes

- Reopen the current-cycle official pages before any deadline-sensitive advice; the submission
  model is the single most volatile part of ISSTA.
- Treat the ISSTA 2026 facts here as historical anchors, not permanent rules — the number of
  deadlines, the page limit, the badge set, and the criteria have all changed across editions.
- Verify the current artifact-evaluation call each year; badge names and the Zenodo requirement
  are cycle-specific.
- Confirm the live venue: ISSTA 2026 is co-located with SPLASH in Oakland, California
  (October 3-9, 2026); ISSTA 2027 is announced for Singapore with dates still 待核实.
