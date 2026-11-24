# Official Source Map - ACM FAccT

Access date: 2026-11-24 (first compiled 2026-07-09). FAccT 2027 call, Author Guide, Reviewer
Guide, conference home page, FAccT Blog posts and the OpenReview FAccT 2027 group
**re-verified 2026-11-24** against the live pages; FAccT 2026 history rows re-read the same day.

**Edition status, checked 2026-11-24.** The live edition is **FAccT 2027**, the tenth annual ACM
Conference on Fairness, Accountability, and Transparency, **Porto, Portugal, June 21-24, 2027**
(the city is on the facctconference.org home page and in the OpenReview FAccT 2027 group; the
dates are in the 2027 CFP). The FAccT 2027 Call for Papers (page last updated 12 Nov 2026), Author
Guide ("Last Updated: October 2026") and Reviewer Guide ("Last Updated: August 2026") are all
published, so this pack now describes FAccT 2027. FAccT 2027 **moved its deadlines about ten
weeks earlier** than FAccT 2026: abstracts were due **October 27, 2026** and full papers
**November 3, 2026** (11:59 PM AoE). Both deadlines have **already passed** as of this check; the
cycle is in its review period (reviews due 25 Nov 2026). First-round decisions are released
**December 22, 2026**, revisions + rebuttals are due **January 28, 2027**, and final accept/reject
notifications go out **March 23, 2027**; the camera-ready deadline is still **TBD** on the CFP.
FAccT 2027 has no committees page yet (`/2027/committees.html` returns 404), so its General Chairs
are not announced; the 2027 CRAFT, tutorial and Doctoral Colloquium calls are not published.
FAccT 2026 (Montréal, June 25-28, 2026) has met; its facts are kept below as labelled history.

## Access method note

