# De-clone plan — `Chinese-SocialScience-Journal-Skills` breadth bundle

## Problem (verified)
~82 of the bundle's 103 single-journal `SKILL.md` are **name-swap clones** (>0.90 normalized
similarity): swap the 《刊名》 + 3 选题 bullets + 1 改投 line and the file reads identically.
They carry **no checkable facts** (no 主办单位, founding year, fee policy, review model, abstract/
keyword/citation rules, portal). This is the exact defect `.maintenance/METHODOLOGY.md` exists to
kill — it was fixed for the 11 English depth packs (waves 1–2) and audited-clean for the 14 Chinese
*depth* packs (wave 6), but the Chinese **breadth bundle** was never de-cloned.

## Feasibility (PROVEN, 2026-05-31)
Real, citable, venue-specific facts ARE obtainable via WebSearch over official 投稿须知 +
reputable aggregators, even when WebFetch is blocked. Two journals fully verified + rewritten as a
sample (see below). Caveat from prior waves: some obscure journals' official sites may be
unreachable from the sandbox — for those, assert only what is confirmable and **honestly flag 待核实**
(never invent), per the methodology.

## Sample delivered (this session) — proves the pipeline
| Journal | slug | facts injected | clone-similarity before→after |
|---|---|---|---|
| 《经济问题》 | `economic-problems` | 山西省社科院主办·1979·月刊; 不收审稿/版面费; 审稿~2月、见刊6–9月; 查重≤10%; 官网 jjwt.juqk.net | 0.94 → **0.65** |
| 《管理评论》 | `management-review` | 中科院大学主办·月刊; 全程匿名+纯线上审稿; 中文摘要200–300字/英文300–400词; 关键词3–8; 顺序编码参考文献; 图表中英对照; 官网 guanlipl.cn | clone → differentiated |
Both: audit tool still green (844/44/200), bundle still 103 skills, frontmatter keys preserved.

## Per-journal pipeline (repeat ×~80)
1. `WebSearch "《刊名》 投稿须知 字数 审稿周期 版面费 参考文献"` (+ a 2nd search for 主办/创刊 if needed).
2. Extract the checkable set: **主办/主管单位 · 创刊年 · 刊期 · 费用(审稿/版面) · 审稿模式(匿名?) · 投稿系统(线上/邮箱/官网) · 摘要字数 · 关键词数 · 参考文献体例 · 审稿/见刊周期 · 查重阈值 · 选题边界**.
3. Rewrite `SKILL.md` keeping the spec skeleton (期刊定位/触发时机/选题偏好/方法与证据/结构与写作/官方核验清单/投稿前自检/高频拒稿雷区/改投判断/输出格式) and the `name`/`description` frontmatter keys. Add a **「## 关键事实（核验日期 2026-05；以官网最新为准）」** block. Enrich the `description` with 1–2 real anchors.
4. Verify改投 target slugs resolve to real bundle siblings (the bundle uses `economist-cn`, `economic-theory-and-business-management`, `journal-of-management-sciences-china`, … — easy to mis-slug).
5. Honesty: assert only verified facts; numbers get "以官网最新《投稿须知》为准" hedge; unreachable journals → keep generic but mark 待核实, do NOT fabricate.
6. Check: normalized similarity vs a same-cluster sibling should drop below ~0.75.

## Clone clusters (≈82 files, from the content-audit)
- **sci-tech-policy (11)**: bulletin-of-chinese-academy-of-sciences, china-soft-science, forum-on-science-and-technology-in-china, research-and-development-management, science-and-technology-progress-and-policy, science-of-science-and-management-of-st, soft-science, studies-in-science-of-science, science-research-management, scientific-management-research, …
- **finance-univ/econ-policy (11)**: contemporary-finance-and-economics, economic-problems✅, inquiry-into-economic-issues, journal-of-{central,guangdong,jiangxi,shanxi}-university-of-finance-and-economics, journal-of-zhongnan-university-of-economics-and-law, …
- **general-econ (10)**: china-economic-studies, economic-perspectives, economic-review-cn, economist-cn, industrial-economics-research, …
- **management (7)**: business-management-journal, chinese-journal-of-management, foreign-economics-and-management, journal-of-management, management-review✅, organization-and-management, …
- **public-admin (6)**, **reform/political-econ (6)**, **rural-econ (5)**, **finance (5)**, … (✅ = de-cloned this session)

## Recommended execution (on user go-ahead)
Fan out ~6–8 parallel sub-agents, one per cluster (siblings share craft scaffolding, so a
cluster-local agent reuses research efficiently). Each agent: de-clone its cluster per the pipeline,
leave edits uncommitted, log to this file. Budget: ~80 journals × (1–2 searches + rewrite). Keep the
skill **count and folder names stable** (rewrite in place; never add/remove skills).

## Out of scope here / coordination
- Parallel **Codex** owns root README + marketplace + CI + tools — do not edit those.
- Natural-science Science↔PNAS rebuttal/statistics clones + ER-template generic roles in MW/CRE/CFE
  depth packs are a *separate* (smaller) de-clone task, same pipeline.
