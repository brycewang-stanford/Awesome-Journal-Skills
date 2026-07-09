# PODS Skills

Twelve agent skills for papers targeting **PODS — the ACM SIGMOD/SIGACT Symposium on Principles of
Database Systems**, the database-**theory** symposium held jointly with SIGMOD every year. The pack
covers the full arc of a PODS campaign: deciding whether a project is a *theorem* (PODS) or a *system*
(SIGMOD/VLDB/ICDE) — and PODS versus its sister theory venue ICDT; writing a paper that leads with a
precise model and a precise result; building the analytical evidence a theory reviewer trusts (matching
upper and lower bounds, complete classifications, correctly stated assumptions); packaging the
lightweight double-anonymous EasyChair submission with its complete proof appendix; navigating the
multi-cycle calendar and the shepherded **revision** round; and delivering the **PACMMOD PODS-track**
camera-ready plus the full version on arXiv.

Official basis checked on **2026-07-09**: the PODS 2026 (Bengaluru) and PODS 2027 (Huntington Beach)
research calls and Important Dates pages, the PACMMOD PODS-track pages, the PODS EasyChair site, and the
sigmod.org PODS awards pages. Direct fetches of `sigmod.org` and `dl.acm.org` returned 403 in the
verification environment, so official pages were read via search-engine renderings of the exact URLs and
cross-checked against the ACM Digital Library (PACMMOD), dblp, and the databasetheory.org community
mirror; the full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Name-collision warning: **PODC** is the ACM Symposium on Principles of *Distributed* Computing, a
> different venue, and **ICDT** is PODS's sister database-theory conference in the EDBT/ICDT federation.
> No fact in this pack derives from confusing them with PODS.

## What makes PODS different from its siblings

These venue mechanics, verified for the 2026/2027 cycles, drive most of the advice in the skills — and
most of the mistakes made by authors arriving from a systems-DB flagship or from a pure-theory venue:

- **The contribution is a theorem, not a system.** PODS papers are models, bounds, dichotomies, logic,
  and provably optimal algorithms. A benchmark win belongs at SIGMOD/VLDB/ICDE; PODS reviewers read
  your proofs.
- **Multiple submission cycles per year.** PODS runs **two cycles** (PODS 2026: papers 10 Jun 2025 and
  10 Dec 2025). A reject is only a season from another chance — but a resubmission embargo applies, so
  premature submission still costs.
- **A shepherded revision round.** First decisions are **accept / reject / revision**; a revision
  (minor or major) invites a revised version that a **shepherd** must find satisfactory before
  acceptance — closer to a journal R&R than a plain rebuttal.
- **Lightweight double-anonymous review.** Author names and affiliations are hidden, self-citations are
  third-person, and conflicts of interest are declared at submission — a change from PODS's older
  single-blind tradition.
- **The `acmsmall` budget, not sigconf.** `\documentclass[acmsmall,review,anonymous]{acmart}`, up to
  **15 pages excluding references**, plus **unlimited references**, plus a proof **appendix incorporated
  at submission** — PODS forbids online/external appendices, so every proof ships with the paper.
- **No artifact evaluation; the "artifact" is the proof.** As a theory venue PODS has no systems
  artifact track and no ACM badges. The analogue is a complete proof appendix and, by community norm, a
  **full version on arXiv**, DOI-linked to the PACMMOD article.
- **Publication in PACMMOD, presented at PODS.** Accepted papers appear in the **PODS track of the
  Proceedings of the ACM on Management of Data** and are invited for presentation at the symposium.

## Skills

