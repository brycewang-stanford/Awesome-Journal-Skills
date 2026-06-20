---
name: imfer-writing-style
description: Use when an IMF Economic Review (IMFER) manuscript's prose must land for its dual academic/policy audience — a tight intro, an italicized abstract with JEL codes, Chicago style, and a clear policy "so what." Sharpens the writing; it does not build the exhibits (imfer-tables-figures) or run the submission preflight (imfer-submission).
---

# Writing Style (imfer-writing-style)

## When to trigger

- The introduction buries the result and the policy implication under a long literature tour
- The abstract reads like a methods note and a policy reader cannot extract the takeaway
- The paper is rigorous but a mission economist could not tell what to *do* with it
- You are unsure of IMFER house conventions (italicized abstract, JEL codes, Chicago style, American spelling)
- The prose drifts toward JIE-style technical density with no policy register
- Country names, acronyms, and currency conventions are used inconsistently across the paper

## Writing for IMFER's two readers

Every IMFER paper is read by a frontier referee *and* a policy reader. The prose must satisfy both without talking down to either: the **academic claim** must be precise and the **policy "so what"** must be explicit and early. The house conventions reinforce a clean, readable register — the abstract is **italicized** and followed by **JEL codes**, style follows the **Chicago Manual of Style** with **American spelling**, and author biographies (≤80 words each) and contact details go in a **separate file** for double-blind review (检索于 2026-06；以官网为准). Write so the result and its implication survive a skim.

### The introduction (IMFER recipe)
1. **Hook with the policy-relevant puzzle** — the international-macro tension a policymaker recognizes.
2. **State the question and the answer** in the first page; do not make the reader wait for Section 5.
3. **Name the data and the identification** in one or two sentences — credibility up front.
4. **State the contribution as a delta** over the closest work (incl. sibling journals).
5. **Deliver the policy "so what"** — what the finding implies for a CFM, a debt strategy, an intervention rule.
6. **Roadmap** briefly. Keep the literature *placed*, not surveyed.

### The abstract
Italicized, compact, and self-contained: question, data/design, headline magnitude (in policy units), and the policy implication. Follow with JEL codes. A policy reader should get the takeaway from the abstract alone.

### Register
- Active, concrete, quantitative — "a US tightening cuts EM inflows by 0.8% of GDP," not "has a significant effect."
- Translate every key result into a magnitude a policymaker would quote.
- Avoid hedging that erases the implication; state scope and uncertainty instead.
- Define acronyms once; an international-macro reader knows CFM and DSA, but spell out the first use.
- Use consistent country naming and grouping (advanced economies / emerging markets / low-income countries) and one currency convention throughout — sloppiness here signals careless data work to the referee.

### Writing the policy "so what" without overreaching
The hardest sentence in an IMFER paper is the policy implication: too timid and the policy referee sees no contribution, too bold and the academic referee sees overreach. The discipline is to state the implication **at the magnitude and in the regime the evidence supports**, with the conditionality explicit. "Our estimates imply a capital-flow measure of about 2% would offset roughly half of the inflow surge, for economies with the FX exposure of our sample" is defensible; "capital controls are optimal" is not. Write the implication as a *quantified, scoped* statement a mission economist could act on and a referee could not call inflated.

## Checklist

- [ ] Intro states question and answer on the first page; result not buried
- [ ] Data and identification named early; credibility established before the literature tour
- [ ] Contribution stated as a delta over the closest work
- [ ] Policy "so what" explicit in the intro and the abstract, not bolted on at the end
- [ ] Abstract italicized, compact, with a policy-unit magnitude; JEL codes present
- [ ] Chicago style, American spelling; acronyms (CFM, DSA, GFC) defined on first use
- [ ] Author bios (≤80 words) and contact details in a separate file (double-blind)
- [ ] Headline results stated as magnitudes, not "significant effects"

### The one-paragraph contribution test
After the intro is drafted, extract the single paragraph that states what the paper does and what it finds, and read it cold. A policy reader should learn the question, the answer in policy units, and the implication; an academic reader should learn the data, the identification, and the delta over prior work. If that paragraph cannot carry both readers on its own, the intro is not yet doing its job — and at IMFER, that paragraph is what the editor reads first when deciding whether to desk-reject.

## Anti-patterns

- An introduction that surveys the literature for two pages before stating the result
- An abstract that names methods but never the policy takeaway
- "Has a statistically significant effect" with no magnitude in policy units
- Hedging that buries the implication a policymaker needs
- British spelling / non-Chicago citations against house style
- Author-identifying traces in the main file (breaks double-blind)
- Jargon density that loses the policy reader, or oversimplification that loses the referee
- Inconsistent country naming/grouping or mixed currency conventions across sections
- A contribution paragraph that carries only one of the two readers

## Worked vignette (illustrative)

A first-draft intro opens: "The international transmission of monetary policy has been extensively studied (citations across two pages)..." The IMFER rewrite opens with the puzzle a policymaker feels — "When the Fed tightens, capital drains from emerging markets, but by how much, and can a capital-flow measure cushion it?" — then states the answer (a 0.8%-of-GDP outflow per 100bp, halved where macroprudential limits bind), names the high-frequency identification in one sentence, states the delta over the closest paper, and closes the first page with the implication for CFM design. The abstract mirrors this in italics, ends with JEL codes, and a policy reader gets the whole story without turning the page.

## Referee pushback mapped to the writing fix

- *"I had to read to Section 5 to find the result."* → Move the question and answer to the first page; demote the literature tour.
- *"What is the policy takeaway?"* → Put the policy "so what" in the intro and the abstract, in policy units.
- *"The abstract is all methods."* → Rewrite it as question → design → magnitude → implication, italicized, with JEL codes.

## Output format

```text
【Journal】IMF Economic Review
【Skill】imfer-writing-style
【Intro】question + answer on page 1? [Y/N]
【Identification up front】data + design named early? [Y/N]
【Policy "so what"】stated in intro + abstract? [Y/N]
【Abstract】italicized + magnitude + JEL codes? [Y/N]
【House style】Chicago + American spelling; acronyms defined? [Y/N]
【Double-blind】bios/contacts in separate file; main file anonymized? [Y/N]
【Next skill】imfer-replication-package
```
