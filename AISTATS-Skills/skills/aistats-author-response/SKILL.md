---
name: aistats-author-response
description: Use when drafting AISTATS author responses or author-reviewer discussion replies under OpenReview, covering text-only discussion, no-link guidance, no revised-paper upload, anonymity requirements, statistician-reviewer pushback patterns, and decision-focused clarification strategy for theory-plus-experiments papers.
---

# AISTATS Author Response

Use this after AISTATS reviews are released. Reopen the current OpenReview instructions and
author-discussion policy before drafting because response mechanics are cycle-specific.

## Triage

- Answer concerns that affect correctness, novelty, statistical validity, clarity,
  reproducibility, or fit for AISTATS.
- Use existing submitted evidence: paper sections, appendices, supplementary material,
  theorem statements, experiments, checklist entries, and code/data descriptions.
- Keep the reply anonymous. Do not reveal institution, authorship, grants, private URLs, or
  repository ownership.
- Treat discussion as clarification, not revision. Do not depend on uploading a revised paper
  or new supplement unless current instructions explicitly allow it.
- If current rules prohibit links, do not use URLs in the discussion. AISTATS 2026
  author-reviewer discussion was text-only and links were not allowed.
- Correct factual errors first, then address requests for missing comparisons, uncertainty
  estimates, proofs, or hyperparameters.

## Drafting pattern

1. State the decision-critical correction or concession.
2. Point to exact submitted evidence.
3. Explain the statistical or theoretical consequence.
4. Promise a camera-ready wording fix only if it does not add unsupported new claims.

## Statistician-reviewer pushback patterns

| Pushback | What it signals | AISTATS-ready fix |
|---|---|---|
| "Assumption A3 seems strong" | The reviewer traced the proof chain | Point to where A3 is verified, weakened, or shown necessary; never dismiss it as standard without a citation |
| "The experiments violate the theorem conditions" | Theory-experiment mismatch spotted | Identify which conclusions survive misspecification and cite the robustness simulation that shows it |
| "Observed rates do not match the bound" | The reviewer compared empirical slopes against theory | Reference the log-log plot, or explain the constant-dominated regime at the tested sample sizes |
| "Comparison with the classical statistical method is missing" | Statistics-literature gap | Anchor to the appendix comparison, or concede and scope a camera-ready clarification |

## Response micro-example

Reviewer objection: the minimax claim hides its dependence on dimension d. Reply skeleton:

1. Concede that the d-dependence appears only in the appendix constant.
2. Quote the exact constant from Theorem 2 so the reviewer need not search.
3. Note that the simulation at d = 100 in Figure 4 follows the predicted scaling.
4. Offer one camera-ready sentence making the dependence explicit in the main text.

## Discussion-phase calibration

- One decision-critical point per reviewer beats exhaustive replies; AISTATS meta-reviewers
  read for whether the central statistical objection was actually resolved.
- Never paste new theorem statements or fresh proofs into the discussion box; sketch the
  argument and anchor it in submitted material only.
- Respond early in the window — AISTATS discussion periods are short and reviewers who reply
  once rarely reply twice.
- Length and formatting norms vary by cycle; recheck the current discussion instructions
  before sending anything.

## Output format

```text
[Priority issue] <reviewer concern>
[Decision dimension] correctness / novelty / statistical validity / clarity / reproducibility
[Draft response] <AISTATS-ready anonymous text>
[Evidence anchor] <paper/appendix/supplement item>
[Forbidden content removed] <links, identity leaks, new unsupported claims>
```
