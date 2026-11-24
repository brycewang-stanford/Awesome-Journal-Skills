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
plus an ACM-badged, DOI-archived artifact.

Official basis first checked on 2026-07-09 and **re-verified 2026-11-24**: the ISSTA 2027
Research Papers call, the ISSTA 2027 important-dates and organizing-committee pages, the
ISSTA 2026 artifact-evaluation call (the latest posted), and the SPLASH/ISSTA 2026 home, all
fetched directly from `conf.researchr.org`. The pack now describes **ISSTA 2027** (Singapore,
September 7-10, 2027); the full trail, including every item still marked 待核实, is in
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

These venue mechanics, verified for the 2027 cycle, drive most of the advice below — and
most of the mistakes made by authors arriving from ML conferences, from SE journals, or
from the broader SE conferences:

- **Testing and analysis is the whole scope, not a track.** ISSTA exists for techniques
  that *find, characterize, or reason about* software behaviour and defects. A paper whose
  core is a new requirements process or a human-studies result on developer teams is an
  ICSE/FSE contribution wearing an ISSTA costume; route it early.
- **A single main deadline with a real second phase.** ISSTA 2027 has one research-paper
  deadline (mandatory abstract January 8, 2027; full paper January 11, 2027, AoE); first
  outcomes are Accept, **Major Revision**, or Reject, and Major-Revision papers get four weeks to
  revise against a fixed later deadline (May 20, 2027) for a terminal decision (June 17, 2027).
  New in 2027: a two-phase review (two reviewers first, early rejection if both are negative,
  otherwise a third) and a cap of 7 submissions per author. Earlier cycles ran two rolling
  deadlines — the model is cycle-volatile, so re-check.
- **Double-anonymous by construction.** LaTeX submissions use ACM `acmart` with
  `acmsmall,screen,review,anonymous` (single-column); identity may not leak through text,
  self-citation phrasing, repository ownership, or PDF metadata.
- **One generous single-column page box.** ISSTA 2027 sets 18 pages for everything except
  references and the required Data Availability section (all sections, figures, and appendices
  count against it), a change from the older two-column 10+2 model — desk rejection is the named
  penalty for exceeding it or ignoring the format.
- **A journal-style publication with a possible APC.** Accepted papers appear in **PACMSE**
  (Issue ISSTA 2027), open access; authors not covered by ACM OPEN may owe an APC (2027 amount
  to be announced; 2026 was US$250 ACM members / US$350 non-members).
- **A first-class artifact and reproducibility culture.** ISSTA runs a strong artifact
  evaluation awarding up to two ACM badges — *Artifacts Available* (DOI-issuing archive such as
  Zenodo), *Artifacts Evaluated — Functional* or *— Reusable* — every submission must carry a
  Data Availability section, and the reviewer pool treats a runnable tool and a shared benchmark
  as normal, not exceptional.
- **Bug-finding evidence has its own standard.** Claims are graded on real subject programs and
  established benchmarks (Defects4J, real-world CVEs, fuzzing corpora), on fair tool baselines,
  and on statistically defensible comparison — non-parametric tests and effect sizes, not a
  single lucky run.

## Skills

| Skill | What it does |
| --- | --- |
| [`issta-topic-selection`](skills/issta-topic-selection/SKILL.md) | Decide whether a project is ISSTA-shaped or belongs at ICSE, FSE, ASE, ICST, PLDI/CAV, or an SE journal, and name the technique-plus-property at its core. |
| [`issta-workflow`](skills/issta-workflow/SKILL.md) | Run the year backward from the January deadline through the March response, the April decision, the May Major-Revision sprint, the June final decision, artifact evaluation, and September in Singapore. |
| [`issta-writing-style`](skills/issta-writing-style/SKILL.md) | Build the testing/analysis paper skeleton: threat model, technique, evaluation contract, a real threats-to-validity section, and 18-page discipline. |
| [`issta-related-work`](skills/issta-related-work/SKILL.md) | Position delta-first against the nearest technique across ISSTA, ICSE, FSE, ASE, ICST, and PL/verification venues, keeping self-citation double-anonymous. |
| [`issta-experiments`](skills/issta-experiments/SKILL.md) | Match evidence to claim shape: real subjects, established benchmarks, fair equal-budget baselines, non-parametric tests, effect sizes, and bug-finding metrics. |
| [`issta-reproducibility`](skills/issta-reproducibility/SKILL.md) | Build the verifiability spine: pinned subjects and benchmark versions, seeds and budgets, non-determinism disclosure, and claim-to-evidence traceability. |
| [`issta-supplementary`](skills/issta-supplementary/SKILL.md) | Split content between the 18-page body and the artifact so nothing decision-critical lives only where reviewers may not look. |
| [`issta-submission`](skills/issta-submission/SKILL.md) | Audit the HotCRP record, the 18-page box, `acmsmall`/`anonymous` formatting, the Data Availability section, double-anonymous integrity, and the phase-one deadline sequence. |
| [`issta-author-response`](skills/issta-author-response/SKILL.md) | Draft the rebuttal and, when the outcome is Major Revision, convert every reviewer comment into a tracked revision ledger. |
| [`issta-review-process`](skills/issta-review-process/SKILL.md) | Reason about the double-anonymous review, the Major-Revision phase, the named evaluation criteria, and how the decision is synthesized. |
| [`issta-artifact-evaluation`](skills/issta-artifact-evaluation/SKILL.md) | Package a tool, benchmark, and results for the ACM badges (Available / Functional / Reusable) with a DOI-archived deposit. |
| [`issta-camera-ready`](skills/issta-camera-ready/SKILL.md) | De-anonymize, apply the final `acmsmall` layout, complete the ACM rights, APC/ACM OPEN step and DOI, display the artifact badges, and prepare the PACMSE package. |

## The 2027 cycle at a glance (verify every date each edition)

| Milestone | ISSTA 2027 date | Note |
| --- | --- | --- |
| Mandatory abstract | January 8, 2027 (AoE) | HotCRP record, abstract, authors, conflicts |
| Research-paper submission | January 11, 2027 (AoE) | Single main deadline; HotCRP |
| Author response | March 22-25, 2027 | Short window; reply early and precisely |
| First notification | April 20, 2027 | Accept / Major Revision / Reject (incl. early reject) |
| Major-Revision deadline | May 20, 2027 | Resubmit with a reviewer-comment ledger |
| Final notification | June 17, 2027 | Terminal decision for revised papers |
| Camera ready | July 22, 2027 | PACMSE package |
| Symposium | September 7-10, 2027 | Singapore |

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
- Treat the ISSTA 2027 facts here as edition anchors, not permanent rules — the number of
  deadlines, the page limit, the review phases, the badge set, and the criteria have all changed
  across editions.
- Verify the current artifact-evaluation call each year; badge names and the archival
  requirement are cycle-specific (the ISSTA 2027 AE call was not yet posted on 2026-11-24).
- Confirm the live venue: ISSTA 2027 is in Singapore (September 7-10, 2027); ISSTA 2026 was
  co-located with SPLASH in Oakland, California (October 4-9, 2026).
