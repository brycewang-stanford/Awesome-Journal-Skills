# +100 顶级期刊扩张计划（2026-06，补齐最薄弱学科）

> 用户指令（2026-06-19）：用一个月时间全面提升 repo，新增 **100 个顶级期刊**。
> 方向已拍板：**补齐最薄弱学科**（工程技术 + 农业/环境/地球 + 临床医学专科）；
> 形态统一为 **breadth fit-card**（每刊一张 venue-specific `SKILL.md`，与现有四大合集一致）。

## 0. 为什么是这三类

按 `EXPANSION-PLAN.md` 的 10×100 蓝图衡量，现有 `English-NaturalScience-Journal-Skills`（155 刊）
在三处配额最空：

- **cat 7 工程与技术**：仅 ~17 刊，且集中在材料/能源，缺核心工程旗舰（控制/通信/信号/电力/机械/化工/土木/光电/生医工程）。
- **cat 9 农业与环境**：农学/食品/土壤/作物几乎为 0；地球/环境仅 ~13。
- **cat 6 医学与健康**：有 ~33 刊，但临床**专科**旗舰（专科 JAMA/Lancet 子刊、肾内、呼吸、内分泌、肝病、风湿、放射、麻醉、神经病学等）覆盖薄。

## 1. 三个新建 breadth 合集（对齐蓝图大类）

| 合集目录 | plugin slug | workflow skill | 刊数 | 蓝图大类 |
|---|---|---|---:|---|
| `Engineering-Technology-Journal-Skills` | `engineering-technology-journal-skills` | `en-engtech-journal-workflow` | 40 | cat 7 |
| `Agriculture-Environment-Journal-Skills` | `agriculture-environment-journal-skills` | `en-agrienv-journal-workflow` | 30 | cat 9 |
| `Clinical-Medicine-Journal-Skills` | `clinical-medicine-journal-skills` | `en-clinmed-journal-workflow` | 30 | cat 6 |
| **合计** | | | **100** | |

> 每个合集 = 1 个 pack（`.claude-plugin/plugin.json` + `marketplace.json`），N 张单刊卡 + 1 张 workflow 路由卡。
> 因此 `EXPECTED_PACK_COUNT` 122 → 125；`EXPECTED_SKILL_COUNT` 1984 → 1984 + (100 刊卡 + 3 workflow) = **2087**。

## 2. 反臆造与反克隆铁律（本批同样适用）

- fit-card 只编码**稳定公开事实**：学科、出版社/学会、永久性结构特征（如 IEEE Trans. 的双栏正文、CONSORT/试验注册门槛、Cell STAR Methods 式要求）。
- **禁止**写影响因子、接受率、ISSN、精确字数/版面费/编辑姓名；**禁止**捏造文献引用。
- 具体投稿规定一律**指向官网复核**（official-submission checklist）。
- 每张卡必须 venue-specific：scope / method-evidence bar / house-style / desk-reject / re-route 都要按该刊真实定位写，clone 审计 < 0.90（理想 < 0.75）。

## 3. 名册（可增删）

### 3.1 Engineering-Technology（40）

电气/EECS/信号/通信/控制：
`proceedings-of-the-ieee` · `ieee-transactions-on-automatic-control` · `ieee-transactions-on-information-theory` ·
`ieee-transactions-on-signal-processing` · `ieee-transactions-on-communications` ·
`ieee-journal-on-selected-areas-in-communications` · `ieee-transactions-on-wireless-communications` ·
`ieee-transactions-on-power-electronics` · `ieee-transactions-on-power-systems` ·
`ieee-transactions-on-industrial-electronics` · `ieee-transactions-on-antennas-and-propagation` · `automatica`

机器人/光电/电子/生医工程：
`the-international-journal-of-robotics-research` · `ieee-transactions-on-robotics` · `optica` ·
`light-science-and-applications` · `laser-and-photonics-reviews` · `nature-electronics` ·
`nature-biomedical-engineering` · `ieee-transactions-on-medical-imaging` ·
`ieee-transactions-on-biomedical-engineering` · `biomaterials`

