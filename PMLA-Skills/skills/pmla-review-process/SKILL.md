---
name: pmla-review-process
description: Use to understand how PMLA (Publications of the Modern Language Association) evaluates an essay — anonymous (blind) review with at least two reviewers, the Editorial Board's final decision, the Advisory Committee's reports, MLA-membership eligibility, and how anonymity is maintained. Sets expectations and shapes the essay to survive review; it does not contact editors.
---

# Review Process (pmla-review-process)

Knowing how PMLA screens and decides lets you pre-empt the failure modes before submitting. PMLA is
**anonymous (blind)**: until a final decision is reached, the author's name is not made known to
readers, to Editorial Board members, or to the editor.

## When to trigger

- Before submitting, to stress-test the essay against PMLA's standards
- Understanding what reviewers and the Editorial Board weigh
- Interpreting a decision letter and setting expectations
- Confirming eligibility (MLA membership; not previously published; not under review elsewhere)

## How PMLA review works

1. **Eligibility first.** The author (and all coauthors) must be **members of the MLA**. The essay
   must not have been **previously published in any language** or be **under consideration elsewhere**;
   a **revised version of a manuscript previously submitted to PMLA is not considered**.
2. **Anonymous (blind) review.** Reviewers do not know the author; the author's name is concealed from
   readers, the Editorial Board, and the editor until a final decision. Reviewers, board members, or
   the editor **recuse** themselves if they suspect they know the author.
3. **At least two reviewers.** Each eligible essay goes to **at least two** reviewers (often three),
   who are asked for thoughtful, substantive reports.
4. **Editorial Board decides.** Essays recommended by reviewers go to the **Editorial Board**, which
   meets periodically with the editor to **make final decisions**. The **Advisory Committee** reports
   on submitted articles.
5. **Generalist standard.** Decisions favor essays that address a **significant problem**, draw out
   their implications, and engage a **broad readership** — newer scholars publish alongside
   established ones through the blind process.

## Shape the essay to pass

- Make the significance explicit for a generalist (avoids "of interest only to specialists").
- Engage the relevant criticism, including across periods/fields (see `pmla-scholarly-positioning`).
- Ground every claim in close reading the reviewers can check (see `pmla-textual-evidence-and-close-reading`).
- Anonymize thoroughly (see `pmla-submission`) — a self-identifying reference can compromise blind review.
- Disclose any AI-tool-generated content at submission.

## Anti-patterns

- Submitting a narrow specialist piece to a generalist journal
- Ignoring obvious related criticism
- Leaving self-identifying references that break anonymity
- Submitting while the essay is under review elsewhere, or resubmitting a previously declined PMLA essay
- Forgetting the MLA-membership requirement for every author


## Review-risk pass for PMLA

Run this as a concrete capability pass. First lock the object corpus, interpretive intervention, field conversation, and scholarly stakes; then test whether the manuscript addresses humanities reviewers who expect a field-crossing literary or language-studies intervention with careful textual evidence.

- **Primary move:** Turn likely reviewer objections into a ledger with response evidence, manuscript location, and the decision-maker who must be convinced first.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Critical Inquiry for theory-forward essays, New Literary History for literary theory/history, discipline journals for narrower archive work; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Eligibility】MLA member(s)? unpublished? not under review elsewhere? [Y/N]
【Significance】general enough for the membership? [Y/N]
【Criticism engaged】incl. cross-field? [Y/N]
【Reading】claims grounded in checkable close reading? [Y/N]
【Anonymized】self-identifying references removed? [Y/N]
【Realistic outcome】reject / revise / (rare) accept
【Next】pmla-submission (or pmla-revision-and-response if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review process, Editorial Board / Advisory Committee, eligibility, anonymity
