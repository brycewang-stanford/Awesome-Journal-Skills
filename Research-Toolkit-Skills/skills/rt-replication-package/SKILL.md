---
name: rt-replication-package
description: Use before final submission or on acceptance to assemble and validate the Data-Editor replication package against the target venue's data-and-code policy — master script, pinned environment, README/roadmap, restricted-data plan, and a script-to-exhibit output map, with a checklist that catches the numbers a Data Editor would fail to reproduce. Reads the venue policy live from the pack's source-map.
---

# Replication Package (rt-replication-package)

The step that now blocks acceptance at the top (AEA / JF / Management Science Data Editors
re-run your code and check every number). Full manifest + validation checklist:
[`shared-resources/empirical-methods/replication-package.md`](../../../shared-resources/empirical-methods/replication-package.md).

## When to trigger

- Approaching final submission, or a conditional accept with a data-and-code requirement.
- A Data Editor / verification service needs the package.

## What it does

1. **Read the venue policy** from the target pack's `resources/official-source-map.md`
   (code at submission vs. acceptance? Data Editor? AsCollected page? restricted-data rule?
   hosting?). **Match it exactly.**
2. **Assemble the manifest**: master script (raw → all exhibits), ordered steps
   (clean → construct → estimate → robustness → tables), pinned environment, README/roadmap,
   data (or pseudo/synthetic data for restricted access + access instructions), the
   script→exhibit output map, and the disclosure statement.
3. **Validate** with the checklist: runs clean end-to-end on a fresh machine; every reported
   number reproduced (body + appendix); seeded/deterministic; restricted-data plan; output
   map complete; venue policy satisfied.

## Hard rules

1. **Every reported number traces to a script step** (body and appendix).
2. **Deterministic** — pin versions, seed RNGs.
3. **Restricted data → pseudo/synthetic data + access instructions**, never confidential data committed.
4. **Match the venue's exact policy** from the source-map; re-verify before submission.
5. **Keep it in sync with the execution bridge** — when a revision re-runs an estimate,
   regenerate the affected outputs.

## Output format

```
【Venue policy】(code timing, Data Editor, restricted-data rule, hosting)
【Manifest】master · steps · env · README · data · output-map · disclosure — status each
【Validation】end-to-end ✓/✗ · all numbers reproduced ✓/✗ · seeded ✓/✗ · restricted-data plan ✓/✗
【Blocking gaps】what would fail a Data-Editor check, ranked
【Ready?】GO / NOT-YET — deciding items
```

## Anti-patterns

- "Works on my machine" (absolute paths, unpinned versions, manual steps); reported numbers
  the script doesn't reproduce; committing confidential data; leaving assembly to post-accept crunch.
