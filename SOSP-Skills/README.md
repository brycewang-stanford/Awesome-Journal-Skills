# SOSP Skills

**English** | [简体中文](README.zh-CN.md)

Twelve agent skills for papers at the ACM Symposium on Operating Systems Principles
(SOSP) — the flagship SIGOPS venue for built-and-measured research on the design,
implementation, analysis, evaluation, and deployment of computer systems software.
The pack covers the whole campaign: deciding whether a project is SOSP-shaped,
back-scheduling against the spring abstract and paper gates on HotCRP, fitting the
argument into 12 dense pages with references uncounted, surviving double-blind review
with chair-audited conflicts, writing the narrow-charter author response, converting
a July acceptance into a shepherded 13/14-page camera-ready, and earning ACM badges
through the sysartifacts artifact evaluation.

Official basis checked on 2026-07-08: the SOSP 2026 Call for Papers and author
guidelines on sigops.org, the sosp26 HotCRP deadlines page, the sysartifacts
artifact-evaluation pages for SOSP 2025/2026, the SIGOPS annual-cadence announcement,
the SIGOPS Hall of Fame, the ACM Digital Library SOSP proceedings, and dblp. Every
cycle-specific fact traces to a URL in
[`resources/official-source-map.md`](resources/official-source-map.md); anything that
could not be pinned live is marked 待核实 there instead of guessed. Direct fetches to
sigops.org were gateway-blocked during construction, so the source map also documents
the search-rendering + ACM DL/dblp triangulation used to verify each fact.

## What makes SOSP different

This pack is organized around the venue's own mechanics, not generic conference lore:

- **Annual since 2024.** SOSP ended its decades-old biennial alternation with OSDI
  (SIGOPS announcement, 2023). The 30th edition ran in Austin (Nov 2024), the 31st
  in Seoul (Oct 2025), and the 32nd lands in Prague, Sep 29 - Oct 2, 2026. Campaign
  planning is now a rolling circuit, and several skills teach the retargeting math.
- **Two gates, one page budget.** Abstract registration precedes the paper deadline
  and is a real gate: the assigned paper ID replaces the author block on page one.
  Submissions get at most **12 pages of technical content with bibliographic
  references uncounted** — a budget shape that rewards cutting prose, never the
  bibliography.
- **Chair-audited conflicts.** PC chairs review declared conflicts and may add *or
  remove* entries; naming a PC member to dodge a tough reviewer is called out as
  improper. The pack treats the conflict list as a document you must be able to
  defend.
- **A response with a narrow charter.** The pre-PC-meeting author response exists to
  correct factual errors and answer questions reviewers posed — no new experiments,
  no promised work, under 500 words strongly encouraged.
- **Decisions made in a room.** A single-track PC meeting argues every candidate
  live; prose and responses are written to arm an advocate, not to raise a score
  average.
- **Shepherded camera-ready with an expanding page budget.** Final papers get 13
  pages of technical content, and the shepherd can approve a 14th — the extra space
  is for the concerns the reviews raised.
- **Post-acceptance, cooperative artifact evaluation.** The sysartifacts community
  runs SOSP's AE after decisions, single-blind, with authors fixing problems during
  the window and choosing their ACM badge targets (Available / Functional /
  Reusable, with Distinguished Artifact on top).
- **A citable ancestry.** The SIGOPS Hall of Fame and five decades of proceedings
  mean related-work sections are checked against a lineage the PC knows by heart;
  the exemplars library ships verified SOSP classics and the OSDI/ATC
  misattribution traps to avoid.

## Skills

| Skill | Use it to... |
| --- | --- |
| [`sosp-submission`](skills/sosp-submission/SKILL.md) | Audit HotCRP readiness: the two deadlines, 12-page + references format, paper-ID anonymization, defensible conflicts, desk-reject triage. |
| [`sosp-author-response`](skills/sosp-author-response/SKILL.md) | Draft the narrow-charter response: factual corrections and posed questions only, budgeted near 500 words, aimed at the PC meeting. |
| [`sosp-camera-ready`](skills/sosp-camera-ready/SKILL.md) | Run the shepherd thread, spend the 13th/14th page on reviewer concerns, de-anonymize safely, clear ACM rights mechanics. |
| [`sosp-artifact-evaluation`](skills/sosp-artifact-evaluation/SKILL.md) | Register with sysartifacts days after notification, tier claims by runnability, target badges, staff the interactive window. |
| [`sosp-reproducibility`](skills/sosp-reproducibility/SKILL.md) | Pin the platform below userspace, capture environments mechanically, make every figure one command from logged runs. |
| [`sosp-supplementary`](skills/sosp-supplementary/SKILL.md) | Split content between the paper and the separate supplement without exiling review-critical evidence. |
| [`sosp-review-process`](skills/sosp-review-process/SKILL.md) | Model staged reviewing, the response window, and the PC meeting; triage reviews by what can still be moved. |
| [`sosp-writing-style`](skills/sosp-writing-style/SKILL.md) | Lead with an extractable principle, build the first-page arc, budget 12 dense pages, write figures that argue. |
| [`sosp-related-work`](skills/sosp-related-work/SKILL.md) | Position against the SOSP/OSDI lineage on structural axes; handle third-person self-citation and concurrent work. |
| [`sosp-experiments`](skills/sosp-experiments/SKILL.md) | Map claims to experiments, tune baselines fairly, cover micro/end-to-end/trace layers, report tails with spread. |
| [`sosp-workflow`](skills/sosp-workflow/SKILL.md) | Place the project on the annual calendar, run the July-to-August three-thread sprint, retarget rejections across the circuit. |
| [`sosp-topic-selection`](skills/sosp-topic-selection/SKILL.md) | Apply the principle/embodiment/evidence shape test and route to OSDI, ATC, NSDI, FAST, ASPLOS, VLDB, MLSys, EuroSys, or HotOS when it fails. |

