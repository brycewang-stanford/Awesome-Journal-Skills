> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate Journal of Finance (JF) house style. No real-paper facts are stated.
> Corresponding skills: [`jf-writing-style`](../../skills/jf-writing-style/SKILL.md),
> [`jf-topic-selection`](../../skills/jf-topic-selection/SKILL.md),
> [`jf-literature-positioning`](../../skills/jf-literature-positioning/SKILL.md), and
> [`jf-identification`](../../skills/jf-identification/SKILL.md).

# Worked Example: A JF-Style Introduction (before → after)

This demonstrates the **JF introduction arc** from `jf-writing-style`, where the first ~3 pages do the
work: **(1) the question and why it matters** (general-interest, concrete) → **(2) what you do**
(design/data/test in plain terms) → **(3) what you find** (headline result with its **economic
magnitude** in interpretable units) → **(4) why it is credible** (the source of variation) →
**(5) contribution** (closest papers and your delta, per `jf-literature-positioning`) → **(6) brief
roadmap**. The JF rule: a reader who stops at page 3 should know the question, the answer, its size, and
why to believe it — framed for the broad AFA reader, not one subfield.

**Illustrative paper (fictional):** *"Covenant-Lite Loans and Corporate Risk-Taking: Evidence from a
Staggered Lender-Disclosure Reform."* Fictional setting: a reform that, in different years, required
syndicated-loan lenders in different U.S. states to disclose covenant terms, sharply raising the
prevalence of covenant-lite loans for affected borrowers.

---

## Before (buries the idea — typical first-draft intro)

> A large literature in corporate finance studies the relationship between debt structure and firm
> behavior. Many papers examine covenants, leverage, and creditor control. In this paper, we use a
> Callaway and Sant'Anna (2021) staggered difference-in-differences estimator, supplemented with the
> Sun and Abraham (2021) interaction-weighted estimator, to study the effect of covenant-lite lending on
> corporate risk-taking. We assemble a panel of borrowers and estimate event-study specifications.
> Creditor governance is significant at the 1% level and is an important topic for the literature.
> Section 2 reviews the literature, Section 3 describes the data, Section 4 presents the empirical
> strategy, Section 5 reports results, and Section 6 concludes.

**What's wrong (against `jf-writing-style` / `jf-topic-selection` / `jf-literature-positioning`):**

- **Leads with method** ("we use a Callaway and Sant'Anna estimator") instead of the question — the named
  "leading with the estimator" anti-pattern in both `jf-writing-style` and `jf-identification`.
- **No question, answer, or economic magnitude in the first ~3 pages.** A broad AFA reader — an
  asset-pricing reader as much as a corporate one — cannot tell what was found or why it matters.
- **Reports "significant at the 1% level" as if it were the finding** — flagged anti-pattern; JF wants
  the magnitude in interpretable units, not a t-stat dressed up as a result.
- **Throat-clearing** ("a large literature," "an important topic") with vague stakes and three sentences
  of survey before the question.
- **Contribution is not stated**: no closest papers, no delta, no classification as new fact / mechanism
  / method (`jf-literature-positioning`).
- **Source of identifying variation never named** in one sentence (`jf-identification`).
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (JF arc — question + answer + magnitude up front, identification named, contribution early)

> **Does easing creditor control over borrowers make firms take more risk — and does that risk show up
> as value creation or value destruction?** We show that a shift toward covenant-lite lending raises
> borrowers' asset volatility by **18%** and their R&D-to-assets ratio by **2.3 percentage points**, but
> lowers the average announcement return on their subsequent acquisitions by **140 basis points** — risk
> that is taken, but not rewarded. *(question + headline answer + why it matters, with magnitudes in
> interpretable economic units, in the first breath.)*
>
> Isolating this is hard because covenant-lite terms are not handed out at random: lenders relax
> covenants precisely for borrowers whose prospects are already improving, so a naive comparison
> conflates loosened creditor control with the good news that prompted it. *(why it is credible begins
> with naming the endogeneity threat — `jf-identification`.)*
>
> We exploit a reform that required syndicated-loan lenders to disclose covenant terms, rolled out across
> U.S. states in **different years**, which sharply raised covenant-lite prevalence for affected
> borrowers for reasons unrelated to any single borrower's outlook. The staggered timing lets us compare
> each borrower to not-yet-affected borrowers, and we find no differential pre-trends in volatility
> before a borrower's state adopts the rule. *(source of identifying variation named in one sentence;
> testable assumption shown.)*
>
> The effects are economically large and concentrated where theory predicts: risk-taking rises most for
> firms with weak boards and ample free cash flow, and the value-destroying acquisitions are precisely
> those creditors would previously have blocked. The full battery of pre-trend tests, alternative
> estimators, and a manipulation check is reported in the Internet Appendix. *(magnitude interpreted, not
> just significance; heavy diagnostics offloaded, keeping the body within the 60-page limit.)*
>
> We contribute to the literature on **creditor control and corporate investment** (Chava and Roberts
> 2008), which shows that covenant violations transfer control to creditors and curb investment; we show
> the *converse margin* — that relaxing covenant control ex ante unleashes risk-taking that managers,
> not creditors, choose. We also speak to **managerial behavior** (Malmendier and Tate 2005) by showing
> the released risk-taking is strongest among the firms most prone to overinvestment. *(contribution
> stated early, naming the closest papers and the specific delta; classified as a new mechanism — per
> `jf-literature-positioning`, with canon attributed to the correct journal.)*
>
> The paper proceeds as follows. Section 2 describes the reform and data; Section 3 presents the design
> and main results; Section 4 examines the risk-taking mechanism. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the JF bar

Mapped to the skill checklists:

- **Question + finding + economic magnitude in the first ~3 pages** — the JF funnel; the headline numbers
  (18% volatility; +2.3 pp R&D; −140 bps announcement return) appear immediately, in interpretable units
  (`jf-writing-style`: "headline number in interpretable economic units," not a t-stat).
- **General-interest framing** — the question (does weakening creditor control create or destroy value?)
  is legible to a corporate-finance *and* an asset-pricing reader, clearing the `jf-topic-selection`
  broad-interest bar rather than reading as a narrow covenants paper.
- **Source of identifying variation named in one sentence** and the endogeneity threat stated before the
  design — the `jf-identification` requirement; the staggered disclosure reform is the named shock, and
  no-pre-trends is asserted plainly.
- **Method demoted to a tool**, mentioned only where the design is discussed, never as the lead (avoids
  the shared "leading with the estimator" anti-pattern across `jf-writing-style` and `jf-identification`).
- **Contribution stated early, relative to specific prior work** ("the converse margin" of Chava and
  Roberts 2008), classified as a **new mechanism**, not "we contribute to the literature"
  (`jf-literature-positioning`).
- **Significance vs. magnitude discipline** — "significant" is reserved for economic importance; the draft
  never substitutes a p-value for the finding.
- **Body within the 60-page limit** — the diagnostic battery is offloaded to the Internet Appendix
  (`jf-internet-appendix`), not padded into the body.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for verified real JF papers whose intros
> execute this arc (including Chava and Roberts 2008 and Malmendier and Tate 2005, both referenced above),
> and [`../code/`](../code/) for the staggered-DID and event-study command chain
> (`03_did_modern.do`) and the RDD/manipulation checks (`05_rdd.do`) the design above relies on.
