---
name: jet-replication-and-data-policy
description: Use when handling the Journal of Economic Theory (JET) data/code expectations — JET is theorem-proof oriented, but Elsevier Option C applies when research data exist: deposit/cite/link data in a repository or explain why sharing is not possible. Focuses on reproducible computation when a paper has any, plus generative-AI disclosure. Light by design.
---

# Replication & Data Policy (jet-replication-and-data-policy)

## When to trigger

- Your JET paper includes numerical examples, simulations, or computed results and you want to share
  them well
- You are checking what JET requires for data/code at submission or acceptance
- You need to get the generative-AI disclosure right

## What JET actually requires

- **No journal-run replication archive.** Unlike empirical AEA / Econometric Society journals, JET has
  no JAE-Data-Archive-style replication archive. Most JET papers are pure theory, so the main
  reproducibility object is the proof and any supplementary appendix.
- **Elsevier Option C applies when research data exist.** Deposit research data in a relevant
  repository and cite/link it, or state why the data cannot be shared. Data statements are supported
  in the submission flow and appear with the published article.
- **Pure theorem papers still need a clear statement.** If there are no external research data and no
  computation, say so plainly. If there are numerical examples, simulations, or computer-assisted
  proof steps, make those artifacts reproducible and link/deposit them where appropriate.
- **Generative-AI disclosure is required:** authors must declare any use of generative AI in manuscript
  preparation **at submission**. Reviewers and editors are **prohibited** from using generative-AI tools
  during evaluation.

## Reproducible-computation playbook (when the paper has computation)

JET's Option C rule is data-focused, but for a theory paper any numerical content should still be
reproducible because it strengthens the paper and pre-empts referee doubt:

- [ ] One **master script** regenerates every reported number, table, and figure from scratch
- [ ] Environment pinned (`requirements.txt`, `Project.toml`/`Manifest.toml`, recorded toolbox versions)
- [ ] **Seeds set and reported** for any stochastic illustration
- [ ] A short README mapping each script to the theorem/figure it supports
- [ ] If shared, choose **one** channel (repo link / Mendeley Data / Data in Brief) and link it in the
      data statement

## What to package, by content type

| Computational content in the paper | Artifact worth sharing | Channel that fits |
|---|---|---|
| Symbolic verification of closed forms (e.g., checking eq. (7) of a screening model) | one SymPy/Mathematica script per theorem | repo link in the data statement |
| Counterexample found by search | the search code plus a certificate script confirming the final example violates the conclusion | repo; the certificate logic also goes in the paper |
| Computed equilibria (e.g., a numerical fixed point for a dynamic-contract example) | solver script with tolerances and pinned environment | repo or Mendeley Data |
| Experimental/empirical test of the theory (rare at JET) | data, cleaning, and analysis scripts | repository / Mendeley Data / Data in Brief, with Option C statement |
| Pure theory, no computation | no archive to manufacture | no-data statement |

## Supplementary-appendix culture (the theory analogue of replication)

- At a theorem-proof journal, the unit of "replication" is the **omitted proof**, not a dataset.
  Long technical arguments go to an online appendix / supplementary file the referee can read.
- Make the supplementary appendix **self-contained in notation** and citable by numbered
  cross-references from the main text (e.g., "Appendix S.2"), so checking it never requires
  re-deriving the body.
- If any proof step is **computer-assisted** — exhaustive finite-case checking, interval
  arithmetic, symbolic simplification — say so inside the proof and ship the checker; the step is
  only as credible as a referee's ability to re-run it.
- Where the proofs live (in-PDF appendix vs separate supplementary file) varies; confirm against
  the journal's current author guidelines before splitting files.

## Companion README template

```text
README — companion code for "<title>" (JET submission)
verify_thm2_bound.py     → re-derives eq. (7)–(9); confirms the Theorem 2 bound is attained (Example 1)
search_counterexample.jl → finds the Example 3 economy; seed 20250114; runtime < 1 min
check_thm4_cases.py      → exhaustive check of the 12 finite cases cited in Appendix B, Step 3
env: requirements.txt / Manifest.toml (pinned)
Every reported number in the paper appears in the output of exactly one script above.
```

## Anti-patterns

- Assuming JET has a journal-run replication archive — it does not
- Treating Option C as optional when the manuscript uses shareable research data
- Reporting computed numbers no script can reproduce
- Omitting the generative-AI declaration at submission
- Treating the optional data statement as a substitute for a checkable proof — the proof carries the paper

## Output format

```
【Has data/computation?】none / data / computation / both
【Option C】repository citation/link, or no-data/cannot-share statement? [Y/N]
【Reproducible】master script + pinned env + seeds + README? [Y/N]
【AI disclosure】declared at submission? [Y/N]
【Next】jet-submission
```
