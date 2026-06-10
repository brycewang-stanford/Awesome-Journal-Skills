---
name: orgsci-tables-figures
description: Use when building the exhibits for an Organization Science manuscript — data-structure diagrams and process models for qualitative work, correlation/result tables and interaction plots for quantitative work, and simulation/network figures, all in INFORMS house style with self-explanatory titles and notes.
---

# Tables, Figures & Exhibits (orgsci-tables-figures)

## When to trigger

- Your exhibits are cluttered, off house style, or not self-explanatory
- A reviewer cannot follow your qualitative data structure or process model
- Your regression tables omit information readers need to evaluate the claim
- A simulation or network figure does not communicate the mechanism

## House-style basics (INFORMS)

- Number tables and figures **consecutively** with **self-explanatory titles and notes** — each exhibit should be legible without the running text.
- Use **author-date** references in notes and captions (e.g., Norman 1977), consistent with the INFORMS author-date style.
- Keep fonts to the Garamond/Times-New-Roman family the journal specifies; avoid Helvetica Narrow. Minimize footnotes.
- Remember the **all-inclusive ~50-page norm**: exhibits count toward length. Heavy supplementary tables belong in the **separate anonymized appendix** that is submitted standalone for review and later posted as online supplementary material.

## Exhibits by method (the journal is eclectic — build what your design needs)

- **Qualitative / inductive.** A **Gioia-style data structure** (first-order codes → second-order themes → aggregate dimensions), a **process model** diagram, and a **representative-quotation table** keyed to themes — often the paper's centerpiece, carrying the analysis's trustworthiness.
- **Quantitative.** A descriptives/correlation table (reliabilities on the diagonal), nested regression tables that build the model, and **interaction plots with simple slopes**; for multilevel models, variance components and ICCs.
- **Event-history / panel.** Survival curves or hazard-ratio tables with the time structure explicit.
- **Computational / formal.** Figures of the qualitative pattern across parameter ranges with sensitivity panels and a parameter table; for formal models, a comparative-statics table.
- **Network.** A clear sociogram or block structure with the construct (brokerage, cohesion) annotated, not a hairball.

## Quality checks

- Every exhibit is anonymized (no author-identifying site names where they would breach blinding).
- Notes define all abbreviations, significance conventions, units, and N.
- The main-text exhibits tell the core story; the rest go to the standalone appendix.
- A reader who sees only the exhibits could reconstruct the argument.

## Anti-patterns

- A data structure that lists codes but shows no path to aggregate dimensions.
- Regression tables with stars but no effect sizes, CIs, or model-build logic.
- A network "hairball" with no annotated structure.
- Overloading the main text and blowing the ~50-page norm instead of using the appendix.


## Exhibit pass for Organization Science

Treat this skill as an executable review pass, not a prose hint. First lock a level map, a mechanism paragraph, and the cover-letter contribution statement; then judge whether the current manuscript answers the venue's real reader: interdisciplinary organization reviewers who ask whether the mechanism travels across levels of analysis.

- **Do the pass:** For every table or figure, state the estimand or object, sample or case base, uncertainty display, and one sentence the exhibit proves for the venue audience.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against AMJ for empirical management framing, ASQ for organization-theory depth, Management Science for formal/quantitative operations; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Centerpiece exhibit】data structure + process model / nested tables / sensitivity figure
【House style】numbered, self-explanatory titles+notes, author-date, no Helvetica Narrow
【Length plan】main-text exhibits vs. standalone anonymized appendix
【Anonymization】site/author identifiers handled
【Next step】orgsci-writing-style
```
