# 模拟审稿小组（inline panel）：《数字金融试点与中小企业融资约束》，目标期刊《经济研究》

> 本报告是投稿前的预演（rehearsal），用于预判审稿人的攻击面和可能的决定档位，不能替代真实评审，也不预测录用与否。
> 组织方式：**inline panel**，由同一 agent 依次扮演 AE、R1、R2、R3 和核验人。每份审稿意见写完后才进入下一个视角，但审稿人之间仍可能相互锚定。正文用英文写成（brief 允许）。

## 校准（Calibration）

- **期刊 / 表单：** 《经济研究》（Economic Research Journal），**表单 G（中文社科期刊）**，2026-11-23 校准。依据：`review-forms.md` §G；`Economic-Research-Journal-Skills/resources/official-source-map.md`（2026-11-23 复核：编辑部初审、匿名外审、编辑部终审，作者与审稿人双向匿名；中文提要约 300 字；英文梗概约 4,400 字符且须五要素齐全；著者—出版年制；数据与代码在拟录用后提交）；以及 `er-reviewer-lens`、`er-identification`、`er-robustness`、`er-mechanism`、`er-heterogeneity`、`er-theory-hypotheses`、`er-literature-review`。
- **本刊标准：** 按 `er-reviewer-lens`，审稿意见中最高频也最致命的是「理论定位」（例如「理论贡献到底是什么？这只是一篇政策评估」「没有和本刊近 3 年同主题文章对话」）。识别方面，交错 DID 必须使用异质性稳健估计量，配 Bacon 分解、事前联合检验和 Honest DiD；机制检验按江艇（2022）的口径；异质性的组间差异必须做正式检验。`er-theory-hypotheses` 也写明，文字推演的理论分析是本刊「最主流」的写法，「装饰性模型」反而扣分，所以本组不把「必须有数理模型」当作要求。
- **视角：** R1 识别与方法 · R2 贡献与选题 · R3 规范与稳健性。
- **预检（stage 0）：** 结论为 GO，没有任何 finding（摘要长度、匿名、关键词、引文与文献表对应、图表编号、数字可追溯均通过）。审稿人不再讨论这些机械项。

---

## 一、AE 初审（desk screen）

- **选题与刊物匹配：** 契合。中小企业融资约束和数字金融都在本刊近年的选题主轴「数字经济 / 数据要素」之内，对理解信用基础设施的作用有一般意义。
- **致命缺陷扫描：** 未发现。识别设计按当前标准完整：CS 双重稳健估计量为主，配 SA、BJS、尚未处理组、Bacon 分解、事前联合检验（p = 0.78）、Rambachan–Roth、随机化推断，标准误聚类到城市层面。各处数字可复算（14.7%、12.6%、6.0%，Bacon 加权和 0.031，城市×年份 = 3,080）。
- **初审要留意的地方：** 一是贡献表述偏向「政策评估加估计量比较」，理论推进写得薄；二是正文（含表）约 1.0 万字，低于本刊的经验篇幅（1.5–2.5 万字，属经验值，不是官方硬限）。
- **决定：** **送外审。** desk-reject 风险**低**。

---

## 二、外审意见（表单 G）

### 审稿人 1：识别与方法

| 表单 G 项目 | 评价 |
|---|---|
| 1. 选题价值与问题意识 | 良：问题重要；识别出发点（区域指数内生）表述清楚 |
| 2. 创新性与理论贡献 | 中上（主要由 R2 评价） |
| 3. 研究设计与识别 | **优**：CS（never-treated）为主，以 not-yet-treated、SA、BJS 交叉验证；Bacon 分解；事前联合检验；Honest DiD（M̄ = 1 时 CI 为 [0.017, 0.073]，breakdown M̄ = 1.7）；预期效应检验；1,000 次随机化推断；城市层面聚类，CS 用乘数 bootstrap |
| 4. 数据与变量 | 良：样本筛选规则清楚；Cost 变量的样本定义需要讨论（见 M2） |
| 5. 规范与写作 | 良 |

