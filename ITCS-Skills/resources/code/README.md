# ITCS "Code" Adapter — Why This Pure-Theory Pack Ships No Code Kit

ITCS is a **pure-theory** venue. Its papers are judged on **ideas and proofs**, not on software,
datasets, or experiments, and it has **no artifact-evaluation track and no reproducibility
package** in the empirical-CS sense. So, unlike the software-engineering and ML packs in this
repository, this directory intentionally ships **no `check_repro_package.py`, no badge
checklist, and no econometrics kit**. Importing that machinery here would be a category error:
there is nothing to smoke-test because the deliverable is a **proof**, not a program.

What replaces "reproducibility tooling" at ITCS is **proof-checkability discipline**. The
"artifact" is the mathematics itself: a self-contained argument a competent reader can verify
line by line, plus a public full version (arXiv / ECCC / IACR ePrint) that carries every detail
the page-economical body defers. The relevant policy lives in the skills — see
[`../../skills/itcs-reproducibility/SKILL.md`](../../skills/itcs-reproducibility/SKILL.md),
[`../../skills/itcs-supplementary/SKILL.md`](../../skills/itcs-supplementary/SKILL.md), and
[`../../skills/itcs-artifact-evaluation/SKILL.md`](../../skills/itcs-artifact-evaluation/SKILL.md)
— and the cycle facts live in
[`../official-source-map.md`](../official-source-map.md).

## The proof-checkability passes (what to run instead of a script)

These are human passes, not automated ones — but they are the ITCS analogue of a package smoke
test, and you should run every one before the HotCRP upload:

- **Every central claim has a complete proof present.** No "the proof is standard," no "we omit
  the proof," no "see the full version" for anything a reviewer must check to believe the
  result. A missing proof of a load-bearing lemma is the ITCS equivalent of a broken build.
- **Definitions are self-contained.** Every symbol, model parameter, and non-standard notion is
  defined before use; a reviewer should not need your prior papers open to parse a theorem
  statement (which lightweight double-blind would also expose).
- **Dependency provenance is pinned.** Each borrowed theorem carries a precise citation (venue,
  year, statement number) so a reviewer can trace what you *assume* versus what you *prove*, and
  so an error in a cited result does not silently become your error.
- **Constants and quantifiers are consistent.** The bound in the abstract equals the bound in the
  theorem equals the bound the proof delivers; quantifier order ("for all epsilon there exists n"
  vs. the reverse) is uniform between statement and proof.
- **The full version matches the submission.** If you post to arXiv/ECCC/ePrint (encouraged under
  lightweight double-blind), the theorem statements and proofs there agree with the submitted
  PDF; a divergent preprint invites a reviewer to trust the wrong version.

## Rare, well-scoped computational content

Some ITCS papers include a *small* illustrative computation — a search that found a gadget, a SAT
solve certifying a small separation, a numerically evaluated construction. When they do:

- Treat it as **evidence for a proved claim**, never as the claim itself (see
  [`../../skills/itcs-experiments/SKILL.md`](../../skills/itcs-experiments/SKILL.md)).
- Make the computation **checkable**: state the search space, the tool and version, and — if the
  output is a finite object (a graph, a code, a certificate) — include the object so a reviewer
  can verify it directly, without rerunning anything.
- Keep it out of the anonymity leak surface: a linked repository under a personal account is a
  lightweight-double-blind slip; host it neutrally or fold the object into an appendix.

This is not the SE replication-package kit and not the ML-leaderboard kit: at ITCS, the check
that matters is *"can a skeptical expert follow the proof to the end and agree?"*
