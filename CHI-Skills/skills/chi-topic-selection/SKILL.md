---
name: chi-topic-selection
description: Use when deciding whether a project belongs at ACM CHI, which of CHI's contribution types it makes, and which reviewing subcommittee should judge it — or whether the work is better routed to UIST, CSCW, DIS, IUI, ASSETS, IMWUT, or TOCHI before any drafting starts.
---

# CHI Topic Selection

CHI accepts almost every topic that touches people and computing, so "is this in
scope?" is rarely the real question. The decisions that actually shape the outcome
are: *which contribution type is this paper*, and *which subcommittee should read it*.
Both are declared at submission time in PCS, and both are strategy, not paperwork —
CHI 2026 rejected roughly three quarters of 6,730 completed submissions, and a large
share of early rejections trace to papers pitched at the wrong reviewer community
inside CHI itself.

## Start with the human, not the system

Ask: **who changes what they do because this paper exists?** A designer picks a
different pattern, a researcher runs a study differently, a developer builds an
interface differently, a policy team understands a user population differently. If no
answer survives scrutiny, the project is an engineering result wearing an HCI costume,
and reviewers will say exactly that. A system with no study can still be CHI-worthy —
but only when the system itself embodies a claim about interaction that others can
build on.

## Name the contribution type before the venue

CHI's own guidance enumerates the contribution types the conference publishes. Force
the project into exactly one primary type; hybrids are fine but one must lead:

| Contribution type (CHI's list) | Typical evidence | Failure mode when mismatched |
|---|---|---|
| Interface artifacts or techniques | Prototype + comparative or usability study | Demo praised, knowledge contribution doubted |
| Understanding users (empirical) | Interviews, surveys, logs, field data | "Interesting but so what for design?" |
| Systems, tools, architectures | Working system + evaluation of enabled tasks | Judged as engineering, not research |
| Methodology | New method + validation against practice | "Who has actually used this method?" |
| Theory | Concepts/models grounded in literature | Read as an essay without operational value |
| Innovation, creativity, and vision | Provocations, envisionments | Dismissed unless framing is explicit |
| Argument | Well-supported position essay | Torn apart if evidence is thin anywhere |
| Validation and replication | Careful reproduction of prior findings | Undervalued unless framed as such |

Source: the "Contributions to CHI" pages carried across recent cycles
(chi2026.acm.org/contributions-to-chi/, checked 2026-07-08).

## The subcommittee decision

PCS asks you to designate up to two subcommittees, and the official guidance
recommends naming two. In the vast majority of cases one of your two choices reviews
the paper; chairs may transfer it only when another subcommittee would clearly review
it more thoroughly. Practical consequences:

- The subcommittee determines your 1AC, 2AC, and reviewer pool — effectively your
  jury. A quantitative-methods paper sent to a design-led subcommittee gets design
  criticism, and vice versa.
- Read the current cycle's "Selecting a Subcommittee" page and match against the
  posted scope *sentences*, not the subcommittee titles. The CHI 2027 list was not yet
  posted at check time (待核实); the CHI 2026 list is the working draft of what to
  expect.
- Pick the second subcommittee as a genuine alternative reading of the paper, not a
  duplicate of the first.

```text
Subcommittee fit test (run per candidate subcommittee):
1. Do ≥3 papers you cite belong to this community?        yes / no
2. Would its typical reviewer accept your method as rigorous
   *by that community's standards*?                        yes / no
3. Does your contribution statement use that community's
   vocabulary without translation?                         yes / no
3× yes = designate. 2 = possible second choice. ≤1 = do not list it.
```

## When CHI is the wrong room

| Center of gravity | Better first target |
|---|---|
| Novel interaction technique, engineering depth, no broad user claim | UIST |
| Collaboration, communities, social platforms as the object | CSCW |
| The designed artifact and design process as the contribution | DIS |
| Intelligence in the interface (recommenders, adaptive UI) | IUI |
| Disability and accessible technology for a specialist audience | ASSETS |
| Sensing, wearables, continuous field deployment | IMWUT / UbiComp |
| Contribution needs 15,000+ words or journal-depth theory | TOCHI, IJHCS |

CHI remains right when the audience is the *broad* HCI community: the paper's lesson
should matter to people who will never build your exact system. Note the calendar
asymmetry: CHI runs one cycle per year (papers due early September), so a missed fit
costs twelve months — the sibling venues above fill the gap between cycles.

## Anti-signals before you commit a year

- Your related-work section cites no CHI, CSCW, UIST, or TOCHI work — you are writing
  for a community you have not read. (Insufficient contextualization, "ADR-Context,"
  was the most-cited assisted desk-reject reason at CHI 2026.)
- The user study exists to decorate a systems result you would publish anyway.
- The contribution is real but 5,000 words would carry it — that is not a defect
  (short papers are welcome), but plan the paper as short instead of inflating it.
- Every plausible reviewer you can imagine works in one narrow specialty — a
  specialist venue will review it better and cite it more.

## Output format

```text
[Human stake] who changes what: <one sentence>
[Contribution type] primary: <type> / secondary: <type or none>
[Subcommittee designations] 1st: <name + fit-test score> / 2nd: <name + score>
[Venue verdict] CHI-first / CHI-viable / route to <UIST|CSCW|DIS|IUI|ASSETS|IMWUT|TOCHI>
[Length plan] short (<5k words) / standard (5-8k) / justify-longer
[Blocking gap] <the one thing to fix before drafting>
```
