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

- Root navigation and metadata: `README.md`, `README.zh-CN.md`,
  `.claude-plugin/*.json`, `.github/`, and `tools/`.
- Journal content: `*-Skills/skills/**`, `resources/**`, templates, and pack
  README files.
- Imported upstream packs: `AER-skills/`, `nature-skills/`,
  `nature-paper-skills/`, `claude-scholar/`, and
  `codex-claude-academic-skills/`.

Avoid mixing these boundaries in one PR unless the connection is direct and
documented.

## Required checks

Run the repository audit before opening a PR:

```bash
python3 tools/audit_repo.py
```

For edits touching Python tooling, also run:

```bash
python3 -m py_compile tools/audit_repo.py
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

## Submodules

Initialize only first-level submodules:

```bash
git submodule update --init
```

Do not use recursive initialization unless a specific upstream package asks for
it. Some imported upstreams contain nested submodule metadata that is irrelevant
to this index.
