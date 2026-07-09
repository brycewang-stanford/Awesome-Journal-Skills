---
name: jos-workflow
description: 当你要把投向《软件学报》(Journal of Software, JOS) 的全过程从选题到见刊统筹起来时使用。覆盖从选题定位、中文写作与实验、在线投稿、初审→外审→复审→主编终审的多轮修回、录用后定稿清样直到见刊的完整时间线，说明每一步该调用本包哪个技能、如何倒排计划、如何规避专刊截稿与超期等时序陷阱，帮助你把《软件学报》(Journal of Software) 一次投稿的完整生命周期统筹到位，不遗漏关键环节。
---

# 《软件学报》全流程 (Journal of Software Workflow)

本技能把一次《软件学报》(Journal of Software, JOS) 投稿的完整生命周期串起来，并指明每一步
调用哪个技能。本刊无固定征稿截止（常规通道随时投），但专刊有独立截稿；稿件一般 6 个月内
通知结果（见 [`resources/official-source-map.md`](../../resources/official-source-map.md)）。

## 一、阶段总览

```text
选题定位 → 写作+实验 → 在线投稿 → 初审 → 外审 → 复审 → 修回(多轮) → 主编终审
        → 录用 → 定稿/校样/清样 → 见刊
```

## 二、逐阶段与技能映射

| 阶段 | 做什么 | 调用技能 |
| --- | --- | --- |
| 选题定位 | 判断是否契合本刊、选栏目/专刊 | [`jos-topic-selection`](../jos-topic-selection/SKILL.md) |
| 写作 | 搭中文写作骨架、GB/T 7714 | [`jos-writing-style`](../jos-writing-style/SKILL.md) |
| 相关工作 | 差异优先定位增量 | [`jos-related-work`](../jos-related-work/SKILL.md) |
| 实验 | RQ 契约、基线、统计、威胁 | [`jos-experiments`](../jos-experiments/SKILL.md) |
| 可复现 | 材料与出处锁定 | [`jos-reproducibility`](../jos-reproducibility/SKILL.md) |
| 附录 | 正文/附录切分 | [`jos-supplementary`](../jos-supplementary/SKILL.md) |
| 投稿 | 在线投稿审计 | [`jos-submission`](../jos-submission/SKILL.md) |
| 审稿 | 状态解读与预期 | [`jos-review-process`](../jos-review-process/SKILL.md) |
| 修回 | 逐条答复、修改稿 | [`jos-author-response`](../jos-author-response/SKILL.md) |
| 材料 | 代码/数据可用性 | [`jos-artifact-evaluation`](../jos-artifact-evaluation/SKILL.md) |
| 定稿 | 清样与出版事务 | [`jos-camera-ready`](../jos-camera-ready/SKILL.md) |

## 三、倒排计划（从目标见刊倒推）

- **动笔前（最高杠杆）**：先 topic-selection 定刊/定栏目，避免整轮浪费；若投专刊，锁定截稿。
- **做实验时**：experiments 与 reproducibility 同步进行——威胁有效性在设计期命名、出处在
  采集期锁定，事后无法补。
- **写作时**：writing-style 打磨首页弧线与摘要，related-work 讲清增量。
- **投稿周**：submission 端到端审计格式、摘要、证据、GB/T 7714，再在线提交。
- **投稿后**：review-process 校准预期，author-response 处理每一轮修回。
- **录用后**：camera-ready 定稿清样，supplementary/artifact 收尾材料。

## 四、时序陷阱

- 常规通道随时可投，但**专刊有独立截稿**——错过要等下一次或转常规。
- 稿件一般 6 个月内通知；**超期**可在告知编辑部并获确认后自行处理。
- **修改后再审**可能多轮，预留修改与补实验时间。
- 录用到见刊仍有**排期**，不等于立即出版。

## 五、全流程自检清单

