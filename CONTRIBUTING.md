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

## Minimum acceptance bar for a new pack（新 pack 最小验收线）

A new depth pack is mergeable only when ALL of the following hold. This is the
same bar the repo's own maintenance waves are held to:

1. **Structure** — 8–20 skills (12 is the house norm; go past 14 only for a
   deliberately deepened flagship), each a `skills/<name>/SKILL.md` with `name` +
   `description` frontmatter; a pack `README.md` and `README.zh-CN.md`; a
   `.claude-plugin/plugin.json`; registration in the root
   `.claude-plugin/marketplace.json`.
2. **Facts discipline** — `resources/official-source-map.md` with ≥1 official
   URL and a visible check date; every volatile fact (fees, limits, dates,
   acceptance) traces to it or is marked `待核实`/`UNVERIFIED`.
3. **Substance** — every skill body carries real venue-specific guidance
   (target ≈600 substance units/skill for depth packs); descriptions ≥200 chars
   with a "Use when"/使用时机 trigger that names the venue (Latin-script form
   included for Chinese venues).
4. **Not a clone** — `python3 tools/clone_audit.py --threshold 0.75
   --fail-threshold 0.90` reports no pairs involving the pack. A sibling-journal
   reader must not be able to swap the venue name and keep the text.
5. **Empirical packs** — vendor the shared `code/` kit or explain in
   `resources/README.md` why no code applies, and link the shared
   `execution-with-mcp.md` playbook from the analysis-facing skills.
6. **Counters** — bump `tools/audit_repo.py` tripwires and both README count
   blocks in the same commit; `python3 tools/run_checks.py --skip-reports`
   passes end-to-end.
7. **Score floor** — the pack scores ≥90 on
   `python3 tools/quality_scorecard.py` (current repo floor is 94, the formula
   ceiling; aim there).

## How to reuse a pack bundle（如何复用一个 pack bundle）

Everything here is MIT-licensed: you may copy any pack's layout for your own
target venue, in your own repo or as a contribution back. The rules below keep
a replica from becoming the one failure mode this repo audits hardest against —
the find-replace clone.

1. **Reuse structure, not prose.** Copy the file layout (12-skill lifecycle,
   `.claude-plugin/` metadata, bilingual READMEs, `resources/` roles) freely.
   The skill *bodies* must be rewritten around the target venue's real
   workflow; swapping the journal name in existing text is not a replica, it is
   a clone and will be rejected by `tools/clone_audit.py` (0.75 review
   threshold, 0.90 hard fail).
2. **Re-source every volatile fact.** Fees, word/page limits, editor names,
   platforms, policies: each one must trace to the *target* venue's official
   page (URL + access date in `resources/official-source-map.md`) or be marked
   `待核实`. Facts inherited from the source pack are wrong by default.
3. **Contribute back or fork out.** A replica aimed at this repo goes through
   the "Minimum acceptance bar for a new pack" above, counters and all. A
   replica for your own repo has no obligations beyond the MIT license — but
   opening a `bundle-replication-request` issue first gets you a maintainer
   sanity-check on venue fit and a pointer to the closest existing template.
4. **Pick the closest sibling as your base.** Same discipline, same review
   platform, same publication form (conference vs journal, theory vs
   empirical) — the fewer facts you must replace, the fewer you will miss.
