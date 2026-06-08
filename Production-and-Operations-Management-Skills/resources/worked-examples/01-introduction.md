> **Illustrative teaching example.** The paper, setting, model, and every number below are
> **fictional** and exist only to demonstrate *Production and Operations Management* (POM) house style.
> No real-paper facts are stated, and no policy is invented. Corresponding skills:
> [`pom-writing-style`](../../skills/pom-writing-style/SKILL.md),
> [`pom-contribution-framing`](../../skills/pom-contribution-framing/SKILL.md),
> [`pom-topic-selection`](../../skills/pom-topic-selection/SKILL.md), and
> [`pom-theory-development`](../../skills/pom-theory-development/SKILL.md).

# Worked Example: A POM-Style Introduction (before → after)

This demonstrates the **POM introduction arc** assembled from this pack's skills:
**operations decision & decision maker → why it is hard (the operations tension) → setting & model/identification
→ headline result as a managerial lever → theory advance → twin-gate contribution (knowledge *and* practice),
tied to a named Department → brief roadmap.**

The governing POM rules, all from the skills:

- **Front-load the operations problem and the managerial takeaway** (`pom-writing-style`): lead with the
  decision, setting, and mechanism; keep the method **subordinate to the OM insight**.
- **Pass the twin gate** (`pom-contribution-framing`): the work must be of significant interest to
  practicing operations managers *and* advance OM knowledge — name **one practice-changing result** and
  **one theory-advancing result**.
- **Target one named Department** (`pom-topic-selection`): the framing must declare where the paper routes.
- **Express results as decision levers, not signs of derivatives** (`pom-theory-development`).

**Illustrative paper (fictional):** *"Should the Pharmacy Hold the Drug or the Patient? Pooling Versus
Dedicated Staffing for Specialty-Drug Fulfillment."* Fictional setting: a hospital specialty pharmacy
deciding whether to pool pharmacists across drug queues or dedicate them to drug families, under random
prior-authorization delays.

---

## Before (buries the operations decision — typical first-draft intro)

> Queueing models have been studied extensively in the operations literature, and staffing decisions are
> an important problem for service systems. In this paper, we build a multi-class M/M/c queue with
> abandonment and derive the optimal staffing policy under pooling versus dedication. We prove convexity
> of the cost function and characterize a threshold policy, and we conduct a discrete-event simulation to
> validate the analytical results. Staffing is an important topic for managers. Section 2 reviews the
> literature, Section 3 presents the model, Section 4 gives the analysis, Section 5 reports the
> simulation, and Section 6 concludes.

**What's wrong (against this pack's skills):**

