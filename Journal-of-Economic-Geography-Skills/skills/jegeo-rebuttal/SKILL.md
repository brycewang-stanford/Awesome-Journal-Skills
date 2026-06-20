---
name: jegeo-rebuttal
description: Use when a Journal of Economic Geography (JEG) decision letter arrives and you must plan a revision and response that satisfies a cross-disciplinary referee pair. Structures the rebuttal; it does not invent results or concede the core claim.
---

# Rebuttal Strategy (jegeo-rebuttal)

## When to trigger

- An R&R or major-revision letter arrived and you must triage the reports
- The two referees pull in opposite directions — the economist wants more identification, the geographer wants more mechanism/context
- A referee asks for spatial work (different scale, weight matrix, spillover analysis) and you must decide how far to go
- You need a response letter that reads as responsive to *both* communities and to the editor

## Read the panel before you write a word

At JEG the reports almost always come from **both communities**, and the most common rebuttal failure is answering the referee you understand and brushing off the other. Before drafting, classify every comment by where it comes from and what it really wants:

| Comment type | Likely source | What it actually demands |
|--------------|---------------|--------------------------|
| "not identified / selection / weak IV" | economist | a design fix or honest bound, not more prose |
| "inference overstated / spatial correlation" | economist | Conley SEs / corrected clustering |
| "where is the geography / just a fixed effect" | geographer | place made analytically central; mechanism in prose |
| "no mechanism / no theory it speaks to" | geographer | a conceptual frame the result engages |
| "wrong scale / MAUP" | either | re-estimate across scales; justify the unit |
| "over-formalized / flattens real places" | geographer | interpretation and context, not more math |

## Drafting the response

1. **Open with the editor's framing.** Restate the decision's main concerns in one paragraph and how the revision addresses them — editors at JEG weigh whether you bridged both reports.
2. **Point-by-point, grouped by theme**, not strictly by referee, so a fix that answers both communities is shown once and credited to both.
3. **Quote each comment, then answer with evidence** — the new table/map/SE, with a precise location ("now Section 4.2, Figure 3"). Show, do not promise.
4. **Where you decline, decline with a reason** — a substantive argument or an honest scope limit, never silence. Declining is acceptable at JEG if argued; ignoring is fatal.
5. **Protect the core claim.** Concede the bounded points; do not let an accumulation of small concessions dissolve the contribution.

## The cross-disciplinary balancing act

- A change that pleases the economist (more formalism, more controls) can provoke the geographer ("now even more black-box") — when you add machinery, add the matching mechanism/interpretation so both reports stay satisfied.
- When the two referees genuinely conflict (e.g., one wants the model expanded, one wants it simplified), **surface the tension to the editor** and propose a resolution rather than silently siding with one.
- Re-run the spatial robustness a referee requested *honestly* — if a different scale or W weakens the result, report the bounded version; JEG referees reward candor over a defended asterisk.

## Checklist

- [ ] Every comment classified by community and by what it actually demands
- [ ] Response opens with the editor's framing and the bridge across both reports
- [ ] Point-by-point, each comment quoted then answered with located evidence
- [ ] Added machinery is paired with added mechanism/interpretation (both sides stay satisfied)
- [ ] Genuine referee conflicts surfaced to the editor with a proposed resolution
- [ ] Declines are argued, never silent; core claim protected from concession creep
- [ ] Requested spatial checks (scale/W/spillover) re-run honestly and reported even if weakening

## Spatial requests need a decision rule

Referees at JEG often ask for additional *spatial* work — another scale, a different weight matrix, a spillover model, a finer unit. Decide each with a rule, not reflexively:

- **Do it now** if the request targets a load-bearing assumption (the scale the headline depends on, the inference that could be overstated). Re-run it honestly and report even an unfavorable result.
- **Argue the decline** if the request would not change the conclusion or rests on a misreading of the design — show why, with a small bound or a logical argument.
- **Offer partially** when a full request (e.g., re-geocoding everything at a finer resolution) is disproportionate; provide a targeted version that answers the underlying worry.

Reporting a bounded result after a requested spatial check is a strength signal at JEG; quietly dropping the check or reporting only the favorable version is the fastest way to lose the editor's trust on resubmission.

## Anti-patterns

- Answering the economist's report thoroughly and waving off the geographer's, or vice versa
- Promising changes ("we will consider...") instead of showing the revised exhibit
- Adding controls/formalism to satisfy one referee while ignoring the mechanism objection from the other
- Silently ignoring a comment you find unreasonable instead of arguing the decline
- Letting many small concessions erode the central spatial contribution
- Reporting only the favorable scale/W after a referee asked you to test alternatives

## Worked vignette (illustrative)

A major-revision letter has an economist referee demanding the agglomeration elasticity be estimated structurally rather than reduced-form, and a geographer referee warning that "more modeling will bury the regional story." These pull in opposite directions. The losing move is to side silently with one. The winning move: add the structural estimate the economist wants, but pair it in the *same revision* with a tightened mechanism paragraph and a map that keeps the regional story visible for the geographer — then, in the response letter, name the tension explicitly to the editor and explain how the revision serves both. If the structural estimate moves the headline number (say from 0.08 to 0.06, illustrative), report it honestly; a bounded, candid number survives a JEG panel better than a defended original.

## Editor-facing framing (often decisive)

JEG editors sit on the bridge and weigh whether your revision reconciled two reports rather than placating one. Make their job easy: open with their letter's framing, show in one paragraph how the revision addresses the cross-disciplinary tension, and where the referees conflict, propose the resolution rather than forcing the editor to adjudicate. A response that visibly *bridges* the two reports is the strongest signal you understood what JEG is.

## Output format

```text
【Journal】Journal of Economic Geography
【Skill】jegeo-rebuttal
【Decision】R&R / major / minor
【Economist-report fixes】comment → located evidence (done/declined+reason)
【Geographer-report fixes】comment → located evidence (done/declined+reason)
【Conflicts surfaced to editor】tension + proposed resolution
【Core claim status】protected / adjusted (how)
【Next step】resubmit via ScholarOne; route new bottlenecks through jegeo-workflow
```
