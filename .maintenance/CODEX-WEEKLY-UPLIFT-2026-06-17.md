# Codex Weekly Uplift Log — 2026-06-17

## Scope

- No new journals, packs, root cards, or submodules were added.
- Existing dirty files from the parallel lane were treated as out of scope unless already part of the root-card provenance pass.
- Improvements focused on measurable quality: root-card provenance, low-tail skill depth, and acceptance-ready validation evidence.

## Work completed

1. Root journal cards
   - Added visible `Checked` / `核验日期` rows to root cards that lacked provenance dates.
   - Added verified external source rows for the remaining root cards where a reliable, reachable source was available.
   - Left cards without a reliable public URL as transparent advisory warnings instead of adding questionable sources.

2. Low-tail skill depth
   - Strengthened ISR, JCR, and Journal of Finance and Economics skills with revision ledgers, claim-to-evidence ledgers, new-study economy checks, and heterogeneity/reporting safeguards.
   - Strengthened POQ, SPQ, and JMR skills with survey-error audit tables, package synchronization ledgers, mechanism ladders, cross-tradition response matrices, and result-to-claim ledgers.
   - Strengthened JoE, Organization Science, and CAR skills with editor-screen packets, assumption audits, SE-centered revision ledgers, cross-level paragraph tests, accounting terminology ledgers, and reproducibility change ledgers.

## Current metrics snapshot

- Repository inventory remains: 1984 skills, 122 first-party packs, 200 root journal entries.
- `tools/root_entry_audit.py`: 200 enriched root cards, 0 machine-only cards, 4 advisory no-URL warnings.
- `tools/quality_scorecard.py --top 30 --show-skills`: mean 93.1/100, min 90.0, p10 90.6, median 94.0, below 86/88/90 = 0/0/0.

## Remaining advisory items

- Four root cards still lack a reliable public URL: `Gaige`, `Hongguan-Jingji-Yanjiu`, `Jingji-Wenti`, and `Xiandai-Jinrong-Yanjiu`.
- Natural-science low-tail packs and CS conference breadth near-clone pairs are intentionally left to the active parallel lanes recorded in `.maintenance/CLAIMS.md`.

## Final verification targets

- `python3 tools/audit_repo.py --counts`
- `python3 tools/root_entry_audit.py`
- `python3 tools/quality_scorecard.py --top 30 --show-skills`
- `python3 tools/run_checks.py --skip-reports`
- `git diff --check`
