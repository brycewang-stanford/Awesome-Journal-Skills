---
name: poq-theory-and-hypotheses
description: Use when building the theoretical argument and hypotheses of a Public Opinion Quarterly (POQ) manuscript — whether the contribution is to opinion/communication theory or to survey methodology. POQ rewards explicit constructs, mechanisms, and testable hypotheses, and methods papers need a clear claim about a survey-error source. Structures the argument; it does not run analyses.
---

# Theory & Hypotheses (poq-theory-and-hypotheses)

At POQ a result is not a contribution until it is attached to a **clear claim** — about how opinion
forms or moves, how communication shapes it, or how a survey-design choice affects measurement. This
skill turns findings into theory: explicit constructs, mechanisms, and **falsifiable hypotheses**, in
the idiom appropriate to a substantive or a methodological paper.

## When to trigger

- The empirics are strong but the "so what / why" is thin
- A reviewer said the paper is "atheoretical," "ad hoc," or "just a finding"
- You need to state constructs, mechanisms, and hypotheses explicitly
- A methods paper needs a precise claim about which survey-error source it addresses

## Build the argument (by kind of paper)

### Substantive opinion / communication paper
1. **Concept** — define the attitude, behavior, or communication construct precisely; distinguish it
   from neighbors (attitude vs. non-attitude, opinion vs. knowledge, exposure vs. reception).
2. **Mechanism** — the process: how information, identity, framing, or context moves the opinion.
3. **Hypotheses** — directional, falsifiable predictions tied to the mechanism, with the **null** that
   a rival account or measurement artifact would imply.
4. **Scope conditions** — population, period, and context where the claim holds.

### Survey-methodology paper
- State the **survey-error source** at issue (coverage, nonresponse, measurement, mode, weighting) and
  the **specific bias or variance claim** you make about it.
- Frame the hypothesis in **Total Survey Error** terms: which error component changes, in which
  direction, under which design choice.
- Distinguish predictions unique to your account from those a competing methods explanation shares.

## The measurement-validity test (POQ-specific)

For the central construct, write one sentence: *"My measure captures ___ and not ___; if it were
instead picking up a measurement artifact (wording / order / mode / nonresponse), I would see ___."*
If you cannot, the construct is not yet pinned down — strengthen measurement before hypothesizing.

## Anti-patterns

- "Hypothesizing after results are known" (HARKing) — state hypotheses before tests; preregister where possible
- Treating a survey artifact (wording, order, mode) as if it were a substantive opinion effect
- Mechanisms named but never made observable / testable
- Universal claims with no scope conditions or population
- A methods paper with no explicit claim about which error source it improves


## Theory pass for Public Opinion Quarterly

Run this as a concrete capability pass. First lock the public-opinion construct, sampling frame, mode effects, weighting/nonresponse plan, and trend or causal interpretation; then test whether the manuscript addresses survey and public-opinion reviewers who inspect measurement, sampling, mode, nonresponse, and inference about attitudes or behavior.

- **Primary move:** Link every hypothesis to a mechanism, rival account, boundary condition, and observable implication; drop hypotheses that only restate correlations.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Political Analysis for methods-first work, Journal of Politics for political-science theory, Communication Research for media-effects framing; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Kind】substantive-opinion / survey-methodology
【Core claim】one sentence
【Construct(s)】defined + distinguished from neighbors
【Mechanism / error source】the process or the TSE component at issue
【Hypotheses】directional + the null / artifact alternative
【Scope conditions】population / period / context
【Next】poq-survey-design-and-measurement
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — measurement, scaling, and TSE references
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — POQ scope and contribution expectations
