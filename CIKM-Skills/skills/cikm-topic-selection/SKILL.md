---
name: cikm-topic-selection
description: Use when deciding whether a project fits CIKM, the tri-community ACM venue spanning information retrieval, data mining, and knowledge management/databases, when weighing CIKM against SIGIR, KDD, WSDM, TheWebConf, SIGMOD/VLDB, or ISWC, and when choosing among CIKM's five tracks before writing begins.
---

# CIKM Topic Selection

CIKM is the room where three communities meet: information retrieval, data mining, and
knowledge management with its database roots. Its sponsorship tells the story — ACM
SIGIR (since 1993) plus SIGWEB (since 2006) — and its 2026 self-description spans
information access, knowledge representation, data integration, and personalization
(source map, checked 2026-07-08). Fit questions here are therefore different from
single-community venues: the issue is rarely "is this in scope" and usually "is the
breadth an advantage for this particular paper."

## The tri-community fit question

Ask which communities the paper genuinely speaks to, then count:

- **Two or three lanes** — a retrieval model built on a knowledge graph, a mining
  method whose output feeds a search or QA system, an entity-resolution pipeline with
  both database and IR evaluation. This is the CIKM sweet spot: the blended reviewer
  pool is an asset, because no single-community venue gives all lanes credit.
- **Exactly one lane, done deeply** — pure ranking-model work, pure pattern-mining
  theory, pure query optimization. CIKM accepts such papers, but the specialist venue
  (SIGIR, KDD, SIGMOD/VLDB) usually offers sharper reviewers and more career signal.
  Choose CIKM deliberately, e.g., for the calendar, not by default.
- **Zero lanes** — contributions about model architecture, vision, or generic NLP with
  an incidental retrieval experiment. Reframe or reroute; scope-mismatch reads fast
  at a venue whose name states its scope.

## Honest calendar positioning

CIKM's May deadline and November meeting make it the information family's **fall
harvest**: work that missed or matured past SIGIR's January gate, KDD's February
cycle-2 gate, or that wants a decision before WSDM's August gate. Using CIKM as the
next stop after a sibling rejection is normal community practice — but only after the
prior reviews are actually absorbed. A resubmission with untouched weaknesses will
meet a reviewer pool that overlaps heavily with the one that wrote those reviews.

## Sibling contrast table

| Neighbor | Its center of gravity | Send the paper there instead when... |
|---|---|---|
| SIGIR | Retrieval and its evaluation culture | Ranking quality/IR evaluation is the entire contribution |
| KDD | Mining at scale; deployment evidence (ADS) | The story is data-regime scale or a production launch |
| WSDM | Web/social interaction data, small selective single track | The object of study is specifically web or social-web behavior |
| TheWebConf | The web as an artifact and ecosystem | Web standards, platforms, or web-scale measurement lead |
| SIGMOD/VLDB | Data systems internals | The contribution is storage, indexing internals, or query processing |
| ISWC / KR | Semantic-web formalisms; formal reasoning | Ontology languages or logic, not applied knowledge systems |

The reverse routes matter too: knowledge-graph construction and reasoning for
applications, heterogeneous-data integration, entity linking, and enterprise search —
work each specialist venue treats as adjacent — is core CIKM territory.

## Five-track fork (2026 lineup)

CIKM 2026 fields Full Research (≤10 pp incl. appendices), Short Research (≤4 pp),
Applied Research (≤7 pp, requires practical-application evidence such as a system
launch or data release), Resource (≤4 pp), and Demonstration (≤4 pp) tracks. Pick by
the strongest honest artifact: a rounded method study → Full; one crisp finding →
Short; a deployed system with launch evidence → Applied; a dataset/tool others will
adopt → Resource; something a person can touch at a booth → Demo. The concurrent
submission ban applies across venues, so the same contribution cannot hedge.

## Decision walk-through

A team built a temporal knowledge-graph completion model and wired it into an
enterprise document-search assistant. As pure KG-embedding work it competes at scale
venues against heavy theory; as pure search work the IR delta is modest. Framed as
one system — completion quality *and* its measured effect on retrieval answers — it
becomes a two-lane CIKM paper, with the deployment variant a plausible Applied
Research submission if launch metrics exist. That reframing decision is the routing
decision.

## Scope vocabulary sanity check

The venue's name is a scope test you can run on your own abstract. Underline every
noun phrase; a CIKM-shaped abstract naturally contains the venue's working
vocabulary — retrieval, ranking, mining, knowledge graph, entities, integration,
indexing, recommendation, query, corpus, metadata, provenance — because the paper is
*about* information and knowledge objects. If the underlined terms are instead
"architecture, layers, loss, benchmark, SOTA," the paper is currently written as a
model paper that happens to touch information data, and either the framing or the
venue should change. This check costs five minutes and predicts the most common
CIKM review complaint: "unclear what this offers the information-management
community specifically."

## Prestige and career honesty

Advisors and hiring committees read CIKM correctly as a large, credible,
first-tier-adjacent ACM venue — bigger-tent than SIGIR/KDD/WSDM, with more room for
boundary work and applied contributions, and with genuine landmark papers in its
back catalog (the exemplars library holds six, TAGME through BERT4Rec). Honest
implications:

- Choosing CIKM *first* is a positive strategy for boundary papers, resource
  papers, and applied systems — the audiences those papers need actually attend.
- Choosing CIKM *second*, after a specialist-venue rejection, is routine and
  carries no stigma — but the paper must be revised, not merely reformatted,
  because reviewer pools overlap.
- Choosing CIKM to *avoid* a specialist community's standards backfires: that
  community's reviewers are in the CIKM pool too, applying the same standards
  with less patience.

## Timing as a tiebreaker

When fit is genuinely even between CIKM and a specialist sibling, let the calendar
decide like a project manager: a result solid in March comfortably makes CIKM's
May gate; the same result would wait until KDD's next cycle or SIGIR's January.
Six months of shelf life is a real cost in fast-moving areas — LLM-adjacent
retrieval and KG work can be scooped in one arXiv season. Conversely, a result
that needs one more quarter of experiments should not be rushed into May; the
fall slot returns every year.

## Output format

```text
[Lane count] IR / mining / KM-DB lanes the contribution truly occupies
[CIKM verdict] sweet spot / acceptable-but-specialist-venue-stronger / out of scope
[Track] full / short / applied / resource / demo (with the honest-artifact reason)
[Alternative venue] <best single-community target and why it loses or wins>
[Framing action] <what to merge, split, or rename before writing>
```
