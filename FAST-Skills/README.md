# USENIX FAST Skills

Twelve agent skills for papers targeting **FAST — the USENIX Conference on File and Storage
Technologies**, the storage-systems flagship of the USENIX community. FAST is the venue whose whole
identity is *storage*: file systems, SSD/NVM and flash, key-value and object stores, caching,
storage reliability and endurance, crash consistency, and the real-device measurement that anchors
all of it. The pack covers the full arc of a FAST campaign: deciding whether a project is
FAST-shaped or belongs at OSDI, ATC, NSDI, EuroSys, HotStorage, MSST, or ACM TOS; building
storage evidence (workload traces, write amplification, tail latency, wear/endurance,
crash-consistency testing, aging) that survives a storage reviewer; packaging the double-blind
HotCRP submission for one of FAST's **two annual deadlines**; navigating USENIX review, the
**author response**, shepherding, and the **one-shot revision**; and delivering the free
open-access camera-ready plus a USENIX-badged artifact.

Official basis checked on **2026-07-09**: the FAST '26 and FAST '27 Calls for Papers and Important
Dates, the FAST double-blind guidance, the FAST '27 Call for Artifacts, the USENIX Test-of-Time and
Best-Paper pages, and the FAST HotCRP sites. Direct fetches of `usenix.org` and `dl.acm.org`
returned 403 in the verification environment, so official pages were read via search-engine
renderings of the exact URLs and cross-checked against dblp (`conf/fast`), the ACM Digital Library
mirror of the USENIX proceedings, and the FAST HotCRP instances; the full trail, including
everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Acronym-collision warning: "FAST" is reused by other communities (e.g. an IEEE/AST software-test
> workshop and various domain acronyms). This pack is exclusively about the **USENIX** File and
> Storage Technologies conference (`usenix.org/conference/fastNN`, dblp `conf/fast`). No fact here
> derives from a same-named event.

## What makes FAST different from its siblings

These venue mechanics, verified for the 2026/2027 cycles, drive most of the advice in the skills —
and most of the mistakes made by authors arriving from an OS/systems venue, a database venue, or an
architecture venue:

- **It is the storage-specialized USENIX flagship.** Reviewers are storage people. A paper's real
  contribution has to land in *storage* terms — a file-system, device, key-value, cache, or
  reliability lesson — not a general systems result that merely touches disk. A brilliant scheduler
  or network paper is respected and then routed to OSDI/ATC/NSDI.
- **Two submission deadlines a year.** FAST runs a **Spring** and a **Fall** deadline (FAST '27:
  17 Mar 2026 and 15 Sep 2026, AoE). Missing one is not a lost year — the other on-ramp is months
  away — which reshapes calendar strategy versus a single-annual-deadline conference.
- **USENIX double-blind, not "heavy" ACM anonymity.** Anonymize the PDF and references and write
  about your own prior work in the third person; there is an **author-response** period before
  notification. This is the USENIX model, distinct from a conference with camera-ready-only
  anonymity or a journal R&R letter.
- **A one-shot revision, not an open-ended R&R.** Beyond accept/reject, FAST issues
  **accept-with-shepherding** and **one-shot revision**. A one-shot revision's instructions can
  require *specific new experiments*; the revised paper is resubmitted at the next deadline and can
  then only be accepted or rejected. Budget it like a second full deadline.
- **USENIX proceedings, free and open, no APC.** Papers are published open access by USENIX with no
  article-processing charge; the USENIX two-column template and a **12-page (long) / 6-page (short)
  limit excluding references** define the budget — not an ACM `acmart` or IEEE 10+2 box.
- **USENIX artifact badges, three of them.** Post-acceptance, an AEC awards **Artifacts Available /
  Artifacts Functional / Results Reproduced**, shown on the first page — the USENIX three-badge
  scheme, not the ACM four-badge one.
- **A storage-evidence culture.** Real devices and firmware, standard workloads and traces (SNIA
  IOTTA, YCSB, filebench, fio, block traces), write amplification, tail latency, endurance and
  wear, crash-consistency testing, and aging are the community norms a storage reviewer enforces
  even where no rule states them.

## Skills