## Resources

| Resource | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Every official URL behind the pack's facts, access-dated 2026-07-08, with the gateway-blocked verification method and the 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live venue systems (CFP, HotCRP, sysartifacts, ACM DL, Hall of Fame) plus author-side checklists and do-not-infer rules. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Verified SOSP classics organized problem × principle, and the famous OSDI/ATC/EuroSys papers you must not attribute to SOSP. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional systems paper's abstract and introduction rebuilt into the SOSP first-page arc, move by move. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter from the repo-level ML-conference reproducibility kit to OS-level artifacts and sysartifacts staging. |

## The 2026 cycle at a glance (all anchors, not laws)

| Milestone | Date |
| --- | --- |
| Abstract registration | March 27, 2026 (March 26 AoE) |
| Full paper deadline | April 2, 2026, 7:59:59 AM EDT (April 1 AoE) |
| Notification | July 3, 2026 |
| Camera-ready | August 28, 2026 |
| Conference (Prague, Czech Republic) | September 29 - October 2, 2026 |

As of this pack's verification date (2026-07-08), the 2026 decision has just landed:
accepted teams are in the shepherding/AE/logistics sprint, and rejected teams are
retargeting across the now-annual SOSP/OSDI circuit. SOSP 2027 has no posted dates
(待核实); never back-schedule against an implied deadline.

## Repository layout

```text
SOSP-Skills/
├── .claude-plugin/
│   ├── plugin.json           # plugin manifest (sosp-skills, v0.1.0, MIT)
│   └── marketplace.json      # marketplace entry declaring the 12 skill paths
├── assets/cover.svg          # pack cover art
├── skills/                   # 12 skills, one directory per SKILL.md
│   └── sosp-*/SKILL.md
├── resources/
│   ├── official-source-map.md
│   ├── external_tools.md
│   ├── exemplars/library.md
│   ├── worked-examples/01-introduction.md
│   └── code/README.md        # adapter to ../shared-resources/ml-conference-methods
├── README.md / README.zh-CN.md
└── LICENSE (MIT)
```

## How the skills interlock

The skills cross-reference rather than repeat each other. The evaluation triangle —
[`sosp-experiments`](skills/sosp-experiments/SKILL.md) designs the evidence,
[`sosp-reproducibility`](skills/sosp-reproducibility/SKILL.md) makes it traceable,
[`sosp-artifact-evaluation`](skills/sosp-artifact-evaluation/SKILL.md) packages it for
badges — shares one claims-map discipline, defined once and cited twice. Likewise the
response chain: [`sosp-review-process`](skills/sosp-review-process/SKILL.md) triages
what can still move, and [`sosp-author-response`](skills/sosp-author-response/SKILL.md)
spends the sub-500-word budget on exactly those points. Deadline mechanics live only
in [`sosp-submission`](skills/sosp-submission/SKILL.md) and
[`sosp-workflow`](skills/sosp-workflow/SKILL.md); style, positioning, and supplement
policy each live in exactly one place.

## Suggested entry points

- **Twelve months out:** [`sosp-topic-selection`](skills/sosp-topic-selection/SKILL.md)
  → [`sosp-workflow`](skills/sosp-workflow/SKILL.md) →
  [`sosp-experiments`](skills/sosp-experiments/SKILL.md) with
  [`sosp-reproducibility`](skills/sosp-reproducibility/SKILL.md) running underneath.
- **Deadline month:** [`sosp-writing-style`](skills/sosp-writing-style/SKILL.md) →
  [`sosp-related-work`](skills/sosp-related-work/SKILL.md) →
  [`sosp-supplementary`](skills/sosp-supplementary/SKILL.md) →
  [`sosp-submission`](skills/sosp-submission/SKILL.md).
- **Reviews in hand:** [`sosp-review-process`](skills/sosp-review-process/SKILL.md) →
  [`sosp-author-response`](skills/sosp-author-response/SKILL.md).
- **Accepted:** [`sosp-camera-ready`](skills/sosp-camera-ready/SKILL.md) in parallel
  with [`sosp-artifact-evaluation`](skills/sosp-artifact-evaluation/SKILL.md).

## Maintenance notes

- Reopen the current cycle's CFP, authors page, and HotCRP before any
  deadline-sensitive advice; SOSP re-issues rules annually and hosts move.
- Treat the 2026 dates, page limits, response mechanics, and AE details in this pack
  as historical anchors from one verified cycle.
- When official pages disagree, HotCRP controls deadlines and the newest authors
  page controls format; record conflicts in the source map with a fresh access date.
- If direct fetches to sigops.org fail, use the triangulation documented in
  [`resources/official-source-map.md`](resources/official-source-map.md).

## License

MIT — see [`LICENSE`](LICENSE). Maintained by Bryce Wang as part of
[awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills).
