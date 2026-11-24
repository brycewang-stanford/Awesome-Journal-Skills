# Official Source Map - ATC (ACM SIGOPS Annual Technical Conference)

Access date: 2026-07-09 (ATC 2026 snapshot). ATC 2027 home page, Call for Papers and Organizers,
the `atc27.hotcrp.com` and `atc26.hotcrp.com` sites, the ATC 2026 home page and call, the
sysartifacts ATC 2026 page, the USENIX ATC '25 artifact call, the USENIX sunset announcement and
the SIGOPS conference list **re-verified 2026-11-24** against the live pages (direct fetch with
`curl`; the 403 block recorded in July no longer applies to `sigops.org` or `usenix.org`).

**Edition status, checked 2026-11-24.** **USENIX ATC is retired**: USENIX announced "the
bittersweet conclusion of our longest-running event, the USENIX Annual Technical Conference in
July 2025, following USENIX ATC '25", and its Board "made the difficult decision to sunset
USENIX ATC" (source 8). **USENIX ATC '25 was the last USENIX edition**; do not plan for a
USENIX ATC '26 or later. The conference **continues under ACM SIGOPS** with the same acronym as
the **ACM SIGOPS Annual Technical Conference**: ATC 2026 (Hong Kong, November 15-18, 2026) was
the first SIGOPS edition and has now met. The live edition is **ATC 2027**, **28 June – 1 July
2027, Le Couvent des Jacobins, Rennes, France**, whose Call for Papers is published, so this pack
now describes ATC 2027. Its single gate is a **submission deadline of 19 January 2027 (AoE, no
extensions)**; author response 3-5 April 2027; notification 27 April 2027; camera-ready 28 May
2027. ATC 2027 **drops the ATC 2026 two-page extended abstract**: the first review round now
reads the paper's first two pages.

This map records the official and cross-check sources used for ATC-specific facts in this pack.
Almost every mechanic was re-decided in the USENIX-to-SIGOPS handover and again between the 2026
and 2027 SIGOPS editions; reopen the current SIGOPS call for papers, the ATC HotCRP site, the
artifact-evaluation call, and the ACM Open Access terms before giving submission-ready advice.

## Access method note

