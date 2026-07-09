# Official Source Map - DAC (Design Automation Conference)

Access date: 2026-07-09

This map records the official and cross-check sources used for DAC-specific facts in this
pack. DAC is the ACM/IEEE **Design Automation Conference** — branded since recent editions as
**"The Chips to Systems Conference"** — the premier venue for electronic design automation (EDA)
and chip/system design, sponsored by ACM and IEEE and supported by **ACM SIGDA** and **IEEE CEDA**.
Its dates, page budget, deadlines, and track structure are decided per edition. Reopen the
current-cycle Call for Contributions, the Research Manuscripts Guidelines, the Important-Dates
event pages, and the ACM copyright/proceedings notice before giving submission-ready advice.

## Access method note

Direct fetches of `dac.com`, `dl.acm.org`, `ieee-ceda.org`, and `softconf.com` returned or were
expected to return **HTTP 403/blocked egress** from the build sandbox on 2026-07-09 (the same
gateway block seen when verifying other ACM/IEEE venues in this repo). Official pages were
therefore read through **search-engine renderings of the exact URLs** (dac.com/2026 pages, the
IEEE CEDA call announcement) and cross-checked against the **ACM Digital Library** DAC proceedings,
**dblp**, and IEEE CEDA event listings. Facts that could not be pinned to at least two independent
surfaces are labeled **待核实**. Two name-collision guards: (1) **ASP-DAC** (Asia and South
Pacific Design Automation Conference) and **DATE** (Design, Automation and Test in Europe) are
*sibling but distinct* EDA conferences with their own calls and deadlines — no fact here derives
from them; (2) "DAC" also abbreviates *digital-to-analog converter* in circuit papers — an
in-scope research topic, not this conference.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://dac.com/2026 | DAC 2026 (63rd) home: "The Chips to Systems Conference," Long Beach, California, July 26-29, 2026 | 2026-07-09 |
| 2 | https://dac.com/2026/call-for-contributions | DAC 2026 Call for Contributions: Research Manuscripts, Engineering Track, Late Breaking Results, Special Sessions/Panels | 2026-07-09 |
| 3 | https://dac.com/2026/speaker-resource-center/research-manuscripts-guidelines | Research Manuscript format: ≤6 pages + 1 references-only page, double-column, 9-10 pt, ACM template, single PDF; ACM is the 2026 copyright holder, archived on ACM DL | 2026-07-09 |
| 4 | https://dac.com/2026/events/manuscript-submission-deadline-rm | Research Manuscript submission deadline event (mid-to-late November 2025; rendering showed Nov 19, 2025) | 2026-07-09 |
| 5 | https://dac.com/2026/authors/research-frequently-asked-questions | Research FAQ: two-stage abstract-then-manuscript submission, double-blind rules, TPC conflict-of-interest declaration | 2026-07-09 |
| 6 | https://ieee-ceda.org/post/announcement/dac-2026-call-contributions | IEEE CEDA announcement of the DAC 2026 Call for Contributions; ACM/IEEE + SIGDA/CEDA sponsorship | 2026-07-09 |
| 7 | https://dac.com/2026/late-breaking-results and https://softconf.com/dac26/lbr26/ | Late Breaking Results track and the Softconf/START submission system (`dac26`) used by DAC | 2026-07-09 |
| 8 | https://dac.com/2026/engineering-track-presentations | Engineering Track (industry practitioners: front-end/back-end design, IP, embedded systems & software) with a separate review committee | 2026-07-09 |
| 9 | https://dl.acm.org/conference/dac | ACM Digital Library DAC proceedings series (archival record of accepted Research Manuscripts) | 2026-07-09 |
| 10 | https://ieee-ceda.org/awards/a-richard-newton-award and http://sigda.org/archive/node/44.html | ACM/IEEE A. Richard Newton Technical Impact Award in EDA (paper ≥10 years old, peer-reviewed ACM/IEEE archival publication) | 2026-07-09 |

## Verified DAC 2026 facts used in skills

