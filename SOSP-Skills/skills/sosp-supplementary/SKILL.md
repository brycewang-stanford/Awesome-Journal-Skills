---
name: sosp-supplementary
description: Use when deciding what belongs in a SOSP supplementary document versus the 12-page paper, packaging proofs, extended analyses, and methodological detail as a separate anonymized upload, and keeping review-critical evidence out of material reviewers are not obligated to read.
---

# SOSP Supplementary Material

Use this while splitting content between the SOSP paper and its optional supplement.
The CFP (2026 cycle, checked 2026-07-08 via `sigops.org/s/conferences/sosp/2026/cfp.html`
and the `sosp26.hotcrp.com` submission form) allows supplementary material as a
**separate document** uploaded alongside the anonymized PDF. Its charter is narrow:
content that supports the paper but is **not critical to evaluating it** — formal
proofs, extra data analyses, methodological detail. Reviewers may open it; nothing
obligates them to.

## The governing asymmetry

The paper must stand alone inside its 12 pages of technical content. The supplement
can only *deepen* an argument the paper already completes — it cannot *carry* one.
This produces a simple sorting rule for every candidate paragraph, proof, and figure:

| Content | Where it lives | Why |
|---|---|---|
| The invariant your correctness claim rests on, stated and argued | Paper | Review-critical; a reviewer who skips the supplement must still be convinced |
| The full mechanized or manual proof of that invariant | Supplement | Depth behind a claim the paper already supports with a proof sketch |
| Headline performance results and their experimental setup | Paper | Claims and their primary evidence are inseparable |
| Per-workload breakdowns, extra hardware configurations, sensitivity sweeps | Supplement | Corroboration, not the load-bearing evidence |
| Anything a reviewer needs to check soundness of the method | Paper | "Not critical to evaluating the paper" excludes it from the supplement by definition |
| Pseudocode too long for the paper, trace-format specifications | Supplement | Methodological detail |

The classic failure: page pressure at T-minus-two-weeks pushes the failure-recovery
evaluation into the supplement, a reviewer never opens it, and the review reads "no
failure experiments." During SOSP's response phase you may point back to the
supplement — it was part of the submission — but a pointer in a sub-500-word response
is a weak substitute for evidence on the reviewed pages.

## Anonymity extends to the supplement

The supplement is reviewed under the same double-blind rules as the paper. It is the
more dangerous document because it is assembled last and checked least:

- Appendix LaTeX often still carries `\author` blocks, acknowledgment stubs, or grant
  numbers from an earlier tech-report build.
- Extended data tables can leak cluster hostnames, internal project codenames, or
  usernames embedded in file paths.
- PDF metadata is regenerated at every compile; scrub the supplement's, not only the
  paper's.

```bash
# Run the same leak sweep on the supplement as on the paper
pdfinfo supplement.pdf | grep -iE '^(author|creator)'
pdftotext supplement.pdf - | grep -inE 'acknowledg|grant|@[a-z-]+\.(edu|com)|/home/[a-z]|corp\.' | head
# Cross-check: every paper reference to the supplement resolves
pdftotext main.pdf - | grep -oE 'supplement[a-z]* (§|Section |Appendix )?[A-Z0-9.]*' | sort -u
```

## Supplement, artifact, and appendix are three different objects

Teams routinely conflate three artifacts with different clocks and audiences:

1. **Supplementary document** — submitted with the paper in April, anonymized,
   read (maybe) by paper reviewers. Governed by this skill.
2. **Artifact package** — prepared after acceptance for the sysartifacts evaluation,
   non-anonymous, exercised by a separate committee (see `sosp-artifact-evaluation`).
   Do not burn April effort polishing container images no paper reviewer will run.
3. **Camera-ready appendix** — final papers get 13 pages (14 with shepherd approval),
   so some supplement content may graduate into the paper itself after acceptance
   (see `sosp-camera-ready`).

Plan the April supplement knowing routes 2 and 3 exist: its only job is to survive
review, not to be the archival record of everything you know.

## Structuring for a skimming reviewer

A SOSP reviewer opening the supplement is looking for one specific thing mid-review.
Optimize for that entry pattern:

- Open with a half-page **map**: each supplement section, one line on what it adds,
  and which paper section or claim it backs.
- Number supplement sections to continue or clearly reference the paper's numbering,
  and cite them from the paper precisely ("full proof in supplement §B.2"), never as
  a bare "see supplement."
- Keep each section self-contained enough to read without the neighboring ones; a
  reviewer chasing the proof of Invariant I2 should not need supplement §A first.

## Output format

```text
[Split audit] review-critical content found in supplement? <list or none>
[Paper -> supplement pointers] all resolve? <broken refs>
[Anonymity] supplement metadata + text sweep result
[Confusion check] AE-only material mistakenly built now? camera-ready graduation list?
[Map] supplement sections -> paper claims they back
[Fix order] <moves before the upload>
```
