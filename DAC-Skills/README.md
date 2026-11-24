# DAC Skills

Twelve agent skills for papers targeting **DAC — the ACM/IEEE Design Automation Conference**, "The
Chips to Systems Conference," the premier venue for **electronic design automation (EDA)** and
chip/system design, sponsored by ACM and IEEE and supported by **ACM SIGDA** and **IEEE CEDA**. The
pack covers the full arc of a DAC campaign: deciding whether a project is DAC-shaped and, if so,
whether it belongs in the double-blind archival **Research Manuscript** track or the industry-facing
**Engineering Track**; building QoR evidence that survives an EDA reviewer's audit; packaging the
two-stage, double-blind Softconf submission inside the tight **6+1-page** double-column budget
(IEEE template for DAC 2027); navigating a **single-shot, TPC-driven, accept/reject** review; and
delivering the camera-ready for IEEE Xplore and the ACM Digital Library.

Official basis re-checked on **2026-11-24**: the DAC 2027 (64th) home page, Call for Contributions,
Research Manuscript Submissions page (format, rules, AI policy, timeline, FAQ), Engineering Track
page and Committees page on `dac.com/2027`, and the `softconf.com/dac27/research` portal, all fetched
directly. The original 2026-07-09 build read the DAC 2026 pages via search-engine renderings and
cross-checked them against the ACM DL DAC proceedings and dblp; the full trail, including everything
still marked 待核实, is in [`resources/official-source-map.md`](resources/official-source-map.md).

> Name-collision warnings: **ASP-DAC** (Asia and South Pacific DAC) and **DATE** (Design, Automation
> and Test in Europe) are *distinct* EDA conferences with their own calls — no fact here derives from
> them. And "DAC" in a circuits paper often means *digital-to-analog converter*, an in-scope research
> topic, not this conference.

## What makes DAC different from its siblings

These venue mechanics, verified for the DAC 2027 cycle, drive most of the advice in the skills — and most
of the mistakes made by authors arriving from a computer-architecture venue, an ML venue, or an SE
conference:

- **Two peer-reviewed paper tracks, different review models.** DAC hosts a double-blind, archival
  **Research Manuscript** track *and* an industry-facing **Engineering Track** (front-end/back-end
  design, IP, systems and software) run by a separate Engineering Track Committee, with no
  manuscript and no publication. Choosing the track is the
  highest-leverage DAC-specific decision — absent at ISCA/MICRO/HPCA.
