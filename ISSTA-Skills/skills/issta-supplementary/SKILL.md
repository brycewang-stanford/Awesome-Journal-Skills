---
name: issta-supplementary
description: Use when deciding what lives in the ISSTA 18-page body versus the artifact and any appendix, covering the no-unlimited-appendix reality, what reviewers will and will not open, splitting a testing/analysis paper between body and package, anonymity of supplementary material, and keeping decision-critical evidence inside the reviewed pages.
---

# ISSTA Supplementary

Use this when deciding where each piece of content belongs. ISSTA's 18-page limit counts appendices
against the total, so there is no unlimited appendix to absorb overflow: the body must stand on its
own, and the artifact — not a separate PDF supplement — is where extra material goes. Reopen the
current call to confirm whether any in-PDF appendix or separate upload is permitted this cycle.

## The split rule

- Everything decision-critical lives inside the 18 pages: the threat model, the technique, the
  evaluation design, the headline results, and the threats to validity. If a reviewer needs it to
  judge the paper, it cannot live only in the artifact.
- The artifact carries what supports but does not replace the argument: the full tool, complete
  per-subject tables, extra configurations, raw logs, and regeneration scripts.
- Do not hide core method steps or primary results in an appendix or the artifact to make the body
  fit. Reviewers grade what is in the reviewed pages; buried evidence is invisible evidence.
- Because appendix pages count against 18, a long appendix competes directly with the body. Prefer
  moving detail to the artifact over spending page budget on it.

## What reviewers open, and what they do not

| Content | Where it belongs | Reviewer attention |
|---|---|---|
| Technique definition, threat model | Body | Read closely — graded for soundness |
| Headline results + statistics | Body | Read closely — graded for evaluation |
| Threats to validity | Body | Expected; its absence is noticed |
| Full per-subject result tables | Artifact | Skimmed if a body claim is contested |
| Raw fuzzing/analysis logs | Artifact | Rarely opened; ship for completeness |
| The runnable tool | Artifact (evaluated separately) | Run by artifact evaluators, not always by PC |

Assume a PC reviewer reads the 18 pages and dips into the artifact only to resolve a doubt. Design
the body so no such dip is *required* to accept the paper.

## Anonymity of supplementary material

- Keep the review-time artifact double-anonymous: no repository owner, commit authors, container
  labels, institution paths, or acknowledgements.
- Verify archives open on a clean machine with no credentials, caches, or OS metadata baked in.
- An anonymized public mirror or an anonymous upload is fine; a link to your named GitHub is a
  double-anonymous violation.

## Vignette: splitting a static-analysis paper

A submission presenting a new taint-analysis with a soundness argument and a large evaluation: the
body keeps the analysis rules, the soundness sketch, the evaluation protocol, and the two
decision-critical result tables (precision/recall against ground truth, and a comparison to one
established baseline); the artifact holds the full implementation, the complete per-benchmark
tables, alternative sensitivity configurations, and the scripts that regenerate every table.
Nothing needed to accept the paper lives only in the artifact, because artifact inspection by the
PC is discretionary.

```text
Body (<= 18 pp)          Artifact
- analysis rules          - full analyzer implementation
- soundness sketch        - complete per-benchmark tables
- evaluation protocol     - extra sensitivity configs
- 2 headline tables       - table-regeneration scripts + raw logs
- threats to validity     - pinned subjects (SHAs)
```

## Output format

```text
[Split status] Ready / Needs fixes / Not ready
[Body carries] <decision-critical items present in the 18 pages>
[Artifact carries] <supporting material>
[Page-budget risk] <appendix competing with the body?>
[Anonymity checks] passed / issues
[Main-paper dependency] <what breaks if the artifact is never opened>
```
