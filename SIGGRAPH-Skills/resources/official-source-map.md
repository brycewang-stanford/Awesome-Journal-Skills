# Official Source Map - ACM SIGGRAPH Technical Papers

Access date: 2026-07-09 (first build). Submission rules, review model, deadlines, chairs and
next-edition status **re-verified 2026-11-24** against the live `s2026.siggraph.org`,
`s2027.siggraph.org` and `asia.siggraph.org` pages, which were fetched directly this time
(`curl`, HTTP 200). `dl.acm.org` still answers HTTP 403 to automated fetches and
`www.siggraph.org/preparing-your-content/author-instructions/` answers HTTP 307 (bot check), so
sources 5-7 keep their 2026-07-09 search-engine reading; the facts they carried that matter for
submission (acmart ≥ 2.16, TOG issue placement) are restated on the 2026 call itself.

**Edition status, checked 2026-11-24.** The latest edition with a complete, published Technical
Papers call is **SIGGRAPH 2026** (53rd conference, Los Angeles, 19-23 July 2026 — already met);
its sister call **SIGGRAPH Asia 2026** (Kuala Lumpur, KLCC, 1-4 December 2026) uses the same
rules and meets next week, with its submission window long closed. The next submission target
is **SIGGRAPH 2027** — **Anaheim Convention Center, 8-12 August 2027** (exhibition 10-12 August).
Its Technical Papers page already lists deadlines of **21 January 2027** (submission form &
conflicts), **28 January 2027** (paper) and **29 January 2027** (upload), all 22:00 UTC, and names
**Tamy Boubekeur** (Adobe Research) as Technical Papers Chair, but its body still reads
"Submission details coming soon" and the 2027 home page still shows those three deadlines as
"To Be Announced". So the full SIGGRAPH 2027 call (page limits, review model, AI wording) is
**not yet published**; the rules below and the block at the end are the SIGGRAPH 2026 call's,
labelled as such. **SIGGRAPH Asia 2027** is announced for **Tokyo International Forum, 30
November - 3 December 2027** (Conference Chair Takahito Tejima); no Technical Papers call yet.

This map records the official and cross-check sources for the SIGGRAPH-specific facts used in
this pack. SIGGRAPH is the ACM SIGGRAPH annual conference; its **Technical Papers** program is
**journal-integrated** — accepted research is published as a special issue of **ACM Transactions
on Graphics (TOG)** (the SIGGRAPH North America issue and, for the sister conference, the
SIGGRAPH Asia issue). Calendar, page budget, and review mechanics are re-decided per edition and
run on **two cycles a year** (SIGGRAPH North America, deadline ~January; SIGGRAPH Asia, deadline
~May). Reopen the current-cycle technical-papers call, the submissions FAQ, the TOG author
guidelines, and the reviewer-instructions page before giving submission-ready advice.

## Access method note

