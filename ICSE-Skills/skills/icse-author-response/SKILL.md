---
name: icse-author-response
description: Use when drafting an ICSE author response or executing a Major Revision, covering criterion-targeted replies to research-track reviews, the September response window, the four-week revision sprint to the November deadline, response-letter structure, and change tracking that survives PC re-review.
---

# ICSE Author Response

ICSE gives authors two distinct speaking turns, and they demand different
documents. The **author response** (September in the 2027 cycle, checked
2026-07-08) answers reviews before first decisions; the **Major Revision
response letter** (revision due November 17, 2026; final decision December 18)
accompanies a changed paper re-read by the same reviewers. Do not write the
first as if it were the second.

## Turn 1: the author response

You are writing for the PC discussion, not for your own catharsis. Three moves
earn their space:

1. **Correct factual misreadings**, with a page/section pointer: "R2 states we
   evaluate on toy programs; §5.1 lists the 17 real-world projects (median 210
   kLOC)."
2. **Supply requested evidence that already exists** — a number, a table cell,
   a clarification of the study protocol. If it fits in a sentence, give the
   sentence, not a promise.
3. **Commit to feasible changes**, scoped to what a Major Revision window can
   hold. "We will add effect sizes to Table 4" is credible; "we will run a
   controlled experiment with professional developers" is not.

Map every reply to the criterion it defends. ICSE reviews are structured around
novelty, rigor, relevance, and verifiability/transparency — a response that
answers a rigor objection with a relevance argument reads as evasion.

| Objection pattern | Criterion under attack | Response that works |
|---|---|---|
| "Delta over [X] unclear" | Novelty | One-paragraph contrast: what X cannot do, with citation and evidence pointer |
| "Only N subjects / projects" | Rigor | Justify N against comparable published studies; show per-subject variance |
| "Why would practitioners care?" | Relevance | Concrete failure cost, practitioner quote, or deployment context from the paper |
| "Cannot tell how the tool works" | Verifiability | Point to artifact + name the exact section/README that answers it |
| "Threats section is boilerplate" | Rigor | Name the one threat that genuinely worries you and the mitigation you ran |

Response mechanics for the current cycle (length cap, structured forms, whether
revised PDFs are allowed) were not published at check time — 待核实 on the
HotCRP site when the window opens. Draft to fit the tightest historical norm:
short, numbered, no new-contribution smuggling.

## Turn 2: the Major Revision

A Major Revision at ICSE is an itemized contract. The meta-review or reviews
enumerate required changes; December's decision largely reduces to whether each
item is verifiably addressed. The four-week window (Oct 20 notification →
Nov 17 revision in 2027) sets the feasibility bar for what you promise.

Structure the response letter as a ledger:

```markdown
# Response to Reviews — Submission #NNN (Major Revision)

## Summary of changes
Three sentences: the big moves, in reviewer language.

## R1.1 (rigor) — "No baseline against static analysis tools."
**Change:** Added SpotBugs and Infer as baselines; new §5.3, Table 6.
**Where:** pp. 6–7, marked in blue.

## R1.2 (verifiability) — "Prompt templates not disclosed."
**Change:** Full templates now in the replication package (`prompts/`),
summarized in §4.2.

## R3.4 — "Compare on industrial code."
**Declined, with reason:** licensing prevents redistribution; we instead added
two large OSS systems (§5.1) and state the limit in Threats (§7).
```

Rules of the ledger: every numbered reviewer point appears, including the ones
you decline; every change names its section and page; declined items get a
reason, never silence. Submit a diff-marked PDF if the instructions allow one
— reviewers granted four weeks of their own time deserve not to hunt.

## Revision-sprint triage

With four weeks, order work by decision impact per day:

1. **Days 1–3:** parse all reviews into the ledger; agree the decline list with
   coauthors; email the chairs only if a required change is genuinely ambiguous.
2. **Week 1–2:** the evidence items — new baselines, added analyses, statistics.
   These have the longest compute/writing tails.
3. **Week 3:** framing items — intro repositioning, related-work additions,
   threats rewrite.
4. **Final days:** ledger completion pass, diff-PDF build, artifact update so
   the package matches the revised claims.

## Tone calibration

The register that works is technical-neutral: no wounded pride, no
flattery, no lawyering. Compare:

- *Defensive:* "The reviewer apparently did not read §5, where this is
  clearly explained." → *Working:* "§5.2 (Table 4, row 3) reports this; we
  will make the forward reference in §3 explicit."
- *Over-conceding:* "We agree our evaluation is limited and will try to
  improve." → *Working:* "We agree external validity is bounded by the Java
  focus; we now state this in §7 and add two non-JVM subjects to the
  package's extension guide."

Concede real weaknesses precisely (it buys credibility for the pushbacks);
push back on real errors respectfully (silence reads as agreement).

## Anti-patterns

- **The grateful essay.** Paragraphs of thanks before content; reviewers read
  ledgers, not letters of appreciation.
- **The stealth rewrite.** Changing sections nobody complained about invites
  fresh objections in December with no turn left to answer them.
- **The optimistic promise** in Turn 1 that Turn 2 cannot keep — reviewers
  keep receipts across turns; an unkept response commitment is a rejection
  reason all by itself.
- **Artifact drift**: revised claims with an unrevised replication package
  fails exactly the verifiability criterion the revision was meant to satisfy.

## Output format

```text
[Turn] author response / major revision
[Ledger] N reviewer points -> addressed / declined-with-reason / needs decision
[Feasibility] promised work vs days remaining to Nov 17
[Risk items] points where the December decision could still go against you
```
