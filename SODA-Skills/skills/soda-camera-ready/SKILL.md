---
name: soda-camera-ready
description: Use when converting a SODA (ACM-SIAM Symposium on Discrete Algorithms) acceptance into a correct SIAM proceedings entry — following the October final-version instructions, condensing the no-limit submission into the proceedings version, restoring author identity, syncing the arXiv full version, and planning the January talk.
---

# SODA Camera-Ready

For SODA 2027, acceptance notices and final-paper instructions go out in **October
2026**, and the conference runs **January 24-27, 2027 in Philadelphia** (checked
2026-07-08 via the SIAM SODA27 pages, read through search renderings). SODA
proceedings are produced through SIAM's publication machinery and appear in the
SIAM Publications Library (`epubs.siam.org`) as "Proceedings of the [year] Annual
ACM-SIAM Symposium on Discrete Algorithms" — e.g., DOI prefix
`10.1137/1.9781611978322` for 2025 and `10.1137/1.9781611978971` for 2026. The
final-version page allowance, the SIAM macro package to use, and the exact upload
route are specified only in the acceptance email each cycle (2027 values: 待核实
until that email exists).

## The condensation problem

SODA reviews the full version but publishes a proceedings version, so October's
work is usually *compression*, the reverse of page-capped venues where
camera-ready means expansion. Decide early which of the three standard shapes the
final version takes:

| Shape | When to choose it | Cost |
|---|---|---|
| Full paper fits the allowance | Short papers, tight allowances rare | None — reformat only |
| Proceedings version + arXiv full version | The normal SODA outcome | Maintaining two documents that must not drift |
| Proceedings version + journal plan | Results with journal-strength depth (SICOMP, TALG, ACM ToA) | Journal referee round later; note the proceedings appearance |

Rules for the cut:

- Theorem statements never change between versions. If compression forces a
  restatement, something is wrong with the plan, not the theorem.
- Cut proofs bottom-up: routine verifications first, then standard-technique
  lemmas, never the novel-technique core. Each cut gets a pointer: "the proof
  appears in the full version [arXiv:XXXX.XXXXX]."
- Update the arXiv record the same week the proceedings version is finalized, so
  the pointer resolves to the version you actually cite.

## De-anonymization checklist

The submission was lightweight double-blind; the proceedings version is not.
Restore, in one pass:

```text
[ ] Author block: names, affiliations, emails — order agreed by all coauthors
[ ] Funding and grant acknowledgements (agency rules on wording checked)
[ ] Personal acknowledgements (colleagues, referees if the PC permits)
[ ] Self-citations returned to natural first-person phrasing where clearer
[ ] ORCID / author-metadata fields in whatever form SIAM's system requests
[ ] PDF metadata regenerated — title and authors, not "anonymous submission"
```

Then run the reverse check: no leftover "the authors of [7]" circumlocutions that
now read strangely, no `\ifanon` branches still active.

## SIAM machinery specifics

- Follow the macro/style instructions in the acceptance email exactly; SIAM
  copyediting is format-strict, and the proceedings are typeset from what you
  hand over. Package name and options for 2027: 待核实.
- A copyright or publication agreement with SIAM is part of the process; the
  signer must be authorized by all authors. Terms and any open-access mechanics
  for the 2027 volume: 待核实 (do not assume another society's defaults).
- The DOI for your paper will hang off the volume's `10.1137/1.978...` prefix —
  cite the proceedings version by that DOI once live, not by a HotCRP link.

## Version-citation hygiene after publication

Once the proceedings entry exists, three versions of the paper circulate — the
proceedings version, the arXiv full version, and (later, perhaps) a journal
version. Set the citation policy now, because other people's bibliographies
will fossilize whatever you put in front of them first:

```bibtex
@inproceedings{YourKey27,
  author    = {...},
  title     = {...},
  booktitle = {Proceedings of the 2027 Annual ACM-SIAM Symposium
               on Discrete Algorithms (SODA)},
  year      = {2027},
  pages     = {...},           % from the SIAM volume
  doi       = {10.1137/1.978...},
  note      = {Full version: arXiv:XXXX.XXXXX}
}
```

- Announce the canonical citation on the arXiv abstract page ("Appeared in
  SODA 2027; cite the proceedings version").
- If a journal version is planned (SICOMP, TALG, ACM ToA are the community's
  registers of record), say so in the arXiv comments so surveys wait for the
  strongest bound rather than quoting the proceedings one forever
  (`soda-related-work` documents the reader-side of this problem).
- Keep theorem numbering stable across versions where possible; downstream
  papers cite "Theorem 3 of [You]" and renumbering breaks them silently.

## January obligations

- SODA talks are the visible payoff; slots are short. Build the talk around one
  theorem, one picture of the technique, one open problem.
- Presentation/registration requirements (who must register, remote options if
  any) are stated in the SIAM acceptance materials: 待核实 per cycle. Assume at
  least one author attends in person and budget for a January North-American trip.
- Coordinate with co-located ALENEX and SOSA schedules if coauthors have papers
  there — the satellite talks share the venue and the audience.

## Deadline map from acceptance to podium

| When (2027 cycle) | Action |
|---|---|
| October 2026 | Read instructions same-day; calendar the final-version due date |
| Acceptance + 1 week | Choose condensation shape; assign the cut list |
| Acceptance + 3 weeks | Final version compiled in SIAM format; internal proofread of every theorem statement against the submitted version |
| Final-version deadline | Upload; archive the exact source used |
| Same week | Push the updated full version to arXiv; add the "to appear in SODA 2027" note |
| December 2026 | Talk draft; dry run with the group |
| January 24-27, 2027 | Philadelphia |

## Output format

```text
[Camera-ready status] On track / At risk / Blocked
[Condensation plan] <shape chosen; sections cut; full-version pointer>
[Identity restoration] <checklist gaps>
[SIAM process] <instructions followed / 待核实 items outstanding>
[Talk plan] <one-theorem story, presenter, registration state>
```
