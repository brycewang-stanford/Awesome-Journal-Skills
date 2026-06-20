---
name: aeja-topic-selection
description: Use when deciding whether an applied-micro project belongs at the American Economic Journal: Applied Economics (AEJ: Applied) rather than AER, AEJ: Economic Policy, or a field journal, and what its central question should be. Sets venue fit and question scope; it does not design the identification (see aeja-identification).
---

# Topic Selection & Venue Fit (aeja-topic-selection)

## When to trigger

- A project is empirically promising but you are unsure it is "AEJ: Applied-shaped"
- The question reads like a policy evaluation, a field-specialist note, or a top-general-interest swing — and you need to place it
- Several possible framings of the same dataset exist and you must pick the one that lands here
- Reviewers (or a co-author) say "this is fine but why this journal?"

## The AEJ: Applied fit test

AEJ: Applied wants **empirical applied microeconomics** where a **credible causal research design** answers a **substantive economic question** of **broad applied-micro interest** — above a pure field journal but more specialized than AER. Use this decision table to place the project.

| Signal in your project | Likely fit |
|------------------------|-----------|
| Clean identification + a question labor/dev/health/ed/public economists all care about | **AEJ: Applied** (core) |
| Same design but the contribution is mainly a policy verdict / program ROI framing | lean **AEJ: Economic Policy** |
| Genuinely general-interest, agenda-setting, methodologically ambitious, long | aim **AER** first |
| Contribution is field-internal (only sub-field specialists will cite it) | a **field journal** (JHE / JOLE / JDE) |
| New estimator with a toy application | **Econometrica / REStud / JoE**, not AEJ: Applied |

AEJ: Applied is **empirical-first**: theory appears to interpret and discipline the estimate, not to lead. A descriptive or measurement paper can fit *if* the question is sharp and the measurement is the contribution — but it must not overclaim causality.

## Sharpening the question (do this before writing anything)

1. **One-sentence question** with the causal object named: "What is the effect of X on Y for population P, identified by design D?"
2. **Why broad applied-micro readers care** — name two subfields beyond your own that should cite it.
3. **What the headline number will be** (a magnitude with units, even if approximate) — if you cannot imagine the sentence "we find X raises Y by ___," the question is not yet AEJ: Applied-shaped.
4. **The credible-design seed** — which design (RCT / DID / RD / IV / shift-share) makes the estimate believable; if none, the topic is not ready (route to `aeja-identification`).

## Checklist

- [ ] One-sentence causal (or sharply descriptive) question with a named estimand
- [ ] Venue placed against the table above; reason it is AEJ: Applied and not AER / AEJ: Policy / a field journal written in one line
- [ ] Two subfields beyond your own that will cite it, named
- [ ] An imaginable headline sentence with a magnitude and units
- [ ] A candidate research design that could make the estimate credible
- [ ] JEL codes drafted (required at submission) reflecting the cross-field appeal

## Anti-patterns

- A field-internal contribution dressed up as general — desk-reject risk for "fit"
- A pure policy-ROI framing that reads as AEJ: Economic Policy
- An ambitious agenda paper that is really an AER swing sent to AEJ: Applied as a hedge (or vice versa)
- "Interesting dataset, no question" — data-availability is not a contribution
- Implying causality from a design that cannot support it just to clear the bar

## Worked vignette (illustrative)

A researcher has linked administrative tax and education records for one country and wants to "study
inequality." That is a dataset, not a question. Working through the fit test: the cleanest variation in the
data is a school-finance reform that changed per-pupil spending at a sharp formula threshold — an RD. The
question becomes "what is the effect of marginal school spending on adult earnings, identified by the
funding-formula discontinuity?" Two subfields beyond education (labor and public) will cite it; the
imaginable headline is "a $1,000 increase in per-pupil spending raises adult earnings by ~___%." Now it is
AEJ: Applied-shaped — and clearly not an AER agenda paper or an AEJ: Policy program verdict.

## Sibling-placement quick test

- Would a non-specialist applied economist find the *question* interesting, not just the *finding*? → AEJ: Applied
- Is the deliverable a policy recommendation / cost-benefit verdict? → lean AEJ: Economic Policy
- Is the ambition field-defining and the design unusually novel? → try AER first
- Will only sub-field specialists ever cite it? → a field journal

## Output format

```
【Question】one sentence, estimand + population named
【Venue verdict】AEJ: Applied because [not AER: ___] [not AEJ: Policy: ___] [not field: ___]
【Cross-field appeal】subfields that will cite: [..., ...]
【Headline (anticipated)】"X raises/lowers Y by ~___ (units)"
【Design seed】RCT / DID / RD / IV / shift-share / descriptive
【JEL draft】[codes]
【Next step】aeja-literature-positioning
```
