---
name: finman-writing-style
description: Use when the prose, abstract, or introduction of a Financial Management (FM) manuscript buries the idea or its managerial/market payoff — FM's brand is "articles people actually read." Shapes exposition for a general finance audience; it does not establish results (finman-identification) or run the submission preflight (finman-submission).
---

# Writing Style (finman-writing-style)

## When to trigger

- The abstract and intro state what was done but not why a finance reader (or a practitioner) should care
- The paper reads like a technical report — correct, dense, and unread
- The contribution is buried under literature review or methodology before the finding appears
- You are doing the final exposition pass before submission (do this *after* the evidence settles)

## The FM writing bar

FM is unusually explicit that it wants **"a finance journal that publishes academic articles that people actually read."** That is a writing standard, not a slogan. The exposition is judged on whether a **general finance audience** — not just the immediate subfield — grasps the question, the answer, and the **practical relevance** quickly, and whether the paper **provokes and furthers debate.** Concretely: the abstract and first page must deliver the finding and its managerial/market implication before any apparatus; jargon that only insiders parse is a cost; and the "so-what for managers, investors, or regulators" must be stated, not left for the reader to infer. This is the lane that separates FM from siblings whose house voice tolerates a denser, more specialist register.

## The exposition build (in order)

1. **Abstract: finding-first.** Lead with the result and its implication in the first two sentences; method and data come after. A reader should know the "so-what" without reading the paper. (Exact abstract word limit 待核实 — check the Wiley author guidelines.)
2. **First page: the hook and the payoff.** State the live financial question, the answer, and who should change a decision because of it — within the first page, before the literature.
3. **Contribution paragraph.** One paragraph naming the specific delta (from `finman-literature-positioning`) and the general-interest implication; resist the temptation to bury it on page 4.
4. **Mechanism and magnitude in plain finance language.** Explain the channel and the economic magnitude in terms a CFO, investor, or regulator would use, not only in regression-speak.
5. **Practical-relevance close.** End sections (and the paper) by connecting the estimate to a decision; FM rewards a paper that tells the reader what to *do* with the finding.
6. **Cut for readability.** Remove throat-clearing, redundant caveats, and apparatus that does not change a conclusion — every sentence should earn its place.

## The first-page test (FM's hardest sentence-level bar)

FM editors and referees decide interest fast. Treat the first page as the audition and engineer four sentences deliberately:

1. **The hook sentence** — the live financial tension or puzzle a general reader recognizes ("Boards routinely set covenants without knowing how creditors will use control rights").
2. **The finding sentence** — the answer, with the direction and a magnitude in plain terms ("We show creditors cut investment by ~7% after a breach").
3. **The why-it-matters sentence** — the decision that changes ("Boards can price this into covenant design ex ante").
4. **The how-we-know sentence** — the design in one line ("using a staggered covenant-rule change as quasi-exogenous variation").
A first page that delivers these four before the literature review passes FM's interest screen; one that opens with data counts and estimators fails it.

## Checklist

- [ ] Abstract leads with the finding and its implication, not the method
- [ ] The first-page four sentences (hook / finding / why-it-matters / how-we-know) are present
- [ ] The question, answer, and decision-maker appear on the first page, before the literature
- [ ] The contribution and its general-interest payoff are stated in one clear paragraph
- [ ] The mechanism and economic magnitude are explained in plain finance terms
- [ ] At least one explicit "so-what for managers / investors / regulators" statement
- [ ] Jargon minimized; a non-specialist finance reader can follow the argument
- [ ] Prose trimmed of throat-clearing and apparatus that changes no conclusion

## Writing the implications so they survive a skeptical read

The "so-what" is where FM papers most often slide into either vagueness or overreach. Calibrate:

- **Be specific, not gestural.** "Has implications for policy" persuades no one; "regulators weighing covenant disclosure rules should expect investment to fall ~7% post-breach" does.
- **Stay inside the evidence.** Tie each implication to a result you actually identified; a managerial recommendation that outruns the design invites a "you didn't show this" report.
- **Address the decision-maker by name.** CFO, board, lender, investor, regulator — naming who acts makes the relevance concrete and FM-typical.
- **Distinguish positive from normative.** Separate "this is what happens" from "this is what they should do," and flag the assumptions the normative step requires.
A skeptical referee should finish the implications paragraph thinking "supported and useful," not "nice story, unproven."
- **Lead the title with the finding, not the method.** An FM-typical title names the financial phenomenon and its twist, not the estimator; it is the first interest signal the editor sees.

## Anti-patterns

- A method-first abstract that withholds the finding until the last sentence
- A first page dominated by literature review with the contribution deferred to page 4
- Stating significance but never the managerial/market implication — fails FM's relevance brand
- Subfield jargon that locks out the general finance audience FM is written for
- Hedging every sentence into unreadability "to be careful"
- Polishing prose before identification and the evidence hierarchy have settled

## Worked vignette (illustrative)

A draft's abstract opens "Using a panel of 4,312 firm-years and a two-way fixed-effects specification, we estimate…" and the finding arrives in sentence five. A referee says it is "well-executed but a slog." The FM rewrite: open with "Firms cut investment by 7% when creditors gain control after a covenant breach — a response boards can anticipate and price into covenant design," then give the design in one sentence and the magnitude in plain terms. Move the contribution paragraph to page one, and close the introduction with the implication for how CFOs should negotiate covenants. The paper now reads — and a general finance audience reaches the "so-what" in the first two sentences.

## Referee pushback mapped to the writing fix

- *"Well-executed but I lost interest by page three."* → Rebuild the first page around the four-sentence test; move the contribution and so-what forward.
- *"I can't tell why this matters in practice."* → Add an explicit managerial/market implication and translate the coefficient into a decision-relevant unit (basis points, dollars, % of the mean).
- *"This reads like a specialist paper."* → Strip subfield jargon, define the mechanism in general finance terms, and frame the takeaway for the broad FM audience.
- *"The abstract buries the result."* → Reorder so the finding and implication are the first two sentences; demote method and sample to the end.

## Output format

```
【Abstract】finding-first, implication stated up front? [Y/N]
【First page】question + answer + decision-maker before the literature? [Y/N]
【Contribution paragraph】delta + general-interest payoff, one paragraph? [Y/N]
【Magnitude in plain terms】economic significance legible to a practitioner? [Y/N]
【So-what】explicit managerial/market implication present? [Y/N]
【Limits checked】abstract word limit verified or 待核实
【Next skill】finman-referee-strategy
```