| Skill | What it does |
| --- | --- |
| [`fast-topic-selection`](skills/fast-topic-selection/SKILL.md) | Route between FAST and its siblings (OSDI, ATC, NSDI, EuroSys, HotStorage, MSST, DATE/SYSTOR, ACM TOS) using storage-contribution shape, the storage-lesson test, and the two-deadline calendar. |
| [`fast-workflow`](skills/fast-workflow/SKILL.md) | Run the two-deadline year backward from the chosen Spring/Fall cutoff, through double-blind submission, author response, shepherding or one-shot revision, artifact evaluation, and the open-access camera-ready. |
| [`fast-writing-style`](skills/fast-writing-style/SKILL.md) | Build the storage-systems skeleton: the storage problem on the first page, a design/mechanism narrative, an evaluation that answers "what does this cost on real devices?", and USENIX page discipline. |
| [`fast-related-work`](skills/fast-related-work/SKILL.md) | Cover the storage literature lanes (FAST/OSDI/ATC/EuroSys/HotStorage/MSST/TOS), write delta-first positioning, and keep self-citations double-blind. |
| [`fast-experiments`](skills/fast-experiments/SKILL.md) | The storage-evaluation core: real devices and firmware, standard traces and workloads, write amplification, tail latency, endurance/wear, crash-consistency testing, aging, and fair baselines. |
| [`fast-reproducibility`](skills/fast-reproducibility/SKILL.md) | Build the storage-reproducibility story: pin device models, firmware, and trace provenance; state what a reader needs to rebuild results on hardware that ages and varies part-to-part. |
| [`fast-supplementary`](skills/fast-supplementary/SKILL.md) | Split content between the reviewed pages and the artifact by decision-criticality, using the references-excluded page budget and USENIX double-blind rules. |
| [`fast-submission`](skills/fast-submission/SKILL.md) | Final HotCRP audit: pick the Spring/Fall deadline, register the abstract, meet the USENIX template and 12/6-page limit, sweep double-blind leaks, place the artifact-availability story, and triage desk risk. |
| [`fast-review-process`](skills/fast-review-process/SKILL.md) | Model the pipeline — double-blind PC review, outside referees, the author response, shepherding, and the one-shot revision — and where author leverage exists. |
| [`fast-author-response`](skills/fast-author-response/SKILL.md) | Write both turns: the short pre-notification rebuttal and the one-shot-revision change ledger that maps every required change (including new experiments) to a concrete result. |
| [`fast-artifact-evaluation`](skills/fast-artifact-evaluation/SKILL.md) | Convert the accepted paper's package into USENIX badges (Available / Functional / Reproduced), handling storage artifacts that need specific hardware, large traces, or long endurance runs. |
| [`fast-camera-ready`](skills/fast-camera-ready/SKILL.md) | De-anonymize, apply the larger camera-ready budget and USENIX template, permanentize trace/code availability, add the artifact appendix and badges, and meet the final-files deadline. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026/2027 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five archival-verified FAST papers across five storage-contribution shapes — Test-of-Time and Best-Paper honorees — with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional key-value-on-SSD study's abstract and introduction rebuilt to the FAST arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the storage-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./FAST-Skills
claude plugin install fast-skills
```

Or use the files directly: each `skills/fast-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a FAST paper or should it go to OSDI/ATC?" → `fast-topic-selection`
- "Audit my draft against the FAST CFP before the Fall deadline" → `fast-submission`
- "We got a one-shot revision — plan the resubmission" → `fast-author-response`
- "Get this storage artifact ready for the USENIX badges" → `fast-artifact-evaluation`

## Pack structure

```text
FAST-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json (12 skills declared)
├── README.md                  # this file
├── README.zh-CN.md            # 中文说明
├── LICENSE                    # MIT
├── assets/cover.svg           # pack cover
├── skills/
│   └── fast-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md              # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md         # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `fast-topic-selection`; FAST overlaps OSDI/ATC/EuroSys, so choosing by
   storage-community pull and the nearer of the two deadlines matters. Skim the exemplars to see
   what decade-influential FAST contributions look like.
2. **While building evidence** — keep `fast-experiments` and `fast-reproducibility` beside the
   testbed; device models, firmware, and trace provenance pinned at measurement time cannot be
   retrofitted.
3. **While writing** — `fast-writing-style` for the body against the worked example,
   `fast-supplementary` for the body/artifact split, `fast-related-work` for delta-first
   positioning.
4. **Deadline weeks** — pick Spring or Fall, register the abstract early, then `fast-submission`
   end to end on the final PDF.
5. **After submission** — `fast-review-process` to calibrate, `fast-author-response` for the
   rebuttal and any one-shot revision, then `fast-artifact-evaluation` and `fast-camera-ready` — or
   the routing table in `fast-topic-selection` if the decision goes the other way.

## 2026/2027-cycle anchor facts (historical snapshot, not permanent rules)

- FAST '26 is the **24th** edition: Santa Clara, CA (Hyatt Regency Santa Clara), **February 24-26,
  2026**. It ran two deadlines (Spring 18 Mar 2025, Fall 16 Sep 2025) and introduced one-shot
  revisions.
- FAST '27 is the **25th** edition: Santa Clara, CA, **February 23-25, 2027**; two deadlines —
  **Spring 17 Mar 2026** and **Fall 15 Sep 2026** (AoE). Submission limit **12 pages (long) / 6
  pages (short) excluding references**. As of 2026-07-09 the live actionable target is the **Fall
  deadline, 15 Sep 2026**.
- Publication: **USENIX open access**, free, no APC. Review: **double-blind** with an author
  response. Decisions: Accept / Accept-with-shepherding / **One-shot Revision** / Reject.
  Template: **USENIX two-column**. Artifacts: **Available / Functional / Reproduced**.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026/2027 facts** — carry dates/limits and trace to a numbered source in the source
   map (e.g., the two deadlines, the 12/6-page limit, the one-shot-revision rule, the three USENIX
   badges).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., exact hotel
   and any organizing-committee roster beyond what the CFP names).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., FAST '27 Program Co-Chair
   and AEC rosters, the AEC anonymity model, any AI-use disclosure policy, the exact venue city).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and limit above is a **cycle snapshot**. FAST re-decides its structure per edition —
  including the number of deadlines and the revision mechanics — so verify the cadence before
  anything else each year.
- FAST has no standing editor-in-chief and no APC; chairs and the AEC rotate per edition. Treat
  continuity assumptions about people as errors.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar storage tool name
  is not proof of a FAST placement (many landed at OSDI, ATC, EuroSys, or SOSP instead).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
