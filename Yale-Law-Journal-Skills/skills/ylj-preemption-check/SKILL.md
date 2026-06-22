---
name: ylj-preemption-check
description: Use when verifying that a The Yale Law Journal (YLJ) claim is genuinely novel and not preempted by prior scholarship. It runs the systematic SSRN/Westlaw/HeinOnline search and writes the "what's new" paragraph; it does not draft the thesis (use ylj-thesis-and-contribution).
---

# Preemption Check (ylj-preemption-check)

In legal academia, **preemption** means someone already published your claim. A YLJ piece that repeats
an existing argument is dead on arrival — student editors and the faculty they consult are reading the
same SSRN feeds. This skill runs the search systematically and turns the result into the manuscript's
"what's new" paragraph. It assumes the claim is already sharp (`ylj-thesis-and-contribution`).

## When to trigger

- The thesis is sharp and you must confirm no one has made it
- A reviewer/colleague says "didn't so-and-so already argue this?"
- You are about to write the "contribution" paragraph of the introduction
- You need to distinguish your claim from a *close* existing piece, not just confirm absence

## The four-database sweep (do all four; log each)

| Source | What it catches | How to search |
|--------|-----------------|---------------|
| **SSRN** (Legal Scholarship Network) | Working papers not yet in print — the highest preemption risk | Title/abstract keyword + author follows in your subfield |
| **Westlaw** (Secondary Sources / Law Reviews & Journals) | Published law-review articles; KeyCite to see who cites a near-miss | Terms-and-connectors on your core concept + adjacency |
| **HeinOnline** (Law Journal Library) | Full-text historical coverage; older pieces Westlaw may miss | Full-text phrase search; check the foundational articles |
| **Google Scholar / generalist** | Cross-disciplinary work, books, recent preprints | Claim-as-sentence search; "cited by" on the nearest neighbor |

Search the **claim**, not just the topic: combine your novel move with the doctrine (e.g., the specific
mechanism + the specific area), because the topic is crowded but the *claim* may be open.

## Classify each near-miss

For every close piece, decide which applies — and say so explicitly in the draft:

- **Different claim** — same topic, different argument → cite and move on.
- **Same claim, narrower** — they did one circuit / one statute; you generalize → frame as extension.
- **Same claim, different ground** — they argued it on policy; you argue it on text/history → frame as a new justification.
- **Genuinely preempted** — they made your exact move → **change the claim** (back to `ylj-thesis-and-contribution`), do not paper over it.

## Near-miss ledger

Do not rely on memory after the search. Build a ledger for the closest sources and use it as the
validation record for the contribution paragraph:

| Field | What to record |
|-------|----------------|
| **Exact claim searched** | One sentence, with doctrine + mechanism + proposed move |
| **Search string / database** | The query used in SSRN, Westlaw, HeinOnline, and Scholar |
| **Closest source** | Author, title, venue, year, and pinpoint or abstract sentence |
| **Overlap** | Same topic / same mechanism / same remedy / same institutional actor |
| **Classification** | Different claim / narrower / different ground / **PREEMPTED** |
| **Draft action** | Cite and distinguish / frame as extension / change thesis |

Validation rule: the "what's new" paragraph is not ready until the closest near-miss can be described
fairly in one sentence and the piece's added move is different enough that a skeptical student editor
would not call it a relabeling.

## Write the "what's new" paragraph

Output a paragraph that (1) names the closest prior work, (2) states precisely what it did, and (3)
states what your piece adds that it did not. This becomes the contribution paragraph student editors
look for first.

## Checklist

- [ ] All four sources searched on the **claim**, not just the topic
- [ ] SSRN checked for unpublished work in the exact subfield (highest risk)
- [ ] Each near-miss classified (different / narrower / different ground / preempted)
- [ ] No "genuinely preempted" survivor — if found, claim revised
- [ ] "What's new" paragraph drafted, naming the closest prior work explicitly

## Anti-patterns

- Searching only the topic, declaring novelty, and missing a same-claim SSRN draft
- Ignoring an SSRN working paper because it is "not published yet" (editors read it anyway)
- Burying a close competitor in a string cite instead of distinguishing it head-on
- Overclaiming "no one has ever" when a foundational HeinOnline piece said something adjacent
- Reframing as novel a piece that is actually preempted — student editors will find it during source-pull

## Output format

```
【Claim searched】the exact sentence searched, not just the topic
【Sources swept】SSRN / Westlaw / HeinOnline / Scholar (all four? Y/N)
【Closest prior work】author, venue, what it did
【Relationship】different / narrower / different ground / PREEMPTED
【Ledger】search strings + near-miss classifications recorded? Y/N
【What's new】one-paragraph contribution statement
【Next】ylj-argument-structure (or back to ylj-thesis-and-contribution if preempted)
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — SSRN / Westlaw / HeinOnline / legal-research access notes
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — YLJ originality / anonymized-review facts
