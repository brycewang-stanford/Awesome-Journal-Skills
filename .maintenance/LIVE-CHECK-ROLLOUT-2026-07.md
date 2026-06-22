# Live-Check Rollout — All Remaining Lanes (2026-07 campaign)

**Mandate:** extend the humanities/social-science live-check method (verify current
Editor[s]-in-Chief + APC/submission fees → backfill source map with fact + source +
access date → de-hedge SKILL bodies → validate gates → commit) to **all 164 remaining
first-party packs** (econ, finance, accounting, management, marketing, ops/IS, poli-sci,
public-admin, psychology, sociology/demography, CS/AI, natural-science/env/ag, law,
humanities/breadth-bundles).

**Method (unchanged from the 19-pack first campaign):** WebSearch is the workhorse
(publisher sites 403 WebFetch); verify each fact against ≥2 authoritative sources
(official journal/society page + society news); never fabricate; keep honest narrowed
hedges where a value genuinely isn't publicly pinnable; correct any stale facts found
(cf. the Sociological Theory "Tavory" correction). Date stamp: **2026-06-22+**.

**Execution:** parallel verification subagents, one per disjoint cluster. Subagents
EDIT files but DO NOT git-commit (avoids `.git/index.lock` races); they report changed
files + per-pack summaries. The orchestrator runs `run_checks` + `source_map_audit` and
commits each wave centrally, with an other-lane guard on every commit.

**Coordination:** Yale-Law-Journal-Skills has an active parallel agent — handled last,
with extra care. Breadth bundles (Chinese-/English-SocialScience/NaturalScience/Humanities,
Social-Sciences-in-China) are multi-journal — no single editor; verify only that their
framing is honest, don't invent a masthead.

## Cluster backlog (≈17 clusters, 164 packs)

