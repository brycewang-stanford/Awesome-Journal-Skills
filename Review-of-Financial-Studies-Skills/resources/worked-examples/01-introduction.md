> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate RFS house style. No real-paper facts are stated, and no journal policy is
> invented here — RFS-specific rules cited (≤100-word abstract; Chicago author-date references;
> desk-screen before referees) are drawn from this pack's own
> [`rfs-writing-style`](../../skills/rfs-writing-style/SKILL.md) skill. Corresponding skills:
> [`rfs-writing-style`](../../skills/rfs-writing-style/SKILL.md),
> [`rfs-topic-selection`](../../skills/rfs-topic-selection/SKILL.md),
> [`rfs-literature-positioning`](../../skills/rfs-literature-positioning/SKILL.md), and
> [`rfs-identification`](../../skills/rfs-identification/SKILL.md).

# Worked Example: An RFS-Style Introduction (before → after)

This demonstrates the **RFS introduction formula** from `rfs-writing-style`:
**hook (question + why now) → what we do (design + source of variation) → what we find (headline
magnitude + a robustness clause) → why it is new (explicit delta vs. the closest work) → mechanism /
interpretation → brief roadmap** — under the binding RFS constraints that an **Editor desk-screens
before referees, so the contribution must land before page three**, the **abstract is ≤ 100 words**, and
references follow **Chicago Manual of Style author-date** format.

**Illustrative paper (fictional):** *"Margin Calls and the Allocation of Credit: Evidence from a
Collateral-Haircut Shock."* Fictional setting: a clearing house that, for operational reasons unrelated
to firm fundamentals, raised collateral haircuts on one class of corporate bonds in a single year,
tightening the funding of the dealers who hold them.

---

## Before (buries the contribution — typical first-draft intro)

> The literature has long debated the relationship between funding conditions and asset markets. Many
> papers study liquidity, leverage, and intermediary balance sheets. In this paper, we use a
> difference-in-differences design with two-way fixed effects to study how a change in collateral
> haircuts affects corporate bond markets. We assemble a panel of bonds and dealers and estimate
> event-study specifications, controlling for a rich set of bond and issuer characteristics. Funding
> liquidity is an important topic. Section 2 reviews the literature, Section 3 describes the data,
> Section 4 presents the empirical strategy, Section 5 reports results, Section 6 discusses robustness,
> and Section 7 concludes.

**What's wrong (against `rfs-writing-style` / `rfs-topic-selection` / `rfs-identification`):**

- **Opens with "the literature has long debated"** — the exact anti-pattern named in `rfs-writing-style`;
  the new question and answer are nowhere on page one, so the paper risks a **desk reject before page
  three**.
- **Leads with the method**, not the question — `rfs-identification` flags method-first framing.
- **No headline magnitude** in interpretable units anywhere in the intro (`rfs-writing-style`: report
  *economic magnitudes*, not only significance).
- **"controlling for a rich set of … characteristics"** signals the "we control, so it is causal"
  anti-pattern from `rfs-identification`; the **source of exogenous variation is never named**.
- **No explicit delta** vs. the closest paper (`rfs-literature-positioning`).
- **Over-signposted 7-section roadmap** doing the work the argument should do.

---

## After (RFS formula — contribution legible in the first two pages)

