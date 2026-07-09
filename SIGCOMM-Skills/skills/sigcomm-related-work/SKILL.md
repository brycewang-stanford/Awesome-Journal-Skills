---
name: sigcomm-related-work
description: Use when positioning an ACM SIGCOMM submission against the networking literature — sweeping SIGCOMM, NSDI, MobiCom, CoNEXT, IMC, and SIGMETRICS plus journals, proving each placement via dblp and the ACM Digital Library, distinguishing main-track papers from CCR editorials, handling concurrent work, and keeping self-citation double-blind-safe.
---

# SIGCOMM Related Work

Use this to audit novelty and placement. SIGCOMM is the broad networking flagship, so a paper
is read against the strongest prior work in its exact subarea — and against results scattered
across sibling venues. Reopen the current CFP for concurrent-submission and anonymity rules
before advising.

## Positioning checks

- Separate the **mechanism** you contribute from engineering polish: a new protocol, transport
  signal, forwarding architecture, measurement-driven design, or programmable-data-plane
  technique.
- Sweep the whole networking literature, not just SIGCOMM: the nearest prior work may sit in
  NSDI, MobiCom, CoNEXT, IMC, SIGMETRICS, INFOCOM, or a journal like IEEE/ACM Transactions on
  Networking. A bibliography that cites only SIGCOMM signals a narrow read.
- **Prove each placement.** Verify the venue and year on dblp and the ACM DL before you assert
  it; do not rely on memory for where a famous result appeared.
- Distinguish **main-track proceedings** from **CCR editorial notes** — OpenFlow's famous CCR
  note is not a SIGCOMM conference paper, and citing it as one is a checkable error.
- Handle concurrent and prior versions honestly, and keep every self-citation phrased so
  double-blind review survives.

## Venue-coverage table

| Literature lane | Typical venues | What SIGCOMM reviewers check |
|---|---|---|
| Networking design flagships | SIGCOMM, NSDI, CoNEXT | Whether the nearest deployed mechanism is compared or distinguished |
| Wireless / mobile | MobiCom, SIGMOBILE venues | Whether relevant PHY/mobility work is acknowledged when adjacent |
| Measurement | IMC | Whether the motivating measurement rests on the right prior characterizations |
| Performance analysis | SIGMETRICS | Whether known models/bounds are credited |
| Archival journals | IEEE/ACM ToN, JSAC | Whether classical results are not being rediscovered |

A missing state-of-the-art comparison from the *right* venue is a recognizable SIGCOMM reject
pattern that benchmark strength alone does not repair.

## The misattribution guard

```text
Before citing "X appeared at SIGCOMM YYYY":
  1. Find it on dblp.org/db/conf/sigcomm/  -> confirm the edition and page range
  2. Confirm ACM DL lists it in the SIGCOMM conference proceedings, not CCR editorial
  3. Rule out the sibling: Hedera is NSDI, RED is ToN, BBR is CACM
  4. If unresolved -> mark 待核实 and do not assert the venue
```

## Positioning vignette

A paper proposes a data-center transport that schedules flows in the fabric. Its nearest
neighbors: an earlier SIGCOMM congestion-signal paper (DCTCP), a fabric-scheduling paper in the
same lineage (pFabric), and an NSDI flow-scheduling system that is often confused with it. The
novelty sentence should name all three contrasts — a different signal than the first, a
different scheduling granularity than the second, and a design rather than the deployed-system
framing of the NSDI neighbor — with each venue verified.

## Concurrent-work judgment calls

- Independently concurrent work at another venue: cite neutrally, state the technical
  difference, and avoid priority claims reviewers cannot verify under blinding.
- Your own prior workshop or preprint version: cite in a blind-safe third person and confirm
  the current CFP's stance on overlap before relying on it.
- When a venue's archival status is unclear, declare the overlap in the submission rather than
  gambling on a chair's reading.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Closest venues] <SIGCOMM / NSDI / MobiCom / CoNEXT / IMC / journal>
[Nearest 3 works] <work -> distinction, each venue verified>
[Misattribution risk] <CCR-vs-main-track / sibling-venue traps checked>
[Novelty sentence] <SIGCOMM-ready mechanism contrast>
```
