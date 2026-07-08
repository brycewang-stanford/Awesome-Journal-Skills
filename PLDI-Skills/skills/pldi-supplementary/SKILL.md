---
name: pldi-supplementary
description: Use when deciding what accompanies a PLDI submission beyond the 20 text pages — full proofs, extended benchmark data, anonymized code — and how to keep every extra byte double-blind, optional for reviewers, and consistent with the main PDF under summary-rejection formatting rules.
---

# PLDI Supplementary Material

PLDI's cap is on *text pages excluding bibliography* in the main submission
(20 for the 2026 cycle); everything else — complete proofs, full benchmark
tables, anonymized implementations — is supporting material whose exact
submission mechanics (appendix inside the PDF vs separate upload, size limits,
reviewer obligations) are reset per cycle and were **not fully visible for 2026
(待核实)**. Decide placement by role first, then check the live CFP for the
mechanics.

## Placement by role

| Material | Where it belongs | Why |
|---|---|---|
| Proof sketches of main theorems | Main text | Reviewers judge soundness from the body |
| Full proofs, case analyses | Appendix/supplement | Depth on demand; body states theorem + sketch |
| Headline benchmark results | Main text | The claim lives or dies here |
| Per-benchmark raw tables, extra configurations | Supplement | Evidence of thoroughness, not the argument |
| Anonymized source code | Anonymous link or upload | Early credibility; becomes the AE artifact later |
| Semantics figures too large for the text block | Rethink first | If reviewers need it to follow §4, it is not supplementary |

The governing rule: **the 20 pages must carry the whole argument.** PLDI
reviewers are typically not obliged to read beyond the main paper, so a proof
step or baseline definition that exists only in the supplement effectively does
not exist for a skeptical reviewer.

## Anonymity extends to every byte

The double-blind requirement covers supplements with sharper teeth than the PDF,
because archives carry metadata the paper does not:

```bash
# Sweep an anonymized code drop before upload
rm -rf pkg/.git pkg/.github
grep -rniE 'copyright|@[a-z0-9.-]+\.(edu|org|com)|university|author' pkg/ | head
find pkg/ \( -name '*.DS_Store' -o -name '*.orig' -o -path '*__pycache__*' \) -delete
tar tzf pkg.tgz | grep -Ei '/home/|/Users/' && echo "LEAK: user paths in archive"
```

PL-specific leaks: license headers naming the lab, a build script pulling from a
personal GitHub, benchmark result CSVs with hostname columns, and proof files
whose module comments name the authors. Host anonymized code on an anonymizing
service, never on a "private-but-guessable" lab URL.

## Consistency contract with the main PDF

- Numbers quoted in the body must be derivable from supplement tables — same
  runs, same aggregation. A geomean in the paper that cannot be recomputed from
  the supplementary CSVs reads as fabrication risk, not sloppiness.
- Theorem numbering must match between body and full-proof appendix; renumber
  once, late, mechanically.
- If the supplement includes a README, it obeys the same anonymity and
  no-forbidden-links rules as the paper.

## Timing

Build the supplement *with* the paper, not the night after the deadline. The
supplement you assemble in a rush is the one that ships a `.git` directory; and
since the same package matures into the post-acceptance Zenodo artifact
(`pldi-artifact-evaluation`), early hygiene is compounding interest.

## Output format

```text
[Self-containment] can reviewers judge the claim from 20 pages alone? yes/no
[Placement map] item -> body / appendix / code drop
[Anonymity sweep] git dirs / metadata / paths / license headers / hosting
[Consistency] body numbers recomputable from supplement? theorem numbering aligned?
[Mechanics 待核实] appendix-vs-upload rules and size caps from the live CFP
```
