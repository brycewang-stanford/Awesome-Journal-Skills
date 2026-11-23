# Official Source Map - DAC (Design Automation Conference)

Access date: 2026-07-09 (dead links re-checked 2026-11-23). Moved to the DAC 2027 call and
**re-verified 2026-11-24** against the live `dac.com/2027` pages: the home page, the Call for
Contributions, the Research Manuscript Submissions page (format, rules, AI policy, timeline,
FAQ, TPC chairs), the Engineering Track Presentations page, the Committees page and the
`softconf.com/dac27/research` portal, all fetched directly (HTTP 200).

**Edition status, checked 2026-11-24.** The live edition is **DAC 2027**, the **64th**
Design Automation Conference ("The Chips to Systems Conference"), **July 11-14, 2027 at the
San Jose Convention Center, San Jose, California** (source 1). Its Call for Contributions is
published and says "Submissions are now open" for the Research Track, Engineering Track,
Workshops/Tutorials, DAC Pavilion and Exhibitor Forum (sources 1, 2), so this pack now
describes DAC 2027. The DAC 2027 Research-Manuscript route has **already closed**: abstracts
were due **November 11, 2026** and manuscripts **November 18, 2026** (5:00 pm US Pacific
Time); the cycle is now in review, with accepted IDs posted **February 22, 2027** and
accept/reject notifications on **March 8, 2027** (source 3). The DAC 2027 Engineering Track is
still open until **January 11, 2027** (source 4). DAC 2026 (63rd, Long Beach, July 26-29,
2026) has met; its rows below are kept as labelled history.

This map records the official and cross-check sources used for DAC-specific facts in this
pack. DAC is the ACM/IEEE **Design Automation Conference** — branded since recent editions as
**"The Chips to Systems Conference"** — the premier venue for electronic design automation (EDA)
and chip/system design, sponsored by ACM and IEEE and supported by **ACM SIGDA** and **IEEE CEDA**.
Its dates, page budget, deadlines, template and track structure are decided per edition. Reopen
the current-cycle Call for Contributions and Research Manuscript Submissions page before giving
submission-ready advice.

## Access method note

