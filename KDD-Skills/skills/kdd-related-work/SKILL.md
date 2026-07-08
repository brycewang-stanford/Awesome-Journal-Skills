---
name: kdd-related-work
description: Use when positioning a KDD submission against the data-mining lineage (prior KDD volumes, ICDM, SDM, WSDM, CIKM, WWW) and the ML flagships, handling venue misattribution traps, cross-cycle resubmission overlap, concurrent arXiv work, and the mechanism-contrast style of novelty argument that ACM SIGKDD reviewers expect.
---

# KDD Related Work

Use this to audit positioning before the writing freeze. KDD sits inside a dense
family of venues that share topics but not registers, and its reviewers know the
mining lineage personally — misplacing a classic paper's venue or missing the direct
KDD predecessor of your own method are both instantly visible errors here.

## The lineage obligation

A KDD submission is expected to know its own conference's history on the topic.
Before writing, build the ancestry chain: which prior KDD papers created the
problem's vocabulary, and what does this paper change structurally? The
DeepWalk (KDD 2014) → node2vec (KDD 2016) → metapath2vec (KDD 2017) chain in
`resources/exemplars/library.md` is the canonical shape — each successor names the
structural property of the data its predecessor mishandled. A related-work section
that surveys families ("embedding methods can be divided into...") instead of stating
deltas is journal register, not KDD register.

## Venue map for positioning

| Literature lane | Venues | What KDD reviewers check |
|---|---|---|
| Own lineage | Prior KDD volumes (ACM DL) | Is the nearest KDD ancestor cited and contrasted mechanically? |
| Mining siblings | ICDM, SDM, PKDD/ECML, CIKM | Are same-shaped methods here distinguished, not ignored? |
| Web/search/rec | WWW, WSDM, SIGIR, RecSys | For graph/behavior/recsys papers: the applied twin literature |
| ML flagships | NeurIPS, ICML, ICLR | Is a general-ML method quietly identical to yours? |
| Systems/DB | VLDB, SIGMOD | For scalability claims: does a database solution already exist? |
| Applied domain | Domain journals, industry reports | For ADS: is the deployment problem's own literature acknowledged? |

## Misattribution traps

Getting a citation's venue wrong is disproportionately damaging at KDD because
reviewers wrote or reviewed the misplaced papers. Verified traps (see the exemplars
library for DOIs): Isolation Forest is **ICDM**, not KDD; LightGBM is **NeurIPS**,
not KDD despite shadowing XGBoost everywhere; Wide & Deep is a **RecSys workshop**
paper. Check every "seminal KDD paper" claim against the ACM DL record before it
ships.

## Novelty sentence pattern

The strongest KDD positioning names its neighbors and the mechanism-level difference
in one breath:

```text
Template:
  Unlike <nearest KDD ancestor>, which <mechanism> and therefore <failure in
  our regime>, and unlike <ML-flagship neighbor>, which <mechanism> but
  <cost/assumption>, our method <new mechanism>, which is what enables
  <the regime-specific capability the paper demonstrates>.

Instantiated:
  Unlike fixed-decay sketches (KDD'xx), whose single decay rate forces a
  forgetting-vs-staleness trade under drift, and unlike window-retrained
  detectors (ICML'yy) whose state grows with window length, StreamHive
  selects decay rates online, which is what allows bounded memory and
  drift tracking simultaneously.
```

If the sentence cannot be instantiated, the gap is a research problem, not a writing
problem — surface it before the deadline, not in rebuttal.

## Overlap declarations specific to KDD

- **Cross-cycle resubmission** is a formal mechanism, not an overlap problem: declare
  the previous OpenReview forum id and prepend the change summary
  (`kdd-supplementary`). Silently resubmitting a prior cycle's rejected paper as
  "new" risks the AC discovering the old forum anyway.
- **Research vs ADS**: the same underlying system may legitimately produce a methods
  paper and a deployment paper over time, but the *same paper* may not go to both
  tracks in one cycle, and substantial text overlap between two live submissions is a
  dual-submission problem.
- **arXiv and workshop versions**: follow the current CFP's anonymity and
  prior-publication wording (待核实 per cycle); cite concurrent arXiv work neutrally,
  state the technical difference, and avoid priority claims reviewers cannot check.
- Ethics of citation at this venue includes baseline fairness: if you cite a method
  you also benchmark against, the tuning symmetry disclosure in
  `kdd-reproducibility` is part of honest positioning.

## Vignette: positioning an LLM-era mining paper

A 2026-cycle submission uses an LLM to label graph nodes for semi-supervised fraud
detection. Its positioning problem is triangular: the graph-mining lane (prior KDD
fraud and GNN work) will ask what changed structurally; the LLM lane (recent ML
flagship work on LLM annotation) will ask why this is not just prompt engineering;
and the practitioner lane will ask about labeling cost at scale. The section that
works allocates a paragraph per lane and ends each with a delta sentence:

- vs. KDD fraud lineage: same task, but label scarcity is attacked at the labeling
  step rather than the propagation step — cite the nearest KDD ancestor and say what
  it could not do at 0.1% labels.
- vs. LLM-annotation work: those pipelines assume i.i.d. text; the contribution here
  is consistency-checking LLM labels against graph structure — a mechanism, not a
  prompt.
- vs. practice: per-node labeling cost quantified against human annotation budgets,
  which is the sentence the industry reviewer needs.

Triangulated positioning like this also pre-writes the rebuttal: each reviewer lens
already has its paragraph (`kdd-author-response`).

## Pre-freeze audit

1. Nearest KDD ancestor identified, cited, and mechanically contrasted.
2. Every benchmarked baseline is also positioned in prose (benchmarking without
   discussion reads as strawmanning).
3. All venue attributions of "classic" papers spot-checked against ACM DL/DBLP.
4. Two-lane coverage: at least the mining lane and one adjacent lane (ML, systems, or
   domain) are represented, matching where the claims live.
5. Overlap declarations drafted: resubmission id, arXiv status, sibling submissions.

## Output format

```text
[Positioning] delta-stated / survey-style (rewrite) / lineage-missing
[Nearest ancestors] <KDD predecessor>, <ML neighbor>, <systems neighbor>
[Novelty sentence] <instantiated template or BLOCKED: gap unclear>
[Misattribution check] <papers verified against ACM DL / findings>
[Overlap declarations] <resubmission forum id / arXiv / sibling tracks>
```