**一句话概括：** 文章利用分三批（2015、2017、2019；共 82 个城市）推进的数字金融服务试点和 38,642 家中小企业的面板数据，用异质性稳健 DID 估计出获贷概率提高 4.6 个百分点、融资成本下降 0.41 个百分点。

**主要意见（Major）**

- **R1-M1：同期的信用体系类政策没有控制。** §五（二）表 3 第（2）列只控制了「宽带中国」和智慧城市试点（第 170 行）。与本文试点内容最接近的混杂来源，是同样建设企业信用信息平台或推动普惠信贷的政策，例如社会信用体系建设示范城市和普惠金融改革试验区等。这类政策如果与三个批次在时间和城市上重叠，事前检验和随机化推断都无法排除，因为混杂冲击与处理同时发生。*修改建议：* 逐一列出与 82 个试点城市重叠的信用和金融类试点，加入控制或剔除重叠城市后重新估计；报告重叠城市的比例。*Owner：* `er-robustness`（同期政策排除），`er-identification`。
- **R1-M2：融资成本（Cost）只对有息负债为正的企业定义，存在处理后选择。** §三（三）第 89 行及表 2 Panel C（N = 201,577）。试点提高了获贷概率，新进入 Cost 样本的是以前无贷款记录的边际借款人，样本构成因处理而改变，所以 −0.41 不是同一批企业的价格效应。*修改建议：* 在处理前后都有有息负债的固定样本上重估；或报告 Lee bounds；或分开估计「已有借款企业」的利率变化。*Owner：* `er-data-sample`、`er-robustness`。
- **R1-M3：从未处理组由没有申报的城市组成，存在自选择。** 第 79–81 行：试点「地方申报、分批评审」，198 个从未处理城市可能与试点城市系统性不同。*修改建议：* 补充批次时点对基期信贷趋势的回归，证明申报时点与处理前融资趋势无关。*Owner：* `er-identification`。

**次要意见（Minor）**：(a) 机制变量 Info 的定义需要澄清：非试点城市是否也有「地方信用信息平台」？如果平台只在试点后才存在，D→Info 带有机械性（样本均值 0.384 显示非试点城市也有记录，请说明来源）。(b) 表 2 第（1）列 TWFE 含「基期协变量×年份」且为非平衡面板，Goodman-Bacon 分解的标准形式要求平衡面板、无协变量，请说明 21.4% 是基于哪个设定计算的。(c) 第（2）至（5）列标注「企业固定效应：是」，对 CS 和 BJS 来说这一表述不确切，建议改为「个体层面差分 / 插补」。(d) 请报告 CS 主估计中各批次的 ATT(g)，以便判断 2019 批次（只有 3 期处理后数据）的权重。

**我对编辑的建议（confidential）：** 识别部分达到本刊上乘水平。M1、M2 是必须补的稳健性检验，补齐后不改变结论的可能性较大。建议修改后再审或小修。

### 审稿人 2：贡献与选题

| 表单 G 项目 | 评价 |
|---|---|
| 1. 选题价值与问题意识 | 良：问题对中国中小企业金融有直接意义 |
| 2. 创新性与理论贡献 | **中**：三条贡献都是经验或方法层面的，理论推进没有写出来；与最接近的准实验文献缺少对话 |
| 3. 研究设计与识别 | 优（不在本人重点范围内） |
| 4. 数据与变量 | 良：企业层面的征信面板是一个实在的优势 |
| 5. 规范与写作 | 良：文献综述偏短，最新文献不足 |

**主要意见（Major）**

