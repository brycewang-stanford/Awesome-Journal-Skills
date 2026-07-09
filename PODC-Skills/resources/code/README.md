# PODC Proof-and-Simulation Code Adapter

This directory routes PODC authors to the repository-level shared tooling. It stays deliberately
thin: PODC-specific *policy* (the proofs-centric review, lightweight double-blind, the 10-page
merits budget, the no-artifact-track reality) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared
kits so packs do not carry diverging copies.

## What "code" means at a proofs venue

Most PODC papers ship **no code at all** — the contribution is a theorem and its proof. When a PODC
paper does include artifacts, they are almost always **optional simulations** that illustrate a
constant, plot a convergence rate, or sanity-check a bound; they are never the evidence of
correctness. Treat any such script as a figure-generator, not as the paper's claim. There is **no
artifact-evaluation track** to submit it to; it lives in the arXiv full version or an author page.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — a general packaging checklist; use only the parts about seeds, environment pinning, and a
  one-command run for the *optional simulation*. Ignore the badge/anonymous-artifact sections; PODC
  has neither.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free layout smoke checker, useful if you release a simulation bundle alongside the
  arXiv full version.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  — generic pre-submission scaffolding; the PODC-specific readiness gate is the proof appendix and
  the double-blind sweep, in [`../../skills/podc-submission/SKILL.md`](../../skills/podc-submission/SKILL.md).

## Typical use for an optional PODC simulation bundle

```bash
# Layout smoke test on a simulation bundle you plan to link from the arXiv full version
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/podc-simulation-bundle
```

## PODC-specific checks the generic tooling cannot make

- **The proof appendix is self-contained.** Every lemma the main theorem invokes is stated and
  proved (or cited to a precise external statement); the reader never needs a file that is not in the
  submission or its full version (`../../skills/podc-reproducibility/SKILL.md`).
- **The model box is explicit and matches every claim.** Network model (message-passing/shared
  memory), timing (synchronous/asynchronous/partial synchrony), fault model (crash/Byzantine/
  self-stabilizing), adversary (adaptive/oblivious), and the cost measure (rounds/messages/bits/
  space) are fixed before the first theorem, and no proof silently changes them
  (`../../skills/podc-experiments/SKILL.md`).
- **A simulation is labeled optional and honest.** If included, it states the parameter ranges, the
  random seeds, and that it *illustrates* rather than *establishes* the result; it never stands in
  for a missing proof (`../../skills/podc-experiments/SKILL.md`).
- **The double-blind sweep covers the bundle too.** A linked simulation repo, author page, or arXiv
  version must not de-anonymize the submission during review
  (`../../skills/podc-submission/SKILL.md`).

This is not the ACM artifact-badge kit used by the software-engineering packs, and it is not the
econometrics/Stata kit used by the journal packs: PODC has no badges and no empirical-social-science
apparatus. Do not import either here.
