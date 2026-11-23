# External Tools - CVPR

Access date: 2026-07-08 (CVPR 2027 links added and checked 2026-11-24)

Official surfaces for CVPR work, plus the author-side verification passes to run against
them. CVPR policy is re-set by each edition's Program Chairs; the 2027 links below are
the live edition, the 2026 links the most recent completed cycle.

## Official surfaces

- Conference site (current cycle lands here): https://cvpr.thecvf.com/
- CVPR 2027 Call for Papers: https://cvpr.thecvf.com/Conferences/2027/CallForPapers
- CVPR 2027 Author Guidelines: https://cvpr.thecvf.com/Conferences/2027/AuthorGuidelines
- CVPR 2027 Dates and Deadlines: https://cvpr.thecvf.com/Conferences/2027/Dates
- CVPR 2027 Reviewer Guidelines: https://cvpr.thecvf.com/Conferences/2027/ReviewerGuidelines
- CVPR 2027 Organizers: https://cvpr.thecvf.com/Conferences/2027/Organizers
- OpenReview group (2027): https://openreview.net/group?id=thecvf.com/CVPR/2027/Conference
- CVPR 2026 Call for Papers: https://cvpr.thecvf.com/Conferences/2026/CallForPapers
- CVPR 2026 Author Guidelines: https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines
- CVPR 2026 Dates and Deadlines: https://cvpr.thecvf.com/Conferences/2026/Dates
- CVPR 2026 Reviewer Guidelines: https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelines
- Compute Reporting Form pages (2026 only): https://cvpr.thecvf.com/Conferences/2026/ComputeReporting
  and https://cvpr.thecvf.com/Conferences/2026/ComputeReportingClarification
- OpenReview group (2026): https://openreview.net/group?id=thecvf.com/CVPR/2026/Conference
- Official author kit (LaTeX + rebuttal template): https://github.com/cvpr-org/author-kit
- CVF open-access proceedings: https://openaccess.thecvf.com/menu
- IEEE Computer Society TC-PAMI (co-sponsor): https://tc.computer.org/tcpami/cvpr/
- CVF upcoming-conference list (future editions): https://www.thecvf.com/?p=137

Note: at build time (2026-07-08) `cvpr.thecvf.com` and `openaccess.thecvf.com` were not
directly fetchable (HTTP 403 at the gateway) and contents were confirmed via search
renderings and cross-sources; the CVPR 2027 pages were fetched directly on 2026-11-24 —
see the access-method note in [`official-source-map.md`](official-source-map.md).

## Author-side verification passes

1. **Identity pass** — every coauthor's OpenReview profile and author enrollment
   complete (publications imported for reciprocal-reviewer eligibility); run before the
   paper-registration deadline, not the paper deadline.
2. **Format pass** — build from the current author-kit branch, count pages including
   figures/tables against the cap, confirm overflow pages contain only references and the
   LLM Usage Statement.
3. **Anonymity + link pass** — PDF metadata, acknowledgements, self-citations in third
   person, zero external links in paper and supplement.
4. **Form pass** — OpenReview fields (abstract verbatim from PDF, conflicts, subject
   areas) plus the LLM Usage Statement (2027; the 2026 cycle had the Compute Reporting
   Form instead), drafted a day early.
5. **Attestation pass** — dual-submission window clear for every coauthor's other
   papers; media embargo understood by whoever runs the lab's publicity.

## Do not infer

- Do not project 2026 deadlines, the CRF, or reviewer-LLM rules onto 2027; the 2027
  pages differ (Nov 10 / 16 / 23, 2026 deadlines, LLM Usage Statement, quotas,
  conference-approved LLM tools). Do not project 2027 rules onto the next edition.
- Do not assume supplementary size caps, camera-ready forms, or presentation
  obligations from sibling venues (ICCV/ECCV/WACV publish similar-looking but distinct
  rules).
- Where official pages and OpenReview instructions disagree, treat the newest official
  posting as controlling, and record the discrepancy alongside the decision it forced.