On 2026-07-09, direct fetches of `s2026.siggraph.org`, `asia.siggraph.org`, and `dl.acm.org` were
blocked (CONNECT returned HTTP 403 / 405 from the build-sandbox proxy), so that pass read the
official pages through **WebSearch renderings of the exact official URLs** cross-checked across
≥2 independent surfaces. On **2026-11-24** the `siggraph.org` conference sites (sources 1-4, 11-16)
were fetched directly and read in full; `dl.acm.org` (sources 5-6) still returns HTTP 403 and the
ACM SIGGRAPH author-instructions page (source 7) a 307 bot check, so those rows remain on the
earlier search-rendering reading. Facts that could not be pinned to a primary rendering are
labeled **待核实**. NEVER carry a previous cycle's dates or budget forward without reopening the
live call.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://s2026.siggraph.org/program/technical-papers/ | SIGGRAPH 2026 Technical Papers call: two integrated tracks (Journal = ACM TOG; Conference = SIGGRAPH Conference Proceedings); dual-track papers ≤ 7 pages excluding references and at most 2 figures-only pages, Journal-only no maximum; review "double-blind", four full reviews; `\documentclass[acmtog,anonymous,review]{acmart}`, acmart ≥ 2.16, Adobe PDF only; supplemental > 500 MB not guaranteed to be viewed; companion video ≤ 5 minutes; generative-AI disclosure; rebuttal ≤ 1,000 words plain text; ACM Open APC USD 250 (ACM/SIG member) / 350 (non-member) for 2026; Chair Mirela Ben-Chen, Assistant Chair Justin Solomon; timeline 15 / 22 / 23 Jan 2026 | 2026-11-24 |
| 2 | https://s2026.siggraph.org/technical-papers-submissions-faq/ | SIGGRAPH 2026 Technical Papers FAQ: MD5-checksum option, Linklings portal, deadlines 22:00 UTC/GMT | 2026-11-24 |
| 3 | https://s2026.siggraph.org/technical-papers-reviewer-instructions-ethics/ | SIGGRAPH 2026 single 6-point score scale (Strong Reject ... Strong Accept) used for Journal and dual-track papers; committee assigns the track for dual-track papers | 2026-11-24 |
| 4 | https://asia.siggraph.org/2026/submissions/technical-papers/ | SIGGRAPH Asia 2026: KLCC, Kuala Lumpur, 1-4 Dec 2026; submission form 5 May 2026, paper 12 May 2026, upload 13 May 2026 (23:59 AoE); same two tracks, 7-page dual-track cap, double-blind four reviews; Chair Ravi Ramamoorthi, Assistant Chair Huamin Wang; in-person presentation | 2026-11-24 |
| 5 | https://dl.acm.org/journal/tog | ACM Transactions on Graphics journal home; SIGGRAPH/SIGGRAPH Asia proceedings appear as TOG issues (SIGGRAPH 2026 = Vol. 45, Issue 4, also stated in source 1's timeline) | 2026-07-09 (HTTP 403 on 2026-11-24) |
| 6 | https://dl.acm.org/journal/tog/author-guidelines | ACM TOG author guidelines; rolling direct-to-TOG submissions via ScholarOne outside the conference cycle; acmart preparation | 2026-07-09 (HTTP 403 on 2026-11-24) |
| 7 | https://www.siggraph.org/preparing-your-content/author-instructions/ | ACM SIGGRAPH author instructions: acmart class (require v2.16 or higher), representative image, supplemental materials | 2026-07-09 (HTTP 307 on 2026-11-24) |
| 8 | https://www.replicabilitystamp.org/ | Graphics Replicability Stamp Initiative (GRSI), since 2016; volunteers verify code replicates a paper's results; Software Heritage archiving since 2023 | 2026-07-09 (reachable 2026-11-24) |
| 9 | https://replicability.graphics/ | Code Replicability in Computer Graphics (CRCG); since July 2020 checks whether SIGGRAPH papers' results are replicable | 2026-07-09 (reachable 2026-11-24) |
| 10 | https://blog.siggraph.org/2025/06/siggraph-2025-technical-papers-awards-best-papers-honorable-mentions-and-test-of-time.html/ | SIGGRAPH Technical Papers Awards: Best Papers, Honorable Mentions, Test-of-Time; SIGGRAPH 2025 submission/acceptance figures | 2026-07-09 |
| 11 | https://s2026.siggraph.org/anonymity-policy/ | SIGGRAPH Technical Papers Anonymity Policy ("doubly anonymous review"): review period starts two weeks before the deadline (8 Jan 2026 for SIGGRAPH 2026); arXiv/tech-report preprints allowed if they do not say "under review at SIGGRAPH" or use the ACM TOG/conference format; anonymous code repos allowed; direct anonymity breaks lead to desk rejection | 2026-11-24 |
| 12 | https://s2027.siggraph.org/program/technical-papers/ | SIGGRAPH 2027 Technical Papers page: deadlines 21 Jan 2027 (submission form & conflicts), 28 Jan 2027 (paper), 29 Jan 2027 (upload), 22:00 UTC; "Submission details coming soon" | 2026-11-24 |
| 13 | https://s2027.siggraph.org/general-conference-information/ | SIGGRAPH 2027: Anaheim Convention Center; conference 8-12 Aug 2027, exhibition 10-12 Aug 2027 | 2026-11-24 |
| 14 | https://s2027.siggraph.org/siggraph-2027-committee/ | SIGGRAPH 2027 Technical Papers Chair: Tamy Boubekeur (Adobe Research) | 2026-11-24 |
| 15 | https://s2027.siggraph.org/submissions-faq/ | SIGGRAPH 2027 general submissions FAQ: Technical Papers are prepared anonymously (other programs single blind); Linklings portal; MD5 checksum mechanism; representative image ≥ 1,500 x 1,000 px, landscape | 2026-11-24 |
| 16 | https://asia.siggraph.org/2026/about-the-event/siggraph-asia-2027/ | SIGGRAPH Asia 2027: Tokyo International Forum, 30 Nov - 3 Dec 2027; Conference Chair Takahito Tejima | 2026-11-24 |

