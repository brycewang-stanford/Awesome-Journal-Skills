---
name: jbes-review-process
description: Use when planning around the Journal of Business & Economic Statistics (JBES) peer-review process — the multi-Co-Editor model, what method referees scrutinize, and the discussion-paper tradition. Sets expectations; it does not draft the response letter (see jbes-rebuttal).
---

# Review Process (jbes-review-process)

## When to trigger

- You want to understand how JBES handles a submission before you send it
- You are deciding how to frame the cover letter for a multi-Co-Editor journal
- You wonder whether your paper could be an invited discussion paper
- You need to anticipate what method referees will attack

## How JBES review is structured

JBES is run by a **rotating panel of Joint Editors with no single Editor-in-Chief**. The confirmed
2022-2024 term was held by **Atsushi Inoue** and **Ivan Canay**; current Joint Editors are **Yingying
Fan**, **Michael Kolesár**, and **Dacheng Xiu** per the official T&F search snippet. Practical
consequence: unlike a single-Editor-in-Chief journal, **field fit and cover-letter targeting** matter,
because a handling Joint Editor whose expertise matches your method is more likely to evaluate and route
it well. Submission platform, review-anonymity model, and timelines are live-page checks; do not assert
them from this pack alone.

## What method referees scrutinize

Because JBES is a **methods-with-empirics** journal owned by the ASA, referees are method experts who interrogate, in order: (1) **statistical validity** — are the assumptions, asymptotics, and inference correct and as general as claimed? (2) **empirical relevance** — is there a substantive application, and does the method genuinely help it? (3) **reproducibility** — can the simulation and empirical results be regenerated from the supplement? A paper strong on only one axis is vulnerable.

## The discussion-paper tradition

JBES has a long-standing association with **invited discussion papers and published comments/rejoinders**
(a hallmark shared with leading statistics journals such as JASA). Treat this as a strong convention
rather than a submission guarantee: a sufficiently novel and broadly relevant method may be handled as a
discussion paper, which shapes how the contribution should be pitched.

## Checklist

- [ ] Cover letter targets the method to a plausible handling Co-Editor's expertise
- [ ] The three referee axes (validity / relevance / reproducibility) each addressed
- [ ] No claims about platform, review-anonymity model, or timeline without checking live T&F instructions
- [ ] Considered whether the paper fits the discussion-paper format
- [ ] ASA editorial/ethics norms (not AEA Data Editor norms) assumed

## Anti-patterns

- Assuming a single Editor-in-Chief and writing a generic cover letter
- Asserting a blinding model or timeline the official page does not confirm
- Submitting strong theory with no application (or vice versa) to a methods-with-empirics journal
- Expecting an AEA-style mandatory pre-publication replication check; JBES follows ASA policy


## Review-risk pass for Journal of Business & Economic Statistics

Run this as a concrete capability pass. First lock the statistical estimand, identification/simulation evidence, empirical illustration, and reproducibility path; then test whether the manuscript addresses econometrics/statistics reviewers who expect methodological credibility plus a business or economic use case.

- **Primary move:** Turn likely reviewer objections into a ledger with response evidence, manuscript location, and the decision-maker who must be convinced first.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Journal of Econometrics for theory-heavy methods, Econometric Theory for proof-first work, Quantitative Economics for economics-theory methods; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Editor model】multi-Co-Editor; targeted handling editor: ...
【Three axes】validity / relevance / reproducibility addressed? [Y/N each]
【Live-page items】platform / review model / timeline checked if relevant? [Y/N]
【Discussion paper?】plausible fit considered? [Y/N]
【Next step】jbes-submission
```
