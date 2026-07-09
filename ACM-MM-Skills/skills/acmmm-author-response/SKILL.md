---
name: acmmm-author-response
description: Use when drafting the ACM MM (ACM Multimedia) rebuttal — turning multiple anonymous reviews into one focused, anonymous response that fixes factual errors first, adds small confirmatory cross-modal results, concedes calibratedly, and stays inside policy (anonymous, no new external links), written for the area chair who decides.
---

# ACM MM Author Response

Use this to write the ACM Multimedia rebuttal. It is **optional and anonymous**, it must not
add new external links, and its real audience is the **area chair** who will weigh it against
the reviews in discussion.

## Triage before writing

Sort every review point into one of three buckets:

| Bucket | Example | Response |
|---|---|---|
| Factual error | "No ablation of the fusion" (there is one, in §4.3) | Point to it precisely; this is your strongest move |
| Fixable gap | "Missing a late-fusion baseline" | Add the small result if you can run it in time |
| Judgment call | "The delta is incremental" | Reframe the significance briefly, or concede narrowly |

Lead with the factual corrections — they are the points an AC can verify and act on fastest.

## Structure for the AC

Write for a reader who is skimming several rebuttals. Make it navigable:

```text
[R1, R2 shared concern: fusion not shown to matter]
  -> Table A (new): leave-one-modality-out; audio-text term = +X of the +Y total gain.
[R1 factual: "no user study"]
  -> §5 reports a user study, N raters, agreement kappa; see supplement S3.
[R3 judgment: "incremental over late fusion"]
  -> Our gain over the late-fusion baseline is in Table 1; the mechanism (Table A) is the novelty.
[R2 request: clarify synchronization assumption]
  -> Conceded; we will state it explicitly in §3 (one sentence).
```

Group shared concerns once; do not repeat the same answer per reviewer.

## Small confirmatory results

- Add only results you can actually produce before the deadline — a leave-one-modality-out
  ablation, one requested baseline, or a small user-study extension.
- Describe new numbers in text/tables **inside** the rebuttal; you cannot add a link to an
  external file, and you cannot add pages to the paper.
- Do not promise experiments you cannot show; an AC discounts unbacked promises.

## Calibrated concessions

Conceding a fair minor point *raises* credibility on the points you contest. State clearly
what you will change (a sentence, a clarified assumption, a moved figure) and why the core
claim survives it.

## Policy guardrails

```text
Anonymous: no author names, institutions, or identifying links.
No new external links: results go in the rebuttal text/tables, not a URL.
No scope change: you cannot rewrite the contribution or add pages.
No reviewer-targeting: never argue a reviewer is unqualified or try to identify them.
```

## Length and format discipline

- Keep the rebuttal tight and scannable; an AC reading many responses rewards structure over
  volume, and a wall of text buries your best point.
- Put new evidence in a small **in-line table**, not prose — a reviewer can check a table in
  seconds.
- Respect any length limit the cycle sets, and do not try to smuggle in a link to sidestep it.

## Rebuttal skeleton by review type

```text
Strong-reject-on-a-misreading:  correct the fact FIRST, with an exact section/figure pointer.
Borderline-wants-a-baseline:    add the baseline in a mini-table; state it is now in the paper plan.
"Fusion is incremental":        show the mechanism ablation (the term that carries the gain).
"Subjective claim unproven":    report the user study's N, agreement, and result inline.
Fair-minor-point:               concede in one sentence and say exactly what changes.
```

## Tone

Precise and non-defensive. Address the reviewer's underlying concern, not their wording; a
rebuttal that reads as annoyed helps the negative reviewer more than you.

## Output format

```text
[Factual corrections] <ordered, with exact pointers>
[New results] <ablation/baseline/study added in-rebuttal>
[Concessions] <narrow, with the fix>
[Contested] <judgment points, reframed>
[Policy check] anonymous / no new links / no scope change — pass or fix
```
