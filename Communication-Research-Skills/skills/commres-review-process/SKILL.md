---
name: commres-review-process
description: Use to understand how Communication Research (CR) evaluates a manuscript — double-anonymized review, editorial screening for quantitative/theory fit, external review, and the requirement that two independent positive reviews back a Revise or Accept decision. Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (commres-review-process)

Knowing how CR screens and decides lets you pre-empt the failure modes before submitting. CR is
**double-anonymized** and is a **quantitative, theory-testing** journal, so it screens for both fit and
methodological rigor.

## When to trigger

- Before submitting, to stress-test fit, rigor, and anonymization
- Deciding whether the contribution is quantitative and theory-testing enough for CR
- Interpreting a decision letter and setting expectations
- Understanding what reviewers are instructed to weigh

## How CR review works

1. **Double-anonymized.** Reviewers do not know the authors and authors do not know reviewers.
   Anonymize the **main document and supplemental materials**; write self-citations in the third
   person (see `commres-submission`).
2. **Editorial screening first.** Manuscripts that are off-scope (qualitative/interpretive for a
   quantitative venue), descriptive, atheoretical, or methodologically weak may be declined without
   full review. CR screens for a **tested communication mechanism**, not a platform description.
3. **External review.** Manuscripts that pass go to expert referees under the double-anonymized model.
4. **Two independent reviews to advance.** CR requires **two independent reviews** to back a **Revise
   or Accept** decision (检索于 2026-06；以官网为准) — a single enthusiastic reviewer is not enough, so
   the paper must satisfy more than one expert at once.
5. **Decision categories**: typically **reject**, **revise and resubmit** (major or minor), or
   **accept** — the final call is the editor's, weighing the reviews.

## Open practices in review

- A **data-availability statement** is expected; **preregistration** (if any) should be noted in the
  cover letter; **open-materials/data** claims must be deposited to be credited (see
  `commres-transparency-and-data`).

## Shape the paper to pass

- Make the **tested mechanism** explicit (avoids the "descriptive / atheoretical" screen-out).
- Defend measurement validity and identification up front — CR reviewers probe both.
- Engage the relevant empirical literatures, including across communication areas.
- Clear ethics/IRB and human-subjects compliance.
- Write to **two** expert reviewers at once: anticipate the strongest objection of each and answer it
  in the design.

## Two gates, two failure modes (calibration anchor, hedged)

| Gate | Who decides | What kills a paper here | Pre-empt by |
|------|-------------|-------------------------|-------------|
| Editorial fit/rigor screen | handling editor / EIC | qualitative for the venue, descriptive, atheoretical, weak measurement | front-loading a tested mechanism + valid measures |
| External expert review | independent referees (≥2 to advance) | weak theory advance, shaky measurement, no mechanism, CMV/confound | answering each referee's strongest objection in the design |

The fit screen is fast; external review is slow and substantive. Referee count, decision wording, and
timeline are volatile — **confirm against the journal's current submission guidelines (待核实)**.

## Worked micro-example: reading a "major revisions" signal (illustrative)

A "major revisions" letter says "the framing effect is plausible but the mediation is not convincing."
This is an **external-review** objection (the tested mechanism), not a fit screen-out — the editor
already judged the topic and design CR-relevant. The path is a sharper mediation test (manipulate or
better-measure the mediator; report bootstrap CIs), not more covariates. Reading it as a call for
controls is the classic misread that loses a winnable R&R — and because CR needs **two** reviewers on
side, you must convince the skeptical second reviewer, not only the encouraging first.

## Anti-patterns

- Submitting a qualitative or descriptive paper to a quantitative venue (fit screen-out)
- Ignoring measurement-validity or common-method-variance concerns reviewers will raise
- Expecting acceptance without revision — most accepted papers go through at least one R&R
- Satisfying one reviewer while ignoring the second (CR needs two on side to advance)
- Leaving identifiers in supplemental materials (breaks double-anonymization)

## Review-risk pass for Communication Research

Treat this skill as an executable review pass, not a prose hint. First lock the communication process,
the measured constructs, the study design, and the inferential claim; then judge whether the
manuscript answers CR's real reader: a quantitatively trained communication scientist who weighs
theory, measurement validity, identification, and effect interpretation.

- **Do the pass:** Turn probable reviewer objections into a ledger with response evidence, manuscript
  location, and which of the two reviewers each must convince.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows so the next agent
  edits rather than rediscovers the issue.
- **Sibling guard:** *Journal of Communication* (all-paradigm), *Human Communication Research*
  (interpersonal), *New Media & Society* (digital). If a sibling owns the contribution, re-route
  before polishing format.
- **Stop condition:** do not give submission-ready advice until `resources/official-source-map.md`
  has been checked and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Fit check】quantitative, theory-testing? any red flags?
【Mechanism】tested mechanism explicit enough to clear the screen? [Y/N]
【Measurement】validity + CMV defended? [Y/N]
【Anonymization】main doc + supplements clean? [Y/N]
【Two-reviewer test】would two independent experts back R&R? [Y/N]
【Realistic outcome】reject / R&R (major/minor) / (rare) accept
【Next】commres-submission (or commres-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — double-anonymized review, two-review requirement, decision categories
