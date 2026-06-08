# IJCAI Exemplars Library (topic × method)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked against the
> **IJCAI Proceedings** archive (`ijcai.org/proceedings/...` or `ijcai.org/Proceedings/...`) to confirm it
> actually appeared in the proceedings of the **International Joint Conference on Artificial Intelligence
> (IJCAI)**, with year and the proceedings page/PDF path. Papers that could not be confirmed *in the IJCAI
> proceedings* were **omitted and documented** below — this is deliberately a short, clean list rather than a
> long, uncertain one.
>
> **Sibling-confusion guard.** IJCAI is **not** AAAI, NeurIPS, ICML, ICLR, ACL, AAMAS, or KR. A paper being
> famous, or being an AI classic, does **not** mean it was at IJCAI. Several well-known works were excluded
> precisely because they were published at a sibling venue (see the omissions section). Before adding any
> paper, open its `ijcai.org` proceedings page and confirm the year and proceedings entry.
>
> **Use principle (zero hallucination):** this file gives **framing and design positioning only**. It does
> **not** reproduce or invent any reported metric, accuracy number, or finding — read the original on
> `ijcai.org` before citing anything. For IJCAI-specific policy and scope, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **topic × method** is closest to yours, then study how that paper puts a **broad-AI**
contribution on the first page and maps each claim to verifiable evidence — the IJCAI bar (see
[`../../skills/ijcai-writing-style/SKILL.md`](../../skills/ijcai-writing-style/SKILL.md),
[`../../skills/ijcai-topic-selection/SKILL.md`](../../skills/ijcai-topic-selection/SKILL.md), and
[`../../skills/ijcai-experiments/SKILL.md`](../../skills/ijcai-experiments/SKILL.md)). For each, ask the
self-check question before claiming your paper is "IJCAI-shaped." Model your own intro on
[`../worked-examples/01-introduction.md`](../worked-examples/01-introduction.md).

---

## By method

### Empirical comparison of learning paradigms (machine learning)

- **Fisher & McKusick, "An Empirical Comparison of ID3 and Back-propagation," IJCAI-89 (pp. 788–793).**
  Verified: `ijcai.org/Proceedings/89-1/Papers/126.pdf` (IJCAI 1989 proceedings, comparing the ID3
  decision-tree learner and back-propagation).
  - **Why it is an exemplar:** a head-to-head, controlled empirical comparison that adjudicates a debate the
    whole field cared about (symbolic vs. connectionist learning) rather than tuning one method on one
    dataset — broad-AI significance from a clean experimental design.
  - **Self-check:** does your experiment settle a question multiple AI subfields argue about, with matched
    baselines and conditions?

### Declarative knowledge representation / logic programming (KR)

- **Brewka, Niemelä & Truszczyński, "Answer Set Optimization," IJCAI-03.**
  Verified: `ijcai.org/Proceedings/03/Papers/125.pdf` (IJCAI 2003 proceedings).
  - **Why it is an exemplar:** extends a core KR formalism (answer set programming) with a general
    optimization/preference layer — a compact formal contribution with reach across reasoning, planning, and
    configuration, exactly the broad-AI framing IJCAI rewards.
  - **Self-check:** is your formal contribution stated as a general mechanism a broad PC can evaluate, with
    semantics and properties, not just a system?

### Search / SAT for planning (planning & search)

- **Kautz & Selman, "Unifying SAT-based and Graph-based Planning," IJCAI-99.**
  Verified: `ijcai.org/Proceedings/99-1/Papers/047.pdf` (IJCAI 1999 proceedings).
  - **Why it is an exemplar:** unifies two previously separate planning paradigms (SAT encodings and planning
    graphs), turning an apparent rivalry into one framework — a "reframe the problem" contribution that
    travels beyond either technique.
  - **Self-check:** does your paper unify or reframe competing approaches, rather than add one more method to
    a crowded list?

### Deep reinforcement learning for control (reinforcement learning)

- **"Multi-Task Deep Reinforcement Learning for Continuous Action Control," IJCAI 2017.**
  Verified: `ijcai.org/proceedings/2017/461` (IJCAI 2017 proceedings page).
  - **Why it is an exemplar:** tackles continuous-control RL across multiple tasks at once, with the broad
    claim that one policy architecture transfers — significance stated beyond a single environment, which is
    what lifts an RL result above a benchmark report.
  - **Self-check:** does your RL contribution generalize across tasks/environments, with curves and repeated
    runs, not a single leaderboard number?

### Semi-supervised deep learning (machine learning)

