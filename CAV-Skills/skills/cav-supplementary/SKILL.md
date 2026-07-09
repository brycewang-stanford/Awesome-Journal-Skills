---
name: cav-supplementary
description: Use when deciding what belongs in a CAV (Computer Aided Verification) paper body versus its optional appendix and artifact, covering the LNCS page limits, the rule that reviewers are not obliged to read the appendix so decision-critical content stays in the body, where full proofs and benchmark tables live, and double-anonymous supplementary material for the anonymized categories.
---

# CAV Supplementary

Use this when assembling CAV supplementary material. The governing rule is strict and specific to
CAV's format: a **clearly marked appendix is allowed, but reviewers are not obliged to read it**. So
the paper must be **judgeable from the body alone** — anything a reviewer must see to accept lives
inside the page limit, and the appendix and artifact only support it.

## What goes where

| Content | Body (within the page limit) | Appendix / artifact |
|---|---|---|
| The problem, the technique, the main theorem | Yes | — |
| Proof idea / sketch of the main result | Yes | Full formal proof |
| Supporting lemmas | Statement + role | Full proofs |
| Headline benchmark comparison + resource limits | Yes | Full per-instance tables |
| Soundness/differential-check result | The result + method | The raw logs and witnesses |
| Benchmark set + selection | Summary + revision | The full instance list, fetch scripts |
| Tool build/run instructions | A pointer | README + scripts (artifact) |
| Proof certificates / witnesses | A pointer | The certificates + a checker (artifact) |

If a reviewer would need to open the appendix or artifact to know whether the theorem holds or the
comparison is fair, the paper is mis-partitioned — move that content into the body.

## The page-limit discipline

CAV's LNCS limits (Regular 18 pages; Short Tool / Application / Industrial 10 pages) **exclude
references and appendices**, but the appendix is optional-to-read. Consequences:

- Keep the **main theorem's proof idea** and the **headline benchmark result with its resource
  limits** in the body — they are decision-critical.
- Move **full formal proofs**, **per-instance benchmark tables**, and **extra property classes** to
  the appendix or artifact with explicit forward references.
- Do **not** use the appendix to smuggle in a result that would not fit — an argument that only
  closes with unread material reads as unreviewable, and the stage-1 filter is unforgiving.

## Double-anonymous supplementary rules (Regular and Application papers)

```text
[No identity]   no authors, affiliations, acknowledgements, grants, cluster paths, or repo owners in
                the appendix or the review-time artifact; anonymize the tool/solver name
[Anonymized links] the artifact link points at an anonymizing host, not a personal repo or tool site
[Clean archive]  no .git history, .DS_Store, credentials, caches, or large irrelevant files
[Opens clean]    verify the archive unpacks and the README orients a reviewer in minutes on a fresh
                machine (the AEC smoke test mirrors this)
```

Tool and Industrial papers are not anonymized, so their supplementary material may name the tool —
but should still be clean and self-orienting.

## Appendix architecture

- Order appendix sections to mirror the paper: main-theorem proof first, then lemma proofs, then full
  benchmark tables, then extra experiments — reviewers navigate by the claim, not by page number.
- Keep each appendix section referenced from the body at least once; orphaned material is invisible
  under discretionary reading.
- Confirm on the current CFP that appendices are inside the same PDF (not a separate upload) and that
  they do not count against the limit — this is the CAV norm but re-verify.

## Vignette: splitting a technique-plus-tool paper

A Regular Paper with one main soundness theorem, three lemmas, and a large benchmark study: the body
keeps the problem, the technique, the main theorem with its proof idea, the lemma statements, and the
headline cactus/scatter comparison with the resource limits and the soundness cross-check; the
appendix holds the full proofs; the artifact holds the pinned benchmark set, the per-instance logs,
the seeds, the proof witnesses with a checker, and the reproduction scripts. Nothing decision-critical
lives only in unread material, because the stage-1 reviewers judge from the body.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] anything decision-critical outside the body? <none / move: what>
[Page limit] body within the category limit? appendix marked and referenced? yes/no
[Anonymity] appendix + review artifact clean of identity (Regular/Application)? passed/issues
[Body dependency] <what a reviewer can decide without opening the appendix/artifact>
```
