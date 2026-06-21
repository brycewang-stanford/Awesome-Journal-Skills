---
name: arpsych-revision
description: Use when responding to the Annual Review of Psychology (ARPsych) Editor's or Committee's peer-review letter on a delivered review, or to copyediting/proof queries. Handles the post-delivery revision loop; it does not run the pre-delivery preflight (arpsych-submission) or re-audit balance from scratch (arpsych-comprehensiveness-and-balance).
---

# Revision — Responding to the Editor & Committee (arpsych-revision)

## When to trigger

- A review letter arrived from the ARPsych Editor or a Committee member on the delivered draft
- Copyediting or proof queries need responses
- Reviewers flag coverage gaps, balance problems, length over-run, or accuracy issues
- You must turn comments into a tracked, point-by-point revision

## What ARPsych review focuses on (检索于 2026-06；以官网为准)

The Committee assesses delivered reviews for **accuracy, rigor, and balance** (检索于 2026-06；以官网为准). So letters tend to cluster on a few predictable axes — diagnose which you are facing, because the fix differs:

| Comment type | What it really means | Fix route |
|--------------|----------------------|-----------|
| "Missing literature X" | a coverage gap threatens authority | re-run targeted search; place X in a framework cell (`arpsych-literature-synthesis`) |
| "Reads as advocacy / under-covers camp Y" | balance failure | strengthen the rival account; re-weigh by credibility (`arpsych-comprehensiveness-and-balance`) |
| "Effect Z is overstated / didn't replicate" | accuracy/replication issue | recalibrate confidence language; flag replication status |
| "Over the assigned length" | scope too broad | narrow the organizing question, not just trim words (`arpsych-organizing-framework`) |
| "Hard to follow / too specialist" | accessibility | rewrite for the adjacent reader (`arpsych-writing-style`) |
| "Where does this come from?" | transparency | document the search / deposit meta-analysis materials (`arpsych-transparency-and-reproducibility`) |

## How to respond

1. **Point-by-point response letter.** Quote each comment; state the change; cite the new section/figure/line. Be gracious — these are senior colleagues curating a volume of record.
2. **Concede genuine coverage/accuracy gaps.** A missed literature or an overstated effect is a real problem in a review of record; fix it, do not argue it away.
3. **Defend with evidence, not authority.** Where you disagree, make the case from the literature and the framework — never "as the invited expert, I judge…".
4. **Protect the spine.** Add requested coverage *into existing framework cells*; do not bolt on a disconnected section that breaks the organizing idea.
5. **Honor length.** If adding material, cut elsewhere to stay within the assigned length (检索于 2026-06；以官网为准).
6. **Proof stage.** At copyediting/proofs, check that house-style edits did not distort meaning and that re-rendered figures are accurate; answer queries promptly to protect the volume schedule.

## Checklist

- [ ] Every comment addressed in a quoted, point-by-point letter
- [ ] Genuine coverage/accuracy gaps conceded and fixed (not argued away)
- [ ] Disagreements defended from literature/framework, not authorial standing
- [ ] New material folded into existing framework cells (spine intact)
- [ ] Confidence/replication language recalibrated where accuracy was challenged
- [ ] Length kept within the assigned limit after additions (cut to fit)
- [ ] Transparency/meta-analysis materials updated if the search changed
- [ ] Proof/copyedit queries answered promptly; figure re-renders verified

## Anti-patterns

- Arguing away a real coverage gap instead of filling it (fatal in a review of record)
- Defending overstated claims by authority rather than recalibrating to the evidence
- Bolting requested topics on as a disconnected section that breaks the spine
- Letting additions blow past the assigned length
- Ignoring the replication-status concern that prompted an "overstated" comment
- Treating copyediting/proof queries as optional and slipping the volume schedule
- A defensive, status-claiming tone toward Committee colleagues

## Output format

```text
【Letter triage】comment types present (coverage / balance / accuracy / length / accessibility / transparency)
【Concessions】genuine gaps conceded + fixed? Y/N
【Defenses】disagreements argued from evidence (not authority)? Y/N
【Spine intact】new material folded into existing cells? Y/N
【Length】within assigned limit after edits? Y/N
【Transparency】search/meta-analysis materials updated if needed? Y/N | N/A
【Proofs】house-style edits + figure re-renders verified? Y/N
【Next step】return point-by-point response + revised review to the Editor
```
