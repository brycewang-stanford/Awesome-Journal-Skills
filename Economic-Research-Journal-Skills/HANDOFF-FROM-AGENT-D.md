# 交接 / 协作备忘：Agent D → 并行 agent（《经济研究》深度包）

> 写于 2026-06-06。两个 agent 在同一工作树并行打磨本包。本文件把 **Agent D 已联网核实的研究成果**
> 交给正在做结构重建的并行 agent，请在重建时**整合下列已核实事实与纠错**，避免重复劳动与事实错误。
> Agent D 已主动让出「新技能扩展 + `resources/code/` 代码目录」给你（你正在高速构建），不与你争抢。

---

## 一、Agent D 的分工（已落地，未与你冲突）

只动了以下文件，均为「联网核实的事实层 + 互补资源」，**未触碰你正在新建的技能与代码目录**：

- `resources/official-source-map.md` —— **重写为联网核实版**（VERIFIED / 待核实分层，附来源 URL 与访问日期）。
- `skills/er-submission/templates/manuscript_template.md`、`templates/checklist.md` —— **修正参考文献体例事实错误**（见下）。
- `resources/code-templates.md` —— 现代因果推断**命令 + 引文速查**（与你的 `resources/code/*.do` 互补：你给可运行脚本，我给命令出处与引文）。
- `skills/er-identification/SKILL.md` —— 加入**已核实《经济研究》范文** + 现代异质性稳健估计量口径（与你的 `03_did_modern.do` 同一套 CS/SA/dCDH/BJS 工具，互相印证）。

已删除我误建的重复空目录 `er-theory-hypothesis`（你的 `er-theory-hypotheses` 为准）与空 `er-data-sample`。
我的 `er-robustness` 写入被工具拦截 → **你的 `er-robustness` 保留为准**，我不再写。

> 建议你拥有：所有技能正文重写 + 新技能（introduction / reproducibility / robustness /
> theory-hypotheses / reviewer-lens / data-sample…）+ `resources/code/` + README + 清单。
> 我不重写技能正文，避免互相覆盖。下方研究成果请你整合进各技能。

---

## 二、⚠️ 必须修正的事实错误（高优先级）

### 1. 参考文献体例：著者-出版年制，**不是**顺序编码制
原包 `checklist.md`、`manuscript_template.md`、旧 `official-source-map.md` 均误写「顺序编码制」。
**已核实**：《经济研究》用**著者-出版年制（author-year）**。
- 正文夹注：`(作者，年份[，页码])`，如（科斯，1946）；同年多篇 a/b/c；同处多篇分号。
- 文末条目**中文在前、外文在后**，各按拼音/字母排序；**不带 `[1]`、`[J]`、`[M]`**。
- 官方范例：`林毅夫（2007），《潮涌现象与发展中国家宏观经济理论的重新构建》，《经济研究》第1期，第126–131页。`
- 来源：CSSN 官文 + AJCASS 同系刊体例（详见 `official-source-map.md` 第一节第 12 项）。
- **请在你重写的 er-submission / 任何提及引用格式处统一为此口径。**

### 2. 英文梗概字符数「约 4400 字符」官方未证实 → 标 待核实
官文只规定**五要素 + 中文对照**（2017 年起），**未给字符数**。请勿断言 4400；按五要素写。

### 3. 字数/条数/图表/公式硬上限多为「经验值」，官方原文未见 → 加「以投稿当期官网为准」
官方可加载来源中**未见**：正文字数、参考文献 ≤50 条、表≤6/图≤4/图表≤8、公式≤20、引言≥5000 字、
结论≥1500 字、JEL/中图分类号强制。这些很可能源自往年须知，逐年微调。**请勿以官方硬约束口吻断言**，
统一加经验值口径。（详见 `official-source-map.md` 第二节。）

---

## 三、已联网核实的《经济研究》事实（可直接用）

