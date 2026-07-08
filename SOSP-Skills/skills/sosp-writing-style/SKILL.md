---
name: sosp-writing-style
description: Use when drafting or revising SOSP prose — leading with a design principle rather than a feature list, building the intro's problem-to-insight arc, budgeting 12 dense two-column pages across design and evaluation, writing figures that argue, and keeping claims inside what the measurements support.
---

# SOSP Writing Style

Use this at drafting and revision time for a SOSP paper. The format constants (2026
cycle, checked 2026-07-08 against the official author guidelines): at most 12 pages
of technical content in submission, 10-point font on 12-point leading, a 7 x 9 inch
text block in two columns, references uncounted. Those pages are read first by a
skeptical fast pass and later defended live at a PC meeting — the prose must arm an
advocate, not just inform a reader.

## Lead with the principle, not the artifact

The recurring identity question at this venue is "what is the *principle*?" A SOSP
paper is remembered as an idea with a system attached, not a system with features
attached. Concretely:

- Somewhere on page one, a sentence must exist that survives extraction: the
  insight, stated so a PC member can repeat it at the meeting without the paper
  open ("crash consistency can be delegated to the allocation layer because ...").
- Feature-list intros ("we present X, which supports A, B, and C") read as
  workshop papers. Replace the list with the tension the design resolves.
- If the honest one-sentence version is "we engineered X to be faster", the routing
  question comes before the writing question (see `sosp-topic-selection`).

## The first-page arc

| Move | Job | Symptom when missing |
|---|---|---|
| Problem, concrete | Reader can picture the failing scenario | Intro opens with a market-size claim |
| Why existing systems fail | The gap is structural, not un-tried | Related work reads as the real intro |
| Insight | The extractable principle | Reviewers summarize the paper differently from you |
| Embodiment | The system, named, one paragraph | Insight floats with no evidence anchor |
| Headline evidence | 2-3 measured numbers with baselines named | "Extensive experiments show" |
| Honest scope | One clause on what the design gives up | The meeting discovers the limitation for you |

## Budgeting twelve dense pages

A workable allocation for a design-plus-evaluation SOSP paper; deviate deliberately:

```text
Intro + motivation          1.5 pp   the arc above, plus the motivating measurement
Design                      4.0 pp   principle -> mechanisms; invariants stated inline
Implementation              1.0 pp   what was built, LoC, what is borrowed vs new
Evaluation                  4.0 pp   claims mapped to experiments (see sosp-experiments)
Related work                0.75 pp  positioning, not survey (see sosp-related-work)
Discussion + conclusion     0.75 pp  limitations owned, generality argued
(references                 uncounted — never starve them)
```

When over length, cut prose before leading or figures: geometry tampering is a
desk-reject at this venue, and shrunken figures cost more reviewer goodwill than a
trimmed subsection. Move *depth* (full proofs, extra sweeps) to the supplement, never
review-critical evidence (see `sosp-supplementary`).

## Figures that argue

Systems reviewers read figures before prose on the fast pass. Each figure earns its
column-inches by making a claim on its own:

- Caption states the takeaway ("Recovery replays only the log tail; time is flat in
  log size"), not the axes ("Recovery time vs. log size").
- Baselines appear *in* the figure, labeled with the same names the text uses.
- Distributions for tail claims: a p99 bar with no spread is an invitation to a
  soundness attack.

## Register and claim discipline

- Present tense, active voice, the system as subject: "Foo batches acknowledgments"
  beats "acknowledgments are batched by our approach."
- Every superlative is a target at the PC meeting. "Fast" is free; "faster than
  Bar on write-heavy YCSB by 2.1x" is defensible; "optimal" had better come with
  a proof.
- Anonymized self-reference in third person throughout — the double-blind rules
  reach into style ("the Foo paper showed", not "we previously showed").
- Define each invariant once, name it (I1, I2 ...), and cite the name thereafter;
  the response phase will need those anchors when a review misstates one.

```bash
# Weasel-word and overclaim sweep before the freeze
pdftotext main.pdf - | grep -inE 'significant(ly)? (improve|outperform)|extensive experiments|novel(ty)? |clearly|obviously|optimal' | head -20
```

## Revision protocol

1. Extract the paper skeleton: first sentence of every paragraph, read in order. If
   the skeleton does not carry the argument, restructure before polishing.
2. Give the draft to a systems reader for a strict 15-minute pass — abstract, intro,
   figures, conclusion — and ask them to state the principle. Wrong answer means a
   page-one problem, whatever they say about section 4.
3. Only then line-edit for density: merge stub paragraphs, collapse enumerations
   that repeat their lead-in, delete signposting that restates section titles.

## Output format

```text
[Principle] extractable one-liner found on page one? <quote it>
[Arc audit] problem / gap / insight / embodiment / evidence / scope — which missing
[Budget] section page allocation vs the 12-page plan
[Figures] each figure's caption-claim; baselines in-figure?
[Claim sweep] overclaims found -> defensible rewrite
[Skeleton verdict] argument carries on first sentences alone? <yes/no>
```
