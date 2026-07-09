---
name: recsys-camera-ready
description: Use when preparing an accepted ACM RecSys paper for camera-ready, covering ACM two-column de-anonymization and reflow, the ACM Digital Library rights/copyright form, metadata and DOI, integrating rebuttal-promised fixes without overreach, releasing the previously-anonymous code/data repository publicly, and registration and presentation obligations.
---

# RecSys Camera Ready

Use this after a RecSys acceptance. Reopen the current camera-ready instructions, the ACM rights
form, the registration page, and the decision email before advising authors. For 2026 the
Reproducibility and Industry tracks listed a camera-ready deadline of July 27; the Main Track
date was not extractable through the gateway (待核实) — confirm against the decision email.

## Camera-ready audit

- Convert the anonymous submission to the public proceedings version: names, affiliations,
  acknowledgements, funding, platform names where allowed, and the public repository link.
- Apply the current final-page limit and the ACM two-column template; complete the **ACM rights
  and copyright form** and confirm title/abstract metadata and author order for the DOI.
- Integrate the fixes you promised in the rebuttal without changing the accepted contribution
  beyond normal clarification.
- Release the previously-anonymous artifact: replace the anonymized repository mirror with a
  public, licensed, citable archive, and test every link from a logged-out browser.
- Confirm registration and presentation obligations — RecSys expects at least one author to
  register and present; verify the current policy on in-person versus remote.

## ACM two-column reflow

- Flipping the template from anonymous to camera-ready mode changes spacing; recheck every page
  break, figure placement, and the width of every ranking table after the flip.
- Wide offline/online comparison tables and multi-panel figures often need full-column or
  full-width spans; verify nothing is clipped at a column boundary.
- Material that fit the anonymous body can overflow once the author block, acknowledgements, and
  funding lines return; plan the trim before deadline night.
- Keep table, figure, and section numbering stable so the reviews, rebuttal, and meta-review
  remain traceable to the final text.

## De-anonymization sweep

| Item stripped for review | Camera-ready action |
|---|---|
| Author block, affiliations | Restore in ACM template order |
| Acknowledgements, funding | Reinstate; confirm grant numbers |
| Platform / dataset provenance | Restore only what policy and data agreements allow |
| Anonymous repository mirror | Replace with the public, licensed, DOI-able archive |
| Third-person self-citations | Rewrite to first person where it improves clarity |

## Worked example: landing a rebuttal promise

The reviews accepted the paper on condition that the equal-budget tuning protocol move from the
appendix into the main text. Camera-ready move: add two sentences to the experimental setup
naming the shared grid and budget, keep the full grid in the appendix, and add one line to the
abstract that the gain is over tuned baselines — without introducing any number the reviewers did
not see.

## Hedged logistics

- Registration pricing, ACM rights-form mechanics, and the exact camera-ready date change every
  cycle; confirm against the decision email and current proceedings instructions rather than a
  prior year.

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Final package] <PDF / source / bib / ACM rights form / metadata / public artifact>
[Policy checks] <page limit / authors / registration / presentation / artifact release>
[Rebuttal-change map] <promised fix -> final edit>
[Remaining owner] <person -> task>
```
