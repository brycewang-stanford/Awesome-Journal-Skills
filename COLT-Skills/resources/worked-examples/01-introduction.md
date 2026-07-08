> **Illustrative teaching example.** The paper, model, theorem, and every rate below
> are **fictional**, invented solely to demonstrate COLT house style; no real result is
> restated and no venue policy is invented. Corresponding skills:
> [`colt-writing-style`](../../skills/colt-writing-style/SKILL.md),
> [`colt-topic-selection`](../../skills/colt-topic-selection/SKILL.md), and
> [`colt-related-work`](../../skills/colt-related-work/SKILL.md).

# Worked Example: A COLT-Style Abstract + Introduction (before → after)

The target is the COLT first-pages arc from `colt-writing-style`: **problem in the
field's vocabulary → what was known (exact bounds) → the new result, informal →
formal setup before formal theorems → the technique paragraph**. The contribution must
be quotable as a mathematical statement, the delta against prior bounds must be
explicit, and the proof strategy must be sold before the appendix is opened.

**Fictional paper:** *"The Price of Delayed Feedback in Sleeping Bandits."* Fictional
setting: a K-armed adversarial bandit where the available arm set varies per round
(sleeping) and feedback arrives with delay τ.

---

## Before (a draft that would struggle at COLT)

> **Abstract.** Multi-armed bandits are a fundamental framework with many applications
> in recommendation and clinical trials. In practice, feedback is often delayed and
> not all actions are always available. We study this realistic setting and propose a
> novel algorithm, DS-EXP, which handles both challenges simultaneously. We provide a
> rigorous theoretical analysis showing that DS-EXP achieves strong regret guarantees,
> and simulations confirm it outperforms baselines.
>
> **Introduction.** Bandit algorithms have seen enormous success... [half a page of
> application motivation]. Prior work has considered delay and sleeping separately,
> but to the best of our knowledge no work combines them. Our contributions are:
> (1) a novel algorithm; (2) a rigorous analysis under mild conditions; (3) extensive
> simulations. The rest of the paper is organized as follows...

**Why this fails the COLT bar:**

- **No mathematical headline.** "Strong regret guarantees" is not a statement; a COLT
  reader still does not know the rate, the model, or the adversary after the abstract.
- **Known bounds absent.** Neither the delayed-bandit rate nor the sleeping-bandit
  rate is quoted, so the delta is invisible — the reviewer cannot tell whether the
  combined result is a corollary or a contribution.
- **"Mild conditions"** hides assumptions; at this venue hypotheses are stated, not
  advertised (`colt-writing-style` sentence repairs).
- **Applications-first framing** spends the decisive first paragraphs on
  recommendation systems instead of on the learning-theoretic question.
- **"Novel algorithm" + "rigorous analysis"** is self-grading; the technique is never
  described, so no technique credit can be assigned.
- **Simulations as a selling point** signals venue confusion — COLT accepts on
  theorems (`colt-experiments`).

---

## After (COLT arc)

> **Abstract.** In sleeping bandits with delayed feedback, a learner picks an arm from
> an adversarially chosen available set $A_t \subseteq [K]$ and observes its loss
> after τ rounds. With delay alone, regret
> $\Theta(\sqrt{(τ+1) T \log K})$ is known; with sleeping alone,
> $\Theta(\sqrt{TK \log K})$ against the best-ordering benchmark. We show the
> combination is strictly harder than either: any algorithm incurs
> $\Omega(\sqrt{τ T K})$ regret, and a delay-bucketed variant of a
> sleeping-experts reduction attains $O(\sqrt{τ T K \log K})$ — matching up to the
> log factor. The lower bound requires a new instance family in which the adversary
> couples availability with the delayed observation schedule, which may be of
> independent interest. *(model → known rates → new upper and lower bounds → technique,
> all in one paragraph.)*
>
> **Introduction, ¶1 (the question).** How much does delayed feedback cost when the
> action set itself varies? For fixed action sets the answer is understood: delay τ
> inflates minimax regret by exactly $\sqrt{τ+1}$ [refs]. For sleeping bandits without
> delay, the best-ordering benchmark admits $\Theta(\sqrt{TK\log K})$ [refs]. Whether
> these two prices compose — multiply, add, or interact — has been open. *(problem in
> the field's vocabulary; known results with exact rates and citations.)*
>
> **¶2 (the answer, informal).** We prove they interact: the minimax regret is
> $\widetilde{\Theta}(\sqrt{τ T K})$ (Theorems 1 and 2, informal). The delay multiplies
> the *sleeping* rate's $K$-dependence rather than the $\log K$ one would hope for from
> the fixed-set case — a genuine separation between the two models. *(one-breath
> informal theorem with the surprise named.)*
>
> **¶3 (setup pointer + assumptions).** Section 2 defines the protocol: an oblivious
> adversary fixes losses and availability; feedback from round $t$ arrives at $t+τ$
> with τ known. We assume losses in $[0,1]$ (Assumption 1) and per-round non-empty
> availability (Assumption 2); both are used in the lower bound too, so the separation
> is not an artifact of generosity. *(complete formal setup promised before any formal
> theorem; assumptions named, and their role in the lower bound flagged.)*
>
> **¶4 (technique).** The upper bound buckets rounds by delay phase and runs a
> sleeping-experts reduction per bucket; the analysis must handle benchmark orderings
> that differ across buckets, which we resolve with a doubling-indexed potential. The
> lower bound is the novelty: standard delayed-bandit instances fail because sleeping
> lets the learner dodge the confusing arms, so we construct availability sequences
> that force every learner to re-explore within each delay window. *(what is routine
> and what is new, stated honestly — technique credit is claimable because the
> technique is described.)*
>
> **¶5 (context + one open question).** Our rates leave a $\sqrt{\log K}$ gap; we
> conjecture the lower bound is tight and pose closing it as an open question in
> Section 6. All proofs appear in Appendices B-D; Section 5 gives a small simulation
> visualizing the $\sqrt{τ}$ scaling on the lower-bound instance family. *(honest gap
> + COLT's open-question culture + numerics scoped to illustration.)*

---

## What changed, mapped to the skills

- **Headline is a theorem** — rates with explicit parameter dependence replace
  "strong guarantees" (`colt-writing-style`: quantifier and constant hygiene).
- **Known-vs-new is quantitative** — both prior rates are quoted, so the delta
  ("prices interact, $K$ not $\log K$") is checkable (`colt-related-work` ledger).
- **Assumptions surfaced and load-bearing** — the same assumptions govern upper and
  lower bounds, preempting the "generous model" objection (`colt-reproducibility`).
- **Technique paragraph does real work** — routine parts admitted, the new instance
  family flagged "of independent interest" only where defensible
  (`colt-review-process`: novelty-of-technique is a scored dimension).
- **Numerics demoted to illustration** on the hard instances, with the theory
  untouched if deleted (`colt-experiments` deletability test).
- **Open question posed on purpose** — the log-factor gap becomes agenda-setting
  instead of a hidden weakness (`colt-topic-selection`: open-problem culture).

> Next: study real first pages via [`../exemplars/library.md`](../exemplars/library.md)
> (verified COLT papers on PMLR), and confirm current-cycle policy in
> [`../official-source-map.md`](../official-source-map.md).
