# *Journal of Banking & Finance* Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in the **_Journal of Banking & Finance_** (JBF) — the Elsevier banking-and-finance
> field journal (ISSN 0378-4266) — with year and volume/issue, against the publisher record on
> ScienceDirect (`sciencedirect.com/.../journal-of-banking-and-finance`), the IDEAS/RePEc series record
> (`ideas.repec.org/a/eee/jbfina/...`), EconPapers, and corroborating Google Scholar lookups carrying the
> journal name. Papers without full verification **as JBF** were **omitted** — this is deliberately
> a short, clean list, not a long, uncertain one.
>
> **Publisher / identity.** JBF is published by **Elsevier** and handled through Editorial Manager; first
> submission permits any complete, consistent reference style and proof-stage style is numbered Elsevier.
> For JBF-specific scope, fees, blinding, and house style, see
> [`../official-source-map.md`](../official-source-map.md).
>
> **Sibling-journal guard (read this before citing anything).** JBF is a strong field journal, but it sits
> **below the top three** finance outlets — the **_Journal of Finance_ (JF)**, **_Review of Financial
> Studies_ (RFS)**, and **_Journal of Financial Economics_ (JFE)**. Many of the most famous
> "banking" and "corporate-finance" papers people *think* are in JBF are actually in one of those three,
> or in **_Journal of Money, Credit and Banking_ (JMCB)**, the **_World Bank Economic Review_ (WBER)**, or
> **_Journal of Financial Intermediation_ (JFI)** — a sibling in this very repo. The
> [Omitted](#omitted-for-lack-of-full-verification-do-not-attribute-to-jbf) section records the specific
> traps checked and rejected. When a paper "feels canonical," that is a signal to **suspect JF/RFS/JFE**,
> not JBF.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent coefficients, basis points, or specific findings — read the original on ScienceDirect
> before citing any number.

---

## How to use this library

Pick the row whose **method × banking question** is closest to yours, then study how that paper turns a
bank/firm quantity into a contribution that survives the JBF credibility bar — *make the identifying
variation visible and translate coefficients into economics* (see
[`../../skills/jbf-identification-strategy/SKILL.md`](../../skills/jbf-identification-strategy/SKILL.md),
[`../../skills/jbf-writing-style/SKILL.md`](../../skills/jbf-writing-style/SKILL.md), and
[`../../skills/jbf-contribution-framing/SKILL.md`](../../skills/jbf-contribution-framing/SKILL.md)). For
each, ask the self-check question before claiming your paper is "JBF-shaped."

---

## By method

### Simultaneous-equations model confronting reverse causality (capital structure / bank performance)

- **Berger & Bonaccorsi di Patti, "Capital structure and firm performance: A new approach to testing agency theory and an application to the banking industry," _Journal of Banking & Finance_ 2006, 30(4):1065–1102.**
  Verified: RePEc `ideas.repec.org/a/eee/jbfina/v30y2006i4p1065-1102.html`; EconPapers `article/eeejbfina/v_3a30_3ay_3a2006`; ScienceDirect `pii/S0378426605001093`.
  - **Why it is an exemplar:** the headline threat is **reverse causality** — performance can drive
    leverage as easily as leverage drives performance — so the authors estimate a **simultaneous-equations
    system** with profit efficiency as the performance benchmark instead of reading a single OLS
    coefficient as causal. That is the
    [`jbf-identification-strategy`](../../skills/jbf-identification-strategy/SKILL.md) "name the core threat,
    then build the design that defeats it" move, applied to an endogenous regressor.
  - **Self-check:** if performance could plausibly *cause* your key regressor, does your design (system
    estimation, lags, instruments) break that loop rather than assume it away?

### Portfolio decomposition of a risk-return claim (bank diversification / non-interest income)

- **Stiroh & Rumble, "The dark side of diversification: The case of US financial holding companies," _Journal of Banking & Finance_ 2006, 30(8):2131–2161.**
  Verified: RePEc `ideas.repec.org/a/eee/jbfina/v30y2006i8p2131-2161.html`; ScienceDirect `pii/S0378426605001342`.
  - **Why it is an exemplar:** separates a **diversification-gain** component from an **exposure-shift**
    component, showing the two can offset so that the headline "diversification helps" claim reverses on a
    risk-adjusted basis. The contribution is a clean decomposition that names what a naïve average hides —
    the [`jbf-contribution-framing`](../../skills/jbf-contribution-framing/SKILL.md) "distinguish the
    channel prior work conflated" payoff, with the result expressed in risk-adjusted-return terms per
    [`jbf-writing-style`](../../skills/jbf-writing-style/SKILL.md).
  - **Self-check:** does your finding decompose a composite effect into offsetting channels, rather than
    report a net sign that buries the mechanism?

### Bank panel risk regression with heterogeneity splits (income structure / insolvency risk)

- **Lepetit, Nys, Rous & Tarazi, "Bank income structure and risk: An empirical analysis of European banks," _Journal of Banking & Finance_ 2008, 32(8):1452–1467.**
  Verified: RePEc `ideas.repec.org/a/eee/jbfina/v32y2008i8p1452-1467.html`; EconPapers `article/eeejbfina/v_3a32_3ay_3a2008`; ScienceDirect `pii/S0378426607...`.
  - **Why it is an exemplar:** a European bank **panel** relating insolvency-risk measures to income mix,
    then splitting non-interest income into **trading vs. fee/commission** and by **bank size** so the
    average relationship is shown to be driven by a specific subgroup. That is exactly the
    [`jbf-identification-strategy`](../../skills/jbf-identification-strategy/SKILL.md) bank-panel checklist
    (unit, fixed effects, clustering) plus the heterogeneity test that ties the estimate to a finance
    mechanism rather than a pooled coefficient.
  - **Self-check:** when you split your sample by the dimension theory predicts, does the effect
    concentrate where the mechanism says it should — or does it dissolve?

### Cross-sectional event study with institutional moderator (bank M&A / announcement returns)

- **Hagendorff, Collins & Keasey, "Investor protection and the value effects of bank merger announcements in Europe and the US," _Journal of Banking & Finance_ 2008, 32(7):1333–1348.**
  Verified: RePEc `ideas.repec.org/a/eee/jbfina/v32y2008i7p1333-1348.html`; ScienceDirect `pii/S0378426607003482`; SSRN `abstract_id=1093728`.
  - **Why it is an exemplar:** a textbook **event study** (define event, window, benchmark, CARs) whose
    contribution is not the CARs themselves but their **interaction with target-country investor
    protection** — the cross-section of abnormal returns is regressed on an institutional moderator. This
    is the [`jbf-identification-strategy`](../../skills/jbf-identification-strategy/SKILL.md) event-study
    spec done right, *and* the [`jbf-contribution-framing`](../../skills/jbf-contribution-framing/SKILL.md)
    move of turning a stylized fact into a conditional, theory-linked claim.
  - **Self-check:** is your event study's contribution the *moderator* of abnormal returns (why they vary),
    not just the existence of an announcement effect everyone already expects?

### Cash-flow-sensitivity panel for an internal-mechanism claim (internal capital markets / bank lending)

- **Houston & James, "Do bank internal capital markets promote lending?," _Journal of Banking & Finance_ 1998, 22(6–8):899–918.**
  Verified: ScienceDirect `pii/S0378426698000090`; Google Scholar lookup (journal *Journal of Banking and Finance*, vol. 22, pp. 899–918); RePEc `eee/jbfina`.
  - **Why it is an exemplar:** tests whether subsidiary loan growth tracks the **holding company's** cash
    flow and capital rather than the subsidiary's own — a sensitivity design that makes an *internal*
    mechanism (capital allocation across affiliates) observable in the data. The
    [`jbf-data-analysis`](../../skills/jbf-data-analysis/SKILL.md) pattern of building a regressor that
    *only* the proposed mechanism would move.
  - **Self-check:** does your specification isolate a sensitivity that the hypothesized internal mechanism
    predicts and a rival (stand-alone funding) does not?

---

## By topic (each cell is a verified _JBF_ paper above)

| Topic | Verified _JBF_ exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Capital structure & bank performance | Berger & Bonaccorsi di Patti, "Capital structure and firm performance" | 2006, 30(4) | Simultaneous equations (reverse-causality) |
| Diversification & non-interest income | Stiroh & Rumble, "The dark side of diversification" | 2006, 30(8) | Portfolio risk-return decomposition |
| Income structure & bank risk | Lepetit, Nys, Rous & Tarazi, "Bank income structure and risk" | 2008, 32(8) | Bank panel risk regression + heterogeneity |
| Bank M&A / valuation | Hagendorff, Collins & Keasey, "Investor protection and bank merger announcements" | 2008, 32(7) | Event study + institutional moderator |
| Internal capital markets & lending | Houston & James, "Do bank internal capital markets promote lending?" | 1998, 22(6–8) | Cash-flow-sensitivity panel |

---

## Omitted for lack of full verification (do not attribute to _JBF_ without re-checking)

To keep the list zero-hallucination, these strong candidates were **excluded** after web-checking — each
is a real, important paper, but **not in JBF** (the sibling-journal traps the brief warned of). The top-3
finance journals (JF / RFS / JFE) are where most "famous banking" papers actually live:

- **Laeven & Levine, "Is there a diversification discount in financial conglomerates?" (2007)** — verified
  in the **_Journal of Financial Economics_** 85(2):331–367, **not JBF**. The canonical financial-
  conglomerate discount paper.
- **Houston, James & Marcus, "Capital market frictions and the role of internal capital markets in
  banking" (1997)** — verified in the **_Journal of Financial Economics_** 46(2):135–164, **not JBF**.
  (Easy to confuse with the genuinely-JBF Houston & James 1998 above — different paper, different venue.)
- **Beck, Demirgüç-Kunt & Maksimovic, "Financial and Legal Constraints to Growth: Does Firm Size Matter?"
  (2005)** — verified in **_The Journal of Finance_** 60(1):137–177, **not JBF**.
- **Demirgüç-Kunt & Huizinga, "Determinants of Commercial Bank Interest Margins and Profitability: Some
  International Evidence" (1999)** — verified in the **_World Bank Economic Review_** 13(2):379–408, **not
  JBF**. A staple bank-margins reference that is constantly mis-cited to JBF.
- **Stiroh, "Diversification in Banking: Is Noninterest Income the Answer?" (2004)** — verified in the
  **_Journal of Money, Credit and Banking_** 36(5):853–882, **not JBF**. (His *other* diversification
  paper, Stiroh & Rumble 2006, *is* in JBF — see above. Do not merge them.)

Before adding any new paper to this library, confirm it on ScienceDirect (or the
`ideas.repec.org/a/eee/jbfina/...` RePEc record) with volume/issue, and update the access-date header.
When in doubt — especially when a banking paper "feels canonical" — **suspect JF/RFS/JFE and omit**.