On 2026-07-09, direct fetches of `dac.com`, `dl.acm.org`, `ieee-ceda.org`, and `softconf.com`
returned or were expected to return **HTTP 403/blocked egress** from the build sandbox, so the
DAC 2026 pages were read through **search-engine renderings of the exact URLs** and cross-checked
against the ACM Digital Library DAC proceedings, dblp, and IEEE CEDA event listings. On
2026-11-24 the `dac.com/2027` pages, the live `dac.com/2026` guidelines page, the
`softconf.com/dac27/research` portal and the Wayback Machine copy of the DAC 2026 FAQ were all
fetched **directly with `curl -sL`** (HTTP 200) and read as text. Facts that could not be pinned
to an official page are labeled **待核实**. Two name-collision guards: (1) **ASP-DAC** (Asia and
South Pacific Design Automation Conference) and **DATE** (Design, Automation and Test in Europe)
are *sibling but distinct* EDA conferences with their own calls and deadlines — no fact here
derives from them; (2) "DAC" also abbreviates *digital-to-analog converter* in circuit papers —
an in-scope research topic, not this conference.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://dac.com/2027 | DAC 2027 (64th, per the site logo) home: July 11-14, 2027, San Jose Convention Center, San Jose, California; "Submissions are now open for the Research Track, Engineering Track, Workshops/Tutorials, DAC Pavilion, and Exhibitor Forum"; sponsored by ACM and IEEE, supported by ACM SIGDA and IEEE CEDA | 2026-11-24 |
| 2 | https://dac.com/2027/authors/call-for-contributions | DAC 2027 Call for Contributions: Research Manuscript Submissions, Research Special Sessions, Research Panels, Tutorials, Workshops, Engineering Track Presentations, Engineering Track Special Sessions, DAC Pavilion, Exhibitor Forum; topics of interest AI, Design, EDA, Security, Systems (no Late Breaking Results or artifact track listed) | 2026-11-24 |
| 3 | https://dac.com/2027/program/research-manuscript-submissions | DAC 2027 Research Manuscripts: two-stage submission (abstract of approximately 100 words + all co-authors by Nov 11, 2026; manuscript by Nov 18, 2026, 5:00 pm US Pacific); up to 6 pages plus 1 references-only page, double-column, 9 or 10-pt, PDF only, **IEEE Templates**; double-blind (no names/affiliations, third-person self-citation, no "omitted for blind review", author-free PDF metadata); at most 20 manuscripts per author; TPC COI declaration; disclosure of related unpublished work; arXiv allowed; AI-content disclosure section; LLM review-support pilot; IEEE Copyright Form; publication in IEEE Xplore and ACM Digital Library contingent on registration and poster-session presentation; acceptance 20-25%; timeline; WIP poster invitations; TPC Chair and Co-Chairs | 2026-11-24 |
| 4 | https://dac.com/2027/program/engineering-track-presentations | DAC 2027 Engineering Tracks (Back-End Design, Front-End Design, IP, Systems and Software): submission deadline Jan 11, 2027; accept/reject Mar 8, 2027; presenter registration by Apr 10, 2027 | 2026-11-24 |
| 5 | https://dac.com/2027/about/committees | DAC 2027 committees: General Chair David Pan; TPC Chair Ambar Sarkar; TPC Co-Chairs Jiang Hu and Rajiv Joshi; a separate Engineering Program Chair (Henning Spruth) and Engineering Track Committee; ACM SIGDA and IEEE CEDA representatives | 2026-11-24 |
| 6 | https://softconf.com/dac27/research | DAC 2027 research submission portal (Softconf/START `dac27`); the portal banner reads "June 11-14, 2027", which contradicts dac.com — dac.com's July 11-14, 2027 is treated as controlling | 2026-11-24 |
| 7 | https://www.ieee.org/conferences/publishing/templates | IEEE conference templates that the DAC 2027 research page links as the required template | 2026-11-24 (link target taken from source 3) |
| 8 | https://dac.com/2026/speaker-resource-center/research-manuscripts-guidelines | DAC 2026 (history): 6+1 pages, double-column, 9-10 pt, **ACM Templates**; "ACM is the 2026 copyright holder for 63DAC"; ACM Copyright Form; ACM Open Access/APC notice | 2026-07-09; re-read 2026-11-24 |
| 9 | https://web.archive.org/web/20251109213124/https://dac.com/2026/authors/research-frequently-asked-questions (Wayback Machine snapshot of 2025-11-09; the live page returns 404) | DAC 2026 FAQ (history): two-stage submission, double-blind rules, COI; its "follow the IEEE style template" sentence contradicted source 8 — see the template note below | 2026-07-09; archive re-read 2026-11-24 |
| 10 | https://dac.com/2026 and https://ieee-ceda.org/post/announcement/dac-2026-call-contributions | DAC 2026 (63rd) history: Long Beach, July 26-29, 2026; DAC 2026 call announcement | 2026-07-09 |
| 11 | https://web.archive.org/web/20251219174745/https://dac.com/2026/engineering-track-presentations and https://softconf.com/dac26/lbr26/ | DAC 2026 history: Engineering Track (deadline Jan 12, 2026) and the Late Breaking Results track on Softconf `dac26` | 2026-07-09; archive re-read 2026-11-23 |
| 12 | https://dl.acm.org/conference/dac | ACM Digital Library DAC proceedings series (archival record) | 2026-07-09 |
| 13 | https://ieee-ceda.org/awards/a-richard-newton-award and http://sigda.org/archive/node/44.html | ACM/IEEE A. Richard Newton Technical Impact Award in EDA (paper ≥10 years old, peer-reviewed ACM/IEEE archival publication) | 2026-07-09 |

## Verified DAC 2027 facts used in skills

- **DAC 2027 is the 64th Design Automation Conference** ("The Chips to Systems Conference"),
  **July 11-14, 2027, San Jose Convention Center, San Jose, California** (source 1). Sponsored by
  **ACM and IEEE**, supported by **ACM SIGDA** and **IEEE CEDA** (sources 1, 5); the
  `dac.com/2027` site also lists the **IEEE Solid-State Circuits Society** among its affiliates.
