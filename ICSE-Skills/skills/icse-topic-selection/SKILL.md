---
name: icse-topic-selection
description: Use when deciding whether a software-engineering project belongs in the ICSE research track or should be routed to FSE, ASE, ISSTA, MSR, ICSME, EMSE/TSE/TOSEM, or an ICSE co-located track such as NIER, SEIP, SEIS, or Demonstrations, based on contribution type, evidence maturity, and audience.
---

# ICSE Topic Selection

Decide venue before writing a single section. ICSE — the IEEE/ACM International
Conference on Software Engineering — is the flagship of the SE research community,
which means its reviewer pool expects a contribution *to software engineering
knowledge*, evaluated against the four posted criteria of the research track:
novelty, rigor, relevance, and verifiability/transparency (ICSE 2027 CFP wording,
checked 2026-07-08). A technically excellent paper whose lesson is about databases,
PL semantics, or pure ML will be respected and then rejected as out of scope.

## The two-question fit test

1. **Who changes their behavior if this paper is right?** If the answer names
   software developers, testers, maintainers, reviewers, build engineers, or SE
   researchers studying them, ICSE is plausible. If the answer names compiler
   writers, DB implementers, or ML-architecture designers, route elsewhere.
2. **Would an SE empiricist accept the evidence?** ICSE's culture demands evidence
   proportional to the claim: real subject programs or projects, credible baselines,
   a threats-to-validity analysis, and (by the open-science policy) an inspectable
   artifact. A motivating anecdote plus a toy prototype fails the rigor criterion
   regardless of the idea's quality.

## Contribution shapes ICSE rewards

- **Technique + tool + empirical evaluation** — the classic shape: a new analysis,
  testing, repair, or synthesis technique evaluated on real programs against real
  baselines (e.g., automated program repair, whose founding ICSE 2009 paper later won
  the ten-year Most Influential Paper award).
- **Empirical study** — quantitative mining, controlled experiments, or qualitative
  interview/survey work that changes what the community believes about practice.
- **Human-factors / developer-experience study** — how practitioners actually use
  (or refuse) tools, with sound qualitative methodology.
- **SE for AI and AI for SE** — testing ML systems, LLM-based SE techniques; the
  fastest-growing lane, and also the one with the fastest-staling related work.
- **Methodology, benchmark, or dataset** contributions when they unlock a research
  area rather than repackage existing data.

## Routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Idea is promising but evaluation is preliminary | ICSE NIER (4 pages + 1 ref page, requires a "Future Plans" section per the 2027 call) | NIER reviews vision, not completed evidence |
| Contribution is a deployed industrial experience | ICSE SEIP | Reviewed on relevance to practice, not research novelty |
| Contribution is the tool packaging or a reusable dataset | ICSE Demonstrations / Data Showcase | Purpose-built venue with interactive review |
| Societal impact of software is the point | ICSE SEIS | Dedicated reviewer pool |
| Testing/analysis is the core, SE framing thin | ISSTA | Deeper testing expertise, same community |
| Automation of a development task, systems flavor | ASE | Sibling flagship, tool-centric |
| Repository mining is the whole method | MSR | Purpose-built co-located conference |
| Maintenance/evolution focus | ICSME | Scope match |
| Study too long or too nuanced for 10 pages | EMSE, TSE, TOSEM | No page ceiling, journal-first return path to ICSE |
| Already published at TSE/TOSEM/EMSE | ICSE Journal-first (2027 window: journal acceptance between Oct 11, 2025 and Oct 10, 2026) | Presentation slot without re-review; secondary studies excluded |

## Timing reality for the current cycle

The ICSE 2027 research-track deadline (abstract June 23, submission June 30, 2026,
AoE) has already passed as of 2026-07-08, and the 2027 call posts a **single
submission cycle** — a departure from the two-cycle model ICSE ran in 2025 and
2026. So "just aim for the next ICSE window" now means roughly a year of waiting.
That makes routing honesty cheaper than it used to be: FSE, ASE, ISSTA, and the
journals all have nearer deadlines, and a journal-first acceptance can still put
you on the Dublin stage.

## Evidence-maturity ladder

Fit is necessary but not sufficient; the same idea belongs at different ICSE
doors depending on how far the evidence has come. Grade honestly:

| Maturity rung | You have... | Right door now |
|---|---|---|
| Insight | An observation and an argument, no system or study yet | Workshop or NIER; write the "Future Plans" section the NIER call requires |
| Prototype | A working technique, evaluated on examples you chose | NIER, or hold one cycle and build the real evaluation |
| Evidence | Real subjects, credible baselines, statistics, threats analysis, artifact | Research track — the four criteria are all satisfiable |
| Deployment | Adoption data from practice, weaker research novelty | SEIP, whose reviewers weigh practice lessons over novelty |
| Archive-grade depth | More study than 10 pages can hold | TSE/TOSEM/EMSE first, then journal-first back to the ICSE stage |

The costly mismatch is submitting one rung early: research-track reviewers
reject prototypes politely ("promising, but..."), and the year lost to a
single-cycle calendar is the real price. One rung of patience is usually one
rung of acceptance probability.

## Anti-patterns that predict rejection

- **Venue shopping downward**: a paper rejected from a PL or ML venue, resubmitted
  to ICSE without re-framing for the SE audience. Reviewers detect the foreign
  citation graph immediately.
- **Solution looking for a problem**: no evidence any practitioner or researcher
  has the pain the tool cures — fails the relevance criterion.
- **Benchmark-only novelty**: a known technique run on a new dataset with no new
  question answered.
- **Scope camouflage**: renaming an ML contribution "SE for AI" without any
  engineering question. Ask: if the model were swapped, would the SE lesson survive?

## Reading the room before committing

Two cheap reconnaissance moves sharpen the verdict. First, scan the last two
editions' accepted-paper titles (ICSE program pages, dblp) for your exact
subarea: three or more recent acceptances means a reviewer pool exists;
zero may mean either an opening or a scope mismatch — the exemplars in
`resources/exemplars/library.md` help tell which. Second, check where the
papers you cite most were published: if your own bibliography is majority
non-SE venues, ICSE reviewers will experience your paper as a visitor, and
the introduction must do extra naturalization work before the fit test
passes.

## Decision procedure

```text
[Audience] who acts differently if the claim is true? -> SE actors? yes/no
[Claim type] technique / empirical / human-factors / benchmark / methodology
[Evidence maturity] complete + real subjects? -> full track
                    promising + partial?      -> NIER or workshop
                    industrial + deployed?    -> SEIP
[Deadline math] next ICSE window vs FSE/ASE/ISSTA/journal calendars
[Verdict] ICSE research track / co-located track / sibling venue + one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step.
When the verdict is ICSE, continue with `icse-workflow` for the calendar and
`icse-writing-style` for the paper shape.
