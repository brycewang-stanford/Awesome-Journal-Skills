---
name: crim-rebuttal
description: Use when writing the response to a Criminology (ASC / Wiley) revise-and-resubmit. Criminology revisions usually require converting multiple expert reviewers across the field's disciplines while keeping the editor confident the revision is convergent and the theoretical contribution intact. Structures the response letter; it does not fabricate new results.
---

# R&R Rebuttal (crim-rebuttal)

A *Criminology* **R&R is a strong signal** — top criminology journals reserve revisions for papers with
real promise. But getting to acceptance usually means satisfying **several expert reviewers** drawn
from different disciplines (a developmental psychologist, a quantitative criminologist, a theorist),
under the **editor's** judgment. The response letter must move *every* reviewer toward yes while
keeping the editor confident the revision converges and the contribution survives.

## When to trigger

- An R&R (major/minor) arrived and you are planning the revision + response letter
- Reviewers disagree with each other and you must reconcile their demands
- A reviewer requests analyses (e.g., a different trajectory solution or robustness) that could change claims
- Writing the cover note to the editor summarizing the revision

## Strategy

1. **Read the editor's letter as the rubric.** The editor signals which points are decisive — often the
   theoretical contribution and identification. Solve those first; the editor adjudicates reviewer
   disagreements.
2. **One point-by-point response, every comment addressed.** Quote each comment, then respond. Never
   skip one — silence reads as non-compliance.
3. **Concede or rebut explicitly, with evidence.** For each: did what was asked (say where, with the new
   text/table/figure number), or push back **respectfully with a reason** (theory, measurement, design,
   or evidence). A well-argued disagreement beats a capitulation that weakens the paper.
4. **Reconcile conflicting reviewers openly.** When one wants more trajectory groups and another wants
   fewer, or one wants official counts and another self-report, say so, choose a principled path, and
   explain the tradeoff to the editor.
5. **Protect the theoretical contribution.** Add robustness and clarifications; resist changes that
   dilute the mechanism or over-claim beyond the scope conditions. Defend within- vs. between-person
   distinctions and crime-measurement choices rather than papering over them.
6. **Keep anonymity intact** in the revised main document and **update the reproducibility package** so
   new tables/figures remain reproducible (see `crim-data-and-transparency`).

## Response-letter format

For each reviewer comment:

```
> [Quoted reviewer comment]

Response: [What we did / why we respectfully disagree].
Change: [Section/page/table-figure number where the revision appears].
```

Open with a short **summary of the main changes** to the editor; group by reviewer; end each entry with
the location of every change so the editor and reviewers can verify quickly.

## Anti-patterns

- Ignoring or merging away a comment without a visible response
- Capitulating to a request that breaks the theory or the identification just to please a reviewer
- Defensive or dismissive tone toward reviewers
- "We thank the reviewer" with no actual change or argued reason
- Adding analyses that quietly contradict the original criminological claim without acknowledging it
- Letting the revised manuscript or new exhibits drift out of sync with the deposited package

## Reconciling interdisciplinary reviewers (Criminology triage table)

Because the ASC flagship draws reviewers across sociology, psychology, and quantitative criminology,
R&R comments often conflict. Sort each by whether it touches the contribution.

| Comment type | Example | Concede or defend? |
|--------------|---------|--------------------|
| Touches identification | "selection into treatment unaddressed" | concede — add within-person/sensitivity analysis |
| Touches measurement | "official records, not offending" | partly concede — add self-report robustness |
| Touches theory | "this isn't really testing GST" | defend if your prediction separates GST from a rival |
| Conflicting asks | one wants 4 trajectory groups, one wants 3 | choose by BIC/AvePP, explain to the editor |

## Worked vignette: an R&R response move (illustrative)

Reviewer 1 (a psychologist) wants a fifth trajectory group; Reviewer 2 (a quantitative criminologist)
calls the existing four over-fit. The response reports BIC favoring four and AvePP of 0.84
(illustrative), adds the five-group fit to an appendix showing the extra group is < 3% of the sample
and unstable, and tells the editor four is retained on classification grounds. Both reviewers see their
point engaged; the contribution holds.

## R&R referee pushback (with the Criminology fix)

- *"You only added confirming analyses."* Fix: include a check that could have broken the claim; report it honestly.
- *"The revision drifts from the theory."* Fix: protect the mechanism and scope conditions; resist dilution.
- *"New tables don't match the package."* Fix: re-run the master script so every new exhibit reproduces from the deposit.

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Concede vs rebut】each tagged with evidence + change location
【Reviewer conflicts】reconciled and explained to editor? [Y/N]
【Contribution protected】theory + scope conditions intact? [Y/N]
【Anonymity + package updated】[Y/N]
【Next】resubmit via the official ASC/Wiley online submission link
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review/decision norms and editor-discretion items