On 2026-11-24 `facctconference.org`, `facct-blog.github.io` and the OpenReview API
(`api2.openreview.net`) were read **directly** with `curl` (HTTP 200) and converted to text. This
replaces the 2026-07-09 access route, when the verification gateway returned **HTTP 403** for
`facctconference.org` and the pages were read through search-engine renderings of the exact URLs.
`dl.acm.org` still returns **HTTP 403**; the FAccT '26 proceedings DOI was therefore confirmed via
the Crossref API record for `10.1145/3805689` (type "proceedings", publisher ACM, published
2026-06-25) rather than the ACM DL page. Facts that conflict between two official surfaces are
flagged in the register below. Naming history: the venue was **FAT\*** in 2018-2020 and was renamed
**FAccT** from 2021 — the dblp key is still `fat`.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://facctconference.org/2027/cfp.html | FAccT 2027 Call for Papers: key dates (abstract Oct 27, 2026; paper Nov 3, 2026; first-round decisions Dec 22, 2026; revision + rebuttal Jan 28, 2027; final notification Mar 23, 2027; camera-ready TBD; conference June 21-24 2027); six focus areas; OpenReview; 14 pages excluding references, +1 endmatter page, 15 pages at Revision/acceptance; anonymity policy (desk rejection without review); Accept / Revise (major or minor) / Reject; archival vs non-archival; ACM TAPS (LaTeX or Word); all authors must sign up to review; in-person presentation with a virtual option; Program Chairs | 2026-11-24 |
| 2 | https://facctconference.org/2027/authorguide.html | FAccT 2027 Author Guide (Last Updated: October 2026): abstract-registration gate and no author-list changes after it; mutual anonymity; desk-rejection grounds; reviewing pipeline with Senior Area Chairs; single-column `\documentclass[manuscript,screen,review,anonymous]{acmart}`; up to 14 pages including figures and tables plus unlimited references; one extra endmatter-only page; appendices allowed, unlimited, same PDF, not counted; ACM Reference Format for archival papers (any style, e.g. Bluebook, for non-archival); Generative AI Usage Statement required at submission; Ethical Considerations statement at submission; identity-revealing endmatter withheld; preprints allowed; concurrent-submission exceptions; 2026 ACM Open APC subsidy ($250 ACM/SIG members, $350 non-members) with any 2027 subsidy not yet announced | 2026-11-24 |
| 3 | https://facctconference.org/2027/rguide.html | FAccT 2027 Reviewer Guide (Last Updated: August 2026): review criteria, typically three reviewers plus one Area Chair, reviewer timeline (reviews due Nov 25, 2026; re-reviews; final calibration), no LLM-written reviews, contemporaneous work = papers released 4 months before the deadline | 2026-11-24 |
| 4 | https://facctconference.org/ | Conference home: "The tenth annual ACM FAccT conference will be held in Porto, Portugal" | 2026-11-24 |
| 5 | https://facct-blog.github.io/2026-06-24/submission-timeline | FAccT Blog, "Update to ACM FAccT Submission Timeline Beginning in 2027" (by the 2027 Program Chairs Denton, Leslie, Tamò-Larrieux, Valera): earlier deadlines, abstract Oct 27, 2026, paper Nov 3, 2026, final notification Mar 23, 2027 | 2026-11-24 |
| 6 | https://facct-blog.github.io/2026-10-15/preparation | FAccT Blog, "Preparing for FAccT 2027": four changes — AI-writing policy moves from prohibition to disclosure, clearer limits on AI in reviewing, Senior Area Chairs, no separate pre-decision rebuttal (rebuttal submitted with the revision); all authors must sign up to review; expected reviewer load 4 to 5 papers | 2026-11-24 |
| 7 | https://openreview.net/group?id=ACM.org/FAccT/2027/Conference | FAccT 2027 OpenReview group (read via `api2.openreview.net/groups?id=ACM.org/FAccT/2027/Conference`): "The Tenth Annual ACM Conference on Fairness, Accountability, and Transparency", location Porto, Portugal, start date 21 June 2027, submissions not public | 2026-11-24 |
| 8 | https://facctconference.org/2026/cfp.html | History: FAccT 2026 CFP — abstract Jan 8, 2026; paper Jan 13, 2026; preliminary reviews Feb 20; rebuttal due Feb 24; notification Mar 2; revision Mar 25; final notification Apr 15, 2026; camera-ready Apr 24 (round 1) / May 11, 2026 (after Revise); Le Centre Sheraton Montréal, June 25-28, 2026 | 2026-11-24 |
| 9 | https://facctconference.org/2026/index.html | History: FAccT 2026, the ninth annual conference, Montréal; "Final Notification for Revise & Resubmit Papers: Wednesday, April 15, 2026" | 2026-11-24 |
| 10 | https://facctconference.org/2026/committees.html | History: FAccT 2026 General Chairs Su Lin Blodgett, Robert Soden, Zee Talat; Program Chairs Michele Gilman, Michael Madaio, Luke Stark, Julia Stoyanovich; CRAFT and tutorial chairs | 2026-11-24 |
| 11 | https://facctconference.org/2026/cfpcraft.html | History: FAccT 2026 CRAFT call — proposals (no more than 4 pages excluding references, any readable layout) via EasyChair, due March 27, 2026, notification (expected) April 15, 2026 | 2026-11-24 |
| 12 | https://facctconference.org/2026/callfordc.html | History: FAccT 2026 Doctoral Colloquium — applications via EasyChair due February 24, 2026, notifications March 23, 2026 | 2026-11-24 |
| 13 | https://facct-blog.github.io/2025-10-16/announce-cfp | History: FAccT 2026 CFP announcement (OpenReview adoption, Generative AI Usage Statement, revise-and-resubmit) | 2026-07-09 |
| 14 | https://facct-blog.github.io/2025-12-17/submit | History: "Submitting to FAccT 2026" (OpenReview mechanics, abstract-registration gate, focus areas) | 2026-07-09 |
| 15 | https://openreview.net/group?id=ACM.org/FAccT/2026/Conference | History: FAccT 2026 OpenReview group | 2026-07-09 |
| 16 | https://dl.acm.org/doi/proceedings/10.1145/3805689 | Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency (FAccT '26); ACM DL returned 403, DOI confirmed through the Crossref API; cross-check dblp `db/conf/fat` | 2026-11-24 |
| 17 | https://facctconference.org/organization.html | Standing organisation: Executive Committee, Strategy and Sponsorship chairs (no editor-in-chief) | 2026-11-24 |

## Verified FAccT 2027 facts used in skills

- **FAccT 2027 is the tenth annual ACM Conference on Fairness, Accountability, and Transparency**,
  **Porto, Portugal**, **June 21-24, 2027** (sources 1, 4, 7). Venue building and registration
  details are not yet published ("Stay tuned for more details!").
