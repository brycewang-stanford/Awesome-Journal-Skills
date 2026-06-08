# JAR Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-07.** Every paper below was checked against publisher /
> index records (Wiley Online Library `onlinelibrary.wiley.com/.../1475-679X...`, and the RePEc/EconPapers
> `bla:joares` series, which is the *Journal of Accounting Research* series code) to confirm it actually
> appeared in **the Journal of Accounting Research (JAR — Chicago Booth, published by Wiley)**, with year
> and volume(issue):pages. Candidates that turned out to be in a **sibling** journal — *The Accounting
> Review* (TAR), *Journal of Accounting and Economics* (JAE), *Contemporary Accounting Research* (CAR), or
> *Review of Accounting Studies* (RAST) — were **omitted** and are listed in the guardrail section below.
> It is deliberately a short, clean, verified list rather than a long, uncertain one.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent regression coefficients or specific findings — read the original on Wiley / the
> authors' pages before citing any number. For JAR-specific policy, scope, and the venue facts, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes a
*credibly identified* result carry a *first-order accounting* lesson — the JAR bar (see
[`../../skills/jar-topic-selection/SKILL.md`](../../skills/jar-topic-selection/SKILL.md),
[`../../skills/jar-literature-positioning/SKILL.md`](../../skills/jar-literature-positioning/SKILL.md), and
[`../../skills/jar-writing-style/SKILL.md`](../../skills/jar-writing-style/SKILL.md)). For each, ask the
self-check question before claiming your paper is "JAR-shaped." The fictional worked example in
[`../worked-examples/01-introduction.md`](../worked-examples/01-introduction.md) shows the intro arc these
papers execute.

---

## By method

### Returns–earnings event study (foundational capital-markets archival)

- **Ball & Brown, "An Empirical Evaluation of Accounting Income Numbers," JAR 1968, 6(2):159–178.**
  Verified: RePEc/EconPapers `bla:joares` v6 1968; DOI 10.2307/2490232.
  - **Why it is an exemplar:** founds the Ball-Brown tradition that is JAR's gravitational center — it
    shows accounting income numbers are *informative* by tying earnings news to the direction of abnormal
    returns, turning "does accounting matter?" into a testable capital-markets question.
  - **Self-check:** does your design let market behavior *adjudicate* whether an accounting number carries
    information, rather than assume it?

### Volume / return-variance announcement study (information-content design)

- **Beaver, "The Information Content of Annual Earnings Announcements," JAR 1968, 6:67–92.**
  Verified: RePEc/EconPapers `bla:joares` v6 1968 (`ideas.repec.org/a/bla/joares/v6y1968ip67-92.html`).
  - **Why it is an exemplar:** identifies information content through *trading volume and price-variance*
    reactions around the announcement window — a complementary research-design template to Ball-Brown for
    detecting that a disclosure moved beliefs. Pairs with the short-window event-study logic in
    [`../../skills/jar-methods/SKILL.md`](../../skills/jar-methods/SKILL.md).
  - **Self-check:** is your event window tight enough that the reaction can be attributed to the
    disclosure, not to confounding news?

### Cross-sectional determinants of disclosure quality (disclosure archival)

- **Lang & Lundholm, "Cross-Sectional Determinants of Analyst Ratings of Corporate Disclosures," JAR 1993, 31(2):246–271.**
  Verified: RePEc/EconPapers `bla:joares` v31 1993; DOI 10.2307/2491273.
  - **Why it is an exemplar:** brings a measured construct (analyst-rated disclosure quality) to a clean
    cross-sectional question about *what kinds of firms* disclose more — a model for measure-driven
    disclosure work in the voluntary-disclosure stream named in
    [`../../skills/jar-literature-positioning/SKILL.md`](../../skills/jar-literature-positioning/SKILL.md).
  - **Self-check:** is your disclosure construct validated and tied to an economic argument, not just a
    convenient proxy?

### Disclosure-regime change / quasi-experiment (economic-consequences design)

- **Leuz & Verrecchia, "The Economic Consequences of Increased Disclosure," JAR 2000, 38(Suppl.):91–124.**
  Verified: RePEc/EconPapers `bla:joares` v38 2000 (`ideas.repec.org/a/bla/joares/v38y2000ip91-124.html`).
  - **Why it is an exemplar:** uses firms switching reporting regimes to tie *increased disclosure* to
    information-asymmetry proxies (bid-ask spread, volume) — the canonical "does disclosure lower the cost
    of capital?" economic-consequences design, with a setting that supplies the variation. The fictional
    worked-example intro is built on this kind of regime-change logic.
  - **Self-check:** does your setting give a credible source of variation in disclosure, so the asymmetry
    change is plausibly *caused* by disclosure rather than by selection into it?

### Cross-country mandatory-adoption quasi-experiment (regulation / standard-setting)

