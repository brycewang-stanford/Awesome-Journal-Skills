---
name: jmis-topic-selection
description: Use when deciding whether a question is the right shape for a Journal of Management Information Systems (JMIS) manuscript — an IS-management or economics-of-IS problem, not a generic tech study or a pure CS contribution. Pressure-tests fit and outlet choice before theory work begins; it does not build the mechanism (jmis-theory-development).
---

# Topic Selection (jmis-topic-selection)

## When to trigger

- You have an IS/technology phenomenon but cannot say what *managerial or economic* question it answers
- The work might be a better fit for MISQ, ISR, JAIS, Management Science, or a CS venue and you need to decide before investing in theory
- A reviewer or colleague says "this is a technical exercise" or "where is the management contribution?"
- The dataset (platform logs, firm IT spend, e-commerce transactions, security incidents) is rich but the question is not yet sharp

## What makes a question JMIS-shaped

JMIS rewards questions at the **technology–organization–economics nexus**: how information systems and technology are *managed*, *valued*, and *governed*, and how they reshape firms, markets, and platforms. The strongest JMIS topics make the **technology load-bearing in an economic or managerial mechanism** — not a backdrop. Use these tests:

1. **The IS-management hinge.** Does the answer change how a manager, firm, platform, or policymaker should act on technology? "We predict churn with a new model" is CS; "we show how a recommender's design shifts platform-side seller competition and revenue" is JMIS.
2. **The economics-of-IS angle.** JMIS (Zwass's IJEC lineage) is unusually receptive to IT economics, e-commerce, digital platforms, network effects, IT business value, and the economics of security/privacy. If your question has incentives, information, matching, or value at its core, it fits.
3. **Generalizable beyond one system.** The insight should travel past the specific artifact or firm to a class of IS phenomena.

## Decision table: route by what the question is really about

| Your question is really about… | Strong JMIS fit if… | Reroute / risk |
|--------------------------------|---------------------|----------------|
| IT investment and firm performance | identification of IT's *causal* value, not just correlation with spend | pure finance → a finance journal |
| a digital platform / marketplace | network effects, two-sidedness, governance, or pricing are theorized | descriptive platform stats → weak fit |
| IS adoption / use / behavior | a technology-specific behavioral mechanism, validated | generic TAM replication → desk-reject risk |
| a built artifact / ML system | managerial *utility* evaluated vs. real baselines, design knowledge generalized | algorithm-only novelty → a CS venue |
| security / privacy | the *economics or management* of risk, disclosure, breaches | a crypto/protocol result → a security venue |
| a policy / governance change | the IT-mediated effect on firms or markets is the point | a pure econ result with IS as setting → econ journal |

## JMIS vs. its neighbors at the topic stage

- **vs. MISQ** — MISQ leans into design-science and theory-method pluralism; JMIS leans into management/economics of IS. If the contribution is a *design theory*, MISQ may fit better.
- **vs. ISR** — ISR prizes *sociotechnical, intradisciplinary, silo-bridging* work and analytical models as co-equal. If your edge is bridging behavioral and economic paradigms, weigh ISR.
- **vs. Management Science (IS dept.)** — broader OR/management generality; JMIS wants the IS audience and an IS-specific takeaway.
- **vs. a CS / data-mining venue** — if removing the management/economics framing loses nothing, the paper is not JMIS-shaped.

## Worked vignette: from a dataset to a JMIS question (illustrative)

A team has clickstream and seller data from a marketplace and a draft titled "Predicting which sellers churn." As written it is a churn-prediction paper — a CS/data-mining contribution. The JMIS-shaped version asks an *economic-of-platforms* question: *does the platform's algorithmic ranking redesign cause marginal sellers to exit, and does that shrink buyer-side variety and platform revenue?* Now the technology (the ranking algorithm) is load-bearing, there is an identifying event (the redesign), and the takeaway is managerial (how aggressively to personalize ranking trades off short-run match quality against long-run seller supply). Same data, JMIS-grade question.

## Pre-commit the fit decision before theory work

Topic selection is also an outlet decision, and it is cheaper to make now than after a desk return. Write the single sentence, then ask three coauthor-style questions: *Who on the JMIS board would champion this? Which reviewer would say "wrong journal"? If a reviewer says "this is really a MISQ/ISR/econ paper," can I answer in one sentence?* If you cannot, the fit is borderline and you should resolve it — by sharpening the management/economics angle or by rerouting — before investing in `jmis-theory-development`.

## Checklist

- [ ] The one-sentence question names the technology *and* the managerial/economic stake
- [ ] Removing the IT artifact would break the contribution (technology is load-bearing)
- [ ] The economics-of-IS or IT-value angle is explicit where the phenomenon supports it
- [ ] You can name the JMIS audience segment that cares and the one that would desk-reject
- [ ] Fit vs. MISQ/ISR/JAIS/Management Science is argued, not assumed
- [ ] The insight generalizes beyond the single system, firm, or dataset
- [ ] The question passes the deletion, audience, and decision tests
- [ ] The phenomenon maps onto a JMIS-rewarded area (IT value, platforms, e-commerce, security/privacy economics, analytics)

## Topics JMIS has historically rewarded

JMIS's identity — shaped by Vladimir Zwass's long editorship and his parallel work on electronic commerce — leans toward the *management and economics* of IS. Questions that sit squarely in its wheelhouse: the business value and complementarities of IT and emerging tech (now including AI/analytics); the design, governance, and competition of **digital platforms and marketplaces**; **e-commerce** and digital channels; the economics of **information security and privacy**; decision support and business analytics in real managerial settings; and the organizational and market impacts of new technology. A topic that maps cleanly onto one of these — with the technology load-bearing — starts with the wind at its back; one that only borrows an IS setting to make a reference-discipline point starts behind.

## Anti-patterns

- A technically strong model with no managerial or economic question — reads as a CS paper in IS clothing
- A generic technology-adoption replication with no IS-specific mechanism
- Treating the IT artifact as an interchangeable "treatment" or setting
- Picking JMIS only because it is T&F and easy to email, when MISQ/ISR is the natural home
- Inventing an exemplar JMIS paper to justify fit instead of verifying it in the archive
- Choosing the topic for data availability alone, with no managerial or economic question attached
- A purely descriptive "we characterize X" framing with no decision it would change

## Stress-test the scope before you commit

Three quick tests separate a JMIS topic from a near-miss. **The deletion test:** remove the IT artifact from the question — if it still makes sense, the technology was a setting, not the subject, and the paper is probably not IS. **The audience test:** picture the JMIS readership (IS scholars who study the management and economics of technology) — can you name the subset who would cite this and the subset who would shrug? If you cannot name either, the topic is too diffuse. **The decision test:** does answering the question change a real technology decision (invest, govern, price, design, disclose)? JMIS's management identity rewards a question whose answer a manager or platform could act on; a purely descriptive "we characterize X" topic, however novel, sits closer to the journal's margin.

## Hand off only when fit is settled

Do not route to `jmis-theory-development` while the fit verdict is still "borderline." A topic that is unsure of its home wastes theory and analysis effort, because a reframe at the contribution stage often forces the mechanism to be rebuilt. Resolve the fit first — sharpen the management/economics angle until the deletion, audience, and decision tests all pass, or reroute honestly to the sibling that fits — and only then commit downstream work.

## Output format

```text
【Journal】Journal of Management Information Systems (JMIS)
【One-sentence question】technology + managerial/economic stake
【IS-management hinge】who acts differently and how
【Economics-of-IS angle】incentives / value / platform / security economics (or n/a)
【Fit verdict】strong / borderline / reroute → which sibling
【Next skill】jmis-theory-development
```
