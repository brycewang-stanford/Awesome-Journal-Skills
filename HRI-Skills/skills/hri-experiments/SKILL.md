---
name: hri-experiments
description: Use when designing or auditing the human-subjects study at the heart of an ACM/IEEE HRI full paper — choosing between/within-subjects designs, running Wizard-of-Oz honestly, powering the sample, reporting statistics with effect sizes and qualitative rigor, selecting validated scales, adding manipulation checks, pre-registering, and meeting HRI's human-participants ethics obligations.
---

# HRI Experiments

The human-subjects study is HRI's currency. A brilliant robot behavior with a broken study fails;
a modest behavior with an airtight study can win a Best Paper. HRI reviewers — drawn from
psychology and HCI as well as robotics — hold study design to a standard closer to experimental
psychology than to a robotics benchmark. This skill covers the design decisions that decide the
paper, and HRI's specific ethics obligations. It pairs with the shared reporting kit in
[`../../resources/code/README.md`](../../resources/code/README.md).

## Match the evidence to the claim

Decide what *kind* of claim you are making, then design to it:

| Claim shape | Evidence HRI expects |
| --- | --- |
| "Robot behavior X changes outcome Y" (causal) | A controlled experiment manipulating X, measuring Y, with a manipulation check and effect sizes |
| "People experience the robot as Z" (perception) | A validated instrument for Z, adequate power, and honest CIs |
| "This interaction/design works better" | A comparison with a fair baseline and a behavioral or task outcome, ideally shown on video |
| "Here is how people make sense of robots" (qualitative) | A rigorous qualitative method (thematic/grounded), reflexivity, transferable insight — not counts |
| "This method/measure is valid" (methods) | Psychometric or methodological evidence, not a single-use demo |

A mismatch — e.g., claiming behavior change but measuring only a liking scale — is the most common
reason an HRI study is judged inadequate.

## Choose the design deliberately

- **Between-subjects** — each participant sees one condition. Cleaner (no carryover, no demand from
  seeing the manipulation) but needs more participants for the same power. Default when exposure to
  the robot changes people.
- **Within-subjects** — each participant sees all conditions. More powerful per participant, but risks
  order effects (counterbalance) and demand characteristics (participants guess the hypothesis).
- **Mixed** — a between factor (e.g., robot type) crossed with a within factor (e.g., task phase).
- Justify the choice in the paper; reviewers will ask why. State counterbalancing and how you
  controlled order/demand for within-subjects designs.

## Wizard-of-Oz, done honestly

Wizard-of-Oz (WoZ) — a human covertly controlling some robot behavior — is a legitimate and common
HRI method, but it is a credibility minefield if mishandled:

- **Disclose it.** State clearly what was **autonomous** and what the **wizard** controlled.
  Presenting teleoperated behavior as autonomous is a serious integrity problem reviewers actively
  probe.
- **Constrain and log the wizard.** Define the wizard's action space, script or protocol, and report
  **wizard error rates** and training; an unconstrained wizard makes the stimulus irreproducible and
  the condition ill-defined.
- **Watch consistency.** Wizard behavior must be consistent across participants and conditions, or
  the "manipulation" is really wizard variance.
- Cite and follow the community's WoZ **reporting guidance** (a well-known systematic review lives in
  the JHRI journal — see the exemplars-library guard; it is a *journal* work, cite it as such).

## Power, sample size, and analysis

- **Power the study.** Estimate sample size from an expected effect size (from pilots or prior HRI
  work) before collecting data; an underpowered null is uninformative. Report the basis for N.
- **Report effect sizes and confidence intervals**, always — Cohen's d, η², odds ratios, or the
  appropriate measure — not just p-values. HRI reviewers increasingly treat "significant, no effect
  size" as incomplete.
- **Correct for multiple comparisons** when you run many tests; a scale battery with no correction
  invites the "garden of forking paths" critique.
- **Pre-register** the primary hypothesis and analysis where you can, and clearly separate
  **confirmatory** from **exploratory** results. Label post-hoc findings as post-hoc.
- **Check assumptions** and use methods appropriate to your data (ordinal Likert data, repeated
  measures, nested/mixed models for multi-trial designs).

## Validated scales and constructs

Prefer established, validated instruments over homemade items so results are comparable and the
construct is defensible:

- Robot-perception constructs commonly use published scales for anthropomorphism/animacy/likeability,
  warmth and competence, trust, negative attitudes toward robots, and similar. Cite the scale to its
  source and report reliability (e.g., Cronbach's α) for your sample.
- If you must build a measure, justify it, pilot it, and report its properties — reviewers distrust
  an ad hoc single item for a rich construct.
- Include a **manipulation check** so you can show the intended difference was actually perceived.

## Qualitative and mixed methods

HRI values qualitative rigor, not just experiments:

- Name the method (thematic analysis, grounded theory, interaction analysis) and follow it; report
  coding process, and inter-rater reliability *where the method calls for it* (not all do).
- Practice **reflexivity** — who coded, their stance, how themes were derived — instead of implying a
  false objectivity or a fake "n."
- In mixed-methods work, say how the strands integrate (triangulation, explanation, expansion), not
  just that both exist.

## Ethics is not optional at HRI

Submitting binds you to **ACM's Policy on Research Involving Human Participants and Subjects**:

- Obtain and **state IRB/ethics approval** (or a documented exemption rationale); report **informed
  consent**.
- If the study uses **deception** (common with WoZ or staged robot failures), justify it and describe
  **debriefing**.
- Protect participants and data: de-identify, secure recordings, and mind vulnerable populations
  (children, older adults, clinical) with extra care.
- Anonymize ethics details for review (institution names can leak identity — see `hri-submission`),
  but do not omit that approval exists.

## Anti-patterns HRI reviewers flag

- **Undisclosed or unconstrained Wizard-of-Oz.**
- **Underpowered study** with a null spun as evidence of no effect.
- **Scale battery + no correction + no pre-registration** (fishing).
- **Liking/rating as a stand-in** for the behavioral or theory-linked outcome the claim needs.
- **Missing manipulation check** — no evidence the manipulation worked.
- **No effect sizes**; **p < .05** treated as the whole result.
- **Qualitative work reported as frequencies** with no method named.

## Output format

```text
[Claim ↔ evidence] claim shape and whether the design measures it
[Design] between/within/mixed · justified · counterbalanced?
[WoZ] used? autonomy vs wizard disclosed · wizard constrained + error reported?
[Power/stats] N basis · effect sizes + CIs · multiple-comparison correction · pre-registered?
[Measures] validated scales cited + reliability · manipulation check present?
[Qualitative] method named · reflexivity · integration (if mixed)?
[Ethics] IRB/consent stated · deception justified + debriefed?
[Fix queue] <ordered, design fixes before data collection where possible>
```
