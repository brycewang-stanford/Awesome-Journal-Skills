---
name: hlr-preemption-check
description: Use when verifying that a Harvard Law Review (HLR) argument has not already been made — the law-review "preemption check" run across SSRN, Westlaw/Lexis, HeinOnline, and Google Scholar BEFORE drafting. Confirms originality and refines the claim; it does not draft the thesis (hlr-thesis-and-contribution) or the literature engagement in the body.
---

# Preemption Check (hlr-preemption-check)

In legal scholarship, **"preemption"** means: has someone already published your argument? Running this
search **before** you write is the single highest-return habit in the field — discovering that your claim
appeared in a 2024 article *after* you have drafted 25,000 words is the classic wasted summer. A clean
preemption check both protects originality and sharpens your contribution against the nearest prior work.

## When to trigger

- You have a candidate thesis and have not yet written the body
- You are about to claim "no one has argued X" or "first to address Y"
- A draft is done and you want to confirm nothing close appeared while you wrote
- An editor or colleague says "isn't this just [Author]'s point?"

## Where to search (run all four; do not stop at one)

| Source | What it catches | Note |
|--------|-----------------|------|
| **SSRN / bepress** | Working papers and forthcoming articles not yet in print | Catches the most recent, still-in-press work — the highest preemption risk |
| **Westlaw / Lexis** journals databases | Published law-review articles, full text | Use field-restricted and date-restricted queries |
| **HeinOnline** | Deep historical law-review archive, PDF page images | Best for older and exact-pinpoint history of an idea |
| **Google Scholar** | Cross-disciplinary and gray-literature reach | Catches non-law work and citation chains |

## How to search well

1. **Search the claim, not just the topic.** Anyone can find articles on "qualified immunity"; search the
   *specific move* — e.g., "qualified immunity" + "common-law indemnification" + your distinctive hook.
2. **Vary vocabulary.** Authors name the same idea differently; run synonyms and the doctrinal terms of
   art, not only your coinage.
3. **Date-bound and re-run.** Restrict to the last 2-3 years for in-press risk, then re-run the search
   right before submission — SSRN updates daily during the seasons.
4. **Follow the citation web.** When you find the nearest neighbor, read what it cites and what cites it.
5. **Read the abstracts and intros**, not just titles — preemption hides in the framing, not the keyword.

## Reading the result (three outcomes)

- **Genuinely new** → state originality precisely and cite the nearest neighbors as the literature you
  advance (hand to `hlr-argument-structure` for engagement).
- **Partially preempted** → refine the claim to the part that remains open; recast the contribution
  ("prior work shows A; this piece shows the stronger/different B"). Loop `hlr-thesis-and-contribution`.
- **Fully preempted** → change the claim or the angle before investing in the draft. Better now than after.

## Checklist

- [ ] Searched SSRN, Westlaw/Lexis, HeinOnline, and Google Scholar — not just one
- [ ] Searched the specific *argument*, with synonyms and terms of art, not only the topic
- [ ] Found and read the 3-5 nearest-neighbor pieces (intros + abstracts)
- [ ] Stated exactly how the claim differs from each nearest neighbor
- [ ] Date-restricted pass for in-press work; plan to re-run before submission
- [ ] Any "first to" language is backed by the search, or removed

## Anti-patterns

- Searching only the topic ("free speech") instead of the argument — everything looks preempted or nothing does
- Relying on a single database (especially skipping SSRN, where in-press preemption lives)
- Searching once, months before submission, and never re-running
- Hiding the nearest competitor instead of citing and distinguishing it
- Keeping a "first to address" claim the search cannot support

## Preemption is not the same as the literature review

A preemption check protects **originality**: has *this argument* been published? The literature review in
the body does different work — it situates the claim among the scholarship a generalist editor expects you
to engage (handled inside `hlr-argument-structure`). The same searches feed both: the nearest neighbors you
find here become the works you distinguish in the body. Do not let a clean preemption result excuse a thin
literature engagement, and do not let a thorough literature review substitute for the targeted, claim-level
preemption search — they answer different questions.

## Worked micro-pattern (illustrative)

A hypothetical author plans to argue that a doctrine *D* should be abolished. A topic-level search for "*D*"
returns hundreds of hits and feels hopeless. Re-running the search at the **argument** level — "*D*" +
"abolition" + the distinctive ground the author relies on — surfaces only two close pieces: one argues for
*narrowing* D (not abolishing it), the other abolishes D on *different* grounds. The verdict is **partially
preempted**: the claim survives, recast as "prior work narrows D or abolishes it on ground X; this Article
abolishes it on the stronger ground Y." The contribution is now sharper *because* of the search. (Counts
and grounds illustrative.)

## Output format

```
【Claim searched】the specific argument (not the topic)
【Databases】SSRN / Westlaw-Lexis / HeinOnline / Scholar [all run? Y/N]
【Nearest neighbors】the 3-5 closest pieces (author, year, the move they make)
【Verdict】new / partially preempted / preempted
【Refinement】how the claim now differs from each neighbor
【Next】hlr-argument-structure (if new) or hlr-thesis-and-contribution (if recast)
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — SSRN, Westlaw, Lexis, HeinOnline access notes
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — sourcing discipline for originality claims
