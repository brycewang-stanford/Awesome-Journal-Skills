---
name: orgstud-contribution-framing
description: Use when sharpening the one-sentence theoretical contribution of an Organization Studies (OS) manuscript and the intro/discussion claims that carry it. Frames the contribution; it does not build the theory (see orgstud-theory-development) or run analysis.
---

# Contribution Framing (orgstud-contribution-framing)

## When to trigger

- The theory and evidence are settled but the paper cannot say its contribution in one sentence
- The intro lists findings rather than a theoretical move; the discussion restates results
- A reviewer says "I don't see the contribution," "this is incremental," or "what does this add to theory?"
- The contribution is described as a *finding* ("we find X") rather than a usable *theoretical move*

## At OS, the contribution is a theoretical move others can use

The single most important sentence in an OS paper is: *"We contribute to [conversation] by [the theoretical move], which shows that [the new understanding]."* The move must be something a reader **elsewhere can pick up and apply** — a new mechanism, a reconceptualized construct, a process model, a resolved tension, a boundary that wasn't seen. A finding is not a contribution; a finding *plus what it changes in how we theorize organizing* is.

OS distinguishes sharply between **empirical contribution** ("we found this happens") and **theoretical contribution** ("this changes how the field should think"). OS desk-rejects papers whose contribution is only the former. Frame the move at the level of the theory, then use the evidence as warrant.

## Calibrating the *size* of the claim

| Claim type | OS verdict | Fix |
|-----------|-----------|-----|
| "First study of X in setting Y" | weak (empirical novelty only) | Reframe as a theoretical move the setting *enabled* |
| "We extend theory T to context C" | risky (often incremental) | Specify what about C *forces* an amendment to T |
| "We reconceptualize construct K" | strong if earned | Show a puzzle that dissolves under the new conception |
| "We theorize a new process/mechanism M" | strong | State M's logic and a non-obvious implication |
| "We bridge conversations A and B" | strong if usable | Give the bridge a name and show what it newly explains |

Avoid both under- and over-claiming. Under-claiming buries a real move under hedges; over-claiming ("we overturn institutional theory") invites reviewers to find the move smaller than advertised. Match the claim to exactly what the mechanism and evidence support (`orgstud-data-analysis` sets that ceiling).

## Where the contribution must appear

- **Abstract** — the move stated plainly within the 300-word unstructured limit.
- **Intro** — the puzzle, why existing theory fails, and the one-sentence contribution, landed on the first page or two.
- **Discussion** — the contribution *developed*: implications for the conversation, boundary conditions, and what new questions it opens (generativity, not a findings recap).
- The same move should read consistently across all three; drift between abstract, intro, and discussion is a common reviewer flag.

## Checklist

- [ ] The contribution fits the sentence "We contribute to [conversation] by [move], showing [new understanding]"
- [ ] It is a *theoretical move others can use*, not just a finding or an empirical first
- [ ] The claim size matches what the mechanism + evidence support (no under/over-claiming)
- [ ] The move is stated consistently across abstract, intro, and discussion
- [ ] The discussion develops the contribution and opens questions, rather than restating results
- [ ] Boundary conditions and scope of the contribution are explicit
- [ ] The framing is unmistakably OS (theory-first), not an empirical-journal framing

## Anti-patterns

- "Contribution" stated as a finding or as empirical novelty ("first study of...")
- Burying a real theoretical move under hedges and qualifications
- Over-claiming relative to the evidence — inviting reviewers to shrink the contribution
- A discussion that recaps results instead of developing the theoretical move
- Abstract/intro/discussion describing three subtly different contributions
- Framing that would suit AMJ/Org Science empirics rather than OS theory

## Referee pushback mapped to the framing fix

- *"I don't see the contribution."* → The intro states findings, not a move. Rewrite the contribution sentence at the level of the theory and put it on page one or two.
- *"This is incremental / well-known."* → The claim is an extension, not a reconceptualization. Show what about your case *forces* an amendment the prior account cannot make.
- *"The contribution is overstated."* → The claim exceeds the evidence ceiling. Pull it back to exactly what the mechanism supports (`orgstud-data-analysis` sets that ceiling).
- *"The discussion just repeats the results."* → Develop the move instead: implications for the conversation, boundary conditions, and the new questions it opens.

## Output format

```text
【Contribution sentence】We contribute to [conversation] by [move], showing [new understanding]
【Move type】new mechanism / reconceptualization / process model / resolved tension / bridge
【Claim calibration】matched to evidence ceiling? (under / right / over)
【Where stated】abstract / intro / discussion — consistent? (Y/N)
【Generativity】the new questions it opens
【Next skill】orgstud-tables-figures
```
