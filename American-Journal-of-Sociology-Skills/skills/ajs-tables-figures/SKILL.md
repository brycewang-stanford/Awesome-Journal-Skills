---
name: ajs-tables-figures
description: Use when building tables and figures for an American Journal of Sociology (AJS) manuscript to AJS house conventions — discrete consecutive numbering, appendix-table lettering, separate exhibit sections after the text, and mandatory alt text for every figure at submission. Prepares exhibits; it does not generate data.
---

# Tables & Figures (ajs-tables-figures)

AJS has **specific house conventions** for exhibits, and it now **requires alt text for every figure
at submission**. Get the mechanics right so the exhibits read cleanly under double-blind review and
pass straight into production. Verify current formatting against the AJS Manuscript Preparation pages
and Formatting PDF before submission.

## When to trigger

- Building or revising tables and figures for an AJS submission
- Preparing the post-text exhibit sections and appendix tables
- Writing alt text and captions
- A reader said an exhibit was unreadable, mislabeled, or non-self-contained

## AJS exhibit conventions (verify on the live prep pages / PDF)

- **Numbering:** number tables/figures **consecutively** as they appear in the text. AJS **strongly
  prefers numbering discrete items separately** (table 1, table 2, table 3 …) rather than grouping
  several panels under one number.
- **Appendix exhibits:** number as **table A1, A2 … / table B1, B2 …** (lettered by appendix).
- **Placement:** **notes, references, tables, figures, and appendices appear in separate sections
  following the text, in that order** — not embedded inline.
- **Alt text (required):** provide **alternative text for every figure, image, or inline graphic**,
  included **with the figure captions at the time of submission**.
- **Self-contained:** each exhibit readable on its own — units, N, source, and what varies stated in
  title/notes.

## Make exhibits do theoretical work

- Lead with the exhibit that carries the **main claim**; do not bury it among robustness tables.
- Prefer figures that show a **mechanism or pattern** (marginal effects, event-study, sequence,
  network structure) over dense coefficient dumps where a plot would communicate better.
- Colorblind-safe, legible in grayscale; vector output (PDF/EPS) for print.

## Referee/production conformance check (AJS-specific)

| Slip referees and production catch | AJS-specific fix |
|------------------------------------|------------------|
| Panels grouped under one number | discrete, consecutive: table 1, 2, 3 |
| Appendix table continues the main sequence | letter it: table A1/B1 |
| Exhibit embedded inline | move to the separate post-text sections |
| Perfunctory or missing alt text | one descriptive line per figure, with captions |
| Exhibit unreadable without the body | state units, N, source in title/notes |

## Calibration: exhibits as argument, not decoration (hedged)

Craft heuristics fitting AJS's culture, not graded rules; confirm specifics against the journal's current submission guidelines. Because AJS rewards a carefully built argument, the lead exhibit should carry the *theoretical* claim, not merely display a model — a figure that makes a mechanism visible (a sequence plot, a network diagram, marginal effects rather than a coefficient dump) does more work than a wall of stars, and pacing the long-form article means placing the claim-bearing exhibit early. Illustrative: a regime-transitions paper buries its headline pattern in table 6; the author promotes it to a lead event-sequence figure, renumbers the rest discretely (tables 1–7), moves diagnostics to a lettered appendix (A1–A3), and gives every figure descriptive alt text.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-supplement drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AJS is general sociology with a strong theory tradition; apply the chain below to its quantitative-empirical lane.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Grouping panels under one number when AJS wants discrete numbering
- Embedding tables/figures inline instead of in the post-text sections
- Missing or perfunctory alt text (now required at submission)
- Exhibits that need the body text to be intelligible (no units, no N, no source)
- A wall of stars where a single figure would carry the argument, or burying the claim-bearing exhibit among robustness tables


## Exhibit pass for American Journal of Sociology

Treat this skill as an executable review pass, not a prose hint. First lock the social process, data leverage, causal or interpretive warrant, and theoretical payoff; then judge whether the current manuscript answers the venue's real reader: sociology reviewers who value deep theory, durable empirical leverage, and careful social-mechanism claims.

- **Do the pass:** For every table or figure, state the estimand or object, sample or case base, uncertainty display, and one sentence the exhibit proves for the venue audience.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against ASR for broader empirical sociology, Social Forces for wider substantive range, Demography for population mechanisms; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Main exhibit】the one carrying the central claim (lead with it)
【Numbering】discrete + consecutive? appendix as A1/B1? [Y/N]
【Placement】in separate post-text sections (notes/refs/tables/figures/appendices)? [Y/N]
【Alt text】present for every figure, with captions? [Y/N]
【Self-contained】units / N / source / accessible? [Y/N]
【Next】ajs-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — plotting and exhibit tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AJS exhibit numbering, post-text sections, and alt-text requirement