- **A tight 6+1 page budget.** The manuscript is **within 6 pages excluding references, plus one
  references-only page**, double-column at 9-10 pt, in the **IEEE template** for DAC 2027 (DAC 2026
  used the ACM template — the template has tracked the edition's copyright holder). Any non-reference content
  on the seventh page is grounds for **desk rejection**. This is a far smaller box than the
  architecture and SE venues.
- **Two-stage submission on Softconf.** An **abstract stage** (title, ~100-word abstract, all
  co-authors, TPC conflicts) precedes the **manuscript stage** by a week; miss the abstract stage and
  no PDF slot exists.
- **Single-shot, TPC-driven, accept/reject review.** There is **no journal-style Major Revision**,
  and DAC's research review has **no author rebuttal** (none in the DAC 2027 timeline) — leverage
  is almost entirely front-loaded onto baseline and benchmark choices.
- **Evidence is QoR on EDA benchmarks.** Reviewers judge measured **PPA (power/performance/area)**,
  wirelength, timing slack, coverage, and runtime on recognized suites (ISPD, EPFL, ISCAS/ITC, TAU,
  CircuitNet) against the strongest tuned baseline — not accuracy on a proxy.
- **No artifact-badging track.** Unlike FSE/ICSE or MICRO/ISCA, DAC does **not** run a formal
  artifact-evaluation/badge track (none in the DAC 2027 call); artifacts earn reviewer credibility
  and community reuse, not a badge.
- **IEEE Xplore + ACM DL, single annual deadline.** Accepted Research Manuscripts publish in **IEEE
  Xplore and the ACM Digital Library** (DAC 2027: IEEE Copyright Form), contingent on a full
  Speaker Registration and in-person presentation at the poster session, with one archival deadline
  a year in mid-November leading to a July conference.

## Skills

| Skill | What it does |
| --- | --- |
| [`dac-topic-selection`](skills/dac-topic-selection/SKILL.md) | Route between DAC and its siblings (ICCAD, DATE, ASP-DAC, ISCA/MICRO/HPCA) and, within DAC, between the Research Manuscript and Engineering tracks, using contribution shape, the QoR-impact and model-swap tests, and the November calendar. |
| [`dac-workflow`](skills/dac-workflow/SKILL.md) | Run the single-cycle year backward from the November manuscript deadline through the two-stage Softconf submission, winter review, March notification, the end-of-March proceedings manuscript, and April registration. |
| [`dac-writing-style`](skills/dac-writing-style/SKILL.md) | Build the QoR-forward first page, state the contribution as a measured delta, and fit a complete argument into six double-column pages with third-person self-citation. |
| [`dac-related-work`](skills/dac-related-work/SKILL.md) | Cover the EDA literature lanes (DAC/ICCAD/DATE/ASP-DAC/TCAD/TODAES), write delta-first positioning, and name the strongest baseline as the thing to beat. |
| [`dac-experiments`](skills/dac-experiments/SKILL.md) | Match evidence to QoR claims: standard benchmark suites, fair tuned baselines, full PPA + runtime reporting, ablations, and contamination-aware ML-for-EDA evaluation. |
| [`dac-reproducibility`](skills/dac-reproducibility/SKILL.md) | Pin benchmark versions, disclose flow/PDK/tool versions, report seeds and variance, and plan the anonymized-then-DOI-archived repository path. |
| [`dac-supplementary`](skills/dac-supplementary/SKILL.md) | Split content by decision-criticality — anything that decides acceptance lives in the six body pages; the seventh page is references only. |
| [`dac-submission`](skills/dac-submission/SKILL.md) | Final Softconf audit: the two-stage abstract+manuscript deadline, the 6+1 IEEE-template budget, the double-blind sweep, TPC conflict declaration, AI-content disclosure, and desk-reject triage. |
| [`dac-review-process`](skills/dac-review-process/SKILL.md) | Model the pipeline — double-blind, TPC-driven, novelty-plus-QoR, single-shot accept/reject (WIP-poster invitations), ~20-25% selective — and where the (front-loaded) author leverage exists. |
| [`dac-author-response`](skills/dac-author-response/SKILL.md) | Handle reviews with DAC's reality: no rebuttal in DAC 2027, so a targeted fix-and-reroute to ICCAD/DATE/ASP-DAC or a journal response letter (and a concise rebuttal only if a future cycle adds one). |
| [`dac-artifact-evaluation`](skills/dac-artifact-evaluation/SKILL.md) | Package the tool/benchmarks/flow for reviewer credibility and community reuse (DOI-archived, licensed), given DAC runs no ACM badge track. |
| [`dac-camera-ready`](skills/dac-camera-ready/SKILL.md) | De-anonymize systematically, complete the IEEE copyright form, pass metadata checks by the end-of-March proceedings deadline, and meet the registration/presentation conditions for IEEE Xplore and ACM DL. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Thirteen sources with URLs and access dates; verified DAC 2027 facts (with DAC 2026 as history); the access-method note; the 待核实 list; the machine-readable rules block. |
| [`resources/external_tools.md`](resources/external_tools.md) | Official DAC/IEEE-CEDA/ACM-DL/Softconf surfaces, EDA benchmark suites and open flows, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Four archival-verified DAC papers (Chaff, ABC rewriting, logic-obfuscation security, DREAMPlace) across four EDA subfields, with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional congestion-aware-router study's abstract and introduction rebuilt to the DAC QoR arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the DAC-specific QoR/flow/provenance checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./DAC-Skills
claude plugin install dac-skills
```

Or use the files directly: each `skills/dac-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a DAC paper, and Research or Engineering track?" → `dac-topic-selection`
- "Audit my draft against the DAC research-manuscript rules" → `dac-submission`
- "My baseline/benchmark evaluation — is it DAC-strong?" → `dac-experiments`
- "We got rejected with no rebuttal — reroute to ICCAD/DATE" → `dac-author-response`

## Pack structure

```text
DAC-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── dac-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `dac-topic-selection`; the DAC-vs-sibling and Research-vs-Engineering
   decisions dominate everything downstream. Skim the exemplars library to see what decade-influential
   DAC contributions look like.
2. **While building evidence** — keep `dac-experiments` and `dac-reproducibility` beside the study;
   the baseline, benchmark suite, and provenance chosen at design time cannot be retrofitted after
   the deadline (and there is no rebuttal to fix them).
3. **While writing** — `dac-writing-style` for the six-page body against the worked example,
   `dac-supplementary` for the body/repo split, `dac-related-work` for delta-first positioning.
4. **Deadline weeks** — complete the abstract stage before its cutoff, then `dac-submission` end to
   end on the final anonymized PDF.
5. **After decision** — `dac-review-process` to calibrate, `dac-author-response` for the
   fix-and-reroute, then `dac-camera-ready` — or the routing table in
   `dac-topic-selection` if the decision goes the other way.

## DAC 2027 anchor facts (cycle snapshot, not permanent rules)

- DAC 2027 is the **64th** Design Automation Conference: **San Jose Convention Center, San Jose,
  California**, **July 11-14, 2027**. Research abstracts were due **11 Nov 2026** and manuscripts
  **18 Nov 2026** (5 PM US Pacific; both closed); accepted IDs 22 Feb 2027; accept/reject 8 Mar
  2027; proceedings manuscript 31 Mar 2027; author registration 10 Apr 2027. Engineering Tracks:
  11 Jan 2027.
- Format: **6 pages body + 1 references-only page**, **double-column**, 9-10 pt, single PDF, **IEEE
  template**; IEEE Copyright Form; published in **IEEE Xplore and the ACM Digital Library**.
- Review: **double-blind, TPC-driven, single-shot accept/reject** with possible WIP-poster
  invitations; **no rebuttal** and **no artifact-badging track**; acceptance **20-25%**. A
  "Content Generated by AI" section is required if LLM-generated content is used.
- Leadership: General Chair David Pan; TPC Chair Ambar Sarkar; TPC Co-Chairs Jiang Hu and Rajiv
  Joshi.
- Sponsored by **ACM and IEEE**, supported by **ACM SIGDA** and **IEEE CEDA**.
- History: DAC 2026 (63rd) met in Long Beach, July 26-29, 2026, with the ACM template and ACM as
  copyright holder.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified DAC 2027 facts** — carry dates/budgets and trace to a numbered source in the source map
   (e.g., the 6+1 budget, the IEEE template, double-blind review, the November manuscript deadline).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., DAC 2026
   history read via search renderings).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the full DAC 2027 TPC
   roster, the final-version IEEE copyright-notice wording, whether a 2027 LBR call appears).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. DAC re-decides its structure per edition —
  including deadlines, whether any response period exists, and the topic-area list — so verify the
  current Call for Contributions before anything else each year.
- DAC has no standing editor-in-chief; the rotating analogue is the per-edition General Chair,
  Technical Program Chair, and Track Chairs under ACM SIGDA and IEEE CEDA.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar tool name is not
  proof of a DAC placement (ABC's tool paper is CAV; EPIC is DATE; IC-fingerprinting is S&P).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
