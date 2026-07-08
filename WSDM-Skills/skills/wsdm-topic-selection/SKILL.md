---
name: wsdm-topic-selection
description: Use when deciding whether a project belongs at WSDM or a neighbor - tests for the web/social-data core and the practical-yet-principled bar, scope coverage from web search and recommendation to social networks and responsible web AI, routing against SIGIR, KDD, WWW, CIKM, RecSys, and ICWSM, and long-versus-short-track fit.
---

# WSDM Topic Selection

Decide if a project is WSDM-shaped before anyone formats a page. WSDM
(pronounced "wisdom") is deliberately narrow: search and data mining **on the
Web and the Social Web**, run as a small, highly selective, traditionally
single-track winter meeting jointly sponsored by four ACM SIGs (SIGIR, SIGKDD,
SIGMOD, SIGWEB). The sponsorship list is the scope diagram - the venue lives at
the intersection of retrieval, mining, data management, and the web itself.

## The two-gate test

**Gate 1 - the data gate.** Is the primary object of study web or social-web
data: queries and clicks, documents and links, user-item interactions, social
graphs, ads, reviews, conversational sessions? A method paper whose experiments
merely *include* a web dataset fails this gate; the web data must be what the
contribution is *about*. Tabular-ML, vision, and generic NLP work fail here
regardless of quality.

**Gate 2 - the "practical yet principled" gate.** The series describes its
emphasis as practical yet principled approaches, and the PC enforces both
adjectives:

- *Practical*: plausible at platform scale, aware of serving cost, evaluated on
  realistic interaction data.
- *Principled*: a nameable mechanism, bias-aware evaluation, and an explanation
  of why it works - not a leaderboard delta.

Projects strong on one adjective route elsewhere: principled-only theory
toward theory-friendly venues, practical-only system reports toward industry
tracks or applied venues.

## Scope coverage check (2026 CFP areas)

The 2026 call organized scope roughly as: web search (including query
analysis, evaluation, user behavior and log analysis, and explicitly "Search
with Foundation Models"); web mining and content analysis (including
recommender systems, crawling/indexing); social networks (link prediction,
community detection, computational social science, influence, trust); fairness,
accountability, and explainability for ranking, recommendation, and ads; and
conversational search and assistants. If the project needs a paragraph of
throat-clearing to sound like one of these, note that as a fit warning.

## Routing table

| Signal in your project | Better first target | Why |
|---|---|---|
| Core IR theory, test-collection evaluation, no web-mining angle | SIGIR | Deeper IR-methods bench |
| General-purpose mining/ML method, web data incidental | KDD | Scope is data mining at large |
| Web systems, standards, platform measurement, web economics | TheWebConf (WWW) | Broader web-as-artifact scope |
| Solid applied IR/DB/mining result, breadth over selectivity | CIKM | Larger, broader program |
| Recommender-systems contribution with user-centric evaluation | RecSys | Dedicated community and review lens |
| Social-media phenomena, computational social science first | ICWSM | Social-science evaluation standards |
| Learning theory / new architecture, evaluation on static benchmarks | NeurIPS/ICML/ICLR | Method-first review culture |
| Web search/mining/rec with logs, bias-awareness, deployment realism | **WSDM** | This is the lane |

Tie-breakers when two venues survive: (1) whose recent proceedings contain the
papers you must cite - submit to the ongoing conversation; (2) whose review
process suits the work - WSDM's no-rebuttal, one-in-six regime punishes papers
that need explaining; (3) calendar position (`wsdm-workflow` maps the chain).

## Selectivity realism

Anchor numbers: WSDM 2025 accepted just over 100 of more than 600 submissions
(~16-17%). Single-track capacity keeps the program small by design. Honest
self-assessment questions before committing the August slot:

```text
1. Name the WSDM lineage this joins (see wsdm-related-work).       [____]
2. State the behavioral fact the paper exploits or corrects.       [____]
3. State the mechanism in one clause, no "framework" words.        [____]
4. Which quadrant of evidence is weakest (wsdm-experiments)?       [____]
5. Would the industry half of the PC call the setting realistic?   [____]
6. Is there a reason to *choose* this paper, not just no flaw?     [____]
```

Blank boxes at question 1-3 usually mean the project is a neighbor-venue paper
wearing WSDM formatting. A weak answer at 6 with strong answers elsewhere
suggests the short-paper track (since 2026) over the long track.

## Routing vignettes (fictional)

- *A contrastive-learning objective evaluated on MovieLens and two vision
  benchmarks.* Fails Gate 1 - web data is a test case, not the object. Route
  to the ML flagships; return to WSDM only if a version emerges whose claims
  are about interaction data specifically.
- *A measurement study of coordinated inauthentic amplification on a
  microblog platform, with a detection heuristic.* Passes Gate 1; Gate 2
  depends on the mechanism. If detection is principled and evaluated for
  ranking/mining impact, WSDM fits; if the contribution is the social
  phenomenon itself, ICWSM's review culture will value it higher.
- *An LLM-based relevance judge replacing crowd labels, validated against
  human judgments on public query sets.* Passes both gates via the
  evaluation lineage; equally at home at SIGIR - apply tie-breaker (1):
  wherever the papers it must cite appeared last two years.
- *A vector-database sharding scheme with a web-corpus benchmark.* The
  contribution is data management; the web corpus is incidental. VLDB-family
  first, WSDM only with a retrieval-behavior angle.

## Foundation-model-era fit

LLM work is in scope only through the web lens - the 2026 CFP names "Search
with Foundation Models" and the 2026 Industry Day theme was LLMs and agentic
AI in industrial settings. The test: does the contribution concern how
foundation models *interact with web-scale search, recommendation, or user
behavior* (retrieval-augmentation for search, LLM-based ranking or judgment,
agentic browsing, synthetic-content effects on ranking ecosystems)? A prompt
technique evaluated on static QA benchmarks fails Gate 1 regardless of the
word "search" in its title.

## Output format

```text
[Gate 1] web/social data is the object of study: pass / fail (reason)
[Gate 2] practical + principled both present: pass / weak adjective named
[Scope area] 2026-CFP area matched: <area or none>
[Routing] WSDM / <neighbor> with tie-breaker rationale
[Track] long / short / demo / cup / defer a year
[Confidence] choose-this-paper reason in one sentence
```
