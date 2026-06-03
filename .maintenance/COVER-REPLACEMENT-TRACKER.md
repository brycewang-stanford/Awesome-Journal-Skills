# Journal Cover Replacement Tracker

Goal: replace every remaining **generated placeholder** cover (`assets/covers/<slug>.png`) with a
**real journal cover**. The README galleries already point at `assets/covers/<slug>.png`, so swapping
the file in place updates the display — no markup changes needed.

Covers are installed by `assets/install_cover.py`, which validates the image (real raster, ≥6 KB),
resizes to a cover-shaped PNG (max edge 320 px), and appends a provenance row to
`assets/covers/REAL-COVERS.tsv` (the recovery manifest — every real cover is traceable there).

---

## ⚠️ Environment note (discovered 2026-06-02, session 2)

This working copy is under an **auto-commit + auto-push** mechanism (commits authored as
`Bryce Wang <brycew6m@stanford.edu>`, conventional-commit messages like `chore: refresh cover assets
chunk N`). During session 2 it committed **and pushed every cover change to `origin/main`** on its
own — `install_cover.py` itself never commits, but the surrounding hook does.

**Consequence:** the old "covers land uncommitted for the user's 验收" convention **no longer holds** —
changes go live to the public remote immediately, and the hook also sweeps in any other untracked
files present in the tree. If a review-before-publish gate is wanted, the hook must be disabled first.
Every cover installed in session 2 was visually verified *before* the next step, so the live state is
clean, but this is the user's call going forward.

---

## Live counts