- **R2-M1：理论贡献和文献定位不足，相对最接近文献的增量被高估。** 有三处体现。(i) §一 第 51 行的三条边际贡献分别是「企业层面因果证据」「比较多种估计量、量化 TWFE 偏误」「用江艇（2022）的方法区分渠道」，没有一条说明本文在信贷配给或信息不对称理论上推进了什么。按 `er-reviewer-lens`，这正是本刊最高频、最致命的「这只是一篇政策评估」式质疑。「量化 TWFE 偏误」是计量层面的观察，不构成对经济学的贡献。(ii) §二（二）（三）第 61–73 行直接列出 H1–H3，没有推演出彼此对立、可以区分的预测（`er-theory-hypotheses`：好的理论分析会主动提出对立预期并说明如何区分）。信息渠道和竞争渠道都只预测「某组效应更强」。(iii) 相对最接近的文献，增量没有被检验。第 45 和 63 行把现有研究概括为基于地区指数的相关性证据，但用政策试点做 DID、研究信用信息基础设施与企业融资的国内准实验文献（例如以社会信用体系建设示范城市等批次试点为冲击的研究）没有被引用或讨论。参考文献中，2022 年以后没有任何一篇中文文献，本刊近 3 年的同主题文章也一篇都没有引用。*修改建议：* 重写贡献段，把发现提到理论层面，例如说明信息硬化在什么条件下替代关系型信贷，以及价格配给与数量配给的不同预测；在 §二 推出能区分信息渠道与竞争渠道的对立预测（如对利率与对贷款数量的不同影响）；补齐与准实验文献和本刊近 3 年同主题文章的比较。*Owner：* `er-introduction`、`er-theory-hypotheses`、`er-literature-review`。
- **R2-M2：「区分信息渠道与竞争渠道」的说法与证据不一致。** H3 写的是「加剧地区信贷市场竞争」（第 73 行）。§六（二）第 196 行把结果解释为「数字信贷对原有信贷供给的补充作用」。引言第 49 行又写成「关系型信贷替代空间更大的城市」，这其实是信息渠道的解释。结论第 224 行则写「通过补充信贷供给发挥作用」。银行集中度高的城市效应更强，这一结果同样符合信息渠道。所以摘要和贡献中「区分两条渠道」的说法偏强。*修改建议：* 统一 H3 的表述，补一个直接的竞争检验（如试点后在位银行的贷款利率或市场份额变化），或把表述降为「两条渠道均有证据」。*Owner：* `er-mechanism`、`er-theory-hypotheses`。

**次要意见（Minor）**：(a) 制度背景（§三（一））应写明试点的政策文件名称和文号，以便读者核对批次与城市名单（匿名期间可放附录）。(b) 政策含义（§七（二））写得克制、落在「意义层」，值得肯定；第三条「数据开放与隐私保护」与本文证据关系较弱，可以压缩。(c) 正文偏短，建议把批次 ATT(g)、样本筛选流程等补入附录。

**我对编辑的建议：** 实证可信度高，但作为《经济研究》论文，理论定位和文献对话需要明显加强。建议修改后再审。

### 审稿人 3：规范与稳健性

| 表单 G 项目 | 评价 |
|---|---|
| 1. 选题价值与问题意识 | 良 |
| 2. 创新性与理论贡献 | 中上 |
| 3. 研究设计与识别（稳健性、推断） | 良：稳健性组合完整；**表 4 Panel C 组间差异的推断有误**（见 M1） |
| 4. 数据与变量 | 良：数据可得性说明规范，附匿名代码仓库 |
| 5. 规范与写作 | 良：英文梗概约 4,390 字符、五要素齐全，并有中文参照；文献体例与本刊官方范式有出入（见次要意见） |

**主要意见（Major）**

