# Official Source Map - ACM IMC

Access date: 2026-07-09

This map records the official and cross-check sources used for IMC-specific facts in this pack.
IMC is the **ACM Internet Measurement Conference**, the SIGCOMM-sponsored flagship for empirical
Internet/network measurement. Its defining mechanics — two submission deadlines per year, the
**One-Shot-Revision** decision, the mandatory **Ethics** appendix, the **artifact-availability
declaration**, and the **Replicability Track** — are decided per edition. Reopen the current
call for papers, submission instructions, and committees page before giving submission-ready
advice.

## Access method note

Direct fetches of `conferences.sigcomm.org` and `dl.acm.org` returned **HTTP 403** from the
verification gateway on 2026-07-09 (the same block seen when verifying other ACM/SIGCOMM
venues). Official pages were therefore read through **search-engine renderings of the exact
URLs** and cross-checked against the IMC HotCRP sites, the ACM Digital Library IMC proceedings,
dblp, and the SIGCOMM event pages. Facts that could not be pinned to a primary rendering plus at
least one cross-check surface are labeled **待核实**. Beware a name collision: "IMC" is also the
Leeds *International Medieval Congress*, an *Indian Management Conclave*, and an IEEE
services-computing track — **none** of those is this IMC, and no fact here derives from them.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://conferences.sigcomm.org/imc/2026/cfp/ | IMC 2026 call: two deadlines/year, One-Shot-Revision, artifact-availability declaration, Replicability Track, awards | 2026-07-09 |
| 2 | https://conferences.sigcomm.org/imc/2026/submission-instructions/ | IMC 2026 formatting: double-blind, acmart template, BBL upload, page limits, mandatory Ethics section/appendix | 2026-07-09 |
| 3 | https://conferences.sigcomm.org/imc/2026/committees/ | IMC 2026 organizing/program committee: General Chairs Christian Wressnegger (KIT), Nurullah Demir (Stanford); Program Chairs Alan Mislove (Northeastern), Italo Cunha (UFMG) | 2026-07-09 |
| 4 | https://conferences.sigcomm.org/imc/2026/ | IMC 2026 event home: Karlsruhe, Germany, October 12-16, 2026; deadline calendar | 2026-07-09 |
| 5 | https://conferences.sigcomm.org/imc/2025/cfp/ | IMC 2025 call: full paper up to 13 pages text+figures + unlimited references/appendix; short paper up to 6 pages; >6 pages technical content reviewed as full | 2026-07-09 |
| 6 | https://imc2026.hotcrp.com/ | IMC 2026 main-track HotCRP submission site (cycle-specific instances) | 2026-07-09 待核实 exact instance URLs |
| 7 | https://imc2026-repro.hotcrp.com/ | IMC 2026 Replicability Track Expression-of-Interest HotCRP site (EoI deadline 29 Jan 2026) | 2026-07-09 |
| 8 | https://www.sigcomm.org/events/imc-conference | SIGCOMM IMC series identity: the ACM Internet Measurement Conference, sponsored by ACM SIGCOMM | 2026-07-09 |
| 9 | https://dl.acm.org/doi/proceedings/10.1145/3730567 | IMC '25 proceedings (ACM DL) — proceedings identity and prior-edition cross-check | 2026-07-09 |
| 10 | https://conferences.sigcomm.org/imc/2026/submission-instructions/ + https://conferences.sigcomm.org/imc/2022/cfp/ | Ethics-statement requirement (Belmont Report principles, IRB/human-subjects), and award structure evolution (Best Paper + Community Contribution) | 2026-07-09 |

## Verified 2026 facts used in skills

- **IMC 2026 is held in Karlsruhe, Germany, October 12-16, 2026** (source 4). General Chairs
  **Christian Wressnegger** (Karlsruhe Institute of Technology) and **Nurullah Demir** (Stanford
  University); Program Chairs **Alan Mislove** (Northeastern University) and **Italo Cunha**
  (Universidade Federal de Minas Gerais) (source 3).
