---
name: stoc-artifact-evaluation
description: Use when deciding what evidence objects a STOC (ACM Symposium on Theory of Computing) paper must ship, given that STOC runs no artifact-evaluation track — the durable artifact is the public full version on arXiv/ECCC, plus verifiable certificates whenever a proof leans on computation, and optional mechanization.
---

# STOC Artifact Evaluation

STOC has no artifact-evaluation committee, no badges, and no code-upload channel:
nothing of that kind appears in the STOC 2026 Call for Papers (checked
2026-07-08). Importing an ML-conference artifact checklist would answer questions
this venue never asks. But STOC is not artifact-free either — the 2026 CFP
*expects* accepted authors to place the full paper, with all proofs, on arXiv or
ECCC by camera-ready. So the venue's real artifact policy is: **the extended
abstract advertises; the public full version is the object of record.** Plan your
evidence around that split.

## The STOC evidence stack

| Evidence object | Lives where | Consumed by | Binding? |
|---|---|---|---|
| Theorem statements + overview | First 12 pages of the submission | The whole PC, guaranteed | Yes — the reading contract |
| Complete proofs | Appendix of the submission; later the arXiv/ECCC full version | Assigned reviewers; posterity | Yes — correctness rests here |
| Certificates for computer-assisted steps | Appendix description + released checker | Any skeptic with a laptop | Yes, if a proof step depends on them |
| Illustration code (plots, small searches) | Public repository linked from the full version | Casual readers | No |
| Mechanized proofs (Lean, Coq, Isabelle) | Repository + a coverage statement in the paper | Formal-methods-inclined readers | No, but rising in credibility value |

## When computation is inside the proof

The one place STOC treats code with journal-referee seriousness is a
**computer-assisted step**: an exhaustive case check, a SAT/ILP-certified
combinatorial fact, an interval-arithmetic bound, a verified base case for an
induction. House expectations, drawn from how such papers are read:

- State in the theorem's proof, not a footnote, that a step is machine-checked,
  and characterize the computation: search space, pruning logic, runtime, and
  what exactly the program's output certifies.
- Prefer computations that emit a **certificate checkable by independent code**
  (a DRAT proof from a SAT solver, an explicit combinatorial witness) over "our
  program found no counterexample."
- Ship the checker with the full version. arXiv accepts ancillary files, which is
  the cleanest venue-native mechanism:

```bash
# arXiv ancillary files ride inside the source tarball under anc/
mkdir -p anc
cp verify_certificate.py certificate.drat anc/
tar czf stoc-full.tar.gz full-version.tex macros.tex refs.bib anc/
# arXiv lists anc/* as downloadable ancillary files next to the paper
```

- Pin the environment in one line ("Python 3.12, no dependencies; verified
  independently with drat-trim") — a skeptic should reproduce the check in
  minutes, because at least one will try.

## The full version as the artifact of record

Before camera-ready (and ideally before submission, since theory reviewers
routinely search for the full version even under double-blind), audit it as you
would a released artifact:

- **Completeness:** no proof step deferred to "the full version" *inside* the
  full version; that document is the end of the chain.
- **Self-containment:** definitions and notation resolve internally; a reader
  must not need the extended abstract open in a second window.
- **Versioning:** arXiv revisions are the community's errata mechanism. When a
  bug is found post-publication, the corrected arXiv version plus a changelog
  note in the abstract field is standard practice; silent replacement is not.
- **Anonymity timing:** if the full version goes up before notification, keep it
  consistent with the double-blind submission rules of the current cycle
  (待核实 each year — the interaction between preprint posting and STOC's newly
  adopted anonymization is exactly the kind of policy that gets refined).

## Worked vignette: a construction found by search

Suppose a submission's key lemma asserts that a particular 11-vertex gadget
with a rare expansion property exists, and the gadget was found by a randomized
search over labeled graphs. The evidence plan under STOC norms:

- The lemma's proof in the appendix presents the gadget explicitly (adjacency
  list in a figure) and verifies its property *analytically* where feasible; if
  the property check is itself a finite computation, the proof says exactly
  what was computed and by what procedure.
- The search program is credited in one sentence and never trusted: "the gadget
  was located by simulated annealing; its properties are verified below."
- A 25-line standalone checker that re-verifies the property from the adjacency
  list ships as an arXiv ancillary file with the full version.
- Nothing about the search's hyperparameters, runtime, or seed enters the
  paper — those matter only when a *nonexistence* claim rests on the search,
  which would move the computation into the certified-proof-step regime.

## Optional strengtheners, priced honestly

- A **Lean/Coq mechanization** of a central lemma is a strong credibility signal
  in the current theory climate (STOC 2026's TheoryFest even hosted a workshop on
  AI and theorem-proving), but state coverage precisely: which statements, which
  axioms, what remains informal. Overclaiming formality is worse than none.
- A **reference implementation** of a new algorithm helps readers, but do not let
  it drift into benchmark claims the paper does not make — that invites the
  question of why the paper is not at an experimental venue.
- The STOC 2026 opt-in **LLM pre-submission feedback** experiment (full paper due
  November 1, output visible only to authors) is a free adversarial reader for
  rigor, not an artifact process; treat its output as hints to verify, never as
  verification.

## Quick decision rubric

- Claim depends on a computation → certified proof step: determinism,
  certificate, independent checker, all shipped. Non-negotiable.
- Computation only *found* something humans then verified → one sentence of
  credit; the found object carries the weight.
- Code merely illustrates → public repository after acceptance, linked from
  the full version; keep it out of the reviewed pages.
- Someone suggests an "artifact appendix" with environment tables → decline;
  that is another venue's ritual and reads as venue confusion here.

## Output format

```text
[Evidence stack] <object -> location -> binding or optional>
[Computer-assisted steps] none / certified (checker shipped?) / uncertified <- fix
[Full-version audit] complete / gaps: <list>
[Mechanization] none / partial (coverage stated?) / full
[Release plan] <arXiv/ECCC timing, anc files, repository>
```
