---
name: pods-artifact-evaluation
description: Use for the PODS analogue of artifact evaluation — there is no systems artifact track at this theory symposium, so this skill covers formal-claims verification instead: a complete at-submission proof appendix, a claim-to-proof mapping reviewers can check, the full-version-on-arXiv norm, and, only when a paper claims practicality, an honest optional code artifact.
---

# PODS Artifact Evaluation

Use this to prepare the PODS equivalent of an artifact. **PODS has no artifact-evaluation track in the
systems sense and no ACM reproducibility badges** — it is a database-theory symposium. The deliverable
that plays the role of an artifact is your **formal-claims package**: a complete, self-contained proof
appendix that ships with the submission, a mapping from every stated result to its proof, and, at
camera-ready, a **full version on arXiv**. Do not import a systems artifact process; adapt to proof
verification.

## The PODS "badges" — what actually certifies a theory paper

| Analogue | What it certifies | What earns it |
|---|---|---|
| Complete proofs (at submission) | Every stated theorem is proved and checkable now | The appendix incorporated in the submitted PDF, with no gap deferred off-paper |
| Claim-to-proof mapping | A reviewer can locate the proof of each result quickly | Forward references from each body statement to its body/appendix proof |
| Full version on arXiv (at camera-ready) | The community can read the complete development | A de-anonymized arXiv full version, DOI-linked to the PACMMOD paper |
| Optional code (only if practicality is claimed) | A secondary empirical illustration reproduces | A small, documented, public repository — never a substitute for a proof |

The high-value, low-cost "badge" is **complete proofs in the appendix**: it is what the reviewers
verify, and it is entirely in your control. The failure mode at PODS is never "did not run on their
machine" — it is "the proof had a gap" or "the claimed proof was not in the PDF."

## What PODS reviewers check first

| Claim type | First thing inspected | Common failure caught |
|---|---|---|
| A complexity bound | The proof of the bound and its matching lower bound | Upper bound only; lower bound "sketched" |
| A dichotomy | Completeness — that every case is classified and proved | A tractable sub-class, not a full classification |
| A new semantics | Well-definedness and a decidability/complexity result | A definition with no algorithmic content |
| A conditional result | Whether the assumption (ETH/OMv/#P) is stated at point of use | Conditional hardness presented as unconditional |

Assume a reviewer reads the key proofs in the body and opens the appendix for the deferred ones. Design
the appendix so each proof is found and checked without reconstructing context.

## Formal-claims packaging plan

```text
[Appendix]     complete proofs of every deferred result, in the submitted PDF (acmsmall, unlimited
               appendix); PODS forbids external/online appendices
[Mapping]      an explicit body -> proof map: each theorem/lemma forward-references its proof location
[Self-contain] each proof restates the claim, lists assumptions, cites the exact prior lemmas used
[Assumptions]  every conditional bound labeled with its conjecture where it is used
[Full version] an arXiv full version prepared: anonymized (or withheld) at submission, public at
               camera-ready with a DOI link to the PACMMOD article
[Optional code] only if the paper claims practicality: a small, documented public repo, clearly
               secondary, that reproduces the illustrative measurements
```

## Anonymized submission package vs. public full version

- **At submission:** the proof appendix ships inside the anonymized PDF — no author names,
  acknowledgements, funding, or a named system; any arXiv full version is withheld or anonymized so it
  cannot reveal authorship.
- **After acceptance:** post the de-anonymized full version on arXiv, add the DOI link in the
  camera-ready, and (if a code illustration exists) make its repository public. This is the PODS
  analogue of releasing an artifact — a readable full proof, not a runnable badge.

## Worked vignette: packaging a dichotomy paper's claims

A paper proves a PTIME/hard dichotomy. To make the formal-claims package airtight: put the tractable
algorithm and its complexity proof, the hardness reduction, and the completeness lemma in the body's
statements with full proofs in the appendix; add a body-to-appendix map so each theorem points to its
proof; label the hardness result with its complexity assumption at the point of use; prepare an arXiv
full version with the extended development; and, if the paper also claims the algorithm is practical,
add a small optional repository — stated honestly as illustration, not evidence for the theorem.

## Calibration

- There is **no separate artifact deadline and no badge** at PODS; the "artifact" obligations are met
  inside the submitted PDF (proofs) and at camera-ready (arXiv full version).
- If a future PODS edition introduces any formal-verification or reproducibility initiative, confirm it
  on the current call rather than assuming this static picture.

## Output format

```text
[Formal-claims readiness] strong / adequate / gap present
[Appendix] every deferred proof present in the submitted PDF? yes/no
[Claim mapping] <theorem -> proof location present and forward-referenced? yes/no>
[Assumptions] <conditional bounds labeled at point of use? yes/no>
[Full-version plan] <arXiv prepared, anonymized now, DOI-linked at camera-ready>
[Optional code] <present only if practicality claimed; clearly secondary? yes/no/NA>
```
