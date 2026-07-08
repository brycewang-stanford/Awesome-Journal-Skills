---
name: emnlp-related-work
description: Use when positioning an EMNLP submission inside NLP's fast-moving literature — covering ACL Anthology lineages and arXiv concurrency, citing Findings and workshop papers correctly, tracing dataset and benchmark ancestry, verifying every reference resolves under the hallucinated-citation policy, and keeping self-citation double-blind.
---

# EMNLP Related Work

Use this to audit positioning and citation hygiene. NLP's literature moves faster than
any reviewing cycle: between your ARR submission and the meta-review, the arXiv
neighborhood of your paper will visibly change. EMNLP reviewers know this and calibrate
— what they do not forgive is missing the lineage that existed *before* you submitted,
or citing papers that do not exist.

## The lineage obligations

An EMNLP related-work section owes coverage on distinct axes:

| Axis | The reviewer's question | Where to check |
|---|---|---|
| Task lineage | Who defined and reshaped this task? | ACL Anthology back through renamings |
| Dataset ancestry | What data does your benchmark descend from or contain? | Dataset papers + their own provenance sections |
| Method neighbors | Which current approaches would contest your comparison table? | Last 2-3 years of ACL-family venues + arXiv |
| Evaluation critique | Has this metric or protocol been critiqued? | The methodology literature this venue itself publishes |
| Adjacent fields | Does IR / speech / ML own part of this idea? | Cross-community search before claiming firsts |

Dataset ancestry is the EMNLP-specific trap: benchmarks are frequently derived,
filtered, or re-annotated versions of earlier corpora, and claiming novelty over a
dataset whose ancestor solved the same problem is a reviewer catch that costs
credibility beyond the one paragraph.

## Anthology-status literacy

Citations at an ACL-family venue signal whether you know how your own field publishes:

- **Findings papers are real publications** — cite them as "Findings of the Association
  for Computational Linguistics: EMNLP 20XX," not as the main proceedings and not as
  preprints.
- **Workshop papers are archival in the Anthology** but represent a different review
  bar; leaning a central comparison on one deserves a sentence of context.
- **Prefer the Anthology version over arXiv** whenever both exist — citing arXiv for a
  paper with a published version suggests reference lists assembled by search engine.
- **TACL and Computational Linguistics** are journals inside the same ecosystem; their
  results are not "concurrent work" excuses, they are prior art.

## Concurrency etiquette

For genuinely simultaneous arXiv work: cite it, mark it as concurrent, and state the
technical difference in one neutral sentence — no priority litigation reviewers cannot
adjudicate. ACL policy abolished the anonymity embargo, so your *own* preprint may be
public; handle it in the third person like any other paper and do not cite it in a way
that completes the identity loop ("we extend Xu et al." where Xu is you, plus a
matching acknowledgements slip, is the classic double-blind failure).

## The hallucination gate

The 2026 EMNLP call names hallucinated citations as a sanctionable integrity problem —
a direct response to LLM-assisted writing. If any tool touched your bibliography,
verify mechanically:

```bash
# Every entry must resolve to a real, checkable identifier
grep -Eo 'doi\.org/[^ ,}]+|aclanthology\.org/[^ ,}]+|arxiv\.org/abs/[0-9.]+' refs.bib \
  | sort -u > ids.txt   # then spot-resolve each; zero tolerance for near-miss titles
# Red flags: plausible title + plausible authors + no findable venue = fabrication
```

Author-year pairs that "sound right," merged titles of two real papers, and wrong-venue
attributions are the common fabrication shapes. One hallucinated reference now risks
the whole submission, not a bibliography correction.

## Positioning prose that works here

The strong EMNLP positioning move is *evaluative contrast*, not adjacency listing:
state what the nearest work measured, what it could not see with that measurement, and
which experiment in your paper closes the gap. Three sentences of that beat two
paragraphs of "X did A. Y did B. Z did C." — and it survives the reviewer who knows X,
Y, and Z personally. Reserve explicit tables-of-differences for when reviewers of a
previous cycle demanded one; otherwise the contrast belongs woven into the experiment
motivation.

## Prior versions of your own work

ARR's continuity makes self-lineage a form field, not just a citation question:

- A resubmission across cycles declares itself, and the revision note is effectively
  related-work prose about your own previous version — write it with the same
  precision you demand of external comparisons.
- A published workshop version of the same idea must be cited and differentiated like
  anyone else's paper, in the third person, with the delta stated; the overlap
  question on the form exists to be answered honestly.
- An earlier paper from your group that shares infrastructure (the same corpus, the
  same codebase) is a disclosure judgment call: cite it neutrally if published, and
  avoid constructions that only make sense if the reader knows the two papers share
  authors.
- Never split one contribution across two concurrent ARR submissions and cite them at
  each other — reviewers drawn from the same pool see both, and the 2026 integrity
  language about thin slicing is aimed at exactly this shape.

## Freshness without churn-chasing

Cover everything Anthology-published in your niche through the submission cycle; treat
the newest arXiv layer with judgment — cite what genuinely shapes your claims, skip the
weekly leaderboard shuffle. A response-phase reviewer pointing at a paper newer than
your submission is asking about robustness of your conclusions, not accusing you of
omission; answer that question, not an imagined one.

## Two vocabularies, one section

Empirical NLP sits between linguistics and machine learning, and reviewers arrive from
both directions. A related-work section that cites only the ML lineage of a phenomenon
("hallucination," "faithfulness") while ignoring decades of linguistic work on the
underlying construct (presupposition, veridicality, entailment) will draw the one
reviewer who knows the older literature — and that review writes itself. The inverse
failure exists too. One paragraph acknowledging the other community's framing, with
two accurate citations, is cheap insurance and often genuinely improves the paper's
construct definitions.

## Output format

```text
[Axis coverage] <task / dataset / method / evaluation / adjacent — gaps per axis>
[Anthology hygiene] <Findings-vs-main errors, arXiv-vs-published swaps>
[Concurrency handling] <concurrent items + one-line distinctions>
[Citation verification] <resolved N/N; unresolvable entries listed>
[Positioning sentence] <the evaluative contrast, drafted>
```
