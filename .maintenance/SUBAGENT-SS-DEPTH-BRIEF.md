# Subagent Build Brief — NEW social-science depth pack (flagship quality)

Build ONE complete, NEW 12-skill journal depth pack inside /Users/brycewang/Awesome-Journal-Skills.
Your task message gives IDENTITY (DIR, PREFIX, PLUGIN, TITLE), a SKILL-SET VARIANT name, a CODE-KIT
flag, a JOURNAL FACT SEED, and a COVER spec. This file is the contract. The bar is FLAGSHIP prose
(the quality of `Quantitative-Economics-Skills` and `American-Political-Science-Review-Skills`) — NOT
a fill-in-the-blank template.

## Read first
- `assets/depth-pack-spec.md` (file list, JSON skeletons, README skeleton).
- `American-Political-Science-Review-Skills/` and `American-Sociological-Review-Skills/` — existing
  social-science depth packs to imitate for tone/altitude. Also `Quantitative-Economics-Skills/` for
  the resource layer + output-contract style.

## Hard rules
- Create everything ONLY under your new `DIR`. Do NOT touch root READMEs, `tools/`, `.maintenance/`,
  other packs, or breadth bundles. Never `git init`, never commit.
- Content must be genuinely journal-specific (real scope, editor/owner, portal, review model, length/
  format, house style, data/transparency policy, exemplar awareness, real anti-patterns). No filler,
  no TODO/lorem, no leftover `{p}`/`<X>`.

## Files to create (exact — same as the depth-pack spec)
```
DIR/.gitignore  DIR/LICENSE  DIR/README.md  DIR/README.zh-CN.md
DIR/.claude-plugin/plugin.json  DIR/.claude-plugin/marketplace.json
DIR/assets/cover.svg
DIR/skills/<PREFIX>-<slug>/SKILL.md            # the 12 from your SKILL-SET VARIANT, in order
DIR/skills/<PREFIX>-submission/templates/checklist.md
DIR/resources/external_tools.md
DIR/resources/official-source-map.md
DIR/resources/README.md
DIR/resources/worked-examples/01-introduction.md
DIR/resources/exemplars/library.md
DIR/resources/code/                            # ONLY if CODE-KIT = WITH (see below)
```

## SKILL-SET VARIANTS (use the one named in your task; replace <p> with PREFIX)
- **EMPIRICAL** (quant/mixed social science): `<p>-workflow, <p>-topic-selection, <p>-literature-positioning,
  <p>-theory-building, <p>-research-design, <p>-data-analysis, <p>-tables-figures, <p>-writing-style,
  <p>-transparency-and-data, <p>-review-process, <p>-submission, <p>-rebuttal`
- **PSYCHOLOGY** (experimental psych): `<p>-workflow, <p>-topic-selection, <p>-theory-and-hypotheses,
  <p>-literature-positioning, <p>-study-design, <p>-data-analysis, <p>-tables-figures, <p>-writing-style,
  <p>-open-science-and-transparency, <p>-review-process, <p>-submission, <p>-rebuttal`
- **THEORY** (no data): `<p>-workflow, <p>-topic-selection, <p>-theory-construction, <p>-literature-positioning,
  <p>-argument-development, <p>-boundary-conditions, <p>-conceptual-exhibits, <p>-writing-style,
  <p>-contribution-framing, <p>-review-process, <p>-submission, <p>-rebuttal`
- **METHODS**: `<p>-workflow, <p>-topic-selection, <p>-method-contribution, <p>-literature-positioning,
  <p>-derivation-and-properties, <p>-simulation-studies, <p>-empirical-illustration, <p>-tables-figures,
  <p>-writing-style, <p>-software-and-reproducibility, <p>-submission, <p>-rebuttal`
- **REVIEW** (invited surveys): `<p>-workflow, <p>-topic-selection, <p>-proposal-and-commissioning,
  <p>-literature-synthesis, <p>-organizing-framework, <p>-comprehensiveness-and-balance, <p>-tables-figures,
  <p>-writing-style, <p>-transparency-and-reproducibility, <p>-editor-strategy, <p>-submission, <p>-revision`