- **Two submission deadlines per year:** cycle 1 submission **20 November 2025** (registration
  ~13 November 2025), cycle 2 submission **29 April 2026**, both AoE. Cycle 1 decisions ~17 March
  2026, camera-ready ~14 April 2026; cycle 2 decisions ~4 August 2026, camera-ready ~1 September
  2026 (sources 1, 4).
- **Decision categories: Accept / One-Shot-Revision / Reject.** One-Shot-Revision gives specific
  action points (up to 3 additions/changes) and requires **at least one champion** among the
  reviewers; the paper is resubmitted at the next deadline and judged by the **same reviewers**.
  Consensus-reject papers are notified **early** so authors can move on (source 1).
- **Double-blind review**, **ACM `acmart` template**, and authors must upload the **BBL file** of
  references on the reviewing system (source 2).
- **Page limits (IMC 2025, carried into 2026 unless the current call says otherwise):** full
  papers **up to 13 pages** of text and figures **+ unlimited** references and appendix; short
  papers **up to 6 pages** text and figures; any paper with **more than 6 pages** of technical
  content is reviewed as a full paper (source 5; 2026 exact number **待核实** against the live
  submission-instructions page).
- **A mandatory Ethics statement**, in a clearly marked section or appendix, is required;
  papers without one may be rejected. Human-subjects work must have **IRB** approval/exemption
  and the determination form is submitted (anonymized); ethics is judged against **Belmont
  Report** principles — respect for persons, beneficence, justice (sources 2, 10).
- **Artifact-availability declaration** (full / partial / no availability) is required at
  submission; accepted papers are **shepherded** to ensure promised artifacts are made available;
  legitimate proprietary/privacy reasons are accepted if explained (sources 1, 2).
- **Replicability Track:** an **Expression of Interest** (EoI deadline 29 January 2026) is
  screened by a small committee; strong abstracts are invited to full submission judged by the
  TPC against the same criteria as the main track; **priority to replicability over
  reproducibility** studies (sources 1, 7).
- **Awards:** a **Best Paper** award (all accepted papers eligible), a **Best Student Paper**
  award, and a **Community Contribution Award** for an outstanding dataset, source-code
  distribution, open platform, or service to the community — eligible only if the data/code/tool
  is **public by the camera-ready deadline** (source 10).

## The two-deadline / One-Shot-Revision model (honest reading of the cycle)

Since the recent restructuring, IMC runs **two deadlines a year** with a shared review pipeline.
The distinctive round is **One-Shot-Revision**: not a full journal-style major revision, but a
tightly bounded revise-and-resubmit — a limited number of concrete action points, a required
reviewer champion, and re-judgement by the *same* reviewers at the *next* deadline. This is
IMC's answer to giving good-but-incomplete measurement work a second chance without a rolling
journal. Whether a given year keeps exactly this cadence, the exact number of action points, and
the registration-to-submission gap are per-edition decisions — **verify on the current call and
Important Dates before advising**.

## No editor-in-chief; conference registration model

IMC has **no standing editor-in-chief**; the rotating analogue is the per-edition General Chairs
and Program Chairs appointed under ACM SIGCOMM. Proceedings are published in the **ACM Digital
Library**; the cost model is conference registration, and at least one author presents each
accepted paper.

## Still cycle-volatile (verify every year)

- Exact deadline dates, registration-to-submission gap, and AoE cutoffs for both cycles.
- Full-paper and short-paper page limits and the exact `acmart` format variant. **待核实** for
  the precise 2026 body page number (13 carried from 2025; confirm on the live page).
- One-Shot-Revision mechanics: number of allowed action points, champion rule, re-review
  assignment.
- Replicability Track EoI/full-submission dates and its acceptance-into-main-track path.
- Ethics-statement wording, the IRB-form submission requirement, and any responsible-disclosure
  or generative-AI-use policy (**待核实** for exact 2026 wording).
- Whether IMC awards formal **ACM reproducibility badges** in addition to the availability
  declaration and shepherding (**待核实**), and whether the historical **public review** of
  accepted papers is in force this edition (**待核实**).
- The full IMC 2026 Program Committee roster beyond the named chairs (**待核实**).
- Acceptance rate for the current cycle (**待核实**; historically competitive, verify per edition).
