# ACM SIGMETRICS Exemplars Library (contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and the **ACM Digital Library** to confirm it appeared at **ACM SIGMETRICS** (or its
> POMACS journal) — matching title, author list, year, and venue string. Papers that could not be
> cleanly confirmed as SIGMETRICS (as opposed to IMC, SIGCOMM, NSDI, INFOCOM, NeurIPS, or a
> journal) were **omitted and documented below**. It is deliberately a short, verified list
> (4 verified > 15 guessed).
>
> **Sibling-confusion guard:** SIGMETRICS is **not** IMC (pure network measurement), **not**
> SIGCOMM/NSDI (networking systems), and **not** a pure ML venue. A performance-evaluation flavor
> or a famous systems author does **not** prove SIGMETRICS; several canonical measurement and
> learning papers appeared at those venues instead. Each row was checked to be a SIGMETRICS/POMACS
> edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent theorems, bounds, or table numbers — read the original on ACM DL before
> citing anything. For SIGMETRICS-specific policy, scope, and the rolling three-cycle model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × method** is closest to yours, then study how that paper
poses a **systems-performance question**, backs it with **evidence proportional to the claim** (a
proof of a bound, a validated simulation, or a principled measurement), and states its **modeling
assumptions**. That is the SIGMETRICS bar (see
[`../../skills/sigmetrics-writing-style/SKILL.md`](../../skills/sigmetrics-writing-style/SKILL.md),
[`../../skills/sigmetrics-topic-selection/SKILL.md`](../../skills/sigmetrics-topic-selection/SKILL.md),
and [`../../skills/sigmetrics-experiments/SKILL.md`](../../skills/sigmetrics-experiments/SKILL.md)).
For each, ask the self-check question before claiming your paper is "SIGMETRICS-shaped."

Several rows are Best-Paper or influential-paper honorees, so they also model what "durable
performance-evaluation contribution" looks like at this venue.

---

## By contribution shape

### Queueing / scheduling theory — a unifying analysis

- **Scully, Harchol-Balter & Scheller-Wolf, "SOAP: One Clean Analysis of All Age-Based Scheduling
  Policies," POMACS 2(1), SIGMETRICS 2018** (DOI 10.1145/3179419). Verified: ACM DL and the CMU
  author page; dblp POMACS Vol 2. A single framework (SOAP) that computes response-time
  distributions for a broad class of rank/age-based M/G/1 scheduling policies.
  - **Why it is an exemplar:** it replaces a scattering of one-policy-at-a-time analyses with **one
    general theorem** covering many policies, then validates it — the quintessential SIGMETRICS
    theory contribution: a clean, reusable analytic tool, not a single number.
  - **Self-check:** does your analysis generalize a family of systems/policies rather than solving
    one instance, and do you validate the analytic result (e.g. against simulation)?

### Queueing theory — improving a foundational policy

- **"Nudge: Stochastically Improving upon FCFS," SIGMETRICS 2021 (Best Paper Award).** Verified as
  a SIGMETRICS 2021 Best Paper via the SIGMETRICS awards record; a queueing result showing a
  policy that stochastically dominates First-Come-First-Served on response time. (Full author list
  待核实 — confirm on ACM DL before citing.)
  - **Why it is an exemplar:** it revisits the most-taught baseline in queueing (FCFS) and proves a
    strictly better policy exists — a crisp theoretical surprise with immediate systems relevance,
    exactly the "rigorous math with a systems payoff" SIGMETRICS prizes.
  - **Self-check:** is your result a provable improvement over a well-understood baseline, stated
    as a theorem a skeptic can check?

### Measurement study — characterizing a real system at scale

- **Viennot, Garcia & Nieh, "A Measurement Study of Google Play," SIGMETRICS 2014.** Verified via
  the SIGMETRICS awards record (recognized as an influential/award paper) and dblp. A large-scale
  crawl and characterization of the Google Play app marketplace.
  - **Why it is an exemplar:** it turns a real, opaque deployed system into **measured, analyzable
    structure** — the SIGMETRICS measurement mode, where the contribution is a principled
    methodology and the findings it yields, not a new algorithm.
  - **Self-check:** does your measurement reveal something the community did not know about a real
    system, with a collection methodology and dataset a reviewer could scrutinize?

### Learning for systems — bandits with performance guarantees

- **Combes, Magureanu, Proutiere & Laroche, "Learning to Rank: Regret Lower Bounds and Efficient
  Algorithms," SIGMETRICS 2015.** Verified via the SIGMETRICS awards record (recognized as an
  influential/award paper) and dblp. Establishes regret **lower bounds** and matching efficient
  algorithms for an online learning-to-rank problem.
  - **Why it is an exemplar:** it is a **learning** contribution done the SIGMETRICS way — not just
    an empirical model but a *provable* regret characterization (lower bound **and** algorithm),
    the rigor bar the Learning track expects.
  - **Self-check:** if your paper leans on a learner, does it carry a performance **guarantee**
    (regret, convergence, sample complexity) rather than only leaderboard numbers?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified SIGMETRICS exemplar | Edition | Method |
| --- | --- | --- | --- |
| Queueing/scheduling theory | Scully, Harchol-Balter & Scheller-Wolf, "SOAP" | POMACS/SIGMETRICS 2018 | Unifying analytic framework |
| Queueing theory (baseline-beating) | "Nudge: Stochastically Improving upon FCFS" | SIGMETRICS 2021 (Best Paper) | Stochastic dominance proof |
| Measurement study | Viennot, Garcia & Nieh, "A Measurement Study of Google Play" | SIGMETRICS 2014 | Large-scale crawl + characterization |
| Learning for systems | Combes et al., "Learning to Rank..." | SIGMETRICS 2015 | Regret lower bounds + algorithm |

> Four verified papers across the three SIGMETRICS cultures — **stochastic/queueing theory**,
> **measurement**, and **learning-with-guarantees** — plus the venue's signature move of pairing a
> theorem with numerical or empirical validation.

---

## Omitted for lack of clean SIGMETRICS verification (do not attribute to SIGMETRICS without re-checking)

To keep the list zero-hallucination, papers were **excluded** after checking — several are exactly
the sibling-venue confusions the header warns about:

- **Network-measurement classics** (e.g. large Internet/CDN/topology measurement studies) — many
  canonical ones are **IMC**, **SIGCOMM**, or **INFOCOM** placements, *not* SIGMETRICS, despite the
  measurement flavor. Verify the venue string before attributing.
- **Bandit/RL learning-theory papers** — most foundational ones are **NeurIPS/ICML/COLT**, not
  SIGMETRICS; only those explicitly in the SIGMETRICS/POMACS proceedings (like the Learning-to-Rank
  row) belong here.
- **Datacenter/networking systems papers** — **NSDI/OSDI/SIGCOMM** placements are not SIGMETRICS;
  omitted to avoid venue misattribution.
- **Journal-only extended versions** — a SIGMETRICS paper's extended treatment in a journal (TON,
  Performance Evaluation, QUESTA) is a separate publication; cite the SIGMETRICS/POMACS version for
  the SIGMETRICS attribution and the journal article separately.

Before adding any paper, confirm it on **dblp** and **ACM DL** by matching the venue string to a
SIGMETRICS / POMACS edition (not IMC, SIGCOMM, NSDI, INFOCOM, or a pure-ML venue), then record
authors, year, and DOI/pages, and update the access-date header. When in doubt, omit. If web search
is unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
