# Codex Monthly Uplift Plan — 2026-06-20 to 2026-07-20

## Objective

Raise Awesome Journal Skills one clear quality tier over one month by improving
the current repository rather than inflating counts. This pass is count
disciplined: no new journals, packs, root cards, or submodules unless the user
explicitly opens a separate expansion lane.

## Baseline snapshot

Captured on 2026-06-20 from a clean `main...origin/main` checkout.

| Check | Current result |
|---|---:|
| `tools/audit_repo.py --counts` | 2665 skills / 171 packs / 200 root entries |
| `tools/quality_scorecard.py --top 40 --show-skills` | mean 92.6, min 86.0, below 86/88/90 = 0/5/5 |
| Low-tail packs below 90 | Agriculture-Environment, Chinese Sport Science, Clinical Medicine, Engineering Technology, English Humanities |
| `tools/root_entry_audit.py` | 200 enriched cards, 4 warnings |
| `tools/source_map_audit.py` | 156 source maps, 0 warnings |
| Highest unresolved source maps | Journal of Banking and Finance, Journal of Economic Theory, The Economic Journal, Journal of Econometrics, Journal of Financial Intermediation |
| `tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 40` | no fail-threshold hits; top risks are Science/PNAS rebuttal and CS conference breadth pairs around 0.799 |

## Work worth doing

1. **Raise the low-tail breadth floor.** The five breadth packs at 86.0 are
   the main visible quality debt. They need better router guidance, selection
   patterns, source-map discipline, and domain-specific decision tables, not
   generic prose.
2. **Close root-card provenance warnings.** Four enriched Chinese root cards
   still lack external URLs. Fix only with reliable public sources; otherwise
   keep the warning honest.
3. **Reduce unresolved source-map debt.** The source-map audit has no structural
   warnings, but a few packs still carry many `UNVERIFIED` / `待核实` markers.
   The month should turn reachable official facts into checked entries and
   leave blocked facts explicitly labeled.
4. **Triage high-similarity pairs.** CS conference breadth profiles and the
   Science/PNAS rebuttal pair should be either differentiated with concrete
   sibling-routing logic or documented as intentional shared scaffolding.
5. **Improve maintenance ergonomics.** Keep acceptance commands, score movement,
   and remaining risks visible so future agents do not rediscover the same
   baselines.

## Four-week execution plan

### Week 1 — Measurable cleanup

- Clear the four `root_entry_audit.py` URL warnings if reliable sources exist.
- Improve the five breadth packs below 90 with router-level decision tables,
  field-specific rejection risks, and official-source/use-case scaffolding.
- Re-run `quality_scorecard.py`, `root_entry_audit.py`, and
  `run_checks.py --skip-reports` after each small batch.

### Week 2 — Breadth-pack differentiation

- Use clone-audit output to identify the top CS conference near-clone clusters.
- Add sibling-selection or "do not route here" tables in shared resources
  where many profiles share a template.
- Differentiate only the highest-risk profile pairs first; keep broad template
  structure where it is useful and honest.

### Week 3 — Source-map reliability

- Take the top unresolved source maps in `source_map_audit.py`.
- Convert reachable official-source facts into checked rows with dates.
- Preserve `UNVERIFIED` / `待核实` for blocked, login-only, or unstable facts.
- Record any blocked-source pattern in the pack source map rather than guessing.

### Week 4 — Acceptance hardening

- Refresh score, clone, source-map, root-card, and external-link reports.
- Sync `CONTRIBUTING.md`, `tools/README.md`, and README snippets only if the
  commands or user-facing expectations have changed.
- Produce a final acceptance note with exact commands, score movement, and
  remaining advisory risks.

## Anti-cheat constraints

- Do not lower scorecard thresholds or clone-audit thresholds to make numbers
  look better.
- Do not delete checks, hide warnings, or reclassify weak packs as out of
  scope.
- Do not add low-quality packs or journals just to grow inventory counts.
- Do not invent current journal facts. Use official pages when reachable; mark
  blocked facts transparently.
- Do not touch submodules from this lane.

## Acceptance commands

```bash
python3 tools/audit_repo.py --counts
python3 tools/quality_scorecard.py --top 40 --show-skills
python3 tools/root_entry_audit.py
python3 tools/source_map_audit.py
python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 40
python3 tools/run_checks.py --skip-reports
git diff --check
git status --short --branch
```

## Work log

| Date | Batch | Status | Evidence |
|---|---|---|---|
| 2026-06-20 | Baseline and monthly plan | done | Baseline commands above |
| 2026-06-20 | Root-card provenance closure | done | `python3 tools/root_entry_audit.py` -> 200 enriched, 0 machine-only, 0 warnings |
| 2026-06-20 | Low-tail breadth resource entry points | done | `python3 tools/quality_scorecard.py --min-score 90 --top 8` -> min 90.0, below 86/88/90 = 0/0/0 |
| 2026-06-20 | Clone-audit triage batch | done | `python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90 --top 40` -> no fail-threshold hits; Science/PNAS pair no longer appears >=0.75 |
| 2026-06-20 | JoE source-map policy refresh | done | `python3 tools/source_map_audit.py` -> 0 warnings; JoE removed from highest unresolved source-map list after official 2026-06-20 portal/fee/review/data refresh |
| 2026-06-20 | JBF source-map policy refresh | done | `python3 tools/source_map_audit.py` -> 0 warnings; JBF removed from highest unresolved source-map list after official 2026-06-20 fee/review/editor/data/style refresh |
| 2026-06-20 | JET source-map policy refresh | done | `python3 tools/source_map_audit.py` -> 0 warnings; JET removed from highest unresolved source-map list after official 2026-06-20 editor/review/data/style refresh |
| 2026-06-20 | EJ source-map policy refresh | done | `python3 tools/source_map_audit.py` -> 0 warnings; EJ removed from highest unresolved source-map list after official 2026-06-20 submission-fee/editor/review/data refresh |
| 2026-06-20 | JFI source-map policy refresh | done | `python3 tools/source_map_audit.py` -> 0 warnings; JFI removed from highest unresolved source-map list after official 2026-06-20 fee/editor/review/data refresh |
| 2026-06-20 | User-facing maintenance docs | done | `CONTRIBUTING.md`, `tools/README.md`, `README.md`, and `README.en.md` now point maintainers to the count-disciplined monthly quality program and acceptance commands |
| 2026-06-20 | Post-batch acceptance gates | done | `run_checks.py --skip-reports` passed; counts remain 2665 / 171 / 200; scorecard min 90.0; root/source-map warnings 0; clone audit has no 0.90 fail-threshold hits |
