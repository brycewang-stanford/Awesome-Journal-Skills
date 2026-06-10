---
name: icml-author-response
description: Use when drafting ICML rebuttals and reviewer-author discussion replies under OpenReview double-blind constraints, where authors respond after initial reviews, reviewers may then have one additional discussion round, no revised paper can be uploaded during the period, and responses must stay anonymous. Use to triage objections by soundness, originality, significance, clarity, ethics, and reproducibility for the AC.
---

# ICML Author Response

Use this after initial ICML reviews arrive. The response should clarify and correct; it cannot rely
on uploading a revised paper during the feedback period.

## ICML response model

ICML 2026 author instructions state that authors can respond after initial reviews, that reviewers
see those responses after the response period, and that reviewers and authors may then have one
additional communication round. Responses must remain anonymous and should not contain
non-anonymized URLs, personal websites, or shortened URLs. Reviewer instructions tell reviewers to
explain whether the rebuttal changed their final recommendation.

## Triage logic

- Prioritize objections that affect soundness, originality, significance, clarity, ethics, or
  reproducibility.
- Answer the AC's likely decision question, not every minor reviewer note.
- Treat contradictions between reviewers as a chance to give the AC a clean synthesis.
- Use new analyses sparingly and only to clarify an existing claim.
- Keep all links anonymous and policy-compliant. Reviewers are not expected to follow external URLs
  in responses.

## Drafting pattern

1. Open with the central correction or concession.
2. Refer to exact paper sections, appendix items, figures, tables, or supplement files.
3. State what will change in camera-ready only if the paper is accepted.
4. Maintain a professional, concise tone.
5. Avoid identity leakage, score arguments, and broad promises.

## Objection-to-response routing

ICML gives one response window plus one discussion round, so spend words on what an AC can quote, not
on every minor note.

| Reviewer objection | Best ICML response move |
| --- | --- |
| "Assumptions do not match the experiments" | Concede the regime, point to the in-regime figure, state the camera-ready clarification |
| "Missing tuned baseline" | Supply a single decisive table row from a feasible run |
| "Unclear novelty vs concurrent work" | Restate the one-line technical delta and the appendix PDF |
| "Reproducibility unclear" | Cite the exact supplement command and seed |

## Worked vignette: defending the optimizer paper

Reviewer 2 says the convergence proof assumes bounded variance that ImageNet training violates. The
strongest response opens with the concession, narrows the theoretical claim to the stated regime,
adds a small plot showing the rate still tracks empirically where assumptions hold, and promises only
a camera-ready wording fix. It does not argue the score or upload a revised PDF, both of which the
ICML response model disallows.

## Output format

```text
[Priority issue] <reviewer/AC concern>
[Decision dimension] soundness / originality / significance / clarity / ethics / reproducibility
[Draft response] <ICML-ready anonymous text>
[Evidence anchor] <paper/appendix/supplement item>
[Discussion follow-up] <one possible reply if reviewer pushes back>
```

