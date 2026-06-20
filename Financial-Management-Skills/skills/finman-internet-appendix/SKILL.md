---
name: finman-internet-appendix
description: Use when deciding what belongs in a Financial Management (FM) internet appendix vs. the main paper, and how to organize it so each supplementary exhibit maps to a main-text claim. Structures supporting material; it does not establish results (finman-identification / finman-robustness) or finalize the data/code package (finman-submission).
---

# Internet Appendix (finman-internet-appendix)

## When to trigger

- The main paper is bloated with secondary tables that crowd the headline result
- A referee asked for a check whose result is reassuring but not central to the story
- Variable-construction detail, sample screens, or derivations are too long for the main text
- You are about to submit and need the supplementary materials organized and labeled

## The FM internet-appendix bar

FM's "people actually read" brand and its **less weight on trivial robustness** stance make the internet appendix a strategic tool, not a dumping ground. The main paper should carry only what a reader needs to be convinced; everything that is *reassuring but not load-bearing* belongs in the internet appendix. The discipline is **traceability**: every internet-appendix exhibit must map to a specific main-text claim or referee concern, and the main text must point to it where relevant. An appendix that is a disorganized pile of leftover tables undercuts the paper; one that is a clean, indexed companion makes the main paper lean and the author look in command of the evidence. (FM's exact archiving/hosting and data-and-code policy — 待核实 against the Wiley author guidelines at submission time.)

## What goes where

| Material | Main paper | Internet appendix |
|----------|-----------|-------------------|
| Headline result + its one identification figure | yes | — |
| The one check that defuses the leading alternative | yes | — |
| Specification sweeps (winsorization, control sets) | — | yes |
| Secondary subsample / placebo tables | — | yes (referenced) |
| Full variable definitions and source fields | summary | full table |
| Sample-screen detail beyond the attrition table | counts only | full screens |
| Derivations / proofs / model details | sketch | full |
| Alternative-measure replications | mention | full |

## Organizing sequence

1. **Index it.** Open the appendix with a short table of contents mapping each IA exhibit to the main-text section or referee point it supports.
2. **Cross-reference both ways.** The main text says "see Internet Appendix Table IA.3"; the IA exhibit's note says which main-text claim it backs.
3. **Keep numbering distinct.** Use an IA prefix (Table IA.1, Figure IA.1) so the main and supplementary sets never collide.
4. **Make each IA exhibit self-contained.** Same standard as the main exhibits — sample, units, clustering, period in the note — because referees read the IA without re-reading the paper.
5. **Resist scope creep.** If an IA exhibit is doing real persuasive work for a binding concern, promote it to the main paper; if it persuades no one of anything, cut it.

## Checklist

- [ ] The internet appendix opens with an index mapping each exhibit to a main-text claim or referee point
- [ ] Every IA exhibit is cross-referenced from the main text where relevant
- [ ] IA numbering is distinct (IA.1, IA.2 …) and never collides with the main set
- [ ] Each IA exhibit is self-contained (sample, units, clustering, period in the note)
- [ ] Load-bearing material was promoted to the main paper; dead weight was cut, not parked
- [ ] Full variable definitions and sample screens live here, summarized in the main text

## Anti-patterns

- An internet appendix that is an unindexed pile of leftover tables
- IA exhibits referenced nowhere in the main text (orphans)
- A genuinely decisive check hidden in the appendix where the editor may miss it
- IA numbering that overlaps the main paper and confuses cross-references
- Treating the appendix as a place to satisfy the urge for trivial robustness FM under-weights
- IA exhibits with no self-contained notes, forcing the referee back into the paper

## Worked vignette (illustrative)

A draft's main paper has eighteen tables, several of them winsorization and control-set sweeps; the headline gets lost. The FM fix: keep five exhibits in the main paper (summary stats, the headline table, the event-study figure, the one Oster sensitivity check, and the economic-magnitude exhibit), move the thirteen sweeps and secondary subsamples to an indexed internet appendix (Tables IA.1–IA.13), and add cross-references both ways. One placebo table that actually rules out a confound gets *promoted* into the main paper. The main paper is now readable in one sitting and the appendix is a clean, navigable companion.

## The promote / park / cut decision

For every candidate supplementary exhibit, make a deliberate call rather than defaulting to "park it":

- **Promote** to the main paper if it defuses a *binding* concern (the editor or a likely referee would reject without it). Decisive evidence buried in an appendix is a wasted asset.
- **Park** in the internet appendix if it is reassuring and a referee may want it, but no reader needs it to be convinced (alternative measures, secondary subsamples, full variable tables).
- **Cut** entirely if it persuades no one of anything — FM's under-weighting of trivial robustness means a sweep that varies nothing material is dead weight even in the appendix.

This three-way call is the actual craft; an appendix that is purely "everything that didn't fit" signals the author never made it.

## Referee pushback mapped to the appendix fix

- *"The paper is too long / I lost the thread."* → Move secondary and sweep tables to an indexed internet appendix; keep the main paper lean.
- *"Where is the check you mention?"* → Add two-way cross-references between the text and each IA exhibit.
- *"This appendix is a mess."* → Open with an exhibit→claim index and give every IA exhibit a self-contained note.

## Code and data alongside the appendix

The internet appendix usually travels with the replication materials. Keep them in sync from the first submission: the IA exhibits should be reproducible from the deposited code, variable definitions in the IA must match the code's construction, and any data-access restrictions (vendor licenses on Compustat, CRSP, governance feeds) should be stated so a referee or the editorial office knows what can and cannot be shared. (FM/Wiley's exact data-and-code policy — 待核实; confirm before depositing.)

## Output format

```
【Main vs. IA split】load-bearing in main; reassuring in IA? [Y/N]
【Index】IA opens with an exhibit→claim map? [Y/N]
【Cross-references】both directions present? [Y/N]
【Numbering】distinct IA prefix, no collisions? [Y/N]
【Promotions/cuts】decisive checks promoted; dead weight cut? [Y/N]
【Policy check】Wiley data/code & hosting policy verified or 待核实
【Next skill】finman-writing-style
```