On 2026-07-09 direct fetches of `sigops.org`, `usenix.org` and aggregator sites returned **HTTP
403** from the verification gateway, and the 2026 facts were read through search-engine
renderings of the exact URLs. On **2026-11-24** `sigops.org` / `atc.sigops.org`, `usenix.org`,
`hotcrp.com` and `sysartifacts.github.io` answered direct `curl -sL` requests, so every ATC 2027
fact below, and the re-checked 2026 facts, were read from the live page text. Wikipedia was not
re-read. Name-collision guard: ATC is not the *American Transplant Congress* or an *Academic Tax
Conference*.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://atc.sigops.org/2027/call-for-papers/ | ATC 2027 CFP: dates (submission 19 Jan 2027 AoE, no extensions; 72-hour author response 3-5 Apr 2027; notification 27 Apr 2027; camera-ready 28 May 2027; conference 28 Jun – 1 Jul 2027, Rennes); new for 2027 — per-author cap of 2 papers, and not every accepted paper gets an oral slot; topics; systems-only scope (quantum work without systems contributions out of scope); judging criteria incl. accessibility to the broader systems community; originality, workshop extensions, arXiv/tech reports/talks/social media explicitly permitted; resubmissions of rejected papers supply previous-submission information and a change summary (about one page, anonymized, shown to reviewers after their reviews); author list frozen at submission; double-blind with paper ID on page 1 and an anonymized system name if the name is already known; concurrent related submissions cited anonymously and emailed to the PC chairs; long papers at most 12 pages and short at most 6, excluding references but **including appendices**; optional appendix allowed within the limit; Operational Systems Track (may identify the organization); optional author response limited to factual corrections and answering questions, no new experiments/data/promises, 72 hours; two review rounds, the first based on the first two pages; A4/US letter, 178 x 229 mm block, two columns 8 mm apart, 10-point Times on 12-point leading, numbered pages, hyperlinked references; desk rejection for violations; `\documentclass[sigplan,10pt]{acmart}` recommended; generative-AI rule (no papers produced entirely or substantively by AI; AI for editing and framing allowed); conflict rules; PC chairs do not submit; conditional acceptance with shepherd approval; artifact evaluation encouraged; papers online before the conference; papers of merit forwarded to ACM TOCS and CACM Research Highlights; all accepted papers presented orally and/or as a poster, one author must attend; ACM Open Access with APCs for authors outside ACM Open. | 2026-11-24 |
| 2 | https://atc.sigops.org/2027/ (also https://sigops.org/s/conferences/atc/2027/index.html) | ATC 2027 home: 28 June – 1 July 2027, Rennes, France, Le Couvent des Jacobins; sponsor ACM SIGOPS; submission deadline 19 January 2027. | 2026-11-24 |
| 3 | https://atc.sigops.org/2027/organizers/ | ATC 2027 General Chair David Bromberg (University of Rennes); Program Committee Chairs Vijay Chidambaram (The University of Texas at Austin) and Peter Pietzuch (Imperial College London); Artifact Evaluation Chairs Miguel Matos (University of Lisbon) and Valerio Schiavoni (University of Neuchâtel); Publication Chairs Jia-Ju Bai and Julia Lawall. | 2026-11-24 |
| 4 | https://atc27.hotcrp.com/ | "ACM SIGOPS Annual Technical Conference, 2027 (ATC '27) submissions site"; its `/deadlines` page lists no deadline yet on 2026-11-24. | 2026-11-24 |
| 5 | https://sigops.org/s/conferences/atc/2026/cfp.html | ATC 2026 call (history): submission deadline June 10, 2026 (no extensions; no abstract registration); two-page extended abstract reviewed in round 1 and not published; long ≤ 12 / short ≤ 6 pages excluding references and appendices; generative-AI attestation in HotCRP; conditional acceptance. | 2026-11-24 |
| 6 | https://sigops.org/s/conferences/atc/2026/index.html | ATC 2026 home: November 15-18, 2026, Hyatt Hotel, Shatin, Hong Kong. | 2026-11-24 |
| 7 | https://atc26.hotcrp.com/deadlines | ATC 2026 HotCRP clock: submission deadline Thursday Jun 11, 2026, 4:59:59 AM PDT (= June 10, 2026, AoE). | 2026-11-24 |
| 8 | https://www.usenix.org/blog/usenix-atc-announcement + https://www.usenix.org/blog/preserving-legacy-usenix-atc | USENIX's decision to sunset USENIX ATC after ATC '25 (July 2025) and to preserve its legacy proceedings. | 2026-11-24 |
| 9 | https://sysartifacts.github.io/atc2026/ | ATC 2026 artifact evaluation: single-blind, cooperative, sysartifacts-run; registration at `atc26ae.hotcrp.com`; paper notification September 18, 2026; artifact submission September 22, 2026 (AoE); kick-the-tires phase. | 2026-11-24 |
| 10 | https://www.usenix.org/conference/atc25/call-for-artifacts | USENIX ATC '25 artifact-evaluation call: Artifacts Available / Artifacts Functional / Results Reproduced badges. | 2026-11-24 |
| 11 | https://www.usenix.org/conference/atc25/call-for-papers | USENIX ATC '25 research-track call (last USENIX edition): broad systems scope, 12/6-page limits, double-blind, Deployed Systems Track. | 2026-07-09 |
| 12 | https://www.usenix.org/sites/default/files/atc25_message.pdf | ATC '25 Program Co-Chairs' message: submission volume and artifact-evaluation statistics. | 2026-07-09 |
| 13 | https://www.sigops.org/conferences/ | ACM SIGOPS sponsored-conference list (APSYS, ASPLOS, EuroSys, PODC, SOCC, SOSP, SYSTOR, VEE, HotStorage); **ATC is not listed** there on 2026-11-24, although the ATC 2026 and 2027 sites name ACM SIGOPS as sponsor. | 2026-11-24 |
| 14 | https://2027.eurosys.org/cfp.html | Cross-check for ACM-wide 2027 open-access pricing (subsidized 2027 APC $500 ACM/SIG members, $750 non-members), which the ATC 2027 CFP does not quote. | 2026-11-24 |

