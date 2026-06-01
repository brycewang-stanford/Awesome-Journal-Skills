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
