# ACM FAccT Skills

Twelve agent skills for papers targeting **ACM FAccT — the Conference on Fairness, Accountability,
and Transparency**, the flagship *interdisciplinary* responsible-AI venue. Unlike a pure-ML venue
(NeurIPS/ICML) or an HCI venue (CHI), FAccT uniquely requires that **fairness, accountability, or
transparency be a first-class contribution**, and it convenes a genuinely mixed reviewer pool —
computer scientists, lawyers, social scientists, humanists, and policy scholars. The pack covers the
full arc of a FAccT campaign: deciding whether a project is FAccT-shaped or belongs at an ML/HCI/law
venue; building evidence that satisfies a mixed panel (a rigorous CS audit *and* a critical or
qualitative study are both in scope); packaging the mutually-anonymous OpenReview submission with its
required endmatter statements; navigating the **Accept / Revise (major or minor) / Reject**
revise-and-resubmit cycle; and delivering the ACM `acmart` archival camera-ready with its accountability documentation.

Official basis **re-verified on 2026-11-24** for **FAccT 2027** (tenth edition, **Porto, Portugal,
June 21-24, 2027**): the FAccT 2027 Call for Papers, Author Guide, and Reviewer Guide; the
facctconference.org home page; the FAccT Blog posts on the 2027 timeline and process changes; and
the OpenReview FAccT 2027 group, all read directly. FAccT 2026 pages (CFP, committees, CRAFT and
Doctoral Colloquium calls) were re-read as history; the ACM DL still returned 403, so the FAccT '26
proceedings DOI was confirmed through Crossref. The full trail, including everything still marked
待核实, is in [`resources/official-source-map.md`](resources/official-source-map.md).

> Lineage note: the venue was **FAT\*** in 2018-2020 (FAT\* 2018 published in **PMLR vol 81**; FAT\*
> 2019 was the first ACM DL proceedings) and has been **FAccT** since 2021. The dblp key is still
> `db/conf/fat`. Do not confuse FAccT with the pre-conference **FAT/ML workshop** or the sibling
> **AIES** conference.

## What makes FAccT different from its siblings

These venue mechanics, verified for the 2027 cycle, drive most of the advice in the skills — and most
of the mistakes made by authors arriving from a pure-ML, HCI, or law background:

- **Fairness/accountability/transparency is the contribution, not a paragraph.** A paper whose equity
  framing could be deleted with a publishable core remaining belongs at the ML/HCI/law home of that
  core. FAccT wants the harm, accountability, or transparency question to *be* the paper.
- **The reviewer pool is interdisciplinary.** Papers are matched to reviewers and **Area Chairs** by
  the **focus areas** you select at registration, and a paper is typically read across disciplines —
  each expecting *its* lane's rigor (disaggregation and baselines for an audit; coding and reflexivity
  for a qualitative study; doctrinal precision for a legal paper).
- **Accept / Revise (major or minor) / Reject, with no separate rebuttal.** A **Revise** decision
  (introduced in 2026) is a genuine revise-and-resubmit: you address Area-Chair-prioritized concerns
  and submit the revised paper **together with a rebuttal**, then are re-reviewed. FAccT 2027 dropped
  the short pre-decision rebuttal of 2026 and added **Senior Area Chairs** for calibration.
- **OpenReview, and an autumn deadline.** Submission and review run on OpenReview (since 2026), with
  a hard **abstract-registration gate** (with focus-area selection) a week before the paper deadline.
  From 2027 the deadlines moved to late October / early November of the preceding year.
- **Every author must sign up to review.** FAccT 2027 requires all authors of every paper to fill in
  the reviewer sign-up form; not following through can lead to (desk) rejection.
- **Mutual anonymity, with special endmatter rules.** Authors and reviewers are hidden from each
  other. The **Positionality**, Acknowledgements, Author-Contributions, and Competing-Interests
  statements are **withheld** from the anonymous submission and added only upon acceptance.
