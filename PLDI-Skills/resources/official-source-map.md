# Official Source Map - PLDI

Access date: 2026-07-08

This map records the official sources behind every PLDI-specific fact in this pack.
PLDI mechanics are reset each edition by that year's General Chair and Program Chair;
reopen the current Call for Papers, the research-papers and research-artifacts track
pages, the important-dates page, and the SIGPLAN policy pages before giving any
submission-ready advice.

**Access-method note (2026-07-08):** direct fetches of `sigplan.org`,
`pldi26.sigplan.org`, and the `lists.seas.upenn.edu` CFP archive returned HTTP 403 in
the verification environment, so official-page contents were read through
search-engine renderings of those exact URLs and cross-checked against the ACM
Digital Library (PACMPL tables of contents), dblp conference records, and secondary
mirrors of the CFP. Before relying on any deadline, page cap, or policy sentence,
open the primary URLs below directly.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.sigplan.org/announce/2025-09-24-pldi-2026/ | PLDI 2026 Call for Papers (47th ACM SIGPLAN Conference on Programming Language Design and Implementation): submission format of no more than 20 pages of text excluding bibliography, single-column ACM (acmsmall) layout with 10 pt font and 12 pt line spacing, text block 5.478 in x 7.884 in, `sample-acmsmall-conf.tex` from the acmart package, and summary rejection for format deviations chosen for PACMPL compatibility. | 2026-07-08 |
| 2 | https://pldi26.sigplan.org/track/pldi-2026-papers | PLDI 2026 research-papers track: scope (all aspects of PL research — design, implementation, theory, applications, performance), double-blind reviewing in use for several years, HotCRP submission at https://pldi2026.hotcrp.com/, author response Feb 17-21 2026, notification Mar 5 2026. | 2026-07-08 |
| 3 | https://pldi26.sigplan.org/dates | PLDI 2026 timetable: paper deadline Thu Nov 13, 2025; author response Feb 17-21, 2026; notification Thu Mar 5, 2026; registration opens Mon Mar 16, 2026. | 2026-07-08 |
| 4 | https://pldi26.sigplan.org/ | PLDI 2026 venue and dates: Limelight Boulder, Boulder, Colorado, USA; workshops/tutorials Mon-Tue Jun 15-16, main conference Wed-Fri Jun 17-19, 2026. | 2026-07-08 |
| 5 | https://pldi26.sigplan.org/committee/pldi-2026-organizing-committee | PLDI 2026 rotating leadership: General Chair Bor-Yuh Evan Chang (University of Colorado & Amazon); Program Chair Manu Sridharan (UC Riverside); Artifact Evaluation Co-Chairs Raphaël Monat (Inria & University of Lille) and Qirun Zhang (Georgia Tech). | 2026-07-08 |
| 6 | https://pldi26.sigplan.org/track/pldi-2026-pldi-research-artifacts | PLDI 2026 artifact evaluation: artifacts submitted only after paper acceptance to keep paper and artifact review separate; badges Functional, Reusable (only for artifacts judged Functional and judged well packaged/documented for reuse), and Available (earned by archiving a snapshot on Zenodo with a DOI); no artifact camera-ready deadline because Zenodo accepts new versions at any time. | 2026-07-08 |
| 7 | https://blog.sigplan.org/2022/08/08/pldi-will-join-pacmpl/ | The structural pivot: PLDI publishes its proceedings as an issue of PACMPL starting with PLDI 2023, following a community survey; POPL, OOPSLA, and ICFP already published in PACMPL. | 2026-07-08 |
| 8 | https://dl.acm.org/journal/pacmpl | PACMPL (Proceedings of the ACM on Programming Languages) as a Gold Open Access journal publishing papers selected by the major SIGPLAN conferences; author-side APC of 400 USD (discounted through SIGPLAN support), with SIGPLAN covering the fee for authors who cannot pay, and ACM Open institutional coverage; ACM became a fully open-access publisher on Jan 1, 2026. | 2026-07-08 |
| 9 | https://dl.acm.org/toc/pacmpl/2025/9/PLDI | PACMPL Volume 9, Issue PLDI (June 2025) as the published form of PLDI 2025 — the PACMPL volume/issue anchor used for exemplar verification (Vol 7 = 2023, Vol 8 = 2024, Vol 9 = 2025). | 2026-07-08 |
| 10 | https://pldi25.sigplan.org/ and https://pldi25.sigplan.org/track/pldi-2025-papers | PLDI 2025 anchor edition: Westin Josun Seoul, South Korea, Jun 16-20 2025 (main conference Jun 18-20); PACMPL Issue PLDI authors invited — but not required — to present at the June conference; 89 accepted papers with 6 designated Distinguished Papers under the up-to-10% rule. | 2026-07-08 |
| 11 | https://www.sigplan.org/Resources/EmpiricalEvaluation/ | SIGPLAN Empirical Evaluation Guidelines (Blackburn, Hauswirth, Berger, Hicks, Krishnamurthi, 2018) and their one-page checklist: clearly stated claims, suitable comparison, principled benchmark choice, and adequate data analysis — the methodological yardstick PLDI reviewers and artifact evaluators are pointed to. | 2026-07-08 |
| 12 | https://conf.researchr.org/series/pldi and https://conf.researchr.org/home/pldi-2027 | The PLDI series index and the PLDI 2027 site, which at check time was still a placeholder ("check back soon") with no CFP, dates, or location posted. | 2026-07-08 |

