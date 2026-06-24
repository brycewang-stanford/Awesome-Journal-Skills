---
name: ajs-data-analysis
description: Use when planning or auditing the analysis of an American Journal of Sociology (AJS) manuscript so the evidence credibly supports the theoretical claim. Covers analysis norms, uncertainty, robustness, and triangulation across quantitative, comparative-historical, and ethnographic work. Improves the analysis chain; it does not fabricate results.
---

# Data Analysis (ajs-data-analysis)

At AJS the analysis exists to make the **theoretical claim credible** — not to display technique. A
generalist, double-blind reviewer will ask whether the evidence actually warrants the claim and whether
candor about uncertainty is present. This skill stress-tests the analysis chain in the idiom of your
work.

## When to trigger

- Planning the analysis, or auditing it before writing up
- A reader doubts robustness, the evidence-to-claim link, or the handling of uncertainty
- Reconciling multiple methods or data sources into one coherent argument
- Deciding which analyses are confirmatory vs. exploratory

## Analysis norms (by tradition)

### Quantitative
- Report **uncertainty honestly** (intervals, not just stars); avoid implying causality the design
  cannot support.
- Show that results are **not artifacts**: principled robustness (alternative specifications,
  samples, measures), not a fishing expedition; keep seeds and pinned versions.
- Distinguish **preregistered/confirmatory** from **exploratory** analyses where applicable.

### Comparative-historical
- Make the **inferential logic** explicit (necessary/sufficient conditions, sequence, conjuncture);
  show how disconfirming evidence was sought and weighed.
- Cite primary sources so a reader could follow the trail.

### Ethnographic / interview
- Show the **analytic procedure**: how codes/themes were built, how negative cases were handled, how
  representativeness within the case is judged.
- Quote enough to let the reader assess the inference from data to claim.

## Triangulation (an AJS strength)

AJS often rewards **convergent evidence** — a mechanism shown through more than one window
(e.g., statistics + cases, or interviews + administrative data). When methods disagree, say so and
theorize the discrepancy rather than hiding it.

## Referee-pushback patterns on the evidence chain (AJS fixes)

At a theory-forward generalist journal the analysis is judged by whether it makes the *claim* credible, not by technical novelty:

| Referee writes… | The AJS-specific fix |
|-----------------|--------------------|
| "Robustness theater." | run the one check the mechanism hinges on; drop filler |
| "Mechanism under-theorized." | map each estimate to an implication from `ajs-theory-building` |
| "Causal language the design can't bear." | restate as descriptive/associational and theorize it |
| "Methods disagree, unexplained." | theorize the discrepancy, don't suppress a window |

## Calibration (AJS appetite, hedged)

Orienting heuristics; confirm against the journal's current submission guidelines. AJS rewards convergent evidence and candor over a dense methods display, judging each tradition by its own standard; where a parsimony-first sibling prizes one clean estimate, AJS often prizes a mechanism shown through more than one window. Illustrative: a paper claims a mentoring program narrows a promotion gap "by building cross-rank ties" (an illustrative 6-point reduction, 95% CI ~2–10). A referee writes "the mechanism is asserted, not shown." The fix maps it to an observable implication (mentees gain cross-rank ties), triangulates with an illustrative 24 interviews, reports two units where the gap did *not* close, and softens causal phrasing to "consistent with."

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AJS is general sociology with a strong theory tradition; apply the chain below to its quantitative-empirical lane.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or
  `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`;
  multilevel data → cluster at the right level.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive battery in the supplement. See
the executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Stars-only reporting; implying causation from association
- Robustness theater (a wall of tables that never tests the load-bearing assumption)
- Cherry-picked quotes or cases that ignore negative evidence
- Presenting exploratory results as if confirmatory
- Technique foregrounded over the theoretical question it serves
- A single-window analysis where triangulation was feasible and would have settled the mechanism


## Evidence pass for American Journal of Sociology

Treat this skill as an executable review pass, not a prose hint. First lock the social process, data leverage, causal or interpretive warrant, and theoretical payoff; then judge whether the current manuscript answers the venue's real reader: sociology reviewers who value deep theory, durable empirical leverage, and careful social-mechanism claims.

- **Do the pass:** Audit the research design before polishing prose: unit of analysis, comparison set, uncertainty, sensitivity, missingness, and reproducibility must be visible.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against ASR for broader empirical sociology, Social Forces for wider substantive range, Demography for population mechanisms; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Claim under test】from theory-building
【Primary evidence】the analysis that carries the claim
【Uncertainty】how it is reported and bounded
【Robustness / negative cases】load-bearing checks done? [Y/N]
【Triangulation】convergent evidence across windows? [Y/N/NA]
【Confirmatory vs. exploratory】labeled where relevant? [Y/N]
【Next】ajs-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — analysis packages (R / Stata / Python / CAQDAS / QCA)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AJS evidence expectations and live-check boundary for data policy
