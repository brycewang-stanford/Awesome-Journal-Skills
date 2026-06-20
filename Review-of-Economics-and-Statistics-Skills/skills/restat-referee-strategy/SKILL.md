---
name: restat-referee-strategy
description: Use when anticipating the objections a The Review of Economics and Statistics (REStat) referee will raise for a given design, and pre-empting them in the manuscript before submission. Maps threats to defenses; it does not draft the post-decision response letter (that is restat-rebuttal).
---

# Referee Strategy (restat-referee-strategy)

## When to trigger

- The design is settled and you want to pre-empt the obvious referee objections
- You need to decide which robustness checks belong in the paper vs the online appendix
- You want to write the intro/robustness so a referee's first question is already answered
- Before submission, to stress-test the manuscript against a REStat referee's mindset

## The REStat referee mindset

REStat referees are **applied economists who attack identification and measurement first**. They ask: *Is the design actually clean? Is everything measured well enough to support the claim? Would the result survive the specification I would run? Does the conclusion exceed the evidence?* Because REStat publishes across many applied fields, expect a referee who knows your subfield's data quirks intimately. The winning manuscript **answers the top objection inside the paper** — one paragraph plus one exhibit — before the referee can raise it.

## Threat → pre-emption map by design

| Design | The objection a REStat referee raises first | Pre-empt with |
|--------|---------------------------------------------|---------------|
| DID (staggered) | "TWFE is biased with heterogeneous timing" | Het-robust estimator (CS / Sun–Abraham) + flat event-study + Bacon decomp |
| DID (any) | "Pre-trends / parallel trends fails" | Pre-trend tests + honest-DID bounds (Rambachan–Roth) |
| RD | "The running variable is manipulated" | Density test (CJM) + covariate smoothness + bandwidth sensitivity |
| IV | "Exclusion restriction is violated / instrument is weak" | Institutional + falsification defense of exclusion; effective-F; AR weak-IV sets |
| Shift-share | "Shares/shocks are endogenous" | GPSS share-exogeneity or BHJ shock-exogeneity argument + implied estimates |
| Any | "Your key variable is measured with error" | Validation sample / attenuation correction / bounds (REStat-signature) |
| Any | "Inference ignores clustering / few clusters / many tests" | Right clustering + wild-cluster bootstrap + MHT correction |
| Any | "The conclusion overreaches the estimate" | State the estimand and scope; bound external-validity claims |

## Strategy moves

1. **Rank the threats.** List the 4–6 objections this design invites, hardest first.
2. **Answer the top one in the main text** — one paragraph + one exhibit — so the referee sees it pre-empted.
3. **Budget the rest** between main text and online appendix; signal in the text where the appendix answers a concern.
4. **Pre-write the hard concession.** Where the design is genuinely limited, state the limit and bound it — this buys referee trust.
5. **Match exhibits to threats** (hand to `restat-robustness` for the suite, `restat-tables-figures` for presentation).

## Checklist

- [ ] Top 4–6 objections for THIS design listed, hardest first
- [ ] The single hardest objection is answered in the main text (paragraph + exhibit)
- [ ] Measurement-error objection explicitly addressed (REStat referees raise it)
- [ ] Inference objection pre-empted (clustering / few-cluster / MHT)
- [ ] Scope/external-validity bounded so "overreach" cannot be the easy rejection
- [ ] Remaining checks budgeted between main text and online appendix with signposts

## Anti-patterns

- Hiding the obvious objection and hoping the referee misses it (they will not)
- Burying the answer to the top objection in a footnote or deep appendix
- A defensive tone that argues instead of demonstrating with an exhibit
- Ignoring measurement quality because the identification looks clean
- Overclaiming generality, handing the referee the easiest possible rejection

## Worked vignette: pre-empting the measurement objection (illustrative)

A trade paper uses a shift-share instrument and the author is braced for the usual exogeneity questions. But
the *first* objection a REStat referee raises is about **measurement**: the industry-share weights are built
from a base-year census the referee believes is mismeasured for small sectors. Anticipating this, the author
adds, in the main text, a one-paragraph defense plus one exhibit — re-estimating with shares from an
independent survey and showing the estimate barely moves — before any referee sees the paper. The exogeneity
question (shares vs shocks, BHJ) is handled in a second paragraph. By pre-empting the *measurement* objection,
not just the identification one, the author removes the easiest path to a critical report — the REStat-specific
move siblings often miss.

## Output format

```
【Design】[DID / RD / IV / shift-share / measurement]
【Top objections (ranked)】1:[...] 2:[...] 3:[...] (4–6)
【Hardest answered in main text?】paragraph + exhibit? [Y/N]
【Measurement objection addressed?】[Y/N]
【Inference objection pre-empted?】[Y/N]
【Scope bounded?】external-validity claim limited? [Y/N]
【Main vs appendix budget】main: [...]; appendix: [...]
【Next step】restat-submission
```
