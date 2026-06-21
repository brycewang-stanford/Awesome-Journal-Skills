---
name: msom-review-process
description: Use to understand how Manufacturing & Service Operations Management (M&SOM) review and decisions work — the author-routed six-department structure, the Department Editor / Associate Editor / referee chain, double-anonymous review, special tracks (OM Forum, Practice Platform, OM Grand Challenges), and how to read a decision letter — before or after submitting.
---

# Review Process (msom-review-process)

## When to trigger

- You want to set realistic expectations before submitting to M&SOM
- You received a decision letter and need to understand the roles behind it
- You are deciding whether a special track (OM Forum, Practice Platform, Grand Challenges) fits
- You are unsure how department routing shapes who handles your paper

## The editorial chain: department routing decides your fate

M&SOM uses an **author-driven version of departmental routing**. You choose a primary **Department** and name **two preferred Department Editors**; the manuscript is then handled by a **Department Editor (DE)**, who assigns an **Associate Editor (AE)**, who recruits **referees**. The stable routing frame is organized around Manufacturing & Supply Chain Operations, Services/Platforms/Revenue Management, Environment/Health/Society, Operational Innovation, Analytics in OM, and Practice Platform; the current editorial-board page also lists AI in Operations and Outreach groups. Because routing is by department, *matching the right department is as consequential as the paper's quality* — a misrouted paper meets the wrong expertise.

## Double-anonymous review

Review is **double-anonymous**: authors and referees are blind to each other. Author identities are known only to the **Editor-in-Chief**, the DE, the AE, and editorial staff, and remain confidential to referees. This is why anonymization (see `msom-submission`) is strictly enforced.

## Decision criteria and special tracks

Decisions weigh **importance, originality, clarity, validity, and relevance**, gated by the **operations-centrality** requirement. Beyond standard research articles, M&SOM institutionalizes practice and perspective:

- **OM Forum** — thought-leadership/perspective pieces under an identifying banner.
- **Practice Platform** — a dedicated department for field-driven, practice-based OM.
- **OM Grand Challenges (2026)** — SDG-aligned academic-practitioner proposals; accepted proposals presented at the 2026 MSOM Conference (12–14 July 2026) automatically advance into a second review cycle for a dedicated M&SOM special issue — a conference-to-journal fast-track.

> Editor context: Georgia Perakis (MIT) is listed as Editor-in-Chief on the 2026-06-20 M&SOM pages; INFORMS announced that her final term expires 31 December 2026 and that the search committee aims to propose a successor by 1 July 2026. Check the editorial-board page before naming current DEs or AEs in a submission plan.

## Reading a decision letter

- **Reject / desk reject:** often an operations-centrality or fit miss — reassess venue and department.
- **Major revision:** the DE/AE see a path; the referee points are the contract for the next round.
- **Minor revision:** address precisely; do not reopen settled modeling choices.
- Identify which comments come from the **DE/AE** (binding priorities) vs. **referees** (must be addressed or rebutted).

## Checklist

- [ ] Primary Department and the role chain (DE → AE → referees) understood
- [ ] Double-anonymous expectations clear; manuscript fully anonymized
- [ ] Special-track fit assessed (OM Forum / Practice Platform / Grand Challenges)
- [ ] Decision letter parsed into DE/AE priorities vs. referee points
- [ ] Realistic timeline and multi-round expectations set

## Anti-patterns

- Picking a department by prestige rather than fit, drawing the wrong expertise.
- Treating all reviewer comments as equal weight, ignoring DE/AE signals.
- Assuming a perspective piece will be judged as a standard research article (it is OM Forum).

## Desk-screen and decision patterns to expect

A desk reject on "fit" usually means the operations decision is a backdrop; an "incremental" reject means structure was proven but no managerial insight attached; an "identification" reject means endogenous operations were treated as exogenous; a perspective piece judged as a research article was on the wrong track (it belongs in OM Forum). M&SOM is the INFORMS MSOM-Society journal for the operations management of manufacturing and service systems, so a contribution a practitioner can use is the bar.

## Worked micro-example (illustrative)

Vignette: a paper on warehouse pick-path optimization is submitted to "Analytics in OM." Two referees split: one praises the method, the other notes the warehouse layout is treated as fixed when it is in fact a managed decision. The AE flags layout endogeneity as the binding item and asks for a clearer takeaway. Reading the letter correctly means treating the AE's items — not the referee's praise — as the contract, then switching into `msom-rebuttal`.

## Referee-pushback patterns and the venue fix

- *"Strong analytics, but where is the operations decision?"* → Re-center on the operating lever; analytics in service of an OM decision, not for its own sake.
- *"This belongs in a broader OR/MS or general-management outlet."* → If a sibling venue genuinely owns the contribution, re-route; M&SOM's scope is tighter and OM-specific.

## Output format

```
【Department / role chain】DE → AE → referees ...
【Review model】double-anonymous; anonymization OK? ...
【Track】standard / OM Forum / Practice Platform / Grand Challenges ...
【Decision parsed】DE-AE priorities vs. referee points ...
【Next step】on R&R → msom-rebuttal
```
