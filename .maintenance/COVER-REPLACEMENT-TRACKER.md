# Journal Cover Replacement Tracker

Goal: replace every remaining **generated placeholder** cover (`assets/covers/<slug>.png`) with a
**real journal cover**. The README galleries already point at `assets/covers/<slug>.png`, so swapping
the file in place updates the display — no markup changes needed.

Status is updated as covers are installed. Covers are left **uncommitted** for the user's 验收
(per repo convention — `install_cover.py` never commits/pushes).

---

## Live counts

| Metric | Value |
|---|---|
| Total gallery covers | 304 |
| Real covers (in `REAL-COVERS.tsv`) | **170** |
| Placeholders remaining | **134** |
| Last updated | 2026-06-02 (session 1 of the month-long pass) |

Recompute anytime:
```bash
python3 - <<'PY'
import os
C="assets/covers"; png={f[:-4] for f in os.listdir(C) if f.endswith(".png")}
real={ln.split("\t")[0] for i,ln in enumerate(open(f"{C}/REAL-COVERS.tsv",encoding="utf-8")) if i and ln.strip()}
ph=sorted(png-real); print(f"real={len(real)} placeholders={len(ph)}"); print("\n".join(ph))
PY
```

---

## Proven source routes (use in this priority order)

### Route 1 — Elsevier / Cell Press / Lancet (deterministic, highest confidence)
`https://ars.els-cdn.com/content/image/X<ISSN-no-dash>.jpg` (use the journal's print/linking ISSN).
```bash
python3 assets/install_cover.py <slug> "https://ars.els-cdn.com/content/image/X<ISSN>.jpg" "Publisher:Elsevier" "publisher cover (fair-use)"
```
Verified working this session: AOS, One Earth, The Innovation, Trends in Cognitive Sciences,
Cell Host & Microbe, Cell Metabolism, Chem, World Development, Review of Economic Dynamics,
The Lancet {Infectious Diseases, Oncology, Neurology}.

### Route 2 — Chinese journals via 维普 cqvip (proven, ~2 web calls/journal)
1. `WebSearch "<中文刊名> 期刊 维普 cqvip www.cqvip.com/journal"` → get the `www.cqvip.com/journal/<id>/<id>` page URL.
2. `WebFetch` that page → extract the cover URL `http://image.cqvip.com/vip1000/qkclearimg/<NNNNN[x|a]>/<NNNNN[x|a]>.jpg`.
3. Install:
```bash
python3 assets/install_cover.py <slug> "http://image.cqvip.com/vip1000/qkclearimg/<ID>/<ID>.jpg" "Publisher:维普 cqvip (<中文刊名>)" "Publisher:cqvip"
```
Verified this session: 中国工业经济, 会计研究, 金融研究, 经济学(季刊), 中国社会科学.

### ⚠️ Routes that DON'T work from this environment (don't waste calls)
- **Wikipedia `pageimages` API** — exhausted. The first round already took every easy Wikipedia
  cover. For the remainder it returns *nothing* or the *wrong* image (logos; PRB cover served for
  PRD/PRX-Quantum; parent Lancet cover for specialty Lancet; World Bank photo for WBER). Auto-using
  it caused 8 wrong installs this session — all reverted. If you must use Wikipedia, find the EXACT
  fair-use file URL by hand and verify the rendered PNG.
- **AEA site** (AER/AEJ/JEP/JEL) — covers are CSS/text, not downloadable images.
- **Baidu Baike** — gives logos (形象标识), not covers, for many journals.
- **Bot-blocked publisher CDNs** — SAGE, Wiley, Taylor&Francis, Univ-of-Chicago Press, INFORMS,
  AIS, OUP/Silverchair (signed URLs), IOP, APS. Need a real browser; candidates for the user to
  hand-download, or retry if a free mirror appears.

### ⚠️ MUST visually verify every install
`Read assets/covers/<slug>.png` after installing — the cover prints the journal title, so wrong
covers / logos are caught at a glance. A wrong cover is worse than an honest placeholder.

### ⚠️ Maintenance gotcha
Do **NOT** re-run `assets/gen_covers.py` / `assets/gen_breadth_covers.py` blindly — they regenerate
placeholder cards and clobber real covers. `REAL-COVERS.tsv` is the recovery manifest.

---

## Remaining placeholders by route

### Group A — Chinese journals → Route 2 (cqvip). ~60, the bulk of remaining work.
Slug → best-guess 中文刊名 (verify on cqvip before install; ⚠ = known trap from round 1).

| slug | 中文刊名 (verify) | note |
|---|---|---|
| accounting-and-economics-research | 审计与经济研究 | |
| asia-pacific-economic-review | 亚太经济 | |
| auditing-research | 审计研究 | |
| bulletin-of-chinese-academy-of-sciences | 中国科学院院刊 | |
| business-management-journal | 经济管理 | |
| china-accounting-review | 中国会计评论 | ⚠ round1 title-fix done; confirm identity |
| china-economic-studies | 中国经济问题 | |
| china-public-administration-review | 公共行政评论 | English/bilingual; try cqvip then publisher |
| china-rural-economy | 中国农村经济 | CASS rural 双刊 sibling |
| china-rural-survey | 中国农村观察 | CASS rural 双刊 sibling |
| china-soft-science | 中国软科学 | |
| chinese-journal-of-management | 管理学报 (华科大) | |
| chinese-journal-of-management-science | 中国管理科学 | |
| chinese-public-administration | 中国行政管理 | |
| chinese-review-of-financial-studies | 金融评论 | |
| comparative-economic-and-social-systems | 经济社会体制比较 | |
| contemporary-finance-and-economics | 当代财经 | |
| e-government | 电子政务 | |
| east-china-economic-management | 华东经济管理 | |
| economic-review-cn | 经济评论 | |
| economic-theory-and-business-management | 经济理论与经济管理 | |
| economist-cn | 经济学家 | |
| finance-and-economics | 财经科学 | |
| finance-and-trade-economics | 财贸经济 | |
| financial-regulation-research | 金融监管研究 | |
| foreign-economics-and-management | 外国经济与管理 | |
| forum-on-science-and-technology-in-china | 中国科技论坛 | |
| frontiers-of-engineering-management-science-and-technology | 工程管理科技前沿 | =合肥工大原《预测》 |
| governance-studies | 治理研究 | |
| inquiry-into-economic-issues | 经济问题探索 | ⚠ 云南省发改委系统研究院 |
| international-economic-review-cn | 国际经济评论 | |
| international-economics-and-trade-research | 国际经贸探索 | |
| issues-in-agricultural-economy | 农业经济问题 | |
| journal-of-agrotechnical-economics | 农业技术经济 | |
| journal-of-business-economics | 商业经济与管理 | |
| journal-of-central-university-of-finance-and-economics | 中央财经大学学报 | 财经大学学报 family |
| journal-of-finance-and-economics | 财经研究 (上财) | |
| journal-of-guangdong-university-of-finance-and-economics | 广东财经大学学报 | 财经大学学报 family |
| journal-of-industrial-engineering-and-engineering-management | 工业工程与管理? | verify exact title |
| journal-of-international-trade | 国际贸易问题 | |
| journal-of-jiangxi-university-of-finance-and-economics | 江西财经大学学报 | 财经大学学报 family |
| journal-of-zhongnan-university-of-economics-and-law | 中南财经政法大学学报 | ⚠ NOT 《法商研究》 |
| macroeconomics | 宏观经济研究 | verify |
| modern-finance-and-economics | 现代财经(天津财大) | |
| modern-financial-research | 现代金融研究 | ⚠ cqvip search returns 《金融论坛》— verify hard |
| public-administration-and-policy-review | 公共管理与政策评论 | |
| public-finance-research | 财政研究 | |
| reform | 改革 | |
| reform-of-economic-system | 经济体制改革 | |
| research-and-development-management | 研究与发展管理 | |
| research-on-economics-and-management | 经济与管理研究 | |
| research-on-financial-and-economic-issues | 财经问题研究 | |
| rural-economy | 农村经济 | |
| science-and-technology-progress-and-policy | 科技进步与对策 | |
| science-of-science-and-management-of-st | 科学学与科学技术管理 | |
| science-research-management | 科研管理 | |
| scientific-decision-making | 科学决策 | |
| scientific-management-research | 科学管理研究 | |
| securities-market-herald | 证券市场导报 | |
| shanghai-journal-of-economics | 上海经济研究 | |
| social-security-studies | 社会保障研究 | |
| sociological-studies | 社会学研究 | cqvip id surfaced: journal/19790 |
| soft-science | 软科学 | |
| south-china-journal-of-economics | 南方经济 | |
| studies-in-labor-economics | 劳动经济研究 | |
| studies-in-science-of-science | 科学学研究 | |
| studies-of-financial-economics | 财经理论与实践? | verify exact title |
| studies-of-international-finance | 国际金融研究 | cqvip: journal/98100X |
| systems-engineering-theory-and-practice | 系统工程理论与实践 | |
| tax-research | 税务研究 | |
| world-economic-papers | 世界经济文汇 | |
| world-economic-studies | 世界经济研究 | |

### Group B — English journals, publisher-CDN BLOCKED → need a real browser / hand-download. ~40.
SAGE/Wiley/T&F/UChicago/INFORMS/AIS/OUP/IOP/APS. Low automation yield from here.

academy-of-management-annals · academy-of-management-journal · academy-of-management-review ·
angewandte-chemie-international-edition · ca-a-cancer-journal-for-clinicians ·
contemporary-accounting-research · entrepreneurship-theory-and-practice · financial-management ·
human-resource-management · ieee-transactions-on-pattern-analysis-and-machine-intelligence ·
informs-journal-on-computing · international-economic-review · journal-of-accounting-research ·
journal-of-applied-econometrics · journal-of-business-and-economic-statistics ·
journal-of-economic-geography · journal-of-labor-economics · journal-of-law-and-economics ·
journal-of-machine-learning-research · journal-of-management-en ·
journal-of-management-information-systems · journal-of-management-studies · journal-of-marketing ·
journal-of-marketing-research · journal-of-money-credit-and-banking · journal-of-political-economy ·
journal-of-the-association-for-information-systems · marketing-science · mathematical-finance ·
organization-science · physical-review-d · physical-review-letters · physical-review-x ·
production-and-operations-management · prx-quantum · reports-on-progress-in-physics ·
review-of-economic-studies · review-of-financial-studies · review-of-political-economy ·
reviews-of-modern-physics · strategic-management-journal · the-astrophysical-journal ·
the-econometrics-journal · the-economic-journal · world-bank-economic-review

Notes:
- **journal-of-money-credit-and-banking** — a real fair-use cover exists on Wikipedia
  (`Journal_of_Money,_Credit_and_Banking.jpg`) but is **5.4 KB**, just under install_cover.py's 6 KB
  raster floor. Recoverable with a manual size override if desired.
- **physical-review-* / prx-quantum / reviews-of-modern-physics** — APS Wikipedia infoboxes serve
  the **PRB** cover. Must source each journal's own cover; otherwise leave as placeholder.
- **the-lancet-* ** — DONE this session via Elsevier ISSN (Group A route 1), not blocked.

### Group C — AEA text-covers / no pictorial cover → low priority (acceptable as polished cards).
aej-applied-economics · aej-economic-policy · aej-macroeconomics · aej-microeconomics · aer-insights ·
economic-perspectives · economic-policy · journal-of-economic-literature · journal-of-economic-perspectives ·
brookings-papers-on-economic-activity

### Group D — special cases (do NOT auto-fill).
- **english-socsci** — homepage card for the English-SocialScience breadth *bundle*, not a single
  journal. Keep the branded card.
- **organization-and-management** (《组织与管理》) — round 1 found no verifiable mainland CSSCI
  journal by this name (only a Taiwan one). Leave placeholder unless identity is confirmed.
- **annual-review-of-economics** — Annual Reviews uses a wide web *banner*, not a portrait cover;
  it breaks the gallery grid. Left as placeholder by choice.
- **angewandte-chemie / elife / academy-of-management-journal / journal-of-management-studies** —
  Wikipedia/Commons only have *logos*, not covers.

---

## Session log
- **2026-06-02 (session 1):** Built `assets/wiki_cover.py`; proven routes 1 & 2. Installed +17 real
  covers (9 Elsevier, 5 cqvip incl. full hero gallery, 3 Lancet specialty). Reverted 8 wrong
  Wikipedia-pageimages auto-installs. Real 153→170, placeholders 151→134.
