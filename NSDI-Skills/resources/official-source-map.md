# Official Source Map - NSDI

Access date: 2026-07-08. NSDI '27 home page, Call for Papers, Call for Artifacts, Instructions
for Presenters, Spring Accepted Papers, the NSDI '27 fall HotCRP deadline page, the NSDI '26
pages and the USENIX Test of Time Awards page **re-verified 2026-11-24** against the live
pages (direct fetch with `curl`; the 403 block recorded in July no longer applies).

**Edition status, checked 2026-11-24.** The live edition is still **NSDI '27**, the 24th
USENIX Symposium on Networked Systems Design and Implementation, **May 11-13, 2027, Omni
Providence Hotel, Providence, RI, USA**. Both of its submission cycles are closed: the spring
cycle (papers April 23, 2026) has notified and its accepted-papers list is public, and the fall
cycle (papers September 17, 2026) notifies on **December 8, 2026**. The next submission gate
belongs to **NSDI '28**, whose page at `usenix.org/conference/nsdi28` exists but is an empty
placeholder on 2026-11-24 — no dates, location, or Call for Papers — so no NSDI '28 date is
stated anywhere in this pack. Until that CFP appears, the NSDI '27 rules below are the latest
published rules.

This map records the official sources behind every NSDI-specific fact in this pack.
NSDI reissues its Call for Papers, deadline pair, track structure, and artifact rules for
every edition, and the same edition runs **two submission deadlines**, so a fact that was
true for the spring deadline can be stale by the fall one (the NSDI '27 Authorship Policy,
for example, was added "new for the fall deadline"). Reopen the current
`usenix.org/conference/nsdi<yy>` pages before giving submission-ready advice.

## Access-method note

