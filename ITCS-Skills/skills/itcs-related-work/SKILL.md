---
name: itcs-related-work
description: Use when positioning an ITCS paper against the theory literature — writing the delta that proves the model/question is genuinely new, covering the right STOC/FOCS/SODA/CCC/TCC lanes, and staying honest under lightweight double-blind where the reference list is not anonymized.
---

# ITCS Related Work

At ITCS, related work carries a heavier burden than at a depth venue: since **conceptual novelty
is the selection criterion**, your positioning must prove the contribution is *genuinely new*,
not merely stronger. A reviewer's most damaging finding is not "someone proved a better bound" —
it is "**someone already asked this question**" or "this is a known model under a new name." The
related-work discussion is where you win or lose the novelty claim, so it is a *load-bearing*
part of an ITCS paper, not an obligatory appendix.

## Delta-first positioning

Lead each comparison with the **delta**, not the citation:

- Name the **closest prior model or question**, state what it did, and then state precisely what
  it **did not ask** that you do. "Prior work bounds the prover's computation; none bounds its
  memory of the interaction" is a delta. "Many works study interactive proofs [3-19]" is a dump.
- Distinguish **new question** from **new answer**. If the question existed and you answer it
  better, say so honestly — and reconsider whether ITCS is the right venue (see
  [`itcs-topic-selection`](../itcs-topic-selection/SKILL.md)); if the *question* is new, make that
  the headline of the paragraph.
- Address **independent and concurrent work** plainly. In a small community with heavy
  arXiv/ECCC posting, a near-simultaneous related idea is common; acknowledging it and drawing the
  distinction reads as strength, not weakness.

## Cover the right lanes

An ITCS paper usually sits at a seam between areas, so its related work must reach across lanes a
single-area reader might miss:

| Lane | Typical venues to survey | Why it matters at ITCS |
|---|---|---|
| Your core area's depth work | STOC, FOCS, the specialist venue (CCC/SODA/TCC) | Shows you know the hard results your idea sits near |
| The *other* area you connect to | wherever that field publishes | An ITCS bridge is only novel if both banks are cited |
| Prior *models/definitions* near yours | ITCS/ICS back-catalog, journals | This is where "already asked" hides — search it hardest |
| Folklore and surveys | monographs, lecture notes, Dagstuhl reports | New questions are often "known folklore"; pre-empt that charge |

Scan the ITCS/ICS back-catalog (dblp `conf/innovations`, LIPIcs volumes) specifically: because
ITCS is *where new models are introduced*, the venue most likely to already contain your idea is
ITCS itself.

## Honesty under lightweight double-blind

ITCS review is **lightweight double-blind**: the PDF hides author names, affiliations, and
emails, but the **reference list is NOT anonymized**, and authors are encouraged to post a
non-anonymous full version to arXiv/ECCC/ePrint. Practical consequences for related work:

- **Cite your own prior work normally in the third person.** Do not anonymize references or write
  "[removed for anonymity]." Refer to your own earlier papers as "[Author, YEAR] shows..." the
  way you would cite anyone — the reference stays in the list, the prose stays neutral.
- **Do not write "in our previous work [12] we..."** — that first-person self-reference is the
  classic leak the anonymity sweep must catch (see [`itcs-submission`](../itcs-submission/SKILL.md)).
- **Do not sabotage coverage to hide identity.** Omitting the obviously-relevant paper by your own
  group to avoid a tell is worse than the tell: reviewers notice the gap, and it damages the
  novelty case. Cite it neutrally.

## Positioning the novelty claim itself

Make the *newness* checkable, the way the rest of the paper makes theorems checkable:

- State the **novelty claim explicitly** ("to our knowledge, no prior work models X as Y") rather
  than implying it — an explicit claim is one a reviewer can confirm or refute, which is the
  honest posture.
- **Bound the claim.** "New, to our knowledge, in the *unconditional* setting" is safer and more
  credible than a blanket "first ever."
- **Credit the lineage.** Showing your idea *descends* from a recognizable line ("this extends
  the non-malleability philosophy to ...") makes it legible and generous without weakening the
  delta.

## Common failure modes

| Symptom | Why it fails at ITCS | Fix |
|---|---|---|
| Citation dump with no deltas | Does not prove novelty, the selection axis | Lead each comparison with what prior work did *not* ask |
| Missed the closest prior *model* | "Already asked" — fatal to a novelty paper | Search the ITCS/ICS back-catalog hardest |
| Anonymized/removed references | Violates the not-anonymized reference rule | Cite normally in the third person |
| "In our prior work [12] we..." | Anonymity leak under lightweight double-blind | Rewrite as a neutral third-person citation |
| Blanket "first ever" claim | One counterexample sinks it | Bound the claim to a precise setting |
| Only your own area cited | An ITCS bridge needs both banks | Survey the connected area too |

## Output format

```text
[ITCS positioning status] novelty-proven / at-risk / unclear
[Closest prior model] <named> ; delta: <what they did NOT ask that you do>
[Back-catalog check] searched ITCS/ICS + connected area for a prior version? yes/no
[Novelty claim] stated explicitly and bounded to a setting? yes/no
[Anonymity] references un-anonymized; no first-person self-cites? yes/no
[Fix queue] <ordered edits>
```