```text
[ ] 选题已判定契合本刊、栏目/专刊已定
[ ] 若投专刊，已确认截稿与特约编辑通道
[ ] 写作完成首页弧线、摘要、GB/T 7714
[ ] 实验证据相称、威胁有效性齐备、材料可复现
[ ] 投稿前完成 submission 审计
[ ] 投稿后按状态链正确解读、按时修回
[ ] 每轮修回逐条答复、多轮一致
[ ] 录用后完成定稿清样与出版事务
```

## 六、输出格式

```text
【当前阶段】选题/写作/投稿/审稿/修回/定稿
【关键动作】此刻应做：________
【调用技能】________
【时序风险】专刊截稿 / 超 6 个月 / 见刊排期：________
【下一步】________
```

## 七、决策路由

- 若"不确定投不投本刊"→ [`jos-topic-selection`](../jos-topic-selection/SKILL.md)。
- 若"稿件已成型要投"→ [`jos-submission`](../jos-submission/SKILL.md)。
- 若"收到修改后再审"→ [`jos-author-response`](../jos-author-response/SKILL.md)。
- 若"已录用"→ [`jos-camera-ready`](../jos-camera-ready/SKILL.md)。
- 若"决定改投"→ 回到 topic-selection 的兄弟刊路由表。

## 七点五、为什么要倒排

《软件学报》(Journal of Software) 的许多环节一旦错过就无法补救，因此必须从目标结果倒排、而
非顺着写。威胁有效性要在实验**设计期**命名，采集完数据再想补往往缺少对照；挖掘类研究的仓库
快照与 commit SHA 要在**采集期**锁定，时过境迁便不可复现；专刊截稿一旦错过，就只能等下一次
征稿或转常规通道，而常规通道又意味着不同的评审聚焦与时间线。把这些"不可逆点"提前标在时间
线上，能避免临投稿才发现材料缺失、或临见刊才发现链接失效。倒排的另一个好处是让写作顺序更
自然：内容最实的方法与实验先写，贡献最清楚时再回头写引言和摘要，全文的一致性也更容易保证。

一个务实的做法是：把本包的十二个技能按阶段贴在项目看板上，每推进一步就回到对应技能核对一次
清单，确保"选题—写作—实验—投稿—审稿—修回—定稿"每个交接处都没有掉链子。

## 八、两条典型路径

**路径 A：常规通道研究论文**

```text
1. topic-selection 判定契合本刊、选研究论文栏目
2. writing-style + related-work + experiments + reproducibility 完成稿件与材料
3. submission 端到端审计后在线投稿
4. review-process 跟踪：初审→外审→复审
5. 若"修改后再审"→ author-response 逐条修回（可能多轮）
6. 主编终审→录用→ camera-ready 定稿清样→见刊
```

**路径 B：专刊（special issue）论文**

```text
1. topic-selection 确认主题落在开放专刊范围内，锁定截稿
2. （如需）在 CCF ChinaSoft 中国软件大会作口头报告
3. 按专刊征稿页与 2021 模板准备稿件，走专刊通道投稿
4. 特约（客座）编辑组织的聚焦评审→修回
5. 录用→ camera-ready 随专刊出版
```

## 九、里程碑核对

```text
[ ] 里程碑1 选题定稿：刊/栏目/（专刊截稿）已定
[ ] 里程碑2 投稿就绪：格式/摘要/证据/材料齐备
[ ] 里程碑3 首次决定：正确解读并规划修回
[ ] 里程碑4 录用：进入定稿清样
[ ] 里程碑5 见刊：链接稳定、勘误流程清楚
```

把这五个里程碑贴在项目看板上，每到一个就回到本表核对，能有效避免《软件学报》(Journal of
Software) 投稿过程中的环节遗漏与时序踩坑。

> 提醒：审稿周期、专刊截稿、见刊排期等属逐稿/逐期而异或 **待核实** 项，请以《软件学报》
> (Journal of Software) 官网、编辑部通知与 CCF ChinaSoft 专刊征稿页为准。
