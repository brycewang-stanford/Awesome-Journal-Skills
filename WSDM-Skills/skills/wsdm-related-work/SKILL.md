---
name: wsdm-related-work
description: Use when positioning a paper against prior literature for WSDM - locating the work inside WSDM's own research lineages (click models, unbiased LTR, sequential recommendation, community detection), contrasting against SIGIR/KDD/WWW/CIKM/RecSys neighbors, venue-misattribution traps, and compressing the section for the tight page budget.
---

# WSDM Related Work

Position a submission against the literature the WSDM PC actually knows. At a
small single-track venue, related-work errors are unusually visible: the person
who wrote the paper you mis-cited may be your SPC. The section's job in a
9-page-inclusive budget is *positioning* - establishing which conversation the
paper joins and what precisely it adds - not coverage.

## Join a lineage, don't float free

WSDM has multi-edition research lineages, and reviewers instinctively slot new
work into them. Naming your lineage does the slotting for them (all rows
verified against ACM DL/dblp; see `../../resources/exemplars/library.md`):

| Lineage | Anchor papers at WSDM | If your paper is here, position against |
|---|---|---|
| Click models / position bias | Craswell et al. 2008 (cascade model) | Subsequent click-model and propensity work |
| Unbiased learning-to-rank | Joachims et al. 2017 | The ULTR line it started, incl. recent WSDM/SIGIR follow-ups |
| Sequential recommendation | Tang & Wang 2018 (Caser) | The CNN/attention sequential-rec succession |
| RL / bandits for recommendation | Chen et al. 2019 (Top-K off-policy, YouTube) | Off-policy and bandit rec work since |
| Community detection / graph mining | Yang & Leskovec 2013 (BigCLAM) | Scalable overlapping-community successors |

If no WSDM lineage fits, that is routing information, not a citation problem -
run `wsdm-topic-selection` before writing further.

## The contrast sentence

For each of the three to five closest works, write one sentence with this
anatomy: *their mechanism, their setting, the delta, why the delta matters
here*. Citation-listing ("[3,7,12] studied recommendation") communicates
nothing and spends budget.

```text
Template:
  <Closest work> <does X by mechanism M> <in setting S>; we differ by <Δ>,
  which matters because <consequence in our data regime>.

Instance (fictional):
  CDR-Net transfers cross-domain preferences via shared user embeddings,
  assuming overlapping user sets; we require no user overlap, which is the
  common case for the partner-site logs we target.
```

Reviewers at this venue read contrast sentences as competence signals: they
show you know the mechanism, not just the title.

## Sibling-venue positioning

WSDM's neighborhood is dense - SIGIR, KDD, TheWebConf (WWW), CIKM, RecSys, and
ICWSM publish adjacent work continuously. Rules:

- **Cite by contribution, not by venue prestige.** Missing the directly
  relevant RecSys paper because you only searched WSDM+SIGIR is a standard
  negative-review trigger.
- **Recency bar:** at minimum, sweep the last two editions of WSDM, SIGIR, KDD,
  WWW, and CIKM for your exact topic before claiming novelty; the overlap
  between these communities makes "we are the first" claims fragile.
- **Concurrent work:** if a recent preprint does something similar, cite and
  contrast it calmly; at a no-rebuttal venue you cannot later explain that you
  "were unaware" - the paper must already handle it.

## Misattribution traps

Famous papers cluster in this neighborhood, and attributing them to the wrong
venue damages credibility with reviewers who know exactly where they appeared.
Verified placements to guard against common mix-ups:

- **DeepWalk, node2vec, XGBoost** - KDD papers, not WSDM.
- **BERT4Rec** - CIKM 2019, not WSDM/SIGIR.
- **Neural Graph Collaborative Filtering (NGCF)** - SIGIR 2019.
- **"WTF: The Who to Follow Service at Twitter"** - WWW 2013.
- **SASRec** - ICDM 2018.
- Conversely, the five lineage anchors in the table above *are* WSDM papers -
  citing Craswell et al.'s cascade model or Caser to another venue is the same
  error mirrored.

When in doubt, resolve the venue on dblp before the citation enters the draft;
never trust memory or a secondhand BibTeX file for venue fields.

## Worked positioning paragraph (fictional)

A dwell-time debiasing paper joining the unbiased-LTR lineage might position
itself in four sentences - lineage entry, two contrasts, one boundary:

```text
Learning from logged interactions without inheriting their biases is a
long-standing WSDM concern, from cascade-style click models [Craswell et
al., 2008] to counterfactual learning-to-rank [Joachims et al., 2017].
Propensity-based ULTR corrects exposure bias but treats post-click signals
as unbiased; we show dwell time carries its own salience confound and
extend the counterfactual framework to post-click behavior. Session-aware
rerankers <fictional cites> model dwell directly but require editorial
labels for calibration; our estimator calibrates from abandonment
behavior alone. Unlike both lines, we assume no access to the production
propensity model, matching the partner-platform setting of Section 5.
```

Note what the paragraph never does: survey the field, praise prior work
emptily, or cite anything it does not contrast. Each sentence moves the
paper's coordinates.

## Compression for the budget

Target half a page to three-quarters. Structure that survives compression:

1. Two or three lineage paragraphs (one per relevant lineage), each ending in
   a contrast sentence for the closest works.
2. One paragraph for adjacent-venue and concurrent work.
3. Zero survey paragraphs. History lessons ("early work in information
   retrieval...") belong in theses.

Where the intro already contrasts the closest work (it should - see
`wsdm-writing-style`), the related-work section elaborates rather than
repeats: same contrast, mechanism-level detail.

## Output format

```text
[Lineage] WSDM lineage(s) joined: <named or "none - route check">
[Contrast sentences] closest 3-5 works each have mechanism-level contrast: yes / gaps
[Neighbor sweep] WSDM/SIGIR/KDD/WWW/CIKM last-2-editions checked: date + hits
[Misattribution scan] venue fields dblp-verified: yes / fixes made
[Budget] section length vs target: pass / compress list
```