- **Research-track calendar (sources 1, 3, 5):** abstract registration **October 27, 2026**; full
  paper **November 3, 2026**; reviewer bidding Oct 29 - Nov 5; reviews due **November 25, 2026**;
  reviews and first-round decisions (Accept / Revise major or minor / Reject) **December 22,
  2026**; revision **and** rebuttal due **January 28, 2027**; re-review Jan 28 - Feb 22, 2027;
  final accept/reject notification **March 23, 2027**; camera-ready **TBD**. All deadlines 11:59 PM
  Anywhere on Earth. (The Reviewer Guide's line "Re-reviews due: February 18th, 2026" is an
  evident year typo for 2027.)
- **No separate pre-decision rebuttal in 2027** (sources 1, 2, 6). FAccT 2026 had a short rebuttal
  (Feb 20-24, 2026) before the first decision; FAccT 2027 drops it. Authors with a Revise (major or
  minor) decision submit the revised paper **together with a rebuttal** explaining how the
  prioritized feedback was addressed, and the original reviewers and AC re-review it.
- **Senior Area Chairs (new for 2027)** sit between ACs and Program Chairs, calibrate decisions
  across AC pools, handle escalations, and join final calibration (sources 2, 3, 6).
- **Submission platform is OpenReview** (`ACM.org/FAccT/2027/Conference`); authors without an
  institutional affiliation were told to create a profile by 10/16/26 (16 October 2026) because
  verification can take weeks (sources 1, 2, 6).
- **Review is mutually anonymous**; non-compliant submissions are rejected without review. Papers
  get typically **three** reviewers and one Area Chair, matched by the author-selected **focus
  areas** (six for 2027: Evaluations and evaluation practices; Experiences and interactions; Law and
  policy; Normative foundations and implications; Power and practice; System development and
  deployment), the abstract, and bidding (sources 1-3).
- **Page budget:** no longer than **14 pages excluding references** (including all figures and
  tables; most papers 12-14), single-column; **one extra page** usable only for endmatter
  statements; **references unlimited**; **appendices allowed, any length**, in the same PDF, not
  counted, and reviewers are not obliged to read them. Papers sent to Revision and accepted papers
  may use **15** content pages, excluding references and endmatter (sources 1, 2).
- **Format:** ACM TAPS workflow, **LaTeX or Microsoft Word** (Overleaf/LaTeX strongly recommended;
  formatting errors lead to desk rejection). LaTeX: start from `sample-sigconf-authordraft.tex`
  with `\documentclass[manuscript,screen,review,anonymous]{acmart}`; the copyright/bottom-page
  block may be removed at initial submission. Archival papers use the **ACM Reference Format**;
  non-archival papers may use any reference style (e.g., Bluebook) (source 2).
- **Generative AI Usage Statement — required at submission, in the anonymized endmatter, even if
  no AI was used**; it does not count toward the page limit, and failure to disclose AI use is
  grounds for desk rejection. **Policy change for 2027:** FAccT 2026 prohibited using LLMs to
  generate manuscript text; FAccT 2027 follows ACM's Policy on Authorship — generative AI may be
  used to create content if disclosed (tool, model version, task, extent of human validation; also
  in a Methods section when AI is core to the work), AI cannot be an author, and even routine
  assistive use (grammar, translation) must be reported in the statement (sources 2, 6).
- **Ethical Considerations statement** (ethical concerns and adverse impacts considered and
  mitigated) "should be included at submission time"; the Endmatter section lists it among the
  statements authors "may include ... if applicable" (source 2). **Withheld until acceptance:**
  Author Contributions, Acknowledgements, Competing Interests, and Positionality (if identifying).
  Endmatter is not for limitations, which belong in the main body.
- **Archival vs non-archival:** archival papers appear in the ACM DL proceedings; non-archival
  papers appear only as abstracts. The choice is made at abstract registration and cannot be
  changed; reviewers are not told which was chosen. A conference-length version of a paper under
  journal review may be submitted only as non-archival (sources 1, 2).
- **Dual submission and preprints:** no papers identical or substantially similar to work under
  review, published, or accepted elsewhere; exceptions for preprints/technical reports (do not cite
  them), non-archival workshop papers, and prior short papers of at most 4 pages; preprints allowed
  under ACM's self-archiving policy (source 2).
