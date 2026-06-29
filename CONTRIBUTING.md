# Contributing

Awesome Journal Skills is maintained as a multi-pack index. Keep changes narrow,
source-backed, and easy to review.

## Before editing

1. Run `git status --short --branch` and inspect `.maintenance/CLAIMS.md` for
   active lanes.
2. If another agent or contributor is editing a pack, do not touch that pack in
   the same change.
3. Keep third-party packs as external links. Do not vendor upstream repositories
   into this index unless the repository ownership model changes explicitly.

## Safe change boundaries

- Root navigation and metadata: `README.md`, `README.en.md`,
  `.claude-plugin/*.json`, `.github/`, and `tools/`.
- Journal content: `*-Skills/skills/**`, `resources/**`, templates, and pack
  README files.
- External third-party listings: README links to AER, Nature-family packs,
  `claude-scholar`, and `codex-claude-academic-skills`.

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
