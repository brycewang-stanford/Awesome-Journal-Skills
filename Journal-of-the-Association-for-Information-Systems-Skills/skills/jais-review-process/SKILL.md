---
name: jais-review-process
description: Use when calibrating expectations for the Journal of the Association for Information Systems (JAIS) editorial process — the developmental, Senior-Editor-led, double-blind review; how the seven-category routing works; what a JAIS decision letter means; and when to engage the journal's developmental culture. Sets expectations and reads decisions; it does not draft the response (jais-rebuttal) or run the submission preflight (jais-submission).
---

# Review Process (jais-review-process)

## When to trigger

- You are about to submit and want to understand how JAIS will handle the paper
- A decision letter arrived and you need to read it correctly before reacting
- You are unsure who owns the decision (Senior Editor vs. reviewers) and how to weight comments
- You want to understand JAIS's "developmental reviewing" culture and how to engage it
- You are deciding whether a major-revision invitation is worth the effort or signals a likely path to acceptance

## Fit is screened before quality

Like its Basket siblings, JAIS screens **fit** before it spends reviewer effort on quality — the Editor-in-Chief (or a deputy) assesses whether the paper belongs in JAIS and in the declared category before routing it for full review. This is why a technically excellent paper can be desk-rejected: not because the work is weak, but because the contribution is not a JAIS contribution, or the category is wrong. Practically, the fit screen rewards the upstream work in `jais-topic-selection` and `jais-contribution-framing` more than any amount of late polish. If you keep getting desk rejects, the problem is almost always fit or contribution, not execution.

## How JAIS review actually works

JAIS runs a **double-blind** process: the Editor-in-Chief routes a submission, typically to a **Senior Editor** in the relevant category, who manages the review (commonly through an Associate Editor and reviewers). The distinctive feature is the journal's stated commitment to **"developmental reviewing"** with "an editorial board of eminent scholars engaging with authors on promising papers" — JAIS frames itself as trying to *build* good papers, not merely gate them. Practically: the SE's letter is the authoritative synthesis of where the paper stands and what it needs, and a developmental tone in the letter is a real signal that the editor sees promise.

> The masthead changes: Monideepa Tarafdar is Editor-in-Chief (effective Sept 1, 2024); category Senior Editors (e.g., Literature Reviews — Gregory Vial; Research Perspectives — Dirk Hovorka; Foundational — Varun Grover; Policy and Impact — Roman Beck) are 待核实. Confirm at aisel.aisnet.org/jais.

## Category routing shapes the review

Because JAIS has seven categories each with its own SE, **the category you chose at submission determines who reviews you and against what bar**. A Theory submission is read for generative theory; a Foundational submission for disciplined description of a novel phenomenon; a Literature Review for method and theoretical payoff. If a paper is mis-categorized, expect a fit challenge or a re-route before substantive review — which is why category selection (`jais-topic-selection`) is upstream of everything.

## What the seven Senior Editors signal about routing

Each category's Senior Editor brings that genre's standards, so the *identity* of your handling editor is a clue to what your reviews will emphasize. A Theory submission routed to the Theory SE will be pressed hardest on construct novelty and generativity; a Literature Review under Gregory Vial on method and theoretical payoff; a Research Perspective under Dirk Hovorka on the strength and defensibility of the argument; a Foundational submission under Varun Grover on disciplined description of a genuinely novel phenomenon; a Policy and Impact paper under Roman Beck on the credibility of the research-to-policy bridge (SE names 待核实 — confirm before relying on them). If your paper would be stronger under a different category's bar, that is a topic-selection signal, not a review-process one.

## Read the decision letter for what it actually says

