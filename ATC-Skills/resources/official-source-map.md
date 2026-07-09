# Official Source Map - ATC (ACM SIGOPS Annual Technical Conference)

Access date: 2026-07-09

This map records the official and cross-check sources used for ATC-specific facts in this pack.
**ATC is in the middle of a sponsorship transition:** after roughly fifty years (1975-2025) as the
**USENIX Annual Technical Conference**, USENIX decided to sunset the event, and **ACM SIGOPS** took
it over. The conference **kept the acronym ATC** but changed its full name to the **ACM SIGOPS
Annual Technical Conference**, with ATC 2026 the first SIGOPS-run edition. Reopen the current-cycle
SIGOPS call for papers, the ATC HotCRP site, the artifact-evaluation call, and the ACM Open Access
terms before giving submission-ready advice — almost every mechanic below was re-decided in the
handover.

## Access method note

Direct fetches of `sigops.org`, `usenix.org`, `en.wikipedia.org`, and the aggregator sites
(`myhuiban.com`, `getpaperpilot.com`, `wikicfp.com`) returned **HTTP 403** from the verification
gateway on 2026-07-09 (the same egress block seen when verifying other systems venues). Official
pages were therefore read through **search-engine renderings of the exact URLs** and cross-checked
across the ATC 2026 SIGOPS CFP rendering, the USENIX ATC '25 call for papers and call for
artifacts, the ACM SIGOPS conference list, the Wikipedia "ACM SIGOPS Annual Technical Conference"
article, the USENIX transition blog posts, and dblp. Facts that could not be pinned to at least two
independent surfaces are labeled **待核实**. Note two easy confusions: (1) ATC's acronym collides
with the *American Transplant Congress* and an *Academic Tax Conference* — neither is this ATC, and
no fact here derives from them; (2) ATC 2026 is **not** OSDI '26, though both are SIGOPS-adjacent
systems venues in 2026.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://sigops.org/s/conferences/atc/2026/cfp.html | ATC 2026 SIGOPS call: two-round extended-abstract review, 12-page/6-page limits, two-column 10pt format, double-blind, conditional acceptance + shepherding, extended abstract not published | 2026-07-09 |
| 2 | https://sigops.org/s/conferences/atc/2026/index.html | ATC 2026 home: 15-18 November 2026, Hyatt Hotel, Shatin, Hong Kong; ACM SIGOPS sponsorship | 2026-07-09 |
| 3 | https://atc26.hotcrp.com/ | ATC 2026 HotCRP submission site | 2026-07-09 |
| 4 | https://www.usenix.org/conference/atc25/call-for-papers | USENIX ATC '25 research-track call: broad systems scope, 12/6-page limits, double-blind, Deployed Systems Track | 2026-07-09 |
| 5 | https://www.usenix.org/conference/atc25/call-for-artifacts | USENIX ATC '25 artifact-evaluation call: Available / Functional / Reproduced badges, AEC via HotCRP, post-notification schedule | 2026-07-09 |
| 6 | https://www.usenix.org/sites/default/files/atc25_message.pdf | ATC '25 Program Co-Chairs' message: submission volume and artifact-evaluation outcome statistics | 2026-07-09 |
| 7 | https://en.wikipedia.org/wiki/ACM_SIGOPS_Annual_Technical_Conference | History 1975-2025, the USENIX-to-SIGOPS transition, name change, three-continent rotation | 2026-07-09 |
| 8 | https://www.usenix.org/blog/usenix-atc-announcement + https://www.usenix.org/blog/preserving-legacy-usenix-atc | USENIX's decision to end ATC and preserve its legacy proceedings | 2026-07-09 |
| 9 | https://www.sigops.org/conferences/ | ACM SIGOPS sponsored-conference list placing ATC alongside SOSP, EuroSys, and the SIGOPS workshops | 2026-07-09 |
| 10 | https://atc25ae.usenix.hotcrp.com/ + https://atc25ae.usenix.hotcrp.com/deadlines | ATC '25 Artifact Evaluation HotCRP and its separate post-notification deadline | 2026-07-09 |

## Verified 2026 facts used in skills

- **ATC 2026 is the first ACM SIGOPS Annual Technical Conference**, the continuation of the former
  USENIX ATC under new sponsorship, held **15-18 November 2026** at the **Hyatt Hotel, Shatin,
  Hong Kong** (sources 1, 2, 7). Under SIGOPS the conference rotates among **Asia, Europe, and
  North America** on a three-year cycle (source 7).
- **The submission deadline is early June 2026 (AoE).** Renderings disagree on the exact day —
  one lists **1 June 2026**, another **10 June 2026** — so the precise date is **待核实**; the
  November conference date is a deliberate break from the historical USENIX ATC winter-deadline /
  summer-conference rhythm (sources 1, 2).