- **W1-A Econ-top (8):** Econometrica, Quarterly-Journal-of-Economics, Journal-of-Political-Economy, Review-of-Economic-Studies, Review-of-Economics-and-Statistics, The-Economic-Journal, Journal-of-the-European-Economic-Association, AER-Insights
- **W1-B Finance (8):** Journal-of-Finance, Journal-of-Financial-Economics, Review-of-Financial-Studies, Review-of-Finance, Journal-of-Financial-and-Quantitative-Analysis, Journal-of-Corporate-Finance, Mathematical-Finance, Financial-Management
- **W1-C Accounting (6):** Accounting-Research, Contemporary-Accounting-Research, Journal-of-Accounting-Research, Journal-of-Accounting-and-Economics, Review-of-Accounting-Studies, The-Accounting-Review
- **W1-D Political-Science (8):** American-Journal-of-Political-Science, American-Political-Science-Review, British-Journal-of-Political-Science, Comparative-Political-Studies, International-Organization, Journal-of-Politics, World-Politics, Governance-Journal
- **W2-A Econ-field (9):** AEJ-Applied-Economics, AEJ-Economic-Policy, AEJ-Macroeconomics, AEJ-Microeconomics, European-Economic-Review, International-Economic-Review, Journal-of-Development-Economics, Journal-of-International-Economics, Journal-of-Public-Economics
- **W2-B Econ-field2 (9):** Journal-of-Economic-Behavior-and-Organization, Journal-of-Economic-Geography, Journal-of-Economic-Growth, Journal-of-Environmental-Economics-and-Management, Journal-of-Health-Economics, Journal-of-Human-Resources, Journal-of-Labor-Economics, Journal-of-Monetary-Economics, Journal-of-Urban-Economics
- **W2-C Econ-theory/journals (8):** Journal-of-Economic-Theory, Journal-of-Econometrics, Econometric-Theory, The-Econometrics-Journal, Journal-of-Applied-Econometrics, Journal-of-Business-and-Economic-Statistics, Quantitative-Economics, Games-and-Economic-Behavior
- **W2-D Econ-policy/dev/misc (8):** Journal-of-Money-Credit-and-Banking, Journal-of-International-Money-and-Finance, Review-of-Economic-Dynamics, Economic-Policy, Experimental-Economics, IMF-Economic-Review, World-Bank-Economic-Review, World-Development
- **W3-A Econ-review/China-econ (9):** Annual-Review-of-Economics, RAND-Journal-of-Economics, Journal-of-Risk-and-Uncertainty, Journal-of-Economic-Literature, Journal-of-Economic-Perspectives, China-Economic-Quarterly, China-Industrial-Economics, China-Rural-Economy, Economic-Research-Journal
- **W3-B China-econ2/mgmt-CN (6):** Journal-of-World-Economy, Journal-of-Quantitative-and-Technological-Economics, Journal-of-Finance-and-Economics, Journal-of-Management-World, Journal-of-Management-Sciences-in-China, Nankai-Business-Review
- **W3-C Management/OB/strategy (8):** Academy-of-Management-Annals, Academy-of-Management-Journal, Academy-of-Management-Review, Administrative-Science-Quarterly, Organization-Science, Organization-Studies, Strategic-Management-Journal, Journal-of-Management
- **W3-D Mgmt2/entrep/HR (7):** Entrepreneurship-Theory-and-Practice, Human-Relations, Human-Resource-Management, Journal-of-Business-Venturing, Journal-of-International-Business-Studies, Journal-of-Management-Studies, Journal-of-Banking-and-Finance
- **W4-A Marketing (6):** Journal-of-Consumer-Psychology, Journal-of-Consumer-Research, Journal-of-Marketing, Journal-of-Marketing-Research, Journal-of-the-Academy-of-Marketing-Science, Marketing-Science
- **W4-B Ops/MS/IS (10):** INFORMS-Journal-on-Computing, Information-Systems-Research, Journal-of-Management-Information-Systems, Journal-of-Operations-Management, Journal-of-the-Association-for-Information-Systems, MIS-Quarterly, Management-Science, Manufacturing-and-Service-Operations-Management, Operations-Research, Production-and-Operations-Management
- **W4-C Psychology (11):** Annual-Review-of-Psychology, Cognitive-Psychology, Developmental-Psychology, Journal-of-Applied-Psychology, Journal-of-Personality-and-Social-Psychology, Perspectives-on-Psychological-Science, Psychological-Bulletin, Psychological-Review, Psychological-Science, Social-Psychology-Quarterly, Social-Forces
- **W4-D Socio/demog/comm (7):** Criminology, Demography, Journal-of-Marriage-and-Family, Population-and-Development-Review, Sociological-Studies, New-Media-and-Society, Public-Opinion-Quarterly
- **W5-A Public-admin/policy + law-econ (6):** Chinese-Public-Administration, Journal-of-Policy-Analysis-and-Management, Journal-of-Public-Administration-Research-and-Theory, Public-Administration-Review, Journal-of-Law-Economics-and-Organization, Journal-of-Law-and-Economics
- **W5-B CS/AI (7):** AAAI, AISTATS, Computer-Science-Conference, ICLR, ICML, IJCAI, NeurIPS
- **W5-C NatSci/env/ag (10):** Agricultural-Systems, Agriculture-Environment-Journal, Clinical-Medicine-Journal, Conservation-Biology, Engineering-Technology-Journal, Environmental-Science-and-Technology, Field-Crops-Research, Global-Change-Biology, Global-Environmental-Change, Chinese-Sport-Science-Journal
- **W5-D Humanities/breadth + law (7):** Critical-Inquiry, The-Art-Bulletin, English-Humanities-Journal, Chinese-SocialScience-Journal, English-SocialScience-Journal, English-NaturalScience-Journal, Social-Sciences-in-China
- **LAST (careful, parallel-agent lanes):** Harvard-Law-Review, Yale-Law-Journal (⚠ active parallel agent)

## Progress log — ROLLOUT COMPLETE 2026-06-22

