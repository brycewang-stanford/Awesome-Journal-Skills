---
name: jebo-referee-strategy
description: Use when anticipating the objections a Journal of Economic Behavior & Organization (JEBO) referee will raise before submitting — demand effects, mechanism-vs-alternative, external validity, sibling-journal fit. Pre-empts the modal JEBO referee; it does not draft the rebuttal to a received report.
---

# Referee Strategy (jebo-referee-strategy)

## When to trigger

- The draft is near-complete and you want to find the holes a referee will find first
- You suspect a referee will say "interesting, but it belongs in [sibling journal]"
- You cannot articulate why your behavioral mechanism beats the obvious alternative
- A coauthor wants to know which objections are fatal vs. addressable
- You are deciding what to add now vs. defend in the response letter

## Who referees for JEBO

JEBO uses **single-anonymized** review (referees anonymous, authors named), typically **two-plus referees** after an editor screen (检索于 2026-06；以官网为准). The modal referee is a behavioral or experimental economist who has *seen the closest prior experiment* and is alert to the standard ways a behavioral claim can fail. Single-anonymized review means your name and prior work are visible — consistency with your own record and the relevant literature matters.

## The objections JEBO referees raise most, and how to pre-empt

| Referee objection | Pre-empt before submitting |
|-------------------|----------------------------|
| "This could be an experimenter-demand effect." | Build in a demand-effect bound/treatment; address it in the text, not only if asked. |
| "Your mechanism isn't separated from [rival channel]." | Add a moderation/mediation test the rival does not predict; name the alternative explicitly. |
| "It's a single lab task — does it generalize?" | State the external-validity scope; if possible, a field or alternative-pool replication. |
| "Significance, but is the effect *meaningful*?" | Report effect sizes in interpretable units; compare to a behavioral benchmark. |
| "Why JEBO and not ExpEcon / GEB / JEP?" | Make the behavioral-economics contribution (not the method or the psychology) the headline. |
| "Many comparisons, no correction." | Pre-register the primary outcome; report MHT-corrected results. |
| "Is this just a replication?" | If partly, frame the value-added honestly (new pool, moderator, contested-result confirmation). |
| "The model adds notation but no testable prediction." | Ensure the theory yields a pre-stated comparative static the data test. |

## Triage: fatal vs. addressable

- **Fatal if unaddressed before submission:** deception in an incentivized study without justification; no demand-effect consideration; a confound that fully substitutes for the claimed mechanism; clear wrong-journal fit.
- **Addressable now (cheap, do it):** MHT correction, effect-size reporting, comprehension-pass subsample, balance/attrition tables, a falsification check.
- **Defensible in the letter (if cost is high):** an additional subject pool, a full structural extension — flag in limitations and offer in the response if requested.

## Suggesting and excluding reviewers

Editorial Manager lets you suggest/oppose reviewers. Suggest scholars who know the literature but are not close collaborators (single-anonymized review makes obvious conflicts visible); a credible suggestion of the scholar who owns the closest prior result can help, since they will be invited anyway.

## Checklist

- [ ] Each likely objection above has a pre-empt in the current draft or a planned response
- [ ] Experimenter-demand and mechanism-vs-alternative are addressed in the text, not only reactively
- [ ] External-validity scope is stated honestly
- [ ] Effect sizes are interpretable; not relying on significance alone
- [ ] The "why JEBO" answer is explicit and survives the sibling-journal test
- [ ] MHT/pre-registration handled for multi-arm/multi-outcome designs
- [ ] Reviewer suggestions/exclusions prepared with conflicts in mind

## Anti-patterns

- Hoping the referee won't notice the demand-effect or rival-mechanism gap
- Answering "does it generalize?" with silence rather than a bounded scope statement
- Leaning on asterisks when asked whether the effect is *meaningful*
- Submitting a paper whose strongest fit is a sibling journal and hoping the editor disagrees
- Suggesting only friendly reviewers (transparent under single-anonymized review)
- Deferring cheap, obviously-required checks to "if the referee asks"

## Output format

```text
【Review model】single-anonymized; ~2+ referees after editor screen
【Top 3 anticipated objections】
  1. <objection> → <pre-empt: in-text now / planned response>
  2. ...
  3. ...
【Fatal-if-unaddressed】<list>
【Why-JEBO answer】<one sentence surviving sibling test>
【Reviewer suggestions/exclusions】<prepared>
【Next step】jebo-submission
```
