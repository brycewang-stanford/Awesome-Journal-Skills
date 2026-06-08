> **Illustrative teaching example.** The paper, model, theorem, and every number below are **fictional**
> and exist only to demonstrate *Operations Research* house style. No real-paper facts are stated, and no
> real system is invoked. Corresponding skills:
> [`ors-writing-style`](../../skills/ors-writing-style/SKILL.md),
> [`ors-topic-selection`](../../skills/ors-topic-selection/SKILL.md), and
> [`ors-theory-development`](../../skills/ors-theory-development/SKILL.md).

# Worked Example: An *Operations Research*-Style Introduction (before → after)

This demonstrates the introduction arc *Operations Research* rewards (from `ors-writing-style` and
`ors-topic-selection`): **decision/operational problem → why it matters to the OR community → model class
and method → the analytical or computational result, in plain words → the managerial/algorithmic insight
→ brief roadmap.** Two governing rules from `ors-writing-style` shape the whole passage. First, the
introduction is **equation-free**: it states the problem, the results, and their significance with no
mathematical notation — every result is written as "we show that …". Second, lead with the **operational
problem and the contribution**, not the machinery. Notation, the model, and the theorems appear only
after the introduction.

**Illustrative paper (fictional):** *"Staffing a Time-Varying Service System with Uncertain Abandonment:
A Robust Square-Root Rule."* Fictional setting: a single multiserver service system whose arrival rate
varies over the day and whose customers abandon while waiting, with the per-period mean abandonment rate
known only to lie in an interval.

---

## Before (buries the contribution — typical first-draft intro)

> Queueing systems with abandonment have been studied extensively in the operations research and applied
> probability literature. Let $\lambda(t)$ denote the arrival rate, $\mu$ the service rate, and $\theta$
> the abandonment rate; the offered load is $R(t) = \lambda(t)/\mu$. We consider the Erlang-A model and
> formulate a staffing optimization problem $\min_{s(t)} \int c\, s(t)\,dt$ subject to a delay
> constraint. We solve this model and present numerical experiments. Staffing is an important problem for
> managers. Section 2 reviews the literature, Section 3 presents the model, Section 4 the analysis,
> Section 5 the experiments, and Section 6 concludes.

**What's wrong (against `ors-writing-style` / `ors-topic-selection` / `ors-theory-development`):**

- **Equations in the introduction** ($\lambda(t)$, $R(t)$, the $\min$ program) — a hard violation of the
  *Operations Research* equation-free-introduction rule in `ors-writing-style`.
- **Leads with the model machinery** (Erlang-A, the optimization program) instead of the operational
  decision and why the OR community should care — the anti-pattern `ors-writing-style` names.
- **No statement of the result.** A reader cannot tell whether the contribution is a new staffing rule, a
  performance guarantee, a complexity result, or an experiment — failing the `ors-theory-development`
  "claim at the right strength" test and the `ors-topic-selection` "genuine methodological contribution"
  test.
- **No significance to OR.** "Important for managers" is throat-clearing, not a contribution to OR/MS
  methodology.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (*Operations Research* arc — operational problem + result + insight, equation-free, contribution early)

> **How should a service system be staffed over the day when customers abandon the queue and the
> abandonment rate is not known precisely — only that it lies within a range?** Standard square-root
> staffing rules assume the abandonment rate is known and fixed; when it is uncertain, a manager who plugs
> in a point estimate can systematically understaff in exactly the periods when abandonment is most
> costly. We study a time-varying multiserver system in which the mean abandonment rate in each period is
> known only to lie in an interval, and we ask for a staffing policy that performs well against the worst
> case in that range. *(Operational problem + why the standard approach fails, in the first breath, with
> no notation.)*
>
> This problem is hard because robustness and time variation interact: protecting against the worst-case
> abandonment rate period by period can be far too conservative, since the worst case need not occur in
> every period at once, yet ignoring the interaction gives a policy with no performance guarantee.
> *(Why it is hard — the methodological tension, stated in plain OR terms.)*
>
> We show that the worst-case staffing problem admits a **robust square-root staffing rule**: the optimal
> robust staffing level in each period is the offered load plus a safety term proportional to the square
> root of the load, where the proportionality constant is determined by a single budget parameter that
> trades the manager's tolerance for the uncertainty in the abandonment rate against staffing cost. We
> prove that this rule is optimal for the worst-case delay objective, that its robust counterpart remains
> efficiently solvable, and that the loss relative to a clairvoyant policy that knew the true abandonment
> rate is bounded by a quantity that shrinks as the system grows large. *(The analytical results, written
> as "we show that …" / "we prove that …" — no equations, but the model class, the guarantee, and the
> asymptotic optimality are all named, per `ors-theory-development`.)*
>
> The managerial insight is that **robustness to abandonment uncertainty costs only a square-root-order
> increase in staff, not a worst-case-everywhere increase**: a manager can buy a guaranteed service level
> across the whole range of plausible abandonment rates by adjusting one interpretable budget parameter,
> rather than re-solving the staffing problem for every scenario. In a computational study on
> time-varying load profiles, the robust rule attains the target delay across the uncertainty range while
> a nominal point-estimate rule violates it in the high-abandonment periods. *(The
> algorithmic/managerial payoff — what travels beyond the model, tied to the computational evidence that
> `ors-data-analysis` requires.)*
>
> The paper proceeds as follows. Section 2 positions the robust staffing rule against the square-root
> staffing and many-server heavy-traffic literatures; Section 3 states the model and the worst-case
> objective; Section 4 proves optimality of the robust rule and the asymptotic-loss bound; Section 5
> reports the computational study. *(Brief roadmap — no over-signposting.)*

---

## Why the "after" meets the *Operations Research* bar

Mapped to the skill checklists:

- **Equation-free introduction** — the entire "after" states the problem, the results, and their
  significance with **no notation**, exactly as `ors-writing-style` requires; the offered load and safety
  term are described in words, and the model/theorems are deferred to later sections.
- **Operational problem leads, machinery follows** — the staffing decision under abandonment uncertainty
  opens the passage; "Erlang-A," the optimization program, and the budget constraint are demoted to the
  model section (`ors-writing-style`: do not lead with the method).
- **Results stated at the right strength** — the passage names an **optimality theorem** for the
  worst-case objective and an **asymptotic-loss bound**, written as plain-language "we prove that …,"
  satisfying `ors-theory-development`'s claim-strength discipline (theorem vs. heuristic).
- **Significance to the OR community is explicit** — the contribution is a *robust staffing rule with a
  guarantee*, a methodological advance over point-estimate square-root staffing, meeting the
  `ors-topic-selection` "genuine OR/MS methodological contribution" test rather than a routine
  application.
- **Tractability is part of the contribution** — the robust counterpart is said to remain efficiently
  solvable, the `ors-theory-development` move of choosing a model whose structure enables both theorems
  and computation.
- **The result is positioned against the closest prior work** — square-root staffing and many-server
  heavy-traffic — naming the precise delta (uncertain vs. known abandonment rate), as
  `ors-literature-positioning` demands.
- **Computation supports, not substitutes for, the theory** — the study shows the proved guarantee
  holding and the nominal rule failing, the supporting-evidence role `ors-data-analysis` assigns to
  experiments.

> Next: adapt the reproducible computational-study skeleton in [`../code/`](../code/) when turning this
> introduction arc into a full benchmark-and-baseline study.