- **Required Generative AI Usage Statement.** Every submission must disclose whether and how
  generative AI was used, even if it was not. FAccT 2026 prohibited LLM-generated manuscript text;
  FAccT 2027 follows ACM's authorship policy instead: AI may create content if the use is disclosed
  (tool, model version, task, human validation), and undisclosed use is grounds for desk rejection.
  An **Ethical Considerations** statement (covering adverse impacts) is expected at submission; the
  endmatter sits on an extra page that does not count against the limit.
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
| [`facct-workflow`](skills/facct-workflow/SKILL.md) | Run the single-deadline year backward from the abstract-registration gate, through OpenReview, the Revise round with its combined revision + rebuttal, camera-ready, and presentation. |
| [`facct-writing-style`](skills/facct-writing-style/SKILL.md) | Make the FAccT contribution legible to a mixed panel: who is affected on page one, claims scoped to a population, harms argued not recited. |
| [`facct-related-work`](skills/facct-related-work/SKILL.md) | Cover the disciplinary lanes (ML-fairness, HCI, law, STS), write delta-first cross-lane positioning, and cite borrowed constructs to their origin. |
| [`facct-experiments`](skills/facct-experiments/SKILL.md) | Match evidence to the claim: disaggregated audits with fair baselines, qualitative rigor and reflexivity, proxy validity, consent and ethics. |
| [`facct-reproducibility`](skills/facct-reproducibility/SKILL.md) | Build transparency: released code/data, datasheets/model cards/data statements, and auditable qualitative work without breaking confidentiality. |
| [`facct-supplementary`](skills/facct-supplementary/SKILL.md) | Split content across body, the endmatter statement zone, and the artifact — and get the anonymity rules for each right. |
| [`facct-submission`](skills/facct-submission/SKILL.md) | Final OpenReview audit: the abstract gate + focus areas, the acmart anonymous PDF, mutual anonymity, required/optional endmatter, archival choice. |
| [`facct-review-process`](skills/facct-review-process/SKILL.md) | Model the pipeline — mutually anonymous, interdisciplinary, Area Chairs and Senior Area Chairs, Accept/Revise/Reject, re-review — and where author leverage exists. |
| [`facct-author-response`](skills/facct-author-response/SKILL.md) | Write the Revise-round rebuttal that ships with the revised paper, mapping each prioritized concern to a change (and the 2026-style short rebuttal if a cycle restores it). |
| [`facct-artifact-evaluation`](skills/facct-artifact-evaluation/SKILL.md) | Prepare the accountability documentation (datasheets, model cards, impact assessments) and released code/data FAccT expects instead of badges. |
| [`facct-camera-ready`](skills/facct-camera-ready/SKILL.md) | De-anonymize, add the withheld Positionality/Acks, reformat in the ACM format, complete ACM metadata, handle the OA/APC question and the camera-ready deadline. |

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
5. **After submission** — `facct-review-process` to calibrate, `facct-author-response` for any
   Revise round and its rebuttal, then `facct-artifact-evaluation` and `facct-camera-ready` — or the
   routing table in `facct-topic-selection` if the decision goes the other way.

## FAccT 2027 anchor facts (cycle snapshot, not permanent rules)

- FAccT 2027 is the **10th** annual conference: **Porto, Portugal**, **June 21-24, 2027**. Abstract
  registration **27 Oct 2026**; paper **3 Nov 2026** (both passed as of 2026-11-24); first-round
  decisions (Accept / Revise major or minor / Reject) **22 Dec 2026**; revision + rebuttal
  **28 Jan 2027**; final notification **23 Mar 2027**; camera-ready **TBD**. Program Chairs per the
  CFP: Remi Denton, David Leslie, Aurelia Tamò-Larrieux, Isabel Valera (a blog byline names a
  different four — 待核实); General Chairs not yet announced.
- Platform: **OpenReview**. Review: **mutually anonymous**, interdisciplinary, focus-area matched
  (six focus areas), typically three reviewers + an Area Chair, with **Senior Area Chairs** (new).
  Template: **ACM TAPS** (LaTeX `acmart` review/anonymous, or Word), single-column; **14 pages +
  1 endmatter page**, references and appendices unlimited; **15** pages at Revision/acceptance.
- Required **Generative AI Usage Statement** (disclosure-based policy in 2027); **Ethical
  Considerations** statement at submission; Positionality, Acknowledgements, Author Contributions,
  and Competing Interests only upon acceptance. Archival ACM proceedings (non-archival option);
  **100% Open Access** since 1 Jan 2026 (2026 APC subsidy $250 members / $350 non-members).
- History: FAccT 2026 (9th, Montréal, June 25-28, 2026) had deadlines of 8 / 13 Jan 2026, a short
  rebuttal (due 24 Feb 2026), first notification 2 Mar, revision 25 Mar, final notification
  15 Apr 2026.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2027 facts** — carry dates/budgets and trace to a numbered source in the source map
   (e.g., the 14+1 page budget, mutual anonymity, the Revise round, the required Generative AI Usage
   Statement).
2. **Reported facts** — read only via secondary surfaces and labeled as such (e.g., the FAccT '26
   proceedings DOI, confirmed through Crossref because the ACM DL refuses automated access).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the conflicting 2027
   Program Chair lists, the 2027 camera-ready date, General Chairs, the 2027 CRAFT/Doctoral-Colloquium
   calls, and any 2027 APC subsidy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it against
the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. FAccT re-decides its structure per edition —
  2026 introduced OpenReview, the Revise round, and the Generative AI Usage Statement; 2027 moved the
  deadline to the autumn, merged rebuttal into the revision, added Senior Area Chairs, and relaxed the
  AI-writing prohibition into a disclosure rule — so verify whether each persists before advising.
- FAccT has no standing editor-in-chief; General and PC Chairs rotate yearly. Treat continuity
  assumptions about people as errors.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar responsible-AI paper
  may actually be a workshop, journal, or AIES placement, not FAccT.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
