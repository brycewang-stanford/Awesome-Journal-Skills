# Replication Package — assemble + validate against the venue's data-and-code policy

The step that now blocks acceptance at the top: a Data Editor (AEA, *Journal of Finance*,
*Management Science* AsCollected, many others) re-runs your code from the raw data and
checks every reported number. This capability **assembles** that package from the
execution chain and **validates** it against the *target venue's* policy before you submit.

> The run *is* the package. If you produced your results through the
> [`execution-with-mcp`](execution-with-mcp.md) bridge / the `code/` skeleton, you already
> have the ordered scripts — this turns them into a Data-Editor-ready deliverable.

## Read the venue's policy first (it varies a lot)

From the target pack's `resources/official-source-map.md`: is code required at submission
or on acceptance? Is there a Data Editor / verification service? An AsCollected-style
project page? What is the restricted-data exception (pseudo/synthetic data, access
instructions)? Where is the package hosted? **Match that policy exactly** — a
non-compliant package delays production or the decision.

## Assemble (the manifest)

| Component | What it must contain |
|---|---|
| **Master script** | `00_master` that runs every step in order, raw data → all exhibits, on a clean machine |
| **Ordered steps** | clean → construct → descriptive → estimate (DiD/IV/RDD/DML/…) → robustness → tables/figures (the `code/` skeleton's order) |
| **Environment** | pinned software + package versions (Stata version + `.do` `which`; or `requirements.txt` / `renv.lock` / `conda` env) |
| **README / roadmap** | what each script does, run order, expected runtime, hardware, and the **script → table/figure map** |
| **Data** | raw datasets *or*, if restricted, a **pseudo/synthetic dataset** that lets every program execute, plus precise access instructions and the DUA citation |
| **Output map** | every reported number → the script + line/table that produces it (this is what the Data Editor checks) |
| **Disclosure statement** | data sources, access dates, licenses, conflicts, and the restricted-data plan |

## Validate (run the checklist before submitting)

- [ ] **Runs clean end-to-end** from raw → outputs on a fresh environment (no manual steps,
      no absolute paths, no uncommitted hand-edits).
- [ ] **Every reported number reproduced** — body and appendix — by the master script;
      reconcile any that don't match (the classic Data-Editor failure).
- [ ] **Environment pinned** — versions recorded; randomness seeded (e.g. StatsPAI
      `session(seed=…)` / `set seed`) so results are deterministic.
- [ ] **Restricted data handled** — pseudo/synthetic data ships so code executes; real-data
      access documented; nothing confidential committed.
- [ ] **Output map complete** — each table/figure traces to a script step.
- [ ] **Venue policy satisfied** — hosting, project page, submission-vs-acceptance timing,
      and format all match the source-map.

## Output format

```
【Venue policy】(from source-map: code timing, Data Editor, restricted-data rule, hosting)
【Manifest】master script · steps · environment · README · data · output-map · disclosure — status each
【Validation】end-to-end run ✓/✗ · all numbers reproduced ✓/✗ · seeded ✓/✗ · restricted-data plan ✓/✗
【Blocking gaps】what would fail a Data-Editor check, ranked
【Ready?】GO / NOT-YET — the deciding items
```

## Anti-patterns

- A package that "works on my machine" — absolute paths, unpinned versions, manual steps.
- Reported numbers the script does not reproduce (the #1 Data-Editor rejection).
- Committing confidential data, or having **no** executable path when data are restricted
  (ship pseudo-data so the code still runs).
- Leaving package assembly to post-acceptance crunch — build it as you analyze.

## Hard rules

1. **Every reported number traces to a script step** — body and appendix.
2. **Deterministic** — pin versions, seed RNGs.
3. **Restricted data → pseudo/synthetic data + access instructions**, never confidential
   data in the repo.
4. **Match the venue's exact policy** from the source-map; re-verify before submission.
5. Keep it **in sync with the execution bridge** — when you re-run an estimate for a
   revision, regenerate the affected outputs in the package.

---
*Pairs with [`execution-with-mcp.md`](execution-with-mcp.md) (the run that produces the
package), the `code/` skeleton (the ordered scripts), and each pack's
`*-submission` / `*-replication-package` skill + `official-source-map.md` (the venue policy).*
