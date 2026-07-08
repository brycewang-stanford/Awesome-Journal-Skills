---
name: ieeesp-related-work
description: Use when positioning an IEEE S&P (Oakland) paper against prior literature, including coverage across the four security flagships, concurrent-work and arXiv norms, the 40% resubmission-overlap disclosure, verifying venue attribution via dblp and IEEE Xplore, and anonymity-safe self-citation.
---

# IEEE S&P Related Work

Use this when building the positioning sections. Security literature is
scattered across four flagship conferences with staggered deadlines, so
"prior work" at S&P means a moving window across venues — and the PC
contains authors of the papers you are positioning against.

## The coverage lanes an Oakland reviewer checks

| Lane | Where it lives | Typical miss |
|---|---|---|
| Same attack/defense family | S&P, USENIX Security, CCS, NDSS — last ~3 years of each | Citing only "your" flagship |
| The system/protocol being attacked | Its home community (systems, networking, ML, crypto venues) | Attacking a strawman version already fixed upstream |
| Prior SoKs of the area | S&P especially (SoK lane since 2010) | Re-taxonomizing without citing the existing taxonomy |
| Defenses your attack bypasses / attacks your defense stops | Both academic and *deployed* (vendor advisories, OS release notes) | Ignoring deployed mitigations reviewers run daily |
| Measurement baselines | PAM/IMC + the flagships | Claiming novelty for a re-measurement |

The staggered-deadline effect: by any S&P cycle's close, the previous
USENIX Security and CCS programs are public. Reviewers will know the
three-month-old paper adjacent to yours; sweep all four programs' accepted
lists in registration week, not just indexed proceedings.

## Positioning is a delta statement, not a list

For each close neighbor, write one sentence of the form *"X does A under
adversary B; we differ in C, which matters because D."* Two S&P-specific
rules:

- The delta must be a **security** delta — a stronger adversary handled, a
  weaker assumption needed, a class rather than an instance — not only
  performance. "Faster than X" is a systems claim; "works without X's
  root-access assumption" is an Oakland claim.
- Comparisons against deployed defenses state version and date ("bypasses
  <mitigation> as shipped in <OS> <version>"), because deployed defenses
  move mid-review (`ieeesp-reproducibility`).

## Concurrent work and arXiv

Security has an active preprint and embargoed-disclosure culture; collisions
are common. Handle per the current CFP's wording (待核实 each cycle), with
these stable norms:

- Work public after your submission date is concurrent; note it in the
  camera-ready without being forced to claim priority battles in review.
- Your own preprint: check the cycle's anonymity policy before linking
  anything; never cite your preprint in a way that deanonymizes.
- A vendor advisory or incident report covering "your" vulnerability is not
  a research paper, but reviewers expect it acknowledged and differenced.

## The 40% rule creates a disclosure duty

S&P treats a submission overlapping a previously rejected S&P paper by
roughly ≥40% as a resubmission bound by the one-year embargo (2027 CFP,
checked 2026-07-08). When revising a previously rejected paper for a new
cycle, the related-work pass must also cover *your own* prior submission:
what changed, and does the current CFP require declaring the resubmission
(待核实)? Silently resubmitting recognizable work is a chair-level problem.

## Verify venue attribution before citing

Security bibliographies rot: arXiv versions, tech reports, and conference
versions of the same title differ in content and year.

```bash
# For each load-bearing citation:
# 1. dblp is the venue authority for conf/sp and siblings
curl -s "https://dblp.org/search/publ/api?q=<title>&format=json" | jq '.result.hits.hit[].info | {title, venue, year}'
# 2. Cross-check pages/DOI on IEEE Xplore for S&P papers
# 3. Cite the peer-reviewed version; mention the preprint only if content differs
```

Common traps: attacks named after their website (cite the paper, not the
logo site); "S&P" vs "EuroS&P" confusion; workshop versions (e.g., SPW
workshops co-located with S&P) cited as main-conference papers.

## Anonymous self-citation discipline

The CFP requires third-person self-citation. The related-work section is
where most anonymity failures happen: "we extend our prior system [12]"
plus reference [12] identifies the lab. Write "this work extends the
system of [12]" and audit that *the set* of self-citations does not
uniquely fingerprint the group (three papers from one niche lab cited
together often do).

## Output format

```text
[Lane coverage] family / target-domain / SoKs / bypassed-deployed / baselines: ✓/✗ each
[Fresh sweep] last USENIX Sec + CCS + NDSS programs checked on <date>?
[Delta audit] <n> neighbors with security-delta sentences; <n> missing>
[Self-overlap] prior S&P rejection? overlap estimate <n>% vs 40% rule
[Attribution] <n> citations dblp/Xplore-verified; suspicious: <list>
```
