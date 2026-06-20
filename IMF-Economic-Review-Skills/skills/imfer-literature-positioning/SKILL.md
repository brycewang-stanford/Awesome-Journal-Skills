---
name: imfer-literature-positioning
description: Use when the contribution of an IMF Economic Review (IMFER) manuscript relative to the international-macro frontier and the sibling journals is unclear or undersold. Stakes the claim against JIE/JIMF/JMCB and the IMF research stream; it does not select the topic (imfer-topic-selection) or design identification (imfer-identification).
---

# Literature Positioning (imfer-literature-positioning)

## When to trigger

- A referee or coauthor says "I am not sure what is new here relative to [JIE / JIMF paper]"
- The paper cites broadly but never states the **one-sentence delta** over the closest prior work
- You cannot tell whether the contribution is empirical (new fact), methodological, or policy-design
- The framing reads like a JIE or JIMF paper and you must pull it toward IMFER's policy-relevant frontier
- You need to place the paper in the **IMF research stream** (WEO/GFSR themes, ARC topics, prior IMFER issues) without name-dropping
- A reviewer suspects the result restates a known global-financial-cycle / sudden-stop finding under a new label

## How IMFER weighs a contribution

IMFER referees ask three things at once: *Is the finding new at the frontier? Is the identification credible? Does it change how a policymaker should think about an international-macro problem?* A paper that is new but policy-mute, or policy-relevant but already known, stalls. Position the contribution on the axis where it is strongest, and be explicit about the **closest two or three papers** — including the sibling-journal ones — so the referee never has to guess what you are adding.

| Contribution type | What "new" means at IMFER | The trap to avoid |
|-------------------|---------------------------|-------------------|
| New stylized fact / measurement | a cross-country regularity prior work missed (e.g., a new capital-flow or debt pattern) | "we have newer data" with no new economics |
| New identification of a known relationship | credibly causal where the literature was correlational | claiming causality the design cannot deliver |
| New mechanism / channel | distinguishing a transmission channel rivals cannot | a channel the data cannot separate |
| New policy-design implication | a usable rule/threshold for a CFM, intervention, or DSA | a "policy implication" paragraph bolted on at the end |
| New theory disciplined by data | an open-economy model that resolves a puzzle | a model that merely re-labels the finding |

## The sibling map (know exactly where you sit)

IMFER is confused with several journals; positioning means knowing the boundary and stating it.

| Sibling | Its center | The IMFER difference |
|---------|-----------|----------------------|
| Journal of International Economics (JIE) | trade + international finance, frontier method, less policy framing | IMFER foregrounds the *policy-relevant* implication and the institutional audience |
| J. of International Money & Finance (JIMF) | broad open-economy money/finance, faster, less selective | IMFER is more selective and more explicitly policy-flagship |
| J. of Money, Credit & Banking (JMCB) | monetary economics, often closed-economy | IMFER requires the *international/open-economy* margin |
| Economic Policy | European-leaning policy economics, panel-discussed | IMFER is the *IMF's* flagship with the ARC pipeline and a global-institution audience |
| AEJ: Macro | general macro, theory or quant, US-macro common | IMFER requires the international dimension and policy relevance |

## Positioning craft

1. **Write the delta sentence.** "Relative to [closest paper], we show [X] using [data/design], which implies [policy object]." If you cannot, the contribution is not yet sharp.
2. **Name the frontier honestly.** Cite the two or three closest papers — across IMFER, JIE, JIMF — and say exactly what each leaves open.
3. **Locate the policy frontier, not just the academic one.** Connect to the live IMF-relevant debate (capital-flow management, debt restructuring, the global financial cycle) the finding speaks to.
4. **Choose one primary axis.** A paper that claims to be new on four axes usually is new on none; lead with the strongest and let the others be secondary.
5. **Pre-empt the "this is JIE/JIMF" reflex** by foregrounding the policy-relevant delta that makes it IMFER.

## Checklist

- [ ] A single delta sentence states what is new relative to the closest prior paper
- [ ] The two or three closest papers (incl. sibling-journal) are named with what each leaves open
- [ ] The contribution is placed on one primary axis (fact / identification / mechanism / policy / theory)
- [ ] The policy-relevant frontier (IMF-relevant debate) is connected, not just the academic one
- [ ] The framing makes clear why this is IMFER and not JIE / JIMF / JMCB
- [ ] No overclaiming beyond what the design and data support
- [ ] Citations real and verifiable; no invented papers (see exemplars guardrail in resources)

## Anti-patterns

- A "literature review" that summarizes the field but never states the delta
- Claiming novelty on data alone ("we use newer/wider coverage") with no new economics
- A bolted-on final-paragraph "policy implications" that the analysis never earned
- Hiding the closest competing paper to make the gap look larger
- Positioning as a pure-trade or domestic-macro contribution, then submitting to IMFER
- Citing the entire international-finance canon while never engaging the one paper that did almost exactly this

## Worked vignette (illustrative)

A paper documents that EM sovereign spreads react more to US shocks after 2010. The weak positioning cites thirty global-financial-cycle papers and claims "we extend the literature." The IMFER positioning instead writes the delta: "Relative to [closest paper], which shows the global financial cycle moves EM spreads on average, we show the *sensitivity itself* rose with the post-GFC investor-base shift to bond funds, identified from EPFR flows — implying that a debt-management office should now hedge differently." One primary axis (a new conditioning fact), the closest paper named, the policy object explicit. The referee no longer has to reconstruct what is new.

## Referee pushback mapped to the positioning fix

- *"How is this different from [JIMF/JIE paper]?"* → State the delta sentence in the intro and a paragraph in the literature section naming exactly what that paper leaves open.
- *"This is just a new dataset on a known result."* → Lead with the new *economics* (a new conditioning variable, mechanism, or policy object), not the data.
- *"The policy implications feel tacked on."* → Connect the contribution to a live IMF-relevant debate from the start, so the implication is structural, not cosmetic.

## Output format

```text
【Journal】IMF Economic Review
【Skill】imfer-literature-positioning
【Delta sentence】relative to ___, we show ___ using ___, implying ___
【Primary axis】fact / identification / mechanism / policy-design / theory
【Closest papers】[paper → what it leaves open] ×2–3
【Policy frontier】the IMF-relevant debate this enters: ___
【Sibling guard】why IMFER not JIE/JIMF/JMCB: ___
【Verdict】pass / sharpen / reroute
【Next skill】imfer-identification
```