- **Reviewer duty:** **all authors of every paper must sign up to review** (not all are selected);
  failing to sign up and follow through can lead to (desk) rejection. Expected load 4 to 5 papers,
  reduced load of 3 possible (sources 1, 6).
- **Attendance:** at least one author of each accepted paper must register, attend and present for
  the paper to appear in the proceedings; in-person is expected, with a virtual-presentation option
  for authors who cannot travel (source 1). Accepted papers also prepare a poster (source 2).
- **Open Access / APCs:** ACM has been 100% Open Access since **1 January 2026** (ACM Open
  institutional model or an APC). For 2026 conferences ACM's temporary subsidy set the APC at
  **$250** for ACM/SIG members and **$350** for non-members; the Author Guide says any 2027 subsidy
  will be announced (source 2). Waivers are rare and follow ACM's discretionary waiver policy.
- **Program Chairs (sources 1, 5):** Remi Denton, David Leslie, Aurelia Tamò-Larrieux, Isabel
  Valera (program-chairs@facctconference.org). See the register below for a conflicting byline.

## FAccT 2026 (history, kept for calibration)

- 9th annual conference, Le Centre Sheraton Montréal, June 25-28, 2026 (sources 8, 9).
- Calendar: abstract Jan 8, 2026; paper Jan 13, 2026; preliminary reviews Feb 20; rebuttal due
  Feb 24; first notification (Accept / Revise / Reject) Mar 2; revision Mar 25; final notification
  for Revise papers **April 15, 2026** (resolved 2026-11-24); camera-ready Apr 24 (round 1) and
  May 11, 2026 (after Revise) (sources 8, 9).
- 2026 introduced OpenReview, the Revise round, and the Generative AI Usage Statement; its AI
  policy prohibited LLM-generated manuscript text (sources 6, 13).
- Committees (source 10, corrects the earlier record): General Chairs **Su Lin Blodgett, Robert
  Soden, Zee Talat**; Program Chairs **Michele Gilman, Michael Madaio, Luke Stark, Julia
  Stoyanovich**.
- CRAFT 2026: proposals via EasyChair, no more than 4 pages excluding references, due March 27,
  2026, notification April 15, 2026 (source 11). Doctoral Colloquium 2026: applications due
  February 24, 2026, notifications March 23, 2026 (source 12).

## What makes FAccT's model distinctive (honest reading)

FAccT is the *interdisciplinary* responsible-AI flagship. Unlike a pure-ML venue (NeurIPS/ICML) or
a pure-HCI venue (CHI), FAccT requires deep engagement with the social components of computational
systems — work on "purely hypothetical concerns" is out of scope — and it convenes a genuinely
mixed reviewer pool of computer scientists, lawyers, social scientists, humanists, and policy
scholars. A rigorous CS method paper **and** a critical/qualitative or legal-analysis paper are
**both in scope**; the review criteria (relevance, quality and clarity, originality, potential for
impact) reward depth of exposition and honest treatment of strengths *and* limitations rather than
a single benchmark number, and reviewers are told not to penalize simple methods or not using the
latest models. The 2026-2027 run of structural changes — OpenReview, the Revise round, the
mandatory Generative AI Usage Statement (2026), then Senior Area Chairs, the merged
revision-plus-rebuttal, the disclosure-based AI policy and the autumn deadline (2027) — means
every process detail is cycle-volatile.

## Naming, lineage, and no editor-in-chief

- The venue was **FAT\*** for 2018-2020 (**FAT\* 2018**, New York — proceedings in **PMLR vol 81**;
  **FAT\* 2019**, Atlanta — first ACM DL proceedings; **FAT\* 2020**, Barcelona) and has been
  **FAccT** since 2021. The dblp key remains `db/conf/fat`.
- Like every venue in this collection, FAccT has **no standing editor-in-chief**; leadership is the
  per-edition General Chairs and Program Chairs, rotating yearly, under a standing Executive
  Committee (source 17). Do not carry a chair's name forward between editions.

## Still cycle-volatile — 待核实 register

