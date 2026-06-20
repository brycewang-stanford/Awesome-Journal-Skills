---
name: aejmac-referee-strategy
description: Use when anticipating the objections referees and coeditors will raise on an American Economic Journal: Macroeconomics (AEJ: Macro) manuscript, and calibrating desk-reject and revision odds, before submission. Pre-empts pushback and plans the review; it does not draft the post-decision response letter (use aejmac-rebuttal).
---

# Referee Strategy (aejmac-referee-strategy)

## When to trigger

- The draft is near-complete and you want to find the holes a referee will exploit
- You are gauging desk-reject risk or whether the paper is "ready"
- You need to decide which robustness checks to run *before* submitting vs. hold in reserve
- You want to pre-empt the predictable macro objections in the paper itself

## How AEJ: Macro review works (verified 2026-06; re-confirm on the official AEA pages)

- Managed by the **Editor** (Ayşegül Şahin, 检索于 2026-06；以官网为准) and **coeditors**; **single-blind** external peer review (the author is known to the referee; referees are anonymous to the author). Note this is **single-blind**, unlike some AEJs/economics venues that anonymize the author.
- **Desk rejection** is possible without referees; editorial decisions weigh the probability of meeting AEJ: Macro standards, **breadth of topic, and interest to the AEJ: Macro audience**.
- After conditional acceptance, the **AEA Data Editor** runs the reproducibility check before publication (see `aejmac-replication-package`).

## The predictable macro objections (pre-empt each in the paper)

| Objection a macro referee raises | Where it lands | Pre-emption |
|---|---|---|
| "The identifying assumption is not defended" (Cholesky ordering, sign set, exclusion) | identification | Argue the assumption economically; show robustness to alternatives (`aejmac-identification`) |
| "The shock is anticipated / endogenous" | identification | Show unpredictability from macro history; use narrative/high-frequency instruments |
| "This is a Great-Moderation / pre-ZLB artifact" | robustness | Sample splits across the breaks, baseline shown alongside (`aejmac-robustness`) |
| "Calibration is undisciplined / free parameters" | theory-model | Source every parameter; targeted + untargeted moments; sensitivity |
| "The counterfactual ignores the Lucas critique" | theory-model | Argue policy-invariance of estimated parameters |
| "SVAR and LP would disagree" | robustness | Run the cross-method check and show agreement |
| "Set-identified results reported as a point" | identification / tables | Report the identified set / median-target with a band |
| "Not broad enough for AEJ: Macro" | topic / positioning | Re-frame for general interest; name the audience (`aejmac-topic-selection`) |
| "Results not reproducible" | replication | Build the openICPSR package early, incl. simulation code |

## Calibrating the odds

- **Desk-reject risk is high when**: breadth is thin (a field-specialist paper), the contribution sentence is missing, or the headline quantity is buried. Fix with `aejmac-topic-selection` / `aejmac-literature-positioning` / `aejmac-writing-style` *before* submitting.
- **R&R is likely when** the question is broad and the result credible but the robustness/identification defense is incomplete — referees will ask for the checks. Pre-running the obvious ones shortens the cycle.
- **Hold-in-reserve strategy**: run the decisive robustness checks before submission; keep a second tier ready to deploy in the response letter rather than front-loading every table.

## Suggesting referees & framing the cover

- Suggest referees who span the **theory and empirical** sides if the paper is a hybrid, so neither side is judged only by the other camp.
- The cover letter / framing should state the **broad-interest claim and the headline quantity** plainly — give the editor the breadth argument they need to send it out.

## Checklist

- [ ] Each predictable macro objection above has a one-paragraph + one-exhibit answer in the paper
- [ ] Desk-reject risk assessed (breadth, contribution sentence, headline visibility)
- [ ] Decisive robustness/identification checks run before submission
- [ ] Second-tier checks identified to hold in reserve for the response
- [ ] Referee suggestions span the relevant theory/empirical communities
- [ ] Single-blind reviewed: nothing in the paper assumes anonymity of the author

## Anti-patterns

- Submitting before the obvious adversarial robustness check is run
- Assuming double-blind anonymity (AEJ: Macro is single-blind)
- A paper a desk editor cannot pitch as broad-interest in one sentence
- Front-loading every conceivable robustness table, leaving nothing for the response
- Suggesting only referees from one camp for a hybrid paper

## Output format

```
【Top 3 objections this paper invites】1) ... 2) ... 3) ...
【Pre-emption status】answered-in-paper / needs-work for each
【Desk-reject risk】low / medium / high + why
【Run-now vs. reserve checks】...
【Referee suggestions span】theory + empirical? [Y/N]
【Next step】aejmac-submission
```
