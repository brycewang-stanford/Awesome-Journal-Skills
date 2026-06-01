---
name: rje-rebuttal
description: Use when responding to a revise-and-resubmit from The RAND Journal of Economics (RJE) — answering the two anonymous referees and the handling Editor on an industrial-organization manuscript while respecting the hard page caps and RJE house style. Strategy for the response letter; it does not rewrite the article.
---

# R&R Rebuttal Strategy (rje-rebuttal)

## When to trigger

- You received an R&R from the RJE handling Editor with two referee reports
- You must reconcile conflicting referee demands without blowing the 50-page cap
- You are drafting the point-by-point response letter

## RJE-specific rebuttal posture

RJE decisions come from a **handling Editor** synthesizing **two anonymous referees** after an upfront screen, so the Editor's letter is the binding document — prioritize the points the Editor flags, then address each referee. Two structural constraints shape the response:

- **Page caps are hard.** Main text **<=40 pp**, total **<=50 pp**, double-spaced. You usually cannot satisfy every referee by adding material. Move new robustness, derivations, and counterfactuals into the **appendix** (counts toward the <=10-page appendix+references budget) or, sparingly, into **supporting information** — but note RJE **discourages supporting information** and may decline it, so do not park core results there.
- **House style persists in the revision.** Keep author-date cites with **no page numbers**, references with **no issue numbers**, unnumbered subsections, and the usage rules (because/as not *since*; whereas/although not *while*; **"article"** not *"paper"*). A revision that drifts off style reads as careless.

## IO-specific responses referees expect

- **Identification / specification.** For structural work: justify functional form, instruments for price (cost shifters, BLP/Gandhi–Houde), and the estimator; show the result survives a reasonable alternative specification. For reduced-form: defend the policy/merger variation and report modern-DID or weak-IV-robust diagnostics.
- **Counterfactual and welfare claims.** IO referees probe out-of-sample counterfactuals hard — bound them and state the maintained assumptions.
- **Market definition and external validity.** Say what the estimated market teaches beyond itself.

## Response-letter mechanics

- One numbered point per referee comment; quote the comment, then the change, then a page/section pointer.
- Lead each reply with the **action taken**, not justification.
- Where you decline, give a crisp reason and an alternative check — never silence.
- Keep a **changes summary** at the top for the Editor, organized around the Editor's priorities.

## Anti-patterns

- Expanding the main text past 40 pp to appease referees instead of using the appendix
- Dumping core results into discouraged supporting information
- Letting the revision drift off RJE house style
- Treating both referees as equal when the Editor signaled which points are decisive

## Output format

```
【Editor's priorities】[ranked list from the decision letter]
【Referee 1 / Referee 2】[major asks each]
【Page budget】main __/40, total __/50 — within cap? [Y/N]
【Where new material goes】main / appendix / (supporting info, justified)
【Style preserved】author-date no page nos., house usage? [Y/N]
【Next step】rje-submission re-preflight before resubmission
```
