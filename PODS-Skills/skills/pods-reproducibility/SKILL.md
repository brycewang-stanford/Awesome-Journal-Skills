---
name: pods-reproducibility
description: Use when strengthening the verifiability of an ACM PODS paper — a complete claim-to-proof map, self-contained proofs in the at-submission appendix (no external appendices), correctly stated assumptions, honest scope and open cases, the full-version-on-arXiv norm, and consistency between what the paper claims and what the proofs actually establish.
---

# PODS Reproducibility

Use this before submission and again before camera-ready. For a theory venue, "reproducibility" means
**verifiability**: a competent reader can follow every proof and confirm every stated theorem. PODS
makes this concrete by requiring the proof **appendix to be incorporated at submission** — there are
**no online/external appendices** — so the reviewers can check the mathematics now, not on trust.

## Claim-to-proof map

- Map each theorem, lemma, corollary, and reported bound to a **complete proof location** — the body
  or the appendix. No stated result may lack a full proof somewhere in the submitted PDF.
- For each proof, state its assumptions, cite the exact prior lemma or theorem it uses, and do not
  defer a key step to "the full version" or "a routine argument" when the argument is not routine.
- For constructions and algorithms, give enough that a reader could re-derive them: the invariant, the
  data structure, the parameter settings, and the complexity accounting.
- Keep the **assumptions ledger** honest: every conditional result (ETH, OMv, `#P`-hardness) is
  labeled where it is used, and the model (data vs. combined complexity, cost model) is fixed.
- Keep the paper and its proofs **consistent**: an abstract that claims more than the theorems prove,
  or a corollary that does not follow from the stated theorem, is the contradiction reviewers read as
  carelessness.

## Verifiability audit

| Claim in the paper | Weak (reject-prone) form | PODS-ready form |
|---|---|---|
| "Theorem: the problem is hard" | Hardness "sketched"; no reduction given | A complete reduction in the appendix, with the source problem cited |
| "Our algorithm is optimal" | Upper bound only | Upper bound + matching lower bound, both proved |
| "This holds for all such queries" | Proof for the examples shown | A general proof covering every case, or a scoped, honest claim |
| "It is easy to see that..." | The hard step waved away | The argument written out, or a precise appendix pointer |
| "Full proofs in the full version" | Nothing in the appendix | Complete proofs in the at-submission appendix; arXiv full version optional-but-consistent |

"Proof omitted" with no appendix proof is treated at PODS the way "available on request" is treated at
a systems venue — as *not provided*. The appendix exists so nothing decision-critical is off-paper.

## Assumptions and scope pinning

```text
[Model]        fix data model, query class, and complexity/cost measure; use them consistently
[Assumptions]  label every conditional bound with its conjecture at the point of use
[Scope]        state exactly which cases the result covers and which remain open — do not overclaim
[Dependencies] each proof cites the exact prior result it invokes; no circular lemma chains
[Constants]    expose hidden dependence on query size / schema / fixed parameters
```

## Degrees of verifiability (state the one you achieved)

- **Complete:** every theorem has a full, self-contained proof in the submitted PDF (body + appendix).
  This is the PODS default and expectation.
- **Scoped:** the main theorems are fully proved; a clearly labeled extension or a corollary is stated
  with a proof idea and deferred to the journal full version — acceptable only if nothing
  decision-critical is deferred.
- **Conjectural:** a statement is offered as a conjecture with partial evidence — allowed as such,
  never dressed as a theorem.

## The full-version-on-arXiv norm

PODS is an extended-abstract venue: the community norm is to post a **full version on arXiv** (with all
proofs and any extended development) and, at camera-ready, DOI-link it to the PACMMOD paper. At
submission the arXiv version must not break double-anonymity; keep it anonymized or withhold the link
until acceptance. The at-submission appendix, not the arXiv link, is what the reviewers must be able to
verify.

## Vignette: a dichotomy paper

Consider a paper proving a PTIME/hard dichotomy for a query class. Its verifiability spine: the exact
model and query class in preliminaries; the tractable direction as a proved algorithm with complexity;
the hard direction as a complete reduction from a cited problem, under a named assumption if
conditional; a lemma establishing that the two directions partition the class (completeness); and a
scope sentence naming the one extension (e.g. self-joins) left open — every proof in the body or the
at-submission appendix, with a consistent arXiv full version prepared for later.

## Consistency and camera-ready pass

- Before submission: every stated result traces to a complete proof in the PDF; assumptions are
  labeled; the appendix is incorporated and anonymized.
- Before camera-ready: post the (de-anonymized) full version on arXiv and add the DOI link; ensure the
  arXiv version's theorems and the PACMMOD version's theorems agree exactly.

## Output format

```text
[Claim inventory] <theorem/lemma -> complete proof location (body/appendix)>
[Verifiability] complete / scoped / conjectural, stated honestly
[Assumption gaps] <any conditional bound unlabeled? any circular dependency?>
[Scope honesty] <open cases stated? overclaim in the abstract? yes/no>
[Paper fixes] <proofs to complete or pointers to add before submission>
[Full-version plan] <arXiv version prepared, anonymized now, DOI-linked at camera-ready>
```
