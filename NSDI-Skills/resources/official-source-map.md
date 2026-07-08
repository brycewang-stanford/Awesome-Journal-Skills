# Official Source Map - NSDI

Access date: 2026-07-08

This map records the official sources behind every NSDI-specific fact in this pack.
NSDI reissues its Call for Papers, deadline pair, track structure, and artifact rules for
every edition, and the same edition runs **two submission deadlines**, so a fact that was
true for the spring deadline can be stale by the fall one. Reopen the current
`usenix.org/conference/nsdi<yy>` pages before giving submission-ready advice.

## Access-method note

Direct fetches of `usenix.org` (HTML pages and the CFP PDFs under
`usenix.org/sites/default/files/`) and of `dblp.org` returned **HTTP 403** in the
verification environment on 2026-07-08. All facts below were therefore read through
search-engine renderings of the exact official URLs, cross-checked across multiple
independent renderings (USENIX conference pages, the HotCRP deadline pages, dblp
records, and publisher/author pages for exemplars). Anything that could not be
confirmed this way is listed under 待核实 below and is **not** stated as fact anywhere
in the pack.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.usenix.org/conference/nsdi27 | NSDI '27 identity: 24th USENIX Symposium on Networked Systems Design and Implementation, May 11-13, 2027, Omni Providence Hotel, Providence, RI, USA; program-committee membership listing. | 2026-07-08 |
| 2 | https://www.usenix.org/conference/nsdi27/call-for-papers | NSDI '27 two-deadline calendar (spring: abstracts April 16, 2026, papers April 23, 2026, notification July 23, 2026; fall: abstracts September 10, 2026, papers September 17, 2026, notification December 8, 2026; all 11:59 pm US EDT); three tracks (research, operational systems, frontiers); 12-page limit including footnotes, figures, and tables with extra pages allowed for references and appendices; double-blind rules and the operational-track anonymization exception; one-shot revision requirements; eight-submissions-per-author cap across deadlines; the resubmission ban after plain rejection; concurrent-submission citation wording; AI-tools-for-grammar allowance. | 2026-07-08 |
| 3 | https://www.usenix.org/conference/nsdi26 | NSDI '26 identity: 23rd edition, May 4-6, 2026, Hyatt Regency Lake Washington, Renton, WA, USA. | 2026-07-08 |
| 4 | https://www.usenix.org/conference/nsdi26/call-for-papers | NSDI '26 deadline pair as the prior-cycle anchor: spring abstracts April 18, 2025 and papers April 25, 2025 (11:59 pm US PDT), notification July 24, 2025; fall abstracts September 11, 2025 and papers September 18, 2025 (11:59 pm US PDT), notification December 9, 2025. | 2026-07-08 |
| 5 | https://www.usenix.org/conference/nsdi26/additional-info | The multiple-deadlines process: one-shot revision issued with a reviewer list of required issues; resubmission at a subsequent deadline (possibly the following NSDI); review by the same reviewers where possible; revisions that ignore the required issues rejected with no further one-shot option; papers rejected without a revision option barred from the next deadline; fall-deadline PC members who issue one-shot revisions serve as external reviewers the following year. | 2026-07-08 |
| 6 | https://www.usenix.org/conference/nsdi26/call-for-artifacts | NSDI '26 artifact evaluation open to all accepted papers; three separate badges, including Artifacts Available (permanent public retrieval, Zenodo encouraged with DOI); authors choose which badges the AEC should consider; artifact submission deadline July 31, 2025 with decisions October 14, 2025. | 2026-07-08 |
| 7 | https://nsdi27spring.usenix.hotcrp.com/ and https://nsdi26spring.usenix.hotcrp.com/deadlines | NSDI submissions run on per-deadline HotCRP sites named `nsdi<yy>spring` / `nsdi<yy>fall` under `usenix.hotcrp.com`. | 2026-07-08 |
| 8 | https://www.usenix.org/conferences/test-of-time-awards | USENIX Test of Time Awards program: papers presented at least 10 years ago; nominations received by January 4, 2027 considered for the 2026 award. | 2026-07-08 |
| 9 | https://www.usenix.org/conference/nsdi26/instructions-presenters | Accepted papers must designate one co-author as presenter via the Presenter Information form provided by the program co-chairs. | 2026-07-08 |
| 10 | https://dblp.org/db/conf/nsdi/ (read via search renderings) | Exemplar verification: NSDI edition numbering, proceedings titles, author lists, and page ranges for the papers in `exemplars/library.md`. | 2026-07-08 |
| 11 | https://www.usenix.org/conference/nsdi26/spring-accepted-papers | NSDI publishes a per-deadline accepted-papers list (spring cohort visible months before the event), confirming that the two deadlines produce two decision cohorts for the same edition. | 2026-07-08 |

## Verified facts used in the skills (2026-07-08 snapshot)

- NSDI '27 is the **24th** USENIX Symposium on Networked Systems Design and
  Implementation: **May 11-13, 2027, Omni Providence Hotel, Providence, RI, USA**
  (source 1).
