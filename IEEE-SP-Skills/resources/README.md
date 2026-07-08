# IEEE S&P Resources

Working material behind the IEEE S&P (Oakland) skill pack. The `skills/`
directory tells an agent what to do; this directory holds what that advice
stands on — verified official sources, real exemplar papers, a worked
first-page rewrite, and a pointer to reusable reproducibility tooling.

## Contents

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every S&P fact (cycle dates, page caps, decision set, ethics rules, artifact badges) to its official URL and access date, and see exactly which items remain 待核实. |
| [`external_tools.md`](external_tools.md) | Open the live S&P / IEEE-security / HotCRP / dblp / Xplore surfaces and run the author-side verification passes before registration and upload. |
| [`exemplars/library.md`](exemplars/library.md) | Position against metadata-verified S&P papers across attack / defense / measurement / SoK lanes without misattributing sibling security venues. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Watch a fictional side-channel opening rebuilt to survive S&P's first-round, no-rebuttal read (before → after). |
| [`code/README.md`](code/README.md) | Reach the shared reproducibility kit and the S&P-specific checks — target snapshotting, disclosure timing, hardware sensitivity — the generic tooling cannot make. |

## Scope note

This is a security-and-privacy flagship pack. The evidence culture it encodes
— explicit threat models, adaptive-adversary evaluation, responsible
disclosure, IRB/ethics records, and world-snapshotting of live targets —
differs from both the econometrics journal packs (no Stata/DiD kit here) and
the general ML-conference packs (a leaderboard win is not a security result).
Do not import the economics code library.

## What makes S&P mechanically different

These are the venue facts that drive most of the advice, and most of the
mistakes made by authors arriving from other conferences (all checked
2026-07-08; reopen the live pages before acting):

- **Multiple submission cycles per symposium**, each a self-contained
  mini-conference with its own HotCRP site, binding registration freeze,
  review rounds, and decision date — you choose a cycle, not "the deadline."
- **A round structure inside each cycle**: weak papers get an early reject
  **without a rebuttal**; survivors see reviews and file a short rebuttal.
- **A three-way decision — Accept / Revise / Reject** — where **Revise** is a
  structured major revision against a written expectations summary, and
  Accept comes with a shepherd who checks off meta-review concerns.
- **Ethics is structural**: an Ethics Considerations field at registration, a
  Research Ethics Committee that can reject on ethical grounds, the Menlo
  Report as the named baseline, IRB disclosure, and harm mitigation for PII.
- **13 body pages + ≤5 references/appendix (18 total), compsoc template**,
  with reviewers **not required to read appendices**.
- **Post-acceptance artifact evaluation** with Available / Functional /
  Results Reproduced badges.

## Suggested route through the pack

1. **Fit first:** [`../skills/ieeesp-topic-selection`](../skills/ieeesp-topic-selection/SKILL.md)
   with the exemplars library open beside it — is there a real adversary, and
   is it a research paper or an SoK?
2. **Plan the cycle:** [`../skills/ieeesp-workflow`](../skills/ieeesp-workflow/SKILL.md),
   working backward from a specific cycle's registration week.
3. **Build evidence:** [`../skills/ieeesp-experiments`](../skills/ieeesp-experiments/SKILL.md)
   and [`../skills/ieeesp-reproducibility`](../skills/ieeesp-reproducibility/SKILL.md),
   using [`code/README.md`](code/README.md) for artifact smoke checks.
4. **Write and package:** [`../skills/ieeesp-writing-style`](../skills/ieeesp-writing-style/SKILL.md)
   against the worked example, then
   [`../skills/ieeesp-supplementary`](../skills/ieeesp-supplementary/SKILL.md) and
   [`../skills/ieeesp-submission`](../skills/ieeesp-submission/SKILL.md).
5. **Verify last:** reopen everything in
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) — the snapshot in this pack ages
   by design, and every cycle re-sets dates.
