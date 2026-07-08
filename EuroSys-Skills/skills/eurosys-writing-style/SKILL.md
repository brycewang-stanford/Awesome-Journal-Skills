---
name: eurosys-writing-style
description: Use when drafting or revising EuroSys prose — building the problem-to-mechanism arc systems reviewers expect, budgeting the 12 technical pages across design and evaluation, writing figure-first evaluation sections, keeping claims measurement-scoped, and maintaining double-blind voice in the acmart sigplan format.
---

# EuroSys Writing Style

Use this on the manuscript itself. A EuroSys paper succeeds when a broad
systems PC — kernel people, distributed-systems people, cloud and security
people — can each extract the same mechanism and believe the same numbers
within one reading. The two-column `acmart[sigplan]` format and the 12-page
technical budget (EuroSys 2027 CFP, rendered 2026-07-08) reward density that
stays legible, not compression that hides.

## The load order of a EuroSys introduction

1. The operational pain, stated concretely enough to measure.
2. Why the existing abstraction or mechanism structurally cannot fix it —
   named systems, not "prior approaches".
3. The insight: the one idea that unlocks the design.
4. What was built, and the two or three numbers that prove the idea carries.
5. Contributions as verifiable statements, each pointing at a section.

A reader who stops after page one should be able to state your insight in a
sentence. If the insight sentence does not exist, the problem is the research
framing, not the writing (route to `eurosys-topic-selection`).

## Page budget that survives review

| Section | Share of 12 pages | Failure mode when misallocated |
|---|---|---|
| Intro + motivation | ~2 | Motivation essay crowds out the design |
| Design + implementation | ~4.5 | Mechanism described by metaphor, not by structure |
| Evaluation | ~4 | Result dump with no questions being answered |
| Related work + discussion | ~1.5 | Either a stub or a survey; both read badly |

References are free pages at EuroSys — cite generously and spend zero
technical pages on bibliography anxiety.

## Design sections that reviewers can retell

- Name components and keep the names stable; a renamed component is a new
  component to a tired reviewer.
- One architecture figure whose boxes match the subsection structure.
- For each mechanism: the invariant it maintains, the common-case path, the
  failure path, and the cost you pay for it. The cost sentence is what
  separates engineering description from research writing.
- Push code-level detail down to a listing only when the trick *is* the code.

## Evaluation prose discipline

Open with the questions, then answer them in order:

```text
§6 Evaluation. We answer four questions:
  Q1  Does <system> improve end-to-end <metric> on realistic workloads? (§6.2)
  Q2  Where does the gain come from? (§6.3, component breakdown)
  Q3  What does it cost — memory, CPU, complexity? (§6.4)
  Q4  When does it lose? (§6.5, adversarial and edge workloads)
```

Q4 is the EuroSys credibility section: a paper that measures its own worst
case defuses the reviewer whose job is to find it.

- Every figure caption states the takeaway, not just the axes.
- Numbers in prose carry their conditions: "2.1x on the write-heavy trace at
  p99", never bare "2.1x better".
- Banned without qualification: "significantly", "dramatically", "orders of
  magnitude", and any superlative the data does not literally show.

## Sentence surgery

| Draft reflex | EuroSys register |
|---|---|
| "X is a critical challenge in modern datacenters" | Open with the measured symptom, not the genre claim |
| "significantly reduces latency" | "reduces p99 by 38% on trace T at 85% load" |
| "our novel approach" | Name the mechanism; novelty is the reviewer's verdict |
| "due to space constraints, details are omitted" | Point to the artifact or cut the claim |
| "we believe this generalizes" | State the condition under which it generalizes, or drop it |
| "as shown in Figure 6" (alone) | "...which isolates the planner's contribution (Fig. 6)" |

## Revision passes that pay at this venue

1. **Retell pass** — after each design subsection, write its three-sentence
   PC-meeting summary; if you cannot, the subsection is not done.
2. **Number pass** — every performance number in prose gets its conditions
   attached or gets deleted; captions get takeaways.
3. **Skeptic pass** — read only §Evaluation as a hostile reviewer hunting
   untuned baselines and missing worst cases; fix what you find.
4. **Blind pass** — search for lab names, grant strings, first-person
   references to prior systems, and telltale cluster hostnames in listings.
5. **Budget pass** — measure section lengths against the 12-page allocation
   and rebalance before polishing sentences that will be cut anyway.

## Double-blind voice

- Your prior systems appear in third person: "extends Foo [12]" — even when
  the extension is obviously yours.
- Deployment anecdotes get de-identified without being falsified: "a European
  cloud operator" is fine; invented deployments are fraud.
- Acknowledgments, grant numbers, and lab-specific artifact URLs wait for
  camera-ready.

## Output format

```text
[Insight sentence] <the one-sentence idea a reviewer should retell>
[Arc audit] pain -> structural gap -> insight -> system -> numbers: present/missing
[Budget skew] <sections over/under the 12-page allocation>
[Claim hygiene] <unscoped numbers and superlatives found>
[Q4 status] <does the evaluation measure where the system loses?>
```
