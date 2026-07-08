---
name: naacl-topic-selection
description: Use when deciding whether a project should target NAACL rather than ACL, EMNLP, EACL, AACL, LREC-COLING, TACL, or an ML venue — weighing the chapter's Nations-of-the-Americas identity, theme tracks, timing across skipped years, and whether the paper's audience actually convenes at this conference.
---

# NAACL Topic Selection

Every venue in the *ACL family reviews through the same ARR machinery, at
the same rigor, with heavily overlapping reviewer pools. So "is this good
enough for NAACL?" is usually the wrong question. The right ones: *does the
NAACL calendar fit this project's timing*, and *is the room that gathers at
NAACL the room this paper wants*. This skill decides both before a word is
written.

## What the NAACL room is

Since the 2024 renaming — an all-member vote (September 2024) changed
"North American" to "Nations of the Americas" — the chapter's stated
identity spans the hemisphere. That identity shows up materially, not just
nominally: NAACL 2024 in Mexico City ran a "Languages of Latin America"
theme track, NAACL 2025 ran "NLP in a Multicultural World," and workshops
like AmericasNLP (Indigenous languages of the Americas) co-locate here.
None of this narrows scope — general NLP work is the bulk of every program
— but it defines what this venue's audience uniquely rewards:

- work on Spanish, Portuguese, French/Creoles, and Indigenous languages of
  the Americas, especially with community involvement;
- dialectal, code-switching, and migration-linked language phenomena of
  the hemisphere;
- multicultural and cross-variety evaluation methodology;
- plus the full breadth of general NLP that any *ACL flagship takes.

## Routing among near-identical siblings

| Situation | Better target | Reasoning |
|---|---|---|
| Reviews will be ready when a NAACL commitment window is open | NAACL | Timing is the first-order variable in this family |
| No NAACL edition in the next ~12 months (skipped year) | ACL / EMNLP / EACL / AACL | Reviews age; commit them somewhere real |
| Corpus/resource paper where the artifact *is* the contribution | LREC-COLING | Resource-first reviewing culture |
| Result needs >8 content pages of argument | TACL | Journal format, *ACL audience, presentation slot at a conference |
| Contribution is a modeling/optimization advance, language incidental | ML venue (NeurIPS/ICML/ICLR) | The delta is judged against ML lineage, not NLP lineage |
| Americas-language work, early stage or niche | AmericasNLP or another co-located workshop | Right audience, faster feedback, non-archival options |
| Paper speaks to hemisphere-specific phenomena or communities | NAACL over equal-timing siblings | The one case where venue *identity* outranks timing |

## The three-question fit test

1. **Timing:** which ARR cycle would this enter, and does a NAACL
   commitment window plausibly follow it? (If the next edition is
   unannounced, this answer is "unknown" — plan per `naacl-workflow`.)
2. **Audience:** name five groups you want reading this paper. Do they
   attend NAACL specifically — or would any *ACL flagship reach them?
3. **Theme leverage:** does the current edition's theme track (they change
   every edition; verify the live CFP) give this paper a lane where it
   competes on its actual strengths?

```text
Decision rule of thumb:
  timing_fits && (audience_specific || theme_fits)  -> NAACL
  timing_fits && generic *ACL audience              -> NAACL ok,
                                     siblings equally fine — pick by date
  !timing_fits                                      -> nearest sibling now;
                                     NAACL next time it exists
```

## Two routing vignettes

**Vignette A.** A lab finishes a strong instruction-tuning analysis in
June of a skipped year. Audience: general NLP. Timing: the next NAACL is
ten-plus months out and unannounced; an EMNLP-feeding cycle closes in
weeks. Routing: the sibling venue, without sentiment — question two showed
nothing NAACL-specific about the audience, so waiting buys nothing and
costs baseline freshness.

**Vignette B.** A collaboration with a Paraguayan university has built the
first treebank for a Guaraní variety, with community annotators. Audience:
exactly the researchers, community members, and workshop ecosystem that
convene at NAACL and AmericasNLP. Routing: hold for the NAACL window even
at some cost in timing; also weigh LREC-COLING (resource-first reviewing)
and decide by whether the paper's core is the *resource* or the *analysis
the resource enables*. This is the identity-outranks-timing case, and it
is rarer than teams think.

## Shaping the project once NAACL is chosen

- If the work touches any language of the Americas, invest early in native
  data and community contact — the exact dimensions this audience probes.
- Build per-language and per-variety reporting into the experimental design
  from day one rather than retrofitting it.
- Draft the contribution sentence with explicit language scope; if that
  sentence sounds thin, the issue is the evidence plan, not the venue.
- Check the edition's tracks (industry, demos, student research) — a paper
  straining to be a main-conference long paper is sometimes a strong track
  paper.

## Anti-patterns

- Choosing NAACL for prestige-ranking reasons: within this family the
  tiers are a fiction; the programs differ by region and season, not bar.
- Sitting on finished work for a year "for NAACL" while its baselines rot.
- Framing a translated-benchmark study as an Americas-languages paper; the
  audience that rewards the frame is the audience that detects the shortcut.

## Output format

```text
[Fit verdict] NAACL / sibling (which) / workshop / journal / ML venue
[Timing check] <cycle -> commitment window status>
[Audience check] <who convenes here that this paper needs>
[Theme leverage] <current theme track fit, if verified>
[Project shaping] <two concrete design commitments>
```
