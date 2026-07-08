---
name: isca-writing-style
description: Use when drafting or revising an ISCA paper's prose — organizing 11 pages around one architectural insight, writing the motivation section from measured data, describing mechanisms at reviewer-checkable precision with figures that carry the design, and keeping quantitative claims calibrated to the instrument behind them.
---

# ISCA Writing Style

An ISCA paper is an argument that a piece of machine organization should exist. The
prose conventions below are how the architecture community expects that argument to
be laid out — learned from the venue's canon and enforced, softly but consistently,
by its reviewers. Format facts (11 pages of single-spaced two-column text excluding
references, IEEE-flavored template for the 2026 edition) are the verified 2026
snapshot; recheck the current guidelines page before formatting.

## One insight, stated as a mechanism-behavior link

Before drafting, complete this sentence and pin it above the desk:

> Because <structural property of workloads or designs>, organizing the hardware as
> <mechanism> yields <behavioral consequence>, which we demonstrate by <instrument>.

Every section either supports that sentence or gets cut. Papers with two ideas do
worse than either idea alone at this venue — the review form's "key contribution"
box forces a choice, and reviewers make it less charitably than authors would.

## The load-bearing motivation section

The distinctive ISCA move is Section 2 as a *measured* motivation: characterization
data showing the problem exists at magnitude, on workloads the community accepts,
before any proposal appears. A motivation built from citations alone reads as
secondhand. Aim for two or three characterization plots whose captions alone
establish (a) the bottleneck, (b) its trend across configurations or generations,
and (c) why existing mechanisms cannot close it. This section frequently decides
the paper's fate: it is where reviewers decide whether the problem is real.

## Mechanism description at checkable precision

Reviewers must be able to mentally simulate the design. That requires:

- A block diagram naming every added structure, with sizes (entries, bits, ports).
- The walk-through: one concrete event traced end to end through the mechanism
  ("a load misses in L2; the tracker allocates entry E; ...").
- Every policy decision stated with its trigger and its fallback.
- A hardware-cost paragraph: storage, comparators, wiring implications, and where
  in the pipeline the logic sits — even a conservative estimate beats silence.

The failure pattern is prose that describes what the mechanism *achieves* where the
reader needs what it *does*. "The prefetcher adapts to phase changes" is a claim;
"the confidence counter decays every 4K cycles, and entries below threshold T stop
issuing" is a mechanism.

## Calibrated numbers, always with their instrument

Quantitative claims carry their evidence class with them. A useful internal
discipline while drafting:

| Draft phrase | Rewrite that survives review |
|---|---|
| "improves performance by 34%" | "improves geomean IPC by 34% over <baseline> on <suite> in <simulator+config>" |
| "adds negligible overhead" | "adds 18.4 KB of SRAM per core and one pipeline stage on the miss path" |
| "significantly outperforms" | delete "significantly" unless a statistical test appears |
| "our design scales well" | "speedup holds within 5% from 4 to 64 cores (Fig. 9)" |
| "energy-efficient" | "reduces modeled DRAM energy 21% (tool, node, and caveats in §5.1)" |

Absolute claims from relative instruments are the venue's best-known writing sin;
`isca-experiments` covers the underlying methodology contract.

## Budgeting the 11 pages

References are unlimited (verified for 2026), so never starve the bibliography to
save space. A budget that has served the venue's structure well:

```text
1.0   Introduction: problem, insight sentence, contribution list with numbers
1.5   Motivation/characterization: measured, workload-grounded
0.5   Background only if genuinely non-standard; else fold into motivation
3.0   Design: overview figure -> mechanism detail -> walk-through -> cost
1.0   Methodology: instruments, configs, workloads, baselines (see
      isca-experiments; reviewers read this section early)
3.0   Evaluation: headline -> attribution/sensitivity -> overheads -> limits
0.5   Related work (see isca-related-work) + conclusion
= 10.5 of 11, leaving slack for review-driven revision growth
```

Figures deserve disproportionate care: at this venue the design figure and the
headline results figure are what the PC remembers. Design figures should be
redrawn, not screenshotted from slides; results figures need readable axes at
print size and a caption that states the takeaway, not just the contents.

## Sentence-level habits of accepted papers

- Present tense for the design ("the controller tracks"), past tense for
  experiments ("we measured").
- Name structures once and reuse the name exactly; synonyms ("the table", "the
  buffer", "the tracker") force reviewers to guess whether they are one structure.
- Contributions listed as falsifiable statements with pointers ("§5 shows X under
  Y"), not as activities ("we propose, we evaluate").
- Anticipate the obvious objection in-line, once, briefly: "unlike prior decoupled
  designs, no global stall is required because ...". Do not litigate every
  possible objection in the text; that is what the rebuttal window is for.
- Acronym hygiene: define at first use, and assume a reviewer from an adjacent
  subarea (a memory person reading your core paper) throughout.

## Revision-friendliness is a 2026-cycle feature

Because ISCA's review process includes a revision phase (February 16 - March 6 in
the 2026 cycle), write so the paper can absorb change: keep one results subsection
per claim (swappable), avoid cross-references to "the previous paragraph", and
keep 0.5 page of slack. A paper packed to the last line at submission has nowhere
to put the experiment a reviewer asks for.

## Self-edit gate before the deadline

```text
[ ] Insight sentence appears, verbatim or nearly, in abstract and intro
[ ] Motivation section contains measured data, not only citations
[ ] Every added structure has a size; every policy has a trigger
[ ] Every headline number names baseline + workload + instrument
[ ] Figures legible printed at 100%; captions state takeaways
[ ] 0.5 page of revision slack preserved
[ ] References complete and NOT anonymized (2026 rule: never blind references)
```

Format numbers verified 2026-07-08 against the ISCA 2026 guidelines
(`../../resources/official-source-map.md`); the 2027 template and limits are 待核实
until the new site posts them.
