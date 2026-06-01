# Stub landing-card enrichment lane (Agent — root journal-entry browsing layer)

Separate, race-free claim file (do **not** edit the shared CLAIMS.md / PROGRESS.md while Codex
holds them uncommitted). This lane is **file-disjoint** from every other active agent:

| Agent | Owns (do not touch) |
|-------|---------------------|
| Codex | `tools/`, `.github/`, root `README.md` / `README.zh-CN.md`, `CONTRIBUTING.md`, `.maintenance/{CLAIMS,PROGRESS}.md`, + new `resources/official-source-map.md` for 7 Chinese depth packs |
| Claude content-verification | `*-Skills/skills/**/SKILL.md` + `*-Skills/resources/*.md` (the `UNVERIFIED`/`待核实` flags) |
| Agent B | natural-science `SKILL.md` clone fixes (Science/PNAS/Cell/…) |
| **This lane** | **only** the root per-journal stub files `<Journal>/README.md` (the `AJS-ROOT-JOURNAL-ENTRY` cards) |

## Why this lane (decision record)
- Assigned "verify the 84 flags" turned out to **collide** with the content-verification agent's
  active lane AND be **unexecutable** here: `econometricsociety.org` → 403, CN official sites
  JS-rendered/blocked; only secondary aggregators return, which the methodology forbids relying on.
- The 200 root stubs are a 10-line pointer each — the weakest surface of the repo's venue-first
  browsing pitch — and **no agent owns them**.

## Invariants (must not break the audit)
`tools/audit_repo.py` requires every stub to keep, verbatim:
- the `<!-- AJS-ROOT-JOURNAL-ENTRY -->` marker,
- a `- Canonical skill: [..](..)` line, a `- Skill name: `..`` line, a `- Bundle: [..](..)` line,
- and **no** `SKILL.md` in the folder.
Enrichment only **adds** prose/metadata around those lines. Run `python3 tools/audit_repo.py`
after each batch (expect: 844 skills / 44 packs / 200 root entries).

## Quality bar (same spirit as METHODOLOGY.md)
Card facts (publisher, ISSN, founded, field, indexing/tier, official URL, one-line scope) must be
source-backed. Where a fact cannot be confirmed from an authoritative source, omit it rather than
guess. Never invent ISSNs, founding years, or publishers.

## Process
1. `git status <Journal>/` before editing; skip if dirty.
2. Enrich the card; keep the 3 machine lines verbatim.
3. Leave the **pilot** uncommitted for the user's design 验收; after approval, commit per batch with
   targeted `git add <Journal>/README.md …` (never `git add -A`); do not push.

## Card template (user-approved 2026-05-31)
Marker → `# Title` → right-aligned cover `<a><img width=150 align=right></a>` linking to the skill →
one-line scope blockquote → `| At a glance |` 2-col table (Field, Publisher, Founded, ISSN,
Frequency, Standing, Official) → `**▶ Use the skill — `slug`:** …` CTA → bundle subline →
`---` → **verbatim** original machine-line block (Canonical skill / Skill name / Bundle) + no-SKILL note.

Rules: facts source-backed; **omit a row** if not verifiable (never guess ISSN/founded/publisher).
**Standing** row: include only verifiable indexing/tier (SSCI/SCIE/CSSCI/北大核心/FT50/ABS/AMI);
omit otherwise. EN stubs in English, CN stubs in Chinese. Cover = `assets/covers/<skill-name>.png`
when it exists, else omit the image.

## Sourcing rule for the Chinese half (CN official sites are 403/JS-blocked)
For CN journals I cannot reach the primary site, so a fact (主办单位/ISSN/CN刊号/创刊/CSSCI) is
included only if **corroborated across ≥2 independent secondary sources** (e.g. 百度百科 + CNKI/
期刊数据库 + 主办机构页). Anything not corroborated is **omitted** (row dropped), never guessed.
"收录/地位" lists only CSSCI / 北大核心 / AMI / CSCD where corroborated.

## Log
- 2026-05-31 — batch 0 (pilot, user-approved): Journal-of-Finance, Quarterly-Journal-of-Economics,
  Guanli-Shijie (《管理世界》), Jingji-Yanjiu (《经济研究》). Audit green. Committed `2e2690d`.
- 2026-05-31 — batch 1: 24 EN flagship cards (econ/finance/mgmt). Committed `b8f77c7`. Audit green.
- 2026-05-31 — batch 2: 36 EN field cards (econ/econometrics/applied). Committed `937d4b4`. Audit green.
- 2026-05-31 — batch 3: 38 EN cards (finance/accounting/mgmt/mktg/IS/OM). Committed `689e68a`. Audit green.
- **English half COMPLETE: 100/100 EN + 2 CN = 102/200.** Facts researched by parallel sub-agents,
  source-cited; I generated + wrote all cards (machine-line footer preserved verbatim).
- NEXT: Chinese half — 98 CN stub cards, smaller batches, sourcing rule above.
