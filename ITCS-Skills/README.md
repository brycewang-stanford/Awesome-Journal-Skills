# ITCS Skills

Twelve agent skills for papers targeting **ITCS — the Innovations in Theoretical Computer
Science conference**, the theory venue built, from its 2010 founding, to reward **conceptual
novelty**: a new model, a new question, a surprising connection, a direction the field had not
thought to take. Where STOC and FOCS reward the deepest, most polished theorem of the year, ITCS
asks a different first question — *is this a new question worth asking?* — and the whole pack is
written to that ethos. It covers the full arc of an ITCS campaign: deciding whether an idea is
ITCS-shaped or belongs at STOC/FOCS/SODA/a journal; framing a conceptual contribution so a PC
sees the innovation before the theorem; assembling the lightweight double-blind LIPIcs
submission with **complete proofs**; understanding a **no-rebuttal** review; and delivering the
open-access LIPIcs camera-ready.

Official basis checked on **2026-07-09**: the ITCS 2026 (Bocconi, Milan) HotCRP site and
deadlines page, the `itcs-conf.org` calls for papers, the LIPIcs/DROPS proceedings (Vol 362 =
ITCS 2026), dblp's `conf/innovations` stream, the Bocconi Department of Computing Sciences ITCS
2026 page, and the Wikipedia history entry. Direct fetches of `itcs2026.hotcrp.com`,
`itcs-conf.org`, `cs.unibocconi.eu`, and `drops.dagstuhl.de` returned 403 in the verification
environment, so official pages were read via search-engine renderings of the exact URLs and
cross-checked across at least two independent surfaces; the full trail, including everything
still marked 待核实, is in [`resources/official-source-map.md`](resources/official-source-map.md).

> Acronym-collision warning: several unrelated venues abbreviate to "ITCS" (the IEEE Intelligent
> Transportation Systems Conference is *ITSC*; assorted "Information Technology and Computer
> Science / Convergence and Services" workshops appear on WikiCFP). **No fact in this pack
> derives from any of them** — every source resolves to *Innovations in Theoretical Computer
> Science*.

## What makes ITCS different from its siblings

These venue mechanics, verified for the 2026 cycle, drive most of the advice in the skills — and
most of the mistakes made by authors arriving from STOC/FOCS, from SODA, or from a journal:

- **Conceptual novelty is the selection criterion, not a tiebreaker.** ITCS explicitly seeks
  papers that introduce a new model, ask a new question, or forge an unexpected connection. A
  technically flawless but incremental result that would place at STOC/FOCS on depth can be
  passed over here for want of a *new idea* — and a bold, imperfect new direction can be
  accepted. Frame the innovation first.
- **Pure theory: ideas and proofs, no code.** There is **no artifact-evaluation track and no
  reproducibility package**. The analogue of "reproducibility" is a **complete, checkable
  proof**; the analogue of "artifact" is a **full-version appendix or arXiv/ECCC posting** that
  lets a reviewer verify every central claim.
- **One annual deadline, in early September.** ITCS 2026 closed **6 September 2025**, with
  notification in November and the conference the following January (Bocconi, 27-30 Jan 2026).
  There is a single research deadline per year — no rolling rounds, no second cycle.
- **Lightweight double-blind.** Submissions omit names, affiliations, and emails, but authors are
  **encouraged to post the full version to arXiv / ECCC / the Cryptology ePrint Archive**, and
  important references are **not** anonymized. It is "lightweight" because deanonymization via a
  preprint is tolerated rather than policed.
- **No rebuttal.** Following theory-conference norms, ITCS reaches accept/reject decisions
  **without an author-response round** and without a revise-and-resubmit. There is no second turn
  to argue in — the submission has to answer the reviewer's objections before it is sent.
- **LIPIcs open access, no APC.** Papers publish in **LIPIcs** (Schloss Dagstuhl) under the
  `lipics-v2021` class, open access, Creative-Commons-licensed, with **no article-processing
  charge**. This is the Dagstuhl path, not the ACM `acmart` or IEEE `IEEEtran` box.
- **Generous page budget with full proofs, and a 10-page merits window.** Submissions are single
  column, font >= 11pt, with **no hard page ceiling**; the norm is a first-10-page presentation
  of the paper's merits and significance, followed by **complete proofs** (in an appendix if
  needed).
- **The Graduating Bits culture.** A standing session of short talks by soon-to-graduate (on
  either side) researchers gives ITCS a smaller-community, direction-setting, people-first feel
  that shapes what the room rewards.

## Skills

