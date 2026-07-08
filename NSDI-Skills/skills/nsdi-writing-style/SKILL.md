---
name: nsdi-writing-style
description: Use when drafting or revising NSDI prose — building the operational-pain-to-design-principle arc, fitting argument and figures into 12 pages with references and appendices outside the cap, calibrating claims to trace and testbed evidence, and writing for reviewers who read tail percentiles before adjectives.
---

# NSDI Writing Style

An NSDI paper argues that a nameable design idea, embodied in a working networked
system, holds up under realistic traffic. The prose exists to make that chain
checkable. Format facts below are the NSDI '27 CFP as rendered on 2026-07-08.

## The opening arc

NSDI first pages that work tend to execute five beats in order (see the rebuilt
example in
[`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md)):

1. **Operational pain, evidenced** — a failure shape, cost, or limit shown in a trace
   or deployment, not asserted from intuition.
2. **Why the networked setting causes it** — the distributed or stack-level reason
   local fixes fail. This beat is also the scope defense; a paper that cannot write it
   is drifting out of the CFP's "design of networked systems or the networking stack."
3. **The design principle, named** — the transferable idea, stated so another team
   could apply it to a different system.
4. **The built system** — what was implemented, where it runs, what was not built.
5. **Claims with evidence addresses** — each headline number tied to a section, a
   workload, and a percentile.

## Budget arithmetic before sentence polish

The '27 rule: **12 pages including footnotes, figures, and tables; references and
appendices may extend beyond**. Two consequences shape the writing:

- Figures are inside the cap, so every plot pays rent. Cut the third bar chart saying
  "ours is faster again"; keep the breakdown that explains *why*.
- Appendices exist but are overflow, not annex: reviewers judge the 12 pages. Nothing
  load-bearing (a baseline, the key workload description, a correctness argument)
  may live only past the references (`nsdi-supplementary`).

A workable allocation for a 12-page systems paper:

| Section | Pages | Job |
|---|---|---|
| Intro + motivation measurement | 2 - 2.5 | Beats 1-3 with data |
| Design | 3 - 3.5 | Principle → mechanism → interfaces; failure handling explicit |
| Implementation | 0.5 - 1 | What exists, LoC/frameworks, honest deltas from design |
| Evaluation | 3.5 - 4 | Questions answered, not benchmarks toured |
| Related work + discussion | 1 - 1.5 | Positioning + stated limits |

## Sentence-level calibration

Systems reviewers at this venue distrust superlatives and read distributions. Editing
passes that consistently improve NSDI drafts:

- Replace every "up to N×" with the percentile, workload, and range: "2.1-3.4× at
  p99.9 on the replayed incident weeks."
- Replace "significantly / dramatically / novel" with the measured delta or the named
  mechanism. Adjectives signal missing numbers.
- Convert passive mechanism descriptions into agent-explicit ones — *which component
  decides, on what signal, at what timescale*.
- State the boundary honestly, in the body: the regime where the design loses
  (incast, single replica, cold caches). NSDI culture treats a named limitation as
  competence, and an unnamed one found by a reviewer as concealment.
- Keep terminology bijective: one name per component, one component per name, figures
  and text agreeing exactly.

```text
Weak:  "Our novel scheduler significantly reduces latency (up to 4.1x)
        compared to state-of-the-art approaches."
NSDI:  "Shifting retries off congested paths cuts p99.9 latency 2.1-3.4x
        vs tuned exponential backoff across the three incident classes
        (§6.2); gains vanish when RTT < the lease renewal interval (§7)."
```

## Anonymity constraints on prose

Double-blind shapes phrasing, with one NSDI-specific fork: research-track papers
neutralize identifying deployment details ("a large provider's fleet"), while
**operational-track papers may keep real system and company names** with author names
still withheld. Write self-citations in the third person; never delete a reference to
hide identity; cite a concurrent NSDI submission as "Under submission. Details omitted
for double-blind reviewing." The CFP endorses AI tools for grammar and clarity of
human-written text — the ideas, and the responsibility, stay human.

## Revision-letter prose (one-shot resubmissions)

A resubmitted revision is read by the same reviewers against their own issue list, so
the writing task inverts: instead of impressing a stranger, show a known reader that
each demanded change exists. Keep new text visually traceable — the auxiliary
change-highlighted PDF must let a reviewer jump from issue to fix in seconds
(`nsdi-author-response`). Prose that quietly rewrites unrelated sections invites
re-litigation of settled points.

## Figures as argument, not decoration

Because figures bill against the 12 pages, each one should be designed like a
paragraph with a topic sentence:

- Caption states the takeaway ("Leases cap retry amplification at 1.3× during all
  three incident classes"), not the axes ("Latency vs. time").
- One visual idea per figure; a plot needing three sentences of legend explanation
  is two plots or zero.
- CDFs for distribution claims, timelines for dynamic behavior, breakdowns for
  "why" claims — the form should match the claim type (`nsdi-experiments`).
- Readability at print scale: systems reviewers annotate paper printouts; 6-point
  axis labels get skipped, and a skipped figure is a page of rent paid for nothing.

## Self-edit checklist

- [ ] First page executes all five beats; a stranger can quote the design principle.
- [ ] Every claim has an evidence address (section + workload + metric).
- [ ] No superlative survives without a number; tails reported where tails matter.
- [ ] Failure regimes named in the body, not confessed in the appendix.
- [ ] 12-page count verified on the built PDF, figures included.
- [ ] Anonymization style matches the declared track.

## Output format

```text
[Arc check] beats 1-5 present? weakest beat + fix
[Budget] pages by section vs allocation; what to cut first
[Calibration] list of unbacked superlatives / missing percentiles
[Boundary] named failure regimes: <list or MISSING>
[Track-consistent anonymity] research-neutralized / operational-named
[Edit order] highest-leverage rewrite first
```