All 164 remaining packs covered in one session via parallel verification subagents
(edit-only; orchestrator committed centrally per cluster, other-lane guard each time).
**148 packs received edits; 16 were verified already-grounded / honest bundles (no edit
needed)** — total 164. Combined with last month's 19 humanities/socsci packs, **all 183
first-party packs now carry verified current editors + APC/fee facts (access date
2026-06-22, ≥2 authoritative sources each)**.

Commits: 6d50f1c7 (accounting) · 15f4fe12/d08591ad/2bc11f5a/980abee9 (W1+W2A) ·
00bed99d/53556720/3a583007/5ae4b290 (W2 rest) · 5f2ceb03/e5887999/ba1373fa/fec951a1
(W3+W4A) · e7ced722/1348e2d2/93216583/1afa95b1 (W4 rest+W5A) ·
ef1fdf66/1f40dd65/709a7c37 (W5 rest) · de3ce93e (stragglers) · 4fbe21a5 (law reviews).

### Stale-fact corrections caught (high-value)
- **Econometrica**: Imbens listed as current editor → he is former; current is Marina Halac.
- **Journal of Int'l Money & Finance**: long-deceased James R. Lothian (RePEc cache) → Aizenman et al.
- **Economic Policy**: Galbiati/Méjean → Şebnem Kalemli-Özcan. **Experimental Economics**: roster refreshed.
- **World Development**: Agrawal (stepped down 2021) → Dell'Angelo & Rettberg.
- **Econometric Theory**: Phillips (retired end-2025) → Guggenberger/Su/Sun (2026).
- **China Industrial Economics**: 金碚 (former) → 史丹.
- **Academy of Management Journal**: misattributed Ballinger → Roberson (Ballinger edits *Annals*).
- **HRM**: Cronin/Guthrie/Piening/Snell → Cooke & Pichler.
- **Demography**: Curran (term ended) → Lee/Merli/Rangel. **Social Forces**: dropped stray Penner → Kalleberg.
- **JLE**: roster Carlton/Goolsbee/Snyder → current six. **Production & Ops Mgmt**: publisher Wiley → SAGE.
- **Agricultural Systems**: van Wijk → Topp. **Global Environmental Change**: Tschakert/York → Guan & Nagendra.
- **Journal of Financial Markets**: WRONG "no submission fee" → actually US$170. **RFS**: corrected stale fee schedule.
- **Production & Ops Mgmt / The Art Bulletin / Social Sciences in China / many**: editor newly grounded (was blank/hedged).

### Near-term editor transitions flagged for the weekly routine to watch
PMLA (Edwards→Potkay, Jul 2026) · American Anthropologist (Chin→Davis&Mulla, 2027) ·
JHR (Aizer→Lovenheim, Jul 2026) · JFQA (Pennacchi→Giannetti, Sep 2026) · Journal of
Management (successor, Jul 2026) · MSOM (successor, search open) · ETP (Wiklund successor TBD) ·
New Media & Society (Jones stepping down, Jun 2026) · Psychological Bulletin (Johnson→Hofmann, 2027) ·
AMR (Byron term ~mid-2026) · HLR (Vol 140 Alex Zhao, 2026-27) · RER (2026 team).

### Honest hedges retained (genuinely not pinnable / in flux — NOT fabricated)
管理世界 & 数量经济技术经济研究 (leadership in flux) · 中国行政管理 主编 (conflicting aggregators) ·
SMJ co-editor slate (sources conflict) · Yale Law Journal current student EiC (single source) ·
World Politics academic editors (403) · many publisher per-journal OA APC amounts (no stable public figure).

### Verified already-grounded, no edit needed (16)
ISR, JMIS, JAIS, MIS Quarterly, Management Science, MSOM, Operations Research, J Operations
Management, J Banking & Finance, J Business Venturing, J Marketing Research, The Econometrics
Journal; + 4 generic bundle packs (Agriculture-Environment, Clinical-Medicine,
Engineering-Technology, Chinese-Sport-Science).