- **Daske, Hail, Leuz & Verdi, "Mandatory IFRS Reporting around the World: Early Evidence on the Economic Consequences," JAR 2008, 46(5):1085–1142.**
  Verified: Wiley `onlinelibrary.wiley.com/doi/abs/10.1111/j.1475-679X.2008.00306.x`; RePEc `bla:joares`
  v46(5) 2008.
  - **Why it is an exemplar:** exploits *mandatory* IFRS adoption across 26 countries as a
    regulation-driven natural experiment for liquidity, cost of capital, and valuation — the
    standard-setting-shock template `jar-topic-selection` prizes, with cross-country institutional
    variation as the identifying lever. Adapt with
    [`../code/stata/03_did_modern.do`](../code/stata/03_did_modern.do).
  - **Self-check:** does your mandate create comparison groups (and timing) clean enough to separate the
    rule's effect from contemporaneous macro/market changes?

### Measurement-error methodology that disciplines a literature (archival methods)

- **Hribar & Collins, "Errors in Estimating Accruals: Implications for Empirical Research," JAR 2002, 40(1):105–134.**
  Verified: Wiley `onlinelibrary.wiley.com/doi/abs/10.1111/1475-679X.00041`; RePEc `bla:joares` v40 2002.
  - **Why it is an exemplar:** shows that a standard construction (balance-sheet accruals) injects
    measurement error that biases earnings-management and mispricing tests — a methods contribution that
    *reopens* a literature by changing how everyone should measure, exactly the "new measure / method that
    reopens a literature" increment in
    [`../../skills/jar-contribution-framing/SKILL.md`](../../skills/jar-contribution-framing/SKILL.md).
  - **Self-check:** does your measurement critique change downstream *inferences*, not just refine a
    number nobody disputes?

---

## By topic (each cell is a verified JAR paper above)

| Topic | Verified JAR exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Earnings informativeness / value relevance | Ball & Brown, "Empirical Evaluation of Accounting Income Numbers" | 1968, 6(2) | Returns–earnings event study |
| Information content of announcements | Beaver, "Information Content of Annual Earnings Announcements" | 1968, 6 | Volume / variance event study |
| Voluntary disclosure quality | Lang & Lundholm, "Analyst Ratings of Corporate Disclosures" | 1993, 31(2) | Cross-sectional determinants |
| Disclosure & cost of capital | Leuz & Verrecchia, "Economic Consequences of Increased Disclosure" | 2000, 38 | Regime-change quasi-experiment |
| Standard-setting / IFRS regulation | Daske, Hail, Leuz & Verdi, "Mandatory IFRS Reporting around the World" | 2008, 46(5) | Cross-country mandatory-adoption |
| Accruals / earnings-management measurement | Hribar & Collins, "Errors in Estimating Accruals" | 2002, 40(1) | Measurement-error methodology |

---

## Omitted for sibling-journal placement (do NOT attribute to JAR — guardrail)

To keep the list zero-hallucination, the following well-known accounting papers were **checked and
excluded** because web search placed them in a **sibling** journal, not JAR. They are the exact
misattribution traps the pack warns about (JAR ≠ TAR/JAE/CAR/RAST):

- **Dechow, Sloan & Sweeney, "Detecting Earnings Management" (1995)** — verified to be in
  ***The Accounting Review*** 70(2):193–225, **not JAR**. (A separately titled "Detecting Earnings
  Management: A New Approach," Dechow et al., did appear in JAR 2012, but that is a *different* paper and
  is not listed here without its own full verification.)
- **Li, "Annual Report Readability, Current Earnings, and Earnings Persistence" (2008)** — verified to be
  in the ***Journal of Accounting and Economics*** 45(2–3):221–247, **not JAR**.
- **Dechow & Dichev, "The Quality of Accruals and Earnings" (2002)** — verified to be in
  ***The Accounting Review*** 77(Suppl.):35–59, **not JAR**.
- **Burgstahler & Dichev, "Earnings Management to Avoid Earnings Decreases and Losses" (1997)** —
  verified to be in the ***Journal of Accounting and Economics*** 24(1):99–126, **not JAR**.
- **Frankel, McNichols & Wilson, "Discretionary Disclosure and External Financing" (1995)** — verified to
  be in ***The Accounting Review*** 70(1):135–150, **not JAR**.
- **Healy, Hutton & Palepu, "Stock Performance and Intermediation Changes Surrounding Sustained Increases
  in Disclosure" (1999)** — verified to be in ***Contemporary Accounting Research*** 16(3):485–520,
  **not JAR**.

Before adding any new paper to this library, confirm it on Wiley (`onlinelibrary.wiley.com`, DOI prefix
`10.1111/1475-679X` or `10.2307/...` for early JAR) or RePEc `bla:joares`, with volume(issue):pages, and
update the access-date header. When the venue cannot be cleanly confirmed as JAR, **omit**.
