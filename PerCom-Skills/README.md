# IEEE PerCom Skills

Twelve agent skills for papers targeting **IEEE PerCom — the IEEE International Conference on
Pervasive Computing and Communications**, the IEEE flagship for **human-centric ubiquitous
computing**: activity recognition, context modeling, mobile and wearable sensing, and smart
environments. The pack covers the full arc of a PerCom campaign: deciding whether a project is
PerCom-shaped or belongs at ACM UbiComp/IMWUT, MobiCom, SenSys, or IPSN; building human-subjects
sensing evidence that survives a ubicomp reviewer's audit; packaging the **double-blind HotCRP**
submission on the **IEEEtran 9+1** budget; navigating the **single-round rebuttal** review with its
early-rejection stage; and delivering the IEEE Xplore camera-ready plus a reproducible sensing
dataset.

Official basis checked on **2026-07-09**: the PerCom 2027 Call for Papers and Important Dates
pages, the PerCom HotCRP site, the Work-in-Progress call, the Mark Weiser Best Paper and Test of
Time award pages, IEEE Xplore, and dblp. Direct fetches of `percom.org` returned 403 in the
verification environment, so official pages were read via search-engine renderings of the exact
URLs and cross-checked against the PerCom HotCRP site, IEEE Xplore / IEEE Computer Society Digital
Library, and dblp; the full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Temporal note: as of 2026-07-09, **PerCom 2026 (Pisa, Italy, 16-20 March 2026) has concluded**,
> so the live next research target is **PerCom 2027 (Goa, India, 8-12 March 2027)**. All
> submission-cycle advice anchors to the PerCom 2027 call.

## What makes PerCom different from its neighbors

These venue mechanics, verified for the 2026/2027 cycles, drive most of the advice in the skills —
and most of the mistakes made by authors arriving from ACM UbiComp/IMWUT, from a networked-sensor
venue (SenSys/IPSN), or from an ML conference:

- **It is IEEE, and human-centric.** PerCom is IEEE Computer Society's pervasive-computing flagship;
  its center of gravity is **people** — activity recognition, context-awareness, wearables, smart
  spaces — rather than the pure networked-sensor-systems focus of SenSys/IPSN. Papers publish in
  **IEEE Xplore** using the **IEEE two-column conference template**, not ACM `acmart`.
- **A single annual deadline feeding one review round with a rebuttal.** PerCom 2027 registration
  closes 4 Sep 2026, submission 11 Sep 2026 (AoE). There is no journal-style revise-and-resubmit
  and no second deadline within the cycle.
- **A bounded rebuttal, gated by an early-rejection stage.** After the initial reviews, papers with
  no positive review are **early-rejected** (notified ~20 Nov 2026) so authors can move on; papers
  with at least one "weak accept" are **invited to a rebuttal** (~26 Nov 2026) that answers explicit
  reviewer questions. The call states **new experiments are not expected** — the submitted paper
  must already carry its evidence.
- **Double-blind review.** Anonymize the PDF, the dataset/repository links, and testbed/lab names,
  and **cite your own prior work in the third person** rather than omitting it.
- **A tight page budget.** **9 pages** of technical content (10pt, two-column,
  `compsocconf` IEEEtran) **+ 1 page** for references only — a fraction of a single-column ACM
  budget. Compression discipline, not template tampering, is how you fit.
- **A human-subjects, cross-subject evidence culture.** Real participants, IRB/ethics handling,
  **leave-one-subject-out** evaluation, and **F1 on imbalanced activity classes** (not pooled
  accuracy) are community norms the reviewer pool enforces even where no rule states them.
- **A distinctive award culture.** The **Mark Weiser Best Paper Award** (sponsored by Elsevier) and
  the newer **Test of Time Award** (inaugurated at PerCom 2026) mark the venue's memory; a lively
  **PerCom Workshops** constellation (WristSense, PerVehicle, CoMoRea, DIGITA, ...) and **WiP**,
  **demo**, and **industry** tracks surround the main conference.

## Skills