- **FAccT 2027 Program Chairs — conflicting official surfaces.** The 2027 CFP and the June 2026
  blog post name Remi Denton, David Leslie, Aurelia Tamò-Larrieux and Isabel Valera; the October
  2026 "Preparing for FAccT 2027" post is signed "2027 Program Chairs (Abigail Jacobs, Joao Gama,
  Pedro H. Abreu, Yacine Jernite)". Checked 2026-11-24; the pack uses the CFP list (**待核实**).
- **FAccT 2027 General Chairs** — not published (no 2027 committees page on 2026-11-24).
- **FAccT 2027 camera-ready deadline** — "TBD" on the CFP.
- **FAccT 2027 CRAFT, tutorials, and Doctoral Colloquium** calls and deadlines — not published.
- **2027 APC subsidy** — the Author Guide says details of any 2027 subsidy will follow.
- **Ethical Considerations statement status** — the Author Guide labels it "Should be included at
  submission time" but also lists it among optional endmatter; this pack treats it as strongly
  expected, not a hard requirement.
- **Abstract length and keyword requirements** — not stated on the 2027 CFP or Author Guide.
- Whether any optional artifact/badging scheme exists — none is described in the 2027 Author Guide.

Resolved on 2026-11-24 (removed from this register): FAccT 2027 dates and host city; the FAccT
2026 final-notification date for Revise papers (April 15, 2026); the 2026 CRAFT and Doctoral
Colloquium deadlines; the page-budget wording (14 + 1 endmatter page, 15 at Revision/acceptance,
excluding references and endmatter); the acmart options; whether FAccT authors pay APCs (ACM Open
or APC, 2026 subsidy $250/$350); the 2026 committee roster; whether 2027 keeps OpenReview, the
Revise decision, and the Generative AI Usage Statement (it keeps all three).

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and
python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "ACM FAccT 2027",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 14, "source": "https://facctconference.org/2027/cfp.html", "note": "FAccT 2027 initial submission, single-column, including figures and tables; references, appendices and one endmatter-only page not counted; 15 pages at the Revision stage and for accepted papers"},
    "page_limit_includes_references": {"value": false, "source": "https://facctconference.org/2027/authorguide.html"},
    "review_mode": {"value": "double-blind", "source": "https://facctconference.org/2027/authorguide.html", "note": "FAccT calls it mutually anonymous review; non-anonymized submissions are rejected without review"},
    "required_statements": {"value": ["ai_use_disclosure"], "source": "https://facctconference.org/2027/authorguide.html", "note": "Generative AI Usage Statement in the anonymized endmatter of every FAccT 2027 submission, even if no AI was used; Ethical Considerations statement expected at submission; Author Contributions, Acknowledgements, Competing Interests and identifying Positionality statements must be withheld until acceptance"},
    "template": {"value": "ACM TAPS workflow; LaTeX acmart \\documentclass[manuscript,screen,review,anonymous]{acmart} (from sample-sigconf-authordraft.tex) or Microsoft Word; single-column", "source": "https://facctconference.org/2027/authorguide.html"},
    "reference_style": {"value": "ACM Reference Format for archival submissions; any style (e.g. Bluebook) for non-archival", "source": "https://facctconference.org/2027/authorguide.html"},
    "portal": {"value": "OpenReview (ACM.org/FAccT/2027/Conference); abstract registration with focus areas required before the paper deadline", "source": "https://facctconference.org/2027/cfp.html"},
    "supplement_policy": {"value": "appendices of any length allowed at the end of the same PDF; not counted; reviewers not obliged to read them", "source": "https://facctconference.org/2027/authorguide.html"},
    "preprint_policy": {"value": "preprints and technical reports allowed but not cited; no concurrent submission of substantially similar work, except non-archival submission of a paper under journal review", "source": "https://facctconference.org/2027/authorguide.html"},
    "llm_policy": {"value": "generative AI may be used if disclosed (tool, model version, task, human validation); routine assistive use must also be reported in the Generative AI Usage Statement; AI cannot be an author; failure to disclose is grounds for desk rejection", "source": "https://facctconference.org/2027/authorguide.html"},
    "apc": {"value": "ACM Open Access: covered by ACM Open institutions, otherwise an APC; 2026 subsidy USD 250 ACM/SIG members / 350 non-members; 2027 subsidy not yet announced", "source": "https://facctconference.org/2027/authorguide.html"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24"},
    "keywords_required": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```
