---
name: jmcb-writing-style
description: Use when the prose — abstract, introduction, and the policy framing — is the bottleneck for a Journal of Money, Credit and Banking (JMCB) manuscript. Makes the monetary/banking idea and its policy payoff land for a specialist-but-policy audience; it is a late-stage polish, not a substitute for fixing the analysis.
---

# Writing Style (jmcb-writing-style)

## When to trigger

- The abstract states what you did but not what a central banker or regulator should conclude
- The introduction reaches the contribution only on page three
- The prose is technically correct but reads like a working paper, not a policy-relevant article
- Results are described ("the coefficient is significant") rather than interpreted (what it means for transmission/policy)
- The paper is at the 40-page cap and the writing is the place to recover space

## The JMCB voice

JMCB readers are **monetary/banking specialists who also think in policy terms**. The house voice is precise about mechanism and institutions, explicit about magnitudes, and never loses the **policy payoff**. The best JMCB papers tell the reader, early and plainly, what a central bank or regulator should believe differently — and then back it with disciplined evidence. Avoid both extremes: the dense methods-paper voice that hides the policy point, and the loose op-ed voice that overstates it. Magnitudes, not just signs and stars, carry the message.

## The introduction (the highest-leverage page)

Write the JMCB intro as a tight funnel — aim for roughly this arc in the first two pages:
1. **The policy/economic question**, framed so a money/credit/banking reader sees the stakes immediately.
2. **What we do** — the data and the identification, in two or three sentences, with the key institutional/timing fact.
3. **What we find** — the headline *with its magnitude* ("a 100bp tightening cuts low-capital-bank lending 1.8%"), not just "we find a significant effect."
4. **Why it is identified** — one sentence on the variation and the main threat you defuse.
5. **The contribution vs. the frontier** — the one-sentence delta (hand off to `jmcb-literature-positioning` if fuzzy).
6. **The policy takeaway** — what a policymaker should conclude.

## The abstract

- ≤ ~150 words is a safe target (待核实 — confirm the current limit on the official page); lead with the question and the headline magnitude, not the method.
- Name the mechanism and the policy implication. A JMCB abstract that omits the policy payoff undersells the paper.

## Prose discipline

- **Interpret, don't just report.** Every key number gets an economic reading in monetary/banking terms.
- **Foreground institutions and timing** — JMCB rewards papers that show they understand the plumbing.
- **Cut hedging and throat-clearing** — this also reclaims pages under the 40-page recommendation.
- **Use author-year citations** consistent with the journal's style; keep the reference list disciplined since it counts toward the page recommendation.

## Writing the results section for a policy reader

The results section is where JMCB papers most often slip into report-mode. Three habits keep it interpretive:

- **Lead each result with its economic meaning, then the number.** "Lending at low-capital banks contracts sharply — 1.8% per 100bp — while well-capitalized banks are unaffected," not "the interaction term is −0.018 (p<0.01)."
- **Benchmark every headline magnitude.** Situate it against the canonical estimate ("larger than the 1.1% in [prior], consistent with our tighter demand controls") so the reader can judge plausibility.
- **Translate to the policy unit.** Convert coefficients into the quantity a policymaker thinks in — basis points of pass-through, share of transmission attributable to the channel, a welfare or output number.

## Length as a writing discipline

The ~40-page recommendation (including references, tables, and figures) makes prose economy a real constraint, not a nicety. The cheapest pages to reclaim are: hedged throat-clearing ("It is worth noting that…"), restated results that the table already shows, over-long literature paragraphs that a contrast sentence could replace, and method exposition that belongs in the online appendix. Cutting these usually *improves* the paper — a tight monetary/banking argument reads as more confident — while protecting space for the exhibits and robustness that carry the result.

## Checklist

- [ ] Abstract leads with the question + headline magnitude and names the policy implication
- [ ] Introduction delivers question → method → finding-with-magnitude → identification → contribution → policy in ~2 pages
- [ ] Every key result is interpreted in monetary/banking/policy terms, not just reported
- [ ] Institutions and timing are visible; the paper shows it knows the plumbing
- [ ] Magnitudes carry the message; significance language never substitutes for economic size
- [ ] Author-year citations; reference list kept tight against the 40-page recommendation
- [ ] Hedging and redundancy cut to recover length

## Anti-patterns

- An abstract that says "we study the effect of monetary policy on lending" with no magnitude and no policy takeaway
- A buried lede — the contribution arriving on page three of the introduction
- Reporting significance ("p < 0.01") in place of interpreting the economic magnitude
- Op-ed overreach: drawing sweeping policy conclusions the local/identified estimate cannot support
- Methods-paper density that obscures, for a policy reader, why the result matters
- A bloated reference list and hedged prose pushing the paper over the recommended length

## The conclusion as a policy statement

JMCB conclusions are often wasted on a summary the abstract already gave. Use the conclusion to state, plainly, what a central banker or regulator should take away and what the result does *not* license. A strong JMCB close names the policy implication, the scope conditions (the regime, the sample, the local nature of the estimate), and the open question the paper leaves — turning the last page into the one a policy reader remembers.

## Worked vignette (illustrative)

A draft abstract reads: "Using bank-level data, we estimate the response of lending to monetary policy and find statistically significant effects." The JMCB rewrite: "A 100bp monetary tightening reduces lending by 1.8% at banks in the lowest capital quartile but leaves well-capitalized banks unchanged, implying that bank capital shapes the strength of monetary transmission — a margin policymakers can target through capital regulation." Same result; now the question, the magnitude, the mechanism, and the policy payoff are all on the page.

## Output format

```text
【Journal】Journal of Money, Credit and Banking
【Skill】jmcb-writing-style
【Abstract】leads with question + magnitude + policy implication? [Y/N]
【Intro funnel】question→method→finding(magnitude)→ID→contribution→policy in ~2pp? [Y/N]
【Interpretation】key numbers read in policy/banking terms, not just reported? [Y/N]
【Magnitude over stars】economic size carries the message? [Y/N]
【Length】hedging/refs trimmed toward the 40-page recommendation? [Y/N]
【Next skill】jmcb-submission
```
