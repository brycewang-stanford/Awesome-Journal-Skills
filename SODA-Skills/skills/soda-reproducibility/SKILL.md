---
name: soda-reproducibility
description: Use when hardening the verifiability of a SODA (ACM-SIAM Symposium on Discrete Algorithms) paper, where reproducibility means checkable mathematics — complete proofs in the submitted full version, stable statement-proof correspondence, explicit constants and model assumptions, and certificates for any machine-checked step.
---

# SODA Reproducibility

At SODA, "reproducibility" is not seeds and GPUs — it is whether a competent
reader can re-derive every claim from the submitted document. Because SODA takes
full versions with no page limit (2027 CFP, checked 2026-07-08), there is no
"details omitted" escape hatch: the community's expectation is that the PDF on
HotCRP contains a complete, checkable argument. This skill is the audit for that
standard.

## The verifiability ledger

Build a table with one row per claim before the July deadline. It doubles as the
rebuttal-preparation ledger in September (`soda-author-response`).

| Column | What goes in it |
|---|---|
| Claim | Theorem/lemma/corollary number and one-line statement |
| Model | Computation model and input assumptions (RAM model? adversary? degree bounds?) |
| Proof location | Section and page of the complete proof — "sketch only" is a red flag |
| External results used | Exact citation with theorem number, plus where hypotheses are checked |
| Constants | Hidden-constant status: explicit / bounded / genuinely unbounded |
| Checked by | Coauthor who verified the proof without having written it |

Every row must close before submission. The last column is the single most
valuable ritual an algorithms group can institutionalize: author-blind proof
checking catches the drift bugs that referees otherwise find in August.

## Failure modes referees actually report

- **Statement-proof drift.** The theorem says `O(m log n)`, the proof delivers
  `O(m log^2 n)` after a late edit. Mechanically re-derive the final bound from
  the final proof, not from memory.
- **Imported-theorem hypothesis gaps.** A cited result requires constant degree;
  your graph is merely sparse. Quote the hypothesis next to each use.
- **Model slippage.** The lower bound is proved against oblivious adversaries;
  the abstract claims it for adaptive ones. State the model in the theorem, not
  only in the preliminaries.
- **Randomness accounting.** "With high probability" needs a stated exponent and
  a union-bound budget that survives all invocations.
- **Case-analysis holes.** For arguments with many cases, include the case
  inventory explicitly; referees count cases before reading any.

## Worked micro-example: a probability budget

The randomness-accounting failure deserves its own drill because it compounds
silently. Keep a single budget table in the source comments and make every
"w.h.p." claim draw from it:

```text
% Failure-probability budget for Theorem 2 (target: n^{-2} overall)
%   E1: sampling lemma (Lemma 3.1), invoked <= n times ... n * n^{-4}
%   E2: hash collision (Lemma 3.4), invoked once      ... n^{-3}
%   E3: concentration (Lemma 4.2), invoked <= log n   ... log n * n^{-4}
%   Union bound: n^{-3} + o(n^{-3}) <= n^{-2} for n >= n_0 (state n_0!)
```

Audit questions the table forces: does each lemma's stated exponent survive
its *actual* invocation count in the final proof (invocation counts drift when
algorithms get restructured)? Is the constant `n_0` stated anywhere? Does the
theorem statement promise the same exponent the budget delivers? A referee who
finds one unbudgeted invocation will re-check every probabilistic step in the
paper — the budget table is cheap insurance against that spiral.

## Machine-checked steps

When part of the argument is computational (exhaustive search over configurations,
extremal-object certificates, verified constants), the reproducibility bar is a
**rerunnable check**, not a claim of one:

```bash
# The paper should let a referee do exactly this:
git clone <anonymous-archive-url> && cd verification
python3 check.py            # deterministic; prints per-case status
echo $?                     # 0 iff every case verified
```

State in the paper the case count, total runtime on commodity hardware, and the
reduction proving that `check.py` succeeding implies the lemma. See
`soda-artifact-evaluation` for packaging and anonymity.

## Full version as the reproducibility instrument

The arXiv full version is the community's long-term verification record — SODA
proceedings versions are often condensations (`soda-camera-ready`). Discipline:

- The submitted HotCRP version, the arXiv version, and the proceedings version
  must agree on every theorem statement; keep a single source with build flags
  rather than three diverging files.
- When a bug is found post-publication, fix the arXiv version with a dated
  erratum note; silent replacement erodes exactly the trust this skill protects.
- Version the bibliography: a "personal communication" load-bearing citation is
  a reproducibility hole; get the statement into a citable preprint or prove it
  yourself in an appendix.

## Pre-submission audit sequence

1. Ledger complete: every claim has a proof location and a blind checker.
2. Bound re-derivation pass: recompute each headline bound from its final proof.
3. Import pass: every external theorem quoted with hypotheses verified in-text.
4. Probability pass: failure probabilities summed and stated once, correctly.
5. Computation pass: certificates rerun from a clean clone on a second machine.
6. Cross-version pass: submission, arXiv, and any slides state identical bounds.

## Output format

```text
[Verifiability verdict] Checkable / Gaps found / Not checkable
[Ledger gaps] <claims lacking proof location, blind check, or model statement>
[Drift findings] <statement-proof or cross-version mismatches>
[Import findings] <external results with unverified hypotheses>
[Computation findings] <uncertified machine-checked steps>
[Fix order] <ranked repairs before the July deadline>
```
