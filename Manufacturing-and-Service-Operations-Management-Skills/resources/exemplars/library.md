# M&SOM Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked against INFORMS
> PubsOnLine article pages (`pubsonline.informs.org/doi/10.1287/msom...`) to confirm it actually
> appeared in *Manufacturing & Service Operations Management* (M&SOM), with the `10.1287/msom` DOI stem.
> Candidate papers without an M&SOM placement were **omitted** and are documented below — this is
> deliberately a short, clean list rather than a long, uncertain one.
>
> **Sibling-confusion guard.** M&SOM is **not** *Operations Research* (`10.1287/opre`), *Management
> Science* (`10.1287/mnsc`), *Production and Operations Management* (POM), or the *Journal of Operations
> Management* (JOM). Two near-miss classics that operations researchers routinely misattribute to M&SOM
> are confirmed below to live in sibling INFORMS journals.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent model results, theorems, coefficients, or specific findings — read the original on
> PubsOnLine before citing any number. For M&SOM-specific policy and a "do-not-misattribute" list, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes an
**operational decision** the center of the contribution — the M&SOM gate (see
[`../../skills/msom-topic-selection/SKILL.md`](../../skills/msom-topic-selection/SKILL.md) and
[`../../skills/msom-contribution-framing/SKILL.md`](../../skills/msom-contribution-framing/SKILL.md)).
For each, ask the self-check question before claiming your paper is "M&SOM-shaped."

---

## By method

### Analytical retail model with consumer behavior (stochastic modeling)

- **Cachon, Terwiesch & Xu, "Retail Assortment Planning in the Presence of Consumer Search," M&SOM 2005, 7(4):330–346.**
  Verified: `pubsonline.informs.org/doi/10.1287/msom.1050.0088`.
  - **Why it is an exemplar:** the operational decision — *how broad an assortment to stock* — is the
    contribution, and consumer search is modeled only insofar as it changes that stocking lever. The
    structure of the optimal assortment, not the model machinery, is what travels.
  - **Self-check:** is the operational decision (what to stock / how much / when to act) the lead, with
    the behavioral or stochastic model in service of it — not the other way around?

### Behavioral / service queueing model (stochastic service operations)

- **Guo, Haviv, Luo & Wang, "Signaling Service Quality Through Queue Disclosure," M&SOM 2023, 25(2) (DOI `10.1287/msom.2022.1170`).**
  Verified: `pubsonline.informs.org/doi/10.1287/msom.2022.1170` (journal *M&SOM*, vol. 25(2); published online December 2022).
  - **Why it is an exemplar:** the operational lever is a concrete service-design choice — *whether the
    server reveals or conceals its queue length* — and the paper studies how that disclosure decision
    signals quality to waiting customers. A clean "one operational decision, characterized" service paper.
  - **Self-check:** does your service model deliver an actionable design rule (disclose / pool / route /
    prioritize), rather than only a behavioral observation?

### Empirical healthcare operations (field / survey data)

- **Tucker, "An Empirical Study of System Improvement by Frontline Employees in Hospital Units," M&SOM 2007, 9(4):492–505.**
  Verified: `pubsonline.informs.org/doi/10.1287/msom.1060.0156`.
  - **Why it is an exemplar:** an empirical OM paper whose contribution is an identified operational
    effect — the conditions under which frontline staff fix the work system rather than work around
    failures — with a clear operational implication for how units are managed. The empirical-OM
    counterpart to the analytical exemplars. Pairs with the empirical command chain in
    [`../code/`](../code/).
  - **Self-check:** does your empirical study identify an operational effect and the policy it implies,
    not just a correlation in an operations dataset?

### Field-grounded retail operations review / agenda (operations practice & directions)

- **Caro, Kök & Martínez-de-Albéniz, "The Future of Retail Operations," M&SOM 2020 (DOI `10.1287/msom.2019.0824`).**
  Verified: `pubsonline.informs.org/doi/10.1287/msom.2019.0824`.
  - **Why it is an exemplar:** a forward-looking piece organized entirely around retail *operational*
    decisions (assortment, inventory, fulfillment, omnichannel) — a model of how to frame an agenda in
    the vocabulary of operational levers rather than abstract theory.
  - **Self-check:** if you are writing a perspective/agenda piece, is it organized around operational
    decisions, and is it routed to the right venue (OM Forum vs. a standard contribution)?

