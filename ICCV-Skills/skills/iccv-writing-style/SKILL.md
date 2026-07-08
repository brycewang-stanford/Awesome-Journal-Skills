---
name: iccv-writing-style
description: Use when drafting or revising the prose and figures of an ICCV paper, covering writing for an international generalist reviewer pool, the inclusive 8-page economy, mechanism-first exposition, calibrated claims that survive a one-page rebuttal cycle, and captions and figures that carry the paper for readers who skim first.
---

# ICCV Writing Style

An ICCV submission is read by reviewers drawn from the most international pool in
computer vision — in 2025, every author of 11,239 submissions was also a
potential reviewer — and most of them work outside your subfield. The style
target is therefore precise: a paper a *generalist vision researcher* can
evaluate fairly in one sitting, in their second or third language, under
deadline pressure of their own.

## Write for the generalist, cite for the specialist

The three reviewers you draw will rarely all be specialists in your niche.
Concretely:

- Define subfield jargon at first use, in one clause, even terms your lab
  considers standard ("the chamfer-L1 metric, i.e. average nearest-neighbor
  distance in both directions").
- Make the method's *mechanism* explainable to an adjacent-area reviewer:
  what information flows where, and what would break without it. Specialists
  verify details; generalists score the story — you need both.
- Prefer short declarative sentences. Non-native readers (and tired native
  ones) lose subordinate-clause chains; ICCV's reviewer pool is global by
  construction, and prose that filters readers filters scores.

## The inclusive-8-pages economy

The cap is eight pages including figures and tables, references-only overflow
(2025 rule). Treat layout as a market where every element bids for space with
the evidence it delivers:

| Element | Earns its space when | Evict when |
|---|---|---|
| Page-1 overview figure | A stranger states the idea after 30 seconds with it | It needs the body text to decode |
| Pipeline figure | It replaces ≥ its own height in method prose | It restates the obvious encoder→decoder |
| Main results table | Rows = strongest current baselines, matched | Padded with weak ancient rows for bulk |
| Qualitative strip | Shows the *mechanism's* visible signature | Generic pretty outputs any method makes |
| Ablation table | Each row flips one switch (`iccv-experiments`) | Grid dumped without a takeaway sentence |
| Equation block | Notation reused ≥ twice downstream | Formalizing what one sentence says |

Every caption must be self-sufficient — dataset, setting, and the takeaway in
words — because the skim pass reads only captions, and at most venues in this
family the skim pass happens before the real one.

## Mechanism-first sentences

The genre's strongest habit: name the mechanism, then the consequence, then the
number. Compare the two registers:

```text
weak:   "We propose a novel and effective framework that significantly
         outperforms state-of-the-art methods on several benchmarks."
strong: "Replacing per-frame matching with a persistent memory of object
         queries removes the re-detection bottleneck: +3.1 HOTA on
         DanceTrack at identical backbone and training budget."
```

The weak sentence contains zero checkable content — and at ICCV, unfalsifiable
praise adjectives ("novel", "significantly", "state-of-the-art" unscoped) are
read as inexperience markers. The strong sentence makes three commitments a
reviewer can verify, which is exactly what earns scores.

## Claims sized for a one-page defense

Every claim in the abstract will potentially need defending in May inside a
shared, single rebuttal page (`iccv-author-response`). Size claims accordingly
at writing time:

- Scope superlatives to dataset + protocol + budget class, in the sentence
  itself, not a footnote.
- If generalization is claimed, the paper must contain the cross-domain table
  that backs it; otherwise claim the domains you tested.
- Put the limitation you know about into the limitations paragraph *before*
  reviewers find it — a self-reported failure costs a sentence; a discovered
  one costs a score point and rebuttal real estate.
- Never let the intro promise what the conclusion doesn't deliver: read the
  contributions bullets against the conclusion as a final pass; they should be
  the same statements at two altitudes.

## Structure that survives skim-order reading

Reviewers at volume venues read out of order: abstract → figures → tables →
conclusion → (maybe) everything else. Two consequences. First, the paper's
argument must be reconstructible from abstract + captions + table headers alone
— test this literally by extracting them:

```bash
# Skim-pass simulator: what a reviewer sees in the first five minutes
pdftotext -layout paper.pdf - | grep -A2 -E '^(Figure|Table) [0-9]+[.:]' > skim.txt
head -60 skim.txt   # does this sequence state problem → idea → evidence?
```

Second, transitions between sections carry less weight than section *openings*:
begin each section with its conclusion ("Our decoder attends over a persistent
memory; this section details the write and read operations"), not with throat-
clearing history.

## Introduction in five moves

The ICCV intro that works is a proof sketch, not a literature tour: (1) the
visual capability at stake, one paragraph, concrete; (2) why current approaches
miss it — mechanism of failure, not adjectives; (3) the idea, stated so a
generalist could re-derive the design; (4) evidence preview with scoped numbers;
(5) contributions as claims (each one falsifiable), not as an activity log
("we conduct extensive experiments" is an activity, not a contribution).

## Language-level pass, last

Only after structure settles: strip hedge stacks ("could potentially help to"),
convert passive method descriptions to active ("the features are fused" → "the
decoder fuses"), unify tense (present for the method, past for experiments run),
and hunt duplicated notation — vision papers accumulate three symbols for the
same feature map by section 4. If any drafting was machine-assisted, verify
every citation exists and every number matches your tables; author
responsibility for the text is absolute, and fabricated references are
review-killing at every CVF venue.

## Reverify each cycle

- Page cap and reference-overflow wording in the 2027 author kit.
- Any new required sections (limitations, ethics, disclosure statements —
  none verified for 2025, 待核实 for 2027).
- Template version pinned to the current cycle's official kit.

## Output format

```text
[Generalist test] adjacent-area reader states the idea after p.1: yes/no
[Space market] elements not earning their area: <list>
[Caption audit] self-sufficient: n/m
[Claim sizing] unscoped superlatives: <locations>
[Skim pass] abstract+captions+headers carry the argument: yes/no
[Edit queue] <highest score-impact first>
```
