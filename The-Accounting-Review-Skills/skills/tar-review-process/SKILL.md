---
name: tar-review-process
description: Use when understanding how The Accounting Review (TAR) review and decisions work, or when reading a TAR decision letter — the editor routing, double-blind two-reviewer model, decision types, and post-publication integrity rules. Explains and interprets the process; it does not draft the revision and response (tar-rebuttal).
---

# Understanding TAR Review (tar-review-process)

## When to trigger

- You want to set realistic expectations before or after submitting to TAR
- A decision letter arrived and you need to read its signal before responding
- You are unsure who the Senior Editor / Lead Editor / Editor / Ad hoc Editor are in the process
- You want to know what "anonymity," "data authenticity," or "Expression of Concern" mean for you

## How TAR routes a manuscript

TAR uses a **tiered editor structure** distinct from INFORMS-style permanent departmental
area-editors:

- A single **Senior Editor** oversees the whole process — **Mohan Venkatachalam (Duke, Fuqua),
  sitting Senior Editor since June 2026** (succeeding Kathryn Kadous, Emory; verify the current masthead).
- Named **Lead Editors** (e.g., Brian Mittendorf, Edward L. Maydew, Kristina M. Rennekamp, Paul
  Hribar) share Senior-Editor responsibilities: assigning editors, issuing decision letters, handling
  **desk rejections** and **appeals**.
- A bench of roughly two dozen standing **Editors** handle manuscripts in their areas (roster 待核实).
- **Ad hoc Editors** are appointed for specialized topics/methods a manuscript requires.

A submission may be **desk-rejected** by a Lead Editor before review if fit or contribution is
insufficient. Manuscripts that pass initial screening go to an editor and a **minimum of two
reviewers** under **double-blind** review — protecting the anonymity of both authors and reviewers is
described as one of the most critical goals of the process. (Among AAA journals, only the Journal of
Financial Reporting uses single-blind review; TAR is double-blind.)

## Reading the decision

- **Desk reject:** fit/contribution/identification judged insufficient without external review — re-aim
  the paper (often a section or specialist journal) rather than appeal reflexively.
- **Reject after review:** the editor and reviewers see a fundamental flaw — usually identification,
  contribution, or measurement. Salvage requires a different study, not cosmetic edits.
- **Revise and resubmit (R&R):** the developmental, multi-round path to publication. Read the
  **editor's letter first** — it prioritizes which reviewer points are decision-critical.
- Distinguish **decision-critical** demands (identification, contribution, a needed test) from
  **discretionary** ones; the editor's framing tells you which is which.

## Integrity & post-publication rules to know

- **Plagiarism screening** and **anonymity** apply throughout; do not contact reviewers or de-anonymize.
- **Data authenticity** is enforced — be ready to provide the data description and processing code if
  the editor or reviewers ask (see `tar-data-analysis`).
- **Expression of Concern:** AAA may issue one if an institutional research-integrity investigation
  **exceeds 180 days** — a formalized post-publication integrity step worth understanding before any
  question arises.

## What you control

- A clean, anonymized, reproducible submission lowers desk-reject risk.
- Suggesting fitting, non-conflicted area keywords helps route you to the right editor.
- Mind the **8 first-round submissions / 24 months** cap when timing submissions (R&Rs are exempt).

## Checklist

- [ ] You know whether the letter is desk reject, reject, or R&R
- [ ] You read the **editor's** letter before the individual reviews
- [ ] Decision-critical vs. discretionary comments are separated
- [ ] Anonymity is preserved (no reviewer contact, no de-anonymization)
- [ ] The data-authenticity/code package is ready if requested
- [ ] You understand the integrity rules (screening, Expression of Concern at 180 days)

## Anti-patterns

- **Appealing a desk reject reflexively** instead of re-aiming the paper.
- **Treating every reviewer point as equal** and missing the editor's priorities.
- **Reading reviews before the editor's letter** and mis-weighting the demands.
- **De-anonymizing** by guessing reviewers or contacting the editor informally.
- **Confusing reject with R&R** and over- or under-investing in the response.

## Output format

```
【Decision type】desk reject / reject / R&R
【Editor priorities (from the letter)】1... 2... 3...
【Decision-critical vs discretionary】critical: ... ; discretionary: ...
【Routing】Senior/Lead/Editor/Ad hoc — area fit ...
【Integrity items】data-authenticity ready? anonymity preserved? yes/no
【Next step】on R&R → tar-rebuttal; on reject → tar-topic-selection / re-aim
```
