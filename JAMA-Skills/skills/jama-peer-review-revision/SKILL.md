---
name: jama-peer-review-revision
description: Use when responding to JAMA editor and reviewer comments after a revise decision, including the statistical-review queries. Structures the point-by-point response and revision; it does NOT fabricate new analyses or overstate changes.
---

# Peer Review & Revision (jama-peer-review-revision)

## When to trigger

- A decision letter arrives: major/minor revision (or a reject-with-encouragement)
- Reviewer or editor comments need a structured, point-by-point reply
- The statistical reviewer has raised analysis questions
- You must revise the manuscript before writing the response — not after

## How JAMA review works (durable shape)

- Editorial screening first; manuscripts that pass go to **external peer review**.
- JAMA applies **dedicated statistical review** to manuscripts under serious consideration — expect detailed methods/analysis queries.
- Decisions typically come with one or more revision rounds; address every point.

## Response-letter structure

1. **Open with thanks** and a one-paragraph summary of the main changes.
2. **Reproduce each comment verbatim**, then respond beneath it.
3. For each point: **state the change, quote the new manuscript text, and give the page/line**. If you disagree, do so respectfully with evidence — do not ignore a comment.
4. Group editor vs reviewer comments; number them (Reviewer 1, Comment 1.1 …).
5. Keep the manuscript and the letter perfectly consistent (numbers, claims, wording).
6. Provide a **tracked-changes** manuscript alongside a clean copy.

## Handling common JAMA comment types

| Comment type                                          | Response approach                                            |
|-------------------------------------------------------|-------------------------------------------------------------|
| "Report effect sizes with CIs, not p-values"          | Add estimates + 95% CIs throughout; confirm in the letter   |
| "Was this outcome pre-specified?"                     | Cite the protocol/registry; relabel post hoc as exploratory |
| "Analysis should be intention-to-treat"               | Re-run ITT as primary; move per-protocol to sensitivity     |
| "Address multiplicity"                                | Add/justify the correction; downgrade unadjusted subgroups  |
| "Conclusions overstate the data (spin)"               | Rewrite to the primary outcome; bound the claim             |
| "Reporting incomplete (CONSORT/PRISMA item X)"        | Add the item; update the checklist locations                |
| "Generalizability / limitations"                      | Strengthen the limitations paragraph honestly               |
| "Registration timing"                                 | State the facts transparently; do not obscure               |

## Checklist

- [ ] Manuscript revised first; letter written from the revised version
- [ ] Every comment reproduced and answered (none skipped)
- [ ] Each response cites new text with page/line
- [ ] Statistical-reviewer points fully resolved (CIs, ITT, multiplicity, missing data)
- [ ] No spin reintroduced; conclusions still bounded by the primary outcome
- [ ] Reporting checklist updated to match the revised text
- [ ] Tracked-changes + clean copies prepared
- [ ] Letter and manuscript numerically consistent

## Anti-patterns

- Writing the response before actually revising the manuscript
- Silently skipping an uncomfortable comment
- Claiming a change was made that the manuscript does not reflect
- Defensive or dismissive tone toward reviewers
- Running new post hoc analyses and presenting them as confirmatory
- Reintroducing spin while "addressing" the spin comment
- Leaving the checklist out of sync with the revised text


## Operating pass for JAMA

Run this as a concrete capability pass. First lock the clinical question, patient population, estimand or endpoint, safety/ethics issue, and reporting checklist; then test whether the manuscript addresses clinical reviewers who ask whether the evidence changes patient care, policy, or medical decision-making while satisfying reporting standards.

- **Primary move:** Return a claim-evidence-risk ledger; every recommendation must point to a manuscript location or missing artifact.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against NEJM for field-changing clinical medicine, Lancet for global-health breadth, specialty journals for narrower clinical domains; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Decision】major / minor revision / reject-with-encouragement
【Comments addressed】X of X (none skipped)
【Statistical-review points resolved】yes / remaining: ...
【New text cited with page/line】yes / no
【Spin reintroduced?】no / fixed: ...
【Checklist updated】yes / no
【Files ready】tracked + clean + point-by-point letter
```
