---
name: joe-rebuttal
description: Use after a Journal of Econometrics (JoE) revision request to plan the response letter and revised manuscript — handling technical referee objections on assumptions, asymptotics, and Monte Carlo, and resubmitting through the live official route (note the fee can re-trigger on resubmissions over one year old).
---

# Revision Rebuttal (joe-rebuttal)

## When to trigger

- A JoE decision letter arrived with referee reports and a revision request
- Referees challenge an assumption, a proof step, or the adequacy of the Monte Carlo
- You need a response-letter strategy that satisfies technical specialists
- You are about to resubmit and need to know what the current portal expects

## The JoE revision reality

JoE referees are **specialists** who read methods papers closely, and review is **single-anonymized** (they know who you are). Reports are usually detailed and technical: a missing regularity condition, a gap in an asymptotic argument, a Monte Carlo that does not stress the assumptions, or an under-credited competing method. The editors make the final call after weighing the (minimum two) referees. Treat the revision as **making the theory and simulations airtight**, not as a rhetorical exercise. Note: resubmissions **over one year old** can re-trigger the **USD $75 fee** — budget for it.

## Response-letter strategy

1. **Restate each point in your own words** before answering, so the referee sees you understood it.
2. **Answer technically, with evidence.** For a contested assumption: prove it is primitive, weaken it, or show the result is robust to its failure via Monte Carlo. For a proof gap: supply the missing lemma. For "the simulation is too narrow": add DGPs at the boundary and report size/power.
3. **Point to exactly where in the manuscript** each change lives (section, theorem, table number).
4. **Concede gracefully** where the referee is right; **push back precisely** (with a citation, a counterexample, or a derivation) where they are not. Never hand-wave.
5. **Separate referees:** a per-referee section, plus a short cover note to the editor summarizing the main changes.

## Common JoE referee objections → responses

| Objection | Response |
|---|---|
| "Assumption A is high-level / not verifiable" | Replace with a primitive condition, or verify A for a leading model class |
| "The asymptotic argument has a gap" | Supply the lemma; cite the empirical-process / ULLN tool used |
| "Variance estimator not shown consistent" | Prove consistency or supply a valid bootstrap with theory |
| "Monte Carlo too favorable" | Add heavy-tailed / dependent / boundary DGPs; report size + size-adjusted power |
| "How does this differ from [method]?" | Add an explicit analytic + Monte Carlo comparison; sharpen positioning |
| "Illustration over-claims" | Reframe as a demonstration of the method, not an applied finding |

## Resubmission logistics

- Resubmit through the **live official route**. If the Editorial Express resubmission flow applies, use database `je`; if the route points to Editorial Manager, follow that workflow.
- Check whether the **fee re-triggers** and stage **proof of payment** if the live route requests it.
- Provide a clean revised manuscript plus the response letter; keep the Elsevier formatting and ≤250-word abstract intact.
- Update the reproducible artifact (`run_all`, estimator code, seeds) to match any new Monte Carlo.

## Anti-patterns

- Drafting the response letter before the revised manuscript exists
- Rhetorical answers ("we respectfully disagree") with no derivation, citation, or new simulation
- Conceding a point in the letter but not changing the paper (or vice versa)
- Ignoring one referee because another was more positive — editors weigh all of them

## Output format

```
【Decision】R&R / major / minor
【Per-referee plan】R1: [points→responses]; R2: [...]
【Theory changes】assumptions weakened / lemma added / variance proof
【Monte Carlo changes】new DGPs / boundary cases / size-power added
【Manuscript pointers】where each change lives
【Resubmission】live route checked; fee re-trigger checked? [Y/N]
【Next step】joe-submission preflight on the revised PDF
```
