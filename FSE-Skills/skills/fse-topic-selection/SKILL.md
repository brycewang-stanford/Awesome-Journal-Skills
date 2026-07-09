---
name: fse-topic-selection
description: Use when deciding whether a software-engineering project belongs at ESEC/FSE or should be routed to ICSE, ASE, ISSTA, MSR, ICSME, or an SE journal (EMSE/TSE/TOSEM), and when distinguishing FSE from its sibling general-SE flagship ICSE by contribution shape, evidence maturity, and the PACMSE journal-style fit.
---

# FSE Topic Selection

Decide the venue before drafting. FSE — the ACM International Conference on the Foundations of
Software Engineering, historically **ESEC/FSE** on its European rotation — is one of the *two*
general software-engineering flagships, alongside ICSE, and the ACM SIGSOFT home for foundational
and empirical SE. Its research papers are PACMSE journal articles, so reviewers read for a
**durable software-engineering contribution**, not a one-conference result. A technically strong
paper whose real lesson is about compilers, PL semantics, or pure ML is respected and then
rejected as out of scope.

## The routing question that matters most

FSE and ICSE overlap heavily in scope and reviewer pool, so the decisive question is rarely "is
this SE?" but **"which SE community and calendar fits this paper now?"** Both welcome techniques,
empirical studies, and human-factors work. Use the finer signals below and the live deadlines to
choose — a strong paper is publishable at either, and the nearer honest deadline usually wins.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Broad SE contribution, empirical or conceptual, ready now, and the next FSE deadline is nearer | **ESEC/FSE** | PACMSE journal-style track; the second general-SE flagship |
| Equally broad, but ICSE's cycle lands sooner or you want its stage | **ICSE** | Sibling general-SE flagship; different calendar and template (IEEE 10+2) |
| Core is *automating* a development task; tool/systems flavor dominates | **ASE** | Automated software engineering is its named center |
| Core is testing, program analysis, or fault detection with depth | **ISSTA** | Deeper testing/analysis expertise, round-based reviewing |
| The whole method is repository mining | **MSR** | Purpose-built co-located conference |
| Maintenance and software evolution focus | **ICSME** | Scope match |
| Study is too long or too nuanced for the page budget | **EMSE / TSE / TOSEM** | Journals with no conference page ceiling; some offer a journal-first path back to an FSE stage |

## Contribution shapes FSE rewards

- **Technique + tool + evaluation on real subjects** — a new analysis, testing, repair,
  synthesis, or recommendation technique, embodied in a tool and evaluated on real systems against
  credible baselines (the CUTE lineage).
- **Empirical study** — mining, controlled experiments, or mixed-methods work that changes what
  the community believes about how software is built or maintained (the flaky-tests lineage).
- **Methodology / measurement validity** — interrogating an instrument the field relies on (the
  "are mutants a valid substitute?" lineage) — a distinctly prized FSE mode.
- **Human and organizational factors** — how practitioners actually use, trust, or abandon tools,
  with sound qualitative method.
- **Foundational or conceptual** — models, theories, or formal underpinnings with a clear SE
  payoff — the "foundations" in the name is not decorative.

## The model-swap and re-label tests

Two quick tests sharpen a borderline verdict:

- **Model-swap test:** if your paper leans on an LLM or learner, ask whether the software-
  engineering lesson survives swapping the model for another. If not, the model is the
  contribution and a PL/ML venue fits better.
- **Re-label test:** could this paper be submitted to ISSTA or ASE unchanged and read as native
  there? If its heart is testing depth or automation machinery, route accordingly; FSE rewards the
  broader SE framing and empirical breadth.

## Evidence maturity, without the ladder cliché

Fit is necessary but not sufficient: the same idea sits at different doors depending on how far
the evidence has come. An observation with an argument but no study is a workshop or vision paper;
a working technique evaluated only on examples you chose needs real subjects before the research
track; a study too deep for the page budget belongs in a journal first. Submitting one step early
earns a polite "promising, but..." and costs a full cycle, because FSE, like its siblings, runs on
an annual rhythm.

## Cheap reconnaissance before committing

```text
[Scope]   scan the last two FSE programs (dblp, conf.researchr.org) for your subarea
          -> 3+ recent papers = a reviewer pool exists; 0 = opening or mismatch
[Citations] is your bibliography majority SE venues (ICSE/FSE/ASE/ISSTA/EMSE/TSE)?
          -> majority non-SE => reviewers read you as a visitor; naturalize the intro first
[Calendar] compare the next FSE deadline with ICSE/ASE/ISSTA/journal dates -> route to the
          nearest honest fit rather than waiting a year for a marginal preference
```

## Decision procedure

```text
[Audience] who acts differently if the claim holds? -> SE developers/testers/maintainers/researchers?
[Claim type] technique / empirical / methodology / human-factors / foundational
[FSE vs ICSE] both fit? -> choose by calendar, community pull, and template preference
[Sibling check] testing depth -> ISSTA; automation core -> ASE; mining-only -> MSR
[Verdict] ESEC/FSE research track / sibling venue / journal-first, with a one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the
verdict is FSE, continue with `fse-workflow` for the calendar and `fse-writing-style` for the
paper shape.
