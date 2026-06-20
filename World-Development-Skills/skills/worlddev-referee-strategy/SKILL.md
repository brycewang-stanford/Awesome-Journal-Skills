---
name: worlddev-referee-strategy
description: Use when anticipating the objections a World Development (WD) manuscript will draw under double-anonymized, multidisciplinary review. Pre-empts referee pushback before submission; it does not invent evidence or citations.
---

# Referee Strategy (worlddev-referee-strategy)

## When to trigger

- Before submitting, to war-game the reports the paper will draw
- The paper sits between disciplines and could face one economist and one non-economist referee with incompatible standards
- A previous WD or sibling-journal rejection cited objections that were never addressed
- The development relevance is implicit and a referee could read the paper as "just an applied estimate"
- You need to decide what to fix now vs. what to defend in the response letter

## The WD review reality

WD review is **double-anonymized**: at least two independent referees, who cannot see who you are (and you cannot see them). Because WD is multidisciplinary, the referee pool is **heterogeneous in method and standard** — a single paper may be read by an applied economist who wants tighter identification and a development sociologist who wants richer context and reflexivity. The strategic implication: **a WD paper must satisfy more than one evidentiary culture at once.** A paper that is bulletproof to one referee community but illegible or naive to the other is the classic WD split-decision that stalls.

Anonymize hard, too — WD's double-blind model means self-citation patterns, "in our previous work," named local institutions, or a give-away acknowledgments line can unmask you and prejudice review.

## War-gaming the two referee archetypes

| Referee lens | What they will attack | Pre-empt by |
|--------------|----------------------|-------------|
| **The methodologist** (often an economist) | identification, clustering, measurement, robustness, over-claiming | Tight design diagnostics; threat-organized robustness; claims matched to warrant |
| **The contextualist** (political scientist / sociologist / area expert) | thin context, no mechanism, no reflexivity, decontextualized numbers, weak external relevance | Grounded institutional detail; a load-bearing framework; scope conditions; named place |

The best WD papers **anticipate both columns**. Map each anticipated objection to a place in the paper that already answers it, and note where you will defend rather than concede.

## Predictable WD objections and the fix

- *"Interesting, but what's the development contribution?"* → Foreground stakes and policy/practice implication; this is the most common WD desk-or-referee killer.
- *"This is an applied paper that could be set anywhere."* → Show what the development context specifically teaches; argue external relevance.
- *"OLS with controls is presented as causal."* → Strengthen the design or downgrade the claim (see `worlddev-identification`).
- *"The qualitative evidence is cherry-picked."* → Add negative cases and a systematic display.
- *"The framework is decorative."* → Make it load-bearing or cut it.
- *"Generalizing from one site."* → State scope conditions; do not claim more than the case supports.
- *"Numbers with no human meaning."* → Translate magnitudes into development-relevant units.

## Suggesting reviewers (where the portal allows)

If Editorial Manager invites suggested/opposed reviewers, propose scholars who **span the disciplines the paper bridges** — not only co-authors' allies — to ensure the contextualist side is read by someone equipped to value it. Justify briefly. Oppose only with a concrete conflict, sparingly.

## Checklist

- [ ] Each likely objection from BOTH the methodologist and contextualist columns is mapped to where the paper answers it
- [ ] The development contribution is explicit enough to survive the "so what?" referee
- [ ] External relevance / scope conditions stated for single-site or single-case work
- [ ] Manuscript fully anonymized (self-citation, prior-work phrasing, acknowledgments, identifying institutions)
- [ ] Qualitative evidence pre-empts the "cherry-picked" charge with negative cases
- [ ] Concede-vs-defend decided for each major anticipated objection
- [ ] Suggested reviewers (if used) span the relevant disciplines

## Anti-patterns

- Optimizing only for the economist referee and ignoring the contextualist who will also be assigned
- Leaving the development "so what" implicit and hoping the referee infers it
- Self-citation or "our earlier study" that unmasks the authors under double-anonymization
- Suggesting only friendly, same-method reviewers
- Planning to defend every objection in rebuttal instead of fixing the cheap ones now

## Output format

```text
【Journal】World Development (WD)
【Skill】worlddev-referee-strategy
【Verdict】submission-ready / pre-empt first
【Methodologist objections】[objection → where answered / fix]
【Contextualist objections】[objection → where answered / fix]
【Development "so what"】explicit? [Y/N]
【Anonymization】clean for double-blind? [Y/N]
【Concede vs defend】split for major objections
【Source status】verified URL / 待核实 / not asserted
【Next skill】worlddev-submission
```
