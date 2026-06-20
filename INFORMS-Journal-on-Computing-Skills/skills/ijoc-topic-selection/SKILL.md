---
name: ijoc-topic-selection
description: Use when deciding whether a project is computing-first enough for an INFORMS Journal on Computing (IJOC) submission and which of its 10 technical areas fits. Scopes the contribution to the OR↔computing interface; it does not invent results or citations.
---

# Topic Selection (ijoc-topic-selection)

## When to trigger

- You have an OR/analytics result and are unsure whether the **computing is the contribution** or merely the vehicle
- You cannot say which of IJOC's **10 technical areas** the paper belongs to, or it straddles two
- The work could plausibly go to *Operations Research*, *Management Science*, *Mathematical Programming Computation*, or an ACM/IEEE venue and you need to decide
- A coauthor wants the "is this an IJOC paper?" call before any writing starts

## The IJOC scope test

IJOC sits at the **intersection of OR/MS and computer science**. A paper passes the scope test only if the **computational and/or methodological advance is the headline** — a new algorithm, a sharper formulation, a learning method that helps an OR task, a simulation or computational-probability method, or tooling that changes what OR practitioners can compute. Run the four questions in order; a "no" on Q1 usually means a different journal.

1. **Is the news computational/methodological, not the application?** "We solved a logistics problem with CPLEX" is not IJOC; "we designed a decomposition that solves an order-of-magnitude larger logistics instance" is. The application motivates; the method is the contribution.
2. **Is there a measurable computational claim?** IJOC contributions are checkable: faster, larger, tighter bounds, better-quality solutions at equal time, better generalization, lower variance. If you cannot name the axis on which you win, you have a topic but not yet an IJOC paper.
3. **Will it survive a fair experimental comparison?** If the advantage rests on hand-picked instances or asymmetric tuning, the Area Editor will see it. Pick a topic where you can win on **standard, public benchmark instances** against a **credible baseline**.
4. **Can the artifact be deposited and reproduced?** IJOC hosts code/data in its **GitHub Software and Data Repository**. A topic whose data cannot be shared or whose results cannot be reproduced is a poor fit; plan the deposit now, not at acceptance.

## Choosing the technical area

At submission you select **one of 10 areas** in ScholarOne, and that choice routes you to an Area Editor who decides suitability (and desk-rejects ~40%). The wrong area invites a fast rejection. IJOC's areas span computational optimization / mathematical programming, stochastic and robust optimization, heuristic search and metaheuristics, simulation, computational probability, machine learning and data science for OR, networks/graphs, and computational tooling (full current list 待核实 — confirm on the official Areas page). Map your headline method (not your application domain) to the area; if you straddle, pick the area whose Area Editor and reviewer pool will best judge the *method*, and say so in the cover letter.

## Sibling boundary — pick the right venue

| If the news is… | Go to | Not IJOC because |
|-----------------|-------|------------------|
| broad OR theory / a substantive OR model | *Operations Research* | IJOC wants the computing to be the advance |
| a broad management-science result | *Management Science* | same — computing is incidental there |
| a pure computational mathematical-programming method/software | *Mathematical Programming Computation* | MPC is narrower MP-computation; IJOC spans simulation/ML/probability/tooling too |
| optimization theory / new optimization paradigm | *INFORMS Journal on Optimization* | IJOC is the OR↔computing interface, not optimization theory |
| a CS-systems or ML-theory result with no OR task | ACM/IEEE venue | IJOC requires an OR/MS connection |

## Rescuing a borderline topic

If the project fails Q1 (the news is the application), there are two honest paths back to IJOC rather than abandoning it. (a) **Find the computational obstacle the application exposed** — if the off-the-shelf solver failed at the real scale, the methodological fix that makes it tractable *is* the IJOC paper, and the application becomes the motivating instance set. (b) **Generalize from one instance to a class** — a method that solves one company's problem is an application; the same method shown to dominate on a *family* of standard instances is computing. If neither path exists, the work is genuinely an *Operations Research* / *Management Science* model paper, and forcing it into IJOC wastes a desk-reject. Make this call before writing, not after the Area Editor makes it for you.

## Checklist

- [ ] The headline is a computational/methodological advance, not an application win
- [ ] The win axis is named (time / size / bound / quality / generalization / variance) and measurable
- [ ] A public benchmark instance set and a credible baseline exist for fair comparison
- [ ] One of the 10 technical areas is chosen and justified by the *method*, not the domain
- [ ] The code/data can be deposited and reproduced in the IJOC GitHub repository
- [ ] The sibling-boundary call is explicit (why IJOC and not OR / MS / MPC / IJOO)

## Anti-patterns

- An application paper dressed as computing — solver used off-the-shelf, no methodological news
- "We are faster" with no benchmark instances and no baseline named
- Submitting to a technical area that mismatches the method, inviting an Area-Editor desk reject
- Choosing a topic whose data is proprietary and undepositable, then discovering the reproducibility regime at acceptance
- Pitching to IJOC what is really an *Operations Research* model paper or an *IJOO* optimization-theory paper

## Output format

```text
【Journal】INFORMS Journal on Computing
【Skill】ijoc-topic-selection
【Verdict】computing-first IJOC fit / reroute to sibling / not yet
【Headline advance】the one computational/methodological claim
【Win axis】time / size / bound / quality / generalization / variance
【Technical area】chosen area + why (method-based)
【Sibling boundary】why IJOC and not OR / MS / MPC / IJOO
【Source status】verified URL / 待核实
【Next skill】ijoc-theory-development
```