> **When a dealer's funding tightens, does the cost fall on the assets that are hardest to fund — and
> does that distort which firms get credit?** We show that a one-off increase in collateral haircuts on a
> class of corporate bonds raised those bonds' yield spreads by **38 basis points** and cut net new
> issuance by the affected issuers by **11%**, even though the issuers' fundamentals did not change.
> *(hook: first-order question + headline magnitude, in the first breath.)*
>
> Identifying this is hard because haircuts and funding stress usually move *with* the fundamentals of
> the assets they apply to: collateral terms tighten precisely when the underlying credits deteriorate,
> so a naive comparison conflates the funding shock with the deterioration that triggered it. *(why it is
> hard — the endogeneity threat, per `rfs-identification`.)*
>
> We exploit a clearing house's decision to raise haircuts on one bond class in a single year for
> **operational reasons unrelated to issuer fundamentals**, which sharply tightened the funding of the
> dealers holding those bonds while leaving otherwise-similar bonds untouched. We compare affected and
> unaffected bonds around the change in a difference-in-differences design, verify parallel pre-trends in
> spreads, and confirm the result in a placebo that randomizes the treatment date. *(what we do: design +
> the named, exogenous source of variation + the diagnostic, in one paragraph.)*
>
> Affected spreads rise **38 basis points** (relative to a pre-shock mean of 142) and the effect grows
> over the four quarters after the shock and is absent before it; issuance by affected issuers falls
> **11%**, concentrated among issuers with no substitute funding source. The estimates are robust to
> dropping the largest dealers and to dealer-time fixed effects. *(what we find: magnitude restated, with
> the key robustness in a clause.)*
>
> Our contribution is to identify the **allocation** consequence of a funding shock, not only its price
> effect: the shock changes no issuer's fundamentals, yet it reallocates credit away from firms whose
> bonds happen to be expensive to fund. The closest prior work documents that funding and market
> liquidity reinforce each other in *prices*; we provide the first **issuer-level** evidence that the
> spiral reaches the **real allocation of credit**, which earlier data could not see. *(why it is new:
> an explicit, falsifiable delta vs. the closest paper, per `rfs-literature-positioning`.)* This embeds a
> testable prediction of the funding-liquidity channel — that the burden falls on the hardest-to-fund
> collateral — and confirms it directly. *(mechanism / theory–empirics integration.)*
>
> The paper proceeds as follows. Section 2 describes the haircut change and data; Section 3 presents the
> design and main results; Section 4 examines the issuer-level allocation mechanism and robustness.
> *(brief roadmap — two sentences, no over-signposting.)*

---

## A compliant abstract (≤ 100 words, leads with question + finding)

> We ask whether a funding shock to dealers distorts the real allocation of corporate credit, not only
> bond prices. Exploiting a clearing house's operational increase in collateral haircuts on one bond
> class — unrelated to issuer fundamentals — we compare affected and unaffected bonds in a
> difference-in-differences design. Affected yield spreads rise 38 basis points and net issuance by
> affected issuers falls 11%, with effects concentrated among issuers lacking substitute funding. The
> estimates survive placebo and dealer-time-fixed-effects checks. We provide the first issuer-level
> evidence that funding–liquidity spirals reach the allocation of credit, extending price-level findings
> to real outcomes.

*(Word count is held under the RFS 100-word cap from `rfs-writing-style`; it leads with the question and
the finding, states design and magnitude, and ends with the contribution.)*

---

## Why the "after" meets the RFS bar

Mapped to the skill checklists:

- **Contribution legible in the first two pages** — the headline magnitude (38 bps; 11%) appears in
  paragraph one, satisfying `rfs-writing-style` ("headline result appears with economic magnitude on
  page 1–2") and surviving the desk screen.
- **Source of exogenous variation named in one sentence** — the operational haircut change — meeting the
  first item on the `rfs-identification` checklist; **parallel-trends and a placebo** are stated, not the
  "we control, so it is causal" anti-pattern.
- **Explicit, falsifiable delta** ("first issuer-level evidence that the spiral reaches the *allocation*
  of credit") rather than "we add to the literature on liquidity" — the `rfs-literature-positioning`
  delta type "new question / allocation vs. pricing."
- **Theory and empirics integrated** — the funding-liquidity prediction is stated, then tested, then
  confirmed, per `rfs-writing-style` and the `rfs-topic-selection` "mutually reinforcing" rule.
- **Contribution-claim template filled** (`rfs-topic-selection`): question → wedge ("prior work studied
  prices, could not see issuer-level allocation") → what we do → quantified finding → why it matters.
- **Method demoted to a tool**, mentioned only where the design is discussed; the abstract clears the
  **100-word cap** and the prose is active-voice, one-idea-per-sentence.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **verified real RFS papers** whose
> intros execute this arc, and [`../code/`](../code/) for the staggered-DID and RDD command chains
> referenced above (e.g. [`../code/stata/03_did_modern.do`](../code/stata/03_did_modern.do),
> [`../code/stata/05_rdd.do`](../code/stata/05_rdd.do)).