- **DAC 2026 is the 63rd ACM/IEEE Design Automation Conference** ("The Chips to Systems
  Conference"), at the **Long Beach Convention Center, Long Beach, California**, **July 26-29,
  2026** (source 1; a minority of third-party listings said Los Angeles — the official dac.com/2026
  and IEEE CEDA pages say Long Beach). As of the 2026-07-09 access date the conference is upcoming
  and the DAC 2026 review cycle has already run its submission stage.
- **Sponsorship:** ACM and IEEE, supported by **ACM SIGDA** and **IEEE CEDA** (sources 2, 6).
  Historically also associated with EDAC/ESD Alliance; **待核实** for the exact 2026 supporting-org
  list beyond SIGDA/CEDA.
- **Research-Manuscript calendar (DAC 2026):** two-stage submission — an **abstract stage** (title,
  abstract, all co-authors) roughly a week before the **manuscript deadline in mid-to-late November
  2025** (rendering showed **19 November 2025**; abstract stage ~one week earlier). Accepted
  research-manuscript IDs published **23 February 2026**; accept/reject notifications **9 March
  2026**; confirmation forms **23 March 2026**; copyright form and final/proceedings manuscript
  **14 April 2026** (sources 4, 5; third-party timeline aggregation). Treat exact days as **待核实**
  until re-read on the live event pages.
- **Format:** manuscript **within 6 pages excluding references, plus one additional
  references-only page** (the "6+1" budget), **double-column**, **9 or 10-pt** font, single PDF,
  **ACM template**. Any non-reference content on the extra page is grounds for **desk rejection**
  (source 3).
- **Publication/copyright:** **ACM is the 2026 copyright holder** and accepted papers are archived
  on the **ACM Digital Library** (source 3, 9). Given ACM/IEEE co-sponsorship, DAC papers have also
  historically been indexed on **IEEE Xplore** — **待核实** for the exact 2026 Xplore arrangement.
- **Review is double-blind:** author names and affiliations must not appear anywhere on the
  manuscript except where a citation to the authors' own prior work is unavoidable, and such
  self-citations must be written in the **third person** (sources 3, 5).
- **Research acceptance rate** is historically in the **~20-25%** range (source: third-party
  DAC-2026 aggregation cross-checked against DAC's long-standing selectivity; treat the precise
  figure as **待核实** each cycle).
- **Tracks:** the **Research Manuscript** track (double-blind, archival, ACM DL) is distinct from
  the **Engineering Track** (industry practitioners; front-end design, back-end design, IP,
  embedded systems & software; separate review committee; presentation-oriented), and from **Late
  Breaking Results**, **Research/Engineering Special Sessions**, **Panels**, tutorials, workshops,
  and the large **exhibition** floor (sources 2, 7, 8).
- **Topic lanes (DAC 2026):** classical EDA (logic synthesis, physical design, timing, verification
  and test, analog/mixed-signal), **AI/ML for EDA** (agentic AI for verification/synthesis/physical
  design, foundation models for EDA, benchmarks/datasets/model evaluation), **GenAI in chip and
  system design**, **hardware security** (cryptographic primitives, trusted design, post-quantum,
  supply-chain integrity, AI/ML security), embedded systems, chiplets, and quantum (sources 2, 6).
- **Awards:** the ACM/IEEE **A. Richard Newton Technical Impact Award in EDA** honors a
  peer-reviewed ACM/IEEE paper ≥10 years old for lasting impact (not a best-paper prize); DAC also
  runs the **A. Richard Newton Young Student Fellowship** and Best-Paper recognition (source 10).

## The Research-vs-Engineering track question (honest reading)

DAC's defining structural feature versus the academic architecture venues (ISCA/MICRO/HPCA) is its
**dual character**: a rigorous, double-blind, archival **Research Manuscript** track *and* an
industry-facing **Engineering Track** built for practitioners and technical managers, reviewed by a
separate committee and oriented toward presentation rather than archival novelty. Choosing the
right track is the highest-leverage DAC-specific decision and is the subject of
`skills/dac-topic-selection`. The two tracks have **different deadlines, different review criteria,
and different (or no) archival outcomes** — never assume an Engineering-Track deadline or format
matches the Research-Manuscript one.

## Artifact / reproducibility posture (a real divergence from siblings)

Unlike the SE venues (FSE/ICSE/ISSTA) and the architecture venues (MICRO/ISCA/HPCA) that run
**formal artifact-evaluation tracks with ACM badges**, DAC has **historically not operated a
standing, badge-issuing artifact-evaluation track** for research manuscripts. Whether the DAC 2026
cycle introduces any artifact/open-source track is **待核实**. The community's reproducibility
culture instead runs on **shared EDA benchmark suites and open-source flows** (ISPD contest
benchmarks, the EPFL combinational benchmark suite, OpenROAD / OpenROAD-flow-scripts, ISCAS'85/'89
and ITC'99 circuits, the TAU timing contests, CircuitNet and similar ML-for-EDA datasets). The
reproducibility and artifact skills in this pack are written to that reality, not to a badge scheme
DAC does not currently run.

## No editor-in-chief; conference cost model

Like every venue in this collection, DAC has **no standing editor-in-chief**; the rotating analogue
is the per-edition **General Chair, Technical Program Chair, and Track Chairs**, appointed under ACM
SIGDA and IEEE CEDA. DAC is funded by registration and its large industry exhibition, not by an APC.

## Still cycle-volatile (verify every year)

- Exact abstract-stage and manuscript deadlines, AoE/PST cutoff conventions, and notification dates.
- Whether a formal **author rebuttal / response period** exists for research manuscripts (**待核实**:
  not confirmed for DAC 2026; DAC's research review has historically been TPC-driven without the
  ISCA/MICRO-style author response).
- Exact page budget and which ACM template revision is required (DAC 2026: 6+1, double-column).
- Engineering-Track and Late-Breaking-Results deadlines and formats (LBR ran on `softconf.com/dac26`).
- Research acceptance rate, exact topic-area list, and any generative-AI authorship/disclosure rule.
- IEEE Xplore vs ACM-DL-only archival arrangement, and the full 2026 supporting-organization list
  beyond SIGDA/CEDA (**待核实**).
- DAC 2026 full TPC / Track-Chair rosters (**待核实**).
