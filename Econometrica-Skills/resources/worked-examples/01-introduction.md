> **Illustrative teaching example.** The paper, model, estimator, and every symbol and number below are
> **fictional** and exist only to demonstrate Econometrica house style. No real-paper facts are stated, and
> no journal policy is invented (for venue facts see [`../official-source-map.md`](../official-source-map.md)).
> Corresponding skills: [`ecta-writing-style`](../../skills/ecta-writing-style/SKILL.md),
> [`ecta-topic-selection`](../../skills/ecta-topic-selection/SKILL.md),
> [`ecta-theory-model`](../../skills/ecta-theory-model/SKILL.md),
> [`ecta-identification`](../../skills/ecta-identification/SKILL.md), and
> [`ecta-literature-positioning`](../../skills/ecta-literature-positioning/SKILL.md).

# Worked Example: An Econometrica-Style Introduction (before → after)

This demonstrates the **Econometrica introduction arc** from `ecta-writing-style`:
**problem → informal statement of the main result (a theorem or estimator-plus-asymptotics) → why it is hard
→ how the proof works → precise relation to the closest prior result → brief roadmap.** The governing house
rule (`ecta-writing-style`): the introduction *reaches the contribution — ideally an informal statement of
the main theorem — quickly*, then explains the difficulty and the proof architecture. This is a **terse,
formal register** for a specialist reader, not the narrative "question → answer → why-it-matters" funnel that
suits AER / QJE / JPE / REStud. The contribution must be the **estimator / theorem / identification argument
itself**, not an application of an off-the-shelf method (`ecta-topic-selection`).

Econometrica publishes both **theoretical econometrics / economic theory** and **rigorous structural /
empirical** work. We pick a **methods/econometric-theory** angle, since that is where the house register is
most distinctive: a *new estimator with its limiting distribution*. (For the empirical/structural variant the
same arc holds, with the identification argument as the headline — see `ecta-identification` Branch D.)

**Illustrative paper (fictional):** *"Uniformly Valid Inference for a Threshold-Crossing Parameter under
Weak Identification."* Fictional object: a scalar structural parameter `θ₀` identified by a moment condition
whose Jacobian can be near-singular, so standard root-`n` normal inference is unreliable near the
weakly-identified region.

---

## Before (buries the result — typical first-draft intro)

> The estimation of nonlinear models has a long history in econometrics, and a large literature has examined
> the properties of extremum estimators under various conditions. Many authors have studied moment-based
> estimation, and identification has received considerable attention. In this paper we study a moment
> condition model and propose an estimator of a parameter of interest. We establish consistency and derive
> the asymptotic distribution under standard regularity conditions, and we conduct Monte Carlo experiments
> showing that the estimator performs well. We also discuss inference. It is well known that weak
> identification can cause problems for standard methods. Section 2 sets up the model, Section 3 presents the
> estimator, Section 4 gives the asymptotic theory, Section 5 reports simulations, and Section 6 concludes.

**What's wrong (against `ecta-writing-style` / `ecta-topic-selection` / `ecta-literature-positioning`):**

- **No result on page one.** The reader reaches Section 4 before learning what is actually proven; the
  contribution should appear as an *informal statement of the main theorem* in the introduction
  (`ecta-writing-style`: "state the result early").
- **"Standard regularity conditions" / "it is well known"** do the work a stated assumption or a citation
  should do — a named anti-pattern (`ecta-theory-model`, `ecta-identification`).
- **Contribution framed as an application** ("we propose an estimator… and show it performs well"), not as a
  *theorem the reader could not state before*. `ecta-topic-selection` requires naming the theorem and the
  assumption it relaxes, not "we propose a method and show it works."
- **No formal delta vs. prior work.** The relevant weak-identification literature is invoked vaguely; no
  sentence says *what this result gives that the closest prior result lacked* (`ecta-literature-positioning`).
- **Pointwise vs. uniform left implicit.** Whether the asymptotics are *uniformly* valid — the entire point
  under weak identification — is never stated (`ecta-identification`: "pointwise vs. uniform addressed").
- **Over-signposted roadmap** substituting for argument; throat-clearing history burning the scarce
  45-page body budget.

---

## After (Econometrica arc — informal theorem early, difficulty, architecture, formal delta)

