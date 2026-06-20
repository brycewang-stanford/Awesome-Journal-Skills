# Contributing

Awesome Journal Skills is maintained as a multi-pack index. Keep changes narrow,
source-backed, and easy to review.

## Before editing

1. Run `git status --short --branch` and inspect `.maintenance/CLAIMS.md` for
   active lanes.
2. If another agent or contributor is editing a pack, do not touch that pack in
   the same change.
3. Treat submodules as read-only from this repository unless the change is only
   a deliberate submodule pointer bump.

## Safe change boundaries

- Root navigation and metadata: `README.md`, `README.en.md`,
  `.claude-plugin/*.json`, `.github/`, and `tools/`.
- Journal content: `*-Skills/skills/**`, `resources/**`, templates, and pack
  README files.
- Imported upstream packs: `AER-skills/`, `nature-skills/`,
  `nature-paper-skills/`, `claude-scholar/`, and
  `codex-claude-academic-skills/`.

Avoid mixing these boundaries in one PR unless the connection is direct and
documented.

## Required checks

Run the standard local check set before opening a PR:

```bash
python3 tools/run_checks.py
```

For journal-content rewrites, run the clone audit on the affected pack or on
all first-party skills:

```bash
python3 tools/clone_audit.py --bundle Chinese-SocialScience-Journal-Skills --group-all --threshold 0.70
python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90
python3 tools/root_entry_audit.py
```

For edits touching Python tooling, also run:

```bash
python3 -m py_compile tools/*.py
```

Always run:

```bash
git diff --check
```

## Count-disciplined quality uplift lane

When working on the 2026-06 monthly quality program, improve existing
first-party packs before proposing inventory growth. Keep the canonical
inventory stable unless an explicit expansion lane is approved:

```bash
python3 tools/audit_repo.py --counts
python3 tools/quality_scorecard.py --top 40 --show-skills
python3 tools/root_entry_audit.py
python3 tools/source_map_audit.py
python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 40
python3 tools/run_checks.py --skip-reports
git diff --check
```

Record batch evidence in `.maintenance/MONTHLY-UPLIFT-2026-06-20.md` and
`.maintenance/PROGRESS.md`. A good batch raises the scorecard floor, closes
root/source-map warnings with current sources, or differentiates clone-audit
pairs with concrete venue routing; a bad batch merely pads prose, hides
warnings, weakens thresholds, or adds low-quality counts.

## Journal-content quality bar

- Use official journal pages first. If a fact cannot be verified, mark it
  `UNVERIFIED` / `待核实` rather than guessing.
- Do not create find-replace clones. A sibling-journal reader should not be able
  to swap the venue name and have the skill still read correctly.
- Keep skill folder names and frontmatter keys stable unless there is a
  migration plan.
- When adding or removing a `SKILL.md`, update the pack marketplace manifest and
  root README count methodology in the same change.
- If adding a root-level journal entry folder, include the
  `AJS-ROOT-JOURNAL-ENTRY` marker, canonical skill link, skill name, and bundle
  link. The repository audit verifies that this navigation stub points to the
  real installable `SKILL.md` inside its bundle.
- For root-card enrichment batches, run `python3 tools/root_entry_audit.py`.
  It reports enriched cards that need external URLs or visible check dates; the
  hard invariant check remains in `tools/audit_repo.py`.
- Chinese depth packs must keep `resources/official-source-map.md` so volatile
  submission facts are tied to official sources or explicit `待核实` notes. The
  audit expects each source map to include at least one URL and a visible access
  or check date.
- For source-map cleanup, use `python3 tools/source_map_audit.py` to find files
  with missing URLs, missing check dates, or heavy unresolved-flag loads. The
  tool is report-only unless run with `--strict`.

## Submodules

Initialize only first-level submodules:

```bash
git submodule update --init
```

Do not use recursive initialization unless a specific upstream package asks for
it. Some imported upstreams contain nested submodule metadata that is irrelevant
to this index.
