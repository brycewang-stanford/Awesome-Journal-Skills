# Clone Triage — 2026-06-20

## Baseline

Command:

```bash
python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 60
```

Pre-batch state:

- Top pair: `PNAS-Skills/skills/pnas-rebuttal` vs `Science-Skills/skills/sci-rebuttal` at 0.799.
- CS conference breadth pairs dominated the rest of the report, with top pairs around 0.799.
- No pair reached the fail threshold of 0.90.

## Actions taken

- Differentiated `pnas-rebuttal` with a PNAS-specific revision ledger for Significance Statement,
  SI Appendix, main figures, and data/code availability.
- Differentiated `sci-rebuttal` with a Science-specific revision packet for main-text claim ladder,
  figures, supplementary materials, cross-disciplinary readability, and scope statement.
- Added clone-audit guardrails to six CS profile nodes that created cross-family false positives:
  SCA, PacificVis, ISMAR, MICRO, ACML, and ICASSP.
- Added 2026-06-20 clone-audit routing notes to
  `Computer-Science-Conference-Skills/resources/exemplars/selection-patterns.md`.

## Post-batch state

Post-batch command result:

- The Science/PNAS rebuttal pair no longer appears at or above 0.75.
- The top remaining pair is `STOC` vs `FOCS` at 0.788.
- All remaining top-60 pairs are inside `Computer-Science-Conference-Skills`.
- No pair reaches the 0.90 fail threshold.

## Triage classification

### Intentional sibling scaffolding

These pairs remain similar because they are adjacent venues that should share
a fit-card structure while being separated by routing rules:

- `STOC` vs `FOCS`
- `PLDI` vs `POPL`
- `BMVC` vs `3DV`
- `NDSS` vs `USENIX Security`
- `CHI` vs `DIS`
- `AISTATS` vs `UAI`
- `MobiCom` vs `MobiSys`
- `SIGGRAPH` vs `SIGGRAPH Asia`
- `CCS` vs `IEEE S&P`
- `NSDI` vs `OSDI`
- `Eurographics` vs `Pacific Graphics`
- `INLG` vs `*SEM`
- `KDD` vs `WSDM`
- `S&P/CCS/USENIX Security/NDSS` cluster
- `HPCA` vs `ISCA`
- `CoNEXT` vs `SIGCOMM`

### Cross-family false positives to keep reducing

These are not true sibling venues; they should be differentiated in future
profile-body passes if they keep dominating the report:

- `CHIL` with `CPAIOR`, `KDD`, `CSCW`, `FAccT`, or `ECML PKDD`.
- `CPAIOR` with `KDD`, `ICAPS`, `CHIIR`, or `AISTATS`.
- `RecSys` with systems or architecture venues such as `SOSP`, `HotNets`, or
  older MICRO-adjacent profiles.
- `VRST` with `ESEM`, and `UIST`/`SIGDIAL` with storage or systems profiles.
- `ICDE` with `ICPR`, `K-CAP`, or `ISWC`.
- `ASE` with `RE`, and `KR` with security venues.

## Next batch rule

Do not chase every 0.76 pair mechanically. Work down the report by node: pick
one venue that appears in many false-positive pairs, add a concrete
venue-specific guardrail, rerun clone audit, and stop when the top report is
mostly genuine sibling scaffolding.