- **R3-M1：表 4 Panel C 组间差异的标准误不可能成立，支持 H3 的显著性很可能是计算错误造成的。** 表 4 Panel C 中，高集中度城市的系数为 0.059（SE 0.015），低集中度城市为 0.033（SE 0.012），报告的组间差异为 0.026（SE 0.012，p = 0.030，第 196、210–212 行）。分组按「基期城市银行业集中度中位数」划分，两组是**互不重叠的城市集合**，而标准误聚类在城市层面、组间差异的 SE 用城市整群 bootstrap 计算（表注第 214 行）。两组估计因此相互独立，差异的 SE 应约为 √(0.015² + 0.012²) ≈ 0.019，并且不可能小于较大一组的 0.015。按 0.019 计算，z ≈ 1.35，p ≈ 0.18，在常规水平上不显著。作者在 §六（三）第 218 行处理东部与中西部这对同样互不重叠的分组时，算法是正确的（0.013 与 0.017 合成 0.021），所以 Panel C 与之前后不一致。Panel B 的两组企业分布在相同城市中，存在正相关，SE 为 0.012 尚可成立，但也请给出计算方法。这个问题直接关系到 H3、摘要中「银行业集中度较高的城市更强」的说法，以及结论和政策含义的第二条。*修改建议：* 用合并样本加交互项（D × 高集中度）在城市聚类下估计差异，或在同一次城市 bootstrap 中同时重抽两组；如果差异不显著，就把 H3 改为「未获显著支持」，并相应修改摘要、贡献和政策含义。*Owner：* `er-heterogeneity`（组间差异检验）、`er-mechanism`。
- **R3-M2：有一条参考文献无法核实。** 第 61 和 256 行引用的「周文斌、陈立新（2021），《示例经济评论》第 3 期」，期刊名看上去像占位符（「示例」）。本刊要求引用「真实完整确切」，对造假的处理是中止评审（source map 第 12、16 条）。*修改建议：* 核实后替换为真实文献，或者删除。*Owner：* `er-literature-review`、`er-submission`。

**次要意见（Minor）**：(a) 文末参考文献格式应改为本刊官方范式。中文文献用「作者，年份：《题名》，《刊名》第x期。」，现稿写作「郭峰……（2020），《……》，……第1401-1418页」。外文文献用「Amiti, M., O. Itskhoki, and J. Konings, 2014, "Title", Journal, 104(7), 1942—1978.」样式，现稿写作「Baron, Reuben M. & David A. Kenny (1986). Title. …」（`er-style`）。(b) 正文中两位外文作者的引用，范本写作「A & B（年份）」，现稿用「and」，请统一。(c) 随机化推断建议同时给出按批次分层的置换结果。(d) 剔除 2020—2022 年后，2019 批次只剩试点当年的数据，请在表注中说明这对汇总权重的影响。(e) 篇幅偏短（正文含表约 1.0 万字），可适当扩充机制和异质性的讨论（经验值，非官方硬限）。

**我对编辑的建议：** 稳健性组合完整，但 Panel C 的推断错误会改变 H3 的结论，必须更正后再审。

---

## 三、核验（verifier，不是审稿人之一）

