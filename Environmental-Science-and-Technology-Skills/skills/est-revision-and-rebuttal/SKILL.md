---
name: est-revision-and-rebuttal
description: Use when writing the response to an Environmental Science & Technology (ES&T) revision decision. ES&T decisions are editor-led on the back of typically three expert reviews, so the response must convert each reviewer with evidence and QA/QC while keeping the editor confident. It structures the response letter and revision; it does not fabricate new results.
---

# Revision & Rebuttal (est-revision-and-rebuttal)

An ES&T **major/minor revision** is a real opening, but acceptance depends on satisfying typically
**three** expert reviewers and the editor. Environmental-science reviews tend to demand concrete
analytical fixes — more QA/QC, a closed mass balance, added controls, clearer significance — so the
response letter must answer each with evidence, not assurances.

## When to trigger

- A revision decision arrived and you are planning the revision + response letter
- Reviewers disagree and you must reconcile their demands
- A reviewer requests new experiments, controls, or analyses
- Writing the cover note to the editor summarizing the revision

## Strategy

1. **Read the editor's letter as the rubric.** The editor signals which points are decisive — solve
   those first; the editor adjudicates disagreements among reviewers.
2. **One point-by-point response, every comment addressed.** Quote each comment, then respond. Never
   skip one — silence reads as non-compliance.
3. **Concede or rebut with evidence.** Did what was asked (cite the new text/figure/table/SI location),
   or push back **respectfully with a reason** (data, mechanism, or environmental relevance). A
   well-argued disagreement beats a hollow capitulation that weakens the paper.
4. **Answer analytical asks concretely.** Add the requested control/replicate, report the recovery or
   detection limit, close the mass balance, or run the alternative analysis — and show the result.
5. **Reconcile conflicting reviewers openly.** When reviewers want opposite things, say so, choose a
   principled path, and explain the tradeoff to the editor.
6. **Protect the contribution.** Add robustness and clarity; resist changes that dilute the
   environmental-significance claim; defend scope conditions rather than over-claiming.
7. **Keep SI and deposit in sync.** Update the **Supporting Information**, data-availability statement,
   and deposited data/code so new exhibits remain reproducible (see `est-reporting-and-reproducibility`).

## Response-letter format

For each reviewer comment:

```
> [Quoted reviewer comment]

Response: [What we did / why we respectfully disagree].
Change: [Section/page/figure-table/SI location where the revision appears].
```

Open with a short **summary of the main changes** to the editor; group by reviewer; end each entry
with the location of every change so the editor can verify quickly.

## Triaging ES&T reviewer asks: concede, add, or defend

Environmental-science reviews cluster into recognizable demands. Decide the response mode per type so
the letter reads as evidence, not assurance:

| Reviewer ask | Default response mode | What to show |
|--------------|----------------------|--------------|
| "Report detection limits / QA/QC" | concede + add to SI | the blank/recovery/LOD table |
| "Mass balance doesn't close" | concede or bound | closure % and the named missing fraction |
| "Environmental relevance unclear" | defend with framing | tie concentrations/matrix to the real system |
| "Add a control/replicate" | add if feasible | the new result, in a figure/table |
| "Reanalyze censored data" | add | ROS/MLE result vs. original |
| "Conditions unrealistic" | defend or scope | justify, or narrow the claim |

## Worked micro-example (illustrative — answering a QA/QC pushback)

A reviewer on the PFAS-fate paper writes (illustrative): *"The transformation claim is unconvincing
without recovery and blank data; precursor loss could be sorption."* A response that converts the
reviewer:

```
> The transformation claim is unconvincing without recovery and blank data;
> precursor loss could be sorption.

Response: We agree QA/QC was under-reported and that sorption is a competing
explanation. We now report matrix-spike recovery (92±7%, n=6) and field blanks
(<LOQ) in Table S3, and we add an abiotic (autoclaved) control showing <5%
precursor loss (illustrative), ruling out sorption/abiotic pathways as the
dominant sink. The downstream PFHxA increase therefore reflects biotransformation.
Change: Methods p.6; new Figure 3b; Tables S3 and S5; data and code updated on
Zenodo (DOI: illustrative).
```

The pattern that wins: name the competing explanation the reviewer raised, kill it with a *control and
reported numbers*, and point to the exact location — never promise the fix in prose alone.

## Anti-patterns

- Ignoring or merging away a comment without a visible response
- Promising a fix in prose without showing the new data/exhibit
- Capitulating to a request that breaks the paper's logic just to please a reviewer
- Defensive or dismissive tone toward reviewers
- New exhibits that drift out of sync with the SI and deposited data

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Concede vs rebut】each tagged with evidence + change location
【Analytical asks】controls/QA-QC/mass balance addressed with results? [Y/N]
【Reviewer conflicts】reconciled and explained to editor? [Y/N]
【Contribution protected】significance not diluted? [Y/N]
【SI + deposit updated】[Y/N]
【Next】resubmit via the ACS Publishing Center
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — analysis/QA-QC tools for reviewer-requested additions
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — decision flow and editor-discretion policy
