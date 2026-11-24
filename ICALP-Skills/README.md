# ICALP Skills

Twelve agent skills for papers targeting **ICALP — the EATCS International Colloquium on Automata,
Languages, and Programming**, Europe's flagship theoretical-computer-science conference and the annual
meeting of the European Association for Theoretical Computer Science. The pack covers the full arc of
an ICALP campaign: deciding whether a result is ICALP-shaped and whether it is a **Track A**
(algorithms, complexity, games) or **Track B** (automata, logic, semantics) paper; writing a theorem
paper that a subject-expert referee will *check*; packaging the lightweight double-blind HotCRP
submission (no page limit, but the first ten pages must carry the result); handling the Track B
rebuttal; and
delivering the open-access **LIPIcs** camera-ready.

Official basis **re-verified 2026-11-24** by direct fetch: the ICALP 2027 (54th, Kraków) home,
Track B call and committees pages, both ICALP 2027 HotCRP sites, the ICALP 2026 call and site, and
the EATCS series page. The pack now describes **ICALP 2027**; its Track A call and the February-round
dates were not yet posted. That re-check also **corrected a long-standing error**: the "15-page
extended abstract" rule belonged to ICALP 2025 — ICALP 2026 and the ICALP 2027 Track B call have **no
page limit**. The original 2026-07-09 pass read several hosts via search-engine renderings when they
returned 403; the full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Sibling-venue warning: ICALP is **not** STOC, FOCS, or SODA (the US ACM/SIAM theory venues), and not
> LICS. It is EATCS's European flagship, published open-access in LIPIcs, two-track.
> No fact in this pack is carried over from those venues.

## What makes ICALP different from its siblings

These venue mechanics, verified for the ICALP 2027 cycle (Track B call) and ICALP 2026, drive most of the advice in the skills — and most
of the mistakes made by authors arriving from a US theory venue, a systems/ML venue, or a journal:

- **Two tracks, two committees, two HotCRP servers.** **Track A — Algorithms, Complexity and Games**
  and **Track B — Automata, Logic, Semantics and Theory of Programming**. Choosing the track is a real
  decision with real consequences (Track B has a rebuttal; in ICALP 2026 Track A did not).
- **February deadline — and, for Track B, a September round.** Track A has one February deadline
  (ICALP 2026: abstract 3 Feb, submission 6 Feb, AoE); a miss costs a full year. From **ICALP 2027**,
  Track B runs **two rounds** — round 1 closed 15 Sep 2026 (notification 8 Dec 2026), round 2 in
  February 2027 (dates TBA) — and a paper may enter only one.
