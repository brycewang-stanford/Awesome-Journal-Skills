# Official Source Map - CAV (Computer Aided Verification)

Access date: 2026-07-09. CAV 2027 Call for Papers, Artifact Evaluation page, Organizing
Committee, Registration and Proceedings pages **re-verified 2026-11-24** against the live
`conferences.i-cav.org/2027/` pages (direct fetch, HTTP 200; the CFP footer reads "Updated
22 Sep 2026", the Artifact Evaluation page "Updated 3 Nov 2026").

**Edition status, checked 2026-11-24.** The live edition is **CAV 2027**, the 39th
International Conference on Computer-Aided Verification, **Amsterdam, The Netherlands,
July 19-23, 2027** (conference including workshops; main conference Wednesday July 21 -
Friday July 23), at **KIT, formerly the Royal Tropical Institute** — the first CAV held in
the Netherlands. Its full Call for Papers is now published (categories, page limits,
anonymity rules, review process, artifact rules), so **this pack now describes CAV 2027**.
CAV 2026 (38th, Lisbon, part of FLoC 2026, July 26-29, 2026) has met; its rows below are
kept as labelled history. The CAV 2027 rules differ from 2026 in four ways that change
advice: (1) **three** categories instead of four; (2) Tool Papers now get the **same 18-page
limit** as Regular Papers; (3) the Application/Industrial/Case Study category is **not
anonymized** (CAV 2026 anonymized Short Application Papers); (4) **artifact evaluation is
mandatory for Tool Papers** and runs in parallel with paper review. The HotCRP submission
link and the CAV 2027 Program Committee roster beyond the chairs are still "to be added".

This map records the official and cross-check sources for the CAV-specific facts used across
this pack. CAV is the flagship formal-verification conference; its research papers are published
in **Springer Lecture Notes in Computer Science (LNCS)**, and its calendar, submission
categories, page limits, review mechanics, and artifact-evaluation rules are decided per edition
by the current Program Chairs. Reopen the current-cycle Call for Papers, the Artifact Evaluation
page, and the Springer LNCS proceedings page before giving submission-ready advice.

## Access method note

On **2026-11-24** the CAV 2027 pages at `https://conferences.i-cav.org/2027/` loaded directly
(curl, HTTP 200) and were read in full; the CAV 2026 CFP at the same host also loaded directly.
The Springer AI-policy page linked from the CAV 2027 CFP redirected to a Springer
sign-in/cookie wall and could not be read. On 2026-07-09 (the original pass) direct fetches of
`conferences.i-cav.org` / `i-cav.org` and `sigplan.org` returned **HTTP 403** from the
verification gateway, so the CAV 2026 rows were read through **search-engine renderings of
the exact URLs** and cross-checked against **dblp**, the **Springer LNCS** book pages for CAV
2024 and CAV 2025, and the **FLoC 2026** site. Name-collision guard: CAV is *Computer Aided
Verification*; do not confuse it with unrelated "CAV" acronyms (connected/automated vehicles,
etc.), and do not attribute TACAS/FMCAD/VMCAI/POPL/PLDI papers to CAV — those sibling-venue traps
are documented in `resources/exemplars/library.md`.

## Primary official sources (CAV 2027, read 2026-11-24)

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://conferences.i-cav.org/2027/cfp/ | CAV 2027 = 39th CAV; submission deadline Wednesday January 20, 2027, 23:59 AoE (a single "Full papers due" date, no separate abstract deadline listed); early rejection notification March 4, 2027; artifact registration (tool papers) March 8, 2027; author response period April 5-8, 2027; author notification April 23, 2027; artifact registration (non-tool papers) April 26, 2027; camera-ready May 18, 2027; early registration May 18, 2027; conference including workshops July 19-23, 2027, Amsterdam; main conference July 21-23. **Three categories:** Regular Papers (**18 pages** max, must be anonymized, double-blind); Tool Papers (**18 pages** max, need not be anonymized, single-blind); Application/Industrial Experience/Case Study Papers (**10 pages** max, need not be anonymized, single-blind). Page limits exclude references and appendices; a clearly marked appendix is allowed but reviewers are not obliged to read it. LNCS format; note Springer's guidelines regarding AI authorship; no simultaneous submission to other conferences with proceedings or of published material; at most **5** submissions per author across all categories. Camera-ready limits (excluding bibliography and data availability statement): regular and tool papers up to **20 pages**, application papers up to **12 pages** (each includes 2 extra pages). Two-stage review: two reviews in stage 1, early rejection for papers without sufficient support, two additional reviews and a rebuttal option in stage 2. Regular papers evaluated on correctness, technical depth, significance, novelty, clarity and transparency; author names and affiliations omitted and own prior work cited in the third person, non-conforming submissions rejected without review; arXiv allowed but strongly discouraged within 1 week around or 1 month after the deadline. Non-tool papers: artifact invited after acceptance, acceptance not conditional on AE, artifact intent declared at submission and shared with reviewers. Tool papers: artifact **mandatory**, acceptance requires passing both paper review and AE; exemption only if applied for at submission. SIGPLAN Empirical Evaluation Guidelines encouraged. Submission via **HotCRP** ("link will be added here once available"). LNCS proceedings; selected papers invited to special issues of Formal Methods in System Design and the Journal of the ACM. PC Chairs Marieke Huisman (University of Twente) and Joost-Pieter Katoen (RWTH Aachen University & University of Twente); contact Cav2027@lists.utwente.nl. | 2026-11-24 |
| 2 | https://conferences.i-cav.org/2027/artifacts/ | CAV 2027 Artifact Evaluation: two rounds — Round 1 tool-paper artifacts (registration March 8, submission March 11, smoke-test response March 22-25, artifact and paper notification April 23, 2027), Round 2 non-tool artifacts (registration April 26, submission May 3, smoke-test response May 11-14, artifact notification May 28, 2027); tool-paper artifacts must earn at least the **Functional** badge; AE is **single-blind**; badges Available (public archival repository with DOI), Functional, Reusable, aligned with ACM criteria; every artifact submission must nominate one distinct reviewer (load about 3 artifacts each); optional consent to reviewers using an LLM in the smoke test only; smoke-test and full-review phases; Docker image, VirtualBox VM image (.ova), or package for the CAV 2027 AE VM; README + LICENSE required; HotCRP (link TBA). AE Chairs Tim Quatmann (RWTH Aachen) and Tom van Dijk (University of Twente). | 2026-11-24 |
| 3 | https://conferences.i-cav.org/2027/ | CAV 2027 home: 39th edition, July 19-23, 2027, Amsterdam, KIT; first CAV in the Netherlands; keynotes Anne-Kathrin Schmuck, Dino Distefano, Marijn Heule; important dates (submission January 20, response April 5-8, notification April 23, early registration May 18, 2027). | 2026-11-24 |
| 4 | https://conferences.i-cav.org/2027/organizing-committee/ | General Chairs + PC Chairs Marieke Huisman and Joost-Pieter Katoen; Steering Committee Orna Grumberg, Aarti Gupta, Daniel Kröning, Ken McMillan; Local Chair Thomas van Binsbergen; AE Chairs Tim Quatmann, Tom van Dijk; Proceedings Chair Ernst Moritz Hahn. | 2026-11-24 |
| 5 | https://conferences.i-cav.org/2027/registration/ | Registration details "will be announced"; early registration deadline May 18, 2027 (no fees posted). | 2026-11-24 |
| 6 | https://conferences.i-cav.org/2027/proceedings/ | "CAV 2027 proceedings information will be announced here" — no LNCS volume or open-access arrangement posted yet. | 2026-11-24 |
| 7 | https://www.springer.com/gp/editorial-policies/artificial-intelligence--ai-/25428500 | Springer AI policy linked from the CAV 2027 CFP ("Note Springer's guidelines regarding AI Authorship"); on 2026-11-24 it redirected to a Springer sign-in/cookie wall and its text could not be read. | 2026-11-24 (unreadable) |
| 8 | https://www.sigplan.org/Resources/EmpiricalEvaluation/ | SIGPLAN Empirical Evaluation Guidelines, which the CAV 2027 CFP encourages authors to consult. | 2026-11-24 (link only) |

## Historical and cross-check sources (CAV 2026 and earlier)

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 9 | http://conferences.i-cav.org/2026/cfp/ | CAV 2026 Call for Papers: four submission categories, LNCS format, page limits, anonymization matrix, two-stage review, rebuttal, artifact-intent declaration | 2026-07-09 |
| 10 | https://www.sigplan.org/announce/2025-11-21-cav-2026/ | SIGPLAN announcement of the 38th CAV (CAV 2026): identity, deadlines, review model | 2026-07-09 |
| 11 | http://conferences.i-cav.org/2026/ | CAV 2026 home: 38th edition, Lisbon, Portugal, July 26-29, 2026, part of FLoC 2026 | 2026-07-09 |
| 12 | https://conferences.i-cav.org/2026/organization/ | CAV 2026 Program Chairs: Anthony W. Lin, Eva Darulova, Philipp Rümmer | 2026-07-09 |
| 13 | http://conferences.i-cav.org/2026/artifacts/ | CAV 2026 Artifact Evaluation: Available / Functional / Reusable badges, ≥2 AEC members per artifact, smoke-test + full-review phases, optional and non-conditional | 2026-07-09 |
| 14 | https://www.floc26.org/ | FLoC 2026 (9th Federated Logic Conference), Lisbon, Portugal, July 2026, co-locating CAV, CP, CSF, FSCD, ICLP, IJCAR, ITP, KR, LICS, SAT | 2026-07-09 |
| 15 | https://link.springer.com/conference/cav | Springer LNCS CAV proceedings series (open access) | 2026-07-09 |
| 16 | https://link.springer.com/book/10.1007/978-3-031-65627-9 | CAV 2024 (36th), Montreal, LNCS 14681-14683, open access | 2026-07-09 |
| 17 | https://link.springer.com/book/10.1007/978-3-031-98679-6 | CAV 2025 (37th), Zagreb, open-access 4-volume set LNCS 15931-15934; 51 regular + 24 tool + 4 case-study papers from 305 submissions | 2026-07-09 |
| 18 | https://conferences.i-cav.org/2025/award/ | CAV Award (annual, fundamental contributions to computer-aided verification); 2025 laureates cited | 2026-07-09 |
| 19 | https://dblp.org/db/conf/cav/index.html | dblp CAV proceedings stream, for edition numbering and exemplar verification | 2026-07-09 |

## Verified CAV 2027 facts used in skills

- **CAV 2027 is the 39th International Conference on Computer-Aided Verification**, held in
  **Amsterdam, The Netherlands, July 19-23, 2027** (main conference July 21-23), at KIT
  (sources 1, 3).
- **PC Chairs (also General Chairs):** Marieke Huisman (University of Twente) and Joost-Pieter
  Katoen (RWTH Aachen University & University of Twente). **AE Chairs:** Tim Quatmann and Tom van
  Dijk (sources 1, 2, 4).
- **Submission categories (three):** Regular Papers; Tool Papers; Application / Industrial
  Experience / Case Study Papers (source 1).
- **Page limits (LNCS format, excluding references and appendices):** Regular Papers **18 pages**;
  Tool Papers **18 pages**; Application/Industrial/Case Study Papers **10 pages**. A clearly marked
  appendix is allowed but reviewers are **not obliged** to read it. Camera-ready: **20 pages**
  (regular, tool) and **12 pages** (application), excluding bibliography and data availability
  statement (source 1).
- **Anonymity:** Regular Papers are **double-blind** (names and affiliations omitted, own work in the
  third person; non-conforming submissions rejected without review). Tool Papers and
  Application/Industrial/Case Study Papers are **single-blind** and need not be anonymized
  (source 1).
- **Per-author cap:** at most **5** submissions per author across all categories (source 1).
- **Key dates (CAV 2027, 23:59 AoE):** full papers **20 January 2027**; early rejection
  notification **4 March 2027**; tool-paper artifact registration **8 March 2027** (submission
  11 March); author response **5-8 April 2027**; notification **23 April 2027**; non-tool artifact
  registration **26 April 2027** (submission 3 May); camera-ready **18 May 2027**; conference
  **19-23 July 2027** (sources 1, 2).
- **Two-stage reviewing:** stage 1 gives each paper **two** reviews; papers with sufficient support
  get **two additional** reviews in stage 2 and a rebuttal option; the rest are rejected early
  (source 1).
- **Artifact evaluation:** **mandatory for Tool Papers** (at least the Functional badge; acceptance
  requires passing both review and AE; exemption only if requested at submission) and reviewed in
  parallel with the paper; **invited, optional and non-conditional** for the other categories,
  after notification; artifact intent declared at submission. AE is single-blind; badges
  **Available / Functional / Reusable**; every artifact nominates one reviewer (sources 1, 2).
- **Preprints:** arXiv allowed, but CAV strongly encourages not posting within 1 week around or
  1 month after the deadline (source 1).
- **Generative AI:** the CFP points to Springer's guidelines on AI authorship; no CAV-specific
  disclosure statement is required by the CFP (sources 1, 7).
- **Publication:** Springer **LNCS**; selected papers invited to special issues of *Formal Methods
  in System Design* and *Journal of the ACM* (source 1). The CAV 2027 proceedings page has no
  volume or open-access details yet (source 6). CAV 2024 (36th, Montreal): LNCS 14681-14683.
  CAV 2025 (37th, Zagreb): LNCS 15931-15934, 4 volumes, open access; 51 regular + 24 tool
  + 4 case-study papers accepted from **305 submissions** (sources 15-17).
- **CAV Award:** presented annually for fundamental contributions to computer-aided verification;
  a standing steering-committee award, separate from the conference decision (source 18).

## CAV 2026 facts (history, superseded by CAV 2027)

- CAV 2026 was the 38th CAV, **Lisbon, Portugal, July 26-29, 2026**, part of **FLoC 2026**;
  Program Chairs Anthony W. Lin, Eva Darulova and Philipp Rümmer (sources 10-14).
- Four categories: Regular (18 pages, anonymized), Short Tool (10 pages, not anonymized), Short
  Application (10 pages, anonymized), Industrial Experience Reports & Case Studies (10 pages, not
  anonymized) (sources 9, 10).
- Dates: paper deadline 28 January 2026; early-reject outcome about 4 March 2026; response
  30 March - 2 April 2026; notification 17 April 2026; artifact registration 22 April 2026.
- Artifact evaluation optional and non-conditional for every category, ≥2 AEC members per
  artifact (source 13).

## What makes CAV a distinctive process (honest reading)

CAV is not an ACM-journal conference and not an IEEE double-column one. Its research output is a
**Springer LNCS chapter**, single-column, in the `llncs` document class. Three features drive most
of this pack's advice and separate CAV from its siblings:

1. **A first-class Tool Paper track — now with a mandatory artifact.** In CAV 2027 Tool Papers get
   the same 18 pages as Regular Papers, are single-blind, and cannot be accepted unless the
   artifact passes AE (at least Functional). A working, usable verification tool evaluated on
   standard benchmarks is a recognized CAV contribution shape.
2. **Two-stage reviewing with an early reject.** Unlike a single-round rebuttal conference, CAV
   filters after two reviews, so a paper must survive stage 1 before it ever sees a rebuttal.
3. **An unusual anonymity split.** Only Regular Papers are double-blind in 2027; Tool and
   Application/Industrial/Case Study papers are single-blind — because a tool paper that hid its
   tool's identity would be unreviewable.

## Still cycle-volatile (verify every year)

- The **HotCRP submission link** for CAV 2027 (the CFP says it "will be added here once
  available") (**待核实**).
- The **CAV 2027 Program Committee** roster beyond the PC chairs (**待核实**).
- The CAV 2027 **LNCS volume and open-access arrangement** — the proceedings page says it "will be
  announced" (**待核实**).
- The text of **Springer's AI-authorship guidelines** referenced by the CFP — the linked page was
  behind a Springer sign-in wall on 2026-11-24 (**待核实**).
- **Registration fees** for CAV 2027 — not yet posted (**待核实**).
- Which verification competitions co-locate or affiliate in a given year (SMT-COMP historically
  began as a CAV 2005 satellite; SV-COMP runs at TACAS/ETAPS) (**待核实** for 2027).
- Every future edition's category set, page limits, anonymity split and AE rules — CAV changed all
  four between 2026 and 2027.

Resolved on 2026-11-24 (removed from this list): the submission portal (CAV 2027 CFP: HotCRP);
whether a separate abstract deadline precedes the paper deadline (the CAV 2027 CFP lists only
"Full papers due"); the camera-ready deadline (18 May 2027); the first-round notification date
(4 March 2027, no longer "tentative"); and the AE chairs.

## No editor-in-chief; cost model

CAV has **no standing editor-in-chief**; the rotating analogue is the per-edition PC Chairs and
the Steering Committee. CAV 2024 and CAV 2025 proceedings were published open access in LNCS; the
CAV 2027 open-access arrangement is not yet posted, and registration fees are not yet published.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and
python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "CAV 2027",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 18, "source": "https://conferences.i-cav.org/2027/cfp/", "note": "CAV 2027 Regular and Tool Papers; Application/Industrial Experience/Case Study Papers 10 pages; references and appendices excluded; camera-ready 20 (12 for application papers)"},
    "page_limit_includes_references": {"value": false, "source": "https://conferences.i-cav.org/2027/cfp/"},
    "review_mode": {"value": "double-blind", "source": "https://conferences.i-cav.org/2027/cfp/", "note": "Regular Papers only; Tool Papers and Application/Industrial/Case Study Papers are single-blind and need not be anonymized"},
    "template": {"value": "Springer LNCS format (llncs)", "source": "https://conferences.i-cav.org/2027/cfp/"},
    "portal": {"value": "HotCRP (CAV 2027 link not yet posted)", "source": "https://conferences.i-cav.org/2027/cfp/"},
    "supplement_policy": {"value": "clearly marked appendix allowed, reviewers not obliged to read it; artifact intent declared at submission", "source": "https://conferences.i-cav.org/2027/cfp/"},
    "data_code_policy": {"value": "artifact mandatory for Tool Papers (at least Functional badge, reviewed in parallel; exemption only if requested at submission); invited and non-conditional for other categories after acceptance", "source": "https://conferences.i-cav.org/2027/artifacts/"},
    "preprint_policy": {"value": "arXiv allowed; strongly discouraged within 1 week around or 1 month after the submission deadline", "source": "https://conferences.i-cav.org/2027/cfp/"},
    "llm_policy": {"value": "CFP refers authors to Springer's guidelines on AI authorship; no CAV-specific disclosure statement required", "source": "https://conferences.i-cav.org/2027/cfp/"},
    "required_statements": {"value": [], "source": "https://conferences.i-cav.org/2027/cfp/", "note": "no statement required in the submitted paper; a data availability statement is excluded from the camera-ready page limit"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```
