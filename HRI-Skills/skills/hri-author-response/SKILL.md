---
name: hri-author-response
description: Use when writing the single ACM/IEEE HRI full-paper rebuttal that responds to three external reviewers and two area chairs — triaging study-design and statistics critiques, correcting misreadings, promising only what a camera-ready can deliver, staying anonymous and within the length limit, and giving the online reviewer discussion reasons to raise scores.
---

# HRI Author Response (Rebuttal)

HRI gives you **one** rebuttal, and it matters: because reviewers **discuss and can revise scores
after** it, a focused rebuttal routinely changes decisions. But it is a conference rebuttal, not a
journal revise-and-resubmit — you cannot run a new study before the deadline, and there is **no
in-cycle major-revision round**. The job is to make the reviewers who read your paper feel their
concerns were heard and, where they are genuinely wrong, corrected. Timing for the HRI 2026 cycle:
rebuttal due ~12 Nov 2025 (see `resources/official-source-map.md`); confirm the length/format limit
in the current instructions (**待核实**).

## Before writing: triage every point

For each concern across the three externals and two ACs, sort into:

- **Misreading** — the reviewer misunderstood something already in the paper. Correct it crisply,
  quoting where it is (section/figure), without blaming the reviewer.
- **Fixable in camera-ready** — a clarification, an added analysis you already have, a missing
  citation, a reframed claim. Promise the *specific* change and, where possible, give the result now.
- **Real limitation you cannot fix now** — a design choice, a sample bound, a construct-validity
  concern. Acknowledge it honestly, argue why it does not sink the contribution, and scope the claim
  accordingly. Do not pretend it away.

Then rank by **decisiveness**: which concern, if resolved, actually flips a reviewer or wins the
discussion. Spend your limited space there, not on the easy points.

## Answer the HRI-typical critiques

HRI reviews cluster on study and interaction issues; have crisp answers ready:

- **"Underpowered / N too small."** Report your power basis, effect sizes with CIs already in the
  paper, and — if applicable — that the observed effect is large enough to matter. Do not promise
  "we will collect more data" (you cannot before camera-ready); argue the evidence you have.
- **"Confound / demand characteristics."** Point to the manipulation check, counterbalancing, or
  controls already present; if a real confound exists, bound its plausible effect honestly.
- **"Wizard-of-Oz not convincing / undisclosed."** Clarify what was autonomous vs. wizard-controlled
  and the wizard constraints/error logging; if you buried it, promise to foreground it.
- **"Just a liking score, not behavior."** Point to any behavioral/task outcome you measured; if the
  claim overreached the measure, narrow the claim rather than defend the overreach.
- **"Statistics questionable."** Address multiple-comparison correction, the confirmatory/exploratory
  split, and assumption checks; commit to a re-analysis in camera-ready if warranted.
- **"Novelty / positioning."** State the delta against the specific prior work cited, without
  breaking anonymity (third person).
- **"Ethics unclear."** Confirm IRB/consent and (anonymized) deception/debriefing details.

## Promise only what the camera-ready can deliver

The rebuttal's currency is credibility. Every promise should be something you can actually do in the
final version within the 8-page budget: rephrase a claim, add an already-computed analysis or effect
size, foreground a disclosure, add a citation, clarify a figure. **Never** promise a new study, new
data collection, or a result you have not computed — reviewers discount vague promises and remember
broken ones.

## Structure and constraints

- **Group by concern, not by reviewer**, when multiple reviewers raise the same issue — answer it
  once, well, and note it addresses R1/R3.
- Lead with the **most decisive** points; a tight limit means the last third may be skimmed.
- Be **concrete and quantitative**: quote the section, give the number, name the exact change.
- **Stay within the length limit** and any format rules; over-length rebuttals can be truncated.
- **Stay anonymous** — no author/institution names, no identifying links, no "as we showed in [our
  other paper]" in first person.
- **Professional tone.** Thank reviewers briefly, never argue with their competence or tone; give the
  sympathetic reviewer material to defend you in the discussion.

## What not to do

- Do not concede your central contribution to sound agreeable — if the core claim is sound, defend it.
- Do not sprawl across every minor point and run out of room for the decisive one.
- Do not introduce a brand-new claim or result the reviewers had no chance to vet.
- Do not break anonymity to prove a point.

## After the rebuttal

The 1AC opens an **online discussion**; you will not see it. Your rebuttal is the last input you
control before the PC meeting, so make it self-sufficient. If accepted (possibly with shepherding),
carry every promise into `hri-camera-ready`; if rejected, mine the reviews and re-route with
`hri-topic-selection`.

## Output format

```text
[Triage] concerns sorted: misreading / camera-ready-fixable / real-limitation
[Decisive points] the 2-3 objections the rebuttal must win, per reviewer
[Responses] each: correction or promised change, concrete + quantitative
[Promises] all deliverable in camera-ready within 8 pages? no new-study promises?
[Anonymity + length] third-person, within limit?
[Draft] <the rebuttal, grouped by concern, decisive-first>
```
