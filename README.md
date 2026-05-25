# Awesome Journal Skills

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

A curated index of **journal-specific agent skill packs** for social-science manuscript work — selecting topics, identifying causal effects, writing introductions, formatting tables, preparing replication packages, and responding to reviewers.

Each pack is **journal-specific by design**: it encodes the editorial preferences, formatting conventions, identification standards, and review culture of a single target venue. Generic "scientific writing" skill packs miss these constraints.

---

## Why "Journal-Specific" Skills?

Top journals impose constraints that differ materially across venues:

- **AER** desk-rejects on identification design (TWFE, weak IV, naive RDD).
- **《管理世界》** desk-rejects on missing China institutional context.
- **《经济研究》** desk-rejects on missing canonical theory citations.

A one-size-fits-all "economics writing" skill cannot encode these differences. Each pack here is opinionated by venue.

---

## The Skill Packs

| Venue                          | Repository                                                                                  | Discipline                       | Status  |
|--------------------------------|---------------------------------------------------------------------------------------------|---------------------------------|---------|
| **American Economic Review** + AER:Insights + AEJ family | [AER-skills](https://github.com/brycewang-stanford/AER-skills)                              | Economics (top-5)                | v1.0    |
| **《管理世界》** (Management World)        | [management-world-skills](https://github.com/brycewang-stanford/management-world-skills)    | Management + applied economics  | v0.1    |
| **《经济研究》** (Economic Research)        | [economic-research-skills](https://github.com/brycewang-stanford/economic-research-skills)  | Economics (China-CSSCI top)     | v0.1    |

---

## How to Use

### Option A — Claude Code Plugin (recommended)

For each pack you want:

```bash
# AER
/plugin marketplace add https://github.com/brycewang-stanford/AER-skills
/plugin install aer-skills

# 管理世界
/plugin marketplace add https://github.com/brycewang-stanford/management-world-skills
/plugin install management-world-skills

# 经济研究
/plugin marketplace add https://github.com/brycewang-stanford/economic-research-skills
/plugin install economic-research-skills

/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/AER-skills.git
git clone https://github.com/brycewang-stanford/management-world-skills.git
git clone https://github.com/brycewang-stanford/economic-research-skills.git

mkdir -p ~/.claude/skills
cp -R AER-skills/skills/aer-* ~/.claude/skills/
cp -R management-world-skills/skills/mw-* ~/.claude/skills/
cp -R economic-research-skills/skills/er-* ~/.claude/skills/
```

### First Prompt

```
Use aer-workflow (or mw-workflow / er-workflow) to tell me which skill I should
use next for my manuscript targeted at <journal>.
```

---

## Pack-Selection Cheat Sheet

| Your manuscript looks like…                            | Use this pack                |
|--------------------------------------------------------|------------------------------|
| Causal-identification empirical paper aimed at top-5 econ | `AER-skills`                |
| China-context empirical paper with policy actionability   | `management-world-skills`   |
| China-context paper with theoretical grounding            | `economic-research-skills`  |

---

## Roadmap

Future packs under consideration (no commitments):

- **QJE / JPE / RES / Econometrica** — top-5 econ companions to AER
- **《经济学（季刊）》 / CEQ** — methodological econ in Chinese
- **《管理科学学报》** — Chinese management methodology journal
- **JF / JFE / RFS** — top-3 finance
- **AMJ / AMR / ASQ** — top management

Open an issue if you want a specific venue prioritized.

---

## Contributing

Each pack lives in its own repository. To contribute to a pack, open a PR on that pack's repo. To propose a new pack, open an issue here.

Quality bar for inclusion in this index:

1. Opinionated by venue (not generic)
2. Bilingual zh-CN / en README (for China-relevant venues)
3. At least one `*-workflow` router skill
4. Plugin manifests (`.claude-plugin/plugin.json` + `marketplace.json`)
5. MIT-licensed

---

## Related Projects

Generic scientific-writing skill packs (different scope from this index):

- [Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills)
- [nature-skills](https://github.com/Yuan1z0825/nature-skills)

---

## License

MIT