- **Leads with the method** ("queueing models... we build a multi-class M/M/c queue") instead of the
  operations decision — the named anti-pattern in `pom-writing-style` ("method exposition crowds out the
  OM insight") and `pom-theory-development` ("method novelty substituted for an OM theory contribution").
- **No decision maker, no managerial takeaway on page one.** A practicing pharmacy operations lead cannot
  tell what to do differently — fails the **practice-relevance gate** (`pom-topic-selection`,
  `pom-contribution-framing`).
- **No headline result in operational units** (cost, waiting time, fill rate) — only "we prove
  convexity," a structural property with no lever attached.
- **Throat-clearing** ("studied extensively," "is an important topic") with vague stakes.
- **Department fit left implicit** for the editor to guess (`pom-contribution-framing` lists this as an
  avoid).
- **Over-signposted roadmap** doing the work the argument should do (`pom-writing-style` revision target).

---

## After (POM arc — operations decision + managerial lever first, twin-gate contribution, Department named)

> **When prior-authorization delays make specialty-drug demand bursty, should a hospital pharmacy pool its
> pharmacists across all drug queues or dedicate them to drug families?** We show that *conditional*
> pooling — pooling only the drugs whose authorization delays are weakly correlated — cuts the 95th-
> percentile patient wait by **31%** relative to full dedication, while full pooling *raises* it by 8%
> because correlated delay shocks arrive together and overwhelm the shared server. *(operations decision +
> decision maker + headline result in operational units, in the first breath.)*
>
> The decision is hard because pooling trades off two operations forces that move in opposite directions:
> pooling smooths idiosyncratic demand variation (the classic gain), but it also **couples** the queues, so
> when an insurer's system outage delays authorizations for several drugs at once, a pooled team has no
> slack anywhere. Which force dominates is not obvious from intuition and depends on the *correlation
> structure* of the delays — exactly the primitive prior staffing models suppress. *(why it is hard — the
> operations tension, stated in managerial language.)*
>
> We model fulfillment as a multi-class queue whose arrival streams share a common authorization-delay
> shock, and we characterize the optimal pooling partition as a function of the delay-correlation matrix;
> proofs are in the online e-companion. We then validate the policy on a fictional twelve-month stream of
> specialty-drug orders via discrete-event simulation. *(setting & model/identification in one paragraph;
> derivations deferred to the e-companion per the 32-page discipline.)*
>
> Conditional pooling dominates both full pooling and full dedication across the simulated demand regimes,
> and the gain grows as delay correlation rises. The **managerial lever is a partition rule**: group a drug
> into the shared pool only if its authorization-delay correlation with the pool stays below a threshold we
> give in closed form — a rule a pharmacy manager can apply from data already in the dispensing system.
> *(headline result restated as a decision lever, not a sign of a derivative.)*
>
> Our contribution is twofold, in the twin-gate sense POM requires. **For practice**, we replace the
> field's binary "pool or dedicate" heuristic with an implementable partition rule that a hospital pharmacy
> can run on its own delay data, cutting tail waits without adding pharmacists. **For OM knowledge**, we
> identify *delay correlation*, not demand variability alone, as the primitive that governs when pooling
> helps in authorization-gated service systems — a mechanism that extends to any queue where a shared
> upstream approver couples the classes. *(one practice-changing result and one theory-advancing result,
> explicit.)* This paper is framed for the **Healthcare Operations** Department. *(Department fit stated, not
> left to the editor.)*
>
> The paper proceeds as follows. Section 2 develops the correlated-delay queue and the partition result;
> Section 3 reports the simulation; Section 4 discusses implementation and boundary conditions for pharmacy
> managers. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the POM bar

Mapped to this pack's skill checklists:

- **Operations problem and managerial takeaway front-loaded** — the decision (pool vs. dedicate), the
  decision maker (pharmacy operations lead), and the headline number (31% tail-wait reduction) appear in
  the first paragraph, in operational units (`pom-writing-style`: "first page: decision, setting,
  mechanism, contribution — fast").
- **Passes the twin gate** — one practice-changing result (the partition rule) and one theory-advancing
  result (delay correlation as the governing primitive) are named separately, as
  `pom-contribution-framing` requires; neither stands alone.
- **Method demoted to a tool** — the multi-class queue and simulation are introduced only where the design
  is discussed, never as the lead (avoids the `pom-theory-development` / `pom-writing-style`
  "method-dominated" anti-pattern).
- **Result expressed as a lever, not a derivative** — "convexity" from the *before* becomes a closed-form
  **partition threshold a manager applies**, satisfying `pom-theory-development`'s "managerial lever, not
  only a sign of a derivative."
- **Department fit explicit** — routed to Healthcare Operations, so framing, reviewers, and literature
  align (`pom-topic-selection`, `pom-contribution-framing`).
- **32-page discipline respected** — proofs and extended validation are flagged for the **unlimited online
  e-companion**, keeping the main argument uncrowded (`pom-writing-style`, `pom-methods`).
- **Practice-relevance gate cleared** — the mechanism generalizes beyond the focal pharmacy to any
  authorization-gated service queue, so the local result carries a broad OM lesson
  (`pom-topic-selection`'s strong-signal test).

> Next: benchmark against real, web-verified POM papers whose introductions execute this arc, and see
> [`../code/`](../code/) for the empirical-OM command chain an archival version of this study would use.
