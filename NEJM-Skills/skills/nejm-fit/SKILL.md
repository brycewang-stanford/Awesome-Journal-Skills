---
name: nejm-fit
description: Use this first, before any writing, to stress-test whether a clinical study clears NEJM's bar — practice-changing clinical impact, methodological rigor, and generalizability. Decides NEJM vs Lancet/JAMA vs a specialty journal.
---

# Clinical Significance Fit (nejm-fit)

## Why this is skill #1

NEJM triages **the large majority of submissions to rejection without external review**. The gate is not "is the study sound" — it is **"would this change clinical practice, and is the evidence definitive enough to justify that change."** A well-conducted but narrow study is desk-rejected. Run this before investing in prose.

## When to trigger

- Before drafting, to decide if NEJM is even the right venue.
- When a co-author says "this is an NEJM paper" and you need a sober second opinion.
- When choosing between NEJM, Lancet, JAMA, a specialty journal (e.g., Circulation, Blood, JCO), and NEJM Evidence.

## The three gates (all must hold)

NEJM weighs three things together. A paper passes only if it clears all three:

1. **Clinical importance** — does it address a question clinicians and patients actually face, with an outcome that matters (mortality, major morbidity, function, quality of life — not just a surrogate)?
2. **Methodological rigor** — is the design strong enough that the result is believable and not likely to be overturned (adequately powered RCT, rigorous observational design with confounding addressed)?
3. **Generalizability** — do the findings extend beyond a single center / narrow population to the broad practice community NEJM serves?

A large RCT with a surrogate endpoint can still fail gate 1. A striking finding from one underpowered single-center study fails gates 2–3.

## Significance ladder (weak → strong)

1. **Case report / small case series.** (Weak — correspondence or specialty journal.)
2. **Mechanistic or early-phase finding** without clinical outcomes. (Specialty / translational journal.)
3. **Single rigorous study extending known effects** to a new population. (Borderline — JAMA/Lancet/specialty.)
4. **Definitive RCT or landmark study answering a practice question** with a hard outcome. (Strong.)
5. **Practice-changing trial that resolves a controversy or sets a new standard of care.** (Strongest.)

If you cannot place the work at rung 4+, NEJM is a long shot — be honest with the user and name the realistic target.

## Fatal desk-reject triggers

- Outcome is a **surrogate** (lab value, imaging marker) with no patient-important endpoint.
- **Underpowered** for the primary outcome, or the primary outcome was changed post hoc.
- **Single-center**, narrow population, with no claim to generalizability.
- **Not prospectively registered** for a trial (an ICMJE deal-breaker — see `nejm-study-design`).
- **Over-claiming**: causal language on observational data, or a subgroup result sold as the main finding.
- Incremental over the authors' own prior trial with no new practice implication.

## Venue routing

| Situation                                                          | Recommend                          |
|--------------------------------------------------------------------|------------------------------------|
| Definitive, practice-changing, generalizable RCT/landmark study    | **NEJM** (Original Article)        |
| Rigorous and important, but global-health or broad public-health framing | **The Lancet**               |
| Strong clinical trial/study, large general-medicine audience       | **JAMA**                           |
| Methodologically strong, fits open-science/registration ethos      | **BMJ**                            |
| Important to one specialty, not broad practice                     | **specialty journal** (Circulation, Blood, JCO, …) |
| Solid but not top-tier general impact; pragmatic/methods focus     | **NEJM Evidence** / specialty      |
| Early-phase / mechanism / surrogate only                           | translational or specialty journal |

## Output format

```
【Three gates】 clinical importance / rigor / generalizability — pass or fail each, one line
【Significance rung】 1–5 + one-line justification
【Outcome type】 patient-important / surrogate-only → flag if surrogate
【Fatal triggers present】 [...]
【Recommended venue】 NEJM / Lancet / JAMA / BMJ / specialty / NEJM Evidence
【If staying with NEJM, the single sentence of practice-changing impact】 "..."
【Next】 nejm-study-design (if pass) | reconsider venue (if fail)
```

## Anti-patterns

- **Do not** rationalize a narrow result into "practice-changing" with adjectives — editors discount adjectives.
- **Do not** confuse a statistically significant surrogate endpoint with clinical importance.
- **Do not** let sample size alone stand in for rigor — a large biased study is still biased.
- **Do not** let sunk cost ("the trial took five years") drive the venue decision.
