---
name: jpsp-theory-and-hypotheses
description: Use when building the theoretical argument and deriving testable hypotheses for a Journal of Personality and Social Psychology (JPSP) manuscript, where theoretical innovation is the primary bar and each study in the package must test a specific derivation. Structures the theory; it does not invent constructs or results.
---

# Theory & Hypotheses (jpsp-theory-and-hypotheses)

JPSP's first gate is **theoretical innovation**: reviewers ask whether the paper's *underlying ideas*
are interesting and generative enough, often **independent of** how strong the data are. A package of
well-run studies with a thin idea will not clear the bar. This skill builds the theory and the
hypotheses each study tests; the studies themselves are designed in `jpsp-study-design`.

## When to trigger

- Turning a positioned gap into a precise theoretical account
- Deriving hypotheses that map onto specific studies in the package
- A reviewer questioned the novelty, mechanism, or generativity of the idea

## Ways a JPSP paper can be theoretically innovative

(Adapted from JPSP section guidance; verify per section.) A contribution can:
- develop a **new theory** and provide evidence for it;
- use an existing theory to explain a **new phenomenon**;
- make **novel connections between two theories** to address new questions;
- use a theory to **integrate previously unconnected phenomena**;
- offer a **new mechanism** for an established phenomenon;
- specify **moderators** that reconcile conflicting predictions or define when an effect occurs;
- introduce and validate a **new construct** and show it matters;
- examine an existing theory or phenomenon in an **understudied population**.

## Building the argument

1. **State the core claim** in one sentence, then the **mechanism** (the *why*).
2. **Derive hypotheses that distinguish your account from alternatives.** Each hypothesis should be
   one a competing theory would *not* predict — that is what makes the test diagnostic.
3. **Map hypotheses to studies.** H1 → Study 1 (establish), H2 → Study 2 (mechanism/mediation),
   H3 → Study 3 (moderation/boundary), etc. The package should build cumulatively.
4. **Pre-empt salient alternative explanations** (construct validity, alternative mediators,
   alternative causal models) and design at least one study to rule them out.
5. **State scope and generalization** — to which populations/contexts the theory should and should
   not extend.

## Anti-patterns

- Hypotheses so vague any result confirms them (unfalsifiable)
- A "mechanism" that merely restates the effect in different words
- Studies that all test the same hypothesis instead of building cumulatively
- HARKing: presenting exploratory findings as if they were predicted (see `jpsp-data-analysis`)
- Ignoring the obvious alternative account a reviewer will raise

## Clearing the innovation gate: a worked derivation

*Illustrative — invented to model diagnostic hypotheses, not a real theory.*

Claim: incidental gratitude broadens construal because it shifts attention toward self-transcendent goals. The diagnostic test is what separates this from a "clean effect" that fails the gate:

- **H1 (establish, S1).** Gratitude raises abstract construal vs. neutral. A pure-affect account predicts the same, so H1 alone is *not* diagnostic.
- **H2 (mechanism, S2).** Self-transcendence mediates the effect — a prediction a generic positive-affect account does *not* make. This is the diagnostic hypothesis.
- **H3 (boundary, S3).** The effect attenuates under time pressure, which taxes the goal-shift but not affect — separating mechanism from mood.

Each hypothesis maps to one study, and H2/H3 are built so a competing theory predicts otherwise; that diagnosticity is what an ASC reviewer means by "theoretically generative" — the difference between a JPSP package and a demonstration.


## Operating pass for Journal of Personality and Social Psychology

Treat this skill as an executable review pass, not a prose hint. First lock the construct validity, study sequence, power/robustness plan, and boundary conditions; then judge whether the current manuscript answers the venue's real reader: psychology reviewers who need a theoretical construct, validated measurement, and cumulative-study logic.

- **Do the pass:** Return a claim-evidence-risk ledger rather than a prose-only diagnosis; every recommendation must point to a manuscript location or missing artifact.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Psychological Science for shorter general-interest findings, Personality and Social Psychology Bulletin for field scope, Journal of Experimental Social Psychology for experiment-centered claims; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Core claim】one sentence
【Mechanism】the "why"
【Innovation type】new theory / new mechanism / integration / moderator / new construct / …
【Hypotheses → studies】H1→S1, H2→S2 (mechanism), H3→S3 (boundary) …
【Diagnostic vs alternatives】which alternative each test rules out
【Scope / generalization】where the theory applies
【Next】jpsp-study-design
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — SEM / mediation / process tooling for testing derivations
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — section innovation criteria and review gate
