---
name: rt-simulated-referee
description: Use to rehearse peer review before submitting to a named journal or conference — a calibrated Associate Editor desk-screen plus 2–3 independent referees writing on the venue family's actual review form (NeurIPS-style, ARR, economics, management, clinical, natural-science flagship, Chinese journals), a separate verifier that drops unfair concerns, and an AE synthesis with a decision band and a prioritized, skill-mapped fix list. A rehearsal that predicts the attack surface; it does not replace real review.
---

# Simulated Referee Panel (rt-simulated-referee)

Stage 2 of the pre-submission pipeline (`rt-submission-readiness`). It runs the
substantive gauntlet before a real referee does. Full protocol:
[`simulated-referee.md`](../../resources/shared/submission-readiness/simulated-referee.md);
forms: [`review-forms.md`](../../resources/shared/submission-readiness/review-forms.md);
a worked report:
[`worked-example-referee-report.md`](../../resources/shared/submission-readiness/worked-example-referee-report.md).

## When to trigger

- After stage 0–1 of `rt-submission-readiness` (mechanics clean or known).
- When the author asks "what will referees say?" or "is this good enough for <venue>?"
- Before choosing between two venues: run the panel calibrated to each.

## Calibrate first (this is what makes it realistic)

1. **Family and form** — map the venue to form A–G in `review-forms.md`; the target
   pack's review-process / referee-strategy skill overrides it where they differ.
2. **Bar** — selectivity, desk-reject reality and mechanics from the pack's
   `resources/official-source-map.md`; what this venue's referees attack from
   `*-referee-strategy` and the shared
   [`reviewer-objection-checklist`](../../resources/shared/empirical-methods/reviewer-objection-checklist.md).
3. **Lenses** — the family's three lenses (e.g. economics: identification · contribution ·
   inference; ML: soundness/evaluation · novelty · clarity/reproducibility; clinical:
   design · statistics · reporting/ethics).
4. **Preflight report** — attach `preflight.json` so referees skip mechanics.

## Protocol

1. **AE desk-screen** — scope, general interest at this venue's bar, fatal-flaw scan,
   delta vs. closest work → desk-reject risk. Stop if it is a clear desk reject, and say why.
2. **Independent referees** — one subagent per lens with the manuscript *file*, the bar,
   the form and the preflight JSON, and nothing about the other referees. Each fills the
   form, then lists major concerns with location, mechanism, fix and owning skill.
3. **Verification** — a separate verifier tries to refute each major concern against the
   text: `kept` (real, specific, addressable), `downgraded` (real but minor), or `dropped`
   (misreading, already answered in the paper, or not actionable). Quote the line either way.
4. **AE synthesis** — decision band in the family's vocabulary (e.g. ARR: Findings vs
   Conference; economics: reject / major / minor) plus the 1–3 decisive issues.
5. **Skill-mapped fix list** — each decisive issue → pack skill + concrete action (and the
   execution-bridge call when it needs a re-run).

## Worked vignette

*Illustrative, from the repository's benchmark fixture `jf-corporate-did` (seeded copy).*
Calibrated to The Journal of Finance, form C. R1 (identification) flags that the
staggered state-level shock is estimated with a two-way fixed-effects regression and no
heterogeneity-robust estimator (§4, Table 2). The verifier keeps it: the paper has no
Callaway–Sant'Anna or Sun–Abraham check, and early-versus-late comparisons are possible
with these cohorts. R2 says "the contribution over Rajan (2005) is unclear". The verifier
drops it because §1, paragraph 4, states the delta explicitly. The AE band is *major
revision*. The decisive issue is R1, owned by `jf-identification`, and the fix is to run
`callaway_santanna` and `bacon_decomposition` through the execution bridge and report
the event study.

## Hard rules

1. **Calibrate from the pack + source map + the family's form**, never generic.
2. **Independence**: referees do not see each other's drafts; the verifier is not a referee.
3. **Verify before reporting** — every kept concern quotes its location.
4. **Map every decisive issue to a skill + execution bridge.**
5. **Don't soften to please, don't invent to look rigorous** — a clean paper can come back
   with no major concerns, and that is a valid result.
6. **It's a rehearsal** — a decision *band*, never an acceptance probability.

## Output format

```text
【Venue / family】… / form A–G (calibrated YYYY-MM-DD)
【Desk-screen】send out / desk reject — reason; risk low/med/high
【Referee forms】R1 … scores per form · R2 … · R3 …
【Verification】n concerns → kept k · downgraded d · dropped x (reasons)
【Decision band】… (family vocabulary)
【Decisive issues (1–3)】each: location · why it decides · owner skill · concrete fix
【Secondary issues】…
【Author action plan】ordered; tie each to a skill + tool
【Calibration caveats】where the simulation is uncertain
```

Next: fix the decisive issues, then stage 3 (polish) of `rt-submission-readiness`;
after a real decision, `rt-response-to-referees`.