| Metric | Value |
|---|---|
| Total gallery covers | 304 |
| Real covers (in `REAL-COVERS.tsv`) | **244** |
| Placeholders remaining | **60** |
| Last updated | 2026-06-02 (session 2 of the month-long pass) |

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
`https://ars.els-cdn.com/content/image/X<ISSN-no-dash>.jpg` (journal's print/linking ISSN).
```bash
python3 assets/install_cover.py <slug> "https://ars.els-cdn.com/content/image/X<ISSN>.jpg" "Publisher:Elsevier" "publisher cover (fair-use)"
```

### Route 2 — Chinese journals via 维普 cqvip (proven, the Group A workhorse)
1. `WebSearch "<中文刊名> 期刊 维普 cqvip www.cqvip.com/journal"` → find `www.cqvip.com/journal/<ID>/...`.
2. The cover image ID is usually the journal's **gch** code, NOT the numeric URL path segment.
   `WebFetch` the journal page and read the `<img>` whose src contains `image.cqvip.com`/`qkclearimg`,
   or build `http://image.cqvip.com/vip1000/qkclearimg/<gch_lower>/<gch_lower>.jpg`.
3. `python3 assets/install_cover.py <slug> "<cover_url>" "Publisher:维普 cqvip (<中文刊名>)" "Publisher:cqvip" [chunkN.tsv]`
- Note: cqvip serves small-but-real thumbnails (4–6 KB) for some journals — distinct from its **gray
  180×250 "无封面" placeholder** (also 4–6 KB). When a genuine cover is just under the 6 KB floor, fetch
  it, **visually confirm it is the real cover (not the gray placeholder)**, `sips -s format png -Z 320`,
  and add the manifest row by hand. Never wave through the gray placeholder.

### Route 3 — NCPSSD (国家哲学社会科学文献中心) — NEW, proven session 2
When cqvip returns its gray placeholder or 412/500-blocks, NCPSSD often has the real cover:
`https://ft.ncpssd.cn/image/get/qwcover/<year>/<issue>/<GCH>.jpg` (GCH is the same cqvip gch code).
`install_cover.py`'s plain urllib fetch gets through even when `WebFetch` is anti-bot-blocked.
Verified this session for: 中国农村观察, 金融评论, 经济社会体制比较, 中南财经政法大学学报.

### Route 4 — Wikimedia fair-use files (for English journals; use with care)
`https://en.wikipedia.org/wiki/Special:FilePath/<Exact_File_Name>.jpg` (or `commons.wikimedia.org`).
**Fetchable from this environment** (probed 2026-06-02: HTTP 200). This is the route for Group B
journals that have a fair-use cover file on Wikipedia/Commons.
- ⚠️ This is NOT the Wikipedia `pageimages` API (that returned WRONG images and caused 8 reverts in
  session 1). You must find the EXACT correct cover FILE by name and **visually verify the rendered PNG**.
- `journal-of-money-credit-and-banking` cover exists at
  `Special:FilePath/Journal_of_Money,_Credit_and_Banking.jpg` but is **5463 B**, just under the 6 KB
  floor → recoverable with the sub-floor override.

### ⚠️ Routes confirmed BLOCKED from this environment (probed 2026-06-02)
- **Publisher CDNs**: SAGE `journals.sagepub.com` → **HTTP 403**, APS `journals.aps.org` → **HTTP 403**.
  Also (per session 1) Wiley, Taylor&Francis, Univ-of-Chicago Press, INFORMS, AIS, OUP/Silverchair
  (signed URLs), IOP. These need a real browser → hand-download by the user.
- **AEA site** (AER/AEJ/JEP/JEL) — covers are CSS/text, not downloadable images.
- **Baidu Baike** — gives logos (形象标识), not covers.

### ⚠️ MUST visually verify every install
`Read assets/covers/<slug>.png` after installing — the cover prints the journal title, so wrong
covers / logos / gray placeholders are caught at a glance. **A wrong cover is worse than an honest
placeholder.** Wrong installs are reverted with `git checkout -- assets/covers/<slug>.png` (all 304
cover PNGs are git-tracked, so the committed placeholder restores cleanly).

### ⚠️ Maintenance gotcha
Do **NOT** re-run `assets/gen_covers.py` / `assets/gen_breadth_covers.py` blindly — they regenerate
placeholder cards and clobber real covers. `REAL-COVERS.tsv` is the recovery manifest.

---

## Remaining placeholders by route (60)

### Group A — Chinese journals → ✅ COMPLETE (0 remaining)
All ~72 Group A Chinese journals were installed and independently visually verified in session 2
(66 via cqvip Route 2, 7 stragglers via NCPSSD Route 3 / official sites; the smoke test via cqvip).
Provenance for every one is in `REAL-COVERS.tsv`. Zero wrong covers survived (strict verify/revert).

### Group B — English journals (46) → browser hand-off (Wikimedia Route 4 EXHAUSTED — only JMCB had a free cover)
All 47 were checked exhaustively on Wikipedia/Commons (raw wikitext + image API, not the unreliable
pageimages route). Exactly one — `journal-of-money-credit-and-banking` — had a fair-use printed cover
(now installed). The other 46 have only logos, empty infobox cover params, redirects, or no article, and
their publisher CDNs are 403-blocked here. **These need a real browser hand-download by the user.**
academy-of-management-annals · academy-of-management-journal · academy-of-management-review ·
angewandte-chemie-international-edition · annals-of-mathematics · ca-a-cancer-journal-for-clinicians ·
contemporary-accounting-research · entrepreneurship-theory-and-practice · financial-management ·
human-resource-management · ieee-transactions-on-pattern-analysis-and-machine-intelligence ·
informs-journal-on-computing · international-economic-review · journal-of-accounting-research ·
journal-of-applied-econometrics · journal-of-business-and-economic-statistics ·
journal-of-economic-geography · journal-of-labor-economics · journal-of-law-and-economics ·
journal-of-machine-learning-research · journal-of-management-en ·
journal-of-management-information-systems · journal-of-management-studies · journal-of-marketing ·
journal-of-marketing-research · journal-of-political-economy ·
journal-of-the-association-for-information-systems · marketing-science · mathematical-finance ·
organization-science · physical-review-d · physical-review-letters · physical-review-x ·
production-and-operations-management · prx-quantum · quantitative-economics ·
reports-on-progress-in-physics · review-of-economic-studies · review-of-financial-studies ·
review-of-political-economy · reviews-of-modern-physics · strategic-management-journal ·
the-astrophysical-journal · the-econometrics-journal · the-economic-journal · world-bank-economic-review

Plan for Group B:
- **Wikimedia-recoverable subset** (famous journals likely to have a fair-use cover file): try Route 4
  with strict verify/revert. `journal-of-money-credit-and-banking` was recovered via this route.
- **APS family** (physical-review-d/letters/x, prx-quantum, reviews-of-modern-physics, reports-on-progress):
  Wikipedia infoboxes historically serve the *PRB* cover for all of them — each needs its OWN cover; do
  not accept a shared image. Likely browser-only.
- **Remainder** (society journals, no free cover): hand-download by the user from the publisher site.

### Group C — AEA text-covers / no pictorial cover (10) → keep as polished cards (acceptable)
aej-applied-economics · aej-economic-policy · aej-macroeconomics · aej-microeconomics · aer-insights ·
economic-perspectives · economic-policy · journal-of-economic-literature · journal-of-economic-perspectives ·
brookings-papers-on-economic-activity

### Group D — special cases (4) → do NOT auto-fill
- **english-socsci** — homepage card for the English-SocialScience breadth *bundle*, not a single journal.
- **organization-and-management** (《组织与管理》) — no verifiable mainland CSSCI journal by this name.
- **annual-review-of-economics** — Annual Reviews uses a wide web *banner*, not a portrait cover.
- **elife** — Wikipedia/Commons have only the *logo*, not a cover.

---

## Session log
- **2026-06-02 (session 1):** Built `assets/wiki_cover.py`; proven routes 1 & 2. Installed +17 real
  covers (9 Elsevier, 5 cqvip, 3 Lancet). Reverted 8 wrong Wikipedia-pageimages auto-installs.
  Real 153→170, placeholders 151→134.
- **2026-06-02 (session 2):** Completed **all of Group A** — fanned out 8 parallel cqvip agents
  (per-chunk manifests to avoid write races) + 1 straggler agent (NCPSSD Route 3). **+73 real covers**,
  every one independently visually verified (12 high-risk + 53 audit-agent + 7 straggler + smoke = 100%);
  **0 wrong covers survived**. Discovered Route 3 (NCPSSD) and Route 4 (Wikimedia fetchable; SAGE/APS
  confirmed 403). Discovered the auto-commit/push environment behavior (see top note). Real 170→243,
  placeholders 134→61. Remaining: Group B (47, publisher-blocked / partial Wikimedia), C (10, keep), D (4, keep).
- **2026-06-02 (session 2, Group B smoke):** Recovered `journal-of-money-credit-and-banking` via the
  exact Wikipedia fair-use file route after the 6 KB floor issue was handled manually. Real 243→244,
  placeholders 61→60.
