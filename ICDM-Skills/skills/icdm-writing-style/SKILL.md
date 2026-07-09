---
name: icdm-writing-style
description: Use when drafting or revising prose for an ICDM (IEEE International Conference on Data Mining) paper - the data-regime-first register, the named-mechanism discipline, measured-scale language instead of scalability adjectives, discovery-validity sentences, triple-blind-safe self-reference, and compression into the single 10-page IEEE all-inclusive cap.
---

# ICDM Writing Style

Revise a manuscript into the register ICDM reviewers reward: a **data-mining mechanism**
made legible to a data-centric IEEE audience, with claims a reviewer can check and a scale
story that is measured rather than asserted. Two hard constraints shape every choice — the
Research Track is **triple-blind**, so the prose cannot lean on author identity, and the
whole paper (references and appendix included) must fit **10 IEEE two-column pages**.

## Open with the data regime, not the model family

ICDM work starts from the shape of the data: streams seen once, power-law-sparse graphs,
implicit rather than explicit feedback, evolving edges, high-dimensional transactions. The
strongest openings name that regime and make the mechanism its consequence.

```text
Weak (model-first):
  "We propose a novel graph neural network with a new attention module
   for anomaly detection, achieving state-of-the-art results."

ICDM-shaped (regime-first):
  "Interaction graphs arrive as an unbounded edge stream seen once and
   cannot be stored. We give a one-pass detector whose memory is
   sub-linear in the number of edges, with a stated error bound."
```

The second version names the regime, implies why existing methods fail, and scopes the
mechanism before a reviewer asks.

## Name the mechanism, and give it a reason

- Replace architecture nouns ("a transformer with X") with a **named mining mechanism** and
  the one property that makes it work (isolation, sparsity, restart probability, sketching).
- Attach every strong adjective to the mechanism: not "our method is scalable" but "the
  sketch updates in amortized constant time per edge."
- State the objective or the guarantee plainly enough that a reviewer sees *why* it should
  generalize before seeing the tables.

## Measure scale; do not adjective it

ICDM referees read "efficient" and "scalable" as claims to be tested. Convert them:

| Adjective (avoid) | Measured claim (prefer) |
|---|---|
| "scalable" | "constant per-edge latency as the stream grows 100x (Fig. 2)" |
| "efficient" | "linear in |E|, sub-linear memory in the number of edges" |
| "outperforms baselines" | "matches the batch detector's top-k ranking at 1/10 the memory" |
| "robust" | "ranking quality within one std over 20 seeds across noise levels" |

## Write discovery-validity sentences

The distinctive ICDM instinct is "is the finding real, or an artifact of the evaluation?"
Pre-empt it: say *why* a flagged pattern, cluster, or anomaly means what you claim — tie it
to a bound, a controlled injection with known truth, or a baseline that shares the setup.
A result that could be an evaluation artifact reads as unfinished here.

## Keep self-reference triple-blind-safe

- Cite your own prior work in the third person: "Prior work [7] introduced X" — never "in
  our earlier paper [7] we introduced X."
- Remove "our deployed system," internal names, and acknowledgements from the body; they
  are anonymity violations, not style slips (see `icdm-submission`).

## Compress into 10 all-inclusive pages

- Every paragraph competes with the appendix and references for the same 10 pages. Cut
  signposting roadmaps and background everyone knows.
- Push protocol detail to an in-cap appendix or the cited anonymized repository, and keep
  the body's argument self-contained — because with no rebuttal, the body is your only
  chance to be understood.

## Vignette: rescuing a buried contribution

A draft opens with two paragraphs on the importance of data mining and a model diagram.
The revision deletes both, opens on "transactions arrive faster than they can be labeled,"
names the sparsity mechanism in sentence two, converts three "efficient/scalable" claims
into measured latencies, and adds one discovery-validity sentence tying flagged
transactions to a known-injection experiment. Same result, half a page shorter, and now
legible to an ICDM reviewer on the first read.

## Output format

```text
[Register] ICDM-ready / drifting to ML-flagship / drifting to journal
[First-page arc] regime / task / mechanism / evidence / validity - present or missing
[Scale language] measured / adjectival
[Anonymity] third-person self-cites: yes / leaks found
[Cut list] <paragraphs to remove to fit the 10-page all-inclusive cap>
```
