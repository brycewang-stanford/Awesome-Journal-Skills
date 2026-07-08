---
name: usenixsec-topic-selection
description: Use when deciding whether a project belongs at the USENIX Security Symposium or a sibling venue — routing among USENIX Security, IEEE S&P, ACM CCS, NDSS, and specialty venues (PETS, SOUPS, RAID, WOOT), and confirming the work has the artifact/measurement/systems evidence USENIX Security rewards.
---

# USENIX Security Topic Selection

The most expensive USENIX Security mistake is made before writing: submitting a
paper whose center of gravity is somewhere else. USENIX Security is now USENIX's
flagship summer event (USENIX ATC ended after 2025, leaving Security as the
association's premier venue), and it draws a specific kind of security paper. This
skill decides fit and routes the misfits before a cycle is spent.

## What USENIX Security is especially strong for

The venue rewards security research whose evidence can be **audited and reused** —
a bias reflected in its mandatory Open Science policy and two-phase artifact
evaluation. It is the natural home for:

- Systems and software security with a working artifact (defenses, hardening,
  program analysis, fuzzing, TEE/OS/firmware work).
- Empirical security **measurement** at scale (internet-wide scanning, ecosystem
  studies, abuse and fraud measurement).
- Vulnerability discovery and analysis with responsible disclosure.
- Usable security and privacy with a systems or measurement backbone.
- Applied cryptography and privacy tech evaluated as built systems.

The through-line: a security contribution other researchers can pick up, run, and
extend. If the artifact, dataset, or measurement is the beating heart of the paper,
USENIX Security is likely the right seat.

## The Big-Four routing table (from the USENIX Security seat)

| If the paper is most centrally... | Prefer | Because |
|---|---|---|
| An auditable systems/measurement artifact | **USENIX Security** | Open-science + AE culture rewards reusable evidence |
| Broad security with strong theory/formal framing | IEEE S&P (Oakland) | S&P's remit spans foundational and policy-adjacent security |
| Applied crypto, or a topic in a CCS-strong subcommunity | ACM CCS | Deep applied-crypto and large PC coverage |
| Network/protocol-centered, or wants a specific spring slot | NDSS | Network-and-distributed-systems framing, one annual cycle |
| Privacy-defining (PETs, anonymity, disclosure control) | PETS/PoPETs | Privacy-specialist reviewers |
| Human-subjects / usability-centered | SOUPS | Usable-security expert pool |
| Offense/PoC or exploit-forward | WOOT (or S&P/CCS) | Offensive-research venue |
| Systems contribution with security as an application | OSDI/SOSP/NSDI | Systems PC judges the systems core |

The four flagships heavily overlap; the deciding question is **which committee's
expertise the paper most needs**, not which deadline is soonest. A measurement
paper wants USENIX Security's measurement reviewers; a lattice-crypto proof wants
CCS's or S&P's crypto reviewers. Route by reviewer fit.

## The "is it security research here?" test

Some projects are systems or ML papers wearing a security hat. Apply a subtraction
test: **remove the adversary — does a contribution remain that USENIX Security
reviewers would still value?** If the paper is really a performance result with a
threat-model paragraph bolted on, systems reviewers at OSDI/NSDI will judge the
core better. If removing the adversary collapses the contribution, it is genuinely
a security paper — now pick among the security venues by reviewer fit above.

## Scoping: one paper or two?

USENIX Security's 13-page body enforces focus. Signals a project is oversized:

- Two distinct threat models each with a full evaluation.
- An attack *and* a defense each strong enough to stand alone.
- A measurement study plus a systems tool that only share a dataset.

Splitting usually produces two stronger papers than one crowded one — and with two
cycles a year plus the sibling venues, the calendar rewards the split (see
`usenixsec-workflow`).

## Readiness gate before committing

```text
[ ] The contribution survives the remove-the-adversary test
[ ] There is an artifact/dataset/measurement reviewers could reuse
    (or a defensible Open Science reason there isn't)
[ ] Ethics/disclosure path is clear and, for live work, already moving
[ ] The nearest prior work is at USENIX Security or a Big-Four sibling,
    not a distant field — the reviewer pool will recognize the problem
[ ] The evidence bar (adaptive attacker / base rates / vantage validity)
    is reachable before the target cycle's deadline
```

Fail two or more and either reshape the paper or route it elsewhere before writing.

## Reverify each cycle

- Topic scope statements in the current CFP; committees re-weight subareas yearly.
- Sibling-venue deadlines when routing away (all four flagships run per cycle).
- Whether the current CFP solicits SoK submissions and on what terms (待核实).

## Output format

```text
[Fit verdict] USENIX Security / sibling venue / reshape first
[Subtraction test] contribution remaining after removing the adversary
[Reviewer-fit routing] chosen venue + the committee-expertise reason
[Scope] one paper / split, with the split lines if any
[Readiness] gate items passed n/6 + blockers
```
