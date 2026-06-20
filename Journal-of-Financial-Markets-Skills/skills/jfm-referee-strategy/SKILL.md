---
name: jfm-referee-strategy
description: Use when anticipating the microstructure referee's objections for a Journal of Financial Markets (JFM) manuscript — a pre-submission pre-mortem and, post-decision, a triage of the report. Anticipates and triages; it does not invent evidence or citations.
---

# Referee Strategy (jfm-referee-strategy)

## When to trigger

- Pre-submission: you want to surface the objections a microstructure insider will raise before they do
- A report arrived and you need to triage which comments are fatal, fixable, or push-back
- You suspect the referee will challenge measurement or endogeneity rather than the idea
- You need to estimate whether the asks are within an R&R's reach or signal a reject
- The editor's letter prioritizes some comments and you must read the signal

## The objections JFM referees actually raise

A JFM referee is a microstructure specialist. The predictable lines of attack cluster, and most live in measurement and identification, not novelty.

| Referee line | What they really doubt | Pre-empt with |
|--------------|------------------------|---------------|
| "This is not really microstructure" | the mechanism is broad finance | `jfm-topic-selection` framing; lead with the trading-process object |
| "The result is driven by the liquidity measure" | measurement artifact | `jfm-empirical-design` + alternative constructs in `jfm-robustness` |
| "Liquidity is endogenous here" | reverse causality / confounding | `jfm-identification`: a market-structure shock or defensible IV |
| "Your event window / filters are arbitrary" | researcher-degrees-of-freedom | justify window from mechanics; document every filter |
| "Standard errors overstate precision" | un-clustered panel inference | two-way clustering / NW; state it in table notes |
| "Incremental to [known paper]" | contribution undersold | `jfm-literature-positioning`: explicit they/we gap |
| "PIN/structural estimates are fragile" | numerical instability | report solver settings, multistart, sensitivity |

## Running the pre-mortem and the triage

**Pre-submission pre-mortem.** For each row above that could apply, write the strongest version of the objection and the exhibit/argument that answers it. If an answer requires analysis you have not run, run it now — it is cheaper than an R&R cycle. The output is a list of latent weaknesses, each with a planned defense.

**Post-decision triage.** Sort every comment into: (1) **fatal-if-true** — goes to the top of the response and gets the most work; (2) **fixable** — new analysis or exposition; (3) **defensible** — politely push back with evidence; (4) **editor-flagged** — the editor signaled priority, so it is effectively (1). Read the editor's letter for the real decision rule: which comments must be resolved for acceptance. Then hand the sorted list to `jfm-rebuttal`.

## Timing the pre-mortem

Run the pre-mortem twice. The first pass is **before submission**, while there is still time to run the analysis that closes a foreseeable objection — this is its highest value, since adding an alternative-measure column now costs days, whereas discovering the gap in an R&R costs months. The second pass is **on receiving the report**, to triage the actual comments against your anticipated list: comments you predicted are already half-answered, and genuinely new ones tell you where your model of the field was incomplete. Skipping the pre-submission pass is the most expensive economy in the whole process.

## Worked pre-mortem (illustrative)

A paper claims a new dark-pool venue worsened lit-market liquidity. The pre-mortem surfaces: (1) *"It's just the measure"* — the result holds only for quoted spread → run effective and realized before submitting; (2) *"Endogenous venue choice"* — flow self-selects into the dark pool → exploit the staggered venue launch and cluster by stock; (3) *"Time-of-day"* — dark trading concentrates midday → add intraday-bin fixed effects; (4) *"Incremental to known fragmentation work"* — name the closest 3 papers and the gap. Each is answered with a concrete exhibit before the editor ever sees the paper. The output is a short table of latent weakness → planned defense → exhibit number, which doubles as the skeleton of the eventual response letter.

## Reading the decision letter

The editor's letter, not the referee reports, encodes the real decision rule. Look for: which comments the editor calls "essential" or "must address"; whether the tone is "revise" (fixable) or "we would consider a substantially revised paper" (closer to reject); and whether referees conflict (your cue to ask the editor to adjudicate rather than guess). An R&R that asks only for measurement and inference checks is far more tractable than one questioning the core identification — calibrate the effort and the timeline accordingly, and be honest with coauthors about which it is.

## The two reviewer profiles to plan for

JFM submissions typically draw a microstructure specialist and, sometimes, a broader-finance reader. Plan for both. The **specialist** scrutinizes measurement, institutional accuracy, and the mechanism — answer them with construction detail, alternative measures, and a heterogeneity test. The **generalist** asks why the result matters beyond the plumbing — answer them with a clear economic-magnitude statement and a sentence on the broader implication for market quality. A paper written only for the specialist can read as narrow to the generalist; one written only for the generalist loses the specialist's trust. The intro and abstract should satisfy both in their first paragraphs.

## Checklist

- [ ] Each predictable microstructure objection has a planned answer before submission
- [ ] Measurement-artifact and endogeneity objections are pre-empted with concrete exhibits
- [ ] Inference (clustering) objection is closed in advance
- [ ] Post-decision: every comment classified fatal / fixable / defensible / editor-flagged
- [ ] The editor's priorities are extracted from the letter, not just the referees'
- [ ] Push-backs are evidence-based, never tone-based
- [ ] The paper carries at least one advocacy hook (clean shock, new measure, exact institutions, or mechanism-predicted heterogeneity)

## What a microstructure referee rewards, beyond catching flaws

Anticipating objections is defensive; the strongest submissions also give the referee reasons to advocate. A microstructure specialist becomes a champion when the paper (1) gets the **institutional detail exactly right** — they trust authors who clearly know the market's plumbing; (2) offers a **clean identifying shock** they had not thought to exploit; (3) introduces a **measure or decomposition** they will want to use themselves; (4) shows the effect **where the theory predicts**, demonstrating command of the mechanism. Build at least one of these into the paper deliberately, and surface it in the intro and cover letter. A pre-mortem that only patches weaknesses produces a defensible paper; adding an advocacy hook produces an accepted one.

## Anti-patterns

- Treating a microstructure referee like a generalist and under-explaining the mechanism
- Ignoring the measurement-artifact objection because the idea feels strong
- Reading referee reports without separating editor-prioritized comments from the rest
- Planning to argue down a fatal endogeneity concern instead of redesigning
- Discovering a foreseeable objection only after the reject

## Estimating whether an R&R is reachable

Not every revise request is equally winnable. Sort the editor's asks by the cost and risk of the work they demand. **Tractable** R&Rs ask for alternative liquidity measures, better clustering, more robustness, sharper exposition, or an added subsample — all additive, none threatening the core. **Hard but doable** R&Rs ask for a heterogeneity test of the mechanism or a new data source for generalizability. **Near-reject** R&Rs question the identification itself ("we are not convinced liquidity is exogenous here") — these require a redesign, not a patch, and you should decide honestly whether you can deliver one before sinking months into a revision. Tell coauthors which bucket the letter is in; mis-reading a near-reject as a tractable R&R wastes a cycle.

## Output format

```text
【Journal】Journal of Financial Markets (JFM)
【Skill】jfm-referee-strategy
【Mode】pre-mortem / post-decision triage
【Top objection】<microstructure line> → planned answer
【Measurement defense】alternative constructs ready? [Y/N]
【Endogeneity defense】shock/IV ready? [Y/N]
【Triage (if report)】fatal / fixable / defensible / editor-flagged counts
【Editor signal】what must be resolved for acceptance
【Next skill】jfm-rebuttal
```
