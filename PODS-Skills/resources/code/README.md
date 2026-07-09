# ACM PODS Proof-Package Adapter

This directory routes PODS authors to the repository-level shared tooling. It stays deliberately
thin, and it is deliberately **not** a code-artifact kit: PODS is a database-**theory** symposium
with no systems artifact-evaluation track. PODS-specific *policy* (the multi-cycle calendar, the
PACMMOD PODS track, lightweight double-anonymous review, the revision/shepherd round, the proof
appendix and full-version-on-arXiv norm) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *scaffolding* lives in the shared
kits.

## Shared kits (adapt, do not import wholesale)

- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  — generic pre-submission checks; keep the format/anonymity/deadline items, drop anything that
  assumes a code artifact or benchmark run.
- [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — response scaffolding; adapt it to the PODS 48-hour rebuttal and the revision cover letter in
  [`../../skills/pods-author-response/SKILL.md`](../../skills/pods-author-response/SKILL.md).

There is intentionally **no** `check_repro_package.py`-style smoke checker here: a PODS submission
has no runnable package to smoke-test. The analogue is a human (or careful re-derivation) reading
the proof appendix end to end.

## The PODS "package" is the proof, not code

Replace the systems notion of an artifact with a **claim-to-proof matrix** and an anonymized proof
appendix:

```text
[Claim inventory]  every theorem/lemma/corollary in the body -> its full proof location
                   (body or appendix); no stated result without a complete proof somewhere
[Appendix]         complete proofs incorporated at submission (acmsmall appendix, unlimited length);
                   PODS forbids external/online appendices, so nothing lives off-paper
[Self-containment]  each proof states its assumptions, cites the exact prior lemma it uses, and
                   does not defer a key step to "the full version"
[Anonymity]        no author names, affiliations, acknowledgements, funding, or a named system/tool
                   anywhere in the paper or appendix (lightweight double-anonymous)
[Full version]     an arXiv full version prepared for camera-ready, DOI-linked to the PACMMOD paper
```

## PODS-specific checks the generic tooling cannot make

- **Every claim has a complete, self-contained proof.** A theorem whose proof is "omitted for space"
  or "in the full version" with no appendix proof is the classic PODS reject — the appendix is
  incorporated at submission precisely so reviewers can verify (`../../skills/pods-reproducibility/SKILL.md`).
- **The model and problem are pinned before the proof.** Definitions, the data/query model, the
  complexity measure, and the exact statement (data vs. combined complexity, worst-case vs.
  parameterized) are fixed so the bound is unambiguous (`../../skills/pods-writing-style/SKILL.md`).
- **Anonymity extends into the appendix and the rebuttal.** Lightweight double-anonymity means the
  proof appendix and the 48-hour rebuttal must not reveal authorship or link to an identifying
  homepage/preprint (`../../skills/pods-submission/SKILL.md`, `../../skills/pods-author-response/SKILL.md`).
- **The full-version handoff is a camera-ready task.** After acceptance, post the full version on
  arXiv and add the DOI link; this is the PODS analogue of a public artifact, not a badge
  (`../../skills/pods-camera-ready/SKILL.md`).

This is not a systems-DB artifact kit and not an ML-leaderboard kit: do not add a benchmark harness
or a reproducibility badge checklist here.
