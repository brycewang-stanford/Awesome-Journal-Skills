# External Tools - DAC (Design Automation Conference)

Access date: 2026-07-09

Use these surfaces after reopening the current DAC cycle pages. DAC mechanics — abstract/manuscript
deadlines, page budget, track structure, whether any response period exists — are decided per
edition, and the `dac.com`/`dl.acm.org`/`ieee-ceda.org`/`softconf.com` gateway may block direct
fetches (read via search renderings and cross-check ACM DL and dblp). Do not confuse this venue with
**ASP-DAC** (Asia and South Pacific DAC) or **DATE** (Design, Automation and Test in Europe), which
are distinct EDA conferences with their own calls; and note "DAC" in a circuits paper often means
*digital-to-analog converter*, an in-scope topic, not the conference.

## Official workflow

- DAC 2026 home (Long Beach, Jul 26-29, 2026): https://dac.com/2026
- DAC 2026 Call for Contributions: https://dac.com/2026/call-for-contributions
- Research Manuscripts Guidelines (6+1, ACM double-column): https://dac.com/2026/speaker-resource-center/research-manuscripts-guidelines
- Research FAQ (two-stage submission, double-blind, COI): https://dac.com/2026/authors/research-frequently-asked-questions
- Manuscript submission deadline event: https://dac.com/2026/events/manuscript-submission-deadline-rm
- Engineering Track: https://dac.com/2026/engineering-track-presentations
- Late Breaking Results: https://dac.com/2026/late-breaking-results and Softconf `dac26`: https://softconf.com/dac26/lbr26/
- IEEE CEDA DAC 2026 announcement: https://ieee-ceda.org/post/announcement/dac-2026-call-contributions
- A. Richard Newton Technical Impact Award: https://ieee-ceda.org/awards/a-richard-newton-award

## Cross-check surfaces (when the gateway blocks the primary page)

- ACM DL DAC proceedings series: https://dl.acm.org/conference/dac (per-edition tables of contents;
  62nd = 2025, 63rd = 2026).
- dblp DAC stream: https://dblp.org/db/conf/dac/index.html — for exemplar verification and the exact
  proceedings string.
- The Softconf/START `dac26` submission portals (research, LBR, engineering) for the machine-readable
  cutoffs the CFP paraphrases.
- IEEE CEDA event listing for the 63rd DAC for sponsorship and date confirmation.

## EDA benchmark suites and open flows (evidence surfaces)

- **ISPD** placement/routing contest benchmarks (physical design).
- **EPFL** combinational benchmark suite (logic synthesis).
- **ISCAS'85/'89** and **ITC'99** circuits (test/verification).
- **TAU** timing-analysis contest sets (STA).
- **CircuitNet / OpenABC-D** and similar ML-for-EDA datasets.
- **OpenROAD / OpenROAD-flow-scripts**, **ABC**, **Yosys**, **KLayout** open flows; open PDKs
  (Nangate45, ASAP7, SkyWater) for reproducible QoR.

## Author-side checks

- Softconf profile, the **two-stage** abstract-then-manuscript submission, all co-authors entered at
  the abstract stage, and TPC **conflict-of-interest** declarations.
- ACM double-column template compliance, the **6-page body + 1 references-only page** budget, single
  readable PDF, 9-10 pt.
- Double-blind sweep: PDF metadata, **third-person self-citations**, anonymized tool/repo names,
  removed acknowledgements/funding, no cluster paths or vendor-flow fingerprints.
- Standard benchmark suite + strongest tuned baseline + per-benchmark QoR + runtime + ablation.
- Post-acceptance: ACM copyright form, first-page rights/DOI stamp, and the April proceedings
  (ACM DL) deadline.

## Do not infer

- Do not infer a **rebuttal/response period** exists — DAC research review has historically been
  TPC-driven without one (**待核实** for the current cycle).
- Do not assume DAC runs a **formal artifact-evaluation / ACM badge track** — it historically has
  not (**待核实**); build artifacts for credibility and reuse, not a badge.
- Do not assume the page budget, ACM template revision, deadlines, or acceptance rate carry over
  between editions, or that Engineering-Track/LBR deadlines match the Research one.
- If pages disagree, treat the newest Call for Contributions, the Research Manuscripts Guidelines,
  or the Softconf deadline page as controlling, and record the conflict.
