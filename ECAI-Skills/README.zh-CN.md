# ECAI 技能包

面向投稿 **ECAI（欧洲人工智能会议，European Conference on Artificial Intelligence）** 的十二个智能体技能。
ECAI 是 **EurAI（欧洲人工智能协会）** 及其成员国家学会的综合性 AI 旗舰会议。本技能包覆盖一次 ECAI 投稿的完整
链路：判断课题是否适合 ECAI，还是更适合 IJCAI、AAAI、AAMAS、KR 或纯机器学习会议（以及应投主赛道还是同场举办的
**PAIS** 应用赛道）；构建能经受广泛评审池检验的证据——理论贡献给出证明，实证贡献给出公平比较；在
**双盲**、**先摘要后全文的两阶段截止**流程中，把论文压进紧凑的 **7 页正文**；应对
**单轮评审 + 摘要初筛（summary reject）+ 一次 rebuttal**（没有期刊式的 major revision 修回轮）；
并交付 **开放获取（open access）** 的相机就绪版（camera-ready）。

官方信息核对日期 **2026-07-09**：IJCAI-ECAI 2026 征稿与重要日期页、ECAI 2024/2023 独立版征稿页、
IOS Press **FAIA** 论文集卷、`eurai.org` 与 dblp。核验环境屏蔽了会议与出版商域名的直接访问，因此官方页面通过
搜索引擎对精确 URL 的渲染读取，并在 ≥2 个来源间交叉核对（IJCAI-ECAI 2026 页面、`ecai2024.eu`、IOS Press FAIA、
researchr、EurAI、AIhub、dblp）；完整证据链（含所有仍标注 待核实 的项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> **本届最关键的事实：** ECAI 2026 **不是**独立会议，而是与 IJCAI 合办的 **IJCAI-ECAI 2026**
>（德国不来梅，2026 年 8 月 15–21 日），采用 IJCAI 的流程、模板与开放获取论文集。ECAI 的**常态身份**——
> IOS Press FAIA、`ecai.cls` 模板、同场 PAIS 赛道——将在下一届独立版回归。多个技能都取决于先判断目标届次
> 处于**哪种模式**。
>
> 名称混淆提醒：此处 **FAIA** 指 IOS Press 的 *Frontiers in Artificial Intelligence and Applications*
> 丛书，**不是** *Federated AI Meeting（FAIM）*；**ECCAI** 是 **EurAI** 的旧名（2015 年更名）。

## ECAI 与同类会议的不同之处

以下会议机制驱动了技能中的大部分建议，也是从 ML 会议、软件工程会议或期刊转投而来的作者最容易犯错之处：

- **由 EurAI 主办的综合性 AI 旗舰。** ECAI 覆盖符号推理、知识表示（KR）、规划、搜索、多智能体系统、机器学习与
  应用——评审池**广**，因此贡献必须对一般 AI 读者可读，而非仅限某个细分方向。
- **丛书式开放获取论文集（IOS Press FAIA）。** 独立版 ECAI 发表于 **FAIA**（开放获取、无 APC 版面费），使用
  **`ecai.cls`** 模板——**不是** ACM `acmart`，**不是** IEEE `IEEEtran`，**不是** LNCS。这是真正的格式差异点。
- **紧凑的 7 页正文。** 送审论文正文 **7 页**；参考文献是唯一溢出区（独立版 1 页，IJCAI-ECAI 2026 为 2 页）。
  论文内没有无限附录。
- **先摘要后全文的两阶段截止。** 摘要/注册截止约早于 PDF 一周；已注册摘要驱动评审竞标。
- **单轮双盲评审 + rebuttal，且无修回轮。** 先有摘要初筛，再有一次作者答复窗口，最终 accept/reject。
  **没有 Major Revision 兜底**，因此提交时论文必须已经完整。
- **PAIS 应用赛道。** 同场举办的 **Prestigious Applications of Intelligent Systems** 会议是 ECAI
  面向真实部署应用的归属（独立版）。
- **没有 ACM/IEEE 制品徽章。** 可复现性由同一批评审者从论文与匿名补充材料中就地判断——没有单独的徽章委员会或
  制品截止日。
- **本届与 IJCAI 合办。** ECAI 2026 = IJCAI-ECAI 2026（不来梅），采用 IJCAI 流程、`ijcai.sty`、7+2 页预算
  与 IJCAI 自有开放获取论文集。

## 技能列表

