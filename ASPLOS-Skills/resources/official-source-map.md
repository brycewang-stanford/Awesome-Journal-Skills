# Official Source Map - ASPLOS

Access date: 2026-07-08

This map records the official sources behind every ASPLOS-specific fact in this pack.
ASPLOS mechanics are re-decided per edition by that edition's organizing committee;
reopen the current Call for Papers, the HotCRP cycle pages, and the artifact-evaluation
pages before giving submission-ready advice.

**Access-method note (2026-07-08):** direct fetches of `asplos-conference.org`, the
HotCRP sites, and `dblp.org` were blocked by the network gateway used for verification,
so official-page contents were read through search-engine renderings of those exact
URLs and cross-checked against the ACM Digital Library proceedings pages and the
SIGARCH award pages. Before relying on any deadline, cap, or policy below, open the
primary URLs directly.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.asplos-conference.org/asplos2027/cfp/ | ASPLOS 2027 Call for Papers: two submission deadlines (April 15, 2026 and September 9, 2026, AoE); scope = OS, PL, computer architecture and their intersection; topics list; 11-page limit for single-spaced two-column text covering all text, figures, tables, and footnotes, references excluded; full non-abbreviated first and last names of all co-authors in citations (no "et al."); hyperlinked citations and DOIs requested; appendices/supplemental in the submission file with no page limit but reviewers neither required nor encouraged to read them; self-containment rule; double-blind rules (third-person self-citation, no "removed for blind review", arXiv/tech-report postings not prior publication and may be ignored by the submission); double-blind rapid review round on the first two pages, modeled on early screening at journals such as Science/Nature, prioritizing intersection work; rebuttal guidance (correct factual errors, answer reviewer questions; no hard word cap but reviewers not expected to read beyond 800 words); Accept / Major Revision / Reject outcomes with Major Revision resubmitted at the camera-ready deadline (6 weeks from notification) and a revision counting as a submission; mandatory LaTeX template with rejection-without-review for violations; ACM authorship policy incl. Generative-AI disclosure (in Acknowledgments before References if used). | 2026-07-08 |
| 2 | https://asplos27-apr.hotcrp.com/deadlines | ASPLOS'27 April-cycle HotCRP site and its deadline page: full-paper deadline Wednesday, April 15, 2026, 11:59 PM AoE; submissions must be complete in HotCRP by the deadline to be reviewed. | 2026-07-08 |
| 3 | https://www.asplos-conference.org/ | ASPLOS 2027 identity: Heraklion, Crete, Greece, April 11-15, 2027; ASPLOS as ACM's premier forum for multidisciplinary systems research spanning hardware and software; 2027 timeline (April cycle: author response July 6-9, 2026, notification July 27, 2026; September cycle: submission September 9, 2026, author response December 1-4, 2026, notification December 21, 2026); no separate abstract deadline for 2027. | 2026-07-08 |
| 4 | https://www.asplos-conference.org/asplos2027/artifact-evaluation/ and https://www.asplos-conference.org/asplos2027/ae-for-authors/ | ASPLOS 2027 artifact evaluation: authors of accepted papers submit an Artifact Appendix (ae.tex template or equivalent sections) describing software/hardware/dataset dependencies, key results to reproduce, and how to prepare, run, and validate experiments; an independent AE committee works with authors collaboratively; three requested badges — Available (requires a publicly accessible archival repository), Functional, Reproducible — scored by reviewers; badges attached by authors or ACM. | 2026-07-08 |
| 5 | https://dl.acm.org/doi/proceedings/10.1145/3760250 and https://dl.acm.org/doi/proceedings/10.1145/3779212 | Proceedings of the 31st ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS 2026), Volumes 1 and 2, on the ACM Digital Library — confirms ASPLOS 2026 as the 31st edition and ACM as publisher. | 2026-07-08 |
| 6 | https://www.asplos-conference.org/asplos2026/ | ASPLOS 2026: Pittsburgh, PA, USA, March 22-26, 2026 (The Landing Hotel) — the most recent completed edition, used as the historical anchor for the multi-cycle model. | 2026-07-08 |
| 7 | https://www.sigarch.org/benefit/awards/acm-sigarch-sigplan-sigops-asplos-influential-paper-award/ | The ACM SIGARCH/SIGPLAN/SIGOPS ASPLOS Influential Paper Award: presented annually since ASPLOS 2011 to papers that appeared ten or more ASPLOS conferences prior; the three sponsoring SIGs confirm the venue's tri-community identity. Winner facts used in `exemplars/library.md`. | 2026-07-08 |
| 8 | https://www.asplos-conference.org/asplos2024/acm-sigarch-sigplan-sigops-asplos-influential-paper-award/ | The 2024 Influential Paper Award page: DianNao (ASPLOS 2014), Paragon (ASPLOS 2013), and ELI (ASPLOS 2012), with full author lists, used to verify exemplar rows. | 2026-07-08 |
| 9 | https://www.sigarch.org/asplos-2025-trip-blog-bridging-communities-the-first-asplos-eurosys-joint-conference/ | ASPLOS 2025 (30th edition, Rotterdam) ran as the first ASPLOS-EuroSys joint conference — context for how venue logistics shift per edition; the 30th-edition proceedings anchor is https://dl.acm.org/doi/proceedings/10.1145/3669940. | 2026-07-08 |
| 10 | https://www.sigarch.org/call-contributions/asplos-2026-2/ | SIGARCH's cross-posting of the ASPLOS 2026 call — secondary confirmation of the 2026 cycle mechanics and of SIGARCH sponsorship. | 2026-07-08 |

