# Content-verification lane (Claude — social-science journal *content*)

Separate file (race-free) from the shared CLAIMS/PROGRESS, because a parallel **Codex**
agent is actively editing those + README + tools/ in the same working tree. My lane is the
**journal content** Codex explicitly excluded ("no journal-content rewrites"): verifying the
honest `UNVERIFIED` / `待核实` flags against official sources and fixing content-level defects
in `skills/*/SKILL.md` + `resources/*.md`. All edits left **uncommitted** for the user's 验收.

Coordination: file-disjoint from Codex (README.md, README.zh-CN.md, .maintenance/{CLAIMS,
PROGRESS,METHODOLOGY}.md, tools/, .github/, the 7 marketplace.json syncs + ER marketplace).
I independently re-verified Codex's deterministic work and it is **correct**: true distinct
skill count = **844** (854 physical SKILL.md − 10 `nature-skills` plugin-mirror dupes; AER 9 +
Nature 28 + toolkits 69 + in-repo 738), the 7 version syncs match their plugin.json, and the
`er-abstract`/`er-style` marketplace additions are real (12 dirs on disk). `tools/audit_repo.py`
passes: 844 skills / 44 packs / 200 root entries.

## Wave C-1 — verified-fact upgrades (official sources, 2026-05-31)

### SMJ — editor roster was stale (stated as fact, now superseded)
The pack asserted Co-Editors **"Agarwal, Benner, Gaba, Silverman"** in 5 places. The official
SMS masthead (strategicmanagement.net/smj) + Wiley now name **Benner, Ethiraj, Gaba** (+ a
4th not individually listed); Ethiraj replaced the earlier slate. Per the methodology ("never
invent editor names"), I removed the hard-coded volatile roster from the SKILL bodies (point to
the masthead) and recorded the verified-current named subset in the source map.
- `skills/smj-workflow/SKILL.md:12`, `skills/smj-review-process/SKILL.md:17`,
  `skills/smj-submission/SKILL.md:55`, `.claude-plugin/plugin.json:3`,
  `resources/official-source-map.md:18`.
- KEPT honest flags: ~7% acceptance + ~54-day first-decision (third-party only; official does
  not publish) — unchanged.

### AMR — resolved two UNVERIFIED flags
- **Submission fee → none.** AOM does not charge submission fees (verified aom.org). Was
  "UNVERIFIED — do not assume a fee." Fixed in `skills/amr-submission/SKILL.md:75`,
  `resources/official-source-map.md`, (template checklist still references it — see TODO).
- **Editor-in-Chief → Kris Byron** (Georgia State; AMR EIC since 2023, succeeding Sherry M. B.
  Thatcher). Corroborated by the AOM AMR editorial-team page + the Georgia State announcement.
  Fixed in `skills/amr-review-process/SKILL.md:22`, `resources/official-source-map.md:50`.
- KEPT honest flags: APA edition, exact word/abstract limits, acceptance rate, membership
  requirement (could not confirm from a primary source) — unchanged.

### Econometrica — kept honest flag (could not reach primary source)
`econometricsociety.org` returns 403 to the fetcher. Secondary sources indicate single-blind,
which matches the existing careful "single-anonymous convention — UNVERIFIED whether currently
required" wording. Per the "primary-source" bar, left the flag as-is. No edit.

## Wave C-2 — broken intra-repo cross-references (deterministic, all verified)

Found via a global skill-name resolver over every routing/改投 line (738 skill names). Real
breakages (target slug exists nowhere) — distinct from valid cross-pack pointers:
- `Chinese-SocialScience-Journal-Skills/skills/review-of-political-economy/SKILL.md:64`:
  `economic-and-social-systems-comparison` → **`comparative-economic-and-social-systems`** (the
  real sibling). Fixed.
- Wrong slug **`journal-of-management-sciences-in-china`** (the real breadth slug is
  `journal-of-management-sciences-china`, no "-in-"; confusion with the depth-pack dir name) in
  3 files — fixed: `Journal-of-Quantitative-and-Technological-Economics-Skills/skills/`
  `{jqte-fit-positioning:44, jqte-workflow:62}`, `Nankai-Business-Review-Skills/skills/nbr-workflow:59`.

Re-verified after edits: 0 broken routing slugs, 0 stale SMJ roster assertions, JSON valid,
audit tool still green.

## Open items (NOT yet done — surfaced for the user's call)

> Codex status note, 2026-05-31: several entries below were resolved after this
> handoff was written. The Chinese breadth-bundle de-clone is recorded in
> `.maintenance/ROUND2-RESULTS.md`; the seven missing Chinese depth-pack source maps
> were added in Codex Wave 10 and are now enforced by `tools/audit_repo.py`; the
> README parity and JF translation nits listed as items 5-6 are currently clean by
> local grep. Item 7 (AMR propagation) was resolved in Codex Wave 11. Remaining
> substantive content work is item 2 (natural-science clone cleanup, Agent B lane)
> and item 3 (MW/CRE/CFE generic role polishing).

1. **BIG: `Chinese-SocialScience-Journal-Skills` breadth bundle ≈80% clones.** ~82 of 103
   single-journal `SKILL.md` are name-swap clones (>0.90 normalized) with near-zero checkable
   facts (no word limit/fee/portal/editor/exemplar). This is the exact defect the methodology
   exists to kill, but this bundle was never de-cloned (historically "Agent B's lane"). De-
   cloning means adding *real* per-journal facts for ~82 Chinese journals — fact-by-fact web
   research, and prior waves noted many CN official sites are unreachable from the sandbox.
   Rewriting without verified facts would only produce *new* boilerplate (a methodology
   violation), so this needs a deliberate, possibly multi-day, source-driven effort.
2. **Science↔PNAS `rebuttal` clone twin** (0.93; ~11/84 lines differ) + `sci-statistics`↔
   `pnas-statistics` (0.86). Nature-science lane.
3. **ER-template generic roles** cloned into MW / CRE / CFE depth packs (rebuttal/style/
   submission/tables-figures). `mw-submission` gives generic boilerplate with no real 管理世界
   portal/publisher facts.
4. **7/14 Chinese depth packs lack `resources/official-source-map.md`** (have journal-profile.md
   or external_tools.md instead): China-Industrial-Economics, China-Rural-Economy,
   Chinese-Public-Administration, Journal-of-Management-World, Journal-of-Finance-and-Economics,
   JQTE, Accounting-Research.
5. **Pack README EN↔zh parity gaps (6):** NEJM/Science zh missing `## Related`; ER/JMW/
   China-Rural/Chinese-Public-Admin EN missing "What this repo does NOT do".
6. **Translation nit:** `Journal-of-Finance-Skills/README.zh-CN.md:1` renders "Journal of
   Finance" as "《金融学刊》" (wrong CN name).
7. **TODO (mine):** AMR fee/EIC flags also live in `amr-submission/templates/checklist.md` and
   `amr-writing-style/SKILL.md` — propagate the same upgrades for consistency.

## Handoff to Codex lane (root README, not mine to edit)
- Root README describes the CN bundle as "102 / ~100 / 100" in different places — normalize.
- Untracked case-variant submodule dirs (`AER-Skills/`, `Nature-Skills/`) are macOS case-fold
  artifacts of the lowercase submodules (same inode) — benign for Linux CI; local hygiene only.