> We construct a confidence set for a scalar structural parameter `θ₀`, defined by the moment restriction
> `E[g(W, θ₀)] = 0`, that is **uniformly valid over a parameter space including the weakly-identified
> region** where the Jacobian `G(θ₀) = E[∂g/∂θ]` is near-singular. Our main result (Theorem 1, stated
> informally here) is that the set `Cₙ = {θ : Sₙ(θ) ≤ χ²₁,₁₋α}`, built from a Jacobian-orthogonalized
> statistic `Sₙ`, has asymptotic coverage `1 − α` **uniformly** over that space, and contracts at the
> root-`n` rate wherever identification is strong. *(Informal main result — the object, its property, and the
> rate — in the first paragraph.)*
>
> The difficulty is that the standard Wald and `t` statistics are not even **pointwise** asymptotically
> `χ²`/normal as `G(θ₀) → 0`: the limiting law depends on the unknown local identification strength, so a
> fixed critical value over- or under-covers depending on where `θ₀` sits, and no single normal approximation
> is valid uniformly. *(Why it is hard — the formal obstruction, stated precisely, not as "weak
> identification causes problems.")*
>
> The proof proceeds by orthogonalizing the moment vector against the estimated Jacobian so that the leading
> term of `Sₙ` is asymptotically pivotal — free of the nuisance identification-strength parameter — and then
> establishing the limit *uniformly* by a drifting-sequence argument over `θ₀` and `G(θ₀)` jointly, using a
> stochastic-equicontinuity bound (Assumptions 1–4) to control the remainder. The novel step is the uniform
> remainder bound under a non-differentiable boundary case; the full proof is in the Supplemental Material.
> *(Proof architecture and the flagged hard step, in one paragraph.)*
>
> The closest prior result delivers a pivotal statistic but only under **pointwise** asymptotics
> (`[Author A, Year]`, who fix `θ₀` and let `n → ∞`); our Theorem 1 supplies the **uniform** validity that
> pointwise theory is known to miss in this region, at the cost of a wider set under strong identification by
> a factor we characterize. A second strand (`[Author B, Year]`) attains uniformity but requires the moment
> function to be differentiable in `θ` everywhere; we drop that, covering the kinked case (Assumption 2′).
> *(Formal delta against each neighbor — uniform vs. pointwise; weaker smoothness — with the honest cost
> stated. Author placeholders are deliberate: a real draft cites the precise theorem.)*
>
> The remainder of the paper is organized as follows. Section 2 states the model and Assumptions 1–4;
> Section 3 develops the estimator and Theorem 1; Section 4 reports Monte Carlo coverage across
> identification strengths; Section 5 concludes. Full proofs are in the Supplemental Material.
> *(Brief roadmap — no over-signposting; secondary material to the Supplement to respect the page cap.)*

---

## Why the "after" meets the Econometrica bar

Mapped to the skill checklists:

- **Result stated early as a theorem, not an application** — the informal Theorem 1, with the object
  (`Cₙ`), its property (uniform `1 − α` coverage), and its rate (root-`n` under strong identification),
  appears in the first paragraph (`ecta-writing-style`: "contribution / informal main theorem within the
  first ~2 pages"; `ecta-topic-selection`: contribution as *estimator-plus-asymptotics*, not "we propose a
  method").
- **The methodological object *is* the contribution** — uniform inference for `θ₀`, not an estimate of any
  particular `θ₀` in an application, which is what keeps it on the Econometrica side of the
  `ecta-topic-selection` eligibility screen (off-the-shelf method + the estimand is the point ⇒ redirect to
  AER / QJE / JPE / REStud).
- **The obstruction is stated precisely** ("not even pointwise `χ²` as `G(θ₀) → 0`") before the construction,
  and **pointwise vs. uniform is made explicit** — the exact `ecta-identification` requirement for
  weak-identification settings, replacing the "it is well known" anti-pattern.
- **Assumptions are numbered, displayed objects** (Assumptions 1–4; the kink relaxation 2′), referenced by
  number — `ecta-writing-style` and `ecta-theory-model`, so a referee can locate each.
- **Proof architecture and the hard step are flagged** (orthogonalization → drifting-sequence uniformity →
  the non-differentiable remainder bound), with full proofs in the Supplemental Material — consistent with
  `ecta-theory-model` and the 45-page body discipline; no "proof omitted to save space."
- **Positioning is a formal delta, with honest cost** — *uniform vs. pointwise* against neighbor A, *weaker
  smoothness* against neighbor B, plus the acknowledged wider-set cost under strong identification — exactly
  the `ecta-literature-positioning` template ("we provide what it lacked / we weaken its assumption," cost
  stated).

> **Note on the empirical/structural variant.** Were this a structural submission, the same arc would lead
> with the **identification argument** (Branch D of `ecta-identification`): the introduction would state, up
> front, *which structural parameters are a one-to-one image of the data distribution under the numbered
> identifying restrictions*, and that the design — not an off-the-shelf DID/RDD/IV — carries a methodological
> innovation. Pure off-the-shelf design with the estimand as the whole point is the most common Econometrica
> mismatch (`ecta-topic-selection`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for verified real Econometrica papers whose
> introductions execute this arc, and [`../code/`](../code/) for the estimator / robustness command chain a
> Monte Carlo section like Section 4 would adapt.
