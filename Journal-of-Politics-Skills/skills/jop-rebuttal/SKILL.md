---
name: jop-rebuttal
description: Use when writing the response to a The Journal of Politics (JOP) revise-and-resubmit. The response must convert each reviewer without alienating the editor, stay within JOP's page budget, keep the manuscript double-blind, and preserve replicability so the eventual JOP replication-analyst check passes. Structures the response letter; it does not fabricate new results.
---

# R&R Rebuttal (jop-rebuttal)

A JOP **R&R is a strong signal** — the editor sees a path to publication. The response letter must move
*every* reviewer toward yes while keeping the editor confident the revision is convergent, and it must do
so without **blowing the page budget**, **breaking double-blind anonymity**, or **breaking
replicability** that the analyst will later check.

## When to trigger

- An R&R decision arrived and you are planning the revision + response letter
- Reviewers disagree with each other and you must reconcile their demands
- A reviewer requests analyses that would change the paper's claims or its length
- Writing the cover note to the editor summarizing the revision

## Strategy

1. **Read the editor's letter as the rubric.** The editor signals which points are decisive. Solve those
   first; the editor adjudicates disagreements among reviewers.
2. **One point-by-point response, every comment addressed.** Quote each comment, then respond. Never
   skip one — silence reads as non-compliance.
3. **Concede or rebut explicitly, with evidence.** For each: did what was asked (say where, with the new
   text/table number), or push back **respectfully with a reason** (theory, design, or evidence).
4. **Reconcile conflicting reviewers openly.** When R2 wants the opposite of R3, say so, choose a
   principled path, and explain the tradeoff to the editor.
5. **Protect the contribution and the page budget.** Added analyses often go to the **Online Appendix
   (≤ 25 pp)** so the main text stays within **35 / 10 pages**; new material must not push you over.
6. **Keep anonymity and replicability intact.** The revised manuscript stays **double-blind**, and any
   new tables/figures must remain **reproducible by the deposited code** so the JOP replication analyst's
   eventual re-run passes (see `jop-replication-and-data-policy`).

## Response-letter format

For each reviewer comment:

```
> [Quoted reviewer comment]

Response: [What we did / why we respectfully disagree].
Change: [Section/page/table-figure number; note if it moved to the Online Appendix].
```

Open with a short **summary of the main changes** to the editor; group by reviewer; end each entry with
the location of every change so the editor can verify quickly.

## Anti-patterns

- Ignoring or merging away a comment without a visible response
- Capitulating to a request that breaks the paper's logic just to please a reviewer
- Adding so much new material that the revision blows the page budget
- New analyses that the deposited code cannot regenerate (will fail the analyst check)
- Defensive tone, or self-identifying phrasing that breaks double-blind in the revised file

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Concede vs rebut】each tagged with evidence + change location
【Reviewer conflicts】reconciled and explained to editor? [Y/N]
【Page budget】revision still within 35 / 10 pp (overflow → appendix)? [Y/N]
【Anonymity + replicability】preserved in revised manuscript + package? [Y/N]
【Next】resubmit via Editorial Manager
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JOP review/decision process, page limits, replicability-contingent acceptance
