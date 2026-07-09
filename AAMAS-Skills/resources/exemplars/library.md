# AAMAS Exemplars Library (topic × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** (`dblp.org/db/conf/atal/`) and/or the **IFAAMAS proceedings** to confirm it actually
> appeared in the **International Conference on Autonomous Agents and Multiagent Systems
> (AAMAS)** - matching edition, year, author list, and page range. Papers that could not be
> cleanly confirmed as **AAMAS proceedings** (as opposed to a sibling AI venue or a journal)
> were **omitted and documented below**. This is a deliberately short, verified list
> (5 verified > 20 guessed).
>
> **Sibling-confusion guard:** AAMAS is **not** NeurIPS, ICML, ICLR, AAAI, or IJCAI, and it is
> **not** the JAAMAS journal. Many famous multiagent papers live in those other venues. dblp
> indexes the AAMAS stream under the historical key **`conf/atal`** (shared lineage with the old
> ATAL workshop and ICMAS) - so a `conf/atal` record *is* AAMAS, but a paper you *remember* as
> "the multiagent RL paper" may actually be NeurIPS or ICML (see omissions). Each row below was
> checked to be an AAMAS edition specifically.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does
> not reproduce or invent results, theorem constants, or table numbers - read the original in
> the IFAAMAS proceedings or ACM DL before citing anything. For AAMAS-specific policy, scope,
> and the do-not-misattribute list, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **topic × method** is closest to yours, then study how that paper puts an
**interaction claim on the first page** - a strategy, equilibrium, coordination result, or
learning dynamic that only exists *because multiple agents are present* - and pairs it with the
matching evidence (a game-theoretic argument, a multiagent simulation, or a deployment). That is
the AAMAS bar (see [`../../skills/aamas-writing-style/SKILL.md`](../../skills/aamas-writing-style/SKILL.md),
[`../../skills/aamas-topic-selection/SKILL.md`](../../skills/aamas-topic-selection/SKILL.md), and
[`../../skills/aamas-experiments/SKILL.md`](../../skills/aamas-experiments/SKILL.md)). For each,
ask the self-check question before claiming your paper is "AAMAS-shaped."

**AAMAS edition ↔ year (verified rows below):** 7th = AAMAS 2008; 10th = AAMAS 2011; 12th =
AAMAS 2013; 16th = AAMAS 2017; 17th = AAMAS 2018.

---

## By method

### Multiagent reinforcement learning in mixed-motive games (emergent behavior)

- **Leibo, Zambaldi, Lanctot, Marecki & Graepel, "Multi-agent Reinforcement Learning in
  Sequential Social Dilemmas," AAMAS 2017, pp. 464-473.** Verified: dblp
  `conf/atal/LeiboZLMG17`.
  - **Why it is an exemplar:** reframes cooperation-vs-defection as a **sequential** social
    dilemma played by independent deep-RL agents, so the contribution is a *behavioral
    finding about interaction* (how learned policies tip between cooperation and conflict),
    not a single-agent scoreboard win. A model of the AAMAS "the multiagent dynamic is the
    result" abstract.
  - **Self-check:** does your finding only exist because agents co-adapt, or would it survive
    if you froze every other agent into a fixed environment?

### Cooperative MARL with a single team reward (credit assignment)

- **Sunehag, Lever, Gruslys, Czarnecki, Zambaldi, Jaderberg, Lanctot, Sonnerat, Leibo, Tuyls
  & Graepel, "Value-Decomposition Networks For Cooperative Multi-Agent Learning Based On Team
  Reward," AAMAS 2018, pp. 2085-2087.** Verified: dblp `conf/atal/SunehagLGCZJLSL18` (appears
  as an extended abstract in the AAMAS 2018 proceedings).
  - **Why it is an exemplar:** attacks the **multiagent credit-assignment** problem head-on -
    decomposing one shared team reward into per-agent values so decentralized agents can act
    - which is a problem that *only* exists in cooperative multiagent settings.
  - **Self-check:** is your mechanism about splitting, shaping, or attributing signal *across
    agents*, rather than a general single-network trick that happens to be run many times?

### Deployed game theory for security (real-world Stackelberg games)

- **Pita, Jain, Marecki, Ordóñez, Portway, Tambe, Western, Paruchuri & Kraus, "Deployed ARMOR
  Protection: The Application of a Game Theoretic Model for Security at the Los Angeles
  International Airport," AAMAS 2008 (Industry Track), pp. 1805-1812.** Verified: IFAAMAS
  proceedings `Proceedings/aamas08/.../AAMAS08_IndTrack_33.pdf`.
  - **Why it is an exemplar:** turns a **Stackelberg security game** into a fielded scheduling
    system, and the contribution is that the equilibrium reasoning *survived deployment* -
    the AAMAS applications-track genre where the evidence is a working system plus its game
    model, not a benchmark table.
  - **Self-check:** if your work is applied, can you name the strategic model *and* show it
    held up against a real adversary or operational constraint, not just a simulator?

