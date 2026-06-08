> **Illustrative teaching example.** The paper, model, and every result below are **fictional** and
> exist only to demonstrate GEB house style. No real-paper facts are stated, and no policy is invented.
> Corresponding skills: [`geb-writing-style`](../../skills/geb-writing-style/SKILL.md),
> [`geb-topic-selection`](../../skills/geb-topic-selection/SKILL.md),
> [`geb-contribution-framing`](../../skills/geb-contribution-framing/SKILL.md), and
> [`geb-literature-positioning`](../../skills/geb-literature-positioning/SKILL.md).

# Worked Example: A GEB-Style Introduction (before → after)

This demonstrates the **GEB introduction arc** from `geb-writing-style`:
**question / phenomenon → why it was open → the result (in words, then formally) → the key idea →
scope & relation to the literature → brief roadmap** — with the GEB rule that the introduction is
**idea-first**: state the strategic question and the theorem early, motivate in words before notation,
and make the advance to *game theory* unmistakable for a general game-theory reader (the
[`geb-contribution-framing`](../../skills/geb-contribution-framing/SKILL.md) "we show that … which …
implying …" sentence on page one).

Because GEB publishes **game theory** — a model plus an equilibrium result — this example states a
game and proves a result about it, rather than running an empirical estimator. (GEB also publishes
experiments; that arc would lead with an identified behavioral finding instead.)

**Illustrative paper (fictional):** *"Patient Bidders: Deadline Design in Sequential Common-Value
Auctions."* Fictional model: a seller runs a sequence of common-value auctions and chooses how long to
keep each round open; bidders privately learn over time and choose *when* to enter.

---

## Before (buries the idea — typical first-draft intro)

> Consider a set $N = \{1, \dots, n\}$ of risk-neutral bidders and a sequence of objects
> $t = 1, \dots, T$ of unknown common value $v$, where each bidder $i$ receives at date $\tau$ a signal
> $s_i^\tau$ drawn from a distribution $F$ with full support on $[\underline{s}, \overline{s}]$. The
> seller commits to a deadline rule $d: H \to \mathbb{R}_+$ mapping histories to closing times. We model
> the resulting interaction as a Bayesian game and apply the concept of perfect Bayesian equilibrium. In
> this paper we use these tools to study auctions with endogenous timing, a topic that has received
> attention in the literature. After defining the strategy space and the belief system, we derive
> equilibrium conditions and characterize the solution. Section 2 sets up the model, Section 3 states the
> assumptions, Section 4 derives the equilibrium, Section 5 discusses extensions, and Section 6 concludes.

**What's wrong (against `geb-writing-style` / `geb-topic-selection` / `geb-contribution-framing`):**

- **Opens with notation and the solution concept** instead of the strategic question — the named
  anti-pattern in `geb-writing-style` ("opening the intro with notation and assumptions instead of the
  question and result") and `geb-contribution-framing` ("'We study a model of …' with no claimed result").
- **No result stated early.** A game theorist finishing this paragraph cannot tell what was *proven* or
  what is new for game theory (`geb-topic-selection`: "what does this teach game theory that we did not
  know?").
- **No key idea / no advance verb** — nothing says *characterize*, *prove existence*, *overturn*
  (`geb-contribution-framing`).
- **No positioning** against the nearest prior result, so a specialist referee cannot see the delta
  (`geb-literature-positioning`).
- **Over-signposted roadmap** doing the argument's job.

---

## After (GEB arc — question → result → key idea → scope, contribution early)

> **When a seller can choose how long to leave an auction open, does giving bidders more time to learn a
> common value help the seller — or does it unravel into strategic waiting?** We show that in a sequence
> of common-value auctions with privately timed learning, every equilibrium under an *open-ended* deadline
> exhibits **late pooling**: all serious bidders delay entry until an endogenous cutoff, and the seller's
> revenue is strictly *lower* than under a short, hard deadline. *(question + headline result, in words,
> in the first breath — and an advance verb: we characterize the equilibrium and show a comparative-static
> reversal.)*
>
> This was open because the two forces point in opposite directions and prior analyses fixed the timing
> exogenously. More time lets bidders refine their estimate of the common value, which the
> winner's-curse logic suggests should raise willingness to pay; but more time also lets each bidder
> *wait to free-ride* on the information revealed by others' entry, a force that earlier sequential-auction
> models — which take the closing rule as given — could not express. *(why it was open: the obstacle is a
> genuine trade-off the existing framework cannot represent.)*
>
> Formally, we study a Bayesian game in which $n$ bidders receive private signals that sharpen over time
> and the seller commits to a deadline rule. **Theorem 1** characterizes the unique symmetric perfect
> Bayesian equilibrium and shows it is a threshold strategy in each bidder's *posterior precision*, not in
> the signal level. **Theorem 2** is the comparative static: revenue under the open-ended rule is
> bounded above by revenue under the optimal hard deadline, with the gap strictly positive whenever
> signals are informative. *(the result stated formally, after the words; the theorems are named so a
> referee can cite them.)*
>
> The key idea is that the deadline is not a constraint on the auction but an **information-disclosure
> instrument**: by closing early the seller suppresses the option to wait, converting a war of attrition
> over information into a one-shot common-value auction. *(the one move that makes it work — stated as an
> idea, not an equation.)*
>
> Our contribution is to show that **endogenous deadline design**, not the bidding rule, governs revenue
> in common-value sequential auctions — *which overturns the intuition that more bidder information is
> good for the seller, implying that optimal auction design should treat time-to-close as a primary
> decision variable.* *(the `geb-contribution-framing` sentence: "we show that [setting] admits [result],
> which overturns [prior understanding], implying [consequence]," stated early.)* Relative to the nearest
> prior work — sequential common-value auctions with *fixed* timing — we drop the exogenous-deadline
> assumption and recover their characterization as the hard-deadline limit of our model, so our result is
> a strict generalization rather than a different model. *(positioning per
> `geb-literature-positioning`: name the delta, recover the prior result as a special case.)* The
> mechanism is game-theoretic, not auction-specific: any sequential mechanism whose designer controls a
> stopping time inherits the same waiting-versus-learning tension.
>
> The paper proceeds as follows. Section 2 sets up the game; Section 3 proves Theorems 1 and 2;
> Section 4 shows the result survives asymmetric signals and reserve prices. *(brief roadmap — no
> over-signposting.)*

---

## Why the "after" meets the GEB bar

Mapped to the skill checklists:

- **Idea-first, result early — in words then formally.** The strategic question and the headline (late
  pooling; revenue falls) appear in the first paragraph; the formal Theorems 1–2 follow, named
  (`geb-writing-style`: "state the main theorem/finding early, in words, then formally").
- **The advance to game theory is explicit.** The contribution sentence uses an advance verb
  (*characterize*, *overturn*) and states what we did not know before — the
  [`geb-topic-selection`](../../skills/geb-topic-selection/SKILL.md) first-page test and the
  [`geb-contribution-framing`](../../skills/geb-contribution-framing/SKILL.md) "we show that … which …
  implying …" form.
- **The key idea is stated as an idea** (deadline as an information-disclosure instrument), before any
  equation — `geb-writing-style`: "give the proof's idea before its steps."
- **Positioned against the nearest result**, with the prior model recovered as a limiting case —
  `geb-literature-positioning`: name the delta and pre-empt the "special case of X" objection.
- **Specialist-but-general framing.** It assumes the vocabulary of Bayesian games and PBE but motivates
  the trade-off in plain words, so a theorist outside auction theory still grasps the bite
  (`geb-writing-style`: "rigorous yet legible beyond one sub-field").
- **Calibrated scope.** The last lines say exactly how far the mechanism generalizes (any designer-controlled
  stopping time) without over-claiming — `geb-contribution-framing` over-claim guard.
- **Notation is demoted to where it is used**, not the lead — fixing the "before" anti-pattern of opening
  on the strategy space and solution concept.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** GEB papers
> whose introductions execute this arc (theory, learning, behavioral, experimental, and market design),
> and [`../external_tools.md`](../external_tools.md) for the equilibrium-computation and proof-checking
> tools (Gambit, `nashpy`, SymPy) that turn a hand characterization into a checkable worked example.
