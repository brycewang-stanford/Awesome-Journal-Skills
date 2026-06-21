---
name: revedres-revision
description: Use when an editor/reviewer decision letter arrives on a Review of Educational Research (RER) review or meta-analysis and you must plan the revision and response. Turns the letter into action and a point-by-point reply; it does not run the submission preflight (revedres-submission) or re-architect the framework from scratch (revedres-organizing-framework).
---

# Revision (revedres-revision)

## When to trigger

- An RER decision letter arrived (major/minor revision, or reject-and-resubmit)
- You must convert masked reviewer comments into a revision plan and a response letter
- Reviewers ask for a wider search, more coding detail, or stronger robustness
- You need to decide which requests to adopt and which to push back on, with evidence

## Read the decision the way RER editors mean it

RER reviews are refereed against rigor of the synthesis *and* rigor of the review process. Most revision requests fall into recognizable buckets — diagnose each before drafting.

| Reviewer request | What it really demands | Skill to revisit |
|---|---|---|
| "Expand/justify the search" | a more exhaustive or better-documented search; updated PRISMA | `revedres-literature-synthesis` |
| "This reads as a summary" | a stronger, more reconciling organizing framework | `revedres-organizing-framework` |
| "Address heterogeneity / bias" | I², moderators, funnel/Egger, sensitivity analyses | `revedres-comprehensiveness-and-balance` |
| "Coding reliability unclear" | reported κ/ICC and a shared codebook | `revedres-transparency-and-reproducibility` |
| "You vote-count conflicting work" | weigh by estimand + design; steelman camps | `revedres-comprehensiveness-and-balance` |
| "Over-reliance on your own work" | re-balance citations identity-blind | `revedres-comprehensiveness-and-balance` |
| "Tighten / APA / abstract" | prose, APA 7, ≤150-word abstract | `revedres-writing-style` |

## How to revise so the second round is clean

1. **Triage the whole letter first.** Group comments by theme (search, framework, analysis, transparency, writing) and by editor vs. reviewer weight — the editor's summary signals what is decisive.
2. **Update the search if asked — and re-run the PRISMA flow.** An expanded search changes counts everywhere; propagate them through tables, the meta-analysis, and the prose.
3. **Strengthen, don't just defend.** Where a request improves the review (more robustness, clearer framework), do it; reviewers reward visible engagement.
4. **Push back with evidence, respectfully.** If a request is out of scope or methodologically wrong, decline with a reasoned, cited explanation — not silence.
5. **Keep changes traceable.** A point-by-point response: quote each comment, state the change, and cite the manuscript location (page/section). Provide a tracked-changes version if requested.

## Drafting the response letter

- **Open with gratitude and a short summary** of the main changes.
- **Point-by-point**, in the reviewers' order: comment → response → exact change + location.
- **Be specific**: "We added a PsycINFO + ProQuest Dissertations search (PRISMA updated: 412→468 included); see Table 2 and Figure 1."
- **Flag any protocol deviations** the revision introduces, and justify them.
- **Stay calm and collegial** even with a harsh review — the editor is the audience.

## Checklist

- [ ] Whole letter triaged by theme and by editor/reviewer weight
- [ ] Search updated if requested; PRISMA counts re-run and propagated to tables/analysis/prose
- [ ] Heterogeneity / bias / sensitivity additions made where asked
- [ ] Coding reliability (κ/ICC) and codebook added/clarified if flagged
- [ ] Conflicting-evidence handling moved from vote-count to credibility-weighted
- [ ] Self-citation balance re-checked if raised
- [ ] APA 7 / abstract / prose tightened per comments
- [ ] Point-by-point response: comment → response → exact change + location, for every point
- [ ] Out-of-scope/incorrect requests declined with reasoned, cited justification
- [ ] Protocol deviations introduced by the revision flagged and justified

## Anti-patterns

- A defensive letter that argues with reviewers instead of improving the review
- Silently ignoring comments the author dislikes (reviewers re-check every one)
- Expanding the search but failing to update the PRISMA flow, tables, and pooled estimates
- "We have addressed this" with no location and no specific change described
- Adding robustness checks but burying contradictory results they surface
- Treating a reject-and-resubmit as a rejection rather than an invitation to rebuild and return

## Output format

```
【Decision】major | minor | reject-and-resubmit
【Triage】comments grouped by theme + editor/reviewer weight? Y/N
【Search updated】PRISMA re-run + propagated to tables/analysis/prose? Y/N
【Analysis adds】heterogeneity / bias / sensitivity added where asked? Y/N
【Transparency adds】κ/ICC + codebook clarified if flagged? Y/N
【Balance】conflict handling credibility-weighted; self-cites re-balanced? Y/N
【Response letter】point-by-point with exact change + location for every comment? Y/N
【Push-backs】out-of-scope/incorrect requests declined with cited reasons? Y/N
【Next step】→ revedres-submission (re-run preflight before resubmitting)
```