| 技能 | 作用 |
| --- | --- |
| [`ecai-topic-selection`](skills/ecai-topic-selection/SKILL.md) | 在 ECAI 与 IJCAI/AAAI/AAMAS/KR/ML 会议之间、以及主赛道与 PAIS 之间选路，用贡献形态、模型替换检验与 2026 合办现实判断。 |
| [`ecai-workflow`](skills/ecai-workflow/SKILL.md) | 从全文截止日倒推整年计划：摘要注册、摘要初筛、rebuttal、通知、开放获取相机就绪。 |
| [`ecai-writing-style`](skills/ecai-writing-style/SKILL.md) | 为一般 AI 读者搭首页论证弧，在紧凑 7 页正文内让证据与主张匹配。 |
| [`ecai-related-work`](skills/ecai-related-work/SKILL.md) | 覆盖符号/学习/多智能体/应用各条线，delta 优先定位，自引保持双盲，控制在 1–2 页参考文献预算内。 |
| [`ecai-experiments`](skills/ecai-experiments/SKILL.md) | 按主张形态在证明与实验间取舍，公平基线、随机种子与波动、诚实消融、固定溯源。 |
| [`ecai-reproducibility`](skills/ecai-reproducibility/SKILL.md) | 就地构建可复现叙事：理论给完整证明附录，实证给固定种子与缓存输出的包，并匿名补充材料。 |
| [`ecai-supplementary`](skills/ecai-supplementary/SKILL.md) | 按“判定关键性”切分内容——凡评审判定论文所需，皆不得置于 7 页正文之外。 |
| [`ecai-submission`](skills/ecai-submission/SKILL.md) | 终审：两阶段截止、正确的模板/出版模式、7 页预算、双盲清查、每作者投稿上限、桌拒风险分诊。 |
| [`ecai-review-process`](skills/ecai-review-process/SKILL.md) | 建模流程——双盲、摘要初筛、领域主席、一次 rebuttal、无修回的 accept/reject——并找出作者可施力之处。 |
| [`ecai-author-response`](skills/ecai-author-response/SKILL.md) | 写唯一一次、简短、双盲的答复：纠正事实误读、补上被点名缺失的证据。 |
| [`ecai-artifact-evaluation`](skills/ecai-artifact-evaluation/SKILL.md) | 在没有 ACM/IEEE 徽章赛道的前提下规划可复现资产——证明附录或可运行包，由评审就地判定。 |
| [`ecai-camera-ready`](skills/ecai-camera-ready/SKILL.md) | 按模式交付开放获取相机就绪版：IOS Press FAIA（`ecai.cls`）或 IJCAI 论文集（`ijcai.sty`）。 |

## 资源

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十二个带 URL 与访问日期的来源；两种模式下经核验的 2026 事实；访问方式说明；显式 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | IJCAI-ECAI 2026 与独立版 ECAI 的官方入口，及网关屏蔽时的交叉核对来源与作者侧核查项。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经网络核验的 ECAI/PAIS 杰出论文，覆盖五种贡献形态，附自检问题与同类会议混淆防护。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构“规划+学习”论文的摘要与引言按 ECAI 论证弧改写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享可复现工具的适配说明，以及通用工具无法完成的 ECAI 专有检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是带有自身 marketplace 清单的自包含插件）：

```bash
# 在仓库克隆中执行
claude plugin marketplace add ./ECAI-Skills
claude plugin install ecai-skills
```

或直接使用文件：每个 `skills/ecai-*/SKILL.md` 都是独立指令文件，其 frontmatter 的 `description`
告诉智能体何时触发。典型调用：

- “这是 ECAI 的论文，还是该投 IJCAI/AAAI/AAMAS？” → `ecai-topic-selection`
- “按 ECAI / IJCAI-ECAI 2026 规则审我的稿” → `ecai-submission`
- “进入 rebuttal 窗口了——规划作者答复” → `ecai-author-response`
- “准备开放获取的 FAIA/IJCAI 相机就绪版” → `ecai-camera-ready`

## 2026 周期锚定事实（历史快照，非永久规则）

- **ECAI 2026 即合办的 IJCAI-ECAI 2026：** 德国不来梅，**2026 年 8 月 15–21 日**；第 35 届 IJCAI 与 ECAI
  在 EurAI 下合办（DFKI、U Bremen Research Alliance、德国信息学会 GI 参与）。摘要 **2026-01-12**，
  全文 **2026-01-19**（AoE）；摘要初筛通知 **2026-03-04**；作者答复 **2026-04-07 至 04-10**；
  通知 **2026-04-29**。正文 **7 页 + 2 页参考文献**（可选伦理声明）；模板 **`ijcai.sty`**；每作者上限 **8**；
  **IJCAI 开放获取论文集**。2026 年对应的 ECAI 届次序号 **待核实**。
- **ECAI 常态身份（独立版，如 ECAI 2024，第 27 届，圣地亚哥-德孔波斯特拉）：** IOS Press **FAIA**
  （ECAI 2024 = 第 392 卷）、**`ecai.cls`**、**7 页 + 1 页参考文献**、先摘要后全文两阶段、同场 **PAIS** 赛道
  （PAIS 2024 = 第 13 届）。
- 治理方：**EurAI**；开放获取、**无 APC**；评审为**双盲、单轮带 rebuttal**（无 Major Revision）。

## 事实纪律

本技能包区分三类陈述，并在技能中保持其可辨识：

1. **经核验的 2026 事实** —— 带日期/预算并追溯到来源图中的编号来源（如 IJCAI-ECAI 2026 日期与 7+2 预算、
   ECAI 2024 的 FAIA 第 392 卷、PAIS 同场）。
2. **转述事实** —— 仅经二手渲染读取并如实标注（如具体组织者名单、作为背景给出的录用数据）。
3. **核验时不可确证项** —— 显式标注 待核实（如 2026 的 ECAI 届次序号、ECAI 2025 细节、合办年是否有应用赛道
   替代 PAIS、各届补充材料机制）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为缺陷，须对照官方页面修正。

## 维护说明

- 上述每个日期与预算都是**周期快照**。ECAI 每届重定其结构——尤其是**独立版（FAIA/`ecai.cls`/PAIS）还是与
  IJCAI 合办**（IJCAI 论文集/`ijcai.sty`）——故先确认模式，再谈其余。
- ECAI 无常任主编、无 APC；组织者每届在 EurAI 下轮换。
- 增补范例论文时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程——
  熟悉的方法或作者并不证明其为 ECAI（而非 IJCAI/AAAI/AAMAS/KR）发表。

## 许可

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
