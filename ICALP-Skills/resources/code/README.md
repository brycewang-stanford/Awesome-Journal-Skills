# ICALP Submission-Readiness Code Adapter

This directory routes ICALP authors to the repository-level shared tooling. It stays deliberately
thin: ICALP-specific *policy* (the two-track structure, the February deadline and the new Track B
September round, lightweight double-blind review, the no-page-limit full version whose first ten pages
must carry the paper, LIPIcs open access) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared kits
so packs do not carry diverging copies.

Because ICALP is a **pure-theory venue with no artifact-evaluation track**, the "code" here is not a
reproducibility harness for a system — it is a small set of checks on the *manuscript* (anonymity,
format, page budget) and a discipline for mapping every claim to a complete proof.

## Shared kits

- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../shared/submission-readiness/readiness-checklist.md)
  — generic pre-submission checklist; adapt the "artifact" rows to the **full-version / appendix**
  rows described in [`../../skills/icalp-supplementary/SKILL.md`](../../skills/icalp-supplementary/SKILL.md).
- [`../../../shared-resources/submission-readiness/response-to-referees.md`](../shared/submission-readiness/response-to-referees.md)
  — generic response scaffolding; adapt it to the **Track B rebuttal** in
  [`../../skills/icalp-author-response/SKILL.md`](../../skills/icalp-author-response/SKILL.md).
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../shared/ml-conference-methods/reproducibility-artifact-checklist.md)
  — use **only** the anonymity/self-reference rows; ignore the runnable-artifact rows, which do not
  apply at ICALP.

## Typical use for an ICALP submission

```bash
# Lightweight double-blind + format sweep on the submission PDF
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'          # scrub identifying metadata
pdftotext paper.pdf - | grep -nEi 'acknowledg|thanks|grant|@[a-z0-9.]+\.(edu|ac\.[a-z]+)' | head
pdftotext paper.pdf - | grep -nEi 'in our (previous|earlier) (work|paper)|we .* \[[0-9]+\]' | head
# no page limit (since ICALP 2026), but check the merits land within the first ten pages after the title page
pdftotext -f 2 -l 11 paper.pdf - | grep -nEi '^(theorem|main result)|we (prove|show|give)' | head
pdftotext paper.pdf - | grep -nEi 'ChatGPT|LLM|large language model|AI tool|Copilot' | head   # AI-use disclosure present if used?
```

Treat these as mechanical smoke tests only. Venue policy still comes from the current ICALP call and
the ICALP skills for submission, supplementary split, and camera-ready.

## ICALP-specific checks the generic tooling cannot make

- **Every theorem maps to a complete proof.** The first ten pages may sketch, but each headline
  claim must have a full, checkable proof somewhere the PC can read it — later in the submission
  (there is no page limit) and/or an arXiv/ECCC full version (`../../skills/icalp-reproducibility/SKILL.md`).
- **Self-reference is third-person under double-blind.** Not "in our previous work [12]" but "in the
  work of [12]"; acknowledgements and grant numbers are removed until camera-ready
  (`../../skills/icalp-submission/SKILL.md`).
- **Everything after page ten is decision-support, not decision-critical.** Only the abstract,
  references and the first ten pages after the title page are guaranteed a read; proofs banished
  entirely past that window are a scored risk, not a safe overflow
  (`../../skills/icalp-supplementary/SKILL.md`).
- **The right track.** An algorithms/complexity result goes to **Track A**; an automata/logic/
  semantics result goes to **Track B**, which carries a rebuttal (and, since ICALP 2027, a September
  round as well as the February one); Track A contacted authors only on correctness issues in ICALP
  2026 — misrouting wastes a cycle (`../../skills/icalp-topic-selection/SKILL.md`).

This is not an ML-artifact or econometrics kit, and ICALP evidence is not a leaderboard score or a
regression table: do not import Docker reproducibility harnesses or DiD notebooks here.
