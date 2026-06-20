---
name: jebo-rebuttal
description: Use when a Journal of Economic Behavior & Organization (JEBO) decision letter arrives and a response-to-referees strategy is needed — triaging a revise-and-resubmit, ordering concessions vs. pushback, and re-running experiments where required. Plans the revision and response letter; it does not run the new analysis.
---

# Rebuttal & Revision (jebo-rebuttal)

## When to trigger

- A JEBO R&R (or reject-and-resubmit) arrived and you must plan the response
- Two referees disagree and you need a coherent strategy across both
- A referee demands a new treatment / additional subjects and you must scope it
- You are deciding which points to concede and which to defend
- You need to structure the point-by-point response letter for the editor

## Read the editor's letter first

The decision letter, not the referee reports, sets the priorities. The editor signals which concerns are **conditions** for acceptance and which are optional. With **single-anonymized** review, the editor can also weigh your standing and the field context. Build the revision around the editor's emphasis; address every referee point but invest most where the editor pointed.

## Triage every comment

Sort each referee point into four bins before writing anything:

| Bin | Action |
|-----|--------|
| Cheap + improves the paper | Do it; thank the referee; show the new exhibit/text. |
| Costly but a genuine condition (new treatment, more subjects) | Scope it, run it, report it; this is usually the make-or-break for a JEBO experimental R&R. |
| Based on a misreading | Clarify *and* edit the text that allowed the misreading — never just say "the referee misunderstood." |
| Wrong / out of scope | Push back with evidence, respectfully; concede the framing even while holding the substance. |

## JEBO-specific revision moves

- **New experimental treatment / sessions.** Experimental R&Rs at JEBO frequently require running an additional arm (e.g., the demand-effect control or a mechanism-separating treatment a referee asked for). Plan the timeline; report the new arm with the same rigor (pre-register the addition if feasible).
- **Mechanism vs. alternative.** If a referee proposed a rival channel, add the test that separates them rather than arguing verbally.
- **Multiplicity after adding analyses.** New outcomes added in revision must be folded into the MHT correction; do not quietly expand the comparison set.
- **External validity.** If asked to generalize, either add a pool/field replication or bound the claim explicitly and say so.

## Writing the response letter

- One document; **quote each referee comment**, then respond directly beneath it; point to the exact section/table/page where the change lives.
- Lead each response with the action taken ("We added Treatment D…"), not with justification.
- Keep a respectful, non-defensive tone — single-anonymized review means the relationship is not anonymous on your side.
- Summarize the major changes in a short cover note to the editor mapped to the editor's stated priorities.
- Maintain a change log so co-authors and the editor can see the manuscript's evolution.

## Checklist

- [ ] Editor's letter parsed; conditions vs. optional points separated
- [ ] Every referee comment binned (do / scope-and-run / clarify+edit / push back)
- [ ] New experimental arms or subjects scoped with a realistic timeline
- [ ] Rival-mechanism objections answered with a test, not prose
- [ ] New analyses folded into MHT correction; comparison set not silently expanded
- [ ] Response letter quotes each comment, leads with the action, cites exact locations
- [ ] Tone respectful (single-anonymized — not anonymous on author side)
- [ ] Misreadings fixed in the text, not merely rebutted

## Anti-patterns

- Responding to referees while ignoring the editor's stated priorities
- "The referee misunderstood" with no edit to the text that caused it
- Verbally dismissing a rival-mechanism concern instead of running the test
- Quietly adding outcomes in revision without updating the multiplicity correction
- A defensive or curt tone toward a referee whose identity the editor knows
- Promising a robustness check in the letter but not actually adding it to the paper

## Output format

```text
【Decision】R&R / major / minor / reject-and-resubmit
【Editor's priorities】<conditions the editor emphasized>
【Comment triage】do / scope-and-run / clarify+edit / push-back (counts)
【New experiment needed?】<arm/sessions + timeline, or none>
【Mechanism-vs-alternative test added?】[Y/N]
【Response letter】quote-then-respond, action-first, locations cited [Y/N]
【Next step】resubmit via Editorial Manager → jebo-workflow if re-triage needed
```