- **Research-Manuscript calendar (DAC 2027)** (source 3): abstract stage (title, abstract of
  approximately 100 words, all co-authors with affiliations, countries and emails, and TPC
  conflicts) **November 11, 2026**, 5:00 pm US Pacific; manuscript **November 18, 2026**, 5:00 pm
  US Pacific — no resubmission to fix problems after it, and no new co-authors or re-ordering
  after it. Then: accepted manuscript IDs on the DAC website **February 22, 2027**; accept/reject
  notifications **March 8, 2027**; manuscript confirmation **March 22, 2027**; proceedings
  manuscript **March 31, 2027**; author registration **April 10, 2027**; draft slides **April 15,
  2027**; slide feedback **May 14, 2027**; final slides **May 21, 2027**; DAC begins **July 11,
  2027**.
- **No author-response window.** The DAC 2027 research timeline and its "Review and Selection
  Process" section list no rebuttal or author-response stage between the manuscript deadline and
  the notifications (source 3).
- **Format:** up to **6 pages excluding references, plus 1 additional page for references only**
  ("6+1, not 7"), **double-column**, **9 or 10-pt** font, PDF only, a single file, following the
  **IEEE Templates** (sources 3, 7). Any non-reference content on the reference page means
  **desk rejection**. The draft must leave room for the author block and acknowledgements in the
  final version without exceeding 6 pages; submitted and final versions should not differ
  significantly. Preliminary submissions are at a disadvantage (source 3).
- **Template question resolved.** The required template has tracked the edition's copyright
  holder, which changed between the last two editions: DAC 2026 required the **ACM Templates** with ACM as the 2026 copyright holder (source 8), and
  DAC 2027 requires the **IEEE Templates** with the **IEEE Copyright Form** (source 3). The DAC
  2026 FAQ's "IEEE style template" sentence (source 9) was an inconsistency on the 2026 site, not
  the 2026 rule; for DAC 2027 every official page agrees on IEEE.
- **Double-blind review** (source 3): no author names or affiliations anywhere in the manuscript
  or abstract (identity reveal = desk rejection); self-citations in the **third person**; "omitted
  for blind review" is **not permitted**; **PDF metadata must not contain author information**;
  identities of authors and reviewers are known only to the TPC Chair.
- **Submission rules** (source 3): an individual may author at most **20** research manuscripts
  (the first 20 by submission time are reviewed, the rest rejected); TPC members at most 5
  submissions to their program and at most 3 to their own subcommittee. Duplicate submissions are
  prohibited; overlapping papers under review elsewhere must be disclosed, and related unpublished
  work (under review or accepted) is listed and uploaded as a PDF for the TPC Chair only. **arXiv
  preprints are allowed** provided the DAC submission stays double-blind compliant. Submissions are
  screened against a similarity database.
- **Conflicts of interest** (source 3): declare TPC conflicts for all co-authors (advisor-advisee;
  co-authors within the last 24 months; same institution; co-PIs within 2 years; close personal or
  family relationship). Missing or false COIs lead to desk rejection.
- **Topic areas** (source 3): **AI, Design (DES), EDA, Security (SEC), Systems (SYS)** with
  numbered subcategories (e.g. AI1 agentic AI for hardware design, EDA7 physical design, SEC2
  hardware security primitives), plus cross-cutting interest in low power, chiplets, 3D-IC and
  quantum computing. In Softconf authors select up to two topic areas and up to three keywords
  from a fixed list (form fields, not manuscript keywords).
- **AI/LLM policy** (source 3): DAC follows ACM/IEEE policy. Content generated by LLMs (text,
  figures, images, code) must be disclosed in a separate section headed **"Content Generated by
  AI"**, naming the LLMs and the sections affected; editing, grammar, translation and knowledge
  retrieval need no disclosure (recommended). LLMs cannot be authors. DAC 2027 also runs a
  **controlled LLM pilot**: organizers generate one report per paper after human reviews are
  locked, used only as a reference in PC discussion; it does not score or decide.
- **Selection criteria** (source 3): technical quality; originality with comparisons to other
  approaches; significance measured by quantitative criteria (runtime, optimality, design-time,
  automation); experimental evidence on industry-strength designs or widely accepted benchmarks;
  **a good discussion of limitations**; writing quality. Acceptance rates are uniform across areas
  and "in the range of 20-25% for the past several years".
