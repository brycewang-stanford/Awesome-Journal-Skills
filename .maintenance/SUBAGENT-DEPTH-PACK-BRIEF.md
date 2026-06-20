# Subagent Build Brief — one 12-skill journal depth pack (generic core)

You build ONE complete journal "depth pack" inside /Users/brycewang/Awesome-Journal-Skills.
Your task message gives you the per-pack IDENTITY (DIR, PREFIX, PLUGIN, TITLE, FAMILY), a
JOURNAL FACT SEED, the SKILL SET (the 12 skill slugs), a COVER spec, and any ADAPTATION notes.
This file is the generic contract. Follow it to the letter.

## Hard rules
- Work ONLY inside the new directory `DIR` you create. Do NOT touch root README files, `tools/`,
  other packs, `.maintenance/`, or anything outside `DIR`. Never run `git init`, never create a
  nested `.git`, never commit.
- Read FIRST: `assets/depth-pack-spec.md` (exact authoring contract) and the reference pack
  `Quantitative-Economics-Skills/` (skills/qe-workflow, skills/qe-submission,
  skills/qe-identification-strategy, README.md, both .claude-plugin/*.json, resources/README.md,
  resources/official-source-map.md, resources/external_tools.md,
  resources/worked-examples/01-introduction.md, resources/exemplars/library.md, assets/cover.svg).
- Content must be genuinely journal-specific. No generic filler, no TODO/lorem/`{prefix}` leftovers.

## Files to create (exact)
```
DIR/.gitignore                         # copy spec §3 verbatim
DIR/LICENSE                            # MIT, "Copyright (c) 2026 Bryce Wang" (body of Quantitative-Economics-Skills/LICENSE)
DIR/README.md                          # English; see README section
DIR/README.zh-CN.md                    # Simplified Chinese mirror
DIR/.claude-plugin/plugin.json         # spec §7
DIR/.claude-plugin/marketplace.json    # spec §8
DIR/assets/cover.svg                   # valid XML; adapt the COVER template in your task (text/colors only)
DIR/skills/<PREFIX>-<slug>/SKILL.md    # 12 of them, slugs from your task, workflow order
DIR/skills/<PREFIX>-submission/templates/checklist.md   # 8-section pre-submission self-check, linked from the submission skill
DIR/resources/external_tools.md
DIR/resources/official-source-map.md
DIR/resources/README.md
DIR/resources/worked-examples/01-introduction.md
DIR/resources/exemplars/library.md
DIR/resources/code/                    # vendored — see Resource layer (SKIP only if your task says "NO CODE KIT")
```

## SKILL.md format (CRITICAL — audit-enforced; a violation fails CI)
Every SKILL.md begins with YAML frontmatter containing EXACTLY two keys and nothing else:
```
---
name: <PREFIX>-<slug>
description: Use when <precise trigger condition> for a <TITLE> manuscript. <one sentence on what it does and does NOT do>
---
```
- `name` MUST equal the folder name. NO other frontmatter keys (no version/tags/author/etc.) — extra keys FAIL the audit.
- Body 70–130 lines: `# <Human title> (<PREFIX>-<slug>)`, `## When to trigger` (bullet symptoms),
  a core section (priority list / decision table specific to THIS stage AND THIS journal),
  `## Checklist` (concrete checkable items), `## Anti-patterns` (failure modes referees at THIS
  journal punish), `## Output format` (a fenced block: a structured handoff naming the next skill).
- The router `<PREFIX>-workflow` instead contains: overview, trigger timing, a routing table
  (symptom → next skill), the default order, and anti-patterns — mirror `qe-workflow`.

## README (both languages)
Mirror the spec §6 / the QE README, kept tight and real: title; centered cover
`<img src="assets/cover.svg" alt="..." width="200">`; one-paragraph positioning; an
"Official basis checked 2026-06 (see resources/official-source-map.md)" line; a 12-row Skills
table (skill → one-line purpose); a Quick Start (plugin install + manual use); a Resources list;
a short "Differences vs. sibling journals" table; License. English in README.md, Simplified
Chinese in README.zh-CN.md. The pack README MUST NOT contain the string `AJS-ROOT-JOURNAL-ENTRY`.

## JSON manifests
Both must be valid JSON (no trailing commas). plugin.json and marketplace.json share name=PLUGIN,
version `0.1.0`, license `MIT`. marketplace.json has exactly ONE plugin entry; its `skills[]` lists
all 12 skill directories as `skills/<PREFIX>-<slug>` in workflow order, set-equal to the actual dirs.
Keywords: 8–12 journal/discipline terms in plugin.json, ~7 in the marketplace entry.

## Resource layer
- Unless your task says "NO CODE KIT": vendor the shared code kit (copies REAL code — zero hallucination):
  `cp -R /Users/brycewang/Awesome-Journal-Skills/shared-resources/empirical-methods/code DIR/resources/code`
  then prepend ONE HTML comment line to `DIR/resources/code/README.md` noting it was vendored from
  `shared-resources/empirical-methods/code` on 2026-06 for <TITLE>. Change no Stata/Python command.
- `resources/README.md`: an index table modeled on the QE one. LINK DEPTHS (audit checks broken links):
  from `resources/README.md` the shared hub is `../../shared-resources/empirical-methods/reviewer-objection-checklist.md`
  and `../../shared-resources/empirical-methods/reporting-standards.md`.
- `resources/worked-examples/01-introduction.md`: a FICTIONAL, clearly-labelled before→after
  introduction in THIS journal's house style (derive only from your own pack's skills; invent no
  real-paper facts). Skill links use `../../skills/<PREFIX>-<slug>/SKILL.md`; shared-hub links use
  `../../../shared-resources/...`.
- `resources/exemplars/library.md`: REAL papers actually published in THIS venue, by method × topic,
  with a header access date (2026-06) and a sibling-journal guard (do NOT attribute sibling-journal
  papers to this venue). You MAY web-verify (load tools via ToolSearch "select:WebSearch,WebFetch").
  If you cannot verify a paper, OMIT it or mark the row 待核实 — NEVER fabricate a citation. 6 verified
  beats 15 guessed. Shared-hub links use `../../../shared-resources/...`.
- `resources/official-source-map.md`: official URLs behind each venue fact, with access date 2026-06
  and honest 待核实 markers where a page was not directly verifiable. Must contain ≥1 https:// URL
  and a 2026-06 date.

## Honesty (repo-wide norm)
Anchor on your fact seed but VERIFY where you can. Mark volatile specifics (current editor names,
exact fees, exact word/length limits, portal) `(检索于 2026-06；以官网为准)` or 待核实. NEVER invent
editor names, fees, or citations. If the seed conflicts with an official page you can read, follow
the official page and note the correction in your report.

## Self-check before finishing (report all)
1. `ls DIR/skills/` = EXACTLY 12 dirs, each with SKILL.md, names == the slugs in workflow order.
2. Both `.claude-plugin/*.json` parse as valid JSON; marketplace `skills[]` == the 12 dirs in order.
3. Every SKILL.md frontmatter has ONLY name+description and name==folder; body 70–130 lines.
4. `grep -rl AJS-ROOT-JOURNAL-ENTRY DIR/` returns nothing.
5. resources present; (code/ populated unless NO CODE KIT); relative-link depths correct; cover.svg valid XML; no TODO/placeholder.
Return a concise report: file tree, per-SKILL line counts, # exemplars web-verified vs 待核实, and any facts you could not verify.
</content>
