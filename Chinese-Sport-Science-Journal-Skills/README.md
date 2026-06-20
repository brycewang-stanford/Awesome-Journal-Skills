# Chinese Sport Science Journal Skills（中文体育学期刊 Skills）

<p align="center">
  <img src="assets/cover.svg" alt="Chinese Sport Science Journal Skills — 12 CSSCI sport-science journals" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Index](https://img.shields.io/badge/index-CSSCI%20Sport%20Science-1f6feb)](#)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

An agent skill stack for the **12 CSSCI source journals of sport science (体育学, 2025–2026)**. This bundle promotes sport science from an *Other* footnote inside the Chinese social-science bundle to **its own first-class discipline category**. It covers the field-defining 《体育科学》 (China Sport Science) and the application-leaning 《中国体育科技》 (China Sport Science and Technology) — both from the China Institute of Sport Science / China Sport Science Society system — the comprehensive journals of the Beijing, Shanghai, Chengdu, Wuhan, Xi'an, Shenyang and Tianjin sport universities, and the humanities-and-social-science-leaning 《体育学刊》《体育学研究》《体育与科学》.

It is the sport-science sibling of [`Chinese-SocialScience-Journal-Skills`](../Chinese-SocialScience-Journal-Skills/). As with the sibling bundle: **one self-contained fit-and-house-style skill per journal**, plus `cn-sport-journal-workflow` for routing. Sport science spans both **运动人体科学** (exercise physiology / biochemistry / biomechanics / sports medicine / fitness & health) and **体育人文社会学** (sport sociology / management / economics / policy / history & philosophy / school PE / training & competitive sport / ethnic traditional sport). Each skill helps answer: *is my manuscript on-target, does it take the natural-science or the social-science path, are the methods and evidence sufficient, and what official submission details must be re-checked?*

## Coverage

| Group | Journals | Count |
|---|---|--:|
| Discipline flagships (society-run) | 《体育科学》, 《中国体育科技》 | 2 |
| Comprehensive sport-university journals | Beijing · Shanghai · Chengdu · Wuhan · Xi'an · Shenyang · Tianjin sport universities | 7 |
| Humanities / social-science leaning | 《体育学刊》, 《体育学研究》, 《体育与科学》 | 3 |
| **Per-journal skills total** | | **12** |
| Routing workflow (`cn-sport-journal-workflow`) | | 1 |

## Skills

| Skill | Journal | Host / Leaning |
|---|---|---|
| `china-sport-science` | 《体育科学》 (China Sport Science) | China Sport Science Society · field-defining |
| `china-sport-science-and-technology` | 《中国体育科技》 (China Sport Science and Technology) | China Inst. of Sport Science · applied / competitive |
| `journal-of-beijing-sport-university` | 《北京体育大学学报》 | BSU · comprehensive |
| `journal-of-shanghai-university-of-sport` | 《上海体育大学学报》 | SUS · comprehensive (social-science strong) |
| `journal-of-chengdu-sport-university` | 《成都体育学院学报》 | CDSU · sport history / ethnic traditional sport |
| `journal-of-wuhan-sports-university` | 《武汉体育学院学报》 | WSU · comprehensive |
| `journal-of-xian-physical-education-university` | 《西安体育学院学报》 | XAPEU · comprehensive |
| `journal-of-shenyang-sport-university` | 《沈阳体育学院学报》 | SYSU · comprehensive |
| `journal-of-tianjin-university-of-sport` | 《天津体育学院学报》 | TUS · comprehensive (exercise science strong) |
| `journal-of-physical-education` | 《体育学刊》 (Journal of Physical Education) | SCNU · humanities / school PE |
| `journal-of-sports-research` | 《体育学研究》 (Journal of Sports Research) | NSI · sport social science / theory |
| `sports-and-science` | 《体育与科学》 (Sports & Science) | Jiangsu · reflective / interdisciplinary |

## How to use

1. **Route first**: start from `cn-sport-journal-workflow`, classify by sub-discipline (exercise science / sport humanities & social science / competitive training / school PE), contribution type and method form, and get a shortlist.
2. **Then fit**: open the preferred journal's skill to check scope, framing, method/evidence bar, house style, and the most likely rejection triggers.
3. **Re-check the official site last**: every skill ends with an official-verification checklist. Before submitting, open the journal's current author guidelines (see [`resources/official-source-map.md`](resources/official-source-map.md)) — **the official site wins.**

## Design rules (same as the sibling bundle)

- **No volatile facts**: no impact factors, APCs, ISSNs, exact word limits, column lists, or editor names — these live on the official site and change.
- **No fabricated citations**: literatures are referred to generically.
- **Only durable conventions**: only persistent structural facts (host institution, disciplinary leaning, the natural-science vs. social-science dual path, ethics/reporting norms) inform fit.
- **Official site first**: if the live official rules conflict with a skill, the official rules win.

## Source discipline

Journal rules change. [`resources/source-basis.md`](resources/source-basis.md) records this bundle's source discipline, and [`resources/official-source-map.md`](resources/official-source-map.md) lists an official-source starting point per journal. Before any real submission, re-check the journal's latest official author guidelines; if a skill conflicts with the official requirements, the official requirements win.

## License

MIT © 2026 Bryce Wang, see [LICENSE](LICENSE).
