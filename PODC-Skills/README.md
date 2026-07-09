# PODC Skills

Twelve agent skills for papers targeting **PODC — the ACM Symposium on Principles of Distributed
Computing**, the SIGACT-SIGOPS flagship for the *theory* of distributed computing. The pack covers
the full arc of a PODC campaign: deciding whether a result is PODC-shaped or belongs at DISC, SPAA,
STOC/FOCS/SODA, or a systems venue; building the model, the theorem, and the proof to the standard
a distributed-theory committee enforces; packaging the **lightweight double-blind** HotCRP
submission with its 10-page merits budget and unbounded full version; choosing between a regular
paper and a **Brief Announcement**; and delivering the ACM proceedings camera-ready plus the arXiv
full version that carries the complete proofs.

Official basis checked on **2026-07-09**: the PODC 2026 call for papers and Important Dates, the
`podc.org` home and program-committee pages, the PODC 2026 HotCRP site, the ACM Digital Library
PODC proceedings, and dblp. Direct fetches of `podc.org` and `dl.acm.org` returned errors in the
verification environment, so official pages were read via search-engine renderings of the exact
URLs and cross-checked against dblp, the ACM DL proceedings, the DMANET call-for-papers
announcement, and wikicfp; the full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Name-collision warning: **PODC is not PODS.** `PODS` is the ACM Symposium on Principles of
> Database Systems (the SIGMOD-week database-theory venue); PODC is the distributed-computing-theory
> symposium. One letter, two different communities — no fact in this pack derives from PODS.

## What makes PODC different from its siblings

These venue mechanics, verified for the 2026 cycle, drive most of the advice in the skills — and
most of the mistakes made by authors arriving from a systems conference, from sequential theory, or
from DISC:

- **It is a proofs venue, not an artifacts venue.** PODC judges a **model, a theorem, and a proof**.
  There is no artifact evaluation and no badge track; the analogue of "does it run" is "does the
  proof close and are the model and failure assumptions stated honestly." A distributed *systems*
  paper with measurements but no analyzed guarantee is usually a mismatch.
- **The 10-page proceedings budget with an unbounded full version.** Accepted regular papers appear
  in **at most 10 pages** in **two-column ACM proceedings format**; the *submission* has no page
  limit, but only the abstract and the **first 10 pages after the title page** are guaranteed to be
  read — everything beyond is read at the committee's discretion. Authors are encouraged to submit
  the **full version** (with all proofs) as the submission.
- **Lightweight double-blind review.** PODC 2026 runs a lightweight double-blind process: the
  submission must not reveal author names, affiliations, or email addresses. This is a real change
  from PODC's historically single-blind norm — verify the exact wording each cycle.
- **A Brief Announcements track.** Alongside regular papers, PODC accepts **Brief Announcements**
  (submission at most 5 pages; published at up to 3 pages) for work in progress, results announced
  in full elsewhere, or bite-sized contributions — a real strategic option, not a consolation prize.
- **The arXiv full-version norm.** Posting the full version on arXiv (with all proofs) is standard
  and encouraged; PODC does not treat a preprint as a dual-submission problem, and the community
  reads the arXiv version for the proofs the 10 proceedings pages cannot hold.
- **A shared-award ecosystem with DISC.** The **Dijkstra Prize** (decade-of-impact) and the
  **Principles of Distributed Computing Doctoral Dissertation Award** are held **jointly by PODC and
  DISC**; the field treats the two conferences as one theory community with two annual meetings.
- **The distributed model is the whole game.** Message-passing vs. shared memory, synchronous vs.
  asynchronous vs. partial synchrony, crash vs. Byzantine vs. self-stabilizing faults, LOCAL vs.
  CONGEST, round/message/space complexity — the model and the cost measure decide correctness *and*
  novelty. This is what separates PODC from the sequential theory of STOC/FOCS/SODA.

## Skills