- **"Tri-net for Semi-Supervised Deep Learning," IJCAI 2018.**
  Verified: `ijcai.org/proceedings/2018/0278.pdf` (IJCAI 2018 proceedings PDF).
  - **Why it is an exemplar:** a disagreement-based method that exploits unlabeled data with three networks —
    a clean core mechanism whose effect can be isolated by ablation, the experimental discipline
    `ijcai-experiments` asks for.
  - **Self-check:** can you ablate your core mechanism so reviewers see it, not your architecture choices,
    drives the gain?

### Field-defining survey (Survey Track / NLP)

- **Bevilacqua, Pasini, Raganato & Navigli, "Recent Trends in Word Sense Disambiguation: A Survey,"
  IJCAI 2021 (Survey Track).**
  Verified: `ijcai.org/proceedings/2021/593` (IJCAI 2021 proceedings page).
  - **Why it is an exemplar:** a model of the IJCAI **Survey Track** — a mature area, an expert team, and a
    structured synthesis of resources and methods that orients the whole subfield. Consider this shape only
    for established topics (`ijcai-topic-selection`: Survey Track for mature areas with established expertise).
  - **Self-check:** is your area mature enough, and your team established enough, that a survey *organizes*
    the field rather than just lists papers?

### Classical search, generalized (game-tree / heuristic search)

- **"Generalisation of Alpha-Beta Search for AND-OR Graphs With Partially Ordered Values," IJCAI 2022.**
  Verified: `ijcai.org/proceedings/2022/661` (IJCAI 2022 proceedings page).
  - **Why it is an exemplar:** takes a textbook algorithm (alpha-beta) and generalizes it to a broader
    structure (AND-OR graphs, partially ordered values) with formal guarantees — a compact, theory-backed
    contribution to a foundational AI technique.
  - **Self-check:** does your paper extend a foundational AI technique in a way stated formally and verified,
    not just engineered?

---

## By topic (each cell is a verified IJCAI paper above)

| Topic | Verified IJCAI exemplar | Year | Method | Proceedings path |
| --- | --- | --- | --- | --- |
| Symbolic vs. connectionist learning | Fisher & McKusick, "ID3 and Back-propagation" | 1989 | Controlled empirical comparison | `Proceedings/89-1/Papers/126.pdf` |
| Knowledge representation / preferences | Brewka, Niemelä & Truszczyński, "Answer Set Optimization" | 2003 | Logic programming / formal | `Proceedings/03/Papers/125.pdf` |
| Automated planning | Kautz & Selman, "Unifying SAT-based and Graph-based Planning" | 1999 | SAT + planning graphs | `Proceedings/99-1/Papers/047.pdf` |
| Reinforcement learning / control | "Multi-Task Deep RL for Continuous Action Control" | 2017 | Deep RL, multi-task | `proceedings/2017/461` |
| Semi-supervised learning | "Tri-net for Semi-Supervised Deep Learning" | 2018 | Disagreement-based deep nets | `proceedings/2018/0278.pdf` |
| NLP / word sense disambiguation | "Recent Trends in WSD: A Survey" | 2021 | Survey Track synthesis | `proceedings/2021/593` |
| Heuristic / game-tree search | "Generalisation of Alpha-Beta Search for AND-OR Graphs" | 2022 | Search algorithm + guarantees | `proceedings/2022/661` |

---

## Omitted for lack of IJCAI-proceedings verification (do not attribute to IJCAI without re-checking)

To keep the list zero-hallucination and sibling-confusion-free, the following well-known works were
**excluded** after checking — each is a real AI classic, but **not** in the IJCAI proceedings:

- **Ribeiro, Singh & Guestrin, "'Why Should I Trust You?': Explaining the Predictions of Any Classifier"** —
  verified to be in **KDD 2016** (ACM SIGKDD, pp. 1135–1144), **not IJCAI**. Listed only as a guardrail.
- **Kautz & Selman, "Planning as Satisfiability"** — the original is **ECAI-92** (pp. 359–363), **not
  IJCAI**. Their *later* "Unifying SAT-based and Graph-based Planning" **is** at IJCAI-99 and is included
  above; do not conflate the two.
- **Blum & Mitchell, "Combining Labeled and Unlabeled Data with Co-Training"** — verified to be in **COLT
  1998**, **not IJCAI**. Excluded.
- **Quinlan, "Learning Logical Definitions from Relations" (FOIL)** — published in the journal **Machine
  Learning** (1990, 5:239–266), **not the IJCAI proceedings**. Excluded.

Before adding any new paper to this library, confirm it on `ijcai.org/proceedings` (proceedings page or PDF
with a year), check it is IJCAI and not a sibling venue (AAAI / NeurIPS / ICML / ICLR / ACL / AAMAS / KR),
and update the access-date header. When in doubt, omit.
