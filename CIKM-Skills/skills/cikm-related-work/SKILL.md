---
name: cikm-related-work
description: Use when positioning a CIKM submission against three literatures at once — retrieval, mining, and knowledge management/databases — building the boundary-work paragraph, guarding against misattributing SIGIR/KDD/ICDM classics to CIKM, and handling preprints under the arXiv-declaration and dual-submission rules.
---

# CIKM Related Work

Related work at CIKM is a three-front obligation. A submission claiming the
IR-mining-KM boundary must show command of each literature it borrows from, plus the
smaller literature that lives *on* the boundary — much of which is CIKM's own back
catalog. A section citing only one lane tells two-thirds of the reviewer pool that
their field's relevant results may be unknown to the authors.

## Three-front coverage plan

| Front | Lineage to command | What its reviewer checks |
|---|---|---|
| Retrieval | Ranking models, neural matching (DRMM-line), evaluation practice | Is the nearest ranking method compared or distinguished? |
| Mining | Representation learning (GraRep-line), graph/sequence models, scale methods | Is the mechanism's delta over the nearest mining method stated? |
| KM / databases | Entity linking (TAGME-line), integration, KG construction and quality | Is the data-management cost and lineage acknowledged? |

The verified exemplars in `../../resources/exemplars/library.md` mark where these
lineages pass through CIKM itself; citing the venue's own milestones — DSSM for
click-supervised semantic matching, RippleNet/BERT4Rec for KG- and
transformer-based recommendation — signals to the panel that the authors know whose
house they are submitting to.

## The boundary-work paragraph

After the three lane surveys, CIKM related-work sections need one paragraph the
single-lane venues do not: the works that already tried to combine the same lanes.
Structure it as three sentences — *who combined what* ("X fused KG signals into
ranking..."), *what they could not do* ("...but only for static graphs at
million-triple scale"), *what this paper changes at the seam* ("we make the fusion
incremental, which is what deployment requires"). Reviewers use exactly this
paragraph to locate the contribution; write it so it can be quoted in a meta-review.

## Misattribution guard

CIKM sits so close to its siblings that venue misattribution is a live review risk —
and a credibility hit when a reviewer authored the misplaced paper. Checked traps
(dblp-verified, 2026-07-08):

- **DeepWalk, node2vec, metapath2vec → KDD**, not CIKM; CIKM's graph-embedding
  milestone is **GraRep (CIKM 2015)**.
- **SASRec → ICDM 2018**; the transformer-recommender at CIKM is **BERT4Rec
  (CIKM 2019)**.
- **NGCF and LightGCN → SIGIR** (2019/2020); CIKM's KG-recommendation landmark is
  **RippleNet (CIKM 2018)**.
- **Conv-KNRM → WSDM 2018**, while **DRMM → CIKM 2016**; the neural-IR lineage
  hops venues paper by paper.
- **TransE → NeurIPS 2013** — KG-embedding origins are not CIKM even though KG
  applications are core CIKM territory.

Rule: before writing "(CIKM 20xx)", confirm on dblp's `conf/cikm` index; before
writing "prior CIKM work has not...", search the last three CIKM proceedings in the
ACM DL — with many hundreds of papers per recent edition, the prior work usually
exists.

## Recency expectations by front

The three fronts age at different speeds, and reviewers calibrate accordingly. A
workable recency floor when drafting:

| Front | Staleness signal reviewers flag | Floor |
|---|---|---|
| Neural retrieval / RAG-adjacent | No baseline or citation from the last ~18 months | Current-year and previous-year venue papers present |
| Graph/sequence mining | Comparing only against pre-transformer-era methods | At least one recent strong method compared, not just cited |
| KM / KG construction | Ignoring the current ecosystem (modern KG tooling, LLM-assisted curation) | Ecosystem named, position stated |
| Foundations | — | Foundational citations never go stale; DSSM-era work still anchors lineages |

Recency is about baselines even more than bibliography: citing a recent method
while comparing only against old ones is the version of staleness that costs
scores (`cikm-experiments` owns that half of the problem).

## Citation hygiene mechanics

- Cite the **published venue version** once it exists — the CIKM/SIGIR/KDD record,
  not the arXiv preprint the PDF happened to be downloaded from. dblp resolves
  this in seconds and the ACM reference format carries the DOI.
- Keep bibliography entries consistent in format; a references section mixing
  five citation styles reads as assembled-by-paste, and at CIKM the references
  are uncounted — there is no budget excuse for truncated entries.
- When a line of work spans venues (the neural-matching lineage deliberately
  does), cite the actual hops rather than attributing the whole line to one
  venue — the misattribution guard above exists because reviewers notice.

## Preprints, concurrency, and the declaration rule

CIKM 2026 bans concurrent submission outright and requires declaring any public
non-anonymized version on the EasyChair form (`cikm-submission`). In the related-work
text itself: cite your own preprint in third person like a stranger's work; cite
independent concurrent arXiv work neutrally with a technical contrast and no
priority argument; and never let a citation resolve the authors' identity (e.g., a
footnoted repository URL owned by an author).

## Auditing the novelty sentence

The contribution statement should survive this adversarial read: for each clause,
name the closest prior work that could claim the same clause, and state the
surviving difference in mechanism terms, not adjective terms.

> Draft: "We are the first to use knowledge graphs for enterprise search."

Audit: KG-for-search has a decade of work (the RippleNet-line alone applies KG
propagation to ranking-adjacent tasks); "first" fails on contact. Repaired: "Prior
KG-augmented retrieval assumes a static graph resolved at index time; we resolve
links at query time against a continuously edited graph, which no prior system in
this line supports." The repaired sentence names the lineage, concedes its
existence, and stakes a mechanism-level difference a reviewer can verify rather
than a primacy claim they can falsify with one citation — the only kind of novelty
sentence that is safe in front of a pool this broad.

## Output format

```text
[Front coverage] retrieval / mining / KM-DB — each surveyed with nearest work named
[Boundary paragraph] <who-combined-what → gap → this paper's seam move>
[CIKM back-catalog] <own-venue milestones cited where they exist>
[Misattribution scan] <every "(CIKM 20xx)" dblp-checked; sibling classics placed right>
[Declaration state] <own preprints third-person, form declaration consistent>
```
