# ICALP Submission-Readiness Code Adapter

This directory routes ICALP authors to the repository-level shared tooling. It stays deliberately
thin: ICALP-specific *policy* (the two-track structure, the single February deadline, lightweight
double-blind review, the 15-page + full-version norm, LIPIcs open access) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared kits
so packs do not carry diverging copies.

Because ICALP is a **pure-theory venue with no artifact-evaluation track**, the "code" here is not a
reproducibility harness for a system — it is a small set of checks on the *manuscript* (anonymity,
format, page budget) and a discipline for mapping every claim to a complete proof.

## Shared kits

- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  — generic pre-submission checklist; adapt the "artifact" rows to the **full-version / appendix**
  rows described in [`../../skills/icalp-supplementary/SKILL.md`](../../skills/icalp-supplementary/SKILL.md).
- [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic response scaffolding; adapt it to the **Track B rebuttal** in
  [`../../skills/icalp-author-response/SKILL.md`](../../skills/icalp-author-response/SKILL.md).
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — use **only** the anonymity/self-reference rows; ignore the runnable-artifact rows, which do not
  apply at ICALP.

## Typical use for an ICALP submission

```bash
# Lightweight double-blind + format sweep on the submission PDF
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'          # scrub identifying metadata
pdftotext paper.pdf - | grep -nEi 'acknowledg|thanks|grant|@[a-z0-9.]+\.(edu|ac\.[a-z]+)' | head
pdftotext paper.pdf - | grep -nEi 'in our (previous|earlier) (work|paper)|we .* \[[0-9]+\]' | head
# page budget: main text (excluding references + clearly labelled appendix) must be <= 15 pages
```

Treat these as mechanical smoke tests only. Venue policy still comes from the current ICALP call and
the ICALP skills for submission, supplementary split, and camera-ready.

## ICALP-specific checks the generic tooling cannot make

- **Every theorem maps to a complete proof.** The 15-page body may sketch, but each headline claim
  must have a full, checkable proof somewhere the PC can read it — the labelled appendix and/or an
  arXiv/ECCC full version (`../../skills/icalp-reproducibility/SKILL.md`).
- **Self-reference is third-person under double-blind.** Not "in our previous work [12]" but "in the
  work of [12]"; acknowledgements and grant numbers are removed until camera-ready
  (`../../skills/icalp-submission/SKILL.md`).
- **The appendix is decision-support, not decision-critical.** Reviewers judge on the 15 body pages;
  proofs banished entirely to an unread appendix are a scored risk, not a safe overflow
  (`../../skills/icalp-supplementary/SKILL.md`).
- **The right track.** An algorithms/complexity result goes to **Track A**; an automata/logic/
  semantics result goes to **Track B**, which alone carries a rebuttal — misrouting wastes a full
  annual cycle (`../../skills/icalp-topic-selection/SKILL.md`).

This is not an ML-artifact or econometrics kit, and ICALP evidence is not a leaderboard score or a
regression table: do not import Docker reproducibility harnesses or DiD notebooks here.