- ISSN 0577-9154；CN 11-1081/F；月刊；1955 创刊；中国社科院经济研究所主办；CSSCI/北核/AMI。
- 主编：黄群慧（建议以当期版权页复核）。
- 投审稿系统：`https://erj.ajcass.com/Admin/user/login`（官文镜像 `jjyj.ajcass.org`）；2018-10 起仅线上。
- 作者 ≤5；恰 1 位通讯作者；每作者署名单位 ≤2、资助课题 ≤2；总课题 ≤ 作者数+2；作者信息**独立页匿名**。
- 中文内容提要约 **300 字**（VERIFIED）。
- 编辑部主页 2025-01-10 改版：经济研究所 `ie.cssn.cn`。

---

## 四、已核实可用范文（exemplars）——务必核对期刊归属

| 论文 | 期号 | 方法/看点 |
| --- | --- | --- |
| 王永钦、董雯《机器人的兴起如何影响中国劳动力市场？》 | 经研 2020(10) | **Bartik/shift-share IV** |
| 张勋、万广华等《数字经济、普惠金融与包容性增长》 | 经研 2019(8)（封面文） | **机制分析范本**：逐层拆渠道 + 群体异质性 |
| 刘生龙、周绍杰、胡鞍钢《义务教育法与中国城镇教育回报：基于断点回归》 | 经研 2016(2) | **清晰制度断点 RDD** |
| 范子英、田彬彬《税收竞争、税收执法与企业避税》 | 经研 2013(9) | **行政断点/准实验 IV** |
| 黄益平等《生产网络视角下的中国经济周期》 | 经研 2024(9) | 现代**宏观/生产网络** |

⚠️ **不要误标为《经济研究》**（实为《管理世界》/《中国工业经济》）：
沪港通（钟覃琳陆正飞，管理世界2018）、产业政策（余明桂等，中国工业经济2016）、
国家高新区（刘瑞明赵仁杰，管理世界2015）、房奴效应（颜色朱国钟，管理世界2013）。

近年选题主轴（2024(6)(9) 目录）：新质生产力、共同富裕、数字经济/数据要素、双碳、央地财政、高质量发展。

---

## 五、机制分析必引：江艇（2022）——弃用三步法/Sobel

**江艇（2022）《因果推断经验研究中的中介效应与调节效应》，《中国工业经济》2022 年第 5 期，第 100–120 页**
（CNKI: GGYY202205006）。核心：中介变量 M 几乎总内生，逐步回归三步法 + Sobel 的 M→Y 段**无因果识别**；
应改为**只可信识别 X→M**（与主回归同一外生冲击）+ **理论驱动的异质性分组**论证渠道。
**请在你的 er-mechanism / er-theory-hypotheses 中以此为标准口径**——机械三步法已是审稿减分项。

---

## 六、已核实的现代因果推断命令（详见 `resources/code-templates.md`）

- 交错 DID：`bacondecomp`（诊断）；主估计 `csdid`(Callaway-Sant'Anna)/`eventstudyinteract`(Sun-Abraham)/
  `did_multiplegt_dyn`(de Chaisemartin)/`did_imputation`(BJS)。
- 平行趋势敏感性：`honestdid`（Rambachan-Roth 2023）+ `pretrends` 功效（Roth 2022）；
  「事前不显著 ≠ 平行趋势成立」。
- IV：`ivreghdfe` + `weakivtest`（Montiel-Olea & Pflueger 有效 F，取代 Stock-Yogo）+ `weakiv`（AR 稳健 CI）+ 必报简约式。
- RDD：`rdrobust` + `rddensity`（Cattaneo-Jansson-Ma 操纵检验）+ 带宽/donut/假断点稳健性。
- 稳健性：`winsor2`、随机化安慰剂(500–1000 次分布检验)、`psmatch2`、`boottest`(wild cluster)、
  `psacalc`(Oster 2019 δ)。

---

## 七、建议（给用户与并行 agent）

1. 两 agent **顺序**而非并行改同一批技能正文最安全：你先完成结构重建，Agent D 之后可在稳定基线上做
   「事实核验 + 引文/范文校对 + 一致性 polish」第二轮（避免实时互相覆盖）。
2. 全包统一参考文献体例为著者-出版年制；删除一切 `[J]/[M]/顺序编码` 痕迹。
3. README/清单/版本号由你统一更新（你在做重建）；Agent D 不动 README 与 manifests，避免冲突。
