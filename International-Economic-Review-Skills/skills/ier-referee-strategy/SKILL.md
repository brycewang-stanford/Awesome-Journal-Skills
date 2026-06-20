---
name: ier-referee-strategy
description: Use when anticipating referee objections before submitting an International Economic Review (IER) manuscript, or when reading the room of an IER review. Maps the likely objections by archetype and pre-empts them; it does not draft the response letter (see ier-rebuttal).
---

# Referee Strategy (ier-referee-strategy)

## When to trigger

- The paper is near submission and you want to find the objection that would sink it before a referee does
- You are deciding what to put in the paper vs. hold in reserve for the response
- A draft is strong but you suspect one undefended assumption or one fragile number is the soft spot
- You want to calibrate expectations for IER's review (a rigor-gated, theory-leaning process)

## How IER referees read

An IER referee is usually a rigor-minded economist who reads for **whether the contribution is correct, general, and tightly linked to its evidence**. Unlike a top-5 referee, they are not primarily asking "is this important enough"; they are asking "is this right, and does it teach a general lesson." The most common reasons an IER paper stalls are: an undefended load-bearing assumption, identification that is "calibration in disguise," a headline number that moves under a reasonable perturbation, or a proof that is not airtight. Pre-empt by archetype:

| Archetype | The objection that sinks it | Pre-empt by |
|-----------|-----------------------------|-------------|
| Pure / applied theory | "The result is knife-edge / re-derives a known fact" | Perturbation test on the load-bearing assumption; state the failure boundary as a result (`ier-theory-model`) |
| Structural / quantitative | "Not credibly identified — calibration in disguise"; "counterfactual not policy-invariant" | Sensitivity matrix + untargeted-moment fit + Lucas-critique argument (`ier-identification`) |
| Econometric method | "What does this buy over the incumbent?"; "no finite-sample evidence" | Head-to-head comparison + Monte Carlo (`ier-theory-model`, `ier-robustness`) |
| Applied micro | "Staggered TWFE is biased here"; "exclusion restriction undefended" | Modern DID estimator + clean event study; theory+institutions+falsification for IV (`ier-identification`) |
| Any empirical | "Is it robust?"; "can it be replicated?" | Threat-mapped robustness + AER-compliant deposit (`ier-robustness`, `ier-replication-package`) |

### The pre-mortem routine

1. **Name the single objection most likely to sink the paper.** Be honest — it is usually the assumption or number you are quietly worried about.
2. **Decide: fix in the paper, or address in the cover/response.** A load-bearing weakness must be fixed *before* submission; a foreseeable-but-defensible concern can be flagged proactively in the cover letter.
3. **Pre-empt in the text.** For each likely objection, place the defense where the referee will look (next to the claim), not buried in an appendix they may not reach.
4. **Write the cover letter to the desk editor's filing decision.** The cover letter's job is to make the general-interest case so the paper is not mis-filed as a field-journal or Econometric Society paper (the boundary from `ier-literature-positioning`).
5. **Reserve, don't withhold.** Have additional robustness ready for the response, but never hide a known weakness — IER referees punish concealment harder than honest limitation.

### Calibrating expectations for an IER review

IER's review is rigor-gated, so the realistic outcomes skew toward "revise to make it correct and general" rather than "reject because not important enough." The desk filter is the first hurdle — the editor decides whether the paper is general-interest enough for IER or belongs at a field journal / an Econometric Society outlet, which is why the cover letter's general-interest framing matters so much. Past the desk, expect referees to drill on the single load-bearing assumption and the identification; a paper that pre-empts those two cleanly converts to an R&R far more often than one that is broad but loose. Process timing and exact desk-reject rates are 待核实 — do not promise the user a timeline.

### Worked example (illustrative)

An author is quietly worried that the headline elasticity is calibrated rather than estimated. The pre-mortem names this as the sink-objection. Rather than hope the referee misses it, the author adds a short subsection showing what data moment would identify the elasticity if estimated, reports the result holds across the calibrated range, and flags in the cover letter that the parameter is set externally for a stated reason with a sensitivity analysis attached. The known weakness is now a controlled, disclosed design choice — the worst it can draw is "please estimate it," which is a survivable R&R comment, not the fatal "calibration in disguise" reject.

### The cover letter does the desk editor's filing for them

At a general-interest journal the first decision is not the referees' — it is the editor's desk decision about whether the paper is general-interest enough for IER, or whether it belongs at a field journal or an Econometric Society outlet. Your cover letter should make that decision easy and correct: in two or three sentences, state the general object that is the contribution, name the two reader segments who care, and (implicitly) draw the sibling boundary. A cover letter that pitches importance like a top-5 submission, or that reads like a field-journal abstract, invites a desk reject or a mis-routing. Treat the cover letter as the editor's filing aid, written in IER's frame of rigor-plus-generality.

### Pre-empt where the referee looks, not where it is convenient

A defense placed in an appendix the referee never opens is no defense. For each likely objection, put the answer next to the claim it protects: the assumption defense next to the assumption, the identification argument next to the estimate, the robustness pointer next to the headline result. The pre-mortem is only useful if it changes *placement*, not just whether the content exists somewhere in the manuscript. An IER referee reading linearly should hit the defense at the moment the doubt arises — that is what converts a potential reject comment into a non-issue.

## Checklist

- [ ] The single most-likely-to-sink objection is named and triaged (fix-now vs. flag-in-cover)
- [ ] Each archetype-specific objection has a defense placed next to the relevant claim
- [ ] The load-bearing assumption is defended in the text, not the appendix
- [ ] Identification objections pre-empted (sensitivity / modern DID / exclusion defense as the branch requires)
- [ ] Robustness is threat-mapped so "is it robust?" already has an answer
- [ ] The cover letter makes the general-interest case and draws the sibling boundary
- [ ] Reserve robustness prepared for the response without hiding any known weakness

## Anti-patterns

- Hoping the referee misses the weak assumption instead of pre-empting it
- Burying the defense of the load-bearing claim in an appendix the referee may not open
- A cover letter that pitches importance (top-5 frame) instead of general-interest rigor (IER frame)
- Withholding a known limitation to "see if they notice" — concealment is the fastest reject
- Treating the review as a top-5 importance contest rather than a correctness-and-generality test

### Branch-specific soft spots to audit before submitting

- **Theory:** is any key result proved only for a convenient functional form? Is uniqueness asserted? Those are the first things a theory referee probes.
- **Structural:** can a reader see what identifies each parameter, and is the counterfactual's policy-invariance argued? "Calibration in disguise" is the modal structural reject.
- **Method:** is there a head-to-head against the incumbent estimator with finite-sample evidence? Asymptotics alone rarely satisfy.
- **Applied:** is the design modern (no naive staggered TWFE), and does the answer speak to a general mechanism rather than one institution?

Audit your paper against its branch's list before the pre-mortem — the soft spot is almost always on it.

## Output format

```text
【Journal】International Economic Review
【Skill】ier-referee-strategy
【Archetype】theory / structural / method / applied-micro
【Sink-objection】the single objection most likely to reject the paper
【Triage】fix-now / flag-in-cover-letter
【Pre-empts placed】objection → where the defense sits in the text
【Cover letter】general-interest case + sibling boundary drawn? [Y/N]
【Reserve】extra robustness ready for the response (nothing concealed)? [Y/N]
【Verdict】defensible / soft-spot-remains
【Next skill】ier-submission
```
