---
name: ngeo-referee-strategy
description: Use when choosing suggested and excluded referees for a Nature Geoscience submission and pre-empting the objections Earth-science referees are likely to raise. Plans referee handling; does not write the manuscript or the rebuttal.
---

# Nature Geoscience Referee Strategy (ngeo-referee-strategy)

## When to trigger

- The Editorial Manager form asks for suggested / excluded reviewers
- You want to anticipate the objections a Nature Geoscience referee will raise and address them in advance
- A prior manuscript was declined and you are rethinking who reviews it
- You are coordinating the cover-letter referee section (see `ngeo-cover-letter`)

## How Nature Geoscience review works (durable shape)

An in-house editor first triages on **broad interest and Earth-system importance**; only a minority of submissions are sent out. Those that pass go to referees (commonly two to three) who assess both **technical soundness** and **significance/breadth**. A referee can recommend rejection on **interest grounds even when the work is correct** — so your strategy must defend the science *and* the venue fit. Review is **single-blind by default**, with an **opt-in double-blind** route (choose it at submission and anonymise the manuscript accordingly). Resubmission and appeal routes exist (handled in `ngeo-revision`).

## Choosing suggested referees

| Principle                          | Practice                                                          |
|------------------------------------|------------------------------------------------------------------|
| Competent on the method            | Can actually judge your instruments, proxy, or model             |
| Spans the breadth claim            | Include someone from the neighboring Earth-science field you claim to reach |
| Covers the evidence type           | If it is field + model, cover both the observational and modelling sides |
| No conflict of interest            | Not recent collaborators, advisors, or same-institution          |
| Constructive, not partisan         | Known for fair, rigorous reports — not reflexive gate-keeping     |
| Grasps the significance            | Will recognise why the result is broad, not just correct         |

Suggest a small set that *together* can vouch for correctness, the evidence, and breadth. Do not stack suggestions only with subfield insiders — editors may read that as evading the broad-interest test. Consider global diversity of expertise; Earth-system questions often need both a regional expert and a global-perspective referee.

## Choosing excluded referees

- Exclude only with a brief, **professional, factual** rationale (a direct competitor with a conflict, a documented dispute). Editors discount emotional or vague objections.
- Do not over-exclude; a long exclusion list signals defensiveness. Nature journals typically cap the number you may exclude.

## Worked example: a referee slate

Suppose the Article reports a proxy-based ocean-circulation reconstruction whose headline consequence bears on climate sensitivity:

1. **Method judge** — a paleoceanographer who runs the same proxy and can interrogate the calibration and age model.
2. **Modelling witness** — a climate modeller who can assess the data–model comparison and the circulation inference.
3. **Breadth witness** — a climate-dynamics scientist who answers "why Nature Geoscience and not a paleo community journal," i.e. why it bears on a first-order question.

The three-role logic transfers to any subfield: one referee for the measurement or model, one for the neighboring field you claim to reach, one independent senior figure. If you cannot name a credible breadth witness, that is diagnostic — revisit `ngeo-scope-fit`.

## Pre-empting the likely objections (do this in the manuscript, not just the letter)

Anticipate the standard Nature Geoscience referee moves and disarm them in advance:

- **"This is regional / not broad enough."** → Strengthen the broad-interest framing in the opening and cover letter (`ngeo-results-framing`, `ngeo-cover-letter`).
- **"The model is not grounded in observations."** → Show the data–model validation in the main text (`ngeo-methods`).
- **"Uncertainty is not quantified."** → State propagated uncertainty on the headline number (`ngeo-methods`).
- **"Incremental over Ref. [X]."** → Make the qualitative Earth-system advance explicit; cite and differentiate.
- **"Can't follow it without the Supplementary."** → Ensure the main text stands alone (`ngeo-supplementary`).
- **"Over-claimed attribution/impact."** → Calibrate claims to evidence (`ngeo-writing-style`).

## Checklist

- [ ] Suggested referees can judge correctness, the evidence type, AND breadth
- [ ] At least one suggested referee represents the claimed neighboring field
- [ ] Observational and modelling sides both covered if the study is mixed
- [ ] No conflicts of interest among suggestions
- [ ] Excluded referees (if any) have a brief, factual, professional rationale
- [ ] The exclusion list is short (within any journal cap)
- [ ] The manuscript already pre-empts the top objections (breadth, grounding, uncertainty)
- [ ] Cover-letter referee section is consistent with the Editorial Manager form
- [ ] Double-blind opt-in decision made and manuscript anonymised if chosen

## Anti-patterns

- Suggesting only close-network insiders (reads as breadth evasion)
- Excluding referees with emotional or unsubstantiated reasons
- A long exclusion list that signals defensiveness
- Suggesting a recent collaborator (conflict) as an "independent" referee
- Ignoring the breadth or grounding objection and hoping the science alone carries it

## Output format

```
【Suggested referees】N — cover correctness + evidence + breadth?  yes / adjust
【Neighboring-field referee included】yes / add
【Obs + model sides covered】yes / n/a / add
【Conflicts checked】clean / fix
【Excluded referees】N (short) — factual rationale?  yes / fix
【Top objections pre-empted】breadth / grounding / uncertainty / increment / stand-alone / over-claim
【Next】ngeo-submission (enter referees) → later ngeo-revision
```

> Referee counts, exclusion caps, and double-blind mechanics evolve — verify on the official Nature Geoscience author pages (Checked: 2026-07-16).
