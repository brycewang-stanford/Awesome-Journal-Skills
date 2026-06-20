---
name: jeem-writing-style
description: Use when the introduction, abstract, or prose of a Journal of Environmental Economics and Management (JEEM) manuscript misses the field voice — when the environmental mechanism → welfare → policy chain is buried or the contribution does not land in the first page. Polishes the framing late; it does not establish identification or results.
---

# Writing Style (jeem-writing-style)

## When to trigger

- The intro reviews the literature for two pages before the reader learns what the paper does
- The abstract states a result but not the **welfare or policy stake**
- The environmental mechanism is implied but never named as the engine of the contribution
- A general-interest editor would not see, by the end of page one, why this is an environmental-economics paper

## Discipline against advocacy

Environmental topics invite moral urgency, and a JEEM paper must resist it without becoming bloodless. The line: state the market failure and the welfare loss in economic terms, let the magnitude speak, and confine normative claims to bounded policy implications the evidence supports. Words like "crisis," "devastating," or "must act now" signal advocacy and undercut credibility with referees who want the economics to do the persuading. The most effective JEEM prose is quietly consequential — a precisely identified marginal damage of $X per ton is more compelling to this audience than any adjective, because it hands the policymaker a number rather than an exhortation.

## The JEEM voice

JEEM prose is **welfare-economics prose with an environmental subject**: precise, mechanism-first, and policy-aware without being advocacy. The reader is a field economist who wants to know, fast, (1) what environmental problem, (2) what credible economics, (3) what number, and (4) what it implies for policy or welfare. The writing's job is to make the **mechanism → welfare → policy** chain unmissable. Avoid both the dry "we estimate equation (1)" register and the breathless climate-advocacy register; JEEM wants disciplined economics that happens to matter for the planet.

## The first page (do these in order)

1. **Open on the environmental problem and its stakes** — the externality, the resource at risk, the policy in play — in one or two sentences a policymaker would recognize.
2. **State the question and the design in one sentence each** — "We use [variation] to identify [welfare object]." Name the design; do not make the reader guess.
3. **State the headline number with its welfare interpretation** — the marginal damage, the WTP, the pass-through, *and* what it means (the efficient tax, the value of the policy).
4. **Stake the contribution against the closest prior work** — one sentence on what was wrong or missing before.
5. **Preview the policy/welfare implication** — what a regulator should do differently, bounded honestly.

## Abstract and section craft

- **Abstract:** problem → variation/design → headline welfare number → implication, in that order; lead with substance, not method machinery. Keep within the journal's abstract limit (待核实 — re-check the guide for authors).
- **Mechanism sections** name the externality/resource structure before the regression; the empirical section should feel like it is testing a stated mechanism, not data-mining.
- **Numbers carry interpretation** — every headline estimate appears in welfare units (dollars, percent of damages, lives) at least once.
- **Policy paragraph, not policy sermon** — state the instrument implication and its caveats (second-best, leakage, distribution); do not advocate beyond the evidence.

## Vocabulary and register that signal the field

JEEM prose uses the field's terms precisely, which signals to the referee that you are inside the conversation. Say **marginal external cost / marginal damage** rather than "harm"; **willingness to pay / compensating variation** rather than "value"; **abatement cost / marginal abatement cost curve** rather than "cost of cleanup"; **capitalization** for amenity effects in prices; **leakage / reshuffling** for incomplete-coverage spillovers; **non-use / existence value** where relevant; **resource rent / user cost** in extraction settings. Misusing these (calling a total a marginal, or a partial-equilibrium estimate a welfare gain) is read as not knowing the field — get them exact.

## Common framing repairs

- A paper that opens on the *method* ("We apply a difference-in-differences estimator...") buries the environmental stakes — invert it so the externality leads.
- A paper that opens on a *climate slogan* ("In an era of unprecedented warming...") reads as advocacy — replace it with the specific market failure and its measurable cost.
- A results section that lists coefficients without ever translating to welfare leaves the contribution implicit — surface the dollar/welfare number in the text, not just the table.
- A conclusion that is the first place the policy implication appears has waited too long — preview it in the intro and pay it off at the end.

## Carrying the mechanism through the paper

The environmental mechanism should not appear only in the intro and conclusion — it should thread the whole paper. The data section motivates measurement choices by the externality or resource it captures; the empirical section frames each specification as testing the stated mechanism; the results translate to welfare; the conclusion returns to the policy stake. When a referee can trace the same mechanism from the first page to the last, the paper reads as genuinely environmental economics rather than an applied-micro exercise with a green label. Where the mechanism disappears for several pages of generic regressions, the framing has come loose and should be re-stitched.

## Checklist

- [ ] By the end of page one: environmental problem, design, headline number, and contribution are all stated
- [ ] The abstract names the welfare/policy stake, not just a coefficient
- [ ] The environmental mechanism is named as the engine, not implied
- [ ] The headline estimate appears in welfare units (not only a regression coefficient)
- [ ] The contribution is staked against named prior work in one sentence
- [ ] The policy implication is bounded (second-best / leakage / distribution), not advocacy
- [ ] Abstract length and formatting conform to the current guide for authors (待核实)

## Anti-patterns

- A two-page literature march before the reader learns what the paper does
- An abstract that reports significance but never the welfare/policy stake
- Climate-advocacy register ("urgent crisis") substituting for disciplined welfare argument
- A headline result stated only as a coefficient, never translated to dollars/welfare
- The environmental angle surfacing only in the conclusion
- Burying the design name so the reader cannot tell DiD from RD from hedonic on page one

## Worked vignette (illustrative)

A weak opening: "Air pollution is an important issue. We use panel data and fixed effects to study its effects." A JEEM opening: "Particulate pollution imposes mortality costs that fall outside the price system. Exploiting the staggered rollout of [regulation], we identify a marginal mortality damage of $X per ton — implying the efficient emissions tax is roughly $Y, well above the current standard." The second version states problem, design, welfare number, and policy stake in three sentences.

## Title and abstract as the first filter

The title and abstract are what the editor reads at the scope screen and what most referees see first, so they must carry the environmental contribution. A strong JEEM title names the environmental object and the contribution ("The Capitalization of Air-Quality Regulation in Housing Markets"), not just the method ("A Difference-in-Differences Study"). The abstract's first sentence should establish the market failure or resource problem; its last should state the welfare or policy implication with the headline number. If a reader who knows nothing of the paper cannot tell from the abstract alone that it is environmental economics with a welfare-relevant result, rewrite it before anything else — that abstract is where desk rejects are decided.

## Output format

```text
【Journal】Journal of Environmental Economics and Management
【Skill】jeem-writing-style
【Page-one test】problem + design + number + contribution all present? [Y/N]
【Abstract】welfare/policy stake stated, not just a coefficient? [Y/N]
【Mechanism】environmental engine named before the regression? [Y/N]
【Welfare units】headline estimate translated to $/welfare? [Y/N]
【Policy tone】bounded implication, not advocacy? [Y/N]
【Source status】verified URL / 待核实 / not asserted
【Next skill】jeem-replication-package
```
