---
name: jfi-rebuttal
description: Use when planning an R&R response letter for the Journal of Financial Intermediation (JFI) — single-blind review where referees know you, often a small number of expert reports, a narrow appeal path, and pushback centered on the intermediation channel. It structures the response; it does not fabricate results.
---

# R&R Rebuttal Strategy (jfi-rebuttal)

## When to trigger

- You received an R&R or a reject-with-encouragement and must reply to referees and the Managing Editor
- War-gaming likely objections before submitting (pre-mortem)

## JFI-specific posture (verified 2026-06-20; re-confirm on the official page)

- Review is **single-anonymized (single-blind)** — referees know who you are, so tone matters and
  gratuitous self-defense reads poorly.
- A paper may rest on a **minimum of one expert reviewer**, so a single decisive report can shape the
  outcome; treat each point as potentially pivotal.
- A formal appeal may be possible under Elsevier's appeal policy, but only one appeal per submission is
  considered and the appeal decision is final. The response letter is still your main instrument; make it
  count rather than relying on later escalation.
- The reviewer is a **banking / financial-intermediation specialist** — answer in the field's terms
  (identification of the intermediary mechanism, sample/bank-panel construction, robustness), not generic
  prose.

## Response-letter structure

1. **Cover note to the Managing Editor** — summarize the 2–4 substantive changes and how the paper is now
   stronger; keep it short.
2. **Point-by-point replies** — quote each referee comment, then respond:
   - **Agree + did it:** state the change and the new exhibit/section/line number.
   - **Agree in part:** scope the change; explain the boundary.
   - **Respectfully disagree:** give evidence (a robustness table, a derivation, a citation), never just assertion.
3. **Summary-of-changes table** — comment → change → location.
4. **Clean revised manuscript** plus a tracked-changes copy.

## Empirical vs. theory rebuttals

- **Empirical (bank/loan-panel):** answer endogeneity/selection challenges with a sharper design, a
  placebo, an alternative sample, or a clustering/inference fix — not hand-waving (see
  jfi-identification-strategy, jfi-data-analysis).
- **Theory:** address generality and assumption objections by stating which results survive a relaxed
  assumption, adding a proposition or a numerical example, or clarifying the proof step questioned.

## Pushback patterns a JFI referee runs, and the credible fix

| Referee line | What it really asks | The JFI-credible fix |
|---|---|---|
| "Demand, not supply" | Does the effect survive within-firm absorption? | Report the firm×time-FE estimate; reconcile the gap with OLS as sorting |
| "The mechanism could be X, not intermediation" | Separate the channels | Heterogeneity by bank capital, relationship intensity, or borrower switchability |
| "One country, one register" | External validity | Frame the register as a laboratory; cite cross-register replications; hedge the claim's scope |
| "The model is a knife-edge case" | Generality | Add a proposition stating which results survive relaxed assumptions, and which do not |
| "Magnitudes look implausible" | Economic size | Convert to aggregate credit terms; benchmark against the lending-channel literature's range |

## A worked reply on the supply–demand point (illustrative)

"The referee asks whether borrower demand drives Table 4. We now estimate the specification with
firm×time fixed effects on the multi-bank subsample (new Table 5): the coefficient falls from −3.0 to
−2.1 (s.e. 0.6) but remains significant, and new Section 5.2 shows single-bank firms exhibit the same
exposure gradient in real outcomes. We interpret the one-third attenuation as borrower–bank sorting, now
discussed on p. 14." Quote, evidence, exact location — no rhetoric, no re-litigation of the question.
Because the appeal path is narrow, prioritize the one or two comments that decide the paper's fate
(usually the identification challenge) and give them new exhibits, not the longest prose. When a referee
proposes an intermediation interpretation you had not considered, test it rather than dismissing it — at
this venue, an added heterogeneity cut often converts a skeptic into an advocate.

## Anti-patterns

- A defensive tone toward a referee who knows your identity
- Promising changes without making them, or burying them where the referee cannot find them
- Treating a single referee's point as ignorable — it may be decisive
- Banking on a later appeal instead of making the revised manuscript and response decisive

## Output format

```
【Editor note】2–4 line summary of substantive changes
【Replies】per comment: agree-did / agree-part / disagree-with-evidence
【Changes table】comment → change → location
【Files】clean + tracked-changes manuscript staged
```