| Skill | What it does |
| --- | --- |
| [`podc-topic-selection`](skills/podc-topic-selection/SKILL.md) | Route between PODC and its neighbors (DISC, SPAA, OPODIS/SIROCCO/SSS, STOC/FOCS/SODA, ICDCS/DSN/OSDI, AFT/FC, and the PODS naming trap) by model, cost measure, and calendar. |
| [`podc-workflow`](skills/podc-workflow/SKILL.md) | Run the single-cycle year backward from the February deadline through the double-blind review, notification, camera-ready, and the arXiv full version. |
| [`podc-writing-style`](skills/podc-writing-style/SKILL.md) | Build the distributed-theory skeleton: model box, result statement up front, proof architecture, and the 10-page-merits discipline. |
| [`podc-related-work`](skills/podc-related-work/SKILL.md) | Position against the distributed-computing literature (PODC/DISC/SPAA/journals), write model-and-bound-precise deltas, and keep self-citation double-blind-safe. |
| [`podc-experiments`](skills/podc-experiments/SKILL.md) | The theory analogue of experiments: tight bounds, matching lower bounds, model/assumption stress-tests, and honest optional simulations. |
| [`podc-reproducibility`](skills/podc-reproducibility/SKILL.md) | Reproducibility for a proofs venue: a self-contained proof appendix, checkable model assumptions, and any optional-simulation transparency. |
| [`podc-supplementary`](skills/podc-supplementary/SKILL.md) | Split content between the 10 read-guaranteed pages and the full version/appendix so nothing that decides acceptance lives past page 10. |
| [`podc-submission`](skills/podc-submission/SKILL.md) | Final HotCRP audit: abstract registration, the ACM template and 10-page-merits budget, the double-blind sweep, regular-vs-Brief-Announcement choice, and desk-risk triage. |
| [`podc-review-process`](skills/podc-review-process/SKILL.md) | Model the pipeline — lightweight double-blind, a PC that reads proofs, accept/reject with no revision round — and where author leverage exists. |
| [`podc-author-response`](skills/podc-author-response/SKILL.md) | Write the rebuttal (if the cycle has one): correct proof misreadings, supply a missing lemma or bound, and stay inside the anonymity envelope. |
| [`podc-artifact-evaluation`](skills/podc-artifact-evaluation/SKILL.md) | PODC has **no artifact track** — this skill redirects that energy into proof-appendix completeness and model/assumption rigor, the real "evaluation" of a theory paper. |
| [`podc-camera-ready`](skills/podc-camera-ready/SKILL.md) | De-anonymize, compress to the 10-page ACM proceedings format without losing the proof map, complete ACM rights metadata, and post the full version to arXiv. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Sources with URLs and access dates; verified 2026 facts; the access-method note; the explicit 待核实 list; and the PODC-vs-PODS and PODC-vs-DISC guards. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Web-verified PODC papers across contribution shapes (population protocols, wait-free hierarchy, failure detectors, impossibility, distributed graph lower bounds) with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional consensus result's abstract and introduction rebuilt to the PODC arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter for the optional-simulation / proof-checking scripts a theory paper may ship, and the PODC-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./PODC-Skills
claude plugin install podc-skills
```

Or use the files directly: each `skills/podc-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a PODC paper or should it go to DISC/SPAA/PODS?" → `podc-topic-selection`
- "Audit my draft against the PODC 2026 call" → `podc-submission`
- "Should this be a regular paper or a Brief Announcement?" → `podc-submission` / `podc-supplementary`
- "Get my full version and proofs ready for arXiv and the 10-page camera-ready" → `podc-camera-ready`

## Pack structure

```text
PODC-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── podc-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to optional-simulation / proof tooling
```

## Suggested use

1. **Before writing** — run `podc-topic-selection`; PODC, DISC, and SPAA overlap, and the PODS
   naming trap is real, so choosing by model, cost measure, and calendar matters. Skim the exemplars
   library to see what decade-influential PODC contributions look like.
2. **While proving** — keep `podc-experiments` (the theory analogue: tight/matching bounds) and
   `podc-writing-style` beside the result; a model stated loosely and a proof gap found late cannot
   be retrofitted in the rebuttal.
3. **While writing** — `podc-writing-style` for the body against the worked example,
   `podc-supplementary` for the 10-page/full-version split, `podc-related-work` for
   model-and-bound-precise positioning.
4. **Deadline weeks** — register the abstract before the earlier cutoff, then `podc-submission` end
   to end on the double-blind PDF and the regular-vs-Brief-Announcement choice.
5. **After submission** — `podc-review-process` to calibrate, `podc-author-response` for any
   rebuttal, then `podc-camera-ready` and the arXiv full version — or the routing table in
   `podc-topic-selection` if the decision goes the other way.

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- PODC 2026 is the **45th** symposium: **Royal Holloway, University of London, Egham, England**,
  **July 6-10, 2026**, co-located with SPAA 2026. Sponsored jointly by **ACM SIGACT and SIGOPS**.
  Program Chair: **Eric Ruppert** (organizing/program page).
- **Calendar:** abstract registration **11 February 2026**, full-paper submission **16 February
  2026** (both 23:59 AoE), notification **29 April 2026**, camera-ready **20 May 2026**, via
  `podc26.hotcrp.com`.
- **Format:** ACM Master template (`acmart`), two-column proceedings. Regular submissions have **no
  page limit** but only the abstract and **first 10 pages after the title page** are guaranteed to
  be read; accepted regular papers appear in **≤10 proceedings pages**. **Brief Announcements**:
  submission **≤5 pages**, published **≤3 pages**.
- **Review:** **lightweight double-blind** (no author names/affiliations/emails in the submission).
  Decisions are accept/reject; there is **no journal-style revision round**.
- **Norms:** arXiv full version encouraged; selected papers invited to **JACM** and a special issue
  of **Distributed Computing**. Awards: **Best Paper**, **Best Student Paper**, **Best
  Presentation**; **Dijkstra Prize** and the **Doctoral Dissertation Award** are held jointly with
  DISC.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026 facts** — carry dates/budgets and trace to a numbered source in the source map
   (e.g., the Feb 11/16 deadlines, the 10-page merits budget, the lightweight double-blind rule,
   the ≤5/≤3-page Brief Announcement).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the exact
   organizing-committee roster beyond the named Program Chair).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., whether the 2026 cycle
   runs an author-response/rebuttal phase, the exact best-paper/award mechanics for 2026, and any
   generative-AI-use disclosure policy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. PODC re-decides details per edition —
  including whether the year runs a rebuttal phase and the exact double-blind wording — so verify
  the current call before anything else each year.
- PODC has no standing editor-in-chief; the rotating analogue is the per-edition Program Chair and
  committee, appointed under ACM SIGACT/SIGOPS. There is no APC; the cost model is registration, and
  at least one author presents each accepted paper in person.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a famous distributed-computing
  result may have appeared at DISC, STOC, FOCS, or in a journal (JACM, *Distributed Computing*)
  rather than at PODC.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
