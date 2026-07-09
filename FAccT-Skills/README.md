# ACM FAccT Skills

Twelve agent skills for papers targeting **ACM FAccT — the Conference on Fairness, Accountability,
and Transparency**, the flagship *interdisciplinary* responsible-AI venue. Unlike a pure-ML venue
(NeurIPS/ICML) or an HCI venue (CHI), FAccT uniquely requires that **fairness, accountability, or
transparency be a first-class contribution**, and it convenes a genuinely mixed reviewer pool —
computer scientists, lawyers, social scientists, humanists, and policy scholars. The pack covers the
full arc of a FAccT campaign: deciding whether a project is FAccT-shaped or belongs at an ML/HCI/law
venue; building evidence that satisfies a mixed panel (a rigorous CS audit *and* a critical or
qualitative study are both in scope); packaging the mutually-anonymous OpenReview submission with its
required endmatter statements; navigating the new **Accept / Revise / Reject** revise-and-resubmit
cycle; and delivering the ACM `acmart` archival camera-ready with its accountability documentation.

Official basis checked on **2026-07-09**: the FAccT 2026 Call for Papers, Author Guide, Reviewer
Guide, and CRAFT call; the FAccT Blog announcement posts; the OpenReview FAccT 2026 group; the ACM
Digital Library FAccT proceedings; and dblp. Direct fetches of `facctconference.org` and `dl.acm.org`
returned 403 in the verification environment, so official pages were read via search-engine
renderings of the exact URLs and cross-checked against OpenReview, ACM DL, dblp, and PMLR (for the
pre-2019 FAT\* editions); the full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Lineage note: the venue was **FAT\*** in 2018-2019 (FAT\* 2018 published in **PMLR vol 81**; FAT\*
> 2019 was the first ACM DL proceedings) and was renamed **FAccT** after 2020. The dblp key is still
> `db/conf/fat`. Do not confuse FAccT with the pre-conference **FAT/ML workshop** or the sibling
> **AIES** conference.

## What makes FAccT different from its siblings

These venue mechanics, verified for the 2026 cycle, drive most of the advice in the skills — and most
of the mistakes made by authors arriving from a pure-ML, HCI, or law background:

- **Fairness/accountability/transparency is the contribution, not a paragraph.** A paper whose equity
  framing could be deleted with a publishable core remaining belongs at the ML/HCI/law home of that
  core. FAccT wants the harm, accountability, or transparency question to *be* the paper.
- **The reviewer pool is interdisciplinary.** Papers are matched to reviewers and **Area Chairs** by
  the **focus areas** you select at registration, and a paper is typically read across disciplines —
  each expecting *its* lane's rigor (disaggregation and baselines for an audit; coding and reflexivity
  for a qualitative study; doctrinal precision for a legal paper).
- **Accept / Revise / Reject — the Revise round is new for 2026.** A **Revise** decision is a genuine
  revise-and-resubmit: you address Area-Chair-prioritized concerns and are re-reviewed. It is not a
  soft reject.
- **OpenReview, new for 2026.** Submission and review moved to OpenReview, with a hard
  **abstract-registration gate** (with focus-area selection) about a week before the paper deadline.
- **Mutual anonymity, with special endmatter rules.** Authors and reviewers are hidden from each
  other. The **Positionality**, Acknowledgements, Author-Contributions, and Competing-Interests
  statements are **withheld** from the anonymous submission and added only upon acceptance.
- **Required Generative AI Usage Statement, new for 2026.** Every submission must disclose whether and
  how generative AI was used; FAccT prohibits wholesale AI-generated text. Optional **Ethical
  Considerations** and **Adverse Impacts** statements sit on an extra endmatter page that does not
  count against the limit.
- **ACM `acmart`, archival, and now 100% Open Access.** Papers publish in the ACM DL proceedings (a
  **non-archival** option exists); since 1 January 2026 all ACM proceedings are Open Access via ACM
  Open or APCs.
- **A documentation and impact culture.** Datasheets, model cards, data statements, and impact
  assessments are the FAccT-native "artifacts" — there is no SIGSOFT-style badging track.
- **The co-located CRAFT program.** Critiquing and Rethinking Accountability, Fairness, and
  Transparency runs participatory and world-building sessions (workshops, fishbowls, unconferences,
  artistic interventions) alongside the paper track.

## Skills

