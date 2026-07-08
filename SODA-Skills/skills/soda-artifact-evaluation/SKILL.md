---
name: soda-artifact-evaluation
description: Use when deciding how code, computations, or data attach to a SODA (ACM-SIAM Symposium on Discrete Algorithms) paper — SODA itself runs no artifact track, so this skill covers computer-assisted proof evidence, implementation companions, and when to route the artifact to co-located ALENEX's formal artifact evaluation instead.
---

# SODA Artifact Evaluation

First, the venue truth: **SODA has no artifact-evaluation track.** Referees judge
proofs, not repositories. But two kinds of computational objects still matter to a
SODA author, and the co-located satellite ALENEX runs a genuine AE process — for
the 2027 cycle, ALENEX's dates were: submission July 20, 2026; notification early
September 2026; artifact submission September 11, 2026; AE rebuttal October 12-14;
AE results by October 16, 2026, with a dedicated HotCRP AE site
(`alenex27ae.hotcrp.com`; checked 2026-07-08 via search renderings of the SIAM
ALENEX27 pages).

## Which of three situations are you in?

| Situation | Artifact's role | Correct home |
|---|---|---|
| Proof relies on machine computation (case enumeration, SAT/ILP certificate, verified numerics) | Part of the proof — reviewers must be able to check it | The SODA submission itself, described in the paper, archive linked |
| Implementation exists but the claim is the theorem | Supporting color; zero review weight at SODA | arXiv full version appendix + repository; one paragraph in the paper |
| The experiments are the contribution (engineering, tuning, real datasets) | The reviewed object | ALENEX, with its AE process — not SODA |

The routing mistake costs a cycle: an implementation-led paper at SODA reads as a
theorem-light submission; a theorem-led paper at ALENEX reads as an experiment-light
one. `soda-experiments` covers the boundary in detail.

## Computer-assisted proof evidence at SODA

When a lemma's truth rests on computation, treat the computation like a proof step:

- State in the paper *what* was computed, *why* the computation's correctness
  implies the lemma, and the reduction from lemma to finite check.
- Prefer **certificates over executions**: a SAT unsatisfiability certificate, an
  LP dual solution, or an exhaustive-search transcript that an independent checker
  can validate is stronger than "our script printed True."
- Pin the environment. A checker that needs one standard tool beats a stack of
  research dependencies.
- Anonymity still applies at submission time (lightweight double-blind): host the
  archive at an anonymous URL or describe it and promise availability; a link to
  `github.com/yourname` defeats the author-block scrubbing.

A minimal verification bundle that a skeptical theorist can run:

```text
verification/
├── README.md          # lemma ↔ computation map; expected output; runtime
├── generate.py        # enumerates the finite case space (deterministic)
├── check.py           # validates each case; exits nonzero on failure
├── certificates/      # per-case witnesses, checkable independently
└── environment.txt    # exact toolchain versions
```

The README's first line should be the command that reproduces the check, and the
paper should quote the total case count so a re-runner knows when they are done.

## Certificate patterns by claim type

Choosing the certificate form is the design decision; everything else is
plumbing. Patterns that referees can check without trusting your code:

| Claim shape | Certificate | Independent check |
|---|---|---|
| "No object with property P exists below size k" | Exhaustive enumeration transcript + case count stated in the paper | Re-run enumeration; compare count |
| "Formula/configuration is unsatisfiable" | DRAT or similar proof log from the solver | Standard proof checker, not your solver |
| "This LP/SDP bound holds" | Dual solution with rational entries | Verify feasibility + objective by exact arithmetic |
| "This extremal object exists" | The object itself, in a documented format | Verify its properties directly (cheap direction) |
| "Constant c < 1.4142" | Interval-arithmetic evaluation script | Re-run with a different interval library |

Two disciplines cut referee effort by an order of magnitude: make the *checking*
program trivial even if the *searching* program was heroic, and put the case
count / certificate size in the paper so a verifier knows what "done" looks
like before starting.

## Routing to ALENEX AE

If the artifact is the point, the ALENEX pipeline gives it real review: artifacts
are submitted after paper notification (September 11, 2026 for the 2027 cycle),
evaluated with a rebuttal round in mid-October, and the results feed the final
paper. Practical notes for a SODA-adjacent group:

- ALENEX's paper deadline (July 20, 2026) sits eleven days after SODA's — a SODA
  submission's experimental spin-off can be written in that gap, but the two
  papers must have genuinely disjoint contributions.
- Prepare the artifact for a stranger's machine: pinned dependencies, dataset
  download scripts with checksums, a single entry point per figure/table.
- The AE rebuttal (October 12-14, 2026) is for fixing evaluator blockers, not for
  adding features — keep a maintainer on call that week.

## Referee psychology of computer-assisted claims

A theory referee meeting a machine-checked lemma asks three questions in order,
and the paper should answer them in the same order: *Is the reduction from
lemma to finite check proved?* (prose, in the paper, no code involved); *Could
the check be wrong?* (certificates checkable by independent tools answer this;
"our program says so" does not); *Can I re-run it before my review is due?*
(state the runtime — an hour on a laptop invites verification, a week on a
cluster invites suspicion). Papers that answer all three convert the
computational step from a reviewing liability into a fully-verified component;
papers that answer none of them get reviews containing the phrase "we were
unable to verify," which at a proofs-are-the-product venue is close to fatal.

## Post-acceptance artifact hygiene (either venue)

- Move from "anonymous archive" to a citable, versioned release (tagged repository
  plus an archival DOI service) referenced in the camera-ready.
- The repository README should state the paper title, venue, and which claims the
  code supports — and, honestly, which it does not.
- Freeze the version that matches the proceedings; development continues on main,
  but the paper points to the tag.

## Output format

```text
[Artifact routing] SODA-internal proof evidence / arXiv companion / ALENEX AE
[Proof-dependence audit] <claims whose truth relies on computation, and their certificates>
[Anonymity state] <archive hosting compatible with double-blind: yes/no>
[AE calendar] <applicable ALENEX dates, owner per deadline>
[Release plan] <post-acceptance versioning and DOI>
```