- **LAW** (student-edited law reviews): `<p>-workflow, <p>-topic-selection, <p>-thesis-and-contribution,
  <p>-preemption-check, <p>-argument-structure, <p>-sources-and-bluebook, <p>-writing-style,
  <p>-placement-strategy, <p>-student-editor-review, <p>-submission, <p>-revision-and-editing,
  <p>-footnotes-and-cite-check`

## SKILL.md format (CRITICAL — audit-enforced)
Frontmatter has EXACTLY two keys; `name` == folder; no other keys:
```
---
name: <PREFIX>-<slug>
description: Use when <precise trigger> for a <TITLE> manuscript. <what it does / does NOT do>
---
```
Body ~90–125 lines (match the reference packs' density; do not pad): `# Title (<PREFIX>-<slug>)`,
`## When to trigger`, a real journal-specific core section (priority list / decision table / branches
with genuine content), `## Checklist`, `## Anti-patterns` (what THIS journal's reviewers punish),
`## Output format` (fenced handoff naming the next skill). Router `<PREFIX>-workflow` = overview +
routing table + default order + anti-patterns (mirror qe-workflow). Make every Output block hand off
to a REAL next skill (no self-loops).

## README / manifests / resources
- README.md (English) + README.zh-CN.md (Chinese): title, `<img src="assets/cover.svg" width="200">`,
  positioning paragraph, "Official basis checked 2026-06" line, 12-row Skills table, Quick Start,
  Resources list, a short "Differences vs. sibling journals" table, License. MUST NOT contain
  `AJS-ROOT-JOURNAL-ENTRY`.
- plugin.json + marketplace.json per spec; valid JSON; name=PLUGIN, version 0.1.0, license MIT
  consistent; one plugin entry; `skills[]` = the 12 dirs in order.
- resources/README.md index; worked-examples/01-introduction.md (FICTIONAL, clearly labelled, in this
  journal's house style); exemplars/library.md (REAL papers in THIS venue, web-verify where you can,
  OMIT/mark 待核实 if unsure, sibling-journal guard, access date 2026-06); official-source-map.md
  (official URLs + 2026-06 date + honest 待核实). external_tools.md (discipline data sources/software).
- LINK DEPTHS: from resources/README.md → `../../shared-resources/empirical-methods/...`; from
  resources/worked-examples/ and resources/exemplars/ → `../../../shared-resources/...`; skill links
  from worked-examples → `../../skills/<PREFIX>-<slug>/SKILL.md`.
- CODE-KIT = WITH: run `cp -R /Users/brycewang/Awesome-Journal-Skills/shared-resources/empirical-methods/code DIR/resources/code`
  and prepend a one-line HTML provenance comment to resources/code/README.md (vendored 2026-06 for <TITLE>).
  CODE-KIT = NO: do NOT create resources/code/ and do NOT link it; in resources/README.md reference the
  shared reviewer-objection-checklist / reporting-standards only as background (`../../shared-resources/...`).

## Honesty
Anchor on the seed; web-verify where you can (ToolSearch "select:WebSearch,WebFetch"). Mark volatile
specifics (current editor, fee, exact word limit, portal) `(检索于 2026-06；以官网为准)` or 待核实.
NEVER fabricate editors, fees, or citations.

## Self-check (report)
1. `ls DIR/skills/` = EXACTLY 12 dirs, each SKILL.md, names == the variant's slugs in order.
2. Both JSONs valid; marketplace `skills[]` == the 12 dirs in order; name/version/license consistent.
3. Every frontmatter exactly name+description, name==folder; body ~90–125 lines; descriptions start "Use when".
4. `grep -rl AJS-ROOT-JOURNAL-ENTRY DIR/` → nothing; no TODO/lorem.
5. resources present (code/ only if WITH); relative-link depths correct; cover.svg valid XML.
Return: file tree, per-SKILL line counts, # exemplars web-verified vs 待核实, facts you could not verify.
</content>
