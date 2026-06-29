# Maintenance Tools

These scripts are dependency-free Python tools for repository maintenance. They
are designed to run on a fresh clone of the repository.

## Hard Gates

| Tool | Purpose | Typical command |
|------|---------|-----------------|
| [`run_checks.py`](run_checks.py) | Runs the standard local hard gates, including the monthly dashboard self-test, latest-worklog gate, live dashboard self-check, render-surface smoke, repository count tripwires, quality floor, clone audit, and whitespace check. By default it also runs report-only source-map and root-card audits. CI uses `--skip-reports` so warnings stay advisory and the hard gate stays fast. | `python3 tools/run_checks.py` |
| [`audit_repo.py`](audit_repo.py) | Validates repository invariants: skill counts, pack counts, root marketplace coverage, root journal entries, plugin metadata, required source maps, frontmatter, local Markdown links, and external-import policy. | `python3 tools/audit_repo.py` |
| [`clone_audit.py`](clone_audit.py) | Finds likely find-replace skill clones. CI reports near-clones at 0.75 and fails only at 0.90. | `python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 20` |

## Report-Only Tools

These tools exit 0 by default when they report warnings, and still exit non-zero
for argument or runtime errors. Use `--strict` only when a focused cleanup batch
should fail on warnings.

| Tool | Purpose | Typical command |
|------|---------|-----------------|
| [`source_map_audit.py`](source_map_audit.py) | Reports first-party `resources/official-source-map.md` files with missing source URLs, missing visible check dates, thin content, and heavy unresolved-flag loads. | `python3 tools/source_map_audit.py` |
| [`root_entry_audit.py`](root_entry_audit.py) | Reports progress and source-anchor gaps for the 200 root journal-entry cards. | `python3 tools/root_entry_audit.py` |
| [`quality_scorecard.py`](quality_scorecard.py) | Scores every first-party pack 0–100 on objective quality dimensions. It distinguishes single-venue `depth` packs, compressed AI-conference `conference` packs, and large `breadth` bundles: depth packs get credit for code/worked examples/exemplars, conference packs use a shorter skill-body target, and breadth bundles get credit for routers, rosters/source maps, worked routing cases, and selection patterns. The `unit` column is cross-language: Latin/technical tokens count as one unit and two CJK characters count as one unit. Venue-cue checks use pack names plus common skill-directory prefixes such as `jbf`, `ectj`, or `red`. `code=n/a` means the pack's resources explicitly explain why runnable econometric code is not discipline-appropriate. `--top N` shows the lowest scorers; `--show-skills` names the thinnest files inside each displayed pack; `--json` for diffing the trajectory over time; `--min-score` can gate a focused cleanup. | `python3 tools/quality_scorecard.py --top 20 --show-skills` |
| [`external_link_audit.py`](external_link_audit.py) | Reports liveness for external official/publisher/submission URLs cited in first-party Markdown. It is network-dependent and advisory: 404/410 are actionable, while 401/403/429 and timeouts usually need manual recheck. Results are cached under `tools/.cache/`; `--cache-summary --json` reads that cache and URL inventory without making network requests, including current cache coverage and orphaned cache rows. | `python3 tools/external_link_audit.py` |
| [`monthly_uplift_report.py`](monthly_uplift_report.py) | Aggregates the monthly quality program signals into one Markdown, JSON, compact handoff, local publish-plan, goal-completion audit, debt-audit, owner-clearance request, external-link action plan, or worklog-template snapshot: live counts, score floor, source-map warnings, root-card warnings, external-link cache advisory/action plan, execution-bridge tail coverage, latest worklog status, clone fail-risk, current git dirt, goal-readiness signals, loop-control status, claims-aware current-target notes, full-output unclaimed score/source-map/execution-bridge candidate pools, owner-clearance queue/request, machine-readable remaining-debt and completion-audit evidence, and dynamic next-batch suggestions. Use `--limit N` to show more rows and widen the candidate pool without changing thresholds. Use `--check` or `--check-only` to validate dashboard self-consistency before trusting the next-lane signal. Use `--handoff` for a short next-loop note, `--publish-plan` for a read-only root/tooling staging plan that keeps pack-content lanes blocked, `--goal-audit` for a read-only requirement-by-requirement completion audit that never changes goal status, `--debt-audit` for a read-only remaining-debt register, `--owner-clearance` for a read-only clearance request grouped by score/source/bridge targets, `--external-link-plan` for a read-only cached-link action plan grouped by link verdict class, `--worklog-template` for a populated maintenance-log entry scaffold, `--surface-smoke --skip-clone` to verify that all generated Markdown surfaces still include their required live handoff fragments, `--check-worklog latest` to verify the newest dated worklog entry and next queue, `--json --output PATH` to save a comparable baseline, `--compare-json PATH` to add trajectory deltas, `--self-test` for dependency-free loop-control regression tests, and `--output PATH` to persist the rendered snapshot for a worklog while still printing it. It is read-only except for the requested snapshot file and does not replace the hard gates. | `python3 tools/monthly_uplift_report.py --check --handoff --limit 20` |
| [`skillopt_gate.py`](skillopt_gate.py) | Applies a SkillOpt-style baseline/candidate/validation gate to count-preserving skill edits. It snapshots inventory, scorecard, source-map, root-card, clone, git, and claim-sensitivity signals; `gate` keeps a candidate only if hard checks pass and validation signals do not regress. See `.maintenance/SKILLOPT-UPLIFT-PROTOCOL.md`. | `python3 tools/skillopt_gate.py snapshot --out /tmp/ajs-skillopt-baseline.json` |

