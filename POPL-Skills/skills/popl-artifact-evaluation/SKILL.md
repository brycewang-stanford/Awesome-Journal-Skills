---
name: popl-artifact-evaluation
description: Use when packaging a POPL artifact — above all a mechanized proof development in Rocq/Coq, Lean, Agda, or Isabelle — for the post-conditional-acceptance evaluation, satisfying the no-admit/no-sorry completeness rule, mapping paper theorems to proof files, pinning toolchains, and earning the Functional, Reusable, and Available badges.
---

# POPL Artifact Evaluation

POPL invites authors of conditionally accepted papers to submit supporting materials
to artifact evaluation, and its AE tracks treat **proof developments as the canonical
artifact**: Coq and Isabelle proof libraries are the track's own examples of reusable
artifacts (POPL 2025/2026 AE pages, read 2026-07-08). A verification tool or
evaluation harness can ride along, but at this venue the evaluator's core question is
usually "does this mechanization actually prove what the paper claims?"

## The badge criteria, proof-flavored

| Badge | Criterion (2025/2026 wording) | For a proof artifact this means |
|---|---|---|
| Artifacts Evaluated - Functional | Supports the paper's claims, documented well enough to run and validate | The development compiles from scratch and each paper theorem is checkable |
| Artifacts Evaluated - Reusable | Additionally packaged for reuse: docs, installation, portability, new examples, open licensing / issue tracker | Definitions and lemmas usable by other projects — and **complete: no `admit` in Coq/Rocq, no `sorry` in Lean or Isabelle** |
| Artifacts Available | Archived eternally on an archival repository (Zenodo, ACM DL) | A DOI-stamped snapshot; a lab GitHub URL is not archival |

The completeness rule is the sharpest tooth: a single admitted lemma demotes a
"reusable" claim, and evaluators grep for it.

## The axiom audit

Closing all goals is not enough — evaluators also ask what the development *assumes*.
Print the axiom footprint of every top-level theorem and disclose it in the README:

```bash
# Rocq/Coq: full consistency check plus per-theorem assumptions
coqchk -silent -o MyDev.Main
echo "Print Assumptions main_soundness." | coqtop -l theories/Main.v
# Lean 4: elaborate and show axioms
lake build && echo '#print axioms Main.soundness' >> Scratch.lean
# Agda: flag unfinished holes and postulates
grep -rn "postulate" src/ ; agda --safe src/Everything.agda
```

Classical axioms, functional extensionality, or proof irrelevance are usually
acceptable *when declared*; an undeclared axiom discovered by the evaluator is a
credibility wound.

## Package for an evaluator with one week and one laptop

- **Pin the toolchain.** Proof assistants break across versions: fix the Rocq/Coq
  release via opam switch or the Lean toolchain via `lean-toolchain`, and ship a
  container or VM where `make` just works.
- **Map claims to files.** A `CORRESPONDENCE.md` table — paper theorem number,
  formal statement name, file, line — is the single highest-leverage document
  (`popl-reproducibility` maintains it from submission onward).
- **Budget honest times.** Say that the full build takes 90 minutes and the
  kick-the-tires target takes 5; give a `make quick` that checks one headline
  theorem.
- **State the deltas.** Where the mechanization simplifies the paper (a smaller
  calculus, a restricted case), say so in the README before the evaluator finds out.
- Archive the exact evaluated snapshot on Zenodo for the Available badge, and keep
  developing in the live repository afterward.

## Output format

```text
[Artifact type] proof development / tool + proofs / tool only
[Completeness] admits: <n>  sorries: <n>  postulates: <n>  (target: 0 declared-only)
[Axiom footprint] <per main theorem>
[Correspondence] <paper theorems mapped / total>
[Badge readiness] Functional: <y/n> Reusable: <y/n> Available: <DOI or missing>
```