| Skill | What it does |
| --- | --- |
| [`itcs-topic-selection`](skills/itcs-topic-selection/SKILL.md) | Route between ITCS and its siblings (STOC, FOCS, SODA, CCC, ICALP, a journal) using the conceptual-novelty test, the "new question worth asking" screen, and the single-deadline calendar. |
| [`itcs-workflow`](skills/itcs-workflow/SKILL.md) | Run the single-cycle year backward from the early-September deadline through the no-rebuttal review, November notification, LIPIcs camera-ready, and the January talk. |
| [`itcs-writing-style`](skills/itcs-writing-style/SKILL.md) | Build the ITCS first pages: the conceptual contribution and *why the question is new* before the theorem, an honest scope-and-limitations posture, full proofs deferred cleanly. |
| [`itcs-related-work`](skills/itcs-related-work/SKILL.md) | Position against the theory literature, write the "why this model/question is new" delta, and keep it honest under lightweight anonymity (references not anonymized). |
| [`itcs-experiments`](skills/itcs-experiments/SKILL.md) | Match evidence to a *theory* claim: proofs as the primary evidence, worked examples and separations, and the rare, well-scoped illustrative experiment or simulation. |
| [`itcs-reproducibility`](skills/itcs-reproducibility/SKILL.md) | Make the mathematics checkable: complete proofs, self-contained definitions, a full version on arXiv/ECCC, and dependency tracking of prior results. |
| [`itcs-supplementary`](skills/itcs-supplementary/SKILL.md) | Split content between the body and the appendix / full version by what a reviewer must verify — no central proof may live only in a preprint the PC need not read. |
| [`itcs-submission`](skills/itcs-submission/SKILL.md) | Final HotCRP audit: single-column >= 11pt format, the first-10-pages merits window, the lightweight double-blind sweep, full-proof completeness, and the archival-prior-publication check. |
| [`itcs-review-process`](skills/itcs-review-process/SKILL.md) | Model the pipeline — PC + external reviewers, conceptual-novelty weighting, lightweight double-blind, **no rebuttal**, accept/reject — and where (little) author leverage exists. |
| [`itcs-author-response`](skills/itcs-author-response/SKILL.md) | Handle the reality that ITCS has **no rebuttal**: pre-empt objections in the submission, and manage post-decision correspondence, resubmission routing, and the camera-ready window. |
| [`itcs-artifact-evaluation`](skills/itcs-artifact-evaluation/SKILL.md) | Adapt "artifact" to pure theory: the full-proof appendix and the arXiv/ECCC full version *are* the artifact — how to make claims independently verifiable without a code track. |
| [`itcs-camera-ready`](skills/itcs-camera-ready/SKILL.md) | De-anonymize, switch to the `lipics-v2021` class, complete LIPIcs metadata (ACM CCS, keywords, funding), and pass the Dagstuhl production checks for open-access publication. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Verified ITCS papers across conceptual-contribution shapes, with self-check questions and a sibling-venue guardrail. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional new-model paper's abstract and introduction rebuilt to the ITCS "innovation-first" arc, before -> after. |
| [`resources/code/README.md`](resources/code/README.md) | Why this pure-theory pack ships no code kit, and the proof-checkability passes that replace it. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ITCS-Skills
claude plugin install itcs-skills
```

Or use the files directly: each `skills/itcs-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an ITCS paper or should it go to STOC/FOCS/SODA?" -> `itcs-topic-selection`
- "Frame my new model so the innovation lands on page one" -> `itcs-writing-style`
- "Audit my draft against the ITCS submission rules" -> `itcs-submission`
- "There's no rebuttal at ITCS — what can I even do after the reviews?" -> `itcs-author-response`

## Pack structure

```text
ITCS-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── itcs-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # why no code kit; proof-checkability passes instead
```

## Suggested use

1. **Before writing** — run `itcs-topic-selection`; ITCS overlaps STOC/FOCS/SODA in scope but
   selects on a different axis (novelty of the question), so choosing correctly is the
   highest-leverage move. Skim the exemplars library to see what "innovation" looks like here.
2. **While framing** — keep `itcs-writing-style` and `itcs-related-work` beside the draft; the
   conceptual contribution and its novelty delta must be legible on the first pages, not mined
   out of Section 4.
3. **While proving** — `itcs-reproducibility` and `itcs-supplementary` for complete, checkable
   proofs and the body/appendix split; `itcs-experiments` only if an illustrative simulation
   genuinely helps a claim.
4. **Deadline week** — `itcs-submission` end to end on the final PDF: format, the 10-page merits
   window, the lightweight double-blind sweep, and full-proof completeness.
5. **After submission** — `itcs-review-process` to calibrate, `itcs-author-response` for the
   no-rebuttal reality and post-decision routing, then `itcs-camera-ready` for the LIPIcs
   production pass — or the routing table in `itcs-topic-selection` if the decision goes the
   other way.

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- ITCS 2026 is the **17th** edition: **Bocconi University, Milan, Italy, 27-30 January 2026**;
  abstract/registration 4 Sep 2025, submission 6 Sep 2025 (7:59:59 PM EDT), notification
  ~10 Nov 2025; via `itcs2026.hotcrp.com`. Proceedings: **LIPIcs Volume 362**.
- Publication: **LIPIcs** (Schloss Dagstuhl), open access, no APC, `lipics-v2021` class. Review:
  **lightweight double-blind**, **no rebuttal**, accept/reject.
- Format: single column, font >= 11pt, **no hard page limit**; first-10-page merits window;
  **complete proofs of all central claims** required (appendix allowed).
- ITCS 2027 host/dates/deadline are **待核实** as of 2026-07-09 — reopen the current call.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026 facts** — carry dates/format and trace to a numbered source in the source map
   (e.g., LIPIcs Vol 362, the early-September deadline, the lightweight double-blind rule, the
   no-rebuttal norm).
2. **Reported facts** — read only via a single secondary rendering and labeled as such (e.g., the
   ITCS 2026 program-chair name and local-organizer roster).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., ITCS 2027 host/dates,
   the camera-ready page limit, the 2026 acceptance rate and paper count).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date above is a **cycle snapshot**. ITCS rotates host and chairs per edition and has a
  single annual deadline; verify the current call before anything else each year.
- ITCS has no standing editor-in-chief and no APC; the program chair and PC rotate per edition.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a famous author or a
  familiar theorem is not proof of an ITCS placement (it may be STOC, FOCS, SODA, or a journal).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
