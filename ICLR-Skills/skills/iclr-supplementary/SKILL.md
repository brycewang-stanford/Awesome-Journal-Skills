---
name: iclr-supplementary
description: Use when organizing ICLR appendices, supplementary files, anonymous code/data, revised PDFs, private links, and discussion-period updates under OpenReview rules. Use when deciding what stays in the main text versus the appendix, how to label a discussion-period revision so reviewers find changes fast, or how to package anonymous artifacts that remain part of the permanent public record after acceptance.
---

# ICLR Supplementary

Use this when deciding what belongs in the main PDF, appendix, supplementary files, or private
discussion-period links. The goal is to make extra evidence easy to find without hiding the paper's
core argument outside the main text.

## Structure

- Keep central method, claims, and minimum evidence in the main text.
- Put derivations, extended ablations, robustness, extra qualitative examples, hyperparameters,
  model cards, dataset cards, and ethics details in the appendix.
- Use supplementary files for code, data, large tables, logs, demos, and artifacts that do not fit
  cleanly in the PDF.
- Include a one-page appendix map at the start when the appendix is long.
- Label discussion-period revisions explicitly so reviewers can find changes quickly.

## Anonymity and access

- Remove author names, institutions, usernames, Git remotes, file paths, cloud buckets, and license
  headers that identify the team.
- Avoid links that reveal visitors or owner accounts. Prefer anonymized repositories, static files,
  or private OpenReview-visible links permitted by the current guide.
- Make supplementary filenames descriptive but neutral.
- If code cannot be released, state the legal or privacy constraint and provide a smaller
  reproducibility substitute.

## Main-text versus appendix placement

ICLR's single-track format means the main PDF carries the argument and appendices come after
references with generous room. The risk is burying decisive evidence where a time-pressed reviewer
never looks, while padding the appendix with material that proves nothing.

| Content | Belongs in | Why |
| --- | --- | --- |
| Central claim and its key result | Main text | Reviewers may not open the appendix |
| Full proof / extended derivation | Appendix | Needed for rigor, not for the headline |
| Hyperparameters, model/dataset cards | Appendix | Reference material, not argument |
| Code, logs, large tables, checkpoints | Supplementary ZIP | Too big or interactive for the PDF |
| Decisive ablation a claim depends on | Main text | Moving it weakens the narrative |

## Worked vignette

A generative-model paper hides its only fairness-of-comparison ablation in Appendix G, so a reviewer
concludes the headline gain is unsupported. The fix: promote a compact version into the main text
near the claim, leave the full grid in the appendix, and add an appendix map. During discussion the
authors upload a revision and label the changelog so the relocation is obvious.

## Reviewer-pushback patterns

- "Key evidence is buried." Promote it; an appendix map is not a substitute for main-text placement.
- "Cannot tell what changed in the revision." Add a dated changelog at the top of the revised PDF.
- "Supplement leaks identity." Re-check file paths, license headers, and remotes before upload.

## Output format

```text
[Supplement plan] PDF appendix / ZIP / anonymous repo / private link / no supplement
[Main-text dependencies] <claims that must move back into main text>
[Reviewer navigation] <appendix map and file names>
[Anonymity risks] <paths, metadata, links, licenses>
[Discussion update note] <short changelog if revised>
```

