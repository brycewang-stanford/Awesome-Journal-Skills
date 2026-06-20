---
name: orgstud-rebuttal
description: Use when drafting the response to reviewers and the revision plan for an Organization Studies (OS) R&R — turning developmental, theory-level reviewer comments into a credible point-by-point reply and revised manuscript. Plans and drafts the response; it does not redo the underlying analysis (route back to the specialist skills).
---

# Rebuttal Strategy (orgstud-rebuttal)

## When to trigger

- An OS R&R arrived (read it first with `orgstud-review-process`) and you are drafting the response
- Reviewers disagree with each other and you must reconcile their asks without breaking the paper
- A reviewer wants a theoretical reframing, deeper engagement, or a different conceptual lens
- You need to decide which asks to accept, which to negotiate, and which to (carefully) decline

## OS rebuttals are developmental, not adversarial

OS review is **developmental**: reviewers often co-build the theory across rounds, so the response letter is a collaboration, not a defense. The tone is respectful and substantive; the goal is to show that you took each reviewer's intellectual contribution seriously and that the paper is *stronger* for it. The editor reads the letter to judge whether you have engaged in good faith with the **theory-level** asks — those carry the decision.

## Structure the response

- **Open with a synthesis.** A short cover note to the editor summarizing the main changes and how you handled the central threads — especially where reviewers diverged.
- **Point-by-point, verbatim comments.** Quote each comment, then respond; never paraphrase away a reviewer's concern.
- **Show, don't assert.** For each accepted point, name the change and quote/locate the revised passage (page/section). "We have clarified the mechanism" is not enough; show the new text.
- **Group related comments** when several reviewers circle the same issue, so the editor sees one coherent fix rather than three partial ones.

## Triage the comments

| Comment type | Default stance | How to handle |
|--------------|---------------|---------------|
| Theory-level (mechanism, contribution, engagement) | **Accept and develop** | These are the decision; route to `orgstud-theory-development` / `orgstud-contribution-framing` and report the substantive change |
| Use of social theory ("engage Bourdieu/logics properly") | Accept | Deepen with the framework's real machinery (`orgstud-literature-positioning`) |
| Method/analysis transparency | Accept | Add the data structure, negative cases, robustness (`orgstud-data-analysis`, `orgstud-tables-figures`) |
| Reflexivity / positionality | Accept (substantive at OS) | Add a genuine reflexive account, not a token line |
| Reviewer disagreement | Reconcile | Take the editor's signal; explain your choice to both reviewers |
| A change that would break the contribution | Negotiate / decline | Decline respectfully *with theoretical reasoning*, and offer an alternative that meets the underlying concern |

## Handling the hard cases

- **Conflicting reviewers:** follow the editor's letter, then write a single integrated solution and explain to each reviewer why it serves their concern. Do not silently side with one.
- **An ask you cannot meet:** never ignore it. State the reason theoretically, show what you *did* do to address the underlying worry, and let the editor adjudicate.
- **A request to become a different paper:** if a reviewer wants a paper you did not write, hold the contribution and explain the scope — but only after confirming with `orgstud-review-process` that this is not the editor's essential thread.
- **Over-revision risk:** do not pile on changes that dilute the contribution to placate every comment; a sharper paper beats a longer one (mind the 13,000-word cap).

## Checklist

- [ ] A cover synthesis names the main changes and how divergent reviews were reconciled
- [ ] Every comment quoted verbatim and answered; none paraphrased away
- [ ] Each accepted point shows the revised text with a location
- [ ] Theory-level asks are developed substantively, not patched cosmetically
- [ ] Declined points are declined respectfully with theoretical reasoning + an alternative
- [ ] Reflexivity/positionality requests addressed genuinely
- [ ] Revisions keep the contribution sharp and the manuscript within the word cap

## Anti-patterns

- A defensive, point-scoring tone in a developmental culture
- "We have addressed this" with no shown text or location
- Paraphrasing a reviewer's concern into something easier to answer
- Silently siding with one reviewer when two conflict
- Ignoring a comment you cannot fully meet instead of reasoning about it
- Over-revising into a bloated paper that loses the theoretical move

## Output format

```text
【Outcome being answered】major / reject-resubmit / minor
【Cover synthesis】main changes + reconciliation of divergent reviews
【Comment triage】accepted-and-developed / accepted / negotiated / declined-with-reason
【Theory-level fixes】mechanism / contribution / social-theory engagement (with locations)
【Reflexivity added】genuine account? (Y/N)
【Resubmission state】contribution intact + within 13,000 words? (Y/N)
【Next step】finalize response letter + revised manuscript; re-run orgstud-submission before resubmitting
```
