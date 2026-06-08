# GEB Exemplars Library (theme × method)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked against
> RePEc/IDEAS and EconPapers article pages (`ideas.repec.org/a/eee/gamebe/...`,
> `econpapers.repec.org/.../gamebe/...`) — and, where available, the Elsevier PDF header line "GAMES AND
> ECONOMIC BEHAVIOR <vol>, <pages> (<year>)" — to confirm it actually appeared in **Games and Economic
> Behavior (Elsevier)**, with year and volume(issue):pages. ScienceDirect article pages returned HTTP 403
> to direct fetch (consistent with the pack's [`../official-source-map.md`](../official-source-map.md)
> note), so volume/page facts were taken from the RePEc/EconPapers indexes rather than the publisher
> page. Papers that could not be fully verified **as GEB specifically** were **omitted** and are listed
> at the bottom — this is deliberately a short, clean list (6 verified) rather than a long, uncertain one.
>
> **Sibling-confusion guard.** GEB is **not** *Econometrica*, the *Journal of Economic Theory* (JET),
> *Theoretical Economics*, *Games* (MDPI), or the *International Journal of Game Theory*. Several famous
> behavioral-game-theory papers people *associate* with GEB actually appeared in the *American Economic
> Review*, the *Quarterly Journal of Economics*, *Econometrica*, or the *Journal of Economic Dynamics and
> Control* — these are documented as omissions below so they are not misattributed to GEB.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent theorems, payoffs, or coefficients — read the original on RePEc / the authors'
> pages before citing any result or number. For GEB-specific policy, scope, and the masthead "to verify"
> notes, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **theme × method** is closest to yours, then study how that paper makes a *clean
game-theoretic move* (a characterization, a new solution concept, a sharp experimental finding) carry a
lesson legible to the *general* game-theory readership — the GEB bar (see
[`../../skills/geb-topic-selection/SKILL.md`](../../skills/geb-topic-selection/SKILL.md) and
[`../../skills/geb-writing-style/SKILL.md`](../../skills/geb-writing-style/SKILL.md)). For each, ask the
self-check question before claiming your paper is "GEB-shaped." Model your introduction on
[`../worked-examples/01-introduction.md`](../worked-examples/01-introduction.md).

---

## By theme

### Equilibrium theory: a new class of games with structure (pure theory)

- **Monderer & Shapley, "Potential Games," GEB 1996, 14(1):124–143.**
  Verified: `ideas.repec.org/a/eee/gamebe/v14y1996i1p124-143.html`; `econpapers.repec.org`
  `RePEc:eee:gamebe:v:14:y:1996:i:1:p:124-143`; Elsevier PDF header "GAMES AND ECONOMIC BEHAVIOR 14,
  124–143 (1996)."
  - **Why it is an exemplar:** defines potential functions for strategic-form games, *characterizes*
    which games admit them, and unifies a sprawl of applications under one structure — the canonical
    "small, clean concept; enormous downstream reach" GEB theory paper.
  - **Self-check:** does your concept *characterize* a class of games (existence/uniqueness/structure),
    not just solve one example?

### Solution concepts for boundedly rational play (theory meeting data)

- **McKelvey & Palfrey, "Quantal Response Equilibria for Normal Form Games," GEB 1995, 10(1):6–38.**
  Verified: `ideas.repec.org/a/eee/gamebe/v10y1995i1p6-38.html`; `econpapers.repec.org`
  `RePEc:eee:gamebe:v:10:y:1995:i:1:p:6-38`.
  - **Why it is an exemplar:** introduces a *new equilibrium concept* (statistical/quantal best response)
    that is both a theoretical object and an estimable model of real play — a solution concept that
    travels across the whole experimental literature.
  - **Self-check:** is your solution concept a genuine generalization of Nash with a precise limiting
    relationship to it, not a one-off adjustment?

### Learning & dynamics: how play converges (theory + experiment)

- **Roth & Erev, "Learning in Extensive-Form Games: Experimental Data and Simple Dynamic Models in the
  Intermediate Term," GEB 1995, 8(1):164–212.**
  Verified: `ideas.repec.org/a/eee/gamebe/v8y1995i1p164-212.html`; `econpapers.repec.org`
  `RePEc:eee:gamebe:v:8:y:1995:i:1:p:164-212`; Elsevier PDF header "GAMES AND ECONOMIC BEHAVIOR 8,
  164–212 (1995)."
  - **Why it is an exemplar:** a *low-rationality* reinforcement-learning dynamic, fit to experimental
    data, predicts intermediate-run play across several games — the model for pairing a simple learning
    rule with data instead of assuming equilibrium.
  - **Self-check:** does your dynamic make a falsifiable out-of-equilibrium prediction that the data can
    confirm or reject?

### Behavioral game theory: a model of strategic reasoning, tested (model + experiment)

- **Stahl & Wilson, "On Players' Models of Other Players: Theory and Experimental Evidence," GEB 1995,
  10(1):218–254.**
  Verified: `ideas.repec.org/a/eee/gamebe/v10y1995i1p218-254.html`; `econpapers.repec.org`
  `RePEc:eee:gamebe:v:10:y:1995:i:1:p:218-254`.
  - **Why it is an exemplar:** posits a *family of boundedly rational types* (a precursor of the level-k /
    cognitive-hierarchy program) and *identifies the type distribution* from experimental data — a model
    well-identified against alternatives, which is the behavioral-advance bar in
    [`../../skills/geb-topic-selection/SKILL.md`](../../skills/geb-topic-selection/SKILL.md).
  - **Self-check:** is your behavioral model identified *against* its rivals in the design, not just
    consistent with the data after the fact?

