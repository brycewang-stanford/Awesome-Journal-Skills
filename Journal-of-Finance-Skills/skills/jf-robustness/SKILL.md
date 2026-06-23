---
name: jf-robustness
description: Use when planning or auditing the robustness, sensitivity, and multiple-testing battery for a The Journal of Finance (JF) manuscript. Decides which checks are load-bearing; it does not design the main test.
---

# Robustness & Multiple Testing (jf-robustness)

## When to trigger

- The main result is in; you must decide which robustness checks to run and where to put them
- A referee will ask "does it survive [alternative measure / subsample / specification]?"
- The finding is one of many you tested and multiple testing is a live concern

## JF norm: decisive in the body, exhaustive in the Internet Appendix

JF favors an accessible body within the **60-page limit**. Put the **3–6 decisive checks** in the main text and move the exhaustive battery to the **Internet Appendix**, which is **bundled at the end of the same PDF** and **does not count toward 60 pages** (see `jf-internet-appendix`). This main-text/IA split is a JF hallmark; do not bury a load-bearing check.

## Multiple testing — a JF-salient concern

JF published the canonical "factor zoo" critique (**Harvey, Liu & Zhu, "…and the Cross-Section of Expected Returns," JF**). Reviewers therefore expect:
- An honest account of **how many specifications/signals were tried**.
- **Adjusted thresholds** (e.g., higher t-cutoffs, FDR control) for any discovery mined from many candidates, not the naive 1.96.
- Pre-registration-style discipline in framing (no HARKing).

## Robustness battery (select the load-bearing ones for the body)

- Alternative measures of the key variable
- Subsamples (time, size, industry) and the obvious excluded-period test
- Alternative standard errors / clustering dimensions
- Alternative controls / fixed effects; placebo and falsification tests
- For asset pricing: alternative factor models and EIV-corrected SEs (see `jf-empirical-design`)

## Body-vs-Internet-Appendix triage table

The hardest robustness decision at JF is not *which checks to run* but *which earn a place in the lean body*. Triage by how load-bearing each check is to the headline claim:

| Check                                              | Lives in body if…                              | Otherwise → Internet Appendix |
|----------------------------------------------------|------------------------------------------------|-------------------------------|
| The single most threatening alternative explanation | A skeptic's first objection turns on it        | never hide it in the IA       |
| Multiple-testing-adjusted threshold (anomalies)    | The discovery was mined from many candidates   | full grid of signals → IA     |
| Value-weighted / NYSE-breakpoint version           | Microcap concentration is plausible            | EW + alt breakpoints → IA     |
| Alternative key-variable measure                   | The measure is contestable and pivotal         | the other 4 measures → IA     |
| Subsample / excluded-period                        | A specific event could drive the result        | exhaustive subsamples → IA    |
| Placebo / falsification                            | One clean falsification clinches credibility   | the rest of the battery → IA  |

The cultural signal at JF: 3–6 decisive checks plus a deep Internet Appendix reads as confident; twenty robustness tables in the body read as defensive.

## Worked vignette — surviving the factor-zoo critique

*Illustrative numbers.* An anomaly paper reports a long-short spread of 0.58%/month, raw t = 3.2, found after screening (honestly disclosed) ~40 candidate signals. JF's published "factor zoo" lens (Harvey, Liu & Zhu) means t = 3.2 is **not** automatically decisive:

- Disclose the search: "We examined 40 supplier-network signals; we report the survivor." HARKing the count down to one is a fatal credibility error if a referee reconstructs it.
- Apply an adjusted threshold: with ~40 tests an illustrative FDR-style cutoff sits near t ≈ 3.1–3.4, so the body must show the adjusted alpha (say 41 bps, t = 2.9 after FF5 + momentum), not the raw spread.
- Body holds the decisive checks — factor-adjusted alpha, value-weighted/NYSE-breakpoint version (say 33 bps), one placebo. The other 37 signals, all factor models, and every subsample go to the Internet Appendix, each cited from the text.

The editor sees a robust effect, a transparent search, and a magnitude that survives the multiple-testing haircut.

### Referee-pushback patterns and the JF-specific fix
| Pushback you will hear                          | JF-specific fix                                                 |
|-------------------------------------------------|-----------------------------------------------------------------|
| "How many specifications did you try?"          | State the count; report an FDR-/Bonferroni-adjusted threshold   |
| "This is a microcap effect"                     | Value-weighted, NYSE-breakpoint version in the body             |
| "You buried the failing robustness check"       | Surface the load-bearing check in the body, not the appendix    |

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just list it. Full map:
[`shared-resources/empirical-methods/execution-with-mcp.md`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JF-specific instantiation:

- **Multiple testing (the JF-salient one):** after disclosing the search count, apply
  `romano_wolf` (step-down, accounts for cross-test correlation — the right tool for a
  factor-zoo screen) or `benjamini_hochberg` / `holm`; report the **adjusted** threshold
  and the alpha that survives it, in the body. The full grid of signals → Internet Appendix.
- **Sensitivity to omitted variables:** `oster_delta` / `sensemakr` to state how strong a
  confounder would need to be to overturn the result — a decisive body exhibit.
- **Inference:** `wild_cluster_bootstrap` when clusters are few; `twoway_cluster` /
  `conley` where the dependence structure demands it.
- **Re-fit checks off one handle:** `audit_result(result_id)` enumerates the missing
  checks; run each `suggest_function` it emits rather than guessing the battery.
- **Emit JF-format exhibits:** `etable` / `did_summary_to_latex` for the decisive tables;
  hand off formatting to `jf-tables-figures`.

Triage the *output* by the body-vs-Internet-Appendix table above: 3–6 executed,
decisive checks in the body; the exhaustive (now actually-run) battery in the bundled IA.

## Checklist

- [ ] 3–6 decisive checks in the body; the rest in the Internet Appendix
- [ ] Number of specifications tried is disclosed
- [ ] Multiple-testing adjustment applied to mined results
- [ ] At least one placebo/falsification test
- [ ] No load-bearing robustness check hidden in the appendix
- [ ] Body stays within 60 pages after the split

## Anti-patterns

- A 20-table robustness section in the body that pushes the paper over 60 pages
- Reporting only the specifications that "work" without disclosing the search
- Treating raw t > 1.96 as decisive after extensive mining
- Hiding the one check that actually threatens the result in the Internet Appendix

## Output format

```
【Decisive checks in body】[3–6]
【Specifications tried disclosed?】yes / no
【Multiple-testing adjustment?】yes / no — method
【Placebo/falsification present?】yes / no
【Body ≤60 pp after split?】yes / no
【Next step】jf-tables-figures
```
