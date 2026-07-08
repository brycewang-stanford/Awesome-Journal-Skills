---
name: webconf-topic-selection
description: Use when deciding whether a project belongs at the Web Conference (WWW) at all, which of the ten research tracks should review it, whether the short-paper or Web4Good lane fits better, and when the work should instead route to WSDM, SIGIR, CIKM, KDD, ICWSM, WebSci, or an ML flagship.
---

# Web Conference Topic Selection

Two decisions, in order: **is the work web-native**, and **which track's reviewer
pool should judge it**. Both are made by the authors, both are effectively
irreversible at the deadline, and the second is as consequential as the first
because the venue reviews inside tracks.

## Decision 1: the web-nativeness test

Ask: *if the Web's specific structure disappeared, would this contribution still
make sense?* Web-native work depends on at least one of: open hypertext and link
structure; platform mechanics and incentives; live, adversarial, user-generated
content; web-scale heterogeneity; or the socio-technical coupling of users and
algorithms. A generic model that merely *evaluates* on a web dataset fails the
test — the dataset is swappable, so an ML venue's pool serves it better.

```text
Web-native?                                  -> route
  Contribution needs link/platform/user      -> Web Conference candidate; go to
  structure to exist                            Decision 2
  Contribution is a general method; web      -> NeurIPS/ICML/ICLR or KDD, cite
  data is one evaluation among many             web results as evidence
  Contribution is about people/society,      -> ICWSM or WebSci if measurement/
  computation is instrumental                   interdisciplinarity dominates
  Contribution is retrieval effectiveness    -> SIGIR first; Web Conference if the
  per se                                        open-web setting changes the problem
  Contribution is mining methodology with    -> WSDM (methods-first) or KDD
  modest web specificity                        (mining/deployment-first)
  Contribution is a deployed web system's   -> Web Conference Industry track, not
  practice lessons                              the research tracks
```

## Decision 2: track fit (2026 lineup)

The 2026 research tracks, with the question each pool is primed to ask:

| Track (2026) | The pool's primary question |
|---|---|
| Economics, online markets and human computation | Are incentives/welfare modeled, not just predicted? |
| Graph algorithms and modeling for the Web | Does the graph method respect web-graph properties? |
| Responsible Web | Are harms, fairness, or governance the *contribution*? |
| Search and retrieval-augmented AI | What beats strong current retrieval/RAG baselines? |
| Security and privacy | Is there a real threat model and adversary? |
| Semantics and knowledge | Does it advance KGs/ontologies/structured data on the web? |
| Social networks and social media | Is the social measurement or model construct-valid? |
| Systems and infrastructure (Web, mobile, WoT) | Does it hold under realistic load/deployment? |
| User modeling, personalization and recommendation | Is the personalization gain real and leak-free? |
| Web mining and content analysis | Is the extracted signal novel and robust at scale? |

Tie-breaks: pick the track whose *evidence you actually have*, not whose name
flatters the abstract. A RAG-for-recommendation paper with strong offline ranking
tables but no retrieval-baseline sweep survives better in "User modeling ..." than
in "Search and retrieval-augmented AI." Track names are re-cut most editions —
confirm the current list before deciding, and remember the cap: at most 7
submissions per author across all research tracks in 2026.

## Lane selection inside the venue

- **Full research paper** (8+refs+appendix ≤ 12 pages): a complete evidence
  program. The default.
- **Short paper** (4 pages incl. references in 2026; main proceedings): one sharp
  idea with focused evidence; the later deadline (+6 weeks in 2026) is a schedule
  fact, not a quality discount.
- **Web4Good** (2026 special track; main proceedings): work whose center is
  measurable societal benefit; do not spin ordinary work into it.
- **Industry track**: deployment truth over methodological novelty; different
  platform (OpenReview in 2026) and reviewer expectations.
- **Workshops** (companion proceedings): early-stage or community-building work.

## The two chronic misroutes

1. **The dressed-up ML paper**: a general architecture with WWW formatting and one
   web dataset. Track panels detect it with the swappability question, and the
   review that follows ("better suited to a specialized venue") wastes a year.
   Route it to the ML flagship and cite the web experiment as evidence there.
2. **The homeless interdisciplinary paper**: strong social-science finding, thin
   computational novelty, submitted to a methods-leaning track. It needed
   "Social networks and social media" (measurement-tolerant) or ICWSM. The fix is
   pool choice, not more models.

## Boundary cases of the current era

- **LLM/RAG papers.** The venue added "Search and retrieval-augmented AI" as a
  2026 track, so LLM work is welcome — *when the Web is load-bearing*: retrieval
  over live/adversarial corpora, LLM-generated content polluting web ecosystems,
  agents navigating real sites. An LLM fine-tuning method evaluated on static QA
  benchmarks remains an ML-venue paper wearing a web costume.
- **Dataset and benchmark contributions.** The 2026 lineup had no dedicated
  resource track (unlike some earlier editions and unlike KDD's separate
  datasets-and-benchmarks track); a dataset paper competes inside a topical track
  on the strength of its measurement or enabling analysis. Check the current
  edition's calls before assuming either way.
- **Web3/blockchain, WoT, and mobile.** In 2026 these lived inside "Systems and
  infrastructure for Web, mobile, and WoT" and the economics track rather than as
  standalone tracks — evidence expectations follow the host track, not the
  subfield's own conferences.
- **Ethics-centered work.** If harms analysis is the contribution, "Responsible
  Web" is the pool primed for it; if harms are one section of a methods paper,
  stay in the methods track and let the ethics paragraph do its job.

## Commitment checklist

- [ ] One-sentence web-native mechanism written (it becomes page 1 —
      `webconf-writing-style`).
- [ ] Track chosen by evidence held; second-choice track named in case the lineup
      changes at the portal.
- [ ] Lane chosen (full/short/Web4Good/industry/workshop) with the calendar
      (`webconf-workflow`) in view.
- [ ] Per-author submission counts across the team checked against the cap.
- [ ] The nearest sibling-venue alternative named, so the team knows its plan B.

## Output format

```text
[Web-native] yes: <mechanism> / no: <reroute target>
[Track] <primary> (evidence basis); fallback <secondary>
[Lane] full / short / Web4Good / industry / workshop
[Misroute risks] <dressed-up ML / homeless interdisciplinary / track mismatch>
[Plan B] <sibling venue + what reframing it would need>
```
