# Maintenance Tools

These scripts are dependency-free Python tools for repository maintenance. They
are designed to run on a fresh clone after first-level submodules are populated.

## Hard Gates

| Tool | Purpose | Typical command |
|------|---------|-----------------|
| [`run_checks.py`](run_checks.py) | Runs the standard local hard gates and, by default, the report-only audits. CI uses `--skip-reports` so warnings stay advisory. | `python3 tools/run_checks.py` |
| [`audit_repo.py`](audit_repo.py) | Validates repository invariants: skill counts, pack counts, root journal entries, plugin metadata, required source maps, frontmatter, local Markdown links, and submodule sync policy. | `python3 tools/audit_repo.py` |
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

### Updating the inventory tripwires

`audit_repo.py` hard-codes the expected skill/pack/root-entry counts so accidental
bulk deletions fail CI. When you intentionally add or remove packs, refresh the
three `EXPECTED_*` constants (and the README badges) in the same commit:

```bash
python3 tools/audit_repo.py --counts   # prints the live numbers to copy in
```

## Python Syntax Check

Run this after editing any script in this directory:

```bash
python3 -m py_compile tools/*.py
```
