---
name: restud-rebuttal
description: Use when a referee report or R&R has arrived for a The Review of Economic Studies (REStud) manuscript and a point-by-point response letter plus aligned manuscript revisions are needed. Structures the revision and the letter; does not redo the science from scratch.
---

# REStud Rebuttal (restud-rebuttal)

## When to trigger

- A decision letter with referee reports has arrived (R&R, or reject-and-resubmit)
- The user has a revised draft and needs the response letter
- The user is unsure which comments to concede, clarify, or push back on
- Multiple referees disagree and the response must reconcile them without contradiction

## REStud revision philosophy

REStud is known for **developing strong papers across rounds** with demanding referees. Treat the R&R as a collaboration, not a defense: the editor wants the paper to become publishable. The strongest response **revises the manuscript first, then writes the letter against the revised version** — never the other way around. Two REStud-specific facts to plan for: (1) referees are anonymous to you (the official guidelines do not ask authors to anonymize), so address "Referee 2" by number; (2) acceptance is conditional on the **Data Editor's pre-publication reproducibility check** (AEA DCAS, Zenodo deposit — see `restud-replication-package`), so a revision that adds empirical results must keep the replication package in lockstep — do not promise a number you cannot regenerate from the deposit. Push new proofs and bulky robustness into the **online appendix** and point to them from the letter.

## Triage every comment

Classify each referee point into one of four actions:

1. **Concede + fix.** The referee is right; make the change and say so plainly. Most comments are this. Conceding gracefully builds credibility for the few points you contest.
2. **Clarify.** The referee misread because the text was unclear. Fix the text so the *next* reader does not misread, then explain the clarification. Do not just say "the referee misunderstood" — that blames the reader.
3. **Push back (rarely).** The referee is wrong on substance. Push back only with evidence — a citation, a new result, a proof — and only on points that matter. Pick these battles sparingly.
4. **Decline (rarely, with reason).** A request is out of scope or would change the paper into a different paper. Decline respectfully, explain why, and offer the smaller version of what they want if possible.

## The response letter

Structure:

- **Cover note to the editor.** Thank the editor, summarize the main changes in a short paragraph, and flag any place where referees disagreed and how you reconciled them.
- **Per-referee sections.** For each referee, restate each comment (quoted or paraphrased faithfully), then the response: the action taken and **the exact location in the revised manuscript** (section, page, table number).
- **Tone:** professional, specific, non-defensive. Every "we have done X" must point to where.

Format each response as:

```
Comment R2.3: "[faithful quote of the referee's point]"
Response: We agree / We have clarified / We respectfully note ...
Change: [what changed] — see Section 4.2, p. 14, and new Table 5.
```

## Reconciling conflicting referees

When two referees want opposite things, do not silently satisfy one and ignore the other. State the tension to the editor, choose the resolution that serves the paper, and explain the choice. The editor adjudicates — give them what they need to back you.

## Checklist

- [ ] Manuscript revised *before* the letter was written
- [ ] Every comment triaged (concede / clarify / push back / decline)
- [ ] Each response cites the exact revised location (section, page, exhibit)
- [ ] Push-backs are evidence-backed and few
- [ ] Declines are respectful and offer a smaller alternative
- [ ] Conflicting referee requests reconciled explicitly for the editor
- [ ] Tone professional and non-defensive throughout

## Anti-patterns

- Writing the letter against the old draft, so "see p. 14" points to the wrong place
- "The referee misunderstood" with no text fix — blaming the reader
- Pushing back on many points; it reads as unwillingness to revise
- Conceding a point in the letter but not actually changing the manuscript
- Silently ignoring one of two conflicting referees
- A letter that argues the paper's importance instead of answering the comments

## Output format

```
【DECISION TYPE】R&R | reject-and-resubmit | minor revision
【COMMENTS TRIAGED】concede X / clarify Y / push-back Z / decline W
【MANUSCRIPT REVISED FIRST】yes / no
【CONFLICTS RECONCILED】[...]/none
【LETTER STATUS】drafted with exact-location cites
【NEXT SKILL】restud-submission (resubmit) | restud-robustness (if new results needed)
```
