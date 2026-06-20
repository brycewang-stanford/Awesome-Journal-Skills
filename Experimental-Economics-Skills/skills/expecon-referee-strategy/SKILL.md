---
name: expecon-referee-strategy
description: Use when anticipating the experimentalist referee's objections for an Experimental Economics (ExpEcon) manuscript before submission. Pre-empts the standard pushbacks; it does not draft the response letter (see expecon-rebuttal).
---

# Referee Strategy (expecon-referee-strategy)

## When to trigger

- The paper is analytically done and you want to pre-empt the objections an ExpEcon referee will raise
- You suspect a specific weak point (a borderline procedure, modest power, a confound) and want to disarm it before submission
- You need to decide what to add now vs. defend in the letter later
- You want to read the draft the way two editors and two anonymous referees will

## Who reviews you here, and what they look for

Experimental Economics uses **anonymous (double-blind) refereeing**, and accepted papers need the approval of **two editors** (检索于 2026-06；以官网为准). Your referees are practicing experimentalists. They are unimpressed by topical novelty and intensely focused on **design integrity**. They read in a predictable order: gates first, then the contrast, then inference, then reproducibility. Pre-empt each.

## The standard pushbacks, ranked by lethality

1. **"This is deception / the incentives aren't real."** Lethal and binary. If any procedure could be read as deceptive, name it explicitly and explain why it is *not* deception under the ESA definition (withholding ≠ misstating). Confirm every elicitation is incentive-compatible and report realized payments. Do not leave the referee to wonder.
2. **"It's underpowered / the unit of inference is wrong."** The most common substantive rejection. Pre-empt with a power/MDE statement at the **session/matching-group** level and group-level inference. A precise null beats a noisy positive.
3. **"A confound, not the mechanism."** Referees hunt for the alternative explanation: comprehension differences, session effects, order/learning, demand effects, experimenter effects. For each plausible alternative, show the design rules it out *or* report the test that does.
4. **"The treatment contrast is impure."** If a treatment changes more than one thing, a referee will say the effect is unattributable. Show the minimal-pair logic, or add the control treatment that isolates the dimension.
5. **"The behavioral models aren't actually distinguished."** If rival accounts predict the same data, the experiment is undiscriminating. Show where predictions diverge and that your design sits on that divergence.
6. **"Not reproducible / instructions missing."** Have the instructions and z-Tree/oTree code ready at submission; referees check them for deception and comprehension.
7. **"Why here and not JEBO/GEB?"** If a referee thinks the contribution is topical (JEBO) or theoretical (GEB), they may recommend transfer. Make the *methods* contribution explicit.

## Turning anticipated objections into pre-emptive moves

- For each top objection, decide: **fix now** (add a treatment/analysis), **disclose and bound** (report the limit honestly with the test), or **defend in text** (a paragraph that pre-rebuts). Build a small internal table before submitting.
- Add a short **"threats to validity" or "robustness" subsection** that names the alternatives and the test for each — referees reward authors who do their job for them.
- Suggesting appropriate (non-conflicted) referees and clearly framing the methods contribution in the cover letter can shape who reviews and how.

## A pre-submission self-review pass

Read your own draft in the referee's order and answer out loud:

1. **Gates** — Could any sentence in Procedures be read as deception? Are all incentives real and incentive-compatible? Is this stated explicitly?
2. **Power** — What is the MDE at the group level, and did the study have power to detect it? Would a referee call the n of *groups* (not subjects) thin?
3. **Confounds** — List every alternative explanation a smart experimentalist would propose; for each, is there a design feature or test that kills it?
4. **Purity** — Does each treatment manipulate exactly one thing?
5. **Discrimination** — Do my contrasts actually separate the competing models, or do they all predict the same pattern?
6. **Repro** — If a referee opened the appendix right now, are the instructions and code there and legible?

If any answer is weak, that is the item to fix or pre-empt before the desk editor ever sends it out.

## The demand-effect and experimenter-effect family

Beyond the headline gates, experimentalist referees reliably probe a cluster of subtle validity threats — treat them as first-order, not nitpicks:

- **Demand effects** — did the design telegraph the hypothesis? Pre-empt with neutral framing, a post-experiment guess question, and (if needed) an obfuscated cover task.
- **Experimenter effects** — could the experimenter's presence or scripting bias responses? Use standardized on-screen instructions and double-blind payment where social-image is at stake.
- **Order/learning effects** — counterbalance and test, or justify a between-subject design.
- **Selection into the lab** — acknowledge the recruited pool and what it does and does not represent.
- **House money / wealth effects** — pay one random round; do not let accumulated earnings contaminate later choices.

For each, the winning move is the same: name the threat in a short validity subsection and show the design feature or test that addresses it, so the referee sees you raised it first.

## Worked vignette (illustrative)

An auction experiment expects the "your stakes are hypothetical in the practice rounds" line to pass unnoticed. A self-review flags it as an incentive-compatibility gap a referee will pounce on. The pre-emptive move: state clearly that *only* practice rounds were unpaid, that all decision rounds were paid via one-randomly-selected-round, and report the realized average payment — turning a likely first-round objection into a non-issue before it is raised.

## Shaping the cover letter and reviewer pool

Under double-blind review you cannot influence the referees' identities, but you can influence *who the editors think should review it* and *how they frame the contribution*. A cover letter that names the methods advance in one crisp sentence steers the paper toward experimentalist referees rather than topical ones. Suggesting two or three non-conflicted experts who know the *procedure* you use (not just the topic) helps the editors route the paper to readers who can evaluate the design on its merits — and who are less likely to mistake a methods paper for a JEBO-style topic paper.

## Checklist

- [ ] The no-deception and incentive-compatibility defenses are explicit in the text, not implicit
- [ ] Power/MDE and group-level inference pre-empt the "underpowered/wrong unit" objection
- [ ] Each plausible confound (comprehension, session, order, demand, experimenter) has a design answer or a test
- [ ] The minimal-pair purity of each contrast is shown
- [ ] Rival behavioral models are shown to be distinguished by the design
- [ ] Instructions + experiment code ready for referees at submission
- [ ] The methods contribution is explicit enough to resist a "transfer to JEBO/GEB" suggestion

## Anti-patterns

- Hoping a borderline procedure goes unnoticed instead of pre-empting the deception question
- A robustness section that lists checks but never names the alternative explanation each addresses
- Ignoring the unit-of-inference objection that nearly every experimentalist referee raises
- Leaving the methods contribution implicit, inviting a transfer recommendation
- Treating referee suggestions of demand effects as nitpicks rather than first-order threats

## What the desk editor screens before referees ever see it

Two editors stand between you and acceptance, and a desk screen comes first. The fastest desk rejects at this journal are: a **deception** procedure; **non-incentivized** choices; **missing instructions**; and an obvious **method mismatch** (a topic paper that should be at JEBO, or a short note that should be at JESA). None of these are about quality — they are about fit and gates. Clear all four in the first read of your own draft, because no amount of clever analysis survives a procedure the editor reads as deceptive on page 6.

## Output format

```text
【Journal】Experimental Economics (ESA method flagship)
【Skill】expecon-referee-strategy
【Verdict】ready / pre-empt-first
【Top objections】ranked (gates → power/unit → confound → purity → models → repro)
【Per objection】fix-now / disclose-and-bound / defend-in-text
【Threats subsection】present and names each alternative + test? [Y/N]
【Methods contribution】explicit enough to resist transfer? [Y/N]
【Next skill】expecon-submission
```
