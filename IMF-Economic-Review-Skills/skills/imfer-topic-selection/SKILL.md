---
name: imfer-topic-selection
description: Use when deciding whether a question is right for an IMF Economic Review (IMFER) manuscript — international macro-finance with genuine policy relevance and an IMF-program or global-institution audience. Tests fit and scope; it does not run the identification (imfer-identification) or stake the contribution (imfer-literature-positioning).
---

# Topic Selection (imfer-topic-selection)

## When to trigger

- You have a question but are unsure it clears IMFER's **international-macro-with-policy-relevance** bar
- The paper could plausibly go to JIE, JIMF, JMCB, AEJ: Macro, or *Economic Policy* and you must decide
- A reduced-form estimate is clean but you cannot name the **policy "so what"** the IMF audience needs
- You were invited to the Jacques Polak ARC / a special issue and must align the question to the issue theme
- A coauthor asks whether the topic is "too domestic" or "too narrowly technical" for IMFER

## What IMFER actually wants

IMFER is the IMF's flagship scholarly journal: it rewards **rigorous research on international macroeconomics and finance whose findings speak to policy** — exchange rates and capital flows, global imbalances, financial crises and contagion, sovereign debt and default, monetary and fiscal policy in open economies, IMF-program-relevant questions, and cross-border spillovers. The double audience is the test: a paper must satisfy a frontier referee on method *and* give someone who could brief an IMF mission a usable implication. A purely domestic US-macro question, or a methods paper with no open-economy or policy hook, is the classic mis-fit.

| Your question's center of gravity | IMFER fit | If it is borderline |
|-----------------------------------|-----------|---------------------|
| Capital flows / controls / capital-flow-management measures | Strong — core IMFER | Make the welfare/policy trade-off explicit |
| Sovereign debt, default, restructuring, debt sustainability | Strong — core IMFER | Tie to DSA / program-design relevance |
| Financial crises, contagion, global financial cycle | Strong — core IMFER | Name the cross-border transmission channel |
| Exchange-rate regimes, intervention, reserves | Strong — core IMFER | Avoid a single-country case with no general lesson |
| Open-economy monetary/fiscal policy, spillovers | Strong — core IMFER | Show it is open-economy, not closed-economy macro |
| Pure international trade (gravity, tariffs, firm exports) | Weak — usually JIE | Reframe around the macro-financial margin or redirect |
| Domestic monetary policy, US-only macro | Weak — JMCB / AEJ: Macro | Add the international spillover dimension or redirect |
| Econometric method paper, no policy object | Weak | Anchor on an IMF-relevant application or redirect |

### The IMF Staff Papers inheritance
IMFER is the named successor to *IMF Staff Papers*, and that lineage shapes taste: the journal has long rewarded work that is **technically serious yet legible to the policy community**, often empirical, often comparative across countries, and explicitly connected to the questions an international financial institution faces. A topic that would have fit *Staff Papers* — measuring a cross-country regularity, evaluating a policy regime, quantifying a spillover — usually fits IMFER. A topic whose only home is a pure-theory or pure-method audience usually does not. Use the inheritance as a sanity check: would this paper inform an IMF surveillance or program discussion while still passing frontier review?

## The fit test (run before writing the intro)

1. **State the question in one sentence** and name the **policy decision** it informs (a capital-control choice, a debt-restructuring design, an intervention rule, a program condition).
2. **Name the international margin.** If nothing crosses a border — flows, prices, spillovers, contagion — IMFER is probably the wrong journal.
3. **Identify the audience split.** Who is the academic referee, and who is the policy reader? If you cannot name a plausible IMF/central-bank reader, sharpen the policy hook.
4. **Check the country scope.** A single-country study needs a *general* lesson; a panel needs a sample whose composition you can defend (see `imfer-robustness`).
5. **Sibling guard.** Write one sentence on why this is IMFER and not JIE/JIMF/JMCB — and keep it honest.

### The ARC / special-issue lens
A large share of IMFER content flows through the **Jacques Polak Annual Research Conference** and its themed special issues (检索于 2026-06；以官网为准). If your paper is invited or you are targeting a call, topic selection is partly *alignment*: the question should sit squarely inside the issue theme (e.g., a year on "the global financial cycle," "debt in turbulent times," or "trade and financial fragmentation") while still standing as an independent contribution. Read the conference theme as a prior on what the editors find timely, but never bend a thin question to fit a theme — the policy "so what" still has to be real.

## Checklist

- [ ] The question names an international/open-economy margin (flows, prices, spillovers, contagion, debt)
- [ ] The policy "so what" for an IMF/central-bank reader is stated in one sentence, not implied
- [ ] The contribution is rigorous enough for a frontier referee, not only policy-relevant
- [ ] Country/sample scope supports a general lesson, not an idiosyncratic case
- [ ] The question would inform an IMF surveillance/program discussion (the *Staff Papers* inheritance test)
- [ ] A one-sentence sibling guard distinguishes IMFER from JIE / JIMF / JMCB / *Economic Policy*
- [ ] If ARC/special-issue invited, the question aligns to the issue theme without being bent to fit it
- [ ] No volatile process fact asserted without `resources/official-source-map.md` or 待核实

## Anti-patterns

- A clean estimate with **no policy implication** an IMF reader could use — reads as the wrong journal
- A **pure-trade** question dressed up as macro, or a **closed-economy** US-macro question with a token international footnote
- A single-country case study that yields no transferable lesson
- A **method-first** paper where the international-macro application is decorative
- Claiming the topic "is policy-relevant" without naming the actual decision it informs
- Chasing the headline crisis of the moment with no general, transferable mechanism
- Bending a thin question to fit an ARC theme just because a special issue is open
- Picking a question whose only audience is pure-theory or pure-method, not the policy community
- A panel whose sample is so dominated by one economy that no general lesson survives

## Worked vignette (illustrative)

A team has clean micro data on a single country's foreign-currency corporate borrowing. As a single-country finance paper it is JIMF or a field journal. The IMFER reframe asks the fit test: the *international margin* is currency mismatch and the *policy decision* is whether macroprudential FX limits reduce crisis risk; the *general lesson* is the mechanism (balance-sheet exposure to exchange-rate shocks), testable beyond the one country; the *policy reader* is a supervisor designing FX-borrowing limits. With the mechanism foregrounded and a second country added for external validity, the same data becomes an IMFER paper.

## Referee pushback mapped to the fit fix

- *"This is too domestic / single-country for IMFER."* → Foreground the transferable mechanism and the international margin; add a second country or a general model if the lesson is otherwise idiosyncratic.
- *"What is the policy takeaway?"* → Name the specific decision (a CFM threshold, an FX limit, a DSA assumption) the finding informs, in one sentence.
- *"Isn't this just JIE/JIMF?"* → State the policy-relevant delta that makes it IMFER, not the trade or pure-finance angle.

## Output format

```text
【Journal】IMF Economic Review
【Skill】imfer-topic-selection
【Question (1 sentence)】___
【International margin】flows / prices / spillovers / contagion / debt: ___
【Policy "so what"】the decision an IMF/central-bank reader gains: ___
【Audience split】academic referee: ___ | policy reader: ___
【Sibling guard】why IMFER not JIE/JIMF/JMCB: ___
【Verdict】fit / sharpen / redirect
【Next skill】imfer-literature-positioning
```
