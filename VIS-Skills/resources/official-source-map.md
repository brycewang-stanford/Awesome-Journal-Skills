# Official Source Map - IEEE VIS

Access date: 2026-07-09 (first build). Submission rules, review process, template, committees and
edition status **re-verified 2026-11-24** against the live ieeevis.org and tc.computer.org pages.

**Edition status, checked 2026-11-24.** The latest published edition is **IEEE VIS 2026**, held in
**Boston, Massachusetts, USA, 9-13 November 2026** (official welcome page); it has now met. The next
edition, **IEEE VIS 2027**, is announced for **Chicago, Illinois, USA** (the ieeevis.org "Upcoming
Years" list and the VSC Town Hall 2026 slides, which also list 2028 Seoul), but no 2027 dates,
Call for Full Papers, page budget or chairs are published: `ieeevis.org/year/2027/...` URLs return
404 and `ieeevis.org` still redirects to the 2026 site. The VSC Town Hall 2026 slides say tentative
**author guidelines for AI use** and an optional **author-contribution-statement pilot** are planned
for 2027, both "pending additional review and community feedback". Until the IEEE VIS 2027 call
appears, this pack keeps the IEEE VIS 2026 rules as the latest published edition, and the
machine-readable block below is labelled as VIS 2026.

This map records the official and cross-check sources for the IEEE VIS-specific facts in this
pack. IEEE VIS is the IEEE Visualization Conference; since 2021 its formerly separate SciVis,
InfoVis, and VAST tracks are unified into a single conference, and its **full papers are published
journal-integrated as articles in IEEE TVCG (Transactions on Visualization and Computer
Graphics)**. Its calendar, page budget, area model, and two-phase review mechanics are decided per
edition. Reopen the current-cycle Call for Full Papers, the Paper Submission Guidelines, the Review
Instructions, and the Area Model page before giving submission-ready advice.

## Access method note

On 2026-07-09 direct fetches of `ieeevis.org`, `ieeexplore.ieee.org`, and `precisionconference.com`
returned **HTTP 403 Forbidden** from the verification gateway, and official pages were then read
through **search-engine renderings of the exact URLs**, cross-checked against the official
`@ieeevis` announcements, the IEEE VIS Wikipedia entry, dblp and IEEE Xplore/TVCG tables of
contents. On **2026-11-24** `ieeevis.org`, `tc.computer.org`, `new.precisionconference.com`,
`replicabilitystamp.org` and GitHub were all fetched **directly** (plain `curl`, HTTP 200), so every
ieeevis.org fact below was re-read from the live page itself. The IEEE Author Center policy page
linked from the generative-AI section still returns 403; the AI-disclosure rule below is taken from
the VIS Paper Submission Guidelines' own restatement of it. Beware a scope collision: IEEE VIS is
**not** IEEE VR and **not** ISMAR — those are sibling VGTC conferences on the same PCS society but
with separate calls; no fact here derives from them.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://ieeevis.org/year/2026/info/call-participation/call-for-participation/ | IEEE VIS 2026 Call for Full Papers: TVCG special issue indexed in IEEE Xplore; six areas; all deadlines 23:59 AoE — abstract (mandatory) 21 March 2026, paper 31 March 2026, supplemental 7 April 2026, first-round notification 6 June 2026, second-cycle paper 1 July 2026, final notification 15 July 2026, camera-ready 8 August 2026; conditional accept then full second review cycle; links the VGTC journal template | 2026-11-24 |
| 2 | https://ieeevis.org/year/2026/info/call-participation/paper-submission-guidelines/ | PCS selection (VGTC → VIS 2026 → VIS 2026 Full Papers); strict 9+2 pages (9 pages of content plus up to 2 pages of references, supplemental links, figure credits, acknowledgements; 11 total; more needs TVCG approval); appendices allowed after page 11 in the main upload; 300 MB per file; author-optional double-blind (first cycle only; second round single-blind); author list final at the abstract deadline; keywords chosen in PCS; IEEE generative-AI disclosure rule; IRB/consent statement expectation for human-participant work; DOIs in references; 1-3 suggested external reviewers; opt-in OSF review publishing | 2026-11-24 |
| 3 | https://ieeevis.org/year/2026/info/call-participation/review-instructions/ | Two-phase (author-optional) double-blind review; primary/secondary PC reviewers; one external reviewer invited by the secondary; optional junior reviewer invited by the primary | 2026-11-24 |
| 4 | https://ieeevis.org/year/2026/info/call-participation/area-model/ | The six-area VIS model and Area Paper Chair / Overall Paper Chair structure | 2026-11-24 |
| 5 | https://ieeevis.org/year/2026/blog/2026-02-03-vis-2026-OPC-blog | VIS 2026 OPCs (Melanie Tory, Alex Endert, Tobias Isenberg); appendices may sit inside the main paper upload and do not count toward the 11-page limit; optional suggestion of up to three external reviewers; reviewer-training programme renamed from **student** to **junior** reviewers. Anonymized reviews are published **opt-in to an OSF repository**, not archived in IEEE Xplore, and need consent from the authors *and every reviewer* (source 2) | 2026-11-24 |
| 6 | https://ieeevis.org/year/2026/info/call-participation/shortpapers/ | VIS 2026 Short Papers: up to 4 pages plus up to 1 page of references, VGTC conference two-column format; author-optional double-blind; PCS track "VIS 2026 Short Papers"; submission 30 April 2026 (no abstract deadline), notification 17 June 2026, camera-ready 1 July 2026; published in the conference proceedings in IEEE Xplore with a DOI, **not** TVCG | 2026-11-24 |
| 7 | https://ieeevis.org/year/2026/info/open-practices/open-practices/ | Open Practices for accepted papers: one requirement (Plan S compliance) and two recommendations (open-access preprint; supplemental material in a long-term archive such as OSF), collected at camera-ready | 2026-11-24 |
| 8 | https://www.replicabilitystamp.org/ | Graphics Replicability Stamp Initiative (GRSI); TVCG Replicability Stamp for verified reproducible code/data | 2026-11-24 |
| 9 | https://tc.computer.org/vgtc/publications/journal/ | VGTC journal templates for special-issue TVCG papers incl. VIS full papers: LaTeX (github.com/ieeevgtc/tvcg-journal-latex, updated June 2026), Word (December 2022), Typst (March 2026); short papers use https://tc.computer.org/vgtc/publications/conference/. The previously cited `github.com/ieee-vgtc/vis-latex-submission-template` was archived on 3 March 2026 and now points here | 2026-11-24 |
| 10 | https://en.wikipedia.org/wiki/IEEE_Visualization + https://ieeevis.org/year/2020/blog/things-are-changing-2021 | History: 2021 unification of SciVis/InfoVis/VAST into a single IEEE VIS; TVCG publication lineage | 2026-07-09 |
| 11 | https://ieeevis.org/year/2026/info/history/test-of-time-awards/ | IEEE VIS Test-of-Time Award lineage used to verify exemplar papers | 2026-07-09 |
| 12 | https://ieeevis.org/year/2026/welcome | VIS 2026 in Boston, 9-13 November 2026; General Chairs; "Upcoming Years" list: 2027 Chicago, 2028 Seoul, 2029 Knoxville, 2030 Salt Lake City, 2031 Atlanta | 2026-11-24 |
| 13 | https://ieeevis.org/year/2026/info/committees/conference-committee | VIS 2026 Overall Paper Chairs and the Area Paper Chair roster for all six areas; Short Paper Chairs | 2026-11-24 |
| 14 | https://ieeevis.org/year/2026/assets/VSC_Townhall_2026.pdf | VSC Town Hall 2026: next conferences 2027 Chicago and 2028 Seoul; tentative 2027 author guidelines for AI use and optional author-contribution-statement pilot (pending) | 2026-11-24 |
| 15 | https://new.precisionconference.com/vgtc | PCS VGTC submission portal (reachable) | 2026-11-24 |

## Verified 2026-cycle facts used in skills

- **IEEE VIS 2026** was held in **Boston, Massachusetts, USA**, **9-13 November 2026** (source 12;
  the day span is now confirmed on the official welcome page). It is the unified IEEE Visualization
  Conference (the "VIS" / "Visualization and Visual Analytics" branding).
- **Full-paper calendar (2026, all 23:59 AoE):** abstract deadline **21 March 2026** (mandatory),
  full-paper (PDF) deadline **31 March 2026**, supplemental-material deadline **7 April 2026**,
  first-round notification **6 June 2026**, second-cycle paper submission **1 July 2026**, final
  notification **15 July 2026**, camera-ready **8 August 2026** (source 1). *Corrected 2026-11-24:*
  this line used to give 15 July 2026 as the first-round notification; the call lists 15 July as the
  **final** notification. The **author list must be final by the abstract deadline**; title,
  abstract, and main PDF are locked after the paper deadline (minor title/abstract edits are allowed
  during review when reviewers request them).
- **Publication venue is IEEE TVCG.** Accepted VIS full papers appear in a **special issue of IEEE
  Transactions on Visualization and Computer Graphics**, indexed in IEEE Xplore, and are presented
  at the conference — the journal-integrated model (sources 1, 10).
- **Submission runs through PCS (Precision Conference System)** under the **VGTC** society. In PCS
  the author selects society **VGTC**, conference **VIS 2026**, track **VIS 2026 Full Papers**, then
  one of the six areas and the VIS paper keywords (sources 2, 15).
- **Review is two-phase and author-optional double-blind**, following the IEEE TVCG process.
  Authors may anonymize (recommended whenever possible) or submit single-blind; reviewers stay
  anonymous. Double-blind applies only to the first cycle — the second-round revision is
  single-blind. Each paper is reviewed by **at least three reviewers** — a **primary** and
  **secondary** (both program committee members) plus **one external** reviewer invited by the
  secondary; since VIS 2025 the primary may add an optional **junior reviewer** (named "student
  reviewer" until 2026) in an advisory role. New in 2026, authors may suggest 1-3 external
  reviewers (sources 2, 3, 5).
- **Conditional accept + second round:** first-round decisions are usually conditional acceptances
  or rejections; conditionally accepted papers carry written requirements and go through a **full
  revision-and-review cycle**; only papers that meet them are accepted after the second round.
  Reviews can be published only on an **opt-in** basis, to an **OSF** repository, when the authors
  and every reviewer consent (sources 2, 3, 5).
- **The six-area model (since 2021):** (1) Theoretical & Empirical; (2) Applications; (3) Systems &
  Rendering; (4) Representations & Interaction; (5) Data Transformations; (6) Analytics & Decisions.
  Each area has **Area Paper Chairs**; **Overall Paper Chairs** ensure cross-area consistency
  (source 4). VIS 2026 OPCs: Melanie Tory, Tobias Isenberg, Alex Endert; the APC roster for all six
  areas is on the conference-committee page (source 13).
- **Template and page budget:** the **IEEE VGTC journal (TVCG special-issue)** template (source 9).
  A full paper runs **up to 9 pages of content plus up to 2 pages** containing only references,
  links to supplemental material, figure credits and acknowledgements (the "9+2" budget, **11 pages**
  total); more reference pages need a justification and TVCG approval. Content beyond 9 pages may be
  desk rejected. Appendices may follow page 11 in the main upload without counting. Each submitted
  file is limited to **300 MB** (source 2).
- **Short papers:** up to **4 pages plus 1 page of references** in the **VGTC conference**
  two-column format, author-optional double-blind, submitted 30 April 2026, published in the
  conference proceedings in IEEE Xplore — **not** in TVCG (source 6).
- **Generative AI (2026):** the guidelines restate the IEEE policy — AI-generated content (text,
  figures, images, code) must be disclosed, naming the AI system and the sections that use it with a
  brief explanation of the level of use; AI used only for editing and grammar is generally outside
  the policy, disclosure optional (source 2).
- **Human participants:** papers reporting human-participant research are expected to state IRB /
  ethics approval or exemption and, where applicable, informed consent (anonymizable at submission);
  missing statements are not a desk-reject ground but are checked on accepted papers (source 2).
- **Reproducibility culture:** the **Graphics Replicability Stamp Initiative (GRSI)** issues the
  **TVCG Replicability Stamp** for independently verified reproducible code/data, and the **Open
  Practices Committee** collects the Plan S requirement plus preprint and open-supplemental-material
  recommendations at camera-ready (sources 7, 8).

## The journal-integrated model (honest reading)

The unification that took effect at **VIS 2021** merged the historically separate SciVis, InfoVis,
and VAST conferences (VIS 2020 was the last three-conference year) into a single IEEE VIS with the
six-area model and one consolidated full-paper review process (source 10). Full papers are TVCG
articles — the venue is simultaneously a conference and a journal issue. This is why the review
carries a genuine **conditional-accept revision round** rather than a single accept/reject: the bar
is a journal bar. Whether a given year keeps the exact area boundaries, the reviewer-count rule, or
the supplemental timing is decided per edition — **verify on the current call before advising**.

## No editor-in-chief for the conference; the journal side differs

The **conference** has no standing editor-in-chief; the rotating analogue is the per-edition VIS
Executive Committee, Overall Paper Chairs, and Area Paper Chairs. TVCG (the **journal**) has its own
editorial board and Editor-in-Chief, but VIS full papers enter through the **conference call**, not
a standalone TVCG submission. Do not conflate the two intake paths.

## Still cycle-volatile (verify every year)

- All dates and AoE cutoffs; the abstract/paper/supplemental split and the second-round timeline.
- Exact page budget and which VGTC/TVCG template revision is required (2026 posts 9+2).
- Whether double-blind is optional or mandatory that year, and the exact anonymization guidance.
- Area-model boundaries and the count/roles of reviewers (primary/secondary/external/junior).
- Short-paper length and cycle (2026: 4+1 pages, IEEE Xplore proceedings, not TVCG).
- Open-Practices requirements and the generative-AI disclosure rule (2026: IEEE policy; 2027
  guidelines announced as tentative).

## 待核实 / UNVERIFIED

- **IEEE VIS 2027** dates, Call for Full Papers, page budget, chairs and AI-use / author-contribution
  rules: not published as of 2026-11-24 (`ieeevis.org/year/2027/...` returns 404; the site still
  serves 2026). Third-party event listings give 7-12 November 2027, but no official page states it,
  so the pack does not use it.
- Preregistration / registered-report options: the 2026 Open Practices page does not mention
  preregistration among its requirement and recommendations; whether VIS offers a registered-report
  route was not found on the official pages read on 2026-11-24.

Resolved on 2026-11-24 (removed from this list): the IEEE VIS 2026 day span (9-13 November, source
12); the short-paper length, cycle and publication venue (source 6); the 2026 generative-AI
disclosure policy (source 2); the Overall/Area Paper Chair roster (source 13).

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and
python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "IEEE VIS 2026",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 9, "source": "https://ieeevis.org/year/2026/info/call-participation/paper-submission-guidelines/", "note": "IEEE VIS 2026 full papers (latest published edition; VIS 2027 call not yet out): 9 pages of content plus up to 2 pages of references, supplemental links, figure credits and acknowledgements (11 total); appendices after page 11 not counted"},
    "page_limit_includes_references": {"value": false, "source": "https://ieeevis.org/year/2026/info/call-participation/paper-submission-guidelines/", "note": "references go on the optional pages 10-11; more than 2 reference pages needs TVCG approval"},
    "review_mode": {"value": "single-blind", "source": "https://ieeevis.org/year/2026/info/call-participation/paper-submission-guidelines/", "note": "author-optional: authors may anonymize (double-blind, recommended whenever possible) or not; reviewers anonymous; second-round revision is single-blind"},
    "conditional_statements": {"value": ["ai_use_disclosure", "ethics_approval", "informed_consent"], "source": "https://ieeevis.org/year/2026/info/call-participation/paper-submission-guidelines/", "note": "AI-generated content must be disclosed (editing/grammar use exempt); human-participant work is expected to state IRB/ethics approval or exemption and informed consent (anonymizable at submission; not a desk-reject ground)"},
    "separate_upload_statements": {"value": ["keywords"], "source": "https://ieeevis.org/year/2026/info/call-participation/paper-submission-guidelines/", "note": "VIS paper keywords are selected in the PCS submission form"},
    "template": {"value": "IEEE VGTC journal (TVCG special-issue) template: LaTeX, Word or Typst", "source": "https://tc.computer.org/vgtc/publications/journal/"},
    "portal": {"value": "PCS (Precision Conference System): VGTC > VIS 2026 > VIS 2026 Full Papers", "source": "https://ieeevis.org/year/2026/info/call-participation/paper-submission-guidelines/"},
    "file_format": {"value": "PDF; each submitted file at most 300 MB", "source": "https://ieeevis.org/year/2026/info/call-participation/paper-submission-guidelines/"},
    "supplement_policy": {"value": "video, code, data and other supplemental material encouraged; editable in PCS until 7 April 2026 (one week after the paper); must not change afterwards; paper must stand alone", "source": "https://ieeevis.org/year/2026/info/call-participation/paper-submission-guidelines/"},
    "llm_policy": {"value": "IEEE policy: disclose AI-generated text, figures, images or code, naming the system and sections; editing/grammar use exempt", "source": "https://ieeevis.org/year/2026/info/call-participation/paper-submission-guidelines/"},
    "preprint_policy": {"value": "non-published preprints (arXiv, OSF, HAL) may be reused without citation; open-access preprint of the accepted paper recommended at camera-ready", "source": "https://ieeevis.org/year/2026/info/call-participation/paper-submission-guidelines/"},
    "data_code_policy": {"value": "code/data encouraged, not required; Open Practices recommend long-term archiving (e.g. OSF) at camera-ready; Plan S compliance required where funders demand it", "source": "https://ieeevis.org/year/2026/info/open-practices/open-practices/"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```