- NSDI '27 runs **two submission deadlines**. Spring: abstracts **April 16, 2026**,
  full papers **April 23, 2026**, notification **July 23, 2026**. Fall: abstracts
  **September 10, 2026**, full papers **September 17, 2026**, notification
  **December 8, 2026**. All cutoffs **11:59 pm US EDT** (source 2). As of 2026-07-08
  the spring deadline has passed (notification pending) and the fall deadline is open.
- NSDI '27 accepts papers in **three tracks**: research, **operational systems**, and a
  **frontiers** track for bold, high-novelty ideas that may lack a complete evaluation
  (source 2).
- Submissions **and final papers** are capped at **12 pages including footnotes,
  figures, and tables**, with additional pages permitted for **references and
  appendices** (source 2).
- Review is **double-blind**; authors remove names, affiliations, acknowledgments, and
  funding, cite their own prior work in the third person, and never omit references for
  anonymity. Concurrent NSDI submissions are cited as "Under submission. Details
  omitted for double-blind reviewing." **Operational-track papers may keep company
  names, links, and real system names while still withholding author names** (source 2).
- A paper not accepted may receive a **one-shot revision**: reviewers list the issues
  that must be fixed; the authors resubmit at a subsequent deadline (possibly the
  following NSDI) with auxiliary material containing a change-highlighted version and a
  high-level change summary; the same reviewers re-review where possible; a revision
  that dodges the required issues is rejected with no second chance (sources 2, 5).
- A paper **rejected without a revision option cannot be submitted to the next
  deadline** — spring rejects skip the same edition's fall deadline, fall rejects skip
  the following edition's spring deadline (source 5).
- Each author may submit **at most eight papers** to NSDI '27 across all deadlines
  (source 2).
- NSDI '27 **encourages AI tools for grammar and clarity of human-written text**;
  questions about other generative-AI use go to the program co-chairs. Simultaneous
  submission, prior publication, and plagiarism are prohibited by USENIX (source 2).
- NSDI '26 (23rd edition) took place **May 4-6, 2026, in Renton, WA** (source 3); its
  deadline pair used **11:59 pm US PDT** cutoffs (source 4) — the time-zone convention
  itself is cycle-volatile.
- NSDI '26 ran **artifact evaluation for all accepted papers with three badges**
  (Artifacts Available confirmed by name; Zenodo-with-DOI encouraged), with artifact
  submission July 31, 2025 and decisions October 14, 2025 (source 6).
- NSDI awards a **Community Award** to the best paper whose code and/or dataset is made
  publicly available by the final-papers deadline (NSDI CFP series; e.g., the NSDI '23
  Community Award to the Magma access-network paper, reported by USENIX pages and
  author institutions).
- Submissions are uploaded to per-deadline **HotCRP** sites (source 7).
- Out-of-scope guidance in the CFP series: papers with no contribution to the design of
  networked systems or the networking stack, hardware architecture, physical-layer
  techniques such as beamforming and modulation, and sensing/localization work
  (sources 2, 4).

## Reported facts (secondary renderings; labeled as reported wherever used)

- NSDI Test of Time selections such as X-Trace (NSDI 2007, honored 2017) and the
  third-party web-tracking study (NSDI 2012, honored at NSDI '23) are reported by the
  authors' institutions (Brown CS, UW Allen School, UCSD) and USENIX loginonline; the
  full official winners list could not be rendered.
- The Spark RDD paper's NSDI '12 Best Paper award is reported by the Apache Spark
  project's own announcement.

## 待核实 (could not be verified live on 2026-07-08 — never state as fact)

- NSDI '27 **program co-chair names** (the CFP rendering references "the program
  co-chairs" without naming them in retrievable text).
- NSDI '27 **camera-ready/final-paper deadlines** for either cohort, and any early
  publication option for spring-accepted papers.
- The NSDI '27 **Call for Artifacts**: badge set, artifact deadlines, and whether the
  evaluation committee coordinates with the sysartifacts/secartifacts community sites.
- The exact names of the **other two NSDI '26 badges** beyond Artifacts Available
  (USENIX's scheme elsewhere uses Artifacts Functional and Results Reproduced, but the
  NSDI '26 wording was not retrievable in full).
- Whether NSDI '27 has **any author-response/rebuttal stage** (none appears in the
  rendered CFP; absence was not confirmable) and whether reviewers are obligated to
  read appendices.
- Registration rates, in-person presentation requirements beyond the presenter form,
  grants/discounts, and the exact ethics-section wording of the '27 CFP.
- NSDI Test of Time winners for 2024-2026 (nominations for the 2026 award close
  January 4, 2027) and the page range of the X-Trace paper.
- Whether the 11:59 pm **EDT vs PDT** convention is a deliberate '27 change or a page
  inconsistency — re-check the live deadline page before deadline week.

## Still cycle-volatile

Deadline dates and time zones, track list (the frontiers track is new in the rendered
'27 CFP), page budget, anonymization wording, one-shot-revision mechanics, artifact
badges, award definitions, HotCRP site names, and registration duties. Every skill in
this pack treats the numbers above as a dated snapshot, not a standing rule.
