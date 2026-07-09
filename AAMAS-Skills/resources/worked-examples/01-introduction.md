> **Illustrative teaching example.** The paper, mechanism, setting, and every number below are
> **fictional** and exist only to demonstrate AAMAS house style. No real-paper facts, datasets,
> or results are stated, and no policy is invented. Corresponding skills:
> [`aamas-writing-style`](../../skills/aamas-writing-style/SKILL.md),
> [`aamas-topic-selection`](../../skills/aamas-topic-selection/SKILL.md), and
> [`aamas-experiments`](../../skills/aamas-experiments/SKILL.md).

# Worked Example: An AAMAS-Style Abstract + Introduction (before → after)

This demonstrates the **AAMAS first-page arc** from `aamas-writing-style`:
**interaction problem → why single-agent or centralized fixes fail → mechanism or learning rule
→ strategic/equilibrium property → multiagent evidence → why it matters for agents and
multiagent systems**. The AAMAS-specific rules: the contribution must be an **interaction**
result (it exists only because multiple self-interested or cooperating agents are present), the
**solution concept or incentive property is named**, and every strategic claim is paired with a
proof, a self-play/population experiment, or a deployment - under **double-blind** wording.

The framing also reflects `aamas-topic-selection`: AAMAS is strongest when the **agents are the
research object**. Here, incentive-compatibility under decentralized learning is the
contribution, not a single-agent throughput win (which would route to a general ML or systems
venue).

**Illustrative paper (fictional):** *"Truthful Decentralized Scheduling: A Learning Mechanism
for Self-Interested Agents Sharing a Bottleneck Resource."* Fictional mechanism: a payment rule
under which no agent gains by misreporting its job value, even while all agents are still
learning.

---

## Before (buries the interaction contribution — typical first-draft abstract + intro)

> **Abstract.** Resource scheduling is an important problem with many applications. We propose a
> new deep reinforcement learning method that schedules jobs on a shared server and achieves
> high throughput, outperforming prior schedulers on several workloads. Our approach uses a
> neural network trained end-to-end and works well in practice.
>
> **Introduction.** Scheduling has been studied for decades. Many heuristics and learning-based
> schedulers exist. In this paper we train an agent with reinforcement learning to allocate a
> shared server among incoming jobs, maximizing total throughput. We evaluate on standard
> workloads and show our method outperforms baselines. Section 2 reviews related work, Section 3
> describes our method, Section 4 presents experiments, and Section 5 concludes.

**What's wrong (against `aamas-writing-style` / `aamas-topic-selection` / `aamas-experiments`):**

- **No interaction on the first page** - it reads as one central scheduler optimizing
  throughput, i.e. a single-agent control paper. Nothing here needs *multiple self-interested
  agents*, so an AAMAS reviewer asks why it is not at a systems or general-ML venue.
- **No solution concept, no incentives** - the jobs' *values* are treated as known inputs, so
  there is no mechanism, no truthfulness, no equilibrium - the AAMAS substance is absent.
- **Overclaims** ("outperforms baselines," "works well") with **no strategic evaluation** - no
  test of what a *strategic* agent would do under the rule, and no seeds or variance.
- **Venue-misfit framing** - pitched as a throughput win (a scheduling/systems contribution),
  the `aamas-topic-selection` re-route signal.
- **Over-signposted roadmap** standing in for an argument.

---

## After (AAMAS arc — interaction → why centralization fails → mechanism → incentive property → evidence → why it matters)