## Monthly Quality Program

The 2026-06 uplift lane is measurement-driven and count-disciplined: do not
change expected skill/pack/root-entry counts unless an explicit expansion lane
is approved. Use this report stack to choose and verify batches:

```bash
python3 tools/audit_repo.py --counts
python3 tools/quality_scorecard.py --top 40 --show-skills
python3 tools/root_entry_audit.py
python3 tools/source_map_audit.py
python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 40
python3 tools/external_link_audit.py --cache-summary --json
python3 tools/monthly_uplift_report.py --json --skip-clone --limit 20 --output /tmp/ajs-monthly-baseline.json
python3 tools/monthly_uplift_report.py --surface-smoke --skip-clone --limit 20
python3 tools/monthly_uplift_report.py --check --handoff --limit 20
python3 tools/monthly_uplift_report.py --check --publish-plan --limit 20
python3 tools/monthly_uplift_report.py --check --goal-audit --limit 20
python3 tools/monthly_uplift_report.py --check --debt-audit --limit 20
python3 tools/monthly_uplift_report.py --check --owner-clearance --limit 20 --output /tmp/ajs-monthly-owner-clearance.md
python3 tools/monthly_uplift_report.py --check --external-link-plan --limit 20 --output /tmp/ajs-monthly-external-link-plan.md
python3 tools/monthly_uplift_report.py --check --worklog-template --limit 20 --output /tmp/ajs-monthly-worklog-template.md
python3 tools/monthly_uplift_report.py --check-worklog latest
python3 tools/monthly_uplift_report.py --check --handoff --limit 20 --compare-json /tmp/ajs-monthly-baseline.json
python3 tools/monthly_uplift_report.py --check --limit 20 --output /tmp/ajs-monthly-uplift.md
python3 tools/skillopt_gate.py snapshot --out /tmp/ajs-skillopt-baseline.json
python3 tools/run_checks.py --skip-reports
git diff --check
```

