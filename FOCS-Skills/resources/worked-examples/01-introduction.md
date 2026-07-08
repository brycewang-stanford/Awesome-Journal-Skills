> **Illustrative teaching example.** The paper, theorems, bounds, and authors
> below are **fictional**, invented solely to demonstrate how a FOCS opening is
> rebuilt for the ten-page attention window. No real results are stated and no
> venue policy is invented. Companion skills:
> [`focs-writing-style`](../../skills/focs-writing-style/SKILL.md),
> [`focs-supplementary`](../../skills/focs-supplementary/SKILL.md),
> [`focs-topic-selection`](../../skills/focs-topic-selection/SKILL.md).

# Worked Example: Rebuilding a FOCS Opening (before → after)

Setting: a fictional submission, *"Deterministic Expander Decomposition with
Certified Boundaries in Near-Linear Time."* The team's first draft opens the
way an arXiv/journal paper opens — patient, historical, definitions-first.
FOCS gives this paper a different contract: a committee member from another
corner of TCS will read the abstract, the references, and ten pages, and then
argue for or against it in a comparative discussion. The rebuild below shows
the same content re-sequenced for that reader.

---

## Before (journal-paced opening — fails the window)

> **Abstract.** Expander decompositions have become a fundamental tool in
> graph algorithms. In this paper we study the problem of computing expander
> decompositions deterministically. After reviewing the history of the
> problem, we present a new algorithm with improved guarantees, based on a
> novel potential-function analysis. We also discuss several applications.
>
> **1. Introduction.** Graph partitioning has a long history going back to
> the 1970s. [Half a page of history.] An expander decomposition of a graph
> partitions its vertices such that... [Formal definition, three displayed
> equations.] Such decompositions have found applications in Laplacian
> solvers, dynamic algorithms, and distributed computing. [Half a page of
> application citations.] Previous algorithms are either randomized or run in
> quadratic time. In Section 4 we describe our algorithm; its analysis
> appears in Sections 5–8; applications are given in Section 9.

**Why this fails at FOCS specifically:**

- **The theorem never appears.** "Improved guarantees" is not a statement; a
  breadth reviewer cannot champion — or even accurately doubt — a bound they
  have not seen. At page ten this reader must vote with confidence.
- **History before contribution.** The venue's reading order is inverted:
  FOCS readers grant you the problem's importance quickly (expander
  decompositions are community infrastructure) and want the delta.
- **No obstacle, no idea.** Nothing says why determinism was hard or what
  "novel potential-function analysis" actually does — the two things a PC
  discussion will spend its minutes on.
- **"Improved" is unquantified**, the exact hedge `focs-writing-style` bans
  from the guaranteed pages.
- **Applications deferred to Section 9**, likely past page ten — so for most
  of the committee, they do not exist.

---

## After (window-first opening)

> **Abstract.** We give the first deterministic algorithm that computes a
> $(\phi, \varepsilon)$-expander decomposition of an $m$-edge graph in time
> $O(m^{1+o(1)})$, matching the randomized state of the art up to the
> $m^{o(1)}$ factor. All previous deterministic algorithms required
> $\Omega(m^2)$ time or produced boundaries a $\log^3 n$ factor larger. Our
> algorithm additionally outputs a *certificate*: a witness verifiable in
> linear time that each part is a $\phi$-expander. The key idea is a
> derandomized boundary-charging scheme in which the random sampling of prior
> work is replaced by a pessimistic-estimator hierarchy that can be updated
> in amortized $m^{o(1)}$ time per refinement step. As consequences we
> derandomize two downstream results: [fictional consequence A] and
> [fictional consequence B].
>
> **1. Our result.** *(First half page — statement before history.)*
>
> **Theorem 1 (informal).** There is a deterministic algorithm that, given
> any graph $G$ with $m$ edges and $\phi \in (0,1)$, computes in
> $m^{1+o(1)}$ time a partition into $\phi$-expanders cutting at most
> $\phi m^{1+o(1)}$ edges, together with a linear-time-verifiable expansion
> certificate for each part.
>
> The formal statement, with the certificate defined precisely, is Theorem
> 3.1 (page 7); its proof spans Sections 5–7. *(Pointer discipline: window
> statement → body address, per `focs-supplementary`.)*
>
> **2. Why determinism was stuck.** *(The obstacle paragraph — the passage a
> PC discussion quotes.)* Every near-linear randomized construction since
> [fictional lineage] samples cut witnesses; the failure probability is then
> united over $\mathrm{poly}(n)$ refinement steps. Direct derandomization via
> conditional expectations must evaluate an estimator over all candidate
> cuts, which is exactly the $\Omega(m^2)$ bottleneck of [fictional prior].
> The open question was whether the estimator itself admits a data structure.
> We show it does: our hierarchy maintains pessimistic estimates for *all*
> cuts of the current part under edge deletions, in $m^{o(1)}$ amortized
> time — this data-structural reading of a probabilistic argument is the
> paper's transferable idea.
>
> **3. Consequences.** *(Still inside page two.)* Plugging Theorem 1 into
> the frameworks of [fictional X] and [fictional Y] removes the last source
> of randomness from both, giving deterministic [A] and [B]. Both
> derivations are short (Section 8) but were blocked precisely on
> deterministic decomposition.
>
> **4. Technical overview.** *(Pages 2–6: the real proof ideas, with honest
> statements of the two delicate lemmas and a paragraph on where the natural
> first attempt fails.)* ... **5. Formal statements.** *(Pages 7–9: every
> theorem and the certificate definition.)* **6. Organization.** *(Page 10:
> one paragraph mapping each statement to its proof section.)*

---

## What changed, mapped to the skills

| Move | Before | After | Skill rule |
|---|---|---|---|
| Headline bound | "improved guarantees" | exact time and cut quality in the abstract | Quantify hedges (`focs-writing-style`) |
| First theorem appears | never in the window | half a page in, informally; formally by p.7 | Every result stated by page ten |
| Obstacle | absent | named bottleneck of prior approach + why it was inherent | The obstacle paragraph |
| Idea | "novel potential-function analysis" | named, one-sentence mechanism (estimator hierarchy) | Name your techniques |
| Consequences | Section 9, past the window | Section 3, page two | Pages 11+ may prove, not announce (`focs-supplementary`) |
| Navigation | section list | statement → proof addresses | Pointer discipline |

The "after" is not shorter — it is *resequenced*: statement, obstacle, idea,
consequences, then depth. That order lets the ten-page reader do their actual
job: represent the paper accurately in a room where someone else is
championing a different one.

> Next: study the real award-verified openings referenced in
> [`../exemplars/library.md`](../exemplars/library.md), and confirm current
> policy in [`../official-source-map.md`](../official-source-map.md) before
> acting on any format detail here.