On 2026-07-08 direct fetches of `usenix.org` and `dblp.org` returned **HTTP 403** in the
verification environment and the facts were read through search-engine renderings of the
exact official URLs. On **2026-11-24** `usenix.org` and `usenix.hotcrp.com` answered direct
`curl -sL` requests (HTTP 200), so every NSDI '27 fact below was re-read from the live page
text. dblp-based exemplar checks were not repeated. Anything still unconfirmed is listed under
待核实 below and is **not** stated as fact anywhere in the pack.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.usenix.org/conference/nsdi27 | NSDI '27 identity: 24th USENIX Symposium on Networked Systems Design and Implementation, May 11-13, 2027, Omni Providence Hotel, Providence, RI, USA; organizers listing. | 2026-11-24 |
| 2 | https://www.usenix.org/conference/nsdi27/call-for-papers | NSDI '27 two-deadline calendar (spring: abstracts April 16, 2026, papers April 23, 2026, notification July 23, 2026, final paper files October 20, 2026; fall: abstracts September 10, 2026, papers September 17, 2026, notification December 8, 2026, final paper files March 4, 2027; submission cutoffs 11:59 pm US EDT); "What's New" (Authorship Policy new for the fall deadline; Frontiers Track; prescreening on the Introduction; at most eight (8) papers per author); three tracks (research, frontiers, operational systems) declared on the title page and the form, no track changes; prescreening of the Introduction (no more than 3 pages) for scope, accessibility to a non-specialist NSDI PC member, and track-conforming claims; 12-page limit including footnotes, figures, and tables for submissions and final papers, extra pages for references and appendices that reviewers are not required to read; two-column, 10-point Times-Roman on 12-point leading, 7" x 9" text block, 8.5" x 11" paper, numbered pages, non-conforming papers rejected without review; double-blind rules and the operational-track anonymization exception; one-shot revision requirements and the under-review status during the revision period; resubmission ban after plain rejection; workshop-paper extensions and SIGCOMM-reject / HotNets-extension resubmissions; generative-AI rule (no papers produced entirely or substantively by AI; HotCRP attestation that text is primarily human written; AI for grammar and clarity encouraged); technical reports (e.g. arXiv) allowed with a different title and system name; ethics attestation at submission; at least one author registers at full price per paper; shepherding of accepted papers; Best Paper and Community Award; program co-chairs. | 2026-11-24 |
| 3 | https://www.usenix.org/conference/nsdi26 | NSDI '26 identity: 23rd edition, May 4-6, 2026, Renton, WA, USA. | 2026-11-24 |
| 4 | https://www.usenix.org/conference/nsdi26/call-for-papers | NSDI '26 deadline pair as the prior-cycle anchor: spring abstracts April 18, 2025 and papers April 25, 2025 (11:59 pm US PDT); fall abstracts September 11, 2025 and papers September 18, 2025 (11:59 pm US PDT). | 2026-11-24 |
| 5 | https://www.usenix.org/conference/nsdi26/additional-info | The multiple-deadlines and one-shot-revision rationale ("pioneered by VLDB") and process: required-issue list, resubmission at a subsequent deadline, same reviewers where possible, no second one-shot, plain rejects barred from the next deadline. | 2026-11-24 |
| 6 | https://www.usenix.org/conference/nsdi27/call-for-artifacts | NSDI '27 artifact evaluation open to all accepted papers, optional, starting only after acceptance; three badges — Artifacts Available (Zenodo with DOI encouraged), Artifacts Functional, Results Reproduced — chosen by the authors at artifact submission; spring cycle artifact submission August 7, 2026 11:59 PM US PDT, decisions October 13, 2026; fall cycle artifact submission December 18, 2026 11:59 PM US PST, decisions February 19, 2027; final papers October 20, 2026 / March 4, 2027; single-blind AE; optional Artifact Appendix of up to two pages; per-cycle AE HotCRP sites. | 2026-11-24 |
| 7 | https://nsdi27fall.usenix.hotcrp.com/deadlines | Per-deadline HotCRP sites (`nsdi27spring` / `nsdi27fall` under `usenix.hotcrp.com`); the fall clock shows registration Thursday Sep 10, 2026 and submission Thursday Sep 17, 2026, each 8:59 PM PDT (= 11:59 pm US EDT). | 2026-11-24 |
| 8 | https://www.usenix.org/conferences/test-of-time-awards | USENIX Test of Time Awards: papers presented at least 10 years ago; winners chosen by steering committees and past program chairs; NSDI invites community nominations via the upcoming symposium's page; NSDI honorees include X-Trace (NSDI '07, honored at NSDI '17), Mesos (NSDI '11, NSDI '21), Third-Party Tracking (NSDI '12, NSDI '23), Header Space Analysis (NSDI '24), Open vSwitch (NSDI '25), and Network Virtualization in Multi-tenant Datacenters (NSDI '26). | 2026-11-24 |
| 9 | https://www.usenix.org/conference/nsdi27/instructions-presenters | Final papers: spring cycle by Tuesday, October 20, 2026; fall cycle by Thursday, March 4, 2027; no longer than 12 pages excluding references and appendices; page numbers suppressed, fonts embedded, OCR applied; HotCRP title/author/abstract must match the PDF; consent-to-publish form per author; one designated presenter per paper via the Presenter Information form; embargo requests to Production. | 2026-11-24 |
| 10 | https://dblp.org/db/conf/nsdi/ (read via search renderings) | Exemplar verification: NSDI edition numbering, proceedings titles, author lists, and page ranges for the papers in `exemplars/library.md`. | 2026-07-08 |
| 11 | https://www.usenix.org/conference/nsdi27/spring_accepted_papers | NSDI '27 Spring Accepted Papers list is public months before the May 2027 event, confirming that the two deadlines produce two decision cohorts for the same edition. | 2026-11-24 |
| 12 | https://www.usenix.org/conference/nsdi28 | NSDI '28 placeholder page: title only, no dates, location, or Call for Papers on 2026-11-24. | 2026-11-24 |

## Verified facts used in the skills (NSDI '27, re-verified 2026-11-24)

- NSDI '27 is the **24th** USENIX Symposium on Networked Systems Design and
  Implementation: **May 11-13, 2027, Omni Providence Hotel, Providence, RI, USA**
  (source 1).
- NSDI '27 runs **two submission deadlines**. Spring: abstracts **April 16, 2026**,
  full papers **April 23, 2026**, notification **July 23, 2026**, final paper files
  **October 20, 2026**. Fall: abstracts **September 10, 2026**, full papers
  **September 17, 2026**, notification **December 8, 2026**, final paper files
  **March 4, 2027**. Submission cutoffs are **11:59 pm US EDT** (source 2); the fall
  HotCRP clock renders them as 8:59 PM PDT, the same instant (source 7). As of
  2026-11-24 both submission gates are closed and fall notification is pending.
- NSDI '27 accepts papers in **three tracks**: traditional research, **operational
  systems**, and **frontiers** (bold, high-novelty ideas that are hard to evaluate in the
  traditional sense — not "early-stage" work). The track is stated on the title page and
  the form, a paper goes to one track only, and it cannot change track (source 2).