Use `monthly_uplift_report.py` as the live triage view after each batch. It
also reads `.maintenance/CLAIMS.md` and labels current low-score or high
source-map targets that look owned by an active, queued, uncommitted, or
awaiting-review lane. Its readiness table should stay `OK` for the score floor,
source-map warnings, root-card warnings, and clone fail threshold; dirty working
tree entries are an explicit review reminder, not a failure by themselves. The
loop-control table and JSON field summarize whether the next safe lane is
unclaimed content work, owner-cleared content work, or tooling/monitoring. Run
`--check` also validates the embedded latest-worklog status, so dashboard
self-checks fail when the current dated worklog no longer passes its own gate.
The full snapshot also includes worklog health in the goal-readiness table, so
an invalid latest loop is visible beside score floor, source-map, root-card,
clone, and working-tree signals.
Run
`python3 tools/monthly_uplift_report.py --check --handoff --limit 20` when you
need a compact next-loop handoff without the full Markdown tables; the handoff
includes the latest worklog gate in its validation command list and marks
truncated dirty-pack queues with a `+N more` suffix. Run
`python3 tools/monthly_uplift_report.py --check --worklog-template --limit 20`
when you need a populated maintenance-log scaffold before or after a batch;
replace the bracketed placeholders with the concrete files, rationale, result,
and validation outcomes before committing the worklog. Run
`python3 tools/monthly_uplift_report.py --check-worklog latest` after updating
the dated worklog; `latest` and `current` automatically resolve to the newest
`.maintenance/MONTHLY-UPLIFT-YYYY-MM-DD.md` file. Pass an explicit path when
auditing an older monthly log. After appending a new loop, add
`--expect-latest-heading "### YYYY-MM-DD - Loop Title"` to prove the entry you
just wrote is the newest dated section rather than being inserted before an
older loop. Generated validation surfaces, including the full Markdown
snapshot, compact handoff, publish plan, debt audit, and worklog template, print
a copy-pastable strict heading command; if you rename the loop heading, update
that command before treating the validation evidence as final. The check fails
if the latest loop is missing
core scope/result/validation markers, if template placeholders remain, or if
the latest loop still contains planned-validation text such as an unchecked
checklist or "scheduled for this loop", if the latest validation block is
missing any shared next-loop command marker, if a strict latest-heading command
does not match the actual newest heading, or if the current next queue no longer
names the loop-control status and the key next-loop regression gates.
The next-queue check tolerates Markdown line wrapping but still requires the
handoff, latest worklog, full monthly snapshot, audit, scorecard, source-map,
root-entry, fast/full `run_checks.py`, and whitespace gates to remain visible.
Save
`python3 tools/monthly_uplift_report.py --json --output /tmp/ajs-monthly-baseline.json`
before a substantial batch and pass that file back with `--compare-json` after
the batch when you need a trajectory delta for score floor, bridge wiring,
source-map debt, root-card warnings, clone fail hits, claims-boundary row
counts/fingerprint, candidate-gate queue counts, worklog loop count, dirty
working-tree size, dirty pack lanes, root/tooling dirty entries, and inventory
stability. Worktree-boundary, publish-policy, and handoff-manifest fingerprint
deltas are labelled as worktree-sensitive so they are not mistaken for durable
content-debt movement.
The JSON payload includes a `schema` object with the dashboard name, numeric
version, contract label, required top-level fields, nested contract registry,
and nested-contract fingerprint. Schema v28 requires the
machine-readable `worktree_boundary`, `external_links`,
`external_link_action_plan`, `execution_bridge_tail`,
`safe_content_queue`, `content_edit_policy`, `remaining_debt`,
`next_batch_plan`, `publish_policy`, `goal_progress`, `completion_audit`,
`handoff_manifest`, `skillopt_gate_plan`, `surface_smoke_plan`,
`owner_clearance_request`, and
`current_next_queue` objects described below. `--check` rejects a missing or stale schema contract in full dashboard
summaries, so saved monthly baselines remain explicit about the
machine-readable surface they depend on.
The JSON `external_links` object is advisory and report-only. It is generated
from `external_link_audit.py --cache-summary --json`, so the monthly dashboard
can expose checked, unchecked, actionable, inconclusive, current-cache-row, and
orphaned-cache-row counts without making network requests during hard gates.
The JSON `external_link_action_plan` object turns that cached advisory into a
read-only next-action contract. It records the recommended action, network
policy, source advisory fingerprint, dead/redirect/unchecked/blocked/
unreachable/orphaned counts, cache-summary and refresh commands, and a
fingerprint. Use `--external-link-plan` when the next useful link-maintenance
step is to review cached dead/redirect rows or refresh unchecked rows without
editing journal pack content.
The JSON `current_next_queue` object stores the live fragments that must remain
visible in `.maintenance/MONTHLY-UPLIFT-*.md` under `Current Next Queue`.
`--check-worklog latest` builds a lightweight live dashboard snapshot and
rejects stale queue status, schema-fingerprint, execution-bridge-tail,
safe-content-queue, owner-clearance queue/request, content-edit policy,
remaining-debt, next-batch plan, local-publish policy status, command-plan
counts, the owner-clearance request command, the external-link action-plan
command, the surface-smoke command, and the explicit quality-floor command
before accepting the worklog. The v9 queue guard
also checks the global `Current Next Queue` block itself for stale schema,
queue, external-link action-plan, owner-clearance queue/request, and
completion-audit contracts plus the live owner-clearance target fingerprint
fragments, so later dated loop entries cannot accidentally mask stale top-level
handoff prose. The v9 queue guard
intentionally leaves dirty path counts, publish-policy fingerprints, and
handoff-manifest fingerprints to the dedicated worktree-boundary, publish-plan,
and handoff checks, so committed clean checkouts and pre-publish local diffs can
share the same durable continuation guidance. Full clone-gate runs additionally
pin goal-progress and completion-audit fingerprints; `--skip-clone` snapshots
keep the mode-stable fragments and leave those clone-derived fingerprints to
the final full gate. The worklog check uses the canonical 20-row monthly display
context even when the caller omits `--limit`, so direct checks and
`tools/run_checks.py` enforce the same handoff fragments. The same guard also
requires labeled SkillOpt snapshot, gate, and final fast hard-gate command
fragments to remain visible when `skillopt_gate_plan` is present, so future
skill-body loops keep a copy-pastable baseline-before-edit path with the
closing check attached instead of satisfying the guard through a generic
regression-gate mention.
Rendered validation surfaces include the live Current Next Queue fragments
where applicable plus the strict latest-heading command, so the next loop can
copy the machine-checked handoff without reconstructing those contract lines by
hand.
The JSON `surface_smoke_plan` object records the generated Markdown surfaces,
their required live fragments, and a fingerprint for that render contract.
`--check` rejects drift from the plan, and the Current Next Queue pins its
contract, surface count, required-fragment count, and fingerprint so future
handoffs cannot silently drop the generated-surface regression gate. The v5
contract also requires the goal-audit requirement table to keep the SkillOpt,
surface-smoke, external-link action-plan, remaining-debt, owner-clearance, and
execution-bridge-tail rows visible, and it requires the debt-audit surface to
keep the score-floor, source-map, execution-bridge, and ownership-boundary rows
visible instead of passing on headings alone. It also includes the
owner-clearance request surface, which must render the requested decision,
target groups, full target rows, and the no-pack-content-edit notice, plus the
external-link action-plan surface, which must render the decision, action
priority, class-handling table, validation commands, and the no-network notice.
`--self-test` includes paired full-clone and skip-clone fixtures for this
boundary, SkillOpt command coverage, strict latest-heading command fixtures,
next-batch and command-plan visibility fixtures, owner-clearance request
surface fixtures, external-link action-plan surface fixtures,
stale-global-section masking fixtures, and a volatility fixture that proves
worktree/publish/handoff fingerprint drift does not change the v9 queue.
The `execution_bridge_tail` object classifies the remaining empirical-depth
bridge gap as `complete`, `unclaimed-candidates`, `owner-clearance-required`,
or `monitoring`, includes the recommended action, records whether that action
is scoped to unclaimed rows only, and carries a blocked recommendation when
claim-sensitive bridge rows must remain owner-clearance gated. The v3 contract
also records a `claim_sensitive_policy`, whether wiring is allowed now, whether
owner clearance is required before wiring, plus explicit safe-to-wire and
blocked owner-clearance pack lists. It carries a fingerprint that
goal-progress, completion-audit, and handoff-manifest snapshots repeat.
The `safe_content_queue` object classifies the currently unclaimed score,
source-map, and execution-bridge candidates after claims and dirty-pack
filtering, records scorecard-ceiling packs separately from actionable score
debt, records the recommended next action, and carries a fingerprint that
goal-progress, completion-audit, and handoff-manifest snapshots repeat.
The `skillopt_gate_plan` object records whether dirty skill-body lanes are
currently present and always carries the canonical `skillopt_gate.py snapshot`,
`gate`, and final fast hard-gate commands required before the next bounded skill
edit. Root/tooling loops may skip the gate when they do not edit skill bodies,
but the dashboard keeps the baseline/gate/final-gate handoff explicit in the
summary line so `as applicable` does not become an untracked judgment call.
The full Markdown snapshot and compact handoff both print the shared next-loop
validation command block, including the read-only publish plan, latest worklog
check, the fast hard gate, the full `run_checks.py` report phase, and
`git diff --check`.
When the loop-control status is `owner-clearance-needed`, the dashboard output
also prints an owner-clearance queue grouped by score-floor, source-map, and
execution-bridge target type; treat those rows as blocked from content edits
until the owning lane clears them. Long owner-clearance groups are capped in
the compact views and marked with a `+N more` suffix so a truncated display is
not mistaken for the full blocked target set. The JSON snapshot also includes
an `owner_clearance_queue` object with a contract label, total target count,
fingerprint, and per-target-type totals. The v2 queue stores the complete
claims-derived `targets` rows plus a per-kind `target_fingerprint`, while
compact Markdown views still render only the displayed subset, omitted counts,
and truncation flags. `--check` validates both the displayed rows and the
complete target rows, so hidden owner-clearance drift cannot be masked behind a
stable `+N more` suffix. Compact handoff, Markdown, debt, goal, and worklog
views also print the per-kind owner-clearance `target_fingerprint` values, and
the Current Next Queue pins that line so target-hash drift remains part of the
next-loop contract. The completion audit also carries those per-kind target
fingerprints, and Current Next Queue v9 pins the completion-audit rendering of
the same targets, so goal-completion evidence cannot hide owner-clearance
target drift behind the aggregate queue hash. The `owner_clearance_request`
object turns the same queue into a read-only handoff contract: request status,
recommended action, requested decision, blocked edit policy, claim-boundary
fingerprint, per-kind target counts/fingerprints, full target rows, content
policy, and execution-bridge pack decision. Use
`python3 tools/monthly_uplift_report.py --check --owner-clearance --limit 20`
when content debt is blocked and the next useful action is asking an owner to
clear named score/source/bridge targets. The dashboard also reports the execution-bridge tail
separately when remaining bridge gaps require owner clearance, including mixed
tails where unclaimed rows may be wired but claim-sensitive rows must stay
blocked. The blocked pack names and claims-derived reasons appear in the
next-batch guidance, compact handoff, and worklog template. It also reports
the `.maintenance/CLAIMS.md` source boundary with parsed row counts, active-row
counts, line count, and a short SHA-256 fingerprint. Treat a missing or
unparseable claims file as a review blocker because content candidates cannot
be trusted without that ownership boundary.
The JSON `content_edit_policy` object turns the claims-aware loop decision into
a small policy surface: whether content edits are allowed, whether owner
clearance is required, whether tooling-only work is recommended, whether any
execution-bridge tail row still requires owner clearance, the unclaimed and
claim-sensitive target counts, dirty pack-lane count, and a short fingerprint.
`--check` rejects this policy if it drifts from loop-control, execution-bridge,
and worktree-boundary data. Use this field before touching pack content; when
it reports `owner-clearance-required`, keep edits in tooling unless the owner
explicitly clears a content lane.
The JSON `remaining_debt` object records the same score-floor, source-map, and
execution-bridge debt in a compact machine-readable register: unclaimed totals,
owner-clearance totals, owner-clearance queue fingerprint, dirty skipped packs,
dirty pack lanes, score floor, source-map max unresolved count, bridge coverage,
reason text, and fingerprint.
Rendered snapshots, handoffs, and worklog templates include the same one-line
remaining-debt summary; `--check` rejects stale totals or fingerprints so
"honestly triaged" debt cannot quietly drift away from the live claims and
worktree boundary.
Run `python3 tools/monthly_uplift_report.py --check --debt-audit --limit 20`
when a loop needs a focused read-only debt register. It renders the
remaining-debt decision, score/source/bridge table, owner-clearance queue,
dirty-pack boundary, publish policy, and the shared validation command block.
The working-tree line also splits dirty entries into pack lanes and
root/tooling entries, so a handoff can separate candidate-blocking content
work from dashboard, documentation, and maintenance evidence changes before
any path-scoped staging. Compact handoffs and worklog templates also print a
dirty-boundary block with the dirty pack-lane names and the exact
root/tooling status lines plus normalized root/tooling paths, which gives the
next publish pass a concrete path-scoped staging checklist without reopening
the pack lanes. It also separates root/tooling paths into tracked and
untracked lists so the handoff distinguishes existing tooling/docs edits from
new maintenance evidence files. The JSON `git` object includes the same
machine-readable `dirty_pack_paths`, `dirty_root_paths`,
`dirty_root_tracked_paths`, and `dirty_root_untracked_paths` arrays plus a
`dirty_root_pathspec_command` preview. The preview is only a handoff aid; the
dashboard never stages files. `--check` validates that the root/tooling path
list has not accidentally absorbed pack-lane files, that tracked/untracked
root paths reconcile to the full root/tooling path list, and that the preview
command still matches the path list.
The JSON `worktree_boundary` object repeats the same dirty-count split in a
small handoff-oriented shape: branch, dirty count, dirty pack-lane count,
root/tooling entry and path counts, the root/tooling staging command, and a
short fingerprint over the dirty boundary. Compact handoffs, full Markdown
snapshots, and worklog templates render this boundary line; `--check` rejects
it if it drifts from the live `git` object. Use it to confirm a root/tooling
publish plan has not silently absorbed pack-content lanes.
The dashboard also derives a `publish_units` object from the same git-status
snapshot. Its `root_tooling` unit records the exact root/tooling paths,
tracked/untracked counts, and staging command for a possible tooling-only
batch, while `pack_content` records dirty pack lanes as a separate
owner-review unit. Compact handoffs, full Markdown snapshots, and worklog
templates render the same publish-unit split; `--check` rejects it if it
drifts from the dirty-boundary data. The worklog checker also requires the
`Current Next Queue` section to keep a `Local publish-unit split:` note with
the owner-review state, so future loops preserve the publish boundary rather
than only recording metric snapshots. The Current Next Queue v9 guard treats
that note as a policy reminder, not as a strict dirty path count: committed
clean checkouts and pre-publish local diffs should both keep validating against
the durable next-lane guidance.
The JSON `publish_policy` object turns the local-only publish boundary into a
small contract: no publish request is active by default, local-only work is
recommended, path-scoped staging is required if publishing is later requested,
`root_tooling` is the only allowed publish unit, and `pack_content` remains
blocked until owner review clears it. It also carries the root/tooling path
count, pack-content lane count, content-edit clearance state, owner-review
state, root/tooling staging command, reason text, and a short fingerprint.
Compact handoffs, full Markdown snapshots, and worklog templates render this
line; `--check` rejects the policy if it drifts from `publish_units` or the
content-edit policy.
Use `python3 tools/monthly_uplift_report.py --check --publish-plan --limit 20`
when a future publish request needs a read-only staging plan. The plan repeats
the local-only policy, allowed `root_tooling` unit, blocked `pack_content` unit,
exact root/tooling staging command, root/tooling paths, dirty pack-content
lanes, owner-clearance queue summary, per-kind owner-clearance target
fingerprints, and required pre-publish checks. It does not execute git
commands.
The JSON `goal_progress` object turns the active month-long objective into an
evidence surface without marking it complete: worklog status and loop count,
score-floor status, source-map warning status, root-card status, clone-audit
status, execution-bridge coverage, command-plan counts, next-batch count,
owner-clearance state, local-only state, dirty pack-lane count, reason text,
and a fingerprint. Fast snapshots that use `--skip-clone` report
`active-partial-clone-skipped`; full gates must still run clone audit before a
completion or publish claim.
Use `python3 tools/monthly_uplift_report.py --check --goal-audit --limit 20`
for a read-only completion audit. It renders the current decision as
`not-complete`, lists each goal requirement with status and evidence, reports
remaining blockers such as owner-clearance-gated debt, includes the shared
validation command block with the strict latest-heading command, and explicitly
states that it does not change goal status.
The JSON `completion_audit` object backs the same renderer with a structured
contract: completion status, goal status action, requirement rows, status
counts, blocker list, clone-gate/owner-clearance flags, bridge-gap count,
execution-bridge tail action/scope/policy/pack-decision evidence, SkillOpt
gate-plan status/fingerprint, surface-smoke plan contract/counts/fingerprint,
owner-clearance request status/count/fingerprint, remaining-debt
status/totals/fingerprint, owner-clearance queue total and
fingerprint, reason text, and a fingerprint. The requirements include distinct
SkillOpt gate discipline, surface-smoke plan, remaining-debt register,
owner-clearance queue, owner-clearance request, and execution-bridge tail rows so unclaimed,
owner-clearance-gated, dirty-lane, generated-surface,
clearance-before-wiring, and baseline-before-skill-edit debt remains visible
before any goal-close decision. The SkillOpt requirement evidence repeats the final fast
hard-gate command, matching the compact/full summary-line handoff. Full
Markdown, compact handoffs, and worklog templates render a one-line
completion-audit summary; `--check` rejects stale requirement evidence or
fingerprints so a future goal-close decision cannot quietly drift away from the
live dashboard state.
The JSON `handoff_manifest` object folds its own manifest contract, the current
schema contract, loop-control status, claims fingerprint, worklog loop count,
worktree-boundary fingerprint, content-edit-policy fingerprint,
SkillOpt gate-plan fingerprint, owner-clearance queue fingerprint,
owner-clearance request fingerprint,
publish-policy fingerprint,
goal-progress fingerprint, completion-audit contract/counts/fingerprint,
command-plan fingerprint, next-batch fingerprint, and publish-unit counts into
one short fingerprint.
Compact handoffs, full Markdown snapshots, and worklog templates render this
line so the next operator can confirm that the local-only handoff still matches
the machine-readable JSON baseline before staging or publishing.
The same checker rejects planned validation phrasing inside the latest loop's
validation block, including `pending final run`, `PASS expected`, and
`should report`-style notes. Record the observed command result after the
command exits rather than leaving future-tense evidence in the durable log.
Compact handoffs and full Markdown snapshots also render a `Measurement
Commands` block. It keeps the start-of-loop baseline explicit: monthly JSON
snapshot, audit counts, scorecard, source-map audit, root-entry audit, and the
clone audit command. Keep this separate from `Validation Commands`; the former
chooses the next lane from live evidence, while the latter proves the bounded
edit is safe to hand off.
The JSON summary exports the same plan as `measurement_commands` and
`validation_commands`, plus a `command_plan` object with command counts and a
short SHA-256 fingerprint. The current built-in plan has 7 measurement commands
and 15 validation commands, with `--publish-plan` included as the local-only
pre-publish boundary check, `--goal-audit` included as the read-only
completion-evidence check, `--debt-audit` included as the focused
remaining-debt register, `--owner-clearance` included as the read-only
clearance request surface, `--external-link-plan` included as the read-only
cached-link action surface, `--surface-smoke --skip-clone` included as the
generated-surface regression gate, `quality_scorecard.py --top 15 --min-score
90` included as the explicit score-floor gate, and `--worklog-template`
included as the durable handoff-scaffold check. The standalone
`monthly_uplift_report.py --check-only --limit 20 --skip-clone` command is also
part of this plan, so live dashboard loop-control drift is visible before the
full report stack runs. `--check` rejects drift from the built-in command plan.
Rendered handoffs and worklog templates consume those JSON fields so the
machine-readable handoff remains the source of truth, and `--compare-json`
surfaces command-plan count or fingerprint drift across monthly baselines.
The JSON summary also exports the rendered next-batch guidance as
`next_batches` plus a `next_batch_plan` contract/count/fingerprint object.
`--check` rejects drift between the structured next-batch plan and the live
computed recommendations, and `--compare-json` surfaces next-batch count or
fingerprint changes across monthly baselines. The Current Next Queue guard pins
the next-batch contract, count, and fingerprint so stale continuation advice is
not accepted when the live next-lane recommendations change, while leaving
dirty worktree counts, publish-policy fingerprints, and handoff-manifest
fingerprints to the dedicated worktree-boundary, publish-plan, and handoff
checks.
Run
`python3 tools/monthly_uplift_report.py --check-only --limit 20` when you need
a fast consistency gate for loop-control counts without printing the whole
snapshot. Run `python3 tools/monthly_uplift_report.py --self-test` when editing
dashboard logic; this covers the synthetic `content-candidates`,
`owner-clearance-needed`, and `monitoring-tooling` branches, dirty/sensitive
candidate rejection, required handoff and owner-clearance sections, and
trajectory-delta claims fingerprint plus worklog-template rendering. The
unclaimed candidate pool scans the full scorecard, source-map audit, and
execution-bridge tail outputs, not only the displayed top rows, so it can still
suggest a lower-risk next batch when the visible low-tail rows are
claim-sensitive. It also skips packs already dirty in the current worktree so
the next-batch queue does not point back to an in-progress local edit. The
dashboard self-check rejects score, source-map, or execution-bridge candidates
that are claim-sensitive, already dirty, or no longer part of the relevant live
tail. Increase `--limit` when you want a wider ranked pool without changing
audit thresholds. Track score movement, source-map debt, clone triage, and
remaining risks in
`.maintenance/MONTHLY-UPLIFT-2026-06-20.md` or the current dated monthly
worklog before handing off.