| Decision | What it usually means | Your move |
|----------|-----------------------|-----------|
| **Desk reject** | fit, theory, or contribution failed the editor's screen | re-diagnose fit/contribution; do not just resubmit |
| **Reject (after review)** | reviewers see a fundamental theory or design flaw | treat as terminal unless explicitly invited to resubmit |
| **Major revision** | promise is real but substantial work remains | the most common path to a JAIS paper — engage fully |
| **Minor revision** | the contribution is accepted; execution polish remains | address precisely; do not reopen settled debates |

A developmental SE letter on a major revision is closer to a roadmap than a verdict. Mine it for the editor's priorities; those, not reviewer word-count, set your revision plan.

## Timeline and expectations, calibrated

JAIS, like its Basket siblings, runs a multi-round developmental process: an initial decision, then typically one or more rounds of major then minor revision before acceptance. Plan for this. A first-round major revision is the *normal* path to publication, not a near-miss; the work happens across rounds as the SE and reviewers engage the paper. Treat exact turnaround times, acceptance rates, and impact-factor figures as **待核实** — they move and vary by category — and do not let an optimistic timeline tempt you into a thin, rushed revision that squanders a developmental opening.

## Weight the comments by authorship

The **Senior Editor owns the decision.** When reviewers conflict, resolve in the direction the SE signals and say so. Reviewer points that the SE did not elevate still deserve a response, but the SE's synthesis is the spine of the revision. Reading the letter this way prevents the classic error of treating every reviewer comment as equally binding.

## Checklist

- [ ] You know which category SE is managing the paper and the bar that implies
- [ ] The decision type is read correctly (desk reject vs. reject vs. major vs. minor)
- [ ] The SE's elevated priorities are extracted and ranked above scattered reviewer points
- [ ] Reviewer conflicts are identified and a resolution direction (per the SE) is noted
- [ ] The developmental tone (or its absence) is read as a promise signal
- [ ] Expectations for revision scope and timeline are realistic for the decision type
- [ ] Volatile facts (SE names, timelines, acceptance rate, impact factor) are treated as 待核实

## Engage the developmental culture deliberately

JAIS's "developmental reviewing" is a resource, not just a label. When an SE letter is constructive and specific, treat it as collaborative coaching: respond to the *spirit* of the editor's concern, not only its letter, and signal in the revision that you understood where the paper is trying to go. JAIS also runs activities that reflect this ethos (for example, theory-development engagement around the IS community); a paper whose authors treat reviewers as partners in building the contribution tends to fare better than one that litigates every point. This is a meaningful contrast with more gatekeeping-style processes elsewhere.

## Worked reading of a decision letter (illustrative)

An SE writes: "All three reviewers find the phenomenon timely, but the theoretical contribution is not yet distinct from prior work; R2's identification concern is secondary to this." Read correctly, this is a developmental **major revision** whose single binding constraint is the theory contribution — not R2's identification point, which the SE has explicitly demoted. The revision plan should therefore lead with sharpening the construct/framework (route to `jais-theory-development` and `jais-contribution-framing`), then address identification proportionately. Spending the revision budget on robustness checks while leaving the theory thin would answer the loudest reviewer and miss the editor — the most common way a promising JAIS R&R fails.

## Anti-patterns

- Reacting to a developmental major-revision letter as if it were a rejection.
- Treating all reviewers as equal and ignoring the Senior Editor's synthesis.
- Resubmitting a desk-rejected paper without re-diagnosing fit, theory, or contribution.
- Reopening points the SE already settled, or arguing with the editor's stated priorities.
- Assuming JAIS works like ISR (INFORMS) or MISQ procedurally — the routing, categories, and developmental ethos differ.

## Output format

```text
【Journal】Journal of the Association for Information Systems (JAIS)
【Category SE / bar】who is managing and against what standard
【Decision read】desk reject / reject / major / minor
【SE priorities (ranked)】1… 2… 3…
【Reviewer conflicts】where, and resolution direction per SE
【Promise signal】developmental tone present / absent
【Source status】verified URL / 待核实 (SE names)
【Next skill】jais-rebuttal (on a revision invite)
```
