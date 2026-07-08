# RSS Exemplars Library (topic × era)

> **Verified via web search, access date 2026-07-08.** Every paper below was confirmed
> against the **free online RSS proceedings** (`roboticsproceedings.org/rssNN/...`) —
> matching the volume page to the RSS edition, plus authors and, where surfaced, the
> `10.15607/RSS.*` DOI — and cross-checked against the dblp RSS index
> (https://dblp.org/db/conf/rss/index.html). Papers that could not be cleanly pinned to
> an RSS edition were left out. Five verified rows beat fifteen guessed ones.
>
> **Venue-misattribution guard:** robotics classics scatter across ICRA, IROS, IJRR,
> T-RO, CoRL, and even ML venues, and community memory routinely mislabels them. An
> arXiv page or a famous project website proves nothing about where a paper was
> published; only a roboticsproceedings.org volume page (or its dblp mirror) proves RSS.
> Four of the five rows below are RSS Test of Time Award recipients, which is itself a
> useful selection signal: the venue's own retrospective judgment of what an RSS paper
> should be.
>
> **Zero-hallucination rule:** this file gives design positioning only. Numbers, task
> success rates, and theorem statements are not reproduced here — read the original PDF
> (free, no login) before citing anything.

---

## How to use this library

Each exemplar shows one way to clear the RSS bar: a **scientific claim about robotics**
— an algorithmic property, an inference structure, a learned capability — backed by
evidence sized to that claim. Pick the row nearest your project, then answer its
self-check question honestly before calling the project "RSS-shaped" (see
[`../../skills/rss-topic-selection/SKILL.md`](../../skills/rss-topic-selection/SKILL.md)
and [`../../skills/rss-writing-style/SKILL.md`](../../skills/rss-writing-style/SKILL.md)).

---

## The verified rows

### Estimation / SLAM as linear algebra (RSS I, 2005)

- **Dellaert, "Square Root SAM," RSS 2005 (Cambridge, MA), RSS I.**
  Verified: `roboticsproceedings.org/rss01/p24.html`, DOI `10.15607/RSS.2005.I.024`;
  Test of Time recipient (2020, jointly with Kaess's follow-on smoothing work).
  - **Why it clears the bar:** reframes SLAM as sparse square-root information
    smoothing — the claim is about the *mathematical structure* of the mapping problem,
    and the robot experiments certify that the structure survives real sensor data.
  - **Self-check:** does your paper change how the community *formulates* a core
    robotics problem, or only tune an existing formulation?

### Planning under uncertainty (RSS IV, 2008)

- **Kurniawati, Hsu & Lee, "SARSOP: Efficient Point-Based POMDP Planning by
  Approximating Optimally Reachable Belief Spaces," RSS 2008 (Zurich), RSS IV.**
  Verified: `roboticsproceedings.org/rss04/p9.html`, DOI `10.15607/RSS.2008.IV.009`;
  Test of Time recipient.
  - **Why it clears the bar:** identifies the *optimally reachable* belief subspace as
    the thing worth sampling, turning POMDP planning from intractable to practical —
    an insight, then an algorithm, then evidence, in that order.
  - **Self-check:** can you state the single structural insight that makes your method
    work, in one sentence, without naming your implementation?

### Sampling-based motion planning with guarantees (RSS VI, 2010)

- **Karaman & Frazzoli, "Incremental Sampling-based Algorithms for Optimal Motion
  Planning," RSS 2010 (Zaragoza), RSS VI.**
  Verified: `roboticsproceedings.org/rss06/p34.html`; Test of Time recipient; the
  conference version of the RRT*/PRM* optimality line.
  - **Why it clears the bar:** proves that popular samplers converge to *non-optimal*
    solutions and then constructs variants with asymptotic-optimality guarantees — a
    theorem-first paper whose experiments illustrate rather than substitute for proof.
  - **Self-check:** if your claim is a property (optimality, completeness, stability),
    is it proved, or only observed on benchmark instances?

### Learning for physical interaction (RSS IX, 2013)

- **Lenz, Lee & Saxena, "Deep Learning for Detecting Robotic Grasps," RSS 2013
  (Berlin), RSS IX.**
  Verified: `roboticsproceedings.org/rss09/p12.html`; Test of Time recipient.
  - **Why it clears the bar:** an early demonstration that learned features beat
    hand-designed ones for grasp detection, with a cascaded design justified by a
    speed/accuracy argument and validated on physical grasping — learning in service
    of a robotics question, not a benchmark score.
  - **Self-check:** does the learned component answer a robotics question a fixed
    pipeline could not, and is that shown on hardware?

### Generative policies for manipulation (RSS XIX, 2023)

- **Chi, Feng, Du, Xu, Cousineau, Burchfiel & Song, "Diffusion Policy: Visuomotor
  Policy Learning via Action Diffusion," RSS 2023, RSS XIX.**
  Verified: `roboticsproceedings.org/rss19/p026.pdf`, DOI `10.15607/RSS.2023.XIX.026`.
  - **Why it clears the bar:** poses action generation as conditional denoising and
    argues *why* that representation suits multimodal manipulation data, then tests the
    argument across many tasks and both simulated and real robots — a modern model of
    breadth-of-evidence matching breadth-of-claim.
  - **Self-check:** does your evaluation span enough tasks and embodiments to license
    the generality your abstract claims?

---

## Topic × era grid

| Lane | Exemplar | Edition / locator | What travels |
| --- | --- | --- | --- |
| Estimation & SLAM | Dellaert, "Square Root SAM" | 2005 / rss01 p24 | Problem reformulation |
| Decision-making under uncertainty | Kurniawati, Hsu & Lee, "SARSOP" | 2008 / rss04 p9 | Structural insight → algorithm |
| Motion planning theory | Karaman & Frazzoli, optimal sampling-based planning | 2010 / rss06 p34 | Negative result + guaranteed fix |
| Learning + manipulation | Lenz, Lee & Saxena, grasp detection | 2013 / rss09 p12 | Learning answering a robotics question |
| Policy learning | Chi et al., "Diffusion Policy" | 2023 / rss19 p026 | Representation argument + broad evidence |

> The 2005-2023 spread is deliberate: it shows the RSS bar is stable even as topics
> rotate — every row leads with a claim about robotics science and sizes its evidence
> to that claim.

---

## Adding a row (verification recipe)

1. Locate the paper's volume page on `roboticsproceedings.org` (volume numbers are
   Roman: RSS I = 2005 ... RSS XXI = 2025) and match title + full author list.
2. Record the `10.15607/RSS.*` DOI when the page exposes one.
3. Cross-check the edition, year, and host city on the dblp RSS index.
4. Reject candidates verified only via arXiv, project pages, citation managers, or
   memory — that is exactly how ICRA/IROS/CoRL papers get misfiled as RSS.
5. If verification tooling is unavailable, add the row marked **待核实** with no
   attribution, and update the access-date header when it is resolved.