## Verified facts used in skills (SIGGRAPH 2026 call, re-read 2026-11-24)

- **SIGGRAPH 2026 is the 53rd ACM SIGGRAPH annual conference**, held at the **Los Angeles
  Convention Center, 19-23 July 2026** (source 1). It has met; its Technical Papers were published
  on 3 July 2026 as **TOG Volume 45, Issue 4** (source 1 timeline).
- **SIGGRAPH 2026 Technical Papers calendar (all 22:00 UTC/GMT):** submission-form deadline
  **15 January 2026** (title, abstract, topic areas, complete co-author list; authors locked after
  this; no new submissions after it); **paper deadline 22 January 2026** (paper PDF or MD5 checksum,
  representative image, supplemental materials); **upload and conflicts deadline 23 January 2026**
  (files matching MD5 checksums; every co-author's conflicts and expertise keywords — a paper with
  no conflicts entered is automatically rejected). Reviews released **5 March 2026**, rebuttals due
  **12 March 2026**, decisions **30 March 2026**, revised paper **29 April 2026**, final version
  **6 May 2026** (source 1).
- **Review is double-blind.** "The SIGGRAPH review process is double-blind": committee members and
  external reviewers do not know the authors, and authors do not know the reviewers. Every paper
  gets **four full reviews** (secondary + three or more tertiary reviewers), with a primary
  moderating. Submissions are anonymized with `\documentclass[acmtog,anonymous,review]{acmart}`
  plus `\acmSubmissionID{paper ID}`; acknowledgements are omitted until acceptance; video narration
  should not use a recognisable author voice; PDF metadata must be clean. Own published work is
  cited in the third person; overlapping work under review elsewhere is cited anonymously and
  uploaded as anonymous supplemental; a public arXiv version of the same paper is **not** cited
  but listed in the form's hidden "Prepublication" field (sources 1, 11).
- **Anonymity policy (source 11):** from two weeks before the deadline until the decision, do not
  list the submission or its preprint on personal/project pages, publicise it through PR, talks or
  social media, or create identifying public code repos. Posting to arXiv or a tech report **is
  allowed**, provided it does not say it is under review at SIGGRAPH, does not carry the submission
  ID, and does not use the ACM TOG/conference format. Direct anonymity breaks in the paper,
  supplemental or code link are desk-rejected.
- **The rebuttal is ≤ 1,000 words of plain text** — self-contained, no URLs to additional material,
  addressing factual errors and specific reviewer questions, not new results; it must preserve
  anonymity (source 1).
- **Two integrated tracks:** *Journal* (ACM Transactions on Graphics) and *Conference* (SIGGRAPH
  Conference Proceedings in the ACM DL). Submissions are either **dual-track** or **Journal only**.
  All submissions are reviewed on **one single scale** — Strong Reject, Reject, Borderline Reject,
  Borderline Accept, Accept, Strong Accept. The committee assigns the track for dual-track papers,
  being less demanding about formal completeness and validation when accepting to the
  **Conference** track (sources 1, 3).
- **Conditional acceptance + second stage:** the full Technical Papers Committee finalizes
  conditional acceptance or rejection; conditionally accepted papers undergo a **second reviewing
  process** in which a committee member (the shepherd) verifies the final version (source 1).
- **Format and length:** ACM double-column format via the **acmtog** template of the **acmart**
  class, **version 2.16 or higher required**; all pages numbered and carrying the paper ID; TAPS-
  approved LaTeX packages only; **Adobe PDF is the only allowed paper format**. **Journal-only**
  submissions have **no maximum or minimum length** (typical 8-12 pages without references).
  **Dual-track** submissions must be **no longer than 7 pages excluding references and
  figures-only pages**, with **at most two figures-only pages** (figures and captions only, no
  tables) after the references; references are unlimited; appendices go only in supplemental.
  Conference-track camera-ready may reach **10 pages plus references** after folding in the
  figures-only pages (plus one page for author list/acknowledgements) (source 1).
- **Supplemental materials** are optional, anonymized, and uploaded in two parts — (A) material
  committed to the ACM DL and (B) review-only material (e.g., anonymized overlapping papers and an
  anonymous cover letter). Videos MP4, images JPG/PNG; a companion video is **five minutes or
  less**; more than **500 MB** of supplemental is not guaranteed to be viewed. Code/data are
  preferred inside the supplemental; an external repo link is allowed only if fully anonymized with
  a verifiable pre-deadline timestamp (source 1). Every submission includes a **representative
  image** (source 15).