## Verified ATC 2027 facts used in skills (re-verified 2026-11-24)

- **ATC 2027** is the second ACM SIGOPS Annual Technical Conference: **28 June – 1 July 2027,
  Le Couvent des Jacobins, Rennes, France**; sponsor ACM SIGOPS (sources 1, 2).
- **Calendar:** submission **19 January 2027**, AoE, no extensions; author response opens **3
  April 2027** and is due **5 April 2027** (72 hours); notification **27 April 2027**;
  camera-ready **28 May 2027** (source 1). HotCRP: `atc27.hotcrp.com` (source 4).
- **Lengths:** long submissions at most **12** pages, short at most **6**, excluding references
  but **including all text, figures, tables, footnotes and appendices** — an optional appendix
  must fit inside the limit (source 1). (ATC 2026 excluded appendices from the limit.)
- **Format:** PDF; A4 or US letter; **178 x 229 mm** (7 x 9 in) block; two columns **8 mm**
  apart; **10-point** Times Roman or similar on **12-point** leading; numbered pages;
  hyperlinked references; `\documentclass[sigplan,10pt]{acmart}` recommended (SIGPLAN
  LaTeX/Word templates); violations may be desk-rejected (source 1).
- **Per-author cap (new):** each author on at most **2** submissions to ATC 2027, regardless of
  length or track; violations may desk-reject every paper listing that author; author lists
  cannot change after submission (source 1).
- **Review:** two rounds; **round 1 is based on the first two pages** (reviewers may read on),
  rejecting papers that are out of scope, poorly motivated, hard to understand, incremental,
  poorly placed in related work, or weakly evaluated; survivors get more reviews; every paper may
  submit an **optional author response** limited to factual corrections and answering reviewer
  questions — no new experiments or data, no promises, no reliance on supplementary material
  (source 1).
- **Double-blind:** paper ID instead of names on page 1; institution not identified; an
  anonymized system name if the real one is publicly known; third-person self-citation;
  concurrent related submissions cited anonymously and emailed to the PC chairs (source 1).
- **Operational Systems Track:** deployment design/experience papers judged on new insights,
  data or lessons; may identify the organization when anonymization is impractical; marked in
  the final program (source 1).
- **Resubmissions:** papers under submission elsewhere are not allowed; for previously rejected
  papers, upload prior-submission information and an anonymized change summary (about one
  page), shown to reviewers after their reviews (source 1).
- **Preprints:** arXiv, technical reports, talks and social media are explicitly permitted
  (source 1).
- **Generative AI:** authors take intellectual responsibility; AI may aid editing and framing,
  but papers produced entirely or substantively by generative AI must not be submitted
  (source 1).
- **Accepted papers:** conditional acceptance, final after shepherd approval; artifact
  evaluation encouraged; papers online before the conference; selected papers forwarded to
  **ACM TOCS** and **CACM Research Highlights**; every paper presented orally and/or as a
  poster (not all get an oral slot), and one author must attend (source 1).
- **ACM Open Access:** ATC publications are open access; authors outside ACM Open pay an APC
  unless they qualify for a rare waiver (source 1). The CFP gives no rate; ACM's 2027 subsidized
  rates as stated on another ACM-sponsored 2027 CFP are **$500** (ACM/SIG members) and **$750**
  (non-members) (source 14).
- **Chairs:** General Chair David Bromberg; PC Chairs Vijay Chidambaram and Peter Pietzuch; AE
  Chairs Miguel Matos and Valerio Schiavoni (source 3).
- **Scope:** all practical aspects of computer systems — operating systems, runtime systems,
  parallel and distributed systems, storage, networking, ML for systems and systems for ML,
  security and privacy, virtualization, software-hardware interactions, performance evaluation,
  reliability, energy, bug-finding and troubleshooting; artifacts valued; non-systems main
  contributions may be desk-rejected (source 1).

## ATC 2026 and USENIX ATC (history)