| Skill | What it does |
| --- | --- |
| [`facct-topic-selection`](skills/facct-topic-selection/SKILL.md) | Route between FAccT and its siblings (NeurIPS/ICML, CHI/CSCW, AIES, law/policy) using the delete-the-equity and mixed-reviewer tests, and paper vs CRAFT. |
| [`facct-workflow`](skills/facct-workflow/SKILL.md) | Run the single-deadline year backward from the abstract-registration gate, through OpenReview, rebuttal, the Revise round, two-round camera-ready, and presentation. |
| [`facct-writing-style`](skills/facct-writing-style/SKILL.md) | Make the FAccT contribution legible to a mixed panel: who is affected on page one, claims scoped to a population, harms argued not recited. |
| [`facct-related-work`](skills/facct-related-work/SKILL.md) | Cover the disciplinary lanes (ML-fairness, HCI, law, STS), write delta-first cross-lane positioning, and cite borrowed constructs to their origin. |
| [`facct-experiments`](skills/facct-experiments/SKILL.md) | Match evidence to the claim: disaggregated audits with fair baselines, qualitative rigor and reflexivity, proxy validity, consent and ethics. |
| [`facct-reproducibility`](skills/facct-reproducibility/SKILL.md) | Build transparency: released code/data, datasheets/model cards/data statements, and auditable qualitative work without breaking confidentiality. |
| [`facct-supplementary`](skills/facct-supplementary/SKILL.md) | Split content across body, the endmatter statement zone, and the artifact — and get the anonymity rules for each right. |
| [`facct-submission`](skills/facct-submission/SKILL.md) | Final OpenReview audit: the abstract gate + focus areas, the acmart anonymous PDF, mutual anonymity, required/optional endmatter, archival choice. |
| [`facct-review-process`](skills/facct-review-process/SKILL.md) | Model the pipeline — mutually anonymous, interdisciplinary, Area Chairs, short rebuttal, Accept/Revise/Reject — and where author leverage exists. |
| [`facct-author-response`](skills/facct-author-response/SKILL.md) | Write both turns: the factual-correction rebuttal and the Revise-and-resubmit response mapping each prioritized concern to a change. |
| [`facct-artifact-evaluation`](skills/facct-artifact-evaluation/SKILL.md) | Prepare the accountability documentation (datasheets, model cards, impact assessments) and released code/data FAccT expects instead of badges. |
| [`facct-camera-ready`](skills/facct-camera-ready/SKILL.md) | De-anonymize, add the withheld Positionality/Acks, switch to acmart sigconf, complete ACM metadata, handle the two-round OA camera-ready. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five archival-verified FAccT/FAT\* papers across five contribution shapes and disciplines, with self-check questions and a sibling-confusion guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional benefits-audit study's abstract and introduction rebuilt to the FAccT arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the FAccT-specific documentation and disaggregation checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./FAccT-Skills
claude plugin install facct-skills
```

Or use the files directly: each `skills/facct-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a FAccT paper or should it go to NeurIPS/CHI/AIES?" → `facct-topic-selection`
- "Audit my draft against the FAccT CFP and endmatter rules" → `facct-submission`
- "We got a Revise — plan the revise-and-resubmit response" → `facct-author-response`
- "Get my datasheet and model card ready" → `facct-artifact-evaluation`

## Pack structure

```text
FAccT-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json (12 skills declared)
├── README.md                  # this file
├── README.zh-CN.md            # 中文说明
├── LICENSE                    # MIT
├── assets/cover.svg           # pack cover
├── skills/
│   └── facct-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md              # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md         # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `facct-topic-selection`; the delete-the-equity and mixed-reviewer tests
   decide whether FAccT (vs. NeurIPS/CHI/AIES/law) is right. Skim the exemplars to see what a
   first-class FAccT contribution looks like across disciplines.
2. **While building evidence** — keep `facct-experiments` and `facct-reproducibility` beside the
   study; disaggregation, proxy validity, consent, and documentation cannot be retrofitted.
3. **While writing** — `facct-writing-style` for the body against the worked example,
   `facct-supplementary` for the body/endmatter/artifact split, `facct-related-work` for cross-lane
   positioning.
4. **Deadline weeks** — register the abstract and focus areas before the earlier gate, then
   `facct-submission` end to end on the final PDF, endmatter, and artifact.
5. **After submission** — `facct-review-process` to calibrate, `facct-author-response` for the
   rebuttal and any Revise round, then `facct-artifact-evaluation` and `facct-camera-ready` — or the
   routing table in `facct-topic-selection` if the decision goes the other way.

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- FAccT 2026 is the **9th** annual conference: **Montréal, Canada** (Le Centre Sheraton Montréal),
  **June 25-28, 2026**. Abstract registration **8 Jan 2026**; paper **13 Jan 2026**; preliminary
  reviews **20 Feb 2026**; first notification (Accept/Revise/Reject) **2 Mar 2026**; revision
  **25 Mar 2026**; camera-ready **24 Apr** (Round 1) / **11 May 2026** (Revise). General Chairs Su Lin
  Blodgett and Zeerak Talat; PC Chair Michael Madaio.
- Platform: **OpenReview** (new). Review: **mutually anonymous**, interdisciplinary, focus-area
  matched, with Area Chairs. Decisions: Accept / **Revise** / Reject (Revise new for 2026). Template:
  **ACM `acmart`**; **14 content pages + 1 endmatter page**, references unlimited.
- Required **Generative AI Usage Statement** (new); optional **Ethical Considerations**, **Adverse
  Impacts**, and (upon acceptance) **Positionality** statements. Archival ACM proceedings (non-archival
  option); **100% Open Access** since 1 Jan 2026.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026 facts** — carry dates/budgets and trace to a numbered source in the source map
   (e.g., the 14+1 page budget, mutual anonymity, the Revise round, the required Generative AI Usage
   Statement).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the exact
   organizing-committee roster beyond the named General and PC Chairs).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., FAccT 2027 dates, the exact
   Revise final-notification date, the CRAFT/Doctoral-Colloquium deadlines, and APC/fee-waiver policy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it against
the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. FAccT re-decides its structure per edition —
  and 2026 introduced three firsts at once (OpenReview, the Revise round, the Generative AI Usage
  Statement) — so verify whether each persists before advising.
- FAccT has no standing editor-in-chief; General and PC Chairs rotate yearly. Treat continuity
  assumptions about people as errors.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar responsible-AI paper
  may actually be a workshop, journal, or AIES placement, not FAccT.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
