---
name: colt-artifact-evaluation
description: Use when deciding what evidence package a COLT (Conference on Learning Theory) paper needs, given that COLT runs no artifact-evaluation track or badges — the proof appendix is the artifact. Covers proof-verification passes, optional code companions for numerics, formalization aids, and post-acceptance release of scripts.
---

# COLT Artifact Evaluation

First, the honest framing: **COLT has no artifact-evaluation track, no artifact
badges, and no code-submission requirement.** Nothing of the kind appears in the COLT
2026 Call for Papers or conference pages (checked 2026-07-08). Do not import
NeurIPS/ICML-style artifact checklists into a COLT plan; they answer questions this
venue does not ask. What replaces artifact review at COLT is the referee's line-by-line
reading of your proofs — so this skill treats the proof appendix as the artifact and
tells you how to make it verifiable.

## What replaces the artifact track

| At an artifact-track venue | The COLT counterpart | Who "evaluates" it |
|---|---|---|
| Code repository with run scripts | Complete proofs in the same PDF | Reviewers, line by line |
| Reproducibility checklist form | Explicit assumption and constant bookkeeping | Reviewers and the AC |
| Artifact badge | Community trust that the argument closes | Readers citing the bound |
| Dockerized environment | Self-contained lemma dependencies | Anyone re-deriving the result |
| Benchmark seeds and configs | Scripts for illustrative numerics, if any | Discretionary reader interest |

## The proof appendix as artifact

A COLT artifact plan is a verification plan:

- Map every theorem to its full proof location and confirm no step says "similarly" or
  "standard" where the step is neither.
- Track constants explicitly through the proof chain; a constant that changes value
  between Lemma 4 and Theorem 1 is the theory equivalent of a failing test.
- List every external result invoked (concentration inequalities, minimax theorems,
  reductions) with a precise citation including theorem number, and check that your
  setting satisfies that result's hypotheses — the most common hidden bug.
- Have a coauthor who did not write a proof verify it cold, logging time-to-verify.
  Sections that take a fresh expert more than an hour per page need restructuring
  before a time-pressed referee sees them.

## A verification ledger you can actually run

Keep a machine-checkable inventory next to the LaTeX source:

```text
# proof-ledger.txt — one line per claim, updated at every freeze
THM1  full proof App.B  | deps: LEM3, LEM4, [BLM13 Thm 6.2]  | verified: RG 2026-01-12
THM2  full proof App.C  | deps: THM1, LEM5                   | verified: none  <-- BLOCKER
LEM3  full proof App.B.1| deps: none                          | verified: SW 2026-01-08
LEM4  sketch only       | deps: [SSBD14 Lemma 26.8]           | verified: n/a   <-- expand
COR1  two lines in body | deps: THM2                          | verified: with THM2
```

The rule: no submission while any load-bearing line reads `verified: none`. This
ledger, not a badge, is COLT-grade artifact discipline.

## When code exists anyway

Many COLT papers include small numerical illustrations, and some results come with
reference implementations. Norms for those:

- The 2026 CFP imposed no code-upload mechanism; if you want reviewers to see code,
  it must be referenced in the PDF via an anonymized link or included as appendix
  pseudocode. Anonymize repository history and hosting if you link during review.
- Keep illustration scripts tiny and dependency-light: one file that regenerates the
  figure from a fixed seed is worth more than a framework.
- Formal-verification companions (Lean or Coq mechanizations of a key lemma) are an
  emerging but optional credibility signal in the theory community — mention one if it
  exists, never fake partial formalization as full.
- After acceptance, publish scripts in a citable repository and link them from the
  arXiv version, since the PMLR PDF is fixed at camera-ready.

## Worked vignette: packaging a bandit paper's evidence

A hypothetical submission proves a $O(\sqrt{TK})$ regret upper bound and a matching
lower bound, and includes one figure simulating both on the lower-bound instance.
Its artifact plan under COLT rules:

- The upper-bound proof (App. B) and lower-bound construction (App. C) are the
  artifacts; both enter the ledger with named verifiers and dates.
- The external-results audit lists the two concentration inequalities used, each with
  source theorem number and a one-line check that boundedness hypotheses hold.
- The figure's generating script (40 lines, numpy only) is described procedurally in
  App. D — instance parameters, seed, 100 replications — because no upload channel
  exists; the script itself is queued for a public repository at acceptance.
- Nothing else ships. No environment files, no hardware table, no checklist — those
  belong to venues that ask for them.

## Post-acceptance release checklist

When code or mechanization exists, release it once anonymity ends:

| Item | Standard | Why it matters at COLT |
|---|---|---|
| Repository | Public, licensed, tagged at camera-ready state | The PMLR PDF is frozen; the repo carries updates |
| Link placement | arXiv version + PMLR "code" field if offered | Theory readers find papers via arXiv first |
| Script scope | Regenerates each figure from a fixed seed | Matches the illustration claims exactly |
| Mechanized proofs | State coverage precisely (which lemmas, which axioms) | Partial formalization overstated reads as spin |

## What not to do

- Do not pad a COLT submission with an "artifact appendix" of configs and hardware
  tables for a paper whose claims are theorems; reviewers read it as misunderstanding
  the venue.
- Do not promise a code release as a substitute for a complete proof — no reviewer
  here will trade executable evidence for a gap.
- Do not cite artifact badges from other venues as evidence of correctness.

## Cycle-volatility warnings

- If a future COLT cycle introduces any code or artifact mechanism, the CFP will say
  so explicitly; absence in 2026 does not bind later years (待核实 each cycle).
- Anonymous-linking rules during review follow the current anonymity policy, which is
  re-issued yearly.

## Output format

```text
[Artifact reality check] proofs are the artifact / paper also ships numerics
[Verification ledger] complete / gaps at <claims>
[External results audit] <result -> hypotheses checked?>
[Code companion] none needed / anonymized link / post-acceptance release
[Blocking item] <the one unverified load-bearing claim>
```
