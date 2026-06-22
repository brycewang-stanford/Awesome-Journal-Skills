# Live-Check Verification Campaign — Humanities & Social-Science Lane (2026-06)

**Owner lane:** humanities + social science (sociology, communication, education,
geography, history, philosophy, religion, literature, anthropology).
**Explicitly OUT of scope** (owned by parallel agents / other lanes, do not touch):
law, political science, public administration, economics, CS, natural sciences.

## Goal (the "one-month" objective)

Ground out every **live-check** item the source maps currently hedge — the two the
user named, **现任主编 (current Editor[s]-in-Chief)** and **各刊 APC / submission fee**,
plus closely-related volatile specifics (`等`) — across the **19 lane packs** below.

For each verified item:
1. **Verify** the current value against authoritative web sources (≥2 independent,
   prefer the official journal/society page; cross-check news/society announcements).
2. **Backfill** the pack's `resources/official-source-map.md`: add the fact + source
   URL + access date **2026-06-22**.
3. **De-hedge** the `SKILL.md` bodies: replace `待核实 / 需复核 / 检索于…以官网为准 /
   "confirm current editor"` with the date-stamped verified fact, keeping only a light
   "re-verify before submission" reminder (good practice, not a hedge).
4. Where a fact **genuinely cannot** be verified, keep an honest, *narrowed* hedge —
   never fabricate.
5. **Validate** (`run_checks.py --skip-reports --skip-diff-check` + `source_map_audit.py
   <pack>`) and **commit** per pack/batch.

## Method note

`WebFetch` 403s/404s on most publisher sites (SAGE, ASA, OUP, Wiley, T&F behind
Cloudflare). `WebSearch` is the reliable channel: it returns the facts plus citable
authoritative URLs. Verification standard = ≥2 independent authoritative sources agree.

## Backlog & status (19 packs)

| # | Pack | Current Editor(s) — live-check | APC / Fee — live-check | Status |
|---|------|-------------------------------|------------------------|--------|
| 1 | American-Sociological-Review (ASR) | not named (hedge) | $25 processing fee (待核实 amount) | ☐ |
| 2 | American-Journal-of-Sociology (AJS) | not named | $30 submission fee | ☐ |
| 3 | Sociological-Methods-and-Research (SMR) | not named | no fee; Sage Choice APC 需复核 | ☐ |
| 4 | Annual-Review-of-Sociology (ARSoc) | Massey & Waters (re-confirm) | S2O / OA | ☐ |
| 5 | European-Sociological-Review (EurSR) | Bernardi (需复核) | OA APC 待核实 | ☐ |
| 6 | Sociological-Theory (ST) | team 待核实 | $25 fee; OA APC | ☐ |
| 7 | Communication-Research (CR) | masthead 待核实 | no fee; OA APC 待核实 | ☐ |
| 8 | Journal-of-Communication (JoC) | EiCs at access time 需复核 | OUP APC 需复核 | ☐ |
| 9 | American-Educational-Research-Journal (AERJ) | Akiba 2025–2027 (confirm) | SAGE Choice fee | ☐ |
| 10 | Journal-of-Educational-Psychology (JEdPsych) | Kendeou→Young-Suk Kim 需复核 | no fee; APC 需复核 | ☐ |
| 11 | Review-of-Educational-Research (RER) | editors/contact 需复核 | none stated (do not assert) | ☐ |
| 12 | Annals AAG (AAAG) | editors volatile 需复核 | no fee; T&F OA APC 待核实 | ☐ |
| 13 | Progress-in-Human-Geography (PiHG) | Castree (检索于 2026-06) | SAGE APC | ☐ |
| 14 | American-Historical-Review (AHR) | Bradley (需复核) | no APC; OA option 需复核 | ☐ |
| 15 | Mind | team not pinned 需复核 | OUP APC not pinned 需复核 | ☐ |
| 16 | Journal of the American Academy of Religion (JAAR) | editors 需复核 | no fee; OA APC 待核实; CMOS ed. | ☐ |
| 17 | PMLA | editor/term 需复核 | no fee; APC 需复核 | ☐ |
| 18 | American-Anthropologist (AA) | Chin since 2020, 6th yr (transition?) | OnlineOpen APC ~$3,570 待核实 | ☐ |
| 19 | Current-Anthropology (CA) | new EiC eff. 2025-01 (检索于 2026-06) | OA APC 需复核 | ☐ |

## Verified-facts log (filled as the loop runs)

### Batch 1 — sociology cluster (DONE 2026-06-22)

- **ASR** — Editors (2024–2028): **David Cort, Laurel Smith-Doerr, Donald Tomaskovic-Devey, Joya
  Misra** (Misra joined 2026), all UMass Amherst. Fee: **$25** non-refundable, waived for ASA
  student members. Sources: SAGE author-instructions/asr, journals.sagepub.com/editorial-board/asr,
  umass.edu/social-sciences/news/asa-editors. De-hedged source map + asr-submission.
- **AJS** — Editor: **John Levi Martin** (University of Chicago). Fee $30 already cited. Source:
  UChicago masthead + Sociology directory. De-hedged source map.
- **ARSoc** — Co-editors **Douglas S. Massey & Mary C. Waters** (since Aug 2023). OA via S2O
  (library-funded, not author APC). De-hedged source map + arsoc-submission.
- **SMR** — EiC **Felix Elwert** (UW-Madison), confirmed (supersedes older Winship listing).
  No submission fee; Sage Choice OA ~US$3,900+tax. De-hedged source map + smr-submission.
- **EurSR** — EiC **Fabrizio Bernardi** (UNED) confirmed (ECSR+OUP+Wikipedia). No submission fee;
  OA APC set by OUP (live page). De-hedged source map + eursr-submission.
- **Sociological Theory** — **CORRECTED a stale error**: source map had named Iddo Tavory (NYU) as
  *current* editor; he is the **former** editor (tenure ended 2023). Current 2024–2026 co-editors:
  **Vrushali Patil (UMBC), Zine Magubane (BC), Omar Lizardo (UCLA), S. L. Crawley (USF)** — took over
  Aug 2023; next term begins 2027-01-01. Fee $25 already cited. Corrected source map + soctheory-workflow.

Gates after batch 1: `run_checks` green; `source_map_audit` 0 warnings across the 6 packs.

### Batch 2 — communication + education (in progress)

- **CR (Communication Research)** — EiCs **Silvia Knobloch-Westerwick (Ohio State) & Jennifer Gibbs
  (UC Santa Barbara)** (per SAGE crx board). No submission fee; optional OA via Sage Choice.
- **JoC (Journal of Communication)** — four EiCs: **David R. Ewoldsen (Michigan State), Natascha Just
  (U Zurich), Chul-joo "CJ" Lee (Seoul National), Keren Tenenboim-Weinblatt (Hebrew U)**; OUP APC live.
- **AERJ** — confirms source map: EiC **Motoko Akiba (Florida State)** + co-editors Gist, Ke, Luschei,
  Rodríguez, Stewart (2025–2027). AERA newsroom + SAGE Editors' Introduction corroborate.
- **JEdPsych** — **Young-Suk Kim (UC Irvine)** now handles submissions → current EiC (was "incoming";
  Kendeou is prior). No submission fee.
- **RER** — most-recent-known co-editors **Mildred Boveda, Karly Sarita Ford, Erica Frankenberg,
  Francesca López (Penn State)** are the **2022–2025** team; likely rotated end-2025 — needs a focused
  2026 re-check before asserting as current.
