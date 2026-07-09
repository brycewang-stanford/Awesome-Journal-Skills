# IEEE INFOCOM Skills

Twelve agent skills for papers targeting **IEEE INFOCOM — the IEEE International Conference on
Computer Communications**, the IEEE Communications Society (ComSoc) networking flagship and one of
the largest, broadest venues in computer networking. The pack covers the full arc of an INFOCOM
campaign: deciding whether a project is INFOCOM-shaped or belongs at SIGCOMM, NSDI, MobiCom, or an
IEEE/ACM networking journal; building the analytical-and-systems evidence an INFOCOM reviewer
expects; packaging the double-blind **EDAS** submission inside the strict **IEEEtran** two-column
page budget; surviving the automated review assignment and the **early-reject** phase; and
delivering the IEEE Xplore camera-ready.

Official basis checked on **2026-07-09**: the INFOCOM 2026 (Tokyo) and INFOCOM 2027 (Honolulu)
Call for Papers and Submission Guidelines pages, the Final Paper Submission Guidelines, the EDAS
portal, the ComSoc conference listing, IEEE Xplore, and dblp. Direct fetches of
`ieee-infocom.org`, `ieeexplore.ieee.org`, and the stats mirrors returned 403 in the verification
environment, so official pages were read via search-engine renderings of the exact URLs and
cross-checked against the ComSoc listing, the IEEE/Wikipedia INFOCOM history, dblp proceedings,
and community statistics; the full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes INFOCOM different from its siblings

These venue mechanics, verified for the 2026/2027 cycles, drive most of the advice in the skills —
and most of the mistakes made by authors arriving from SIGCOMM/NSDI, from a theory venue, or from
an IEEE journal:

- **It is a LARGE flagship, and selectivity comes from volume.** INFOCOM receives on the order of
  ~1,400-1,500 submissions and accepts roughly **18-20%** (INFOCOM 2025: 272 of 1,458 ≈ 18.7%).
  The scale — not a boutique PC — shapes everything: automated reviewer matching, an early-reject
  screen, and a broad reviewer pool spanning subareas.
- **IEEE, not ACM/USENIX.** Papers publish in the **IEEE INFOCOM Proceedings and IEEE Xplore**
  using the **IEEEtran** two-column template — `\documentclass[10pt, conference,
  letterpaper]{IEEEtran}`, version 1.8, 10pt Times. Do not carry an `acmart` single-column habit
  across.
- **A hard, appendix-inclusive page budget.** **10 pages maximum**, of which **≤9 pages** hold all
  text, figures, tables, **and appendices** — only references may spill into the 10th page. There
  is no separate supplementary channel; anything a reviewer must read lives inside the nine pages.
- **Double-blind, on EDAS, with automated assignment.** Submission runs through **EDAS**; the PDF
  must be anonymous (title page, body, metadata); and papers are matched to TPC members by an
  automated assignment system that compares your manuscript to reviewers' publications.
- **An early-reject phase and (traditionally) no author rebuttal.** INFOCOM 2027 posts an
  **early-reject notification (9 Oct 2026)** well before final decisions (8 Dec 2026). Distinct
  from SIGCOMM/NSDI, INFOCOM has **traditionally not offered a standard author rebuttal** — the
  submitted PDF must defend itself. Whether a cycle adds a response window is 待核实 each year.
- **A five-paper-per-author cap.** An individual may appear on **at most five** submissions to a
  given INFOCOM; excess papers past the first five are dropped.
- **An analytical/optimization tradition alongside systems.** INFOCOM's scope is broad — wireless,
  protocols, edge/IoT, measurement — but it retains a strong **modeling/theory** culture
  (queueing, scheduling, optimization, game theory, network economics) where a theorem with a
  proof and a simulation is a first-class contribution, not a second-class one.

## Skills

