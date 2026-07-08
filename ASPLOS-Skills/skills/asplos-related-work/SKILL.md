---
name: asplos-related-work
description: Use when positioning an ASPLOS submission against three communities' literatures at once — covering the architecture, OS/systems, and PL/compiler lanes plus accelerator and prior-ASPLOS lines, handling own-work and arXiv material under the 2027 double-blind rules, and meeting the full-name/DOI citation format.
---

# ASPLOS Related Work

An ASPLOS reviewer pool is assembled from three communities, and each reviewer
checks whether *their* literature is handled competently. Related work at this venue
is therefore a coverage problem across parallel lanes — a paper positioned
beautifully against the OS literature and blankly against the architecture
literature reads as half-researched to half its reviewers.

## The five lanes

| Lane | What must be shown | Failure the lane's reviewers spot |
|---|---|---|
| Architecture (ISCA/MICRO/HPCA lineage) | The hardware structure or mechanism is new relative to prior microarchitectural work | Reinvented prefetcher/hint/metadata scheme under a new name |
| OS/systems (SOSP/OSDI/EuroSys/ATC lineage) | The policy/runtime layer differs from existing kernel or hypervisor mechanisms | "The kernel already does this with tunables" |
| PL/compilers (PLDI/POPL/CGO lineage) | Language/compiler-level alternatives are acknowledged when the problem admits them | Hardware solution to a problem the compiler community solved statically |
| Accelerator/domain (when applicable) | Placement in the accelerator design space with honest technology normalization | Comparing against a three-generation-old design point |
| Prior ASPLOS | The intersection lineage itself — what earlier cross-layer attempts did | Missing the exact ASPLOS paper a PC member wrote or shepherded |

For the last lane, mine the venue's own memory: the ACM DL ASPLOS series and the
Influential Paper Award list (see `../../resources/exemplars/library.md`) identify
the papers the community regards as canonical for a given boundary.

## Differentiate on the boundary, not the components

The distinctive ASPLOS positioning move: prior work usually shares *components*
with yours (a similar hardware structure, a similar kernel policy) while drawing
the **hardware/software boundary elsewhere**. Say precisely where each prior system
draws it and why yours moves it:

```text
Template, per closest-prior system:
  "<System> provides <capability> at <layer>, which requires <cost/assumption>.
   Because it keeps <decision> in <layer>, it cannot <the thing your boundary
   placement enables>. We move <decision> to <layer>, which is what makes
   <headline property> possible."
```

Three such paragraphs beat fifteen one-line dismissals — and the systems that get
this treatment should be the ones a hostile reviewer would name.

## Double-blind handling of your own line of work (2027 rules)

- Cite your prior published work **in the third person**, treated exactly like a
  competitor's system.
- Your own arXiv postings and tech reports are **not prior publications** under the
  2027 CFP, and the submission **may ignore them** — you are not forced into
  contortions differentiating against your own preprint.
- A workshop paper this submission extends, or your related manuscript under review
  elsewhere, goes in as **anonymized supplemental material** so reviewers can judge
  the delta (mechanics in `asplos-supplementary`).
- Never use "removed for blind review" placeholders — disallowed wording.

## Format constraints that reshape this section

ASPLOS's citation rules (verified 2026-07-08) have an underappreciated interaction
with related work: every entry needs **all co-authors' full first and last names**
and a DOI/link, which makes each citation *long*. Since references are outside the
11-page limit this costs no body pages — but it means bibliography hygiene is a
real task: budget an editing pass to expand names (`asplos-submission` has the
mechanical sweep) rather than discovering 90 malformed entries at the deadline.

## Timing and staleness

- Sweep the most recent two editions of ASPLOS, ISCA, MICRO, SOSP/OSDI, and
  PLDI before each gate (the September 9, 2026 deadline follows a spring conference
  season — its output is your reviewers' freshest context).
- Concurrent work that appears between cycles: acknowledge it neutrally in a
  revision or camera-ready; a Major Revision's change note is an expected place to
  add "since submission" positioning.

## Building the lane map before writing

Construct the section from a spreadsheet, not from memory:

1. For each lane, list the 5-10 systems a reviewer from that community would
   expect to see; source them from the last two editions' proceedings tables of
   contents (ACM DL for ASPLOS/ISCA/MICRO/SOSP; the respective sites for
   USENIX and SIGPLAN venues) rather than from citation chains, which
   propagate one group's blind spots.
2. Mark each entry: boundary-competitor (gets a template paragraph),
   component-overlap (grouped sentence), or context (grouped citation).
3. Have the co-author closest to each community audit their lane's list — the
   embarrassing omission is almost always in the lane nobody on the team calls
   home.
4. Recheck the map at every gate: between April and September a spring
   conference season publishes, and a reviewer's own new paper is the citation
   they miss first.

## Using the venue's own canon

The Influential Paper Award list is a positioning instrument, not just an
exemplar source: if your boundary has an award-validated ancestor (an
accelerator argued from data movement, a virtualization boundary redraw — see
`../../resources/exemplars/library.md`), citing the lineage and stating your
delta against it signals venue literacy to every senior reviewer. Conversely,
discovering that a canon paper already occupies your claimed boundary is
cheaper during this pass than in a review.

## Where the section lives

With 11 figure-inclusive pages, a late monolithic related-work section is
expensive real estate. The pattern that survives compression: inline
differentiation at first mention for the two or three boundary-competitors
(they are part of the argument, not an appendix to it), plus a compact
lane-organized section that proves coverage. What must not be compressed away
is the boundary-competitor analysis — cutting it saves half a page and costs
the review that says "does not engage with <System>."

## Output format

```text
[Lane coverage] arch / OS / PL / accelerator / prior-ASPLOS — each: covered / thin / n-a
[Boundary paragraphs] closest-prior systems given the template treatment: list
[Hostile-reviewer test] the 3 systems a skeptic would name — all addressed? Y/N
[Own-work handling] third-person OK · supplements needed · arXiv stance decided
[Bibliography hygiene] full-name + DOI pass scheduled/done
[Staleness] newest cited edition per lane
```