### Experimental game theory: isolating a single behavioral force (experiment)

- **Forsythe, Horowitz, Savin & Sefton, "Fairness in Simple Bargaining Experiments," GEB 1994,
  6(3):347–369.**
  Verified: `ideas.repec.org/a/eee/gamebe/v6y1994i3p347-369.html`.
  - **Why it is an exemplar:** a clean 2×2 design (ultimatum vs. dictator × pay vs. no-pay) shows that
    *fairness alone* cannot explain proposer behavior — a textbook example of using a minimal-pair
    experiment to falsify one explanation. Cluster inference at the independent-session level (see
    [`../external_tools.md`](../external_tools.md)).
  - **Self-check:** does your experiment vary *one* thing at a time so the comparison cleanly identifies
    the mechanism, with power justified per treatment cell?

### Mechanism / market design: an equivalence between constructive mechanisms (theory)

- **Sönmez & Ünver, "House Allocation with Existing Tenants: An Equivalence," GEB 2005, 52(1):153–185.**
  Verified: `ideas.repec.org/a/eee/gamebe/v52y2005i1p153-185.html`.
  - **Why it is an exemplar:** proves that two seemingly different allocation mechanisms (a core-based
    rule with random endowments, and a top-trading-cycles variant) are *equivalent* — an
    impossibility/possibility-style result that tells designers two procedures are the same object.
  - **Self-check:** does your design result *characterize or equate* mechanisms (strategy-proofness,
    equivalence, an impossibility), rather than just propose one mechanism?

---

## By theme (each cell is a verified GEB paper above)

| Theme | Verified GEB exemplar | Year / vol(issue):pages | Method |
| --- | --- | --- | --- |
| Equilibrium theory / new class of games | Monderer & Shapley, "Potential Games" | 1996, 14(1):124–143 | Pure theory |
| Solution concepts | McKelvey & Palfrey, "Quantal Response Equilibria for Normal Form Games" | 1995, 10(1):6–38 | Theory + estimation |
| Learning & dynamics | Roth & Erev, "Learning in Extensive-Form Games" | 1995, 8(1):164–212 | Theory + experiment |
| Behavioral game theory | Stahl & Wilson, "On Players' Models of Other Players" | 1995, 10(1):218–254 | Model + experiment |
| Experimental game theory | Forsythe, Horowitz, Savin & Sefton, "Fairness in Simple Bargaining Experiments" | 1994, 6(3):347–369 | Experiment |
| Mechanism / market design | Sönmez & Ünver, "House Allocation with Existing Tenants: An Equivalence" | 2005, 52(1):153–185 | Mechanism/matching theory |

---

## Omitted for lack of GEB verification (do not attribute to GEB without re-checking)

To keep the list zero-hallucination, these closely related and frequently-cited papers were **excluded**
after web checking — each was verified to belong to a **different journal**, and is recorded here only as
a misattribution guardrail (per the sibling-confusion list above):

- **Nagel, "Unraveling in Guessing Games: An Experimental Study" (1995)** — verified to be in the
  *American Economic Review* 85(5):1313–1326, **not GEB**, despite being a foundational beauty-contest /
  level-k paper.
- **Fehr & Schmidt, "A Theory of Fairness, Competition, and Cooperation" (1999)** — *Quarterly Journal of
  Economics* 114(3):817–868, **not GEB**.
- **Charness & Rabin, "Understanding Social Preferences with Simple Tests" (2002)** — *Quarterly Journal
  of Economics* 117(3):817–869, **not GEB**.
- **Camerer, Ho & Chong, "A Cognitive Hierarchy Model of Games" (2004)** — *Quarterly Journal of
  Economics* 119(3):861–898, **not GEB**.
- **Costa-Gomes & Crawford, "Cognition and Behavior in Two-Person Guessing Games" (2006)** — *American
  Economic Review* 96(5):1737–1768, **not GEB**; and **Costa-Gomes, Crawford & Broseta, "Cognition and
  Behavior in Normal-Form Games" (2001)** — *Econometrica* 69(5):1193–1235, **not GEB**.
- **Bolton & Ockenfels, "ERC: A Theory of Equity, Reciprocity, and Competition" (2000)** — *American
  Economic Review* 90(1):166–193, **not GEB**.
- **Aumann & Brandenburger, "Epistemic Conditions for Nash Equilibrium" (1995)** — *Econometrica*
  63(5):1161–1180, **not GEB**.
- **Fudenberg & Levine, "Consistency and Cautious Fictitious Play" (1995)** — *Journal of Economic
  Dynamics and Control* 19(5–7):1065–1089, **not GEB**.

Before adding any new paper to this library, confirm it on `ideas.repec.org/a/eee/gamebe/...` or
`econpapers.repec.org/.../gamebe/...` (article page with volume(issue):pages) and update the access-date
header. When in doubt, omit.
