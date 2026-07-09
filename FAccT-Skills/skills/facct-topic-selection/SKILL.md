---
name: facct-topic-selection
description: Use when deciding whether a responsible-AI project belongs at ACM FAccT or should route to a pure-ML venue (NeurIPS/ICML/ICLR), an HCI venue (CHI/CSCW), a law/policy venue, or an AI-ethics venue (AIES), by testing whether fairness, accountability, or transparency is a first-class contribution and whether the interdisciplinary framing is native rather than bolted on.
---

# FAccT Topic Selection

Decide the venue before drafting. **ACM FAccT — the Conference on Fairness, Accountability, and
Transparency** — is the flagship *interdisciplinary* responsible-AI venue. Its reviewer pool spans
computer science, law, the social sciences, the humanities, and policy, and its defining demand is
that **fairness, accountability, or transparency (FAccT) is a first-class contribution**, not a
fairness paragraph appended to a systems result. A technically strong paper whose real center is a
new model, a new interaction technique, or a doctrinal legal argument — with FAccT concerns merely
gestured at — is respected and then rejected as out of scope.

## The routing question that matters most

The decisive question is rarely "does this touch fairness/AI?" but **"is a fairness, accountability,
or transparency question the actual contribution, and is the sociotechnical framing native?"** FAccT
uniquely rewards work that takes the *social* and the *technical* as inseparable. A paper that would
lose nothing if you deleted the equity framing belongs elsewhere; a paper whose whole point is who
is harmed, who is accountable, or what can be made legible belongs here.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Fairness/accountability/transparency is the contribution; social + technical are entangled | **ACM FAccT** | The interdisciplinary responsible-AI flagship; FAccT concerns are first-class |
| A new model/algorithm whose fairness angle is a secondary evaluation | **NeurIPS / ICML / ICLR** | ML flagships; a fairness metric alone does not make it FAccT |
| A new interaction technique or system; the study is about *use* more than *justice/power* | **CHI / CSCW** | HCI flagships; FAccT wants the accountability/harm question central |
| Primarily doctrinal legal analysis or regulatory design for a legal readership | **Law reviews / policy venues** | FAccT welcomes law, but wants cross-disciplinary reach, not doctrine alone |
| AI-ethics argument aimed at a philosophy/ethics readership | **AIES** and adjacent | Overlapping sibling; FAccT leans empirical + sociotechnical + policy-facing |
| Critical/qualitative/participatory engagement better as a session than a paper | **FAccT CRAFT track** | Participatory and world-building formats live in CRAFT, not the paper track |

## Contribution shapes FAccT rewards

FAccT is genuinely pluralistic — the following are *all* native, and a good program mixes them:

- **Algorithmic fairness / interpretability method** — a new measure, algorithm, or auditing
  technique for bias, recourse, explainability, or transparency, evaluated on real data (the
  fairness-metrics lineage).
- **Empirical audit** — measuring disparate performance or harm in a deployed or commercial system
  across subgroups (the *Gender Shades* lineage).
- **Documentation / accountability infrastructure** — datasheets, model cards, data statements,
  audit frameworks, and impact-assessment tooling that change how the field builds and reports (the
  *Model Cards* / *Datasheets* lineage).
- **Critical / conceptual / position work** — an argument that reframes what the field takes for
  granted about harm, power, or measurement (the *Stochastic Parrots* lineage).
- **Qualitative / sociotechnical study** — interviews, ethnography, or a case study of how a system
  affects an affected community or institution, with sound method.
- **Law & policy** — legal, regulatory, or governance analysis that engages the technical substrate
  and reaches a mixed audience.

## The two sharpening tests

- **Delete-the-equity test:** remove every sentence about fairness, accountability, transparency,
  harm, or power. If a complete, publishable contribution remains, the FAccT framing is decoration
  — route to the ML/HCI/legal home of the surviving core. If nothing coherent remains without it,
  FAccT is right.
- **Mixed-reviewer test:** imagine your paper read by a computer scientist, a lawyer, and a
  qualitative social scientist at once. FAccT-shaped work gives each of them something to hold and
  survives all three; a paper that only one of them can evaluate is usually a sibling-venue paper
  wearing a FAccT title.

## Interdisciplinary rigor, not interdisciplinary gesture

Fit is necessary but not sufficient. FAccT reviewers penalize *thin* interdisciplinarity: a CS
paper that cites one sociology book without method, or a critical paper that name-drops an algorithm
it never engages. Whichever lane you sit in, meet **that lane's** standard of rigor — statistical
care and honest baselines for a method/audit paper; coding schemes, saturation, and reflexivity for
a qualitative paper; doctrinal precision for a legal paper — and then connect it across the divide.

## Cheap reconnaissance before committing

```text
[Scope]   scan the last two FAccT programs (facctconference.org, ACM DL, dblp db/conf/fat) for
          your topic -> several recent papers = a reviewer pool exists; none = opening or mismatch
[Focus areas] can you name a primary + secondary FAccT focus area (algorithm development; data &
          algorithm evaluation; applications; human factors; privacy & security; law; policy;
          critical/humanistic/social-scientific) that genuinely fit? -> if not, reconsider the venue
[Audience] would a lawyer AND a computer scientist both find a contribution? -> that dual pull is
          the FAccT signature; a single-discipline pull points to a sibling venue
```

## Decision procedure

```text
[Who is affected] whose fairness/accountability/transparency changes if the claim holds?
[Contribution type] method / audit / documentation-infra / critical-conceptual / qualitative / law-policy
[First-class check] delete-the-equity test -> does a contribution survive without the FAccT framing?
[Interdisciplinary check] mixed-reviewer test -> do a CS + a law + a social-science reader each hold something?
[Format check] is it a paper, or a participatory session? -> paper track vs CRAFT
[Verdict] FAccT paper track / FAccT CRAFT / sibling venue (NeurIPS/ICML/CHI/AIES/law), one-line reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the verdict
is FAccT, continue with `facct-workflow` for the calendar and `facct-writing-style` for the paper
shape.