> **Abstract.** When self-interested agents share a bottleneck resource, they can **misreport
> job values** to jump the queue, so a scheduler that trusts reported values is manipulable and
> a central planner that ignores them is inefficient. We introduce **LearnVCG**, a decentralized
> scheduling mechanism that couples a value-elicitation payment rule with independent per-agent
> learning. We prove that **truthful reporting is a dominant strategy** for every agent at every
> round, *regardless of how the other agents are still learning* (Theorem 1), and that the
> mechanism's allocation converges to the efficient one as agents' policies converge
> (Theorem 2). In a 20-agent self-play study where agents are free to learn to lie, LearnVCG
> agents converge to truthful reports while a throughput-only baseline is exploited by a single
> strategic deviator; efficiency loss stays within a bounded gap. We report all outcomes with
> standard errors over 30 seeds and release the strategic-deviation test suite. *(interaction →
> failure of naive fixes → mechanism → incentive property → multiagent evidence → uncertainty
> reported, all on the first page.)*
>
> **Introduction.** *(¶1 - the interaction problem + contribution, first breath.)* A shared
> server is only as good as the **truthfulness of the agents that queue for it**. When each job
> belongs to a **self-interested agent**, reporting a higher value than the truth is a rational
> way to get served first, so throughput-maximizing schedulers quietly reward manipulation. We
> present **LearnVCG**, a decentralized mechanism whose payment rule makes **honest value
> reporting a dominant strategy** even while every agent is still learning its policy.
>
> *(¶2 - why single-agent or centralized fixes are insufficient.)* Existing remedies fail for
> nameable, distinct reasons. A central planner with full information is efficient but assumes
> away the very problem - it needs the private values that agents have an incentive to hide. A
> throughput-trained RL scheduler treats reported values as ground truth, so a **single strategic
> agent can exploit it** by inflating reports. Classic one-shot VCG mechanisms are truthful but
> assume agents *already* best-respond, which does not hold while a population is **mid-learning**
> and off-equilibrium. *(each prior line gets a specific failure, not a vague "prior work is
> limited.")*
>
> *(¶3 - the mechanism + the strategic model made explicit.)* LearnVCG charges each agent the
> externality its allocation imposes on others, computed from reported values, while each agent
> independently updates a reporting-and-bidding policy by reinforcement learning. We model the
> agents as **self-interested learners** in a repeated allocation game and make the incentive
> claim precise: truthfulness is dominant **per round**, so it does not rely on other agents
> having converged. *(the interaction model and solution concept stated plainly, per the AAMAS
> rule that the strategic setting must be legible.)*
>
> *(¶4 - property + evidence, each claim paired.)* We prove per-round dominant-strategy
> truthfulness (Theorem 1, proof in App. A) and asymptotic efficiency as policies converge
> (Theorem 2, App. B). Empirically, in a 20-agent repeated game where agents may learn to
> misreport, LearnVCG populations converge to honest reporting while the throughput-only
> baseline is exploited by one deviator who captures a disproportionate share (Fig. 1; Table 1);
> the realized efficiency gap stays within the Theorem 2 bound at the tested horizons.
> **All numbers carry standard errors over 30 seeds**, and the strategic-deviation protocol,
> opponent set, and reward specification are in App. C. *(every claim → theorem, figure, table,
> or reproducibility location.)*
>
> *(¶5 - why it matters for agents and multiagent systems + roadmap.)* The contribution is to
> make a **classic incentive guarantee hold under decentralized learning**, bridging mechanism
> design and multiagent RL: honesty is not assumed of already-rational agents but *earned* by
> agents that are still adapting. Section 2 formalizes the repeated allocation game; Section 3
> proves the incentive and efficiency results; Section 4 reports the self-play study.
> *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the AAMAS bar

Mapped to the skill checklists:

- **Interaction on the first page** - the abstract and ¶1 lead with self-interested agents,
  manipulation, and a truthfulness guarantee, so the paper is unmistakably about *interaction*
  (`aamas-writing-style`: "put the interaction contribution in the first page";
  `aamas-topic-selection`: agents are the research object).
- **Solution concept named** - dominant-strategy truthfulness and efficiency are stated as the
  properties, not left implicit (`aamas-writing-style`: name the solution concept).
- **Naive fixes ruled out specifically** - central planner, throughput RL, and one-shot VCG each
  get a distinct failure mode (`aamas-related-work`: distinguish the nearest neighbor precisely).
- **Every claim paired with evidence** - truthfulness → Theorem 1/App. A; efficiency →
  Theorem 2/App. B; exploitation → Fig. 1/Table 1; reproducibility → App. C
  (`aamas-experiments` claim→evidence map).
- **Strategic evaluation, not a leaderboard** - the key experiment lets agents *learn to lie*
  and measures whether they do, which tests the incentive claim rather than raw throughput
  (`aamas-experiments`: experiments should probe the interaction, and report seeds/variance).
- **Right venue** - the contribution is an incentive property under multiagent learning, a
  strong AAMAS fit rather than a single-agent scheduling/systems re-route
  (`aamas-topic-selection` fit test).
- **8-page discipline** - proofs and the full strategic-deviation protocol live in the
  appendix while the body carries the argument (`aamas-writing-style`: the 8-page body plus
  unlimited references).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, dblp-verified
> AAMAS papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for AAMAS-specific track and
> submission policy.
