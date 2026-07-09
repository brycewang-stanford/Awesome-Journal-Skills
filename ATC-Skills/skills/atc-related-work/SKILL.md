---
name: atc-related-work
description: Use when writing or auditing the related-work and positioning of an ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) systems paper — covering the systems literature lanes, positioning against OSDI/SOSP/NSDI/EuroSys/FAST, writing delta-first comparisons, and keeping self-citation double-blind.
---

# ATC Related Work

Position the paper in the systems literature, not against a strawman. ATC's broad scope means your
reviewers span subareas, and a related-work section that a storage reviewer and a networking
reviewer both find fair is a signal the paper is well situated. Because review is **double-blind**,
positioning and self-citation must be handled carefully.

## Cover the lanes a systems reviewer expects

For most ATC papers, at least these lanes should be visible:

- **The direct predecessors** — the systems and techniques you build on or replace, with the
  specific mechanism you change.
- **The alternative approaches** — other ways the community has attacked this problem, and why yours
  differs (not just "we are better," but *how* the design differs and what that buys).
- **The adjacent subareas** — where an idea from storage, networking, virtualization, or scheduling
  informs your design; ATC reviewers respect cross-pollination when it is credited.
- **The measurement/experience literature** — prior studies of the phenomenon you address, so your
  motivation rests on evidence, not assertion.

## Delta-first positioning

Write each comparison **delta-first**: state what the prior system does, then the *specific*
difference and its consequence.

- Weak: "Unlike X, our system is more efficient."
- Strong: "X admits objects on first reference, spending write budget before reuse is known; our
  policy defers admission to a probation window, so writes concentrate on reused objects — the
  difference we measure in §4."

A delta a reviewer can check against your evaluation is worth more than a paragraph of adjectives.
Every claimed delta should map to an experiment (see `atc-experiments`).

## Sibling-venue awareness

ATC sits among specialized and flagship systems venues, and reviewers will expect you to engage the
right literature regardless of where it appeared:

- **OSDI / SOSP:** the flagship line for your subarea — cite the landmark systems even though ATC is
  broader; ignoring them reads as unfamiliarity.
- **NSDI:** for anything touching the network stack, dataplanes, or protocols.
- **FAST:** for storage and file-system work.
- **EuroSys:** the other broad SIGOPS-family systems venue — closely related programs.
- **Workshops (HotOS/HotStorage):** where the idea may have first appeared as a position.

Do not misattribute a landmark to ATC because it is famous — many canonical systems papers are
OSDI/SOSP/NSDI (see `resources/exemplars/library.md` for the guardrail list). Cite each to its real
venue.

## Double-blind self-citation

- Cite your own prior systems and papers **in the third person** — "System X [12] admits on first
  reference" — never "our prior system."
- Do **not** write "reference removed for blind review"; keep the citation, anonymized in phrasing.
- Watch for **implicit** de-anonymization: an unusual system name, a niche testbed, or a dataset only
  your group has can identify you as surely as a name. Neutralize the phrasing or note it generically.
- If a comparison genuinely requires your non-anonymous artifact, mirror it behind a blind service
  (see `atc-submission`).

## Common failure modes

- **Adjacent-work blind spot** — missing a sibling-venue line a subarea reviewer will know cold.
- **Comparison without a measurable delta** — claims of superiority not tied to an experiment.
- **Strawman baselines in prose** — describing prior work as weaker than it is; reviewers who know
  it will distrust the rest.
- **Self-citation leak** — first-person references or an identifying system name breaking anonymity.
- **Venue misattribution** — crediting a flagship result to ATC (or vice versa).

## Output format

```text
[Lane coverage] predecessors / alternatives / adjacent subareas / measurement literature: gaps?
[Delta check] each key comparison stated delta-first and mapped to an experiment? yes/no
[Sibling-venue] OSDI/SOSP/NSDI/EuroSys/FAST lines engaged where relevant? misattributions?
[Anonymity] self-citations third-person? identifying names/testbeds neutralized? "removed for review" absent?
[Fix queue] <ordered edits, most reviewer-visible first>
```
