---
name: iclr-supplementary
description: Use when organizing ICLR appendices, supplementary files, anonymous code/data, revised PDFs, private links, and discussion-period updates under OpenReview rules.
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

## Output format

```text
[Supplement plan] PDF appendix / ZIP / anonymous repo / private link / no supplement
[Main-text dependencies] <claims that must move back into main text>
[Reviewer navigation] <appendix map and file names>
[Anonymity risks] <paths, metadata, links, licenses>
[Discussion update note] <short changelog if revised>
```

