---
name: itcs-reproducibility
description: Use to make an ITCS paper's mathematics independently checkable — complete proofs of every central claim, self-contained definitions, pinned dependencies on prior results, and a matching full version on arXiv/ECCC/ePrint — the pure-theory analogue of a reproducibility package.
---

# ITCS Reproducibility

"Reproducibility" at a pure-theory venue means one thing: **a competent, skeptical reader can
verify every central claim from the paper alone.** There is no code to rerun and no dataset to
re-mine — the analogue of a reproducibility package is a **complete, self-contained, correctly
attributed proof**. ITCS makes this concrete in its call: submissions must include **complete
proofs of all central claims** (in an appendix if needed). This skill is the discipline that
makes the mathematics checkable, which — since ITCS has **no rebuttal** — is also your only
defense against a reviewer who gets stuck.

## Completeness: every central claim is fully proved

- **No "proof omitted," no "proof is standard," no "see the full version"** for anything a
  reviewer must check to believe the result. Deferring a *routine* calculation to an appendix is
  fine; deferring the *load-bearing* lemma is a reproducibility failure and, at ITCS, a likely
  reject.
- **Distinguish proved from assumed.** Every step is either proved here or cited to a precise
  prior result. A theorem that quietly relies on an unproved claim is the theory analogue of a
  package that silently calls a missing dependency.
- **Prove the anchoring result in full.** For a new-model paper, the separation/possibility result
  that shows the model is alive is exactly what a reviewer will try hardest to break — give it the
  most complete treatment in the paper.

## Self-containment: definitions and notation

- **Define every symbol and model parameter before use.** A reviewer should verify a theorem
  statement without opening your prior papers — which lightweight double-blind would expose
  anyway (see [`itcs-related-work`](../itcs-related-work/SKILL.md)).
- **State the exact model, not "the usual one."** Small variations in a definition (adaptive vs.
  non-adaptive, worst-case vs. average, the quantifier order) change what is true; pin them down.
- **Restate borrowed results you rely on.** Quote the precise statement (and its hypotheses) of an
  external theorem you invoke, so a reviewer sees exactly what you assume and can check the fit.

## Dependency provenance: pin what you borrow

The theory analogue of "pinning versions" is **precise citation of the results you build on**:

- Cite each borrowed theorem to a specific venue, year, and statement number — not a vague "it is
  known that."
- Flag any dependency on a **recent, unrefereed, or conditional** result (an arXiv/ECCC preprint,
  a conjecture, an unpublished personal communication). A result standing on an unverified
  preprint should say so; its correctness is then explicitly conditional.
- Separate **assumptions** (P != NP, a hardness assumption, a conjecture) from **theorems**, and
  make every conditional result's hypothesis unmissable in its statement.

## The full version as the durable record

Under lightweight double-blind, authors are **encouraged to post the full version** to arXiv,
ECCC, or the IACR ePrint Archive. Treat it as the permanent, complete record:

- **The full version and the submission must agree.** Divergent theorem statements or proofs
  between the two invite a reviewer to trust the wrong one. Keep them in sync, and say in the
  submission that a full version exists.
- **Put genuinely long proofs in the full version *and* an appendix** the PC can read — a proof a
  reviewer must consult to judge the paper cannot live *only* in an external preprint they are not
  obligated to open (see [`itcs-supplementary`](../itcs-supplementary/SKILL.md)).
- **Keep the preprint's identity handling consistent with your strategy** — posting is allowed and
  common, but the *submitted* PDF still omits author names.

## The checkability passes (run before upload)

```text
[Completeness]  every central claim has a full proof present (appendix ok)? no "omitted"/"standard"?
[Self-contain]  every symbol/model/parameter defined before use? theorem statements parseable alone?
[Dependencies]  each borrowed result cited to venue+year+statement number? unrefereed deps flagged?
[Assumptions]   every conditional theorem states its hypothesis in the statement?
[Consistency]   abstract bound = theorem bound = proof bound; quantifier order uniform?
[Full version]  submission and arXiv/ECCC/ePrint version agree? existence noted?
```

## Common failure modes

| Symptom | Why it fails at ITCS | Fix |
|---|---|---|
| Central lemma "proof omitted" | Violates the complete-proofs requirement | Include the full proof (appendix) |
| Theorem parseable only with your prior paper | Not self-contained; anonymity risk too | Define everything in-paper |
| "It is known that ..." with no cite | Dependency unpinned; reviewer cannot check | Cite venue/year/statement |
| Relies on a preprint silently | Correctness is conditional but hidden | State the conditional dependency |
| Preprint proof differs from submission | Reviewer trusts the wrong version | Sync the two |

## Output format

```text
[ITCS checkability status] verifiable / gaps
[Completeness] central claims fully proved (list any "omitted")
[Self-containment] definitions complete? statements parseable alone? yes/no
[Dependencies] borrowed results pinned? unrefereed/conditional ones flagged? yes/no
[Full version] posted and consistent with submission? yes/no
[Fix queue] <ordered, load-bearing gaps first>
```