| ID | 意见 | 判定 | 理由（引文） |
|---|---|---|---|
| R1-M1 | 同期信用和金融类政策未控制 | **downgraded** | 属实但已部分回应。第 170 行写「第（2）列控制同期实施的'宽带中国'示范城市和智慧城市试点政策」，说明文章已有同期政策检验框架，剩下的只是扩充政策清单。正文没有证据显示这些政策与试点重叠。列为「必须补」的次要意见。 |
| R1-M2 | Cost 存在处理后选择 | **downgraded** | 属实（第 89 行「仅对有息负债为正的企业定义」，Panel C N = 201,577），但只涉及次要结果。获贷概率这一主结果不受影响，补一个固定样本或 Lee bounds 即可。降为次要意见。 |
| R1-M3 | 从未处理组自选择 | **dropped** | 已被回应：第 81 行明确依赖条件平行趋势；表 2 第（3）列改用尚未处理组，结果为 0.045；§五（一）给出 Honest DiD，breakdown M̄ = 1.7；表 3 第（6）列允许预期效应；第 232 行在局限中说明了外推边界。批次时点回归属于锦上添花。 |
| R2-M1 | 理论贡献与文献定位不足 | **kept** | 属实：第 51 行三条贡献都是经验或方法层面的，「量化了传统TWFE在此类政策评估中的偏误」也被列为贡献；第 69–73 行 H1–H3 直接列出，没有对立预测；参考文献中 2022 年以后没有中文文献，也没有准实验同类文献。具体：§一、§二、文献表。可修改：重写贡献段和 §二，补充文献对话。按本刊最高频的理论定位标准，这一点会影响决定。 |
| R2-M2 | 渠道区分的说法偏强 | **downgraded** | 属实：第 73 行（竞争）、第 196 行（补充供给）、第 49 行（关系型信贷替代）表述不一致。但结论第 224 行只主张两条渠道都在起作用，Panel A 的两个机制变量也都有变化，问题主要在措辞。实质性的推断问题已由 R3-M1 覆盖，这里降为次要意见。 |
| R3-M1 | 表 4 Panel C 组间差异 SE 不成立 | **kept** | 属实：表 4 中「高于中位数 0.059***（0.015）」「低于中位数 0.033***（0.012）」「组间差异 0.026**（0.012）」；表注写明「组间差异的标准误由城市层面整群自助法」得到；分组变量是城市层面的基期集中度，两组城市互不重叠，因此 SE(diff) ≥ 0.015，约为 0.019，p ≈ 0.18。第 218 行的同类计算是正确的（0.021），可作对照。具体：表 4 Panel C、第 196 行、摘要、H3。可修改：重算后据实改写。 |
| R3-M2 | 参考文献无法核实 | **downgraded** | 属实（第 256 行「《示例经济评论》」），但只是 §二（二）里的一条辅助引文，不影响任何结论。投稿前必须核实或删除，按次要意见中的必改项处理。 |

合计：7 条主要意见 → **kept 2 · downgraded 4 · dropped 1**。

---

## 四、AE 综合意见（输出格式：`rt-simulated-referee`）

```text
【Venue / family】《经济研究》/ form G (calibrated 2026-11-23, pack source map re-verified 2026-11-23)
【Desk-screen】送外审：选题契合本刊数字经济主轴，识别设计完整，无致命缺陷；desk-reject 风险低
【Referee forms】R1 识别与方法：研究设计与识别 优，建议修改后再审或小修 · R2 贡献与选题：创新性与理论贡献 中，建议修改后再审 · R3 规范与稳健性：表 4 Panel C 推断错误，建议修改后再审
【Verification】7 concerns → kept 2 · downgraded 4（同期信用政策、Cost 选择、渠道措辞、可疑文献，均为必改次要项）· dropped 1（从未处理组自选择已由尚未处理组、Honest DiD、预期效应检验回应）
【Decision band】修改后再审（大修）
【Decisive issues (1–3)】
  1. 表 4 Panel C 组间差异 SE 不成立（R3-M1）：两组城市互不重叠，SE(diff) 应约为 0.019 而非 0.012，p 约为 0.18，H3 及摘要、结论中的「集中度更高的城市效应更强」可能不成立。
     Owner: er-heterogeneity + er-mechanism. Fix: 合并样本加交互项、城市聚类，或在同一次城市 bootstrap 中联合重抽；据实改写 H3、摘要、贡献第三条和政策含义第二条。
     Execution bridge: StatsPAI `callaway_santanna`（交互或分组）→ city-cluster bootstrap of the difference.
  2. 理论贡献与文献定位（R2-M1）：三条贡献都是经验或方法层面的；H1–H3 缺少可区分的对立预测；没有与准实验同类文献及本刊近 3 年同主题文章对话。
     Owner: er-introduction + er-theory-hypotheses + er-literature-review. Fix: 把贡献提到信贷配给和信息硬化的理论层面；在 §二 推出信息渠道与竞争渠道对价格和数量的不同预测，并用 Cost 与 Loan 的对比检验；补齐文献比较；把「量化 TWFE 偏误」移出贡献列表。
【Secondary issues】同期信用和金融类试点的控制（必补，表 3 第（2）列扩充）· Cost 的固定样本或 Lee bounds · H3 措辞（竞争 vs 补充 vs 信息）统一并补直接竞争检验 · 核实或删除「《示例经济评论》」文献 · Info 变量是否带机械性 · Bacon 分解的适用设定 · 批次 ATT(g) · 文献体例改为本刊官方范式 · 篇幅（经验值）。
【Author action plan】
  1. 重算表 4 Panel C 的组间差异（er-heterogeneity）；如果不显著，同步修改 H3、摘要、引言第 49 行、结论和政策含义（er-mechanism, er-abstract）。
  2. 补同期信用和金融类政策检验，以及 Cost 固定样本或 Lee bounds（er-robustness, er-data-sample），走 StatsPAI 执行桥并审计。
  3. 重写贡献段和 §二 理论推演，补入准实验与本刊近 3 年同主题文献（er-introduction, er-theory-hypotheses, er-literature-review）。
  4. 核实全部参考文献，按官方范式统一文末格式（er-literature-review, er-style, er-submission）。
【Calibration caveats】inline panel，审稿人之间可能相互锚定。决定档位主要由 R3-M1 推动：如果作者能证明 Panel C 的 SE 来自正确的联合 bootstrap（例如分组实际上并非按城市划分），这一条会被撤销，剩下的理论定位问题在本刊仍常见于「修改后再审」，但也可能被编辑视为「修改后录用」级别。识别部分本身达到本刊上乘水平。篇幅、文献条数等只有经验值，官方没有硬限。
```