- **No page limit, but a ten-page window.** Authors are encouraged to submit the **full version**;
  the first **ten pages** after the title page must present the merits, contributions and key ideas,
  and the rest is read at the PC's discretion. Single column, readable fonts (e.g. 11-point); the
  LIPIcs class is recommended, and the camera-ready is **LIPIcs `lipics-v2021`**. (The 15-page cap
  was ICALP 2025's rule.)
- **AI-use disclosure.** The ICALP 2027 call requires AI use in conducting the research to be
  disclosed in the paper, with specific uses described.
- **Lightweight double-blind.** Submissions are anonymous with third-person self-citation, but the
  regime is deliberately lightweight — an unbiased first read, not undiscoverable authorship.
  (Historically ICALP was single-blind; recent cycles adopted lightweight double-blind — verify per
  cycle.)
- **Asymmetric author interaction.** **Track B** has a rebuttal window in each round (2027 round 1:
  5-9 November 2026; 2026: 21-24 March); in ICALP 2026 **Track A** contacted authors only about
  **correctness**. There is **no revision round** — the submission must be
  correct at the deadline.
- **No artifact evaluation.** ICALP is pure theory: the contribution is a **theorem**, and the analogue
  of an "artifact" is the **full version with complete proofs** (plus optional formalization). This
  pack adapts the usual artifact/reproducibility skills to **proof rigor**.
- **Open access in LIPIcs.** Proceedings appear at Schloss Dagstuhl under Creative Commons, free to
  read, with no reader paywall — the EATCS/European open-access model, not an ACM/IEEE one.

## Skills

| Skill | What it does |
| --- | --- |
| [`icalp-topic-selection`](skills/icalp-topic-selection/SKILL.md) | Decide ICALP vs STOC/FOCS/SODA/LICS or a journal, and Track A vs Track B, by contribution shape, referee community, and the calendar (February; Track B also September). |
| [`icalp-workflow`](skills/icalp-workflow/SKILL.md) | Run the year backward from the February deadline (or Track B's September round), through abstract registration, the Track B rebuttal, notification, and the LIPIcs camera-ready. |
| [`icalp-writing-style`](skills/icalp-writing-style/SKILL.md) | Build the theory skeleton: model before theorem, a legible statement and its improvement on page one, proofs the referee can check, with the case made in the first ten pages. |
| [`icalp-related-work`](skills/icalp-related-work/SKILL.md) | Position against the best known bounds, credit the right TCS venues and journal versions, and keep self-citations third-person under double-blind. |
| [`icalp-experiments`](skills/icalp-experiments/SKILL.md) | Match the proof strategy to the claim shape and handle computation that legitimately supports a theorem (SAT/SMT certificates, exhaustive base cases) without becoming an experimental paper. |
| [`icalp-reproducibility`](skills/icalp-reproducibility/SKILL.md) | Make the result checkable: complete, self-contained proofs, a full version, reproducible certificates, and optional Coq/Lean/Isabelle formalization. |
| [`icalp-supplementary`](skills/icalp-supplementary/SKILL.md) | Split the paper by decision-criticality: the first ten pages earn belief, the rest of the full version earns verification, and nothing that decides acceptance hides past page ten. |
| [`icalp-submission`](skills/icalp-submission/SKILL.md) | Final HotCRP audit: correct track server, the Track B round, the ten-page window, the AI-use disclosure, the double-blind sweep, the no-simultaneous-submission rule, format-reject triage. |
| [`icalp-review-process`](skills/icalp-review-process/SKILL.md) | Model the pipeline — two committees, correctness-centered refereeing, the Track B rebuttal vs Track A correctness contact, single accept/reject — and where author leverage exists. |
| [`icalp-author-response`](skills/icalp-author-response/SKILL.md) | Write the Track B rebuttal (or answer a Track A correctness query): fix misreadings, point to the exact lemma, concede real gaps, stay anonymous. |
| [`icalp-artifact-evaluation`](skills/icalp-artifact-evaluation/SKILL.md) | Understand why ICALP has no artifact track and what replaces it — so authors from a systems/ML venue do not build a package no one evaluates. |
| [`icalp-camera-ready`](skills/icalp-camera-ready/SKILL.md) | Convert to `lipics-v2021`, de-anonymize, complete LIPIcs metadata (ORCID/CCS/funding/related-version), reconcile with the full version, pass Dagstuhl production. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Fourteen sources with URLs and access dates; verified ICALP 2027 facts and ICALP 2026 history; the page-limit correction; the access-method note; the explicit 待核实 list; the machine-readable rules block. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces (ICALP, EATCS, HotCRP, LIPIcs/DROPS) plus cross-check sources when the gateway blocks a direct fetch, and author-side checks. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Seven web-verified ICALP papers across both tracks and seven contribution shapes — Best Paper and Best Student Paper honorees — with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional dynamic-graph result's abstract and introduction rebuilt to the ICALP arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared submission-readiness tooling, plus the ICALP-specific proof-and-anonymity checks a generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ICALP-Skills
claude plugin install icalp-skills
```

Or use the files directly: each `skills/icalp-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an ICALP Track A or Track B paper — or should it go to STOC/SODA?" → `icalp-topic-selection`
- "Audit my draft against the ICALP research-track rules" → `icalp-submission`
- "We got Track B reviews — help me write the rebuttal" → `icalp-author-response`
- "Get this accepted paper ready for the LIPIcs camera-ready" → `icalp-camera-ready`

## Pack structure

```text
ICALP-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json (12 skills declared)
├── README.md                  # this file
├── README.zh-CN.md            # 中文说明
├── LICENSE                    # MIT
├── assets/cover.svg           # pack cover
├── skills/
│   └── icalp-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md              # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md         # adapter to shared submission-readiness tooling
```

## Suggested use

1. **Before writing** — run `icalp-topic-selection`; the ICALP-vs-siblings *and* Track A-vs-B decision
   both matter. Skim the exemplars library to see what decade-influential ICALP contributions look
   like in each track.
2. **While proving** — keep `icalp-experiments` and `icalp-reproducibility` beside the work; a proof
   that is only believed, not written, cannot be accepted, and computation used in a proof must be
   checkable.
3. **While writing** — `icalp-writing-style` for the body against the worked example,
   `icalp-supplementary` for the body/appendix split, `icalp-related-work` for delta-first positioning.
4. **Deadline weeks** — register the abstract before any earlier registration cutoff, then `icalp-submission`
   end to end on the final PDF, on the correct track server.
5. **After submission** — `icalp-review-process` to calibrate, `icalp-author-response` for the Track B
   rebuttal (or a Track A correctness query), then `icalp-camera-ready` — or the routing table in
   `icalp-topic-selection` if the decision goes the other way.

## 2027-cycle anchor facts (snapshot, not permanent rules)

- ICALP 2027 is the **54th** edition: **Kraków, Poland**, **July 5-9, 2027**, hosted by
  Jagiellonian University and PTM, in person.
- **Calendar (AoE):** Track B round 1 — submission **15 Sep 2026**, rebuttal **5-9 Nov 2026**,
  notification **8 Dec 2026**; Track B round 2 and Track A — **TBA** (announced as early-mid
  February 2027).
- **Format:** no page limit; title page (title, abstract, no authors); merits within the first
  **ten** pages; single column, e.g. 11-point; LIPIcs class recommended; **LIPIcs `lipics-v2021`**
  for the camera-ready. AI use in the research disclosed in the paper.
- **Review:** lightweight **double-blind**; **Track A** algorithms/complexity/games, **Track B**
  automata/logic/semantics with rebuttal; **accept/reject**. Publication: **LIPIcs**, open access.
- **Chairs:** Track A **Saket Saurabh**, **Jukka Suomela**; Track B **Manuel Bodirsky**, **Ichiro
  Hasuo**; Proceedings Chair **Gabriele Puppis**.
- **Awards:** best paper and best student paper for each track; the colloquium also hosts the **EATCS
  Award**, **Presburger Award**, **EATCS Distinguished Dissertation Award**, and — alternately with
  STOC — the **Gödel Prize** (EATCS/ACM SIGACT).
- History: ICALP 2026 (53rd) was at Royal Holloway, July 7-10, 2026, co-located with PODC and SPAA
  (submission 6 Feb 2026, notification 20 Apr 2026, camera-ready 11 May 2026).

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2027 facts** — carry dates/limits and trace to a numbered source in the source map (the
   two-track structure, the Track B two-round process, the no-page-limit format, the AI-disclosure
   rule, LIPIcs publication).
2. **Reported facts** — read only via secondary sources and labeled as such (e.g., the DMANET
   "early-mid February 2027" estimate for round 2).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the ICALP 2027 Track A call
   and round-2 dates, whether Track A gains a rebuttal, the 2026 acceptance rate).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it against
the live official pages.

## Maintenance notes

- Every date and limit above is a **cycle snapshot**. ICALP re-decides details per edition — verify
  the dates, the page rule, the round structure, and the blinding regime on the current call before
  advising.
- ICALP has no standing editor-in-chief and no reader paywall; the PC chairs and local organizers
  rotate per edition under EATCS and the ICALP steering committee.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar theorem name is not
  proof of an ICALP placement (the PCP theorem was FOCS; AKS was a journal).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
