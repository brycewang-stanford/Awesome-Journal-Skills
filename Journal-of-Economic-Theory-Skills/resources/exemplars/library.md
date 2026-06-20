# JET Exemplars Library (theme × theory area)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked against its
> Elsevier / ScienceDirect article page to confirm it actually appeared in *The Journal of Economic
> Theory* (publisher Elsevier; DOI/PII family `10.1016/0022-0531...` / `10.1016/j.jet...`, ScienceDirect
> PII beginning `0022-0531` or `S0022-0531`). Papers not fully verified **as JET** — or
> papers found in a sibling journal — were **omitted and documented below**. This is
> deliberately a short, clean list (6 verified) rather than a long, uncertain one.
>
> **Sibling-confusion guard.** JET is **not** *Econometrica*, *Theoretical Economics*, *Games and
> Economic Behavior* (GEB), the *RAND Journal of Economics*, or the *Journal of Mathematical Economics*.
> Several canonical theory papers live in those journals, not JET; see the omissions section.
>
> **Use principle (zero hallucination):** this file gives **design positioning only** — what makes each
> a model JET contribution. It does **not** reproduce or invent theorem statements, parameters, or
> proofs; read the original on ScienceDirect before citing any result. For JET-specific scope, review
> model, and house-style policy, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

JET accepts a paper because it is a **rigorous, original theoretical contribution** — a theorem, a new
model, or a characterization, with empirical/computational content admitted only when grounded in
theory (see [`../../skills/jet-topic-selection/SKILL.md`](../../skills/jet-topic-selection/SKILL.md)).
Pick the row whose **theory area × question** is closest to yours, then study how that paper states one
sharp result and makes its significance legible on the first page — the JET bar (see
[`../../skills/jet-contribution-framing/SKILL.md`](../../skills/jet-contribution-framing/SKILL.md) and
[`../../skills/jet-writing-style/SKILL.md`](../../skills/jet-writing-style/SKILL.md)). For each, ask the
self-check question before claiming your paper is "JET-shaped."

---

## By theory area

### General equilibrium with infinitely many commodities (GE / mathematical economics)

- **Bewley, "Existence of Equilibria in Economies with Infinitely Many Commodities," JET 1972, 4(3):514–540.**
  Verified: ScienceDirect PII `0022053172901366` (`sciencedirect.com/science/article/abs/pii/0022053172901366`).
  - **Why it is an exemplar:** extends the existence theorem to an infinite-dimensional commodity space
    by introducing finite-dimensional (Galerkin) approximations and weak-compactness arguments into
    general-equilibrium theory — a clean existence theorem whose method became a standard tool.
  - **Self-check:** is your headline an existence/characterization *theorem* under transparent
    assumptions, with the proof technique (here, approximation + compactness) named and motivated, not
    hidden — per [`../../skills/jet-identification-strategy/SKILL.md`](../../skills/jet-identification-strategy/SKILL.md)?

### Strategy-proofness and social choice (mechanism design / social choice)

- **Satterthwaite, "Strategy-proofness and Arrow's Conditions: Existence and Correspondence Theorems for Voting Procedures and Social Welfare Functions," JET 1975, 10(2):187–217.**
  Verified: ScienceDirect PII `0022053175900502` (`sciencedirect.com/science/article/abs/pii/0022053175900502`).
  - **Why it is an exemplar:** proves that every strategy-proof voting procedure is dictatorial and ties
    strategy-proofness to Arrow's conditions — one impossibility theorem that reorganized mechanism
    design and social choice. The "Satterthwaite" half of the Gibbard–Satterthwaite theorem (Gibbard's
    is in *Econometrica*; see omissions).
  - **Self-check:** does your result *adjudicate* a possibility/impossibility question the field already
    argues about, stated as a self-contained theorem with its scope (here, range ≥ 3 alternatives) made
    explicit?

### Decision theory: temporal preferences under uncertainty (decision theory)

- **Kreps & Porteus, "Temporal von Neumann–Morgenstern and Induced Preferences," JET 1979, 20(1):81–109.**
  Verified: ScienceDirect PII `0022053179900632` (`sciencedirect.com/science/article/abs/pii/0022053179900632`).
  - **Why it is an exemplar:** an axiomatic representation result for preferences over the *timing* of
    resolution of uncertainty — the foundation later asset-pricing and recursive-utility work builds on.
    A model whose primitives and axioms are stated so cleanly the representation is checkable.
  - **Self-check:** are your axioms each load-bearing (you can name the step that fails without each one)
    and your representation theorem self-contained, per `jet-identification-strategy`'s assumptions
    checklist?

### Information economics: no-trade under common knowledge (information economics)

- **Milgrom & Stokey, "Information, Trade and Common Knowledge," JET 1982, 26(1):17–27.**
  Verified: ScienceDirect PII `0022053182900461` (`sciencedirect.com/science/article/pii/0022053182900461`).
  - **Why it is an exemplar:** the **no-trade theorem** — if a Pareto-efficient allocation among
    weakly-risk-averse agents with concordant priors becomes commonly known to admit a Pareto-improving
    trade, no agent can strictly gain, so they may as well not trade. One short, decisive result with
    enormous downstream reach (speculation, market microstructure).
  - **Self-check:** can your central mechanism be stated and its bite felt in a single short theorem a
    non-specialist theorist grasps immediately — the JET "small model, large lesson" target?