```json
{"decision_band": "修改后再审（大修）/ major revision", "kept_major_concerns": [{"id": "R3-M1", "lens": "规范与稳健性 (inference/robustness)", "location": "表4 Panel C (lines 196, 210-214); also abstract, H3 line 73, conclusion line 224", "concern": "The between-group difference for high vs low bank-concentration cities reports SE 0.012, but the two groups are disjoint city sets with city-clustered/bootstrapped SEs of 0.015 and 0.012, so the difference SE must be about 0.019 (p≈0.18), meaning the evidence for H3 and the 'stronger in concentrated cities' claim is likely spurious."}, {"id": "R2-M1", "lens": "贡献与选题 (contribution)", "location": "§一 line 51; §二 lines 57-73; reference list", "concern": "All three claimed contributions are empirical or econometric (including 'quantifying TWFE bias'), the hypotheses lack distinguishing rival predictions, and the paper does not engage the closest quasi-experimental Chinese literature or any recent 经济研究 work, so the theoretical contribution is not established to this journal's bar."}], "downgraded": [{"id": "R1-M1", "lens": "识别与方法 (identification)", "location": "表3 col (2), line 170", "concern": "Concurrent credit-system / inclusive-finance pilots not controlled; the paper already runs a concurrent-policy check, so this is a must-do extension."}, {"id": "R1-M2", "lens": "识别与方法 (identification)", "location": "§三(三) line 89; 表2 Panel C", "concern": "Cost is defined only for firms with interest-bearing debt, creating post-treatment selection for a secondary outcome; needs a fixed sample or Lee bounds."}, {"id": "R2-M2", "lens": "贡献与选题 (contribution)", "location": "lines 49, 73, 196, 224", "concern": "H3 framed as competition but interpreted as supply complement or relationship-lending substitution; wording overclaims channel separation."}, {"id": "R3-M2", "lens": "规范与稳健性", "location": "lines 61, 256", "concern": "Reference to 《示例经济评论》 looks like a placeholder and must be verified or removed."}], "dropped": [{"id": "R1-M3", "lens": "识别与方法 (identification)", "location": "§三(一) lines 79-81", "concern": "Never-treated cities self-selected by not applying; already answered by conditional PT, the not-yet-treated control (0.045), Honest DiD (breakdown M̄=1.7) and the anticipation check."}]}
```