| Skill | What it does |
| --- | --- |
| [`infocom-topic-selection`](skills/infocom-topic-selection/SKILL.md) | Route between INFOCOM and its siblings (SIGCOMM, NSDI, MobiCom, ICNP, IEEE/ACM ToN, JSAC) using contribution shape, the modeling-vs-building axis, and the calendar. |
| [`infocom-workflow`](skills/infocom-workflow/SKILL.md) | Run the single-summer cycle backward from the late-July deadline through the abstract-then-paper step, the early-reject checkpoint, notification, IEEE Xplore camera-ready, and presentation. |
| [`infocom-writing-style`](skills/infocom-writing-style/SKILL.md) | Build the networking-paper skeleton: problem and system model up front, theorems or protocol design that pay off, evaluation on real or simulated networks, all inside the nine-page budget. |
| [`infocom-related-work`](skills/infocom-related-work/SKILL.md) | Cover the networking literature lanes, write delta-first positioning, and keep self-citations double-blind on EDAS. |
| [`infocom-experiments`](skills/infocom-experiments/SKILL.md) | Match evidence to claim shape: analysis with assumptions stated and proved, simulation with a named simulator and seeds, testbed/measurement with real traffic, and honest baselines. |
| [`infocom-reproducibility`](skills/infocom-reproducibility/SKILL.md) | Make results checkable without a formal artifact track: pin the simulation setup, release code/datasets where possible, and keep proofs and parameters inside the page budget. |
| [`infocom-supplementary`](skills/infocom-supplementary/SKILL.md) | Live within the nine-page, appendix-inclusive budget: decide what fits, what compresses, and why there is no supplementary escape hatch at review time. |
| [`infocom-submission`](skills/infocom-submission/SKILL.md) | Final EDAS audit: the abstract-then-paper metadata step, the IEEEtran page budget, the double-blind sweep, the five-paper cap, and desk-risk triage before the AoE cutoff. |
| [`infocom-review-process`](skills/infocom-review-process/SKILL.md) | Model the pipeline — high volume, automated assignment, double-blind, early-reject, TPC discussion, and (traditionally) no rebuttal — and where author leverage exists. |
| [`infocom-author-response`](skills/infocom-author-response/SKILL.md) | Handle the honest reality: write a self-defending submission because there is usually no rebuttal, and act correctly on an early-reject, a reject, or any response window a cycle does offer. |
| [`infocom-artifact-evaluation`](skills/infocom-artifact-evaluation/SKILL.md) | Package code and data for credibility and IEEE reproducibility badges even though INFOCOM runs no standing artifact-evaluation track, and know what that absence changes. |
| [`infocom-camera-ready`](skills/infocom-camera-ready/SKILL.md) | De-anonymize, pass **PDF eXpress**, complete the **IEEE eCF** copyright form, meet the author-registration rule, and clear IEEE Xplore production checks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026/2027 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Verified INFOCOM papers across contribution shapes — analytical, protocol, and measurement — with self-check questions and sibling-venue guards. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional edge-scheduling study's abstract and introduction rebuilt to the INFOCOM arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the INFOCOM-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./INFOCOM-Skills
claude plugin install infocom-skills
```

Or use the files directly: each `skills/infocom-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an INFOCOM paper or should it go to SIGCOMM/NSDI?" → `infocom-topic-selection`
- "Audit my draft against the INFOCOM IEEEtran page budget and double-blind rules" → `infocom-submission`
- "We got an early-reject — what now?" → `infocom-author-response`
- "Get this camera-ready through PDF eXpress and IEEE Xplore" → `infocom-camera-ready`

## Pack structure

```text
INFOCOM-Skills/
├── .claude-plugin/               # plugin.json + marketplace.json (12 skills declared)
├── README.md                     # this file
├── README.zh-CN.md               # 中文说明
├── LICENSE                       # MIT
├── assets/cover.svg              # pack cover
├── skills/
│   └── infocom-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md                 # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md            # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `infocom-topic-selection`; INFOCOM overlaps SIGCOMM/NSDI/MobiCom in
   scope, so choosing by contribution shape and calendar matters. Skim the exemplars library to
   see what INFOCOM analytical and systems contributions look like.
2. **While building evidence** — keep `infocom-experiments` and `infocom-reproducibility` beside
   the study; a simulator's seeds and a proof's assumptions cannot be retrofitted.
3. **While writing** — `infocom-writing-style` for the body against the worked example,
   `infocom-supplementary` for the nine-page, appendix-inclusive budget, `infocom-related-work`
   for delta-first positioning.
4. **Deadline weeks** — enter the abstract/metadata a week early, then `infocom-submission` end to
   end on the final anonymized PDF in EDAS.
5. **After submission** — `infocom-review-process` to calibrate, `infocom-author-response` for the
   early-reject checkpoint and any response window, then `infocom-camera-ready` — or the routing
   table in `infocom-topic-selection` if the decision goes the other way.

## 2026/2027-cycle anchor facts (historical snapshot, not permanent rules)

- INFOCOM 2026 is the **45th** edition: Tokyo, Japan, **18-21 May 2026**. Abstract due 24 Jul 2025;
  full paper 31 Jul 2025 (AoE); notification 8 Dec 2025; camera-ready 9 Jan 2026. EDAS `N33581`.
- INFOCOM 2027 is the **46th** edition: Honolulu, HI, USA, **24-27 May 2027**; abstract 24 Jul
  2026, full paper 31 Jul 2026 (AoE); **early-reject 9 Oct 2026**; acceptance 8 Dec 2026. This is
  the live next research target as of 2026-07-09.
- Publication: **IEEE Xplore**. Format: **IEEEtran** two-column, **10 pages max / ≤9 pages of
  text incl. appendices**. Review: **double-blind** on **EDAS** with automated assignment; ≤5
  papers per author; traditionally **no rebuttal** (待核实 per cycle).

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026/2027 facts** — carry dates/budgets and trace to a numbered source in the source
   map (e.g., the IEEEtran 10/9-page budget, the EDAS double-blind rule, the early-reject date).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., historical
   acceptance rates from statistics mirrors).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., whether the current cycle
   offers any rebuttal, any artifact-evaluation track, the full TPC Co-Chair roster, AI-disclosure
   policy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. INFOCOM re-decides its structure per edition
  — including whether an early-reject phase or any rebuttal runs — so verify the timeline before
  anything else each year.
- INFOCOM has no standing editor-in-chief and no APC; General and TPC Co-Chairs rotate per edition.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar tool or author
  name is not proof of an INFOCOM placement (SIGCOMM/NSDI/MobiCom look similar on the surface).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