| Skill | What it does |
| --- | --- |
| [`percom-topic-selection`](skills/percom-topic-selection/SKILL.md) | Route between PerCom and its neighbors (ACM UbiComp/IMWUT, MobiCom, SenSys, IPSN, MobiSys) using contribution shape, the human-centricity test, and the model-swap test. |
| [`percom-workflow`](skills/percom-workflow/SKILL.md) | Run the single-cycle year backward from the September deadline, through registration, the early-rejection gate, the rebuttal, the IEEE Xplore camera-ready, and in-person presentation. |
| [`percom-writing-style`](skills/percom-writing-style/SKILL.md) | Build the ubicomp skeleton: pervasive-computing contribution on the first page, cross-subject claims, a limitations section that argues, and 9-page budget discipline. |
| [`percom-related-work`](skills/percom-related-work/SKILL.md) | Cover the ubicomp/mobile/sensing lanes, write delta-first positioning, and keep self-citations double-blind. |
| [`percom-experiments`](skills/percom-experiments/SKILL.md) | Match evidence to claim shape: real human subjects, leave-one-subject-out evaluation, F1 on imbalanced classes, deployment realism, and honest baselines. |
| [`percom-reproducibility`](skills/percom-reproducibility/SKILL.md) | Build the open-data story for human-subjects sensing: de-identified datasets, IRB/ethics handling, sensing provenance, and cross-subject reproducibility. |
| [`percom-supplementary`](skills/percom-supplementary/SKILL.md) | Split content between the 9 reviewed pages and the dataset/artifact by decision-criticality — nothing that decides acceptance may live outside the body. |
| [`percom-submission`](skills/percom-submission/SKILL.md) | Final HotCRP audit: the registration+submission two-step, the IEEEtran 9+1 budget, the double-blind sweep, the open-data plan, and desk-risk triage. |
| [`percom-review-process`](skills/percom-review-process/SKILL.md) | Model the pipeline — double-blind, three TPC reviewers, the early-rejection gate, the bounded single-round rebuttal — and where author leverage exists. |
| [`percom-author-response`](skills/percom-author-response/SKILL.md) | Write the bounded rebuttal that answers explicit reviewer questions, corrects misreadings, and adds no unsupported new claims — respecting double-blindness. |
| [`percom-artifact-evaluation`](skills/percom-artifact-evaluation/SKILL.md) | Package a reusable sensing artifact and dataset for reproducibility/badging (IEEE DataPort / Zenodo, IEEE Open Research Objects where offered — cycle-check). |
| [`percom-camera-ready`](skills/percom-camera-ready/SKILL.md) | De-anonymize, complete IEEE Xplore metadata (PDF eXpress, copyright, ORCID), permanentize dataset links, and pass IEEE production checks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026/2027 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five archival-verified PerCom papers across five contribution shapes — Mark Weiser Best Paper and Test of Time honorees — with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional eating-recognition study's abstract and introduction rebuilt to the PerCom arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility tooling, plus the PerCom-specific human-subjects and cross-subject checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./PerCom-Skills
claude plugin install percom-skills
```

Or use the files directly: each `skills/percom-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a PerCom paper or should it go to UbiComp/IMWUT or SenSys?" → `percom-topic-selection`
- "Audit my draft against the PerCom research-track rules" → `percom-submission`
- "We were invited to rebuttal — plan the reply" → `percom-author-response`
- "Get this sensing dataset ready for release" → `percom-reproducibility`

## Pack structure

```text
PerCom-Skills/
├── .claude-plugin/             # plugin.json + marketplace.json (12 skills declared)
├── README.md                   # this file
├── README.zh-CN.md             # 中文说明
├── LICENSE                     # MIT
├── assets/cover.svg            # pack cover
├── skills/
│   └── percom-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md               # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md          # adapter to shared reproducibility tooling
```

## Suggested use

1. **Before writing** — run `percom-topic-selection`; PerCom and UbiComp/IMWUT overlap in topic
   but differ in model and calendar, so choosing deliberately matters. Skim the exemplars library to
   see what influential PerCom contributions look like.
2. **While building evidence** — keep `percom-experiments` and `percom-reproducibility` beside the
   study; cross-subject splits designed in and IRB/consent handled at collection time cannot be
   retrofitted.
3. **While writing** — `percom-writing-style` for the body against the worked example,
   `percom-supplementary` for the body/dataset split, `percom-related-work` for delta-first
   positioning.
4. **Deadline weeks** — register before the earlier registration cutoff, then `percom-submission`
   end to end on the final PDF and dataset link.
5. **After submission** — `percom-review-process` to calibrate, `percom-author-response` for the
   rebuttal (if you clear the early-rejection gate), then `percom-artifact-evaluation` and
   `percom-camera-ready` — or the routing table in `percom-topic-selection` if the decision goes
   the other way.

## 2026/2027-cycle anchor facts (historical snapshot, not permanent rules)

- PerCom 2026 was the **24th** edition: Pisa, Italy, **16-20 March 2026**; the **Test of Time
  Award** was inaugurated there, honoring "LANDMARC" (PerCom 2003).
- PerCom 2027 is the **25th** edition: Goa, India, **8-12 March 2027**; research registration
  **4 Sep 2026**, submission **11 Sep 2026** (AoE); early-reject / rebuttal invitation **20 Nov
  2026**, rebuttal **26 Nov 2026**, notification **18 Dec 2026**; page budget **9 pages + 1** for
  references; each paper read by **three** TPC members. This is the live next research target as of
  2026-07-09.
- Publication: **IEEE Xplore**. Review: **double-blind**, single round with a **bounded rebuttal**
  and an **early-rejection** gate. Template: **IEEEtran** (`compsocconf`, 10pt, two-column). Portal:
  **HotCRP**.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026/2027 facts** — carry dates/budgets and trace to a numbered source in the source
   map (e.g., the 9+1 IEEEtran budget, the double-blind rebuttal model, the 11 Sep 2026 deadline).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the exact
   organizing-committee roster, or the ~14-15% historical acceptance rate).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the PerCom 2027 TPC Chair
   roster, camera-ready dates, whether a formal reproducibility-badge track runs, any AI-disclosure
   policy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. PerCom re-decides its structure per edition —
  including the rebuttal window and any reproducibility track — so verify the cadence before
  anything else each year.
- PerCom has no standing editor-in-chief and no APC; chairs rotate per edition. The cost model is
  IEEE registration, and at least one author presents in person.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar system name is
  not proof of a PerCom placement (much ubicomp work is at UbiComp/IMWUT, MobiCom, SenSys, or IPSN).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
