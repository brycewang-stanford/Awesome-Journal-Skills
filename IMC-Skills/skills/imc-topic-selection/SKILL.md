---
name: imc-topic-selection
description: Use when deciding whether an empirical networking project belongs at ACM IMC or should be routed to SIGCOMM, NSDI, CoNEXT, PAM, USENIX Security, WWW, or a journal, using the measurement-first test, the dataset/vantage-point lens, the ethics-gate check, and the two-deadline calendar.
---

# IMC Topic Selection

Decide the venue before measuring. IMC — the ACM Internet Measurement Conference, sponsored by ACM
SIGCOMM — is the home for work whose contribution is **what it measured about the real Internet and
how**. A technically strong system whose measurement is a supporting evaluation is respected here
and then routed to SIGCOMM or NSDI; a modest technique that reveals something real and new about
the deployed network is IMC-shaped.

## The measurement-first test

Ask: **is the measurement the contribution, or the support?**

- If the paper's lasting value is a **finding about the Internet**, a **dataset/platform**, or a
  **measurement methodology**, it is IMC-shaped.
- If the lasting value is a **new system, protocol, or algorithm** and the measurement merely
  evaluates it, it belongs at a systems venue. IMC will read a systems paper wearing a measurement
  title as out of scope.

The quick check: if you swapped the specific system for another and re-ran the study, would the
*measurement lesson about the network* survive? If yes, it is a measurement paper.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| The contribution is a finding, dataset, or methodology about the real Internet | **ACM IMC** | The measurement flagship; ethics + availability + Replicability culture |
| A new system/protocol/architecture, evaluated with measurement | **SIGCOMM / NSDI** | Systems and networked-systems design flagships |
| A networked-systems design with a strong experimental component | **CoNEXT** | Networking systems and experiments |
| Focused active-measurement / methods work, often network-path or topology | **PAM** | Passive and Active Measurement — a measurement sibling |
| The core is an attack/defense or vulnerability, measurement in support | **USENIX Security / CCS / NDSS** | Security venues; measurement is a method there |
| The core is Web-platform or online-ecosystem measurement with a Web-community fit | **WWW / IMC** | Both plausible; choose by community and calendar |
| Study too large/longitudinal for a conference, or a dataset-first artifact | **A journal (e.g., ToN, CCR) or a dataset venue** | No conference page/scope ceiling; some offer dataset tracks |

## Contribution shapes IMC rewards

- **Internet-wide measurement of an ecosystem** — scanning or platform data revealing how a piece
  of infrastructure is really deployed and configured (the HTTPS-ecosystem lineage).
- **Active measurement of deployed systems** — probing real hosts/networks to quantify a property in
  the wild, done safely (the deployed-TCP-resilience lineage).
- **Longitudinal empirical study** — vantage-point analysis that changes what the community believes
  about how the Internet behaves (the email-security lineage).
- **Methodology / instrument validity** — auditing a measurement input or technique the field relies
  on (the top-lists lineage) — a distinctly prized IMC mode.
- **Dataset / platform contribution** — a reusable dataset or measurement platform with honest
  coverage analysis (the DoS-ecosystem lineage; the Community Contribution Award target).

## The ethics-gate check (before you commit)

IMC's mandatory Ethics section and IRB/disclosure expectations are stricter than most systems
venues. Before choosing IMC, confirm you can clear the gate:

- If the measurement touches human subjects or user data, can you obtain **IRB** approval/exemption
  in time?
- If it is active measurement, can you design it to be **safe** and provide opt-out?
- If it exposes vulnerabilities, will you commit to **responsible disclosure**?

A project that cannot clear the ethics gate is not IMC-ready regardless of fit (`imc-experiments`,
`imc-submission`).

## The two-deadline calendar as a routing input

IMC's two deadlines a year, plus the One-Shot-Revision path, make it unusually forgiving of timing:
if your measurement will be ready for cycle 2 but a sibling venue's single deadline has passed, IMC
may be the nearest honest fit. Compare the next IMC deadline against SIGCOMM/NSDI/CoNEXT/PAM dates
and route to the nearest fit rather than waiting a year.

## Cheap reconnaissance before committing

```text
[Scope]     scan the last two IMC programs (dblp, sigcomm.org) for your subarea
            -> 3+ recent papers = a reviewer pool exists; 0 = opening or mismatch
[Citations] is your bibliography majority measurement venues (IMC/PAM/SIGCOMM-measurement)?
            -> majority systems/security => reviewers may read you as a visitor; frame accordingly
[Ethics]    can you clear the IRB/safety/disclosure gate before the deadline? -> if not, not IMC-ready
[Calendar]  compare the next IMC deadline (two/year) with sibling venues -> nearest honest fit
```

## Decision procedure

```text
[Contribution] finding-about-the-Internet / dataset / methodology / system?
[Measurement-first test] does the network lesson survive swapping the system? -> yes = IMC
[Sibling check] system core -> SIGCOMM/NSDI; attack/defense core -> Security; path/topology -> PAM
[Ethics gate] IRB/safety/disclosure clearable? -> if not, reconsider
[Calendar] nearest honest deadline among IMC's two cycles and siblings
[Verdict] IMC / sibling venue / journal, with a one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the verdict
is IMC, continue with `imc-workflow` for the calendar and `imc-writing-style` for the paper shape.
