---
name: icsme-topic-selection
description: Use when deciding whether a software-engineering project belongs at IEEE ICSME (maintenance, evolution, reverse engineering, program comprehension, technical debt, refactoring, mining software repositories) or should be routed to ICSE, FSE, ASE, ISSTA, MSR, SANER, SCAM, or an SE journal (TSE/EMSE), and when to use ICSME's Journal-First, Registered Reports, or RENE tracks instead of the research track.
---

# ICSME Topic Selection

Decide the venue before drafting. ICSME — the IEEE International Conference on Software
Maintenance and Evolution — is the field's dedicated home for what happens to software *after*
the first release: maintaining it, evolving it, comprehending it, refactoring it, repaying its
technical debt, and mining the repositories that record its history. A brilliant paper about a
*greenfield* synthesis technique, a novel type system, or a pure ML model is respected and then
rejected as out of scope. The ICSME question is not "is this good SE?" but **"is the paper's
centre of gravity a real maintenance-or-evolution problem?"**

## The routing question that matters most

ICSME overlaps ICSE and FSE (both take maintenance work) and SANER, SCAM, MSR, and ICPC (all
maintenance-adjacent). The decisive test is **which community the paper is arguing with** and
**how central the maintenance lifecycle is** to the contribution — plus which live deadline fits.
A paper whose evidence is a legacy system aging under change, a refactoring that developers must
trust, or a bug that survived years of evolution is natively ICSME; a paper that only *uses*
software as a substrate for a general technique usually belongs elsewhere.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Maintenance/evolution problem is the heart: aging systems, change impact, technical debt, refactoring safety, program comprehension | **ICSME** | The venue built for the post-release lifecycle |
| Broad SE technique or study aimed at the whole field, not specifically maintenance | **ICSE / ESEC/FSE** | General-SE flagships with wider scope and a larger stage |
| The whole method is repository mining and the research question is about mining itself | **MSR** | Purpose-built mining venue (ICSME takes mining *applied to* maintenance) |
| Static/dynamic source-code analysis or transformation is the core machinery | **SCAM** | Co-located with ICSME; deeper source-analysis expertise |
| Reverse engineering / comprehension with a strong tooling or human angle, early-stage | **SANER / ICPC** | Evolution-adjacent siblings with their own communities |
| Testing depth or fault detection is the contribution | **ISSTA / ASE** | Testing/analysis and automation venues |
| Study too long or too deep for the 10-page IEEE budget | **TSE / EMSE** | Journals with no conference ceiling — and the door back via ICSME's Journal-First track |

## Contribution shapes ICSME rewards

- **Maintenance/evolution technique + tool + evaluation on real, evolving systems** — a change-
  impact, refactoring, migration, comprehension, or debt-detection technique, embodied in a tool
  and evaluated on real systems with real change history.
- **Empirical study of how software ages and changes** — mining commit, issue, PR, or release
  history to characterize maintenance practice, defect survival, debt accumulation, or evolution.
- **Reverse engineering / program comprehension** — recovering architecture, models, or intent
  from existing code, with evidence it helps a maintainer.
- **Replication or negative result** (the RENE track's home turf) — re-running prior maintenance
  research on new data and reporting honestly what did and did not reproduce.
- **Technical-debt and refactoring economics** — measuring, predicting, or repaying debt, or
  demonstrating that a refactoring preserves behaviour and pays off.

## The re-label and lifecycle tests

Two quick tests sharpen a borderline verdict:

- **Lifecycle test:** does the contribution only make sense because software *already exists and
  keeps changing*? If you can restate it with no reference to history, maintenance, or evolution,
  ICSME is probably the wrong room — route to ICSE/FSE or a technique venue.
- **Re-label test:** could this be submitted to MSR or SCAM unchanged and read as native there? If
  its heart is mining-for-its-own-sake or source transformation machinery, route accordingly;
  ICSME rewards the maintenance *payoff* of that machinery, not the machinery alone.

## Choosing an ICSME track (not just the research track)

ICSME is unusual in how many doors it opens — pick the one that fits the work's maturity:

```text
[Research track]      a complete maintenance/evolution technique or study, ready now
[Journal-First (J1C2)] a TSE/EMSE paper already accepted (2025-2026 window) not yet conf-presented
[Registered Reports]  a strong protocol whose result is not yet in -> lock the method, review-first
[RENE]                a replication/reproduction on new data, or an honest negative result
[NIER / Visions]      an early idea with an argument but not a full study
[Tool Demo / Data]    a usable tool or a released dataset as the contribution
[Industry]            a practitioner-driven maintenance experience report
```

## Cheap reconnaissance before committing

```text
[Scope]   scan the last two ICSME programs (dblp conf/icsm, conf.researchr.org) for your subarea
          -> 3+ recent papers = a reviewer pool exists; 0 = opening or mismatch
[Citations] is your bibliography majority maintenance/evolution venues (ICSME/SANER/MSR/ICPC/TSE/EMSE)?
          -> majority elsewhere => reviewers read you as a visitor; ground the intro in maintenance first
[Calendar] compare the next ICSME abstract deadline with ICSE/FSE/SANER/journal dates -> route to the
          nearest honest fit rather than idling a year
```

## Decision procedure

```text
[Audience] who acts differently if the claim holds? -> maintainers/reverse-engineers/evolution researchers?
[Claim type] technique / empirical / comprehension / replication / debt-economics
[Lifecycle check] does it depend on software already existing and changing? -> yes = ICSME-shaped
[Sibling check] mining-only -> MSR; source transformation -> SCAM; general SE -> ICSE/FSE
[Track choice] research / journal-first / registered report / RENE / NIER / tool-demo / industry
[Verdict] ICSME <track> / sibling venue / journal-first, with a one-line reason
```

Run this before the writing skills; a wrong venue or wrong-track decision wastes every later step.
When the verdict is ICSME, continue with `icsme-workflow` for the calendar and
`icsme-writing-style` for the paper shape.
