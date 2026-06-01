---
name: jet-replication-and-data-policy
description: Handle the Journal of Economic Theory (JET) data/code expectations — JET has NO mandatory replication archive (consistent with its theorem-proof orientation); Elsevier encourages but does not require data sharing via Mendeley Data, a repository link, a Data in Brief co-submission, or a data statement. Focuses on reproducible computation when a paper has any, plus generative-AI disclosure. Light by design.
---

# Replication & Data Policy (jet-replication-and-data-policy)

## When to trigger

- Your JET paper includes numerical examples, simulations, or computed results and you want to share
  them well
- You are checking what JET requires for data/code at submission or acceptance
- You need to get the generative-AI disclosure right

## What JET actually requires

- **No mandatory data/code availability requirement.** Unlike empirical AEA / Econometric Society
  journals, JET has **no JAE-Data-Archive-style replication archive**. Because most papers are pure
  theory, data/code sharing is **encouraged, not required** — this is a deliberate, distinctive norm.
- As an **Elsevier** journal, JET **encourages** (does not mandate) sharing via:
  - a **linked data statement**,
  - deposit to a repository or **Mendeley Data**,
  - or a **Data in Brief** co-submission.
- **Generative-AI disclosure is required:** authors must declare any use of generative AI in manuscript
  preparation **at submission**. Reviewers and editors are **prohibited** from using generative-AI tools
  during evaluation.

## Reproducible-computation playbook (when the paper has computation)

Even though sharing is optional, make any numerical content reproducible — it strengthens the paper and
pre-empts referee doubt:

- [ ] One **master script** regenerates every reported number, table, and figure from scratch
- [ ] Environment pinned (`requirements.txt`, `Project.toml`/`Manifest.toml`, recorded toolbox versions)
- [ ] **Seeds set and reported** for any stochastic illustration
- [ ] A short README mapping each script to the theorem/figure it supports
- [ ] If shared, choose **one** channel (repo link / Mendeley Data / Data in Brief) and link it in the
      data statement

## Anti-patterns

- Assuming JET requires a formal replication package — it does not (verify wording on the live policy page)
- Reporting computed numbers no script can reproduce
- Omitting the generative-AI declaration at submission
- Treating the optional data statement as a substitute for a checkable proof — the proof carries the paper

## Output format

```
【Has computation?】yes/no  →  if no, data policy is effectively N/A (theory paper)
【Sharing】not required; chosen channel: repo | Mendeley Data | Data in Brief | data statement | none
【Reproducible】master script + pinned env + seeds + README? [Y/N]
【AI disclosure】declared at submission? [Y/N]
【Next】jet-submission
```
