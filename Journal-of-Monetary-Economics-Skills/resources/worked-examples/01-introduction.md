> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate *Journal of Monetary Economics* house style. No real-paper facts are stated,
> and no real policy is invoked. Corresponding skills:
> [`jme-writing-style`](../../skills/jme-writing-style/SKILL.md),
> [`jme-topic-selection`](../../skills/jme-topic-selection/SKILL.md),
> [`jme-contribution-framing`](../../skills/jme-contribution-framing/SKILL.md), and
> [`jme-identification-strategy`](../../skills/jme-identification-strategy/SKILL.md).

# Worked Example: A *JME*-Style Introduction (before → after)

This demonstrates the introduction arc the *Journal of Monetary Economics* rewards (from `jme-writing-style`
and `jme-topic-selection`): **macro/policy question → why it matters for monetary economics → identification
of the shock or mechanism → headline estimate with magnitude and interval → what it identifies and against
which rival → contribution with a policy or conceptual payoff → brief roadmap.** The governing rule from
`jme-writing-style` is **lead with the macro question and the number, demote the method to a tool**; note the
JME abstract convention (≤100 words, may not begin with "This paper" or "We") that the surrounding prose
should match in discipline.

**Illustrative paper (fictional):** *"Forward Guidance at the Effective Lower Bound: High-Frequency Evidence
from a Fictional Central Bank, 2009–2019."* Fictional setting: a fictional central bank's policy
announcements; "guidance surprises" are intraday changes in expected future short rates around the
announcement window that are orthogonal to the current-rate surprise.

---

## Before (buries the contribution — typical first-draft intro)

> Monetary policy and its effects have been studied extensively in macroeconomics. Many papers estimate
> vector autoregressions and local projections to measure how policy affects output and inflation. In this
> paper, we construct high-frequency surprises around central bank announcements and use them in a local
> projection to study the effects of forward guidance. We estimate several specifications and report
> impulse responses. Understanding the transmission of monetary policy is important for central banks.
> Section 2 reviews the literature, Section 3 describes the data, Section 4 presents the methods, Section 5
> reports results, and Section 6 concludes.

**What's wrong (against `jme-writing-style` / `jme-topic-selection` / `jme-contribution-framing`):**

- **Leads with method** ("we construct high-frequency surprises and use them in a local projection")
  instead of the macro question — the named anti-pattern in `jme-writing-style`.
- **No question and no answer on page one.** A reader cannot tell what the magnitude of the guidance effect
  is or why it matters for policy (fails the `jme-topic-selection` payoff test).
- **No headline estimate with magnitude or uncertainty** — violates the estimate-first norm.
- **Identification is asserted, not motivated.** What makes the guidance surprise *clean* of the
  contemporaneous policy surprise and of the central bank's information advantage is never argued (the
  `jme-identification-strategy` gap).
- **Contribution type is unclear** — a new estimate? a resolution of the "forward-guidance puzzle"? (the
  `jme-contribution-framing` test.)
- **Throat-clearing** and an **over-signposted roadmap**.

---

## After (*JME* arc — macro question + estimate + identification, contribution early)

> **At the effective lower bound, how much does *forward guidance* — as opposed to the current policy rate —
> actually move output, and is its effect as implausibly large as standard New Keynesian models predict?** We
> find that a guidance surprise lowering expected one-year-ahead short rates by 25 basis points raises
> industrial production by **0.9% at its 12-month peak (90% CI 0.4–1.4%)** — sizable, but **less than half**
> what a textbook model calibrated to the same announcement implies. *(Macro question + headline estimate
> with magnitude and interval, in the first breath.)*
>
> Identifying this is hard because announcement-window rate changes mix the policy signal with the central
> bank's private information about the economy: a guidance surprise that markets read as bad news about
> fundamentals would bias the output response toward zero or the wrong sign. *(Why it is hard — the
> information-effect problem stated in monetary terms, per `jme-identification-strategy`.)*
>
> We isolate guidance surprises as the component of intraday futures movements orthogonal to the
> current-rate surprise, and we purge the central bank's information advantage by projecting the surprises
> on its published forecast revisions and using the residual as the shock. We then trace dynamic effects
> with local projections, 2009–2019. We validate the cleaned shock by showing it does *not* forecast the
> central bank's own subsequent forecast revisions and is unpredictable from pre-announcement macro data.
> *(Identification in one paragraph; the shock is *defended* against the information effect, not merely
> named — per `jme-identification-strategy` / `jme-data-analysis`.)*
>
> The output response is **concentrated in interest-sensitive sectors and absent before the lower bound
> bound**, and it **survives dropping the information-effect correction only in sign, not magnitude** —
> precisely the pattern a genuine guidance channel, rather than an information leak, would produce.
> *(Headline result restated with the signature that separates the guidance channel from the information
> effect.)*
>
> Our contribution is to deliver a **credibly identified, information-robust estimate of the forward-guidance
> multiplier that is economically large but well below the model-implied value** — quantitative discipline on
> the "forward-guidance puzzle" rather than another puzzle-free calibration. *(Contribution stated early and
> against the specific rival, per `jme-contribution-framing`, with a direct payoff for how central banks
> should weight guidance.)* The information-purging design is **portable** to any high-frequency
> policy-shock setting where the central bank plausibly knows more than markets. *(Portability — the
> macro-knowledge payoff.)*
>
> The paper proceeds as follows. Section 2 places the result in the high-frequency-identification and
> forward-guidance-puzzle literatures and describes the announcement data; Section 3 develops the
> information-robust shock and the local-projection design; Section 4 reports the impulse responses, the
> sectoral heterogeneity, and robustness. *(Brief roadmap — no over-signposting.)*

---

## Why the "after" meets the *JME* bar

Mapped to the skill checklists:

- **Contribution front-loaded** — by the end of the first paragraph the reader has the macro question, the
  headline magnitude with a 90% interval, and what it identifies (`jme-writing-style`: lead with the question
  and the number).
- **Estimate-first prose** — the headline (0.9% peak; 90% CI 0.4–1.4%) leads with magnitude **and
  uncertainty**, then is interpreted, rather than "the impulse responses show…" (`jme-data-analysis`: report
  intervals around IRFs, not bare point paths).
- **Clear policy/conceptual payoff** — it disciplines the forward-guidance puzzle and informs how much weight
  guidance deserves, satisfying the `jme-topic-selection` payoff test.
- **Identification is motivated and defended** — the information effect is named, the orthogonalization and
  forecast-residual purge are argued, and the shock is validated (the `jme-identification-strategy`
  standard), not asserted.
- **The strongest rival is named and adjudicated** — an information-effect story would imply the surprise
  forecasts the bank's own revisions and a wrong-signed or pre-ELB response; the data show the opposite
  (`jme-identification-strategy` adjudication: "if the rival were true… instead it looks like ___").
- **Contribution type is explicit** — a **credibly identified estimate that resolves a quantitative puzzle**,
  the `jme-contribution-framing` move of turning "a paper about forward guidance" into "the first
  information-robust estimate that Y."
- **Method is demoted to a tool** — the high-frequency-surprise and local-projection machinery appears only
  where the design is described, never as the lead (avoids the `jme-writing-style` "leading with the method"
  anti-pattern).

> Next: adapt the reproducible analysis skeleton in [`../code/`](../code/) when turning this introduction arc
> into a full empirical workflow, and pressure-test the design against
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