- **Generative AI / LLMs:** the ACM Policy on Authorship applies; authors must **disclose any use
  of generative AI tools that generate new content** (beyond grammar correction) and are
  responsible for inaccuracies; papers citing non-existent material are rejected, possibly without
  review (source 1).
- **Submission system is Linklings** (`ssl.linklings.net/conferences/siggraph/`; SIGGRAPH Asia
  uses `.../siggraphasia`) (sources 1, 2, 4).
- **Open access and APCs:** ACM moved to full open access on 1 January 2026. Corresponding authors
  at ACM Open institutions pay nothing; others pay an APC, which for 2026 conferences is subsidised
  to **USD 250 for ACM/SIG members and USD 350 for non-members** (source 1). The 2027 rate is not yet
  posted.
- **Chairs:** SIGGRAPH 2026 Technical Papers Chair **Mirela Ben-Chen**, Assistant Chair **Justin
  Solomon** (source 1); SIGGRAPH Asia 2026 Chair **Ravi Ramamoorthi**, Assistant Chair **Huamin
  Wang** (source 4); SIGGRAPH 2027 Technical Papers Chair **Tamy Boubekeur** (source 14).
- **SIGGRAPH Asia 2026** is held at **KLCC, Kuala Lumpur, Malaysia, 1-4 December 2026**; its
  Technical Papers used submission form **5 May 2026**, paper **12 May 2026**, upload **13 May
  2026** (23:59 AoE; all closed), the same two tracks and 7-page dual-track cap, and requires at
  least one author to present in person (source 4).
- **SIGGRAPH 2027** (Anaheim, 8-12 August 2027): Technical Papers deadlines posted as **21 / 28 /
  29 January 2027**, 22:00 UTC; full call pending (sources 12-14).
- **Direct-to-TOG submissions are rolling** through ScholarOne, outside the conference cycle but
  less common; revised or extended versions of conference/workshop papers go to TOG directly
  rather than to SIGGRAPH (sources 1, 6).
- **Reproducibility culture:** the **Graphics Replicability Stamp Initiative (GRSI,
  replicabilitystamp.org, since 2016)** awards a stamp when volunteers verify submitted code
  replicates a paper's results, archiving accepted code via **Software Heritage** (since 2023); the
  related **Code Replicability in Computer Graphics (CRCG, replicability.graphics)** has checked
  SIGGRAPH papers' replicability since July 2020 (sources 8, 9). These are **community-run stamps**,
  not the ACM Artifact Review and Badging scheme used at SIGSOFT/systems venues.
- **Awards:** Best Papers, Honorable Mentions, and a Test-of-Time award are given each year
  (source 10).

## Reported facts (secondary renderings; labeled as such)

- **SIGGRAPH 2026 received more than 1,120 Technical Papers submissions** (ACM SIGGRAPH press
  release / blog rendering); the exact accept count for 2026 is **待核实**. The 2026 call itself
  says only that the acceptance rate "has remained stable in the range of ~20-30%" with no quota.
- **SIGGRAPH 2025** received **more than 970** submissions and accepted **132 Journal + 174
  Conference = 306** papers (~31.5%) (source 10 rendering). Treat as a prior-cycle reference point,
  not a quota — SIGGRAPH sets no fixed acceptance target.

## The journal-integrated model (honest reading)

SIGGRAPH's defining trait among CS venues is that its Technical Papers **are** ACM TOG journal
articles: acceptance yields a TOG DOI and issue placement, not merely conference proceedings. The
single-round review nonetheless resembles a conference — one deadline, external referees, a short
**rebuttal**, then a **Technical Papers Committee meeting** — but folds in a journal-grade
**conditional-accept / second-stage revision** so the published article meets TOG's standard. The
**dual-track** choice (Journal vs Conference publication) is decided by the committee at accept
time, and a "Conference-track" accept is a genuine, lighter-validation path for earlier-stage
work, published in the SIGGRAPH Conference Proceedings rather than the TOG issue. Verify per cycle
whether both tracks are offered and how the track boundary is drawn.

## No editor-in-chief role in the conference; rotating committee

