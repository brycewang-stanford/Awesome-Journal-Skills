---
name: jde-writing-style
description: Use when polishing prose for a Journal of Development Economics (JDE) manuscript so the development question, answer, and policy stakes land for a field audience. A late-stage polish; do not rewrite the intro before identification and framing are settled.
---

# Writing Style (jde-writing-style)

## When to trigger

- The abstract states a setting but not a finding with a magnitude
- The introduction buries the development question under methods or data description
- The prose mixes American and British English, or reads inconsistently
- Identification and contribution are settled and the paper needs its final polish

## The JDE prose bar

JDE readers are development economists; the writing has to make a **first-order development question and its answer** land quickly, with policy stakes explicit. Principles:

- **Abstract states the finding with a number.** Lead with the development question, the design in a
  phrase, and the headline effect in welfare-relevant units — not just "we study X in country Y."
  Regular submissions have a **250-word** abstract cap; pre-results Stage 1 proposals cap the abstract at
  **150 words**.
- **Introduction as an argument.** Question → why it matters for development → setting and design in a few sentences → headline result with magnitude → contribution relative to the frontier → roadmap. Avoid a literature-survey opening.
- **Policy and welfare made visible.** Translate effects into terms a development economist and a policymaker can weigh (poverty gap, cost-effectiveness, test-score SDs).
- **Honest scope.** State external-validity limits plainly; development referees reward calibrated claims and punish overreach.
- **Language consistency.** Write in **either American or British English, not a combination** — JDE requires one consistent variant. Use author-date citations consistently (single author: name + year; two: both names + year; three or more: first author + "et al." + year). JDE accepts any consistent reference style at submission and applies its own at the proof stage, so prioritize consistency over house formatting.

## Tactics

- Cut throat-clearing; the first paragraph should already pose the development question.
- Prefer concrete institutional detail over abstract generality — context is part of the contribution in development work.
- Define constructed variables and indices in words before the reader meets them in a table.
- Keep the conclusion to what the design supports plus honest open questions.

## Abstract rewrite (worked, illustrative)

Hypothetical: a cluster-randomized teacher-incentive experiment in a low-income setting.

- **Weak:** "We study a teacher-incentive program via a randomized experiment and discuss policy implications." Names a topic, states no result.
- **JDE-shaped:** "In a cluster-randomized trial across 200 schools, performance pay raised test scores 0.16 SD (≈ a half-year of learning, *illustrative*); effects faded once incentives ended — pay shifts teacher effort, not durable capital." Design, welfare-unit magnitude, mechanism, scope.

## Prose pushback and the fix

| Referee/editor reaction                              | The JDE-prose fix                                            |
|------------------------------------------------------|-------------------------------------------------------------|
| "The abstract states a topic, not a finding"         | Lead with the headline effect in welfare-relevant units      |
| "A survey delayed the question"                      | Open paragraph one with the development question itself      |
| "Is 0.16 SD meaningful?"                             | Anchor to a policy benchmark (years of learning, cost)       |

## Calibration anchors (hedged)

- Regular submissions have a **250-word** abstract cap; pre-results Stage 1 abstracts cap at **150 words**.

## Anti-patterns

- An abstract that names a topic but states no effect size
- A survey-style introduction that delays the question and result
- Mixing US and UK spelling/usage in the same manuscript
- Inflated external-validity language unsupported by the design


## Style execution pass for Journal of Development Economics

Treat this skill as an executable review pass, not a prose hint. First lock the development constraint, identification, welfare or distribution margin, and implementation context; then judge whether the current manuscript answers the venue's real reader: development economists who expect a development mechanism, credible design, and policy-relevant external validity.

- **Do the pass:** Rewrite the first two pages so each paragraph starts from the venue-level claim, not from chronology or method inventory; preserve exact source-map limits and move technical overflow to appendix or supplement.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against World Development for broader policy audience, JPubE for fiscal/public-finance mechanisms, AER/AEJ Applied for field-wide reach; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Abstract】states finding + magnitude in welfare units? [Y/N]
【Intro arc】question → stakes → design → result → contribution? [Y/N]
【Policy framing】effects in comparable units? [Y/N]
【Language】consistent US or UK English? [Y/N]
【Citations】consistent author-date? [Y/N]
【Next step】jde-replication-and-data-policy
```
