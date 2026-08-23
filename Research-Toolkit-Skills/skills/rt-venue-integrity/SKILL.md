---
name: rt-venue-integrity
description: Use before submitting to a venue this repository does not cover, one that arrived by email solicitation, or one whose indexing status matters for a tenure or degree requirement. Runs a source-by-source verification protocol — indexing, publisher, editorial board, fees, retraction history — and reports what each primary source says. It never labels a journal; it reports checks.
---

# Venue Integrity Check (rt-venue-integrity)

The 743 venues in
[`shared-resources/journal-selection/venue-index.tsv`](../../../shared-resources/journal-selection/venue-index.tsv)
were each curated into this repository from their own published guidance, so a venue
being in the index is at least evidence that someone looked. The moment an author steps
outside it — and
[`journal-match.md`](../../../shared-resources/journal-selection/journal-match.md)'s
coverage-honesty rule requires saying so rather than forcing a poor fit — this
repository has nothing to offer, and that is exactly the moment the risk appears: a
solicitation email, a plausible-looking title, an APC, and a paper that becomes
uncitable and cannot be resubmitted elsewhere.

This is the check to run before that submission.

## First: is it actually outside the index?

```bash
python3 tools/match_venues.py --title "<the venue's name>" --top 5
grep -i "<name fragment>" shared-resources/journal-selection/venue-index.tsv
```

Venues appear under several names, and a Chinese journal's English title or an
acronym's expansion often looks unfamiliar when the venue is in fact covered in depth.
If it is in the index, stop — the pack answers the question better than this checklist
does, and the checks below are for venues nobody here has vetted.

## When to trigger

- The target venue is **not** in `venue-index.tsv` and not in a breadth bundle.
- The invitation arrived unsolicited, by email, praising the author's "esteemed work".
- A degree, tenure or funding rule requires a specific index (SSCI / SCIE / Scopus /
  CSSCI / 北大核心), and the venue's claim to it has not been verified.
- The venue's name closely resembles a well-known journal's.
- An APC is quoted and the author is deciding whether to pay it.

## The protocol

Verify each item **against the source named**, at the time of asking. Record the source
and the date. A claim on the journal's own website is not verification of that claim.

| Check | Verify against | A finding worth stopping for |
|---|---|---|
| Indexing claim (SSCI/SCIE/ESCI) | Clarivate **Master Journal List** search | listed nowhere, or listed only in ESCI while the site claims SCIE |
| Indexing claim (Scopus) | Elsevier **Scopus source list** (title + ISSN) | absent, or marked discontinued |
| Open-access legitimacy | **DOAJ** entry | absent, or removed |
| Chinese index claim | the current **CSSCI** / 北大核心 catalogue for the stated period | claimed for a period it was not listed |
| Delisting history | the index's own discontinued-titles list | delisted, and when |
| ISSN and title | the **ISSN Portal** | ISSN belongs to a different title |
| Publisher identity | publisher's site, membership of **COPE** / OASPA / STM | no traceable publisher, or a membership that cannot be confirmed |
| Editorial board | spot-check three named editors at their stated institutions | editors who do not list the role, or cannot be found |
| Fees | the journal's own author guidelines | fee disclosed only after acceptance |
| Peer review | the stated policy, and the promised timeline | review promised in days; "guaranteed" acceptance |
| Retractions | **Retraction Watch** database, PubPeer for the field | a pattern, not a single retraction |

Five to ten minutes of checking; the failure it prevents is measured in years.

## What this skill will not do

**It ships no list of predatory journals and applies no label.** Those lists are
contested, go stale, and calling a named journal predatory is a factual claim about a
real publisher that this repository is not in a position to make. The output is a table
of *checks*, each with a source and a date, and the author draws the conclusion.

Report a check as **verified**, **failed**, or **could not verify** — and treat "could
not verify" as its own answer, not as a soft pass.

## Output format

```
【Venue】name · publisher · ISSN
【Checks】
  indexing (SSCI)    verified / failed / could not verify — source, date
  indexing (Scopus)  …
  publisher          …
  editorial board    …
  fees               …
  retractions        …
【Unresolved】what could not be verified, and what would resolve it
【What this means for the requirement】whether the degree/tenure index rule is met
【Author's decision】stated as a decision for the author, with the risks named
```

## Hard rules

1. **Name the source and the date for every check.** An unsourced check is not a check.
2. **Never assert that a journal is predatory, fraudulent or fake.** Report what each
   primary source says or does not say.
3. **"Could not verify" is a finding**, and for an unfamiliar venue asking for money it
   is a serious one. Do not round it up to "probably fine".
4. **An indexing requirement is checked against the index, not the journal.** A journal's
   own claim to be indexed is the thing under test.
5. If the venue **is** in `venue-index.tsv`, this skill is not needed — say so and hand
   back to `rt-journal-match`.

## Anti-patterns

- Judging a journal by its APC. Many reputable open-access journals charge; many
  predatory ones are cheap.
- Treating an unfamiliar name as suspect. Small national and specialist journals are
  legitimate and often the right home for a paper.
- Running the check *after* submission. Withdrawal is not always possible, and
  simultaneous submission is misconduct.

---
*The escape hatch for `rt-journal-match`'s coverage-honesty rule: when the right venue is
outside the index, this is what to do instead of forcing a fit. Part of
[`Research-Toolkit-Skills`](../../README.md).*
