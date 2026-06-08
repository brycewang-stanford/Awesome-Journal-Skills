# CAR Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked against Wiley Online
> Library's *Contemporary Accounting Research* article pages (`onlinelibrary.wiley.com/.../1911-3846...`,
> the journal's DOI prefix / ISSN family) to confirm it actually appeared in **Contemporary Accounting
> Research** — the journal of the **Canadian Academic Accounting Association (CAAA)**, published by
> **Wiley** — with year and volume(issue):pages. Candidates that could not be fully verified *as CAR* were
> **omitted** (see the guardrail list): a short, clean, verified list beats a long, uncertain one.
>
> **Sibling-confusion guard (do not misattribute).** CAR is **not** *The Accounting Review* (TAR), the
> *Journal of Accounting Research* (JAR), the *Journal of Accounting and Economics* (JAE), or the *Review
> of Accounting Studies* (RAST). Several of those siblings publish on the exact same topics (segment
> disclosure, tax avoidance, audit judgment, analytical disclosure), so each entry below was confirmed on
> the CAR article page specifically, not by topic match.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent regression coefficients, treatment effects, or specific findings — read the original
> on Wiley Online Library before citing any number. For CAR-specific policy, scope, blinding, and abstract
> rules, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper earns a place in a
*method-agnostic, all-topic-areas-of-accounting* journal — the CAR bar (see
[`../../skills/car-topic-selection/SKILL.md`](../../skills/car-topic-selection/SKILL.md) and
[`../../skills/car-contribution-framing/SKILL.md`](../../skills/car-contribution-framing/SKILL.md)). For
each, ask the self-check question before claiming your paper is "CAR-shaped." The
[shared reviewer-objection checklist](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
and [reporting standards](../../../shared-resources/empirical-methods/reporting-standards.md) cover the
venue-neutral design and inference stakes; defer to this pack's skills for what *CAR specifically* wants.

---

## By method

### Archival / capital-markets — voluntary disclosure & information asymmetry

- **Marquardt & Wiedman, "Voluntary Disclosure, Information Asymmetry, and Insider Selling through
  Secondary Equity Offerings," CAR 1998, 15(4):505–537.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.1111/j.1911-3846.1998.tb00569.x`.
  - **Why it is an exemplar:** ties a disclosure choice (management forecasts) to information asymmetry and
    an insider's trading incentive — the contribution is an *accounting* relation (disclosure ↔ asymmetry),
    not a generic finance event study. A clean template for defending the accounting locus
    (`car-literature-positioning`).
  - **Self-check:** does your archival relation pin down something about accounting *information*, rather
    than use accounting data as a convenience proxy for a pure-finance question?

### Archival / capital-markets — earnings management as a disclosure behavior

- **Bratten, Payne & Thomas, "Earnings Management: Do Firms Play 'Follow the Leader'?," CAR 2016,
  33(2):616–643.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.1111/1911-3846.12157`.
  - **Why it is an exemplar:** reframes discretionary reporting as *strategic and interdependent* — a
    firm's earnings management responds to peers' reported performance — turning a familiar construct into
    a sharper question with cross-sectional bite (`car-theory-development`'s "the moderators are where the
    theory lives").
  - **Self-check:** does your earnings-quality / earnings-management paper offer a mechanism and
    cross-sectional prediction, not just another association with discretionary accruals?

### Archival — tax avoidance & incentives

- **Gaertner, "CEO After-Tax Compensation Incentives and Corporate Tax Avoidance," CAR 2014,
  31(4):1077–1102.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.1111/1911-3846.12058`.
  - **Why it is an exemplar:** links a compensation-design feature (evaluating the CEO on after-tax income)
    to a measurable tax-avoidance outcome — an identified, incentive-grounded accounting relation that
    speaks to both research and compensation/governance practice (`car-contribution-framing`'s
    practice-implication requirement). Adaptable to the panel-archival chain in
    [`../code/stata/03_did_modern.do`](../code/stata/03_did_modern.do).
  - **Self-check:** is your tax result driven by a credibly identified incentive or institutional feature,
    rather than a correlation between two endogenous firm choices?

### Experiment — auditor judgment & decision-making

- **Griffith, Kadous & Young, "Improving Complex Audit Judgments: A Framework and Evidence," CAR 2021,
  38(3):2071–2104.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.1111/1911-3846.12658`.
  - **Why it is an exemplar:** specifies the *psychological process* (when auditors recognize the need for
    analytical vs. heuristic processing) and designs predictions that isolate it — causal evidence on a
    process archival data cannot deliver, the signature of a strong CAR experiment
    (`car-methods` / `car-theory-development`).
  - **Self-check:** does your experiment theorize and test a mediator/boundary condition, so the
    manipulation isolates the construct rather than just moving the dependent variable?

### Analytical / modeling — voluntary disclosure under control concerns

- **Arya & Ramanan, "Voluntary Disclosure in Light of Control Concerns," CAR 2021, 38(4):2824–2850.**
  Verified: `onlinelibrary.wiley.com/doi/10.1111/1911-3846.12717`.
  - **Why it is an exemplar:** the model *is* the theory — an entrepreneur-owner's disclosure trades off
    valuation against control, yielding an equilibrium that rationalizes disclosure patterns and a testable
    implication. Shows CAR publishes analytical work when the economic insight is first-order
    (`car-theory-development`, analytical track).
  - **Self-check:** does your model deliver one memorable economic insight (a trade-off or equilibrium that
    rationalizes a puzzle) with an institutional implication, not just comparative statics?

### Analytical / modeling — disclosure to investors under endowment uncertainty

- **Gao & Zhang, "A Theory of Investors' Disclosure," CAR 2026, 43(1):266–289.**
  Verified: `onlinelibrary.wiley.com/doi/10.1111/1911-3846.70017`.
  - **Why it is an exemplar:** moves the disclosure model from *firms* to *investors* — an investor with
    uncertain information endowment chooses how much of their findings to reveal after trading — a
    contemporary illustration that the analytical-disclosure conversation in CAR is still generative.
  - **Self-check:** does your model reframe *who* discloses or *what* the friction is, rather than re-derive
    a known unraveling/withholding result?

---

## By topic (each cell is a verified CAR paper above)

| Topic | Verified CAR exemplar | Year, vol(issue):pp | Method |
| --- | --- | --- | --- |
| Voluntary disclosure & information asymmetry | Marquardt & Wiedman, "Voluntary Disclosure… Insider Selling" | 1998, 15(4):505–537 | Archival |
| Earnings management | Bratten, Payne & Thomas, "Follow the Leader?" | 2016, 33(2):616–643 | Archival |
| Taxation & incentives | Gaertner, "CEO After-Tax Compensation Incentives…" | 2014, 31(4):1077–1102 | Archival |
| Auditing / judgment & decision-making | Griffith, Kadous & Young, "Improving Complex Audit Judgments" | 2021, 38(3):2071–2104 | Experiment |
| Disclosure (control concerns) | Arya & Ramanan, "Voluntary Disclosure in Light of Control Concerns" | 2021, 38(4):2824–2850 | Analytical |
| Disclosure (investor-side) | Gao & Zhang, "A Theory of Investors' Disclosure" | 2026, 43(1):266–289 | Analytical |

This spans **four traditions** (archival, experimental, analytical) across **five accounting topic
areas** (disclosure, earnings management, tax, auditing, capital-markets) — a deliberate cross-section of
CAR's big-tent, method-agnostic mandate rather than an exhaustive census.

---

## Omitted for lack of full CAR verification (do not attribute to CAR without re-checking)

To keep the list zero-hallucination and sibling-confusion-proof, the following were **excluded** after
checking:

- **Lang & Lundholm, "Voluntary Disclosure and Equity Offerings: Reducing Information Asymmetry or Hyping
  the Stock?"** — this *is* a CAR paper (2000, 17(4)), but it surfaced alongside its CAR *Discussion*
  (Wiedman 2000) and several near-identically-titled JAR disclosure papers; to avoid conflating the
  article with its discussion and with the JAR siblings, it is held out pending a single clean
  volume(issue):pages confirmation. Re-verify before adding.
- **Hsieh/Klenow-style misallocation and Beyer et al., "Voluntary Disclosure, Manipulation, and Real
  Effects"** — the latter is a strong analytical-disclosure match but was verified to be in the **Journal
  of Accounting Research** (JAR 2012, 50(5)), **not CAR**. Listed here only as a sibling-confusion
  guardrail.
- **De Simone et al., "How Reliably Do Empirical Tests Identify Tax Avoidance?"** — appears on the CAR
  page (2020) but is a methods/measurement piece; omitted from the topic exemplars only because the six
  above already cover tax with a cleaner design exemplar, not because of any attribution doubt.

Before adding any new paper to this library, confirm it on `onlinelibrary.wiley.com` under the
*Contemporary Accounting Research* journal (article page with volume(issue):pages and the `1911-3846` DOI
family), check it is not actually TAR / JAR / JAE / RAST, and update the access-date header. When in
doubt, omit.