机械/固体/流体/制造/航空：
`journal-of-the-mechanics-and-physics-of-solids` · `international-journal-of-plasticity` ·
`journal-of-fluid-mechanics` · `international-journal-of-machine-tools-and-manufacture` ·
`additive-manufacturing` · `composites-part-b-engineering` · `progress-in-aerospace-sciences`

化工/过程/能源工程：
`aiche-journal` · `chemical-engineering-journal` · `progress-in-energy-and-combustion-science` ·
`journal-of-membrane-science` · `applied-energy` · `journal-of-power-sources` · `energy-storage-materials`

材料工程/土木交通：
`acta-materialia` · `progress-in-materials-science` · `transportation-research-part-b-methodological` ·
`cement-and-concrete-research`

### 3.2 Agriculture-Environment（30）

农业/食品/植物/土壤/作物：
`nature-food` · `nature-plants` · `new-phytologist` · `the-plant-journal` · `annual-review-of-plant-biology` ·
`field-crops-research` · `agriculture-ecosystems-and-environment` · `soil-biology-and-biochemistry` ·
`agronomy-for-sustainable-development` · `food-chemistry` · `trends-in-food-science-and-technology`

环境/可持续/污染：
`global-change-biology` · `environment-international` · `environmental-health-perspectives` ·
`journal-of-cleaner-production` · `resources-conservation-and-recycling` ·
`annual-review-of-environment-and-resources` · `environmental-pollution`

地球/大气/水文/海洋/气候：
`communications-earth-and-environment` · `journal-of-climate` · `earth-system-science-data` ·
`journal-of-hydrology` · `water-resources-research` · `earth-and-planetary-science-letters` · `geology` ·
`global-biogeochemical-cycles` · `agricultural-and-forest-meteorology` ·
`forest-ecology-and-management` · `bulletin-of-the-american-meteorological-society`

### 3.3 Clinical-Medicine（30，避开自然科学合集已覆盖的综合大刊）

JAMA / Lancet 专科子刊：
`jama-internal-medicine` · `jama-oncology` · `jama-cardiology` · `jama-neurology` · `jama-pediatrics` ·
`jama-psychiatry` · `jama-surgery` · `the-lancet-respiratory-medicine` ·
`the-lancet-diabetes-and-endocrinology` · `the-lancet-public-health` · `the-lancet-psychiatry`

专科学会旗舰：
`annals-of-oncology` · `nature-reviews-clinical-oncology` ·
`american-journal-of-respiratory-and-critical-care-medicine` ·
`journal-of-the-american-society-of-nephrology` · `kidney-international` ·
`journal-of-clinical-endocrinology-and-metabolism` · `diabetologia` · `journal-of-hepatology` ·
`hepatology` · `american-journal-of-gastroenterology` · `journal-of-allergy-and-clinical-immunology` ·
`arthritis-and-rheumatology` · `brain` · `stroke` · `radiology` · `anesthesiology` ·
`critical-care-medicine` · `american-journal-of-obstetrics-and-gynecology` · `european-urology`

## 4. 分波交付（每波独立过 gate 后提交）

- **Wave A**：Engineering-Technology 合集（40 刊 + workflow），过 `run_checks.py` + clone 审计 → commit。
- **Wave B**：Agriculture-Environment 合集（30 刊 + workflow）→ commit。
- **Wave C**：Clinical-Medicine 合集（30 刊 + workflow）→ commit。
- 每波结束：bump `audit_repo.py` 的 `EXPECTED_*` tripwire + 根 `README.md`/`README.en.md` 徽章与计数。

## 5. Definition of Done（每个合集）

1. 结构完整：`LICENSE` / `README.md` / `README.zh-CN.md` / `.claude-plugin/{plugin,marketplace}.json` /
   `resources/{source-basis,official-source-map}.md` / `assets/cover.svg` / `skills/*`。
2. `marketplace.json` 的 skills 列表 == 实际 `skills/*/SKILL.md`。
3. 每张卡 frontmatter 仅 `name`+`description`，name==文件夹名，全仓不重名。
4. clone 审计无 ≥0.90 配对；workflow 卡之间不互相克隆。
5. `python3 tools/run_checks.py` 全绿。
6. 根 README 双语 + 计数同步；`audit_repo.py` tripwire 同步。