- **Two-round, extended-abstract review (new under SIGOPS).** Every submission includes a
  **two-page extended abstract** uploaded with the full paper. **Round 1:** each extended abstract
  is read by **two experienced reviewers** with a broad systems perspective; below-bar papers are
  rejected early. **Round 2:** papers that advance are read in full by **3-4 reviewers**. The
  extended abstract is **for review only and is not published**, and it must stand on its own
  because a reviewer may see only the abstract or only the paper (source 1).
- **Length:** **full papers ≤ 12 pages, short papers ≤ 6 pages**, excluding references and
  appendices but including all text, figures, tables, and footnotes (sources 1, 4).
- **Format:** **two-column**, text block **178 × 229 mm (7 × 9 in)**, **10-point** Times Roman (or
  similar) on 12-point single-spaced leading, A4 or US-letter — the classic USENIX systems format
  (source 1). Which exact template file (the USENIX LaTeX/Word template vs. an ACM equivalent) is
  mandated for the SIGOPS edition is **待核实**.
- **Double-blind review:** author identities are concealed from reviewers and vice versa; authors
  anonymize the PDF and any linked repository, avoid "reference removed for blind review," and cite
  their own prior work in the third person (sources 1, 4).
- **Conditional acceptance + shepherding:** papers the PC selects are **conditionally accepted**,
  with final acceptance subject to revisions approved by a PC member acting as a **shepherd**
  (source 1). A short (about one page) description-of-changes / author-response mechanism supports
  the review (source 1).
- **Broad, practical systems scope:** operating systems, runtime systems, parallel and distributed
  systems, storage, networking, security and privacy, virtualization, hardware-software
  interaction, performance evaluation and workload characterization, reliability, availability,
  scalability, energy and power, and bug-finding/tracing/troubleshooting — systems "of all scales,
  from embedded devices to data centers and clouds," with an emphasis on implementations and
  experimental results (source 4).
- **Deployed Systems / experience track:** USENIX ATC '25 ran a **Deployed Systems Track** whose
  papers describe real-world deployed systems and need **not** present new ideas or results — they
  are judged on practical insight (source 4). Whether the SIGOPS 2026 edition retains this named
  track is **待核实**.
- **Artifact evaluation with three badges:** ATC follows the shared USENIX/SIGOPS scheme —
  **Artifacts Available**, **Artifacts Functional**, and **Results Reproduced** — run by an
  Artifact Evaluation Committee through HotCRP on a separate, post-acceptance schedule (sources 5,
  10). For USENIX ATC '25, **94%** of evaluated artifacts earned Functional and **77%** earned
  Reproduced (source 6).
- **ACM Open Access publication:** ATC 2026 papers publish under ACM's Open Access program; ACM
  approved a **transition subsidy** for 2026 (about **US$250 APC for ACM/SIG members, US$350 for
  non-members**) to bridge from the old USENIX open-access model (sources 7, 9).

## The USENIX-to-SIGOPS transition (honest reading of the moment)

ATC 2026 is the **hinge edition**. USENIX ran ATC as its flagship for about fifty years and
published its proceedings, slides, and talk videos free and open on the USENIX site. Rapid growth
in submissions — reported as more than 350 in 2023, nearly 490 in 2024, and over 630 in 2025 —
together with USENIX's paid-staff cost model led USENIX to **sunset** ATC; a community **"Save ATC"
petition** prompted **ACM SIGOPS** to adopt it, following the earlier precedents of **HotOS** and
**HotStorage** moving from USENIX to SIGOPS. The practical consequences an author must internalize:
the **name, sponsor, publisher, open-access cost model, review structure, and calendar all changed
at once**. Do not carry a pre-2026 USENIX ATC assumption — winter deadline, USENIX proceedings page,
single-round review — into the 2026 cycle without re-checking it against the SIGOPS call.

## No editor-in-chief; open access, now with an APC

Like every conference in this collection, ATC has **no standing editor-in-chief**; its rotating
analogue is the per-edition General/Program Co-Chairs appointed under ACM SIGOPS. Historically
USENIX ATC charged **no APC** (USENIX funded open access from registration); under ACM Open Access
the 2026 edition introduces a **subsidized APC**. Confirm the current APC, waiver, and open-access
terms on the live ACM/SIGOPS pages before advising on cost.

## Still cycle-volatile (verify every year)

- The exact submission deadline (**1 vs. 10 June 2026 unresolved**, 待核实), abstract/notification
  dates, and rebuttal window.
- Whether the two-round extended-abstract model, its reviewer counts, and the "not published"
  rule persist beyond ATC 2026.
- Whether the **Deployed Systems / experience track** continues under SIGOPS (**待核实**).
- The mandated **template file** (USENIX vs. ACM `acmart`/equivalent) for the SIGOPS edition
  (**待核实**).
- Artifact-evaluation timing, the exact badge set and names, and whether AE is single- or
  double-anonymous.
- APC amount, member/non-member split, waivers, and open-access/licensing terms.
- General/Program Co-Chair and AEC-Chair rosters for ATC 2026 (**待核实** — not confirmed to two
  surfaces at access time).
- Any generative-AI authorship/disclosure policy (**待核实**).