## Verified facts used in the skills

- PLDI 2026 is the 47th ACM SIGPLAN Conference on Programming Language Design and
  Implementation, held at Limelight Boulder, Boulder, Colorado, USA — workshops and
  tutorials June 15-16, main conference June 17-19, 2026. As of 2026-07-08 the
  edition has already taken place; it is this pack's most recent completed cycle.
- The PLDI 2026 timetable ran: submission deadline Thursday November 13, 2025;
  author response February 17-21, 2026; notification Thursday March 5, 2026;
  registration opening March 16, 2026. There is one submission deadline per year.
- Submissions went through HotCRP (`pldi2026.hotcrp.com`), not OpenReview.
- Format: at most 20 pages of text excluding bibliography, in the single-column ACM
  `acmsmall` layout (10 pt font, 12 pt line spacing, 5.478 in x 7.884 in text
  block), chosen for compatibility with PACMPL; deviating formats are grounds for
  summary rejection.
- Reviewing is double-blind and has been for several PLDI cycles.
- Since PLDI 2023, accepted papers are published as **PACMPL, Issue PLDI** — a
  journal-formatted proceedings; PLDI thereby joined POPL, OOPSLA, and ICFP, which
  already published in PACMPL. PACMPL volume-to-edition mapping: Vol 7 = 2023,
  Vol 8 = 2024, Vol 9 = 2025.
- PACMPL is Gold Open Access. The author-side APC is 400 USD (deeply discounted by
  SIGPLAN support), SIGPLAN covers it for authors who cannot pay, ACM Open
  institutions are exempt, and ACM moved to full open access on January 1, 2026.
- Artifact evaluation runs after paper acceptance; badges are Functional, Reusable
  (Functional plus reuse-quality packaging), and Available (Zenodo archive with
  DOI). Artifacts have no camera-ready deadline thanks to Zenodo versioning.
- Up to 10% of accepted papers may be designated Distinguished Papers; PLDI 2025
  named 6 of 89 (about 6.7%).
- SIGPLAN publishes Empirical Evaluation Guidelines with a one-page checklist that
  PLDI evaluations are measured against.
- PLDI leadership rotates per edition (2026: General Chair Bor-Yuh Evan Chang,
  Program Chair Manu Sridharan). Like every conference pack in this collection,
  PLDI has no standing editor-in-chief; PACMPL has an editorial board, but
  acceptance decisions for Issue PLDI come from that year's PLDI review process.

## 待核实 (reported or expected, not directly confirmed)

- PLDI 2027 dates, location, and submission deadline: the conf.researchr.org page
  was a placeholder on 2026-07-08. The recent pattern (Nov 13, 2025 deadline for
  PLDI 2026) suggests a deadline around November 2026, but treat that as an
  extrapolation, not a fact, until the PLDI 2027 CFP is posted.
- The PLDI 2026 camera-ready deadline for papers and the exact PACMPL production
  workflow dates — not surfaced in accessible renderings.
- PLDI 2026 acceptance statistics and its PACMPL volume number (expected Vol 10 by
  pattern; confirm on the ACM DL before citing).
- Any PLDI 2026 policy on LLM/AI-assisted writing — none was found in accessible
  renderings; do not assert that one exists or does not exist.
- Rebuttal length caps or revision-upload mechanics beyond the posted Feb 17-21
  response window.
- Registration fees and the in-person presentation obligation wording for 2026
  (the 2025 wording said PACMPL authors are invited but not required to present).

## Still cycle-volatile (recheck every year)

Deadlines, page caps and template versions, the HotCRP instance URL, double-blind
FAQ wording, dual-submission and republication policy references, artifact badge
criteria and AE timeline, distinguished-paper mechanics, registration and
presentation rules, and the identity of all chairs.