The SIGGRAPH Technical Papers process is run by a per-edition **Technical Papers Chair**, an
Assistant Chair, an Advisory Board and a **Technical Papers Committee** of about 100 people (with
external tertiary reviewers), not a standing journal editor-in-chief — even though the output is a
journal. ACM TOG itself has an Editor-in-Chief for the rolling direct-submission stream; do not
conflate the two paths. At least one author presents in person (2026 introduced a deferral option
for verifiable travel barriers).

## Still cycle-volatile (verify every year)

- Both cycles' exact dates and UTC/AoE cutoffs (SIGGRAPH uses 22:00 UTC; SIGGRAPH Asia 2026 used
  23:59 AoE). SIGGRAPH 2027 deadlines are posted but its full call is not (checked 2026-11-24).
- The page budget and which acmart revision is required (2026: acmart ≥ 2.16; dual-track ≤ 7 pages).
- Rebuttal length/format (2026: ≤ 1,000 words, plain text) and the score scale wording.
- Dual-track vs Journal-only options and the conditional-accept / second-stage mechanics.
- The anonymity-policy embargo window (2026: from two weeks before the deadline).
- The APC level after the 2026 subsidy.
- Exact SIGGRAPH 2026 acceptance count (**待核实**).

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and
python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "SIGGRAPH Technical Papers (SIGGRAPH 2026 call)",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 7, "source": "https://s2026.siggraph.org/program/technical-papers/", "note": "SIGGRAPH 2026 call (same in SIGGRAPH Asia 2026): applies to dual-track submissions only, excluding references and up to two figures-only pages; Journal-only submissions have no maximum; SIGGRAPH 2027 full call not yet published as of 2026-11-24"},
    "page_limit_includes_references": {"value": false, "source": "https://s2026.siggraph.org/program/technical-papers/"},
    "review_mode": {"value": "double-blind", "source": "https://s2026.siggraph.org/program/technical-papers/", "note": "SIGGRAPH 2026 call; four full reviews per paper"},
    "anonymized_supplement_required": {"value": true, "source": "https://s2026.siggraph.org/program/technical-papers/"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://s2026.siggraph.org/program/technical-papers/", "note": "disclose generative-AI use that generates new content (beyond grammar correction), per the ACM Policy on Authorship"},
    "cover_letter": {"value": "optional", "source": "https://s2026.siggraph.org/program/technical-papers/", "note": "anonymous cover letter in review-only supplemental (part B) for overlapping work or resubmission with reviewer continuity"},
    "template": {"value": "ACM acmart class v2.16 or higher, acmtog double-column: \\documentclass[acmtog,anonymous,review]{acmart} with \\acmSubmissionID; pages numbered with paper ID", "source": "https://s2026.siggraph.org/program/technical-papers/"},
    "file_format": {"value": "paper as Adobe PDF only; videos MP4, images JPG/PNG recommended; supplemental over 500 MB not guaranteed to be viewed", "source": "https://s2026.siggraph.org/program/technical-papers/"},
    "portal": {"value": "Linklings (ssl.linklings.net/conferences/siggraph/)", "source": "https://s2026.siggraph.org/program/technical-papers/"},
    "supplement_policy": {"value": "optional anonymized supplemental in two parts (A: published in ACM DL; B: review-only); companion video five minutes or less; appendices only as supplemental; representative image required", "source": "https://s2026.siggraph.org/program/technical-papers/"},
    "preprint_policy": {"value": "arXiv/tech-report preprints allowed but must not mention SIGGRAPH review, the submission ID, or use ACM TOG/conference format; not cited in the paper but listed in the hidden Prepublication field; no publicity from two weeks before the deadline until decision", "source": "https://s2026.siggraph.org/anonymity-policy/"},
    "llm_policy": {"value": "ACM Policy on Authorship: disclose generative-AI use beyond grammar correction; citations of non-existent material lead to rejection, possibly without review", "source": "https://s2026.siggraph.org/program/technical-papers/"},
    "data_code_policy": {"value": "code and data encouraged as anonymized supplemental; external repo link only if fully anonymized with a verifiable pre-deadline timestamp; community GRSI replicability stamp is separate and voluntary", "source": "https://s2026.siggraph.org/program/technical-papers/"},
    "apc": {"value": "ACM Open: none for ACM Open institutions; otherwise USD 250 (ACM/SIG member) / 350 (non-member) subsidised rate for 2026 conferences", "source": "https://s2026.siggraph.org/program/technical-papers/", "note": "2027 APC not yet posted"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24 (a separate 50-word website summary is requested only after acceptance)"}
  }
}
```
