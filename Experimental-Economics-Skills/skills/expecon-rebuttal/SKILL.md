---
name: expecon-rebuttal
description: Use when responding to a revise-and-resubmit or referee report for an Experimental Economics (ExpEcon) manuscript — including when a referee demands a new treatment, more sessions, or raises a deception/power concern. Plans the response; it does not run the new analysis.
---

# Rebuttal Strategy (expecon-rebuttal)

## When to trigger

- An R&R or rejection arrived and you must decide what to concede, contest, or re-run
- A referee asks for a **new treatment or more sessions** — the costliest and most common ExpEcon request
- A reviewer raised a **deception** or **power/inference-unit** concern that could be decisive
- Two referees disagree, or the two editors' priorities differ, and you need a coherent plan

## The ExpEcon revision reality: new data is on the table

Unlike journals where revisions are textual, an ExpEcon R&R often requires **collecting new data** — an added control treatment, more matching groups for power, or a robustness condition. Plan the response around that fact.

1. **Triage every comment** into: (a) **new data needed** (new treatment / more sessions), (b) **re-analysis** (correct inference unit, MHT correction, new test), (c) **clarification** (already in the paper, surface it), (d) **respectful disagreement** (with evidence). Most letters are mostly (b)–(c); isolate the (a) items because they set the timeline and budget.
2. **Address the gate concerns first and decisively.** A deception worry is existential: either prove the procedure is not deception under the ESA definition, or re-run without it — there is no middle path. A power/unit concern: re-analyze at the session/matching-group level and report MDE; if truly underpowered, run additional sessions rather than argue.
3. **For each new-data request, decide and justify.** Run it if it sharpens identification or power; if not, explain precisely why the existing design already answers the question (and offer a cheaper analysis that addresses the underlying worry). Never silently ignore a request for a treatment.
4. **Re-deposit the package.** New sessions mean updated data, instructions, and z-Tree/oTree code in the repository; keep the replication deposit in sync with the revised paper.

## Triaging the common ExpEcon requests

| Referee request | Default response | Cost |
|-----------------|------------------|------|
| "Add a control treatment that isolates X" | usually run it — it is the cleanest answer | new sessions |
| "Underpowered / wrong inference unit" | re-analyze at group level; add sessions if MDE not met | re-analysis ± data |
| "Could be deception / demand effects" | prove non-deception per ESA definition, or re-run | possibly fatal |
| "Comprehension/confusion confound" | report pass rates; re-analyze excluding failers | re-analysis |
| "Why not JEBO/GEB?" | sharpen the methods contribution in framing | text only |
| "More structural estimation" | add if it identifies a parameter; else decline with reason | analysis |

## Writing the response letter

- **Point-by-point, quote-then-respond.** Reproduce each comment, then state the change, the location (section/table/figure), and the new result. Editors and referees verify against the manuscript.
- **Lead with what you did, not why the referee was wrong.** Even when contesting, open with the action taken or the evidence, in a collegial register.
- **Report new numbers honestly.** If a new treatment weakened the effect, say so and interpret it; an experimentalist audience values the clean result over the convenient one.
- **Separate primary from exploratory** in everything you add, mirroring the pre-registration logic.
- **Mind the two-editor structure.** Where referees conflict, address both and let the response help the editors converge; do not pick one referee and ignore the other.

## Worked vignette (illustrative)

A referee says a coordination-game result "might be a demand effect — subjects guessed the hypothesis." Three moves: (1) note the **abstract/neutral framing** already used (no leading language — quote the instructions); (2) report the **post-experiment belief question** showing subjects did not infer the hypothesis; (3) if still unconvinced, add a treatment with an obfuscated cover task and show the effect persists (illustrative: 0.7 SD, unchanged). The letter leads with these three actions, not with "the referee is mistaken," and updates the instructions and data in the repository to match.

## Budgeting the new-data round

An added treatment is not just bench cost — it is a *timeline* the editors will weigh. Before committing, estimate: sessions needed for the new arm at the group-level power you must hit, lab availability, IRB amendment time, and re-deposit effort. If a requested treatment is genuinely infeasible, say so explicitly and offer the strongest available substitute (a re-analysis, a bound, or a focused robustness condition) rather than a vague promise. Editors respond far better to "we ran 10 of the 12 sessions you asked for; here is why 12 was infeasible and what the 10 show" than to silence or hand-waving.

## Checklist

- [ ] Every comment triaged: new-data / re-analysis / clarification / disagreement
- [ ] Gate concerns (deception, incentive compatibility) resolved decisively, not argued around
- [ ] Power/inference-unit concerns met with group-level re-analysis or additional sessions
- [ ] Each new-treatment request is run or its omission is precisely justified
- [ ] Response is point-by-point, quote-then-respond, with exact locations of changes
- [ ] New results reported honestly, including any that weaken the original claim
- [ ] Replication deposit (data, instructions, z-Tree/oTree) updated to match the revision

## Keeping pre-registration credible through revision

A subtle ExpEcon trap: a referee asks for a new analysis or treatment, you run it, and your "pre-registered" framing quietly erodes because the new work was not pre-specified. Protect the distinction in the revision. Anything you add at the referee's request is, by definition, **not** part of the original confirmatory plan — label it as referee-requested and exploratory, and keep the original pre-registered primary test reported exactly as filed. For a substantial new treatment, consider pre-registering *its* analysis before collecting it, and say so in the letter. Editors trust authors who keep the confirmatory/exploratory line clean under revision pressure; blurring it to make new results look pre-planned is the fastest way to lose that trust.

## Anti-patterns

- Arguing a deception concern away instead of removing the procedure
- Promising a treatment "in future work" when the referee asked for it now
- Burying a weakened effect from a new treatment instead of interpreting it
- A defensive letter that disputes referees before reporting any changes
- Updating the manuscript but leaving the repository deposit stale
- Satisfying one referee while ignoring the other under a two-editor decision

## When the decision is reject, not R&R

A flagship reject is not the end of the experiment — the data are clean and the design is real. Triage the report for what is *fixable* (positioning, power, a missing control) versus *fatal at this venue* (a deception concern that cannot be removed, or a contribution the editors judge topical rather than methodological). If the core is sound but the contribution was read as too narrow, **JESA** is the natural next ESA home (replications, null results, shorter design notes). If a referee's deception read is correct, the only path is a re-designed follow-up. Do not resubmit the same paper to the flagship after a reject without a substantive change to the dimension that sank it.

## Output format

```text
【Journal】Experimental Economics (ESA method flagship)
【Skill】expecon-rebuttal
【Decision type】R&R / reject-resubmit / conditional accept
【Triage】new-data / re-analysis / clarification / disagreement (counts)
【Gate items】deception / incentive concerns — resolution
【New-data items】treatment/sessions to run or justified omission
【Letter form】point-by-point, quote-then-respond, locations cited? [Y/N]
【Package sync】repository updated to revision? [Y/N]
【Next step】re-run expecon-identification/robustness for new data → expecon-submission for resubmission
```