### Empirical-methods agenda for OM (what good empirical OM is)

- **Fisher, Olivares & Staats, "Why Empirical Research Is Good for Operations Management, and What Is Good Empirical Operations Management?," M&SOM 2020, 22(1):170–178.**
  Verified: `pubsonline.informs.org/doi/10.1287/msom.2019.0812`.
  - **Why it is an exemplar:** states, from within M&SOM, the bar an empirical-OM contribution must
    clear — operational relevance plus credible identification. Read it as the rubric the empirical lane
    in [`../../skills/msom-data-analysis/SKILL.md`](../../skills/msom-data-analysis/SKILL.md) is graded
    against.
  - **Self-check:** does your empirical paper clear *both* tests this piece names — operational
    importance and identification credibility?

### Healthcare-operations empirical agenda (review of an empirical subfield)

- **KC, Scholtes & Terwiesch, "Empirical Research in Healthcare Operations: Past Research, Present Understanding, and Future Opportunities," M&SOM 2020, 22(1):73–83.**
  Verified: `pubsonline.informs.org/doi/10.1287/msom.2019.0826`.
  - **Why it is an exemplar:** maps an entire empirical-OM subfield (healthcare) by the operational
    decisions it studies — workload, discharge, congestion — a template for positioning an empirical
    contribution against a literature organized by *operational lever*.
  - **Self-check:** can you place your empirical paper on a map of operational decisions a subfield
    already studies, and say which decision you move?

---

## By topic (each cell is a verified M&SOM paper above)

| Topic | Verified M&SOM exemplar | Year / vol(issue) or DOI | Method |
| --- | --- | --- | --- |
| Retail assortment / stocking | Cachon, Terwiesch & Xu, "Retail Assortment Planning…" | 2005, 7(4) | Analytical (consumer search) |
| Service / queueing design | Guo, Haviv, Luo & Wang, "Signaling Service Quality Through Queue Disclosure" | 2023, 25(2) | Analytical (service/queueing) |
| Healthcare operations (frontline) | Tucker, "System Improvement by Frontline Employees…" | 2007, 9(4) | Empirical (survey/field) |
| Retail operations agenda | Caro, Kök & Martínez-de-Albéniz, "Future of Retail Operations" | DOI msom.2019.0824 | Perspective / agenda |
| Empirical-OM standards | Fisher, Olivares & Staats, "Why Empirical Research Is Good…" | 2020, 22(1) | Empirical-methods agenda |
| Healthcare-OM empirical agenda | KC, Scholtes & Terwiesch, "Empirical Research in Healthcare Operations" | 2020, 22(1) | Empirical review |

---

## Omitted for sibling-confusion (do not attribute to M&SOM without re-checking)

To keep the list zero-hallucination, the following are **excluded** after checking — several are
canonical OM papers that are *not* in M&SOM:

- **Cachon & Lariviere, "Supply Chain Coordination with Revenue-Sharing Contracts: Strengths and
  Limitations" (2005)** — confirmed to be in ***Management Science*** 51(1):30–44 (DOI
  `10.1287/mnsc.1040.0215`), **not M&SOM**. Listed only as a sibling-confusion guardrail.
- **Netessine & Rudi, "Centralized and Competitive Inventory Models with Demand Substitution" (2003)** —
  confirmed to be in ***Operations Research*** 51(2):329–335 (DOI `10.1287/opre.51.2.329.12788`), **not
  M&SOM**. A frequently misremembered placement; listed as a guardrail.
- **Any POM or JOM paper** — these journals are *not* INFORMS M&SOM and carry no `10.1287/msom` DOI; do
  not import exemplars from them into this list without re-verifying an M&SOM placement.

Before adding any new paper to this library, confirm it on `pubsonline.informs.org` with a
`10.1287/msom...` DOI (article page with volume/issue), and update the access-date header. When the DOI
stem is `mnsc`, `opre`, or anything other than `msom`, it is a sibling journal — exclude it. When in
doubt, omit.