- **Outcome options** (source 3): accept or reject; manuscripts not accepted may be **invited to a
  Work-in-Progress (WIP) poster session** (not published in the proceedings).
- **Publication/copyright** (source 3): authors of accepted papers complete the **IEEE Copyright
  Form** (emailed to the contact author in March). **Publication in IEEE Xplore and the ACM
  Digital Library** is contingent on conference registration and presentation at the poster
  session.
- **Author obligations** (source 3): one co-author pays the full **Speaker Registration** fee
  (no student rate; one unique registration per paper); the paper is presented **in person**
  (international authors name an alternate presenter); every accepted paper also prepares a
  **poster**. Authorship follows IEEE's criteria.
- **Leadership** (sources 3, 5): General Chair **David Pan** (UT Austin and DeepWeave); TPC Chair
  **Ambar Sarkar** (Nvidia); TPC Co-Chairs **Jiang Hu** (Texas A&M) and **Rajiv Joshi** (IBM);
  Engineering Program Chair **Henning Spruth** (NXP).
- **Tracks** (sources 2, 4, 5): the **Research Manuscript** track (double-blind, archival) is
  distinct from the **Engineering Tracks** (Back-End Design, Front-End Design, IP, Systems and
  Software; no manuscript, no publication; deadline **January 11, 2027**), which have their own
  **Engineering Program Chair and Engineering Track Committee**; plus Research Special Sessions,
  Research Panels, Tutorials, Workshops, Engineering Special Sessions, DAC Pavilion and Exhibitor
  Forum. The DAC 2027 call lists **no Late Breaking Results track** as of 2026-11-24
  (`dac.com/2027/late-breaking-results` returns 404); DAC 2026 ran one (source 11).
- **Awards:** the ACM/IEEE **A. Richard Newton Technical Impact Award in EDA** honors a
  peer-reviewed ACM/IEEE paper ≥10 years old for lasting impact (not a best-paper prize); the DAC
  2027 site also lists the DAC Most Influential Papers Award, Under-40 Awards and Young Fellows
  (sources 1, 13).

## DAC 2026 facts (history, closed cycle)

DAC 2026 (63rd) met at the Long Beach Convention Center, July 26-29, 2026 (source 10); its
manuscript deadline was November 19, 2025; it used the ACM Templates with ACM as copyright
holder (source 8); its Engineering Track deadline was January 12, 2026 and it ran Late Breaking
Results on `softconf.com/dac26/lbr26` (source 11).

## The Research-vs-Engineering track question (honest reading)

DAC's defining structural feature versus the academic architecture venues (ISCA/MICRO/HPCA) is its
**dual character**: a rigorous, double-blind, archival **Research Manuscript** track *and* an
industry-facing **Engineering Track** built for practitioners and technical managers, run by a
separate Engineering Program Chair and committee (source 5) and oriented toward presentation rather
than archival novelty — it "do[es] not require a manuscript and entail[s] no publication" (source
3). Choosing the right track is the highest-leverage DAC-specific decision and is the subject of
`skills/dac-topic-selection`. The two tracks have **different deadlines, different review criteria,
and different (or no) archival outcomes** — never assume an Engineering-Track deadline or format
matches the Research-Manuscript one.

## Artifact / reproducibility posture (a real divergence from siblings)

Unlike the SE venues (FSE/ICSE/ISSTA) and the architecture venues (MICRO/ISCA/HPCA) that run
**formal artifact-evaluation tracks with ACM badges**, DAC **does not operate a badge-issuing
artifact-evaluation track** for research manuscripts: the DAC 2027 Call for Contributions and
Research Manuscript page list none (sources 2, 3). The community's reproducibility culture instead
runs on **shared EDA benchmark suites and open-source flows** (ISPD contest benchmarks, the EPFL
combinational benchmark suite, OpenROAD / OpenROAD-flow-scripts, ISCAS'85/'89 and ITC'99 circuits,
the TAU timing contests, CircuitNet and similar ML-for-EDA datasets) — and the DAC 2027 criteria
explicitly reward "industry-strength designs or widely accepted benchmarks". DAC 2027 states no
data- or code-availability requirement.

## No editor-in-chief; conference cost model

