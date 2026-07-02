---
name: jae-topic-selection
description: Use when choosing or sharpening a research question for the Journal of Accounting and Economics (JAE) — testing economics-based fit, distinguishing JAE from JAR/TAR/RAST, and ensuring the question is about accounting's economic role rather than a normative or behavioral puzzle.
---

# Topic Selection & JAE Fit (jae-topic-selection)

## When to trigger

- You have a dataset or a hunch but no economics-based question
- You are unsure whether the idea belongs at JAE versus JAR, TAR, RAST, or a finance journal
- A coauthor frames the project normatively ("how should firms report?") rather than positively
- The question is "interesting" but you cannot name the economic mechanism

## The JAE fit test

JAE publishes **positive (economics-based) accounting research**. A fitting question lives in one of its core domains and is driven by an economic force:

1. **Accounting within the firm** — internal control, budgeting, performance measurement as economic mechanisms.
2. **Information content in capital markets** — how accounting numbers move prices, returns, liquidity, analyst behavior.
3. **Financial contracting & monitoring** — debt covenants, executive compensation, agency relationships, governance.
4. **Determination of accounting standards** — the political/economic forces shaping GAAP/IFRS.
5. **Regulation of disclosure and the profession** — SEC/PCAOB rules, mandatory vs. voluntary disclosure, audit.

Ask: *What economic friction (information asymmetry, agency conflict, transaction cost, regulatory constraint) makes accounting matter here, and what observable behavior does it predict?* If you cannot answer, the topic is not yet JAE-ready.

## Positive, not normative

In the Watts-Zimmerman tradition that founded JAE in 1979, the journal explains and predicts accounting choices and consequences; it does not prescribe what firms *should* do. Reframe "should" questions into "why do firms do X, and with what consequences?" Screen out pure behavioral-experimental puzzles, design-science artifacts, and practitioner how-to pieces — those are off-fit.

## Micro-rewrite: from dataset hunch to JAE question

- **Before**: "Does ESG disclosure affect firm value? We regress Tobin's Q on an ESG-report indicator." — outcome-first phrasing, no friction, no actor, and an obvious selection problem baked into the question itself.
- **After**: "When proprietary costs fall for some firms (a plausibly exogenous drop in rival entry threat), which managers begin disclosing segment detail, and does the liquidity gain concentrate in firms with the widest pre-period information asymmetry?" — the friction (proprietary cost vs. information asymmetry), the actor (the disclosing manager), a shock to exploit, and a cross-sectional partition are all inside the question before any data work.

The rewrite pattern generalizes: replace "does X affect Y" with "which economic force makes the accounting choice vary, and where should its consequence concentrate."

## The desk-screen stress test

Submission is fee-bearing (USD 650 for a new manuscript) and the editor's suitability screen can end the paper without review, so pressure-test the topic before spending the fee:

1. **One-sentence economics test** — state the question as "friction F gives actor A an incentive to make accounting choice C, with consequence Q." If the sentence needs no accounting term, it is a finance paper; if it needs no economics term, it is not a JAE paper.
2. **Watts-Zimmerman generator** — run the idea through the classic determinants (bonus incentives, debt-covenant tightness, political costs) and their modern extensions (proprietary costs, career concerns, monitoring demand). If none generates the question, the economics is decorative.
3. **Consequence test** — a JAE topic predicts a market or contracting consequence (pricing, liquidity, covenant design, compensation weights), not merely a reporting pattern.
4. **Counterfactual test** — can you state what the firm would report absent the friction? If the counterfactual is unimaginable, identification will be too.

## Choosing among accounting journals

- **JAE**: economics-based mechanism + large-sample archival (or analytical) test; contracting/disclosure/capital-markets emphasis.
- **JAR**: similar archival rigor but a **mandatory** replication package — only pursue if you can share code/data.
- **TAR**: wider tent — experimental and analytical work also fit.
- **RAST**: archival, frequently valuation- and capital-markets-focused.
- A pure asset-pricing question with little accounting content belongs at a finance journal (e.g., JFE), not JAE.

## A "ready" JAE question

- Names an economic mechanism, not just a correlation.
- Has a **plausible identification** path (a shock, instrument, or natural experiment) you can access.
- Uses data you can build from WRDS (Compustat/CRSP/I/B/E/S/Execucomp/DealScan/Audit Analytics) or hand-collected disclosure.
- Maps to **JEL codes** (you will need up to 6) — if no JEL code fits, reconsider the economics framing.

## Checklist

- [ ] Question sits in a JAE core domain (firm/markets/contracting/standards/disclosure)
- [ ] An economic friction and a testable prediction are named
- [ ] Framing is positive (explain/predict), not normative
- [ ] A feasible identification strategy is visible
- [ ] Required data are accessible; sample is buildable
- [ ] JEL codes exist for the topic
- [ ] JAE beats JAR/TAR/RAST/JFE as the target for *this* paper

## Anti-patterns

- **"Compustat fishing"**: a significant correlation with no economic story.
- **Normative drift**: "firms should disclose more" with no positive prediction.
- **Wrong-venue behavioral lab study** dressed as archival.
- **No identification**: a topic where endogeneity cannot plausibly be addressed.

## Output format

```
【Domain】firm / capital-markets / contracting / standards / disclosure
【Economic friction】information asymmetry / agency / transaction cost / regulation
【Prediction】...
【Identification idea】shock / IV / DiD / RD ...
【Data】WRDS sources + sample feasibility
【JEL codes】...
【Why JAE (not JAR/TAR/RAST)】...
【Next step】jae-theory-development
```
