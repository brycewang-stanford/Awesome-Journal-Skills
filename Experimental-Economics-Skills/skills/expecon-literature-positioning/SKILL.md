---
name: expecon-literature-positioning
description: Use when staking an Experimental Economics (ExpEcon) manuscript's contribution against prior experiments and the behavioral theory it tests. Sharpens positioning; it does not invent results or citations.
---

# Literature Positioning (expecon-literature-positioning)

## When to trigger

- A referee or coauthor says "we already know this" — the marginal contribution over existing experiments is unclear
- Your design is close to a canonical paradigm (dictator, ultimatum, public goods, trust, beauty contest, double auction) and you must show what is genuinely new
- The intro cites behavioral theory but never says which prediction your treatment *adjudicates*
- You are unsure whether your novelty is a new **treatment**, a new **method/elicitation**, a **replication**, or a **boundary condition**

## What counts as a contribution here

At a method-defined journal, positioning is not "no one has studied topic X." It is "**no prior design could deliver the comparison I deliver**." Locate your paper on this ladder, from weakest to strongest:

1. **Re-label** — same paradigm, new cover story. Usually insufficient on its own.
2. **New boundary condition** — a known effect tested where theory predicts it should vanish/flip; valuable when the prediction is sharp and pre-registered.
3. **Confound removal** — a cleaner control that isolates a mechanism prior designs conflated (e.g., separating altruism from confusion in public-goods contributions). Strong.
4. **New decisive treatment** — a contrast prior work *could not run* that adjudicates between competing behavioral models. Strongest.
5. **Methodology of experimentation** — evidence that a widely used procedure (strategy method, BDM, ELMS, double-blind payment, online vs. lab) biases results. A flagship-distinctive contribution.
6. **Replication** — direct or conceptual replication of a contested finding, ideally pre-registered and adequately powered. Explicitly in scope and valued.

## Positioning the design against its ancestors

- **Name the closest paradigm and the closest prior treatment** explicitly, then state the one dimension you change and the prediction that change adjudicates. Vague "builds on a large literature" framing reads as not knowing the field.
- **Map competing behavioral models to observable predictions.** Inequity aversion, reciprocity, social-image, and confusion often predict the *same* mean contribution; your positioning must show your contrast splits them.
- **Cite the methodological lineage, not just the topical one.** An ExpEcon referee wants to see that you know *why* the standard procedure exists and where it has been criticized.
- **Be honest about replication content.** If your treatment is partly a replication of a prior result, say so and frame it as a strength (a powered re-test), not hide it.

## Sibling boundary in the lit review

A reviewer should never finish the intro thinking "this is a JEBO behavioral paper" or "this is a GEB theory paper with a demo." Your literature should be **dominated by experimental-methods work** and read as a conversation about designs and procedures, not only about a phenomenon.

## Worked vignette (illustrative)

A trust-game paper claims to be "the first to study trust under time pressure." A quick search shows several such studies — so the positioning collapses to a re-label. The fix climbs the ladder: the real contribution is **confound removal** — prior time-pressure designs confounded cognitive load with the *deadline framing* itself, and the new design adds a load-only control that holds framing fixed. Now the intro names the two closest prior treatments, states the single new control, and shows the contrast splits a "depletion of self-control" account (predicts less trust) from a "framing" account (predicts no change). The reference list leans on elicitation-method papers, not the broad trust literature.

## Three sentences every ExpEcon intro needs

1. *The closest design.* "The closest prior experiment is [X], which [contrast]."
2. *The one new thing.* "We change exactly [one dimension], which prior designs could not isolate."
3. *What it adjudicates.* "This separates [model A] from [model B], which agree in [X] but diverge in [our treatment]."

If you cannot write these three sentences, the contribution is not yet positioned — return to `expecon-topic-selection`.

## Building the comparison from paradigm building blocks

ExpEcon literatures are organized around a handful of canonical paradigms; positioning is often clearest when you say which building block you take and what you bolt onto it. Make the lineage explicit:

| Paradigm | Studies | Your move is usually… |
|----------|---------|-----------------------|
| Public goods / VCM | cooperation, punishment | add a clean institution treatment (e.g., communication, sanction design) |
| Trust / gift exchange | reciprocity, fairness | isolate the channel (intentions vs. outcomes) prior work conflated |
| Dictator / ultimatum | social preferences | a boundary condition or a confound-removing control |
| Markets / auctions | price formation, efficiency | a new mechanism or information structure |
| Coordination / beauty contest | strategic reasoning | manipulate the depth-of-reasoning lever |

Naming the building block and the one new piece is itself strong positioning — it tells the referee exactly where your design sits in the family tree.

## Checklist

- [ ] The closest prior paradigm *and* the closest prior treatment are named
- [ ] The contribution is located on the ladder (boundary / confound removal / new treatment / methodology / replication)
- [ ] Competing behavioral models are mapped to distinct observable predictions your contrast separates
- [ ] The methodological lineage of the procedure used is cited, not just the topic
- [ ] Replication content (if any) is disclosed and framed as powered re-testing
- [ ] The reference list is method-heavy enough to read as an ExpEcon paper, not a JEBO/GEB paper

## Engaging the methodological critics

Strong ExpEcon positioning cites not only the studies that *used* a procedure but the ones that **criticized** it. If you elicit risk with Holt–Laury, acknowledge the known issues (multiple switching, framing of the safe option) and say how your implementation handles them. If you use the strategy method, cite the evidence on when it does and does not replicate direct-response behavior. This signals that you chose the procedure deliberately, not by inertia — exactly the methodological self-awareness the flagship rewards, and it pre-empts a referee who knows the critique.

## Anti-patterns

- "First to study X" claims that a five-minute search refutes
- Citing a "large literature" without naming the one paper your design is closest to
- Claiming novelty of topic when the design is a re-label of a canonical paradigm
- Hiding that the result is mostly a replication instead of selling the added power/pre-registration
- A reference list dominated by applied or theory work, signaling the wrong venue

## Positioning a replication or Registered Report

Replications are explicitly in scope, but a flagship replication must do more than re-run: it should be **adequately powered** (often more than the original), **pre-registered**, and framed as resolving a *contested* or *influential* finding — not an arbitrary re-test. State the original effect size, your MDE, and what a confirm-or-overturn outcome would mean for the literature. For a Registered Report, the positioning lives in the Stage-1 protocol: the contribution is the *question and design*, judged before results exist, so the introduction must make the case that the answer matters whichever way it comes out. A "we replicate X and find the same thing" framing with no power story or stakes reads as JESA-scale, not flagship.

## Output format

```text
【Journal】Experimental Economics (ESA method flagship)
【Skill】expecon-literature-positioning
【Verdict】pass / sharpen / reroute
【Closest paradigm + treatment】named prior design
【Contribution rung】boundary / confound-removal / new-treatment / methodology / replication
【Models adjudicated】which behavioral predictions the contrast separates
【Sibling boundary】why not JEBO / GEB / AEJ:Micro
【Next skill】expecon-theory-model
```
