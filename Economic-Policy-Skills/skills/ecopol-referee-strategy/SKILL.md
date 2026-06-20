---
name: ecopol-referee-strategy
description: Use when preparing an Economic Policy (EP) manuscript for its panel review — the two named discussants and the conference debate that replace standard anonymous refereeing. War-games the discussants; it does not invent evidence or citations.
---

# Panel & Discussant Strategy (ecopol-referee-strategy)

## When to trigger

- A paper has been (or is likely to be) invited to present at an EP biannual conference
- You need to anticipate the two discussants and the live panel debate before standing up
- A coauthor assumes EP runs anonymous refereeing and is preparing the wrong way
- The paper is strong academically but you have not stress-tested the policy angle a policy discussant will press
- You must decide what to fix *before* the conference vs. what to commit to revising after

## EP review is a panel, not a referee pool — plan for it

This is the most EP-specific skill in the pack, because EP **does not run standard double-blind refereeing.** Papers are selected by the **Managing Editor / Panel**, presented at a **biannual conference (summer and winter)**, where **two invited discussants** — chosen to bring an **academic** and a **policy** perspective — act as the referees, debate the paper live in front of the panel and audience, and whose **written comments are published alongside the final paper** (检索于 2026-06；以官网为准). This changes the strategy in three ways:

1. **Reviewers are named and public.** You can (and should) anticipate the *specific* people and institutions likely to discuss your paper. Their comments will appear in print next to yours — they have an incentive to be sharp.
2. **The debate is live and oral.** Unlike a referee letter you answer in writing, you respond in real time. You cannot run a new regression mid-session. Pre-empt, don't defer.
3. **Two perspectives, two failure modes.** The academic discussant attacks rigor; the policy discussant attacks relevance, magnitude, and legibility. A paper can pass one and fail the other.

## War-game the two discussants

| Discussant persona | What they will press | Pre-empt by |
|--------------------|----------------------|-------------|
| Academic (subfield expert) | identification, estimator choice, robustness, "have you tried…" | `ecopol-identification` + `ecopol-robustness` done thoroughly; top 3 objections answered in text |
| Policy (ministry/central bank/Commission) | magnitude, welfare/cost framing, external validity, "what do I do with this?" | `ecopol-tables-figures` units + a crisp policy bottom line; legible main text |

Concretely: **name two plausible real discussants** for your paper (by subfield and by institution, not necessarily by individual), then read your draft as each of them. Where each would object, decide: fix now, or prepare a one-paragraph live answer.

## Pre-conference moves

- **Build an objection ledger:** every anticipated point, its source persona, and your response (fix vs. defend).
- **Prepare the live answers** to the top objections you choose not to pre-fix — a sentence and, ideally, a backup slide/appendix exhibit.
- **Make the policy bottom line unmissable** so the policy discussant cannot say "I don't know what to do with this."
- **Tighten the central magnitude's robustness** — the most common live takedown is "your number isn't stable."
- **Have the replication package ready** (`ecopol-replication-package`) so a provenance challenge is answerable on the spot.

## Checklist

- [ ] Two plausible discussant personas named (academic subfield + policy institution)
- [ ] Draft read as each persona; objections logged with fix-vs-defend decisions
- [ ] Top academic objections (identification/robustness) pre-empted in the main text
- [ ] Policy bottom line is crisp and unmissable for the policy discussant
- [ ] Central magnitude's robustness tightened against the "your number moves" attack
- [ ] Live answers prepared for objections you chose not to pre-fix
- [ ] Replication package ready for a provenance challenge at the conference
- [ ] You are not preparing as if for anonymous written refereeing

## Anti-patterns

- Treating EP review as anonymous refereeing and writing a defensive response letter instead of pre-empting live
- Preparing only for the academic discussant and getting blindsided by the policy discussant (or vice versa)
- Deferring a known weakness to "we'll address it in revision" when it will be debated live and published
- No crisp policy takeaway, so the policy discussant fills the vacuum with skepticism
- Ignoring that the discussants' published comments become a permanent part of the record

## Output format

```text
【Journal】Economic Policy (EP)
【Skill】ecopol-referee-strategy
【Review model】panel + two named discussants (NOT anonymous refereeing)
【Academic discussant】subfield → top objections → fix/defend
【Policy discussant】institution → top objections → fix/defend
【Objection ledger】top 3 with responses
【Live-answer prep】backup exhibits ready? Y/N
【Next skill】ecopol-submission
```
