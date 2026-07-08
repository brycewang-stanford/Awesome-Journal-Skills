# Official Source Map - MICRO

Access date: **2026-07-08**

This map records the official sources behind every MICRO-specific fact in this pack.
MICRO policy is set per edition by rotating organizers; reopen the current cycle's
CFP, submission guidelines, and HotCRP site before giving deadline-sensitive advice.

## Access-method note

Direct fetches of `microarch.org`, `sigarch.org`, `ieeetcca.org`, and HotCRP were
blocked (HTTP 403) in the verification environment. Official pages were therefore
read via **search-engine renderings of the exact URLs** and cross-checked against
independent surfaces: the ACM Digital Library proceedings records, IEEE Xplore
proceedings records, dblp entries, and SIGARCH/TCCA repostings of the CFP. Facts
that could not be confirmed by at least one rendered official page plus a
cross-check are marked 待核实 below and are **not** stated as facts in the skills.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.microarch.org/micro59/ | MICRO 2026 identity: 59th IEEE/ACM International Symposium on Microarchitecture, Athens, Greece, October 31 – November 4, 2026. | 2026-07-08 |
| 2 | https://www.microarch.org/micro59/submit/papers.php | 2026 Call for Papers: abstract deadline March 31, 2026 11:59 PM EDT; full paper April 7, 2026 11:59 PM EDT; rebuttal/revision June 3–17, 2026; notification July 7, 2026; camera-ready September 11, 2026; double-blind review. | 2026-07-08 |
| 3 | https://www.microarch.org/micro59/submit/guidelines.php | Submission guidelines: ≤ 11 pages excluding references; **no appendix allowed**; unlimited reference pages; every reference lists all authors (no "et al."); minimum 9pt text; page numbers required; MICRO 2026 LaTeX template; no `\vspace`/space-squeezing; submissions inspected visually and automatically, rejectable even if the HotCRP format check passed; artifact links fully anonymized or removed; no acknowledgments; professional-conduct rule covering reviews, comments, and rebuttals with ACM/IEEE reporting. | 2026-07-08 |
| 4 | https://micro2026.hotcrp.com/ | Official submission site for MICRO 2026 (HotCRP), incl. `/deadlines` page. | 2026-07-08 |
| 5 | https://www.microarch.org/micro59/submit/industrial.php | Inaugural MICRO 2026 Industry Track: dedicated CFP and a review process tailored to production-focused work. | 2026-07-08 |
| 6 | https://www.microarch.org/micro58/submit/artifacts.php | MICRO 2025 artifact evaluation (pattern anchor): post-acceptance AE; ACM badges printed on papers and attached in ACM DL metadata; "Artifact Available" requires a public archival repository (Zenodo, FigShare, Dryad); optional two-page artifact appendix in the camera-ready, free of charge. | 2026-07-08 |
| 7 | https://www.sigmicro.org/awards/tot/ (also https://microarch.org/tot/) | MICRO Test of Time Award: 2024 award to "Utility-Based Cache Partitioning" (Qureshi & Patt, MICRO 2006); 2025 (11th ToT) to "Die Stacking (3D) Microarchitecture" and "Optimizing NUCA Organizations and Wiring Alternatives for Large Caches with CACTI 6.0," selected from 165 eligible MICRO 2003–2007 papers. | 2026-07-08 |
| 8 | https://www.sigmicro.org/micro-hall-of-fame/ | MICRO Hall of Fame: authors with eight or more MICRO papers; founded 2008 by Erik Altman and Amir Roth; inductees announced at the symposium. | 2026-07-08 |
| 9 | https://dl.acm.org/doi/proceedings/10.1145/3725843 and https://ieeexplore.ieee.org/xpl/conhome/1000440/all-proceedings | Proceedings placement: MICRO volumes appear in both the ACM Digital Library (e.g., 58th, 2025) and IEEE Xplore (conference series record); IEEE/ACM co-sponsorship (ACM SIGMICRO + IEEE Computer Society as technical sponsors, per the venue's public records). | 2026-07-08 |
| 10 | Sibling-venue calendars: https://www.asplos-conference.org/ (ASPLOS 2027: Apr 15 & Sept 9, 2026 deadlines, AoE), https://iscaconf.org/isca2026/ + ISCA 2027 postings (abstracts Nov 10 / papers Nov 17, 2026; Atlanta June 5–9, 2027), HPCA 2027 postings via conf.researchr.org (papers July 24, 2026; Salt Lake City, March 2027; notification Nov 6, 2026) | The four-venue architecture calendar taught in `micro-workflow` and `micro-topic-selection`. | 2026-07-08 |

## Verified facts used across the skills

- MICRO 2026 is the **59th** edition — an ordinal consistent with the series'
  1968 origin as the microprogramming workshop (class-2 arithmetic note, see below).
- 2026 deadlines run on **EDT**, not AoE — a deliberate teaching point in
  `micro-submission` and `micro-workflow`.
- The 2026 format rule set: 11 content pages + unlimited references, **no
  appendix**, all-author references, 9pt floor, mandatory page numbers, template
  fidelity, dual (visual + automated) inspection.
- Double-blind obligations persist through the June 3–17 rebuttal/revision window;
  artifact links anonymized-or-removed; no acknowledgments at submission.
- Post-acceptance artifact evaluation with ACM badges is established venue practice
  (2025 verified; 2026 instance 待核实).
- Exemplar bibliographic records verified against ACM DL / dblp: Yeh & Patt
  MICRO 1991 (pp. 51–61, DOI 10.1145/123465.123475); Qureshi & Patt MICRO 2006
  (pp. 423–432, DOI 10.1109/MICRO.2006.49); Muralimanohar et al. MICRO 2007
  (pp. 3–14, DOI 10.1109/MICRO.2007.30); Li et al. MICRO 2009 (pp. 469–480,
  DOI 10.1145/1669112.1669172); Chen et al. MICRO 2014 (pp. 609–622,
  DOI 10.1109/MICRO.2014.58).

## Fact classes

1. **Verified 2026-cycle facts** — trace to sources 1–5 above (dates, page rules,
   anonymity rules).
2. **Derived / secondary facts** — labeled in the skills: the 1968 lineage is
   arithmetic from the 59th ordinal plus the venue's public history pages;
   reviewer-rubric descriptions are community-norm composites, not quoted forms.
3. **待核实 items** — listed below; phrased in the skills as questions, never as
   facts.

## 待核实 (could not be verified live on 2026-07-08)

- MICRO 2026 organizing committee names (the `micro59/committees/org.php` page
  exists but its contents did not render through the access path).
- MICRO 2026 artifact-evaluation page, calendar, and whether the 2025 badge/appendix
  arrangement carries over unchanged.
- Industry Track deadlines, page rules, and review-form details.
- Rebuttal/revision window mechanics: whether a revised PDF may be uploaded and any
  length cap on the text response.
- Camera-ready page allowance, publisher author-kit details, and registration /
  in-person presentation requirements for Athens.
- Any LLM/AI-use authorship policy for the 2026 cycle.
- MICRO 2027 dates, location, and deadline (assumed early-April rhythm in
  `micro-workflow`, explicitly marked as assumption).

## Maintenance rule

Before repeating any date, cap, or policy from this pack: reopen sources 1–3 for
the current cycle, prefer the newest CFP/guidelines/HotCRP text on conflict, and
move anything that fails re-verification into the 待核实 list rather than deleting
the record of the check.