| Skill | What it does |
| --- | --- |
| [`pods-topic-selection`](skills/pods-topic-selection/SKILL.md) | Route between PODS and its siblings (SIGMOD/VLDB/ICDE systems, ICDT theory, LICS/ICALP, TODS/JACM) using the theorem-vs-system and result-swap tests. |
| [`pods-workflow`](skills/pods-workflow/SKILL.md) | Plan the project across PODS's multiple cycles: abstract-then-paper deadlines, the 48-hour rebuttal, the shepherded revision, PACMMOD camera-ready, and the arXiv full version. |
| [`pods-writing-style`](skills/pods-writing-style/SKILL.md) | Lead with a precise model and result, state theorems exactly, match bounds, and keep every proof complete and double-anonymous within the acmsmall budget. |
| [`pods-related-work`](skills/pods-related-work/SKILL.md) | Position at the level of *results* against PODS/ICDT/logic literature, write delta-first contrast, and keep self-citations double-anonymous. |
| [`pods-experiments`](skills/pods-experiments/SKILL.md) | Match rigor to the claim: matching lower bounds, dichotomy completeness, correct complexity assumptions, and only-when-needed empirical illustration. |
| [`pods-reproducibility`](skills/pods-reproducibility/SKILL.md) | Make the paper verifiable: a claim-to-proof map, self-contained appendix proofs, honest assumptions and scope, and the arXiv full-version norm. |
| [`pods-supplementary`](skills/pods-supplementary/SKILL.md) | Split body vs. at-submission appendix under the acmsmall budget, honoring PODS's no-external-appendix rule and double-anonymous hygiene. |
| [`pods-submission`](skills/pods-submission/SKILL.md) | Final EasyChair audit: cycle choice, abstract+COI registration, acmsmall format, the proof appendix, the anonymity sweep, and desk-risk triage. |
| [`pods-review-process`](skills/pods-review-process/SKILL.md) | Model the pipeline — lightweight double-anonymity, two rounds per cycle, accept/reject/revision, the shepherd — and where author leverage exists. |
| [`pods-author-response`](skills/pods-author-response/SKILL.md) | Write both turns: the ~48-hour rebuttal that corrects misreadings, and the revision cover letter that maps every required item to a concrete change. |
| [`pods-artifact-evaluation`](skills/pods-artifact-evaluation/SKILL.md) | The PODS analogue of artifact evaluation: formal-claims verification — complete proofs, a claim-to-proof map, and the arXiv full version, not badges. |
| [`pods-camera-ready`](skills/pods-camera-ready/SKILL.md) | De-anonymize, complete PACMMOD metadata, integrate shepherd-required fixes, and post + DOI-link the arXiv full version. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Eleven sources with URLs and access dates; verified 2026/2027 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five archival-verified PODS papers across five contribution shapes — Test-of-Time and Best-Paper honorees — with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional dichotomy paper's abstract and introduction rebuilt to the PODS arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared submission-readiness tooling, reframed for a theory paper (claim-to-proof matrix, proof-appendix checklist) — no code artifact, because PODS has none. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./PODS-Skills
claude plugin install pods-skills
```

Or use the files directly: each `skills/pods-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a PODS paper or should it go to SIGMOD/ICDT?" → `pods-topic-selection`
- "Audit my draft against the PODS research-track rules" → `pods-submission`
- "We got a revision — plan the shepherded resubmission" → `pods-author-response`
- "Get my proof appendix and arXiv full version ready" → `pods-artifact-evaluation`

## Pack structure

```text
PODS-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── pods-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared submission-readiness tooling
```

## Suggested use

1. **Before writing** — run `pods-topic-selection`; PODS and SIGMOD share a week but not a bar, and
   PODS and ICDT share a community but not a calendar. Skim the exemplars to see what decade-influential
   PODS contributions look like.
2. **While building the theory** — keep `pods-experiments` and `pods-reproducibility` beside the proofs;
   a matching lower bound and a complete appendix cannot be retrofitted after the deadline.
3. **While writing** — `pods-writing-style` for the body against the worked example,
   `pods-supplementary` for the body/appendix split, `pods-related-work` for result-level positioning.
4. **Deadline weeks** — register the abstract and COI before the earlier cutoff, then `pods-submission`
   end to end on the final PDF (body + references + appendix).
5. **After submission** — `pods-review-process` to calibrate, `pods-author-response` for the rebuttal
   and any revision round, then `pods-artifact-evaluation` and `pods-camera-ready` — or the routing
   table in `pods-topic-selection` if the decision goes the other way.

## 2026/2027-cycle anchor facts (historical snapshot, not permanent rules)

- PODS 2026 is the **45th** edition: Bengaluru, India, co-located with SIGMOD, **31 May – 5 June 2026**.
  Two cycles: papers **10 Jun 2025** and **10 Dec 2025** (abstracts a week earlier). PODS PC Chair Ke Yi
  (HKUST).
- PODS 2027 is the **46th** edition: Huntington Beach, California, USA, **13–19 June 2027**. Two cycles:
  Cycle 1 paper **30 May 2026**; Cycle 2 abstract+COI **10 Oct 2026**, paper **17 Oct 2026** (notify
  19 Jan 2027, revision 19 Feb 2027, final 12 Mar 2027). As of 2026-07-09 this **Cycle 2 is the live
  next deadline**.
- Format: **`acmsmall[review,anonymous]`**, **15 pages excl. references** + unlimited references + an
  at-submission appendix. Review: **lightweight double-anonymous** on **EasyChair**. Decisions:
  **accept / reject / revision** (shepherded). Publication: **PACMMOD PODS track**.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them distinguishable:

1. **Verified 2026/2027 facts** — carry dates/budgets and trace to a numbered source in the source map
   (e.g., the two-cycle calendar, the 15-page acmsmall budget, the PACMMOD publication).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the exact
   Cycle-2 rebuttal/notification dates for PODS 2026).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the first double-anonymous
   PODS edition, the PODS 2027 PC roster, the exact cross-cycle resubmission wording, any AI-use
   disclosure policy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it against
the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. PODS re-decides its structure per edition —
  including the number and timing of cycles — so verify the cadence before anything else each year.
- PODS has no standing editor-in-chief; the PODS PC Chair rotates per edition. PACMMOD is open access;
  the cost model is registration, and at least one author presents.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar result is not proof of
  a PODS placement (many database-theory landmarks are ICDT, LICS, or journal papers).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
