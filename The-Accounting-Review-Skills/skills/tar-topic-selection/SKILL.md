---
name: tar-topic-selection
description: Use when choosing or sharpening a research question for a The Accounting Review (TAR) manuscript — testing whether the question is contribution-driven, identifiable with accounting data, and a fit for TAR versus JAR/JAE or a specialist AAA section journal. Selects and scopes the question; it does not build the model (tar-theory-development) or design identification (tar-methods).
---

# Topic Selection & TAR Fit (tar-topic-selection)

## When to trigger

- You have a dataset (Compustat/CRSP/Audit Analytics/EDGAR) and want a publishable accounting question
- You have a regulatory or institutional shock and want to know what it can identify
- You are unsure whether the question belongs at TAR, JAR/JAE, or a specialist journal
- A colleague says "this is a finance paper, not an accounting paper" and you need to reposition

## The TAR fit test

TAR is open to all rigorous methods across financial accounting, capital markets, auditing,
management accounting, taxation, and accounting information systems. Its single overriding criterion
is the **significance of the contribution to the accounting literature**. A good TAR question
therefore must clear four gates:

1. **Accounting-centered.** The phenomenon turns on accounting information, measurement, disclosure,
   assurance, internal control, or taxation — not a generic finance or economics question that
   merely uses accounting data. If the dependent variable is a stock return, the *accounting*
   construct (earnings quality, disclosure, audit, tax) must be doing the theoretical work.
2. **Identifiable.** There is a credible path to a causal or well-specified association — a shock, a
   staggered regulation (e.g., a standard adoption, a PCAOB regime change), a setting that breaks the
   endogeneity, or a clean analytical structure.
3. **Contribution-bearing.** The answer changes how the field thinks, not just confirms an obvious
   prior; "significance of the contribution" is the explicit bar.
4. **Feasible under TAR norms.** It fits the 55-page initial limit and the data-authenticity /
   code-access regime (you can describe the data and share the processing code).

## Where TAR sits versus neighbors

- **TAR vs JAR/JAE**: all three are top-3 archival accounting journals, but JAR (Chicago Booth) and
  JAE (Elsevier) are separately owned with their own norms; pick by editor fit and conversation, not
  prestige alone. TAR's openness to experimental and analytical work is comparatively broad.
- **TAR vs AAA section journals** (Auditing: A Journal of Practice & Theory; JATA for tax; JMAR for
  management accounting; JIS for systems): a section journal suits a question of primarily
  sub-field interest; TAR suits a question with broad accounting significance.
- **TAR vs finance journals**: if the accounting construct is incidental, target finance instead.

## Scoping the question

- State the question as one sentence naming the accounting construct and the outcome.
- Name the identifying variation up front (shock, setting, model) — a TAR question without an
  identification idea is premature.
- Decide the method lane (large-sample archival, experiment, or analytical) honestly; do not retrofit
  a borrowed design onto an ill-suited question.

## Checklist

- [ ] The accounting construct, not a generic finance variable, drives the theory
- [ ] An identification idea (shock/setting/model) is named, not just "I have data"
- [ ] The contribution to the accounting literature is statable in one sentence
- [ ] TAR vs JAR/JAE vs a section journal chosen deliberately
- [ ] Scope fits 55 pages and the data-authenticity/code-access regime

## Anti-patterns

- **Data-first fishing**: "I have WRDS access, what can I run?" with no accounting question.
- **Finance in disguise**: an asset-pricing or corporate-finance question wearing an accounting label.
- **Replication without contribution**: re-running a known result on a new sample with no new insight.
- **Prestige targeting**: choosing TAR over JAR/JAE/section purely by ranking, ignoring conversation fit.

## Output format

```
【Accounting construct】... (financial / audit / tax / managerial / AIS)
【Question (1 sentence)】...
【Identifying variation】shock / setting / model: ...
【Contribution claim】the field will learn ...
【Venue fit】TAR vs JAR/JAE vs section journal — chosen because ...
【Method lane】archival / experiment / analytical
【Next step】tar-theory-development, then tar-literature-positioning
```
