---
name: isr-review-process
description: Use to understand how Information Systems Research (ISR) handles a submission — the EIC fit gate, the Senior-Editor-led process with an Associate Editor and reviewers, double-anonymized review, and how to read an ISR decision letter. Sets expectations and interprets letters; it does not draft the response (isr-rebuttal).
---

# Review Process (isr-review-process)

## When to trigger

- You want to know what happens after you submit to ISR
- A decision letter arrived and you need to read it correctly before responding
- You are unsure who the "SE" and "AE" are and what each controls
- You want to set realistic expectations for rounds and timelines

## How ISR routes and reviews a paper

ISR uses an INFORMS-style **Senior-Editor-led** process, not departmental area editors:

1. **EIC fit gate.** The Editor-in-Chief (currently Suprateek Sarker) makes an initial **editorial fit** assessment against ISR's sociotechnical, intradisciplinary mission. Papers that are off-fit (single-paradigm with no IS contribution, IT-as-wallpaper, or a generic reference-discipline paper) can be returned here — which is exactly why the **~500-word contribution statement** in your cover letter is read first.
2. **Senior Editor (SE).** A fitting paper is assigned to a **Senior Editor** who owns the paper and ultimately makes the **final decision**.
3. **Associate Editor (AE).** The SE works with an **Associate Editor**, who solicits **2-3 reviewers** and integrates their recommendations.
4. **Reviewers.** Provide detailed assessments under **double-anonymized** review.

Understand the hierarchy when you read the letter: reviewers advise, the AE synthesizes, and the **SE decides**. The SE's letter is the one that defines what must change.

## Reading the decision letter

- **Identify the decisive voice.** Weight the **SE's** framing most; it tells you which reviewer points are binding versus optional.
- **Separate "fit/contribution" objections from "execution" objections.** A challenge to the IS contribution or the intradisciplinary framing is more fundamental than a request for another robustness check.
- **Map comments to genre.** Analytical reviewers probe assumptions and proof completeness; behavioral reviewers probe identification, validity, and CMB; design-science reviewers probe evaluation rigor. Multimethod papers draw all three — expect the SE to ask how the methods integrate (per the 2025 ISR 36(2) framework).
- **Note the verdict.** Reject, major revision, or (rarely) minor revision; first-round accepts are essentially unheard of.

## Decision-letter ledger

Build a short ledger before routing to `isr-rebuttal`. ISR letters often mix contribution, theory,
method, and electronic-companion requests; a flat checklist hides which point controls the next
round. Use these rows:

| Row | What to record | Why it matters at ISR |
|-----|----------------|-----------------------|
| SE priority | The one or two issues the SE names as decisive | The SE owns the final recommendation and adjudicates reviewer conflict. |
| IS contribution risk | Whether the paper still reads as IS theory, intradisciplinary IS, or only a reference-discipline exercise | Fit concerns outrank additional robustness because they can trigger a reject even after new analyses. |
| Genre of evidence | Analytical proof, behavioral identification, design-science evaluation, or multimethod integration | The right fix depends on genre; adding a regression does not answer an analytical proof gap. |
| Space route | Main text versus electronic companion | ISR page limits require proofs, measurement detail, and long robustness to be placed deliberately. |

The output should be a priority order, not a complete response letter. If two reviewers disagree,
write the disagreement in the ledger and attach it to the SE priority rather than averaging their
requests.

## Set expectations

ISR review is developmental and multi-round; timelines vary. Treat an R&R as an invitation to a conversation with the SE, not a checklist to clear mechanically.

## Checklist

- [ ] Decisive voice (SE) identified and weighted above individual reviewers
- [ ] Fit/contribution objections separated from execution objections
- [ ] Comments mapped to genre (assumptions / identification / evaluation)
- [ ] Multimethod-integration concerns noted if applicable
- [ ] Verdict and what it permits understood before drafting a response

## Anti-patterns

- **Treating all reviewers equally** and missing the SE's binding priorities.
- **Answering execution nits** while ignoring a contribution/fit challenge.
- **Assuming an R&R is acceptance**; the SE can still reject after revision.

## Output format

```
【Verdict】reject / major / minor
【Decisive voice】SE priorities: [...]
【Fit/contribution objections】[...]
【Execution objections by genre】[...]
【Multimethod-integration asks】[...]
【Next step】isr-rebuttal
```
