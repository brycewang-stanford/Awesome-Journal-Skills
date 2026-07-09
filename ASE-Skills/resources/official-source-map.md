# Official Source Map - ASE (IEEE/ACM Automated Software Engineering)

Access date: 2026-07-09

This map records the official and cross-check sources used for ASE-specific facts in this pack.
ASE is the **IEEE/ACM International Conference on Automated Software Engineering**, dual-sponsored
by IEEE and ACM SIGSOFT, with proceedings that appear in **both IEEE Xplore and the ACM Digital
Library**. Its calendar, page budget, required template, and review mechanics are decided per
edition. Reopen the current-cycle research-track call, the Important Dates page, and the HotCRP
site before giving submission-ready advice.

## Access method note

Direct fetches of `conf.researchr.org` returned **HTTP 403 Forbidden** from the verification
gateway on 2026-07-09 (the same egress block seen when verifying other researchr-hosted venues).
Official pages were therefore read through **WebSearch renderings of the exact URLs** and
cross-checked against the ASE HotCRP sites (`ase26.hotcrp.com`, `ase2026-nier.hotcrp.com`),
**dblp** (the ASE proceedings live under the historical series key `conf/kbse`, from the
conference's original name *Knowledge-Based Software Engineering*), the **ACM Digital Library**
(ASE proceedings, e.g. the 39th ASE at `dl.acm.org/doi/proceedings/10.1145/3691620`), **IEEE
Xplore**, and the community deadline trackers (`se-deadlines.github.io`). Facts that could not be
pinned to at least two independent surfaces are labeled **待核实**. Beware acronym collisions:
"ASE" is also the *Association for Science Education* and the *Association for Surgical Education*;
none of their pages informs this pack, and the Springer journal *Automated Software Engineering*
(AUSE) is a related but distinct venue.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://conf.researchr.org/track/ase-2026/ase-2026-research-track | ASE 2026 research-track: double-anonymous review, ACM `acmart` sigconf template, 10+2 page budget, mandatory Data Availability Statement, early-rejection stage, Accept/Revision/Reject outcomes, criteria-bound revision round | 2026-07-09 |
| 2 | https://conf.researchr.org/home/ase-2026 | ASE 2026 (41st edition) home: Munich, Germany, October 12-16, 2026 | 2026-07-09 |
| 3 | https://conf.researchr.org/dates/ase-2026 | ASE 2026 Important Dates: research submission 26 March 2026, notification 25 May 2026 | 2026-07-09 |
| 4 | https://ase26.hotcrp.com/ | ASE 2026 research-track HotCRP submission site | 2026-07-09 |
| 5 | https://conf.researchr.org/track/ase-2026/ase-2026-nier | ASE 2026 NIER (New Ideas and Emerging Results) track: 4-page limit; groundbreaking / reflection / late-breaking-advances categories; separate HotCRP (`ase2026-nier.hotcrp.com`) | 2026-07-09 |
| 6 | https://conf.researchr.org/track/ase-2026/ase-2026-tools-and-data-sets | ASE 2026 Tools and Datasets (tool demonstrations) track: submissions not to exceed 4 pages including text, references, and figures | 2026-07-09 |
| 7 | https://conf.researchr.org/track/ase-2026/ase-2026-journal-first | ASE 2026 Journal-First track: eligible journals IEEE TSE, ACM TOSEM, EMSE (Springer); paper accepted after 1 Jan 2025 | 2026-07-09 |
| 8 | https://conf.researchr.org/track/ase-2026/ase-2026-artifact-evaluation | ASE 2026 Artifact Evaluation track: Artifacts Available and Artifacts Reusable badges | 2026-07-09 |
| 9 | https://conf.researchr.org/home/ase-2025 + https://dblp.org/db/conf/kbse/ | ASE 2025 (40th edition): Seoul, Republic of Korea, November 16-20, 2025; ASE proceedings series (dblp `conf/kbse`) | 2026-07-09 |
| 10 | http://ase-conferences.org/most-influential-papers + https://conf.researchr.org/track/ase-2025/ase-2025-mip-award | ASE Most Influential Paper (MIP) award (15±1 year window transitioning to 10±1) and the ASE steering-committee awards lineage | 2026-07-09 |

## Verified 2025/2026 facts used in skills

- **ASE 2026 is the 41st IEEE/ACM International Conference on Automated Software Engineering**,
  held in **Munich, Germany, October 12-16, 2026** (source 2). As of the 2026-07-09 access date the
  research-track **notification (25 May 2026) has already passed**, so the live phase is
  camera-ready / artifact evaluation / presentation; the next *submission* target is ASE 2027.
- **ASE 2026 research-track calendar:** paper submission **26 March 2026**, notification
  **25 May 2026**, via `ase26.hotcrp.com` (sources 1, 3, 4). The exact abstract-registration
  deadline preceding the full-paper deadline is **待核实**.
- **Format is the ACM Primary Article (Proceedings) Template**: LaTeX authors use
  `\documentclass[sigconf,review,anonymous]{acmart}` (source 1). This is a per-edition choice —
  because ASE is **dual IEEE/ACM sponsored**, the required template has varied across editions
  (IEEE two-column vs. ACM `acmart`); confirm which template the current call mandates.
- **Page budget:** **10 pages** for all content (text, figures, tables, appendices) **plus 2
  pages** for references only; a **mandatory Data Availability Statement** is placed after the
  Conclusions and counts inside the 10-page limit. Accepted papers are allowed **one additional
  page** of content for revisions (source 1).
- **Review is double-anonymous:** author names and affiliations omitted, prior work referenced in
  the third person (source 1).
- **Review model:** an **early-rejection stage** removes papers with uniformly negative scores
  *before* the rebuttal period; after rebuttal the outcome is **Accept / Revision / Reject**. A
  **Revision** is a criteria-bound revise-and-resubmit: reviewers specify concrete, actionable
  revision criteria and agree to accept in principle if they are met, and authors return a
  revision with a **point-by-point summary of changes** re-checked by a discussion lead (source 1).
- **Tracks (co-located):** Research Papers; **NIER** (4 pages; groundbreaking / reflection /
  late-breaking-advances; source 5); **Tools and Datasets** / tool demonstrations (≤4 pages;
  source 6); **Journal-First** (TSE / TOSEM / EMSE, accepted after 1 Jan 2025; source 7); Industry
  Showcase; Doctoral Symposium; and workshops. **Artifact Evaluation** offers **Available** and
  **Reusable** badges (source 8).
- **Proceedings appear in both IEEE Xplore and the ACM Digital Library** (dual IEEE/ACM
  sponsorship; sources 9-10 and the ACM DL / IEEE Xplore proceedings records).
- **ASE 2025 was the 40th edition**, Seoul, Republic of Korea, November 16-20, 2025 (source 9).
- **The ASE Most Influential Paper award** revisits an influential paper from ~15 years prior
  (window transitioning to ~10 years); ACM SIGSOFT Distinguished Paper awards are also given at
  ASE (source 10).

## The Accept/Revision/Reject model (honest reading of the "two-round" question)

ASE's research track is not a single accept/reject vote. Two mechanisms make it a two-stage
process: (1) an **early-rejection stage** that ends the process before rebuttal for papers with
uniformly negative initial scores, sparing authors and reviewers a pointless rebuttal; and (2) a
first-class **Revision** outcome in which reviewers commit to acceptance-in-principle against
explicit criteria and re-read a revised paper plus its summary-of-changes. This is closer to a
lightweight journal revision than to a one-shot conference rebuttal, and it is the single most
important structural fact for authors arriving from a plain accept/reject venue. Whether a given
edition also splits the *submission* deadline into multiple cycles is decided per year — **verify
the cadence on the current Important Dates page** and never carry a previous year's structure
forward.

## No editor-in-chief; dual sponsorship, dual proceedings

ASE has **no standing editor-in-chief**; the rotating analogue is the per-edition General Chairs
and Program Co-Chairs appointed by the ASE steering committee under IEEE and ACM SIGSOFT. Unlike a
single-society venue, ASE is **jointly sponsored by IEEE and ACM**, and accepted papers are
indexed in **both IEEE Xplore and the ACM Digital Library** — a distinguishing feature relative to
ACM-only (FSE/PACMSE) or the IEEE-flavored side of ICSE.

## Still cycle-volatile (verify every year)

- All dates and AoE cutoffs, and the exact abstract-registration deadline (**待核实** for 2026).
- Which template revision is required (IEEE two-column vs. ACM `acmart`) — this has varied with the
  dual sponsorship; ASE 2026 posts ACM `acmart` sigconf.
- Rebuttal window dates and the early-rejection score threshold (**待核实** for exact dates).
- Revision-round mechanics, summary-of-changes format, and re-review assignment.
- Artifact-evaluation deadlines and whether Functional / Results-Reproduced badges are offered
  beyond Available / Reusable (**待核实**).
- Any generative-AI / LLM-use disclosure policy wording (**待核实**).
- ASE 2026 full Program Co-Chair / General Chair roster (**待核实**).
- ASE 2027 (42nd edition) host city, dates, and deadlines (**待核实** — do not infer from
  same-acronym conferences).
- ASE 2025 exact acceptance rate (a secondary tracker reported ~245/1136 ≈ 22%; **待核实** against
  an official announcement).