Like every venue in this collection, DAC has **no standing editor-in-chief**; the rotating analogue
is the per-edition **General Chair, TPC Chair and Co-Chairs, and subcommittee chairs**, appointed
under ACM SIGDA and IEEE CEDA. DAC charges no submission fee or APC on its research pages; it is
funded by registration and its large industry exhibition, and each accepted paper requires one
full Speaker Registration (source 3).

## Still cycle-volatile / 待核实

- The full DAC 2027 TPC subcommittee roster (the Committees page shows chairs only in the fetched
  text) — **待核实**.
- The exact IEEE template variant and any copyright-notice wording for the DAC 2027 final version
  (the research page links the generic IEEE templates page and says the IEEE Copyright Form is
  emailed in March) — **待核实** until the proceedings instructions are published.
- Whether DAC 2027 will add a Late Breaking Results call later in the cycle (none listed on
  2026-11-24) — **待核实**.
- The softconf portal banner's "June 11-14, 2027" versus dac.com's "July 11-14, 2027" — recorded
  as a portal typo; dac.com controls.
- Next edition (DAC 2028): not checked.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and
python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "DAC 2027",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 6, "source": "https://dac.com/2027/program/research-manuscript-submissions", "note": "DAC 2027 Research Manuscript: 6 pages excluding references, plus 1 additional references-only page; any other content on the reference page means desk rejection"},
    "page_limit_includes_references": {"value": false, "source": "https://dac.com/2027/program/research-manuscript-submissions"},
    "abstract_words_max": {"value": 100, "soft": true, "source": "https://dac.com/2027/program/research-manuscript-submissions", "note": "\"approximately 100 words\", entered at the abstract stage"},
    "review_mode": {"value": "double-blind", "source": "https://dac.com/2027/program/research-manuscript-submissions", "note": "third-person self-citation; 'omitted for blind review' not permitted; PDF metadata must not contain author information"},
    "template": {"value": "IEEE Templates (conference), double-column, 9 or 10-pt font", "source": "https://dac.com/2027/program/research-manuscript-submissions", "note": "DAC 2026 used the ACM Templates; DAC 2027 switched to IEEE"},
    "file_format": {"value": "single readable PDF (manuscript + reference page)", "source": "https://dac.com/2027/program/research-manuscript-submissions"},
    "portal": {"value": "Softconf/START (softconf.com/dac27/research); two stages: abstract Nov 11, 2026, manuscript Nov 18, 2026, 5:00 pm US Pacific", "source": "https://dac.com/2027/program/research-manuscript-submissions"},
    "required_statements": {"value": [], "source": "https://dac.com/2027/program/research-manuscript-submissions", "note": "no statement is required in every manuscript; acknowledgements belong only in the final version"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://dac.com/2027/program/research-manuscript-submissions", "note": "a separate section headed 'Content Generated by AI' if LLM-generated text/figures/images/code is used; editing/grammar/translation use exempt (disclosure recommended)"},
    "separate_upload_statements": {"value": ["conflict_of_interest"], "source": "https://dac.com/2027/program/research-manuscript-submissions", "note": "TPC conflicts of all co-authors entered in the submission form; related unpublished work disclosed as uploaded PDFs"},
    "llm_policy": {"value": "LLM-generated content disclosed in a 'Content Generated by AI' section; LLMs cannot be authors; organizers pilot one post-review LLM report per paper for PC discussion only", "source": "https://dac.com/2027/program/research-manuscript-submissions"},
    "preprint_policy": {"value": "arXiv papers may be submitted if the DAC submission stays double-blind compliant; concurrent submissions prohibited", "source": "https://dac.com/2027/program/research-manuscript-submissions"},
    "supplement_policy": {"value": "no supplementary material: 6 pages + 1 references-only page in a single PDF", "source": "https://dac.com/2027/program/research-manuscript-submissions"},
    "submission_fee": {"value": "none stated; one full Speaker Registration per accepted paper (no student rate)", "source": "https://dac.com/2027/program/research-manuscript-submissions"},
    "data_code_policy": {"value": null, "note": "not stated on the official pages as of 2026-11-24; no artifact-evaluation track"},
    "keywords_required": {"value": null, "note": "not stated for the manuscript as of 2026-11-24; Softconf asks for up to three keywords from a fixed list as a form field"}
  }
}
```