### Repeated games with private information (game theory)

- **Fudenberg & Levine, "An Approximate Folk Theorem with Imperfect Private Information," JET 1991, 54(1):26–47.**
  Verified: ScienceDirect PII `002205319190103B` (`sciencedirect.com/science/article/abs/pii/002205319190103B`).
  - **Why it is an exemplar:** a folk-theorem result for repeated games where players are imperfectly,
    privately informed about the consequences of opponents' actions — extends the equilibrium-payoff
    characterization to a harder information environment, with the scope ("informationally connected,"
    specified intertemporal criteria) stated precisely.
  - **Self-check:** when you generalize a known theorem to a harder case, is the *extra* assumption that
    buys the result named in the statement (not smuggled into the proof), so a referee sees exactly the
    delta — per `jet-contribution-framing` right-sizing?

### Matching / market design grounded in theory (matching, market design)

- **Roth, Sönmez & Ünver, "Pairwise Kidney Exchange," JET 2005, 125(2):151–188.**
  Verified: ScienceDirect PII `S0022053105001055` (`sciencedirect.com/science/article/abs/pii/S0022053105001055`).
  - **Why it is an exemplar:** a real market-design problem (constrained kidney exchange) solved with a
    theorem — a class of constrained-efficient mechanisms that are strategy-proof under 0–1 preferences.
    The model is the contribution; the application is grounded in it, exactly the empirical/applied
    content `jet-topic-selection` admits.
  - **Self-check:** if your paper is motivated by an application, is the deliverable still a
    *characterization or mechanism with a proof* (not a calibration), so it clears the theory-first gate?

---

## By theme (each cell is a verified JET paper above)

| Theme | Verified JET exemplar | Year / vol(issue) | Theory area |
| --- | --- | --- | --- |
| Existence in infinite-dimensional GE | Bewley, "Existence of Equilibria … Infinitely Many Commodities" | 1972, 4(3) | General equilibrium |
| Strategy-proofness / impossibility | Satterthwaite, "Strategy-proofness and Arrow's Conditions" | 1975, 10(2) | Mechanism design / social choice |
| Timing of uncertainty resolution | Kreps & Porteus, "Temporal von Neumann–Morgenstern" | 1979, 20(1) | Decision theory |
| No-trade under common knowledge | Milgrom & Stokey, "Information, Trade and Common Knowledge" | 1982, 26(1) | Information economics |
| Folk theorem, private information | Fudenberg & Levine, "Approximate Folk Theorem …" | 1991, 54(1) | Game theory (repeated games) |
| Constrained-efficient market design | Roth, Sönmez & Ünver, "Pairwise Kidney Exchange" | 2005, 125(2) | Matching / market design |

---

## Omitted for lack of full JET verification (do not attribute to JET without re-checking)

To keep the list zero-hallucination, the following frequently-cited theory papers were **excluded**
after checking — most are in a **sibling** journal, which is precisely the confusion this library
guards against:

- **Gibbard, "Manipulation of Voting Schemes: A General Result" (1973)** — verified to be in
  ***Econometrica*** 41(4):587–601, **not JET**. (Its companion, Satterthwaite 1975, *is* JET and is
  listed above.)
- **Myerson, "Optimal Auction Design" (1981)** — in ***Mathematics of Operations Research*** 6(1):58–73,
  **not JET**.
- **Aumann, "Subjectivity and Correlation in Randomized Strategies" (1974)** — in the ***Journal of
  Mathematical Economics*** 1(1):67–96, **not JET** (a JET sibling on the do-not-confuse list).
- **Rubinstein, "Perfect Equilibrium in a Bargaining Model" (1982)** — in ***Econometrica*** 50(1):97–109,
  **not JET**.
- **Kelso & Crawford, "Job Matching, Coalition Formation, and Gross Substitutes" (1982)** — in
  ***Econometrica*** 50(6):1483–1504, **not JET**.
- **Shapley & Shubik, "The Assignment Game I: The Core" (1972)** — in the ***International Journal of
  Game Theory*** 1(1):111–130, **not JET**.
- **Gul & Pesendorfer, "Temptation and Self-Control" (2001)** — in ***Econometrica*** 69(6):1403–1435,
  **not JET**. (A JET *application* of self-control preferences exists, but the foundational
  axiomatization is Econometrica; not attributed here.)
- **Diamond & Dybvig, "Bank Runs, Deposit Insurance, and Liquidity" (1983)** — in the ***Journal of
  Political Economy*** 91(3):401–419, **not JET**.

Before adding any new paper to this library, confirm it on ScienceDirect (article page with a JET
volume/issue and a `0022-0531` / `S0022-0531` PII, DOI family `10.1016/0022-0531...` or
`10.1016/j.jet...`) and update the access-date header. When in doubt, omit.