- **Prescreening (new in '27):** before full review, reviewers read only the
  **Introduction, which should be no more than 3 pages**, and check (a) scope, (b) that it
  is understandable by an NSDI PC member outside the subfield, and (c) that the claims fit
  the chosen track (source 2).
- Submissions **and final papers** are capped at **12 pages including footnotes,
  figures, and tables**, with additional pages for **references and appendices**; the
  paper must stand alone and **reviewers are not required to read** the appendix material
  (source 2). Format: two-column, **10-point** Times-Roman or similar on **12-point**
  leading, 7" x 9" text block, 8.5" x 11" paper, numbered pages; papers not meeting these
  criteria are **rejected without review**, with no extension for reformatting (source 2).
- Review is **double-blind**; authors remove names, affiliations, acknowledgments, and
  funding, omit links to their own online content (use the form's auxiliary material),
  cite their own prior work in the third person, and never omit references for
  anonymity. Concurrent NSDI submissions are cited as "Under submission. Details
  omitted for double-blind reviewing." **Operational-track papers may keep company
  names, links, and real system names while still withholding author names** (source 2).
- **Technical reports** (e.g. arXiv) may be available concurrently **provided the
  submission uses a different title and system name** (source 2).
- A paper not accepted may receive a **one-shot revision**: reviewers list the issues
  that must be fixed; the authors resubmit at a subsequent deadline (possibly the
  following NSDI) with auxiliary material containing a change-highlighted version and a
  high-level change summary; the same reviewers re-review where possible; a revision
  that dodges the required issues is rejected with no second chance. **During the
  revision period the paper counts as under review at NSDI** and cannot go elsewhere
  unless withdrawn (sources 2, 5).
- A paper **rejected without a revision option cannot be submitted to the next
  deadline** — spring rejects skip the same edition's fall deadline, fall rejects skip
  the following edition's spring deadline. A one-shot paper sent to the immediately next
  deadline may only come as a one-shot revision with its auxiliary material (source 2).
- SIGCOMM-rejected papers and significant extensions of HotNets papers may be submitted
  if those notifications precede the NSDI deadline; workshop-paper extensions need an
  anonymous self-citation, the deanonymized citation and a difference statement on the
  form, and may not be concurrent with the workshop's review (source 2).
- Each author may be listed on **at most eight** submissions or accepted papers to NSDI
  '27 across all deadlines; violations are desk-rejected until the limit holds
  (source 2).
- **Generative AI:** papers produced entirely or substantively by generative AI are not
  allowed (writing an entire section, including related work or the conclusion, with AI
  is a violation); authors **attest in HotCRP that all text was primarily human
  written**; AI tools for grammar and clarity of human-written text are encouraged
  (source 2).
- **Authorship:** from the fall '27 deadline, papers must follow the USENIX Authorship
  Policy (source 2).
- **Ethics:** authors attest at submission that the work complies with their
  institutions' ethical standards; papers with user data are encouraged to include a
  subsection on the ethical issues; the PC may hold its own ethics discussion (source 2).
- Simultaneous submission, prior publication, plagiarism, and NDA-encumbered papers are
  prohibited or not considered (source 2).
- **Accepted papers** are shepherded by a PC member through an editorial revision; at
  least one author per paper registers **at full price** (not the student rate) and
  presents; papers are online to registered attendees before the event and public from
  the first day, with embargo on request (source 2).
- **Final papers** (source 9): spring cycle **October 20, 2026**, fall cycle **March 4,
  2027**; still 12 pages excluding references and appendices; page numbers suppressed;
  fonts embedded; OCR applied; HotCRP metadata must match the PDF; each author signs the
  consent-to-publish form; exactly one designated presenter per paper via the Presenter
  Information form.
- **NSDI '27 artifact evaluation** (source 6): optional, open to all accepted papers,
  starting only after acceptance; **three badges** — **Artifacts Available**, **Artifacts
  Functional**, **Results Reproduced** — chosen by the authors at artifact submission;
  spring cycle artifacts due **August 7, 2026** (11:59 PM US PDT) with decisions
  **October 13, 2026**; fall cycle artifacts due **December 18, 2026** (11:59 PM US PST)
  with decisions **February 19, 2027**; evaluation is single-blind; authors are encouraged
  to add an Artifact Appendix of up to **two** pages.
- NSDI awards **Best Paper** award(s) and a **Community Award** for the best paper whose
  code and/or data set is publicly available by the final paper deadline; authors tag
  their paper for the Community Award during submission (source 2).
- **Program Co-Chairs, NSDI '27:** **Marcos K. Aguilera** (NVIDIA) and **Justine Sherry**
  (Carnegie Mellon University and Amazon Prime Video) (source 2).
- NSDI '26 (23rd edition) took place **May 4-6, 2026, in Renton, WA** (source 3); its
  deadline pair used **11:59 pm US PDT** cutoffs (source 4) — the time-zone convention
  itself is cycle-volatile.
- Out-of-scope guidance in the '27 CFP: papers with no contribution to the design of
  networked systems or the networking stack, hardware architecture, physical-layer
  techniques such as beamforming and modulation, sensing/localization work, and user
  interfaces (source 2).
- **USENIX Test of Time Awards** (source 8) honor papers presented at least 10 years
  earlier; NSDI honorees include X-Trace (NSDI '07, honored at NSDI '17), Mesos (NSDI '11,
  honored at NSDI '21), the third-party web-tracking study (NSDI '12, honored at NSDI '23),
  Header Space Analysis (NSDI '24), Open vSwitch (NSDI '25), and Network Virtualization in
  Multi-tenant Datacenters (NSDI '26).

## Reported facts (secondary renderings; labeled as reported wherever used)

- The Spark RDD paper's NSDI '12 Best Paper award is reported by the Apache Spark
  project's own announcement.
- The NSDI '23 Community Award to the Magma access-network paper is reported by USENIX
  pages and author institutions.

## 待核实 (could not be verified live on 2026-11-24 — never state as fact)

- **NSDI '28**: dates, location, deadline pair, time zone, and any rule changes (the
  conference page is an empty placeholder on 2026-11-24).
- Registration rates, grants/discounts, and the in-person presentation requirement beyond
  the full-price registration and presenter-form rules.
- The full text of the USENIX Authorship Policy's criteria (linked from the CFP, not
  re-read for this pack).
- The page range of the X-Trace paper (dblp not re-read).
- Whether NSDI '27 holds an **author-response/rebuttal stage**: the CFP, read in full on
  2026-11-24, describes prescreening, review, one-shot revision and shepherding but no
  rebuttal; the pack treats "no rebuttal" as the CFP's silence, not as an explicit rule.

## Still cycle-volatile

Deadline dates and time zones, track list (the frontiers track and prescreening are new in
'27), page budget, anonymization wording, one-shot-revision mechanics, generative-AI and
authorship policies, artifact badges and dates, award definitions, HotCRP site names, and
registration duties. Every skill in this pack treats the numbers above as a dated snapshot,
not a standing rule.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and
python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "USENIX NSDI '27",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 12, "source": "https://www.usenix.org/conference/nsdi27/call-for-papers", "note": "NSDI '27 (both cycles): 12 pages including footnotes, figures and tables, for submissions and final papers; references and appendices extra"},
    "page_limit_includes_references": {"value": false, "source": "https://www.usenix.org/conference/nsdi27/call-for-papers"},
    "review_mode": {"value": "double-blind", "source": "https://www.usenix.org/conference/nsdi27/call-for-papers", "note": "operational-systems track may keep company and system names and links but not author names"},
    "separate_upload_statements": {"value": ["ai_use_disclosure", "ethics_approval"], "source": "https://www.usenix.org/conference/nsdi27/call-for-papers", "note": "HotCRP attestation that all text is primarily human written, and an attestation of compliance with institutional ethical standards, both made in the submission process, not in the PDF"},
    "template": {"value": "USENIX two-column, 10-point Times-Roman or similar on 12-point leading, 7 x 9 inch text block, 8.5 x 11 inch paper, numbered pages; non-conforming papers rejected without review", "source": "https://www.usenix.org/conference/nsdi27/call-for-papers"},
    "portal": {"value": "per-deadline HotCRP sites (nsdi27spring / nsdi27fall .usenix.hotcrp.com); both NSDI '27 gates closed; NSDI '28 CFP not yet published on 2026-11-24", "source": "https://nsdi27fall.usenix.hotcrp.com/deadlines"},
    "supplement_policy": {"value": "appendices after the references allowed; paper must stand alone and reviewers are not required to read them; online content critical to the paper goes in the form's auxiliary material", "source": "https://www.usenix.org/conference/nsdi27/call-for-papers"},
    "preprint_policy": {"value": "technical reports such as arXiv allowed only with a different title and system name in the submission", "source": "https://www.usenix.org/conference/nsdi27/call-for-papers"},
    "llm_policy": {"value": "no papers produced entirely or substantively by generative AI (an AI-written section is a violation); attest in HotCRP that text is primarily human written; AI for grammar and clarity encouraged", "source": "https://www.usenix.org/conference/nsdi27/call-for-papers"},
    "data_code_policy": {"value": "optional post-acceptance artifact evaluation with three badges (Available, Functional, Results Reproduced); Community Award for public code/data by the final paper deadline", "source": "https://www.usenix.org/conference/nsdi27/call-for-artifacts"},
    "submission_fee": {"value": null, "note": "no submission fee or APC stated on the official pages as of 2026-11-24; at least one author per accepted paper registers at full price"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```