For bounded SkillOpt-style edits, take a baseline before changing files and run
`python3 tools/skillopt_gate.py gate --baseline /tmp/ajs-skillopt-baseline.json`
before handoff. Use `--skip-clone` only for exploratory iterations; the final
gate should include clone audit or be followed by `tools/run_checks.py`.
The fast hard gate (`tools/run_checks.py --skip-reports`) runs
`monthly_uplift_report.py --self-test`,
`monthly_uplift_report.py --check-worklog latest --limit 20`, and
`monthly_uplift_report.py --check-only --limit 20 --skip-clone`, so dashboard
logic regressions, stale dated worklog evidence, and live dashboard
loop-control drift are caught before publish without invoking the full monthly
report stack. It also runs `quality_scorecard.py --top 15 --min-score 90`, so
score-floor regressions fail the same fast gate.

### Updating the inventory tripwires

`audit_repo.py` hard-codes the expected skill/pack/root-entry counts so accidental
bulk deletions fail CI. When you intentionally add or remove packs, refresh the
three `EXPECTED_*` constants (and the README badges) in the same commit:

```bash
python3 tools/audit_repo.py --counts   # prints the live numbers to copy in
```

## Asset Rendering (Node)

Unlike the Python maintenance scripts above, [`render_posters.mjs`](render_posters.mjs)
is a Node + Playwright helper for regenerating poster/social images from an HTML
deck. It screenshots every `<article class="poster" id="poster-NN">` in the deck
to PNG at native 1080×1920, saved at 2× (2160×3840), and is meant to be re-run
after editing the HTML to refresh the exported PNGs.

```bash
node tools/render_posters.mjs                       # default AJS Xiaohongshu deck
node tools/render_posters.mjs <deck.html>           # custom HTML, PNGs next to it
node tools/render_posters.mjs <deck.html> <outDir>  # custom output dir
```

Requires a global Playwright (`npm i -g playwright`); the script resolves it from
the global module root automatically. If no Chromium is cached, run
`npx playwright install chromium` once.

## Python Syntax Check

Run this after editing any script in this directory:

```bash
python3 -m py_compile tools/*.py
```