## Verified 2027-cycle facts used in the skills

- ASPLOS 2027 takes place April 11-15, 2027 in Heraklion, Crete, Greece. The 2026
  edition was the 31st (ACM DL, source 5), making 2027 the 32nd in sequence — but the
  ordinal for 2027 was not itself read from an official page, so treat "32nd" as
  arithmetic, 待核实 against the eventual proceedings title.
- ASPLOS 2027 accepts submissions at **two deadlines**: April 15, 2026 (passed as of
  2026-07-08) and **September 9, 2026** (the next open gate), both 11:59 PM AoE, with
  no separate abstract-registration deadline. This replaces the three-deadline
  (spring/summer/fall) pattern used by recent editions such as ASPLOS 2026.
- April-cycle pipeline: author response July 6-9, 2026 — **open on the pack's check
  date** — and notification July 27, 2026. September-cycle pipeline: author response
  December 1-4, 2026; notification December 21, 2026.
- Submissions run on **HotCRP**, one site per cycle (April cycle:
  `asplos27-apr.hotcrp.com`).
- Format: at most **11 pages of single-spaced two-column text**, a limit that covers
  all text, figures, tables, and footnotes; **references are excluded** and unlimited;
  the LaTeX template is mandatory and violations risk rejection without review.
- Citation rules unusual for the field: reference entries must give the **full,
  non-abbreviated first and last names of every co-author** (no "et al."), in-text
  citation numbers should hyperlink to the reference list, and DOIs/clickable links
  are requested per entry.
- Appendices and supplemental material may be included in the submission file with no
  page limit, but the 11 pages must be self-contained and **reviewers are neither
  required nor encouraged to read beyond them**.
- Review is **double-blind** with a **rapid review round that considers only the first
  two pages** of each submission; a majority of submissions may not advance past it,
  and it explicitly prioritizes work at the architecture-languages-OS intersection.
- Rebuttals should correct factual errors and answer reviewer questions; there is no
  hard cap, but **reviewers are not expected to read beyond 800 words**.
- Outcomes are **Accept, Major Revision, or Reject**. A Major Revision is resubmitted
  at the camera-ready deadline (6 weeks from notification), and the revision itself
  counts as a submission — a later resubmission's change note describes deltas
  relative to the revision, not the original.
- Self-citation must be in the third person; "removed for blind review" placeholders
  are disallowed; arXiv/tech-report/social postings are not prior publications, and
  the submission may ignore them to preserve anonymity.
- Authors must follow the **ACM authorship policy including its Generative-AI rules**:
  GenAI use must be fully disclosed, in the Acknowledgments immediately before the
  References when that section is used for it.
- Artifact evaluation is post-acceptance, collaborative, and organized around the
  three ACM-style badges (Available / Functional / Reproducible) with an Artifact
  Appendix per the `ae.tex` template; the Available badge requires a public archival
  repository.
- ASPLOS is sponsored by ACM SIGARCH, SIGPLAN, and SIGOPS; proceedings are published
  by ACM in the Digital Library, in multiple volumes per edition under the multi-cycle
  model. There is no standing editor-in-chief — program leadership rotates per edition.

## Reported but not officially confirmed (treat as 待核实)

- The rapid-review advancement rate ("a majority of submissions may not advance") is
  CFP framing, not a published statistic; do not quote an acceptance-rate number.
- ASPLOS 2026 proceedings volume count: two volumes were found on ACM DL (source 5);
  whether a third exists for the fall cycle was not confirmed.

## Not found / still cycle-volatile (待核实 every cycle)

- ASPLOS 2027 Program and General Chairs' names (organization page not directly
  fetchable at check time).
- The September-cycle HotCRP URL (only the April-cycle site was confirmed).
- Camera-ready page allowance, ACM rights-form workflow, and TAPS details for 2027.
- Registration fees, mandatory-attendance and presentation rules for accepted papers.
- Artifact-evaluation calendar dates for each 2027 cycle, AEC chairs, and whether AE
  participation affects any award eligibility.
- Any per-author submission cap for 2027 — none was found; do not assert one exists
  or does not exist.
- Best Paper and distinguished-artifact mechanics for 2027.
- All future-cycle dates, page limits, template versions, and portal URLs.
