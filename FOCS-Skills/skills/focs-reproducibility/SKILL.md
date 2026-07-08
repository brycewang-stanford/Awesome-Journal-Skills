---
name: focs-reproducibility
description: Use when hardening a FOCS (IEEE Symposium on Foundations of Computer Science) paper's checkability — the theory analogue of reproducibility — via hypothesis ledgers, single-source theorem statements that cannot drift between submission and arXiv versions, audits of imported theorems, and certificates for machine-checked steps.
---

# FOCS Reproducibility

FOCS has no reproducibility checklist and asks for no artifacts (2026 CFP,
checked 2026-07-08). At a proofs venue, "reproducing" a result means an
independent expert can re-derive it from the paper alone. That property —
checkability — is engineerable, and papers engineered for it survive both
refereeing and the decade of scrutiny that follows a FOCS acceptance. Four
practices below build it.

## 1. The hypothesis ledger

Every assumption a theorem consumes should be visible at the theorem, not
scattered across ambient conventions declared in Section 2. Keep a ledger
during writing:

| Hypothesis | Introduced | Used by | Discharged or standing? |
|---|---|---|---|
| $G$ simple, connected | §2 conventions | Thm 1, 3; Lem 4.2 | standing |
| $\varepsilon < 1/\log n$ | Thm 3 statement | Lem 5.1–5.4 | standing — stated in Thm 3 ✓ |
| oracle access to exact eigenvalues | §5 ¶1 (silent!) | Lem 5.3 | **must surface in Thm 3** |

The audit question for each row: does the *formal statement* of every theorem
that transitively needs this hypothesis mention it? Silent standing hypotheses
are the most common correctness complaint theory referees file, and the
cheapest to fix before submission.

## 2. Statement freeze across versions

A FOCS project lives as at least three documents — the HotCRP submission, the
arXiv/ECCC full version, and eventually the IEEE proceedings version. Theorem
statements must be bit-identical across them; a bound that strengthens
silently between submission and arXiv is, to a referee who checks, either
sloppiness or misconduct. Enforce the freeze mechanically by extracting and
diffing labeled statements:

```bash
# extract_statements.sh — run against any two versions of the source
for src in "$1" "$2"; do
  awk '/\\begin{(theorem|lemma|corollary)/,/\\end{(theorem|lemma|corollary)/' \
      "$src"/*.tex | tr -d ' \n' | sha256sum
done
# identical hashes => no drift in any formal statement
```

Legitimate post-submission improvements go into a dated "changes since
submission" note in the arXiv version, never into silent edits (see
`focs-camera-ready` for the endgame version ledger).

## 3. The imported-theorem audit

Most FOCS proofs stand on external results, and the failure mode is citing a
theorem for slightly more than it says. Before the freeze, audit every import:

- **Locate the exact statement** in the cited source — theorem number, page,
  and version (arXiv preprints renumber theorems between versions; pin the
  version, per `focs-related-work`).
- **Transcribe its hypotheses** into your ledger and check your invocation
  supplies all of them. The classic bug: importing a bound proved for
  constant-degree instances into an unbounded-degree argument.
- **Check parameter regimes.** "For sufficiently large $n$" in the source must
  be compatible with the $n$ your recursion actually feeds it.
- If the imported proof is folklore or unpublished, prove it in your appendix;
  "well known" is not a citation a referee can check.

## 4. Certificates for computed steps

When a proof step is a computation (`focs-experiments`), checkability means a
stranger can re-verify without trusting your code: publish the certificate
(the enumerated cases, the SAT solver's proof trace, the exact rational
arithmetic transcript), ship a minimal independent checker, pin both with
hashes, and state in the proof what object certifies what claim. A referee
who can re-run a 40-line checker in a minute treats the step as proved; one
who is asked to trust an opaque 4,000-line search does not.

## 5. Errata as a first-class object

Checkability extends past acceptance. FOCS papers are cited for decades, and
the community's memory of an error is shaped by how it was handled:

- Maintain the changelog in the arXiv version as the single erratum channel;
  a correction buried in a later paper's footnote does not reach readers of
  the original.
- Downgrade honestly: if a repaired lemma now yields a weaker bound, the
  changelog and the abstract both change — leaving a stale headline bound on
  a corrected paper is the reputational worst case.
- Notify identifiable downstream users directly when a result they built on
  moves; theory's dependency graph is small enough that this is feasible and
  expected.

## Pre-freeze checkability review

Run as a dedicated pass, separate from proofreading:

1. Ledger complete; no silent standing hypotheses (§1).
2. Statement hashes identical between submission source and full-version
   source (§2).
3. Every external import located, transcribed, regime-checked (§3).
4. Every computed step certified and independently checkable (§4).
5. One non-author has re-derived the most delicate lemma from the paper text
   alone — the strongest single predictor that referees will succeed too.

A paper passing all five is not guaranteed acceptance; it is guaranteed not
to be rejected for the reasons authors most regret, and it is camera-ready
for the public record that FOCS culture expects the full version to become.