### Multiagent learning toward equilibrium (game-theoretic learning dynamics)

- **Cigler & Faltings, "Reaching Correlated Equilibria Through Multi-agent Learning," AAMAS
  2011.** Verified: IFAAMAS proceedings `Proceedings/aamas2011/papers/B4_B59.pdf`.
  - **Why it is an exemplar:** the contribution is a **learning dynamic with a game-theoretic
    target** - decentralized agents converging to a *correlated* equilibrium without a
    mediator - pairing a solution concept with the multiagent process that reaches it.
  - **Self-check:** does your learning result name the **solution concept** it converges to
    (Nash, correlated, coarse-correlated, no-regret), and prove or measure convergence *under
    other agents' simultaneous adaptation*?

### Automated negotiation under incomplete information (agent decision strategy)

- **Baarslag & Hindriks, "Accepting Optimally in Automated Negotiation with Incomplete
  Information," AAMAS 2013, pp. 715-722.** Verified: dblp `conf/atal` (AAMAS 2013 proceedings).
  - **Why it is an exemplar:** isolates one crisp interaction decision - **when an agent should
    accept an offer** given uncertainty about the opponent and a deadline - and gives an
    optimal-stopping-style answer, the AAMAS negotiation genre where a narrow strategic
    decision is analyzed rigorously.
  - **Self-check:** can your negotiation/coordination contribution be stated as a well-posed
    decision an agent makes *about another agent*, with an argued-optimal or measured-better
    policy?

---

## By topic (each cell is a verified AAMAS paper above)

| Topic | Verified AAMAS exemplar | Edition / year : pages | Method |
| --- | --- | --- | --- |
| Mixed-motive MARL / emergent cooperation | Leibo, Zambaldi, Lanctot, Marecki & Graepel, "...Sequential Social Dilemmas" | 2017 (16th) : 464-473 | Independent deep-RL in Markov social dilemmas |
| Cooperative MARL / credit assignment | Sunehag et al., "Value-Decomposition Networks..." | 2018 (17th) : 2085-2087 | Team-reward value decomposition |
| Security / real-world game theory | Pita et al., "Deployed ARMOR Protection..." | 2008 (7th) : 1805-1812 | Deployed Stackelberg security game |
| Multiagent learning toward equilibrium | Cigler & Faltings, "Reaching Correlated Equilibria..." | 2011 (10th) | Decentralized learning to correlated equilibrium |
| Automated negotiation | Baarslag & Hindriks, "Accepting Optimally..." | 2013 (12th) : 715-722 | Optimal acceptance under incomplete information |

> Five verified papers across five topic × method cells. The Leibo → Sunehag pair also
> demonstrates **a research line** (mixed-motive emergent behavior → cooperative credit
> assignment) inside the AAMAS deep-MARL wave, useful when positioning a principled follow-up.

---

## Omitted for lack of clean AAMAS verification (do not attribute to AAMAS without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking - several
are exactly the sibling-venue confusions the header warns about:

- **Lowe, Wu, Tamar, Harb, Abbeel & Mordatch, "Multi-Agent Actor-Critic for Mixed
  Cooperative-Competitive Environments" (MADDPG)** - this is **NeurIPS 2017**, not AAMAS.
  Omitted.
- **Rashid, Samvelyan, de Witt, Farquhar, Foerster & Whiteson, "QMIX"** - **ICML 2018**, not
  AAMAS, even though it is a cooperative-MARL cousin of the VDN row above. Omitted.
- **Foerster, Farquhar, Afouras, Nardelli & Whiteson, "Counterfactual Multi-Agent Policy
  Gradients" (COMA)** - **AAAI 2018**, not AAMAS. A classic near-miss. Omitted.
- **Tambe, "Towards Flexible Teamwork"** - a **JAIR (1997) journal** article that later won
  the **IFAAMAS Influential Paper Award (2012)**; the award is an AAMAS-community honor but the
  paper itself is not in the AAMAS proceedings. Listed here only as an attribution guardrail.

Before adding any new paper, confirm it on **dblp `conf/atal`** or in the **IFAAMAS
proceedings** by matching the AAMAS edition (the record names "International Conference on
Autonomous Agents and Multiagent Systems"), then record author list, year, and pages, and
update the access-date header. When in doubt, omit. If web search is unavailable, add the row
as **待核实 / TO VERIFY** with **no attribution**.
