# ECCV Skills

Twelve agent skills for papers targeting **ECCV — the European Conference on
Computer Vision** — the vision field's even-year flagship, managed by the
European Computer Vision Association (ECVA) and published through **Springer
LNCS with free ECVA open-access mirrors** (not CVF open access — a real
mechanical difference from CVPR and ICCV that runs through this whole pack).
The organizing constraint everywhere is the biennial cadence: an ECCV bet is a
two-year bet, made in a single-column 14-page format that none of the venue's
siblings use.

Official basis checked on **2026-07-08**: the ECCV 2026 Dates, Call for Papers,
Submission Policies, What's New, FAQ, and Reviewer Guide pages, the ECCV 2026
OpenReview group, SpringerLink's ECCV proceedings series, and ECVA's papers
portal. Direct fetches of `eccv.ecva.net` returned HTTP 403 in the verification
environment, so official pages were read through search-engine renderings of
the exact URLs and cross-checked against OpenReview, SpringerLink, ECVA, and
dblp. The full trail — sources, access dates, reported-only facts, and every
待核实 item — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

**Cycle status (2026-07-08):** ECCV 2026 (Malmö, Sweden, September 8–13 at
Malmö Arena and Malmömässan) is mid-cycle: the March 5 paper deadline, May 2–11
rebuttal window, and June 17 decisions are behind us, and the June 30 AoE
camera-ready deadline has just passed. The pack therefore teaches the **live
phases** — Springer camera-ready cleanup, the June-to-September artifact
release runway, the ECVA open-access appearance (~4 weeks pre-conference), and
reviews-driven retargeting toward CVPR's November deadline — plus full-cycle
planning for **ECCV 2028**, whose every detail is still unannounced (待核实).

## The facts this pack is built around

Verified 2026-cycle anchors (each traced in the source map):

- **Biennial, even years.** ECCV completes the CVPR (annual) / ICCV (odd-year)
  triangle; several skills teach the retargeting calendar from the ECCV seat,
  where a June rejection flows naturally into CVPR's November deadline.
- **A three-step front door on a CET clock.** Registration February 26 →
  paper March 5 at 11pm **CET** (not AoE; aggregators disagreed by a day over
  the conversion) → supplementary March 12. The trailing supplement week that
  CVF siblings have abandoned survives here.
- **Springer LNCS format.** 14 pages single-column **including figures and
  tables**, extra pages for cited references only, template changed since
  2024. A different page economy from any two-column CVF venue.
- **One page in May.** Reviews out May 2; optional rebuttal due May 11 as a
  one-page two-column PDF **with references counted inside the page**;
  reviewers receive it May 12; decisions June 17.
- **Enforcement against authors.** All authors were expected to be willing to
  review; late or "highly irresponsible" reviews — including LLM-policy
  violations under the CVPR-2026-aligned LLM ban — exposed *all* of a
  reviewer's own submissions to desk rejection.
- **Springer + ECVA publication.** Camera-ready June 30 AoE (extended);
  publication conditional on at least one author's registration; open-access
  copies via Springer and/or ECVA no earlier than ~4 weeks before the
  conference; the free mirror lives at ecva.net, not openaccess.thecvf.com.
- **Scale anchor (reported).** ECCV 2024 (Milan, 18th edition): LNCS volumes
  15059–15147, 2,387 papers from 8,585 submissions.
- **Ecosystem.** 93 workshops listed for 2026 (Sept 8–9); ECVA's Koenderink
  Prize honors a ten-year-old ECCV paper each edition — used here as a
  durability taste signal, not a rule.

## Skills

