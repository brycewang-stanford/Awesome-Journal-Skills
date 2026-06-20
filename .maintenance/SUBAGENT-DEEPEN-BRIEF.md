# Subagent Deepen Brief — rewrite a templated depth pack to flagship prose

Your task message gives ONE pack DIR (and its TITLE). The pack already exists and PASSES the
structural audit, but its 12 `skills/*/SKILL.md` bodies are **templated/generic** (a "Core decision
map" table, "Evidence block N", "<X> fit notes", "Stage-specific moves" skeleton). Your job is to
**rewrite all 12 SKILL.md bodies into genuine, venue-specific, craft-rich flagship prose** — the
quality of the reference packs — WITHOUT changing structure, manifests, or the resource layer.

## Read first (the quality bar)
- `Quantitative-Economics-Skills/skills/qe-workflow/SKILL.md`, `.../qe-submission/SKILL.md`,
  `.../qe-identification-strategy/SKILL.md` — the gold standard for tone/specificity/output contracts.
- `AEJ-Applied-Economics-Skills/skills/` — a hand-built econ pack at the target quality (94/100).
- For a management-family pack also skim `Academy-of-Management-Journal-Skills/skills/` for theory-
  development / methods / review-process craft.
- The pack you are deepening: read ALL 12 of its current `skills/*/SKILL.md` to learn the exact
  folder names, the current `description:`, and what each skill is supposed to cover.

## Hard rules (do NOT break the passing audit)
- Edit ONLY `DIR/skills/*/SKILL.md`. Do NOT touch manifests (`.claude-plugin/*`), READMEs, LICENSE,
  `assets/`, or `resources/` (those already pass). Do NOT add/remove/rename skill folders. Never
  `git init`, never commit.
- Keep YAML frontmatter to EXACTLY two keys: `name` (UNCHANGED — must equal the folder name) and
  `description`. You MAY sharpen the `description` (keep the shape: "Use when <trigger> for a <TITLE>
  manuscript. <what it does / does not do>") but keep it one logical line and keep only those 2 keys.
- Each rewritten body 90–130 lines. Remove EVERY template tell: no "Core decision map", no "Evidence
  block N", no "<X> fit notes", no "Stage-specific moves", no "is central | Make the … explicit" rows,
  no "Signature vocabulary"/"Official URLs currently used by the pack" boilerplate.

## What each rewritten SKILL.md must contain (like the reference)
1. `# <Human Title> (<prefix>-<slug>)`
2. `## When to trigger` — 4–6 concrete symptoms specific to THIS stage and THIS journal.
3. A **core section with real content** (not a fill-in table): e.g. a priority list, a branch-by-archetype
   decision table with genuine guidance, a worked sequence, or a comparison — written for THIS journal's
   actual scope, methods, and house style. This is where the craft lives; make it genuinely useful.
4. `## Checklist` — concrete, checkable items a referee at THIS journal would care about.
5. `## Anti-patterns` — real failure modes THIS journal's referees punish (named, specific).
6. `## Output format` — a fenced block: a structured handoff that names the next skill in the pack.
   The router (`<prefix>-workflow`) instead carries: overview, when-to-trigger, a routing table
   (symptom → next skill), default order, anti-patterns, and ideally a short "routing by archetype" —
   mirror `qe-workflow`.

## Venue specificity (this is the point of "做扎实")
Anchor on real, verifiable facts about THIS journal: publisher/owner, submission portal, review model
(single/double-blind), length/abstract limits, house citation style, data & code / replication policy,
distinctive process quirks, the sibling journals it is confused with and how it differs, and the kinds
of contributions it rewards vs. desk-rejects. You MAY web-verify (load tools via ToolSearch
"select:WebSearch,WebFetch"). Mark volatile specifics (current editor, exact fee, exact word limit)
`(检索于 2026-06；以官网为准)` or 待核实. NEVER fabricate editors, fees, or citations. If the existing
`resources/official-source-map.md` has facts, reuse them and stay consistent.

## Differentiation (avoid clones)
Each skill must be distinct from its siblings AND from other packs. Do not reuse a generic paragraph
across skills. The pack as a whole must read as written by someone who knows THIS journal.

## Self-check before finishing (report)
1. All 12 SKILL.md still present; frontmatter still exactly name+description; name == folder; each
   description still starts "Use when" and names the journal.
2. `grep -lE "Core decision map|Evidence block|fit notes|Stage-specific moves|Signature vocabulary" DIR/skills` → NOTHING.
3. Each body 90–130 lines; no TODO/lorem/placeholder.
4. You did NOT touch manifests/READMEs/resources/assets/LICENSE.
Return: per-SKILL line counts, a 1-line note on the most journal-specific fact you encoded per skill,
and any facts you marked 待核实.