- ATC 2026 (first SIGOPS edition): **November 15-18, 2026**, Hyatt Hotel, Shatin, Hong Kong
  (source 6); submission deadline **June 10, 2026** (AoE, shown on HotCRP as Jun 11, 4:59:59 AM
  PDT), no abstract registration — this resolves the July 2026 "1 vs. 10 June" question
  (sources 5, 7); a required **two-page extended abstract** read by two reviewers in round 1 and
  not published; 12/6-page limits excluding references and appendices; an HotCRP attestation that
  the paper was not produced substantively by generative AI (source 5); artifact evaluation via
  sysartifacts, artifacts due September 22, 2026 (source 9).
- USENIX ATC ran from 1975 to ATC '25 (July 2025) and published proceedings, slides and videos
  free on usenix.org; USENIX ATC '25 had a Deployed Systems Track and the Available / Functional /
  Reproduced badge triple (sources 8, 10, 11).
- The July 2026 map's statement that the SIGOPS conference list places ATC alongside SOSP and
  EuroSys is **withdrawn**: the list re-read on 2026-11-24 does not include ATC (source 13).

## No editor-in-chief; open access with an APC

Like every conference in this collection, ATC has **no standing editor-in-chief**; its rotating
analogue is the per-edition General Chair and PC Chairs under ACM SIGOPS. Historically USENIX ATC
charged **no APC**; under ACM Open Access the SIGOPS editions charge an APC to authors outside ACM
Open institutions.

## 待核实 (could not be verified on 2026-11-24)

- The ATC 2027 **artifact-evaluation call** (badges, dates) — not yet published; the ATC 2026
  sysartifacts page is the latest.
- ATC 2027 **camera-ready page allowance** and any final-version appendix rules.
- The ATC 2027 HotCRP `/deadlines` clock (empty on 2026-11-24).
- The exact 2027 APC applied to ATC papers (the ATC CFP quotes no figure).
- The 2026 subsidy figures previously carried by this pack (about US$250 / US$350), which came
  from secondary renderings and were not re-confirmed on an official page.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and
python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "ACM SIGOPS ATC 2027",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 12, "source": "https://atc.sigops.org/2027/call-for-papers/", "note": "ATC 2027 long papers: 12 pages excluding references but including appendices; short papers at most 6"},
    "page_limit_includes_references": {"value": false, "source": "https://atc.sigops.org/2027/call-for-papers/"},
    "review_mode": {"value": "double-blind", "source": "https://atc.sigops.org/2027/call-for-papers/", "note": "Operational Systems Track may identify the organization"},
    "template": {"value": "ACM acmart \\documentclass[sigplan,10pt]{acmart}; A4 or US letter, 178 x 229 mm block, two columns 8 mm apart, 10-point Times on 12-point leading, numbered pages, hyperlinked references", "source": "https://atc.sigops.org/2027/call-for-papers/"},
    "file_format": {"value": "PDF", "source": "https://atc.sigops.org/2027/call-for-papers/"},
    "portal": {"value": "HotCRP (atc27.hotcrp.com); submission deadline 19 January 2027 AoE, no extensions", "source": "https://atc.sigops.org/2027/call-for-papers/"},
    "supplement_policy": {"value": "optional appendix allowed but counts toward the 12/6-page limit; PC members need not review supplementary material", "source": "https://atc.sigops.org/2027/call-for-papers/"},
    "preprint_policy": {"value": "arXiv, technical reports, talks and social media explicitly permitted; use an anonymized system name if the real one is known", "source": "https://atc.sigops.org/2027/call-for-papers/"},
    "llm_policy": {"value": "AI may aid editing and framing; papers produced entirely or substantively by generative AI must not be submitted", "source": "https://atc.sigops.org/2027/call-for-papers/"},
    "apc": {"value": "ACM Open Access: no APC for ACM Open institutions; otherwise an APC unless a (rare) waiver applies; the ATC CFP quotes no rate", "source": "https://atc.sigops.org/2027/call-for-papers/"},
    "data_code_policy": {"value": "artifacts valued in review; accepted papers encouraged to supply code and data via artifact evaluation", "source": "https://atc.sigops.org/2027/call-for-papers/"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```