| Skill | What it does |
| --- | --- |
| [`eccv-topic-selection`](skills/eccv-topic-selection/SKILL.md) | Price the two-year bet: ECCV-shaped scope vs CVPR/ICCV/WACV/BMVC/ACCV/journal routes, durability and substrate-independence tests, the Koenderink lineage as taste. |
| [`eccv-workflow`](skills/eccv-workflow/SKILL.md) | Run the even-year campaign: the CET deadline chain, the retargeting triangle from the ECCV seat, where the 2026 cycle stands today, and the backward plan to March 2028. |
| [`eccv-writing-style`](skills/eccv-writing-style/SKILL.md) | Write for the 14-page single-column LNCS economy: page ledger, first-page architecture for adjacent-niche reviewers, numbered-citation prose, rebuttal-sized claims. |
| [`eccv-related-work`](skills/eccv-related-work/SKILL.md) | Cover the two intervening CVPR/ICCV cycles, apply March concurrency conventions and the own-repo citation ban, and audit Springer-vs-CVF venue attribution. |
| [`eccv-experiments`](skills/eccv-experiments/SKILL.md) | Build evidence that survives to September: the six-month-staleness test, matched-substrate fairness table, isolating ablations, falsifier-first run sequencing. |
| [`eccv-reproducibility`](skills/eccv-reproducibility/SKILL.md) | Meet the two-year checkability horizon: recipe ledger, foundation-model pinning block, variance honesty on benchmark deltas, body/supplement/archive placement. |
| [`eccv-supplementary`](skills/eccv-supplementary/SKILL.md) | Use the trailing supplement week correctly: what the +7 days are for, video and qualitative packaging, archive anonymity scrub, body self-containment. |
| [`eccv-artifact-evaluation`](skills/eccv-artifact-evaluation/SKILL.md) | Run the two-phase artifact life: sealed anonymous archive at review time, then the ten-week June→September public-release runway aligned with ECVA/Springer copies. |
| [`eccv-submission`](skills/eccv-submission/SKILL.md) | Final audit: the registration→paper→supplement chain on its CET clock, the 14-page gate, dual-submission and embargo rules, co-author reviewer-duty exposure. |
| [`eccv-review-process`](skills/eccv-review-process/SKILL.md) | Model the pipeline: OpenReview stages to the June 17 decision, the 2026 enforcement regime and LLM review ban, panel composition, AC-discussion leverage. |
| [`eccv-author-response`](skills/eccv-author-response/SKILL.md) | Spend the one page well: nine-day schedule, per-reviewer page budget with references inside the limit, new-result judgment, AC-quotable blocks. |
| [`eccv-camera-ready`](skills/eccv-camera-ready/SKILL.md) | Deliver the Springer + ECVA record: enlarged final budget, licence forms and registration precondition, rebuttal-promise ledger, arXiv sync, Malmö logistics. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with access dates, verified vs reported vs 待核实 grading, and the access-method disclosure. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes (clock, kit, policy, duty, record). |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five Springer-verified ECCV exemplars (COCO, SSD, Perceptual Losses, NeRF, RAFT) with self-checks and a big-three misattribution guard list. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional sparse-view reconstruction paper's first page, before → after, with a transfer checklist. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit plus five ECCV-only checks. |

## Installation and use

This directory is a self-contained Claude Code plugin with its own marketplace
manifest:

```bash
# From a clone of the repository
claude plugin marketplace add ./ECCV-Skills
claude plugin install eccv-skills
```

Or use the skills as plain instruction files — each `skills/eccv-*/SKILL.md`
declares in its frontmatter when it should fire. Typical prompts:

- "Is this reconstruction paper worth holding for ECCV 2028, or do we go to
  CVPR in November?" → `eccv-topic-selection` + `eccv-workflow`
- "Audit the PDF against the LNCS rules before the March freeze" →
  `eccv-submission` + `eccv-writing-style`
- "Three reviews, one page, nine days" → `eccv-author-response`
- "We're accepted — what happens between the decision and Malmö?" →
  `eccv-camera-ready` + `eccv-artifact-evaluation`

## Pack structure

```text
ECCV-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json (12 skills declared)
├── README.md                  # this file
├── README.zh-CN.md            # 中文说明
├── LICENSE                    # MIT
├── assets/cover.svg           # pack cover (even-year bridge motif)
├── skills/
│   └── eccv-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## Fact discipline

Statements in this pack come in three grades, kept distinguishable everywhere:

1. **Verified 2026-cycle facts** — traceable to a numbered source-map entry
   (the CET deadline chain, the 14-page-including-figures rule, the one-page
   rebuttal with references inside it, the reviewer-duty enforcement, the
   Springer/ECVA publication route).
2. **Reported facts** — consistent secondary renderings, labeled as such (the
   2024 acceptance arithmetic, the 15-page camera-ready allowance and its
   counting basis, the 93-workshop count).
3. **待核实 items** — phrased as open questions (the 2026 edition number,
   rebuttal new-results wording, supplement size caps, presentation
   obligations, and the *entire* 2028 process).

A skill asserting grade-2/3 material as grade-1 is a bug; fix it against the
live pages.

## Maintenance notes

- The next real update moment is when the ECCV 2028 pages go live at
  eccv.ecva.net: host, deadline chain and its clock, page rules and counting
  basis, rebuttal format, enforcement wording, and platform all need
  re-verification then.
- Watch the per-cycle "What's New" page first — in 2026 it carried the highest
  policy density (reviewer-duty enforcement, LLM ban, deadline extension).
- The CET-vs-AoE distinction caused real aggregator disagreement in 2026;
  never quote a deadline without its timezone and source.
- Exemplar additions must pass the SpringerLink verification recipe at the
  bottom of [`resources/exemplars/library.md`](resources/exemplars/library.md);
  LNCS formatting alone proves nothing about the venue.

## License

MIT — see [`LICENSE`](LICENSE). 中文说明见 [`README.zh-CN.md`](README.zh-CN.md)。
