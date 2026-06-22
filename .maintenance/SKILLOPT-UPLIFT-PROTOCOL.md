# SkillOpt-Style Uplift Protocol

This repo adapts Microsoft SkillOpt as a maintenance discipline, not as a
blanket rewrite engine. Upstream SkillOpt treats a natural-language skill as the
trainable state of a frozen agent, proposes bounded add/delete/replace edits
from rollout evidence, and accepts a candidate only when held-out validation
improves. SkillOpt-Sleep applies the same idea to local agent usage by mining
past sessions, replaying recurring tasks, gating proposals, and staging them for
review.

For Awesome Journal Skills, the deterministic proxy is:

1. Capture a baseline:

   ```bash
   python3 tools/skillopt_gate.py snapshot --out /tmp/ajs-skillopt-baseline.json
   ```

2. Make a bounded candidate edit:

   - Prefer one pack, one source-map family, or one tool/protocol file at a
     time.
   - Preserve skill/pack/root-entry counts unless an explicit expansion lane is
     open.
   - Re-read `.maintenance/CLAIMS.md` immediately before editing and avoid
     claim-sensitive pack directories.
   - Use add/delete/replace patches, not broad prose regeneration.

3. Gate the candidate:

   ```bash
   python3 tools/skillopt_gate.py gate --baseline /tmp/ajs-skillopt-baseline.json
   ```

4. Keep the candidate only if the gate passes:

   - `tools/run_checks.py --skip-reports` passes.
   - Inventory counts stay fixed unless intentionally allowed.
   - Quality minimum and below-target count do not regress.
   - Source-map warnings, root-card warnings, and machine-only cards do not
     increase.
   - Clone fail hits remain zero.
   - No claim-sensitive pack directory was edited without explicit clearance.

## Current Use

Use this protocol for count-preserving skill improvement. It is especially
appropriate when the lowest scorecard rows are owned by another agent: improve
the validation protocol, source-backed evidence, or unclaimed bottom-band packs
instead of editing active lanes.

For faster exploratory runs, add `--skip-clone` to `snapshot` and `gate`, then
finish with the full gate before handoff. For an intentional expansion lane,
pass `--allow-count-change` only after updating audit tripwires and README
counts in the same bounded batch.
