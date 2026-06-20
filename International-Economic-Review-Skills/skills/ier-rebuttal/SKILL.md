---
name: ier-rebuttal
description: Use when an International Economic Review (IER) decision letter or referee report needs a response strategy and a revision plan. Triages comments and structures the response letter to a rigor-leaning, theory-tilted review; it does not invent new results.
---

# Rebuttal Strategy (ier-rebuttal)

## When to trigger

- An IER R&R (or major/minor revision) letter arrived and you need a response plan
- A reject-and-resubmit or a split decision (referees disagree) needs a strategy
- A referee challenges the load-bearing assumption, the identification, or a proof and you must decide what to concede vs. defend
- You need to convert a stack of referee comments into an ordered, owned revision plan

## Reading an IER decision letter

IER reviews are rigor-gated and theory-leaning, so the comments that *must* be resolved are usually about **correctness and generality**, not framing. Triage every comment into one of four buckets before writing a word of response:

| Bucket | What it is | Response posture |
|--------|------------|------------------|
| Must-fix (correctness) | A genuine error, an undefended load-bearing assumption, an identification hole, a gap in a proof | Fix fully; show the fix in the paper AND summarize it in the letter |
| Must-address (generality) | "Does this survive weaker assumptions / a different specification?" | Run it; report the result honestly (including if it bounds the headline) |
| Reasonable-but-costly | A check the referee would like that adds length/effort | Do the high-value ones; for the rest, explain the trade-off respectfully |
| Misreading / disagreement | The referee misunderstood, or is wrong on the merits | Disagree *with evidence and courtesy*; never just assert |

### The response-letter craft

1. **Lead with a short summary of the main changes** — let the editor see the paper is materially better before the point-by-point.
2. **Quote each comment, then respond directly beneath it**, and **point to the exact section/page/equation** where the change lives. An IER referee re-checks; make re-checking easy.
3. **For correctness fixes, show the math/result, not just a promise.** "We now prove uniqueness in Appendix B.2 under condition C; the condition means [economics]." Concreteness wins.
4. **When a check moves the result, report it and bound it.** IER referees trust authors who say "the welfare gain falls to 3.8% under the alternative elasticity, still positive and economically meaningful" over authors who hide the movement.
5. **Disagree sparingly and with evidence.** If the referee is wrong, say so politely and prove it; pick the one or two hills worth defending, concede the rest gracefully.
6. **Address the editor's synthesis separately.** The editor's letter often names the two or three decisive issues — make sure each is answered prominently, not lost in the per-referee detail.
7. **Mind the page ceiling.** Revisions can push past 50 pages; move added proofs/checks to the online appendix and keep the main text within the limit (检索于 2026-06；以官网为准).

### Handling split decisions and the theory/empirics referee divide

IER's broad readership means a paper can draw referees from different subfields who weight things differently — a theory referee may want the proof tightened while an empirical referee wants more robustness, and they may even disagree on what the paper is for. When referees split, do not average their demands; instead, identify the *editor's* synthesis (the editor's letter usually adjudicates) and align the revision to it. If the editor has not adjudicated, address both demands but make explicit in the letter how you reconciled them — e.g., "Referee 1 asked for a weaker assumption; Referee 2 asked for an additional specification; the revised Section 3 does both, and they are mutually consistent because...". Showing you can hold both perspectives is itself persuasive at a general-interest journal.

### Worked example (illustrative)

A referee writes: "The uniqueness proof is incomplete." This is a must-fix (correctness). The wrong response promises to "clarify in revision." The right IER response completes the proof in the appendix, states in the letter exactly where ("Uniqueness now proved in Appendix B.2 under Assumption 3; the condition is interpreted in Section 2.4"), and notes that the comparative statics in Section 4 rely only on the now-established uniqueness. The referee can re-check in one click, sees the gap is genuinely closed, and the correctness objection — the kind that sinks IER papers — is retired cleanly.

### Make re-checking trivial — the rigor-journal response habit

An IER referee re-reads the revision to verify the fixes, so the response letter's job is to make re-checking as fast as possible. Two practices do most of the work: quote the comment verbatim before responding (so the referee does not hunt for context), and give an exact pointer — section, page, equation, or appendix label — for every change. "We have addressed this" is not a response; "Uniqueness is now proved in Appendix B.2; the new Section 2.4 interprets the condition" is. The faster a referee can confirm each fix, the faster the paper moves, and the more goodwill you accumulate for the comments you choose to push back on.

### Concede well, fight rarely

The strongest revisions concede the minor and reasonable points quickly and graciously, reserving disagreement for the one or two comments that genuinely misread the paper or are wrong on the merits — and even then, disagree with evidence, not assertion. An author who fights every comment reads as defensive and burns the editor's patience; an author who concedes the small things and defends the essential things with proof reads as a careful scholar. At a rigor journal where the editor often adjudicates substance, that posture is itself persuasive.

## Checklist

- [ ] Every comment is triaged (must-fix / must-address / costly / misreading)
- [ ] Correctness and identification comments are fixed *in the paper*, with the fix shown in the letter
- [ ] Each response points to the exact section/page/equation of the change
- [ ] Any check that moves the headline result is reported and bounded, not hidden
- [ ] Disagreements are evidence-backed, courteous, and limited to the hills worth defending
- [ ] The editor's decisive issues are answered prominently and separately
- [ ] The revised paper still respects the ≤50-page ceiling (added material to online appendix)
- [ ] No new claim is added that lacks support; the replication deposit is updated if analyses changed

## Anti-patterns

- A response letter that promises changes without showing them in the paper
- Hiding or soft-pedaling a robustness check that weakened the result — the fastest way to lose referee trust
- Arguing with the referee by assertion instead of by evidence
- Fighting every comment instead of conceding the minor ones and concentrating fire
- Ignoring the editor's synthesis and answering only the referees
- Letting the revision balloon past 50 pages instead of using the online appendix

### Referee comment patterns and the response that retires each

- *"The proof is incomplete / uniqueness unproved."* → Complete it in the appendix; point to the exact label; note which downstream results depend on it.
- *"This isn't credibly identified."* → Add the sensitivity matrix or the design diagnostic; report untargeted-moment fit or a falsification test.
- *"Is the result robust?"* → Add the one decisive threat-mapped check; if it moves the result, report and bound the movement.
- *"I don't see the general-interest contribution."* → Sharpen the intro's delta and the general object; this is a positioning fix (`ier-literature-positioning`), surfaced in the response.

Each pattern maps to a concrete change shown in the paper and summarized in the letter — never to a bare promise.

## Output format

```text
【Journal】International Economic Review
【Skill】ier-rebuttal
【Decision】R&R (major/minor) / reject-resubmit / split
【Triage】comments sorted: must-fix / must-address / costly / misreading
【Correctness fixes】each shown in the paper + summarized in the letter? [Y/N]
【Honest movement】any check that moved the result reported and bounded? [Y/N]
【Disagreements】evidence-backed, courteous, limited to key hills? [Y/N]
【Editor's decisive issues】answered prominently? [Y/N]
【Length】revision within ≤50pp (added material to online appendix)? [Y/N]
【Next step】resubmit via Editorial Express; update replication deposit if analyses changed
```
