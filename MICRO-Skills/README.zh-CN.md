# MICRO Skills

面向 **MICRO（IEEE/ACM International Symposium on Microarchitecture）** 投稿的
12 个 agent skills。MICRO 是微体系结构（microarchitecture）社区的旗舰会议，其
编号谱系可追溯到 1968 年的 microprogramming workshop，是计算机体系结构四大顶会
中最年长的一个。本包覆盖完整的投稿战役：判断机制是否真正"住在机器里面"、构建
带成本核算的模拟器级证据、把论证塞进 11 页且**完全没有附录**的版面、把两周的
rebuttal/revision 窗口用来跑实验而不是措辞，以及把录用转化为带 ACM badge、
同时进入 ACM DL 与 IEEE Xplore 的正式出版记录。

官方依据核验日期：**2026-07-08**。已核验 MICRO 2026（第 59 届）主页、Call for
Papers 与 submission guidelines（`microarch.org/micro59/`）、`micro2026.hotcrp.com`
投稿站点、首届 Industry Track CFP、MICRO 2025 artifact evaluation 页面、SIGMICRO
Test of Time 与 Hall of Fame 页面，以及 ACM DL / IEEE Xplore / dblp 的会议记录。
验证环境中对 `microarch.org` 等站点的直接抓取返回 403，因此官方页面通过搜索引擎
对精确 URL 的渲染读取，并与数字图书馆及 SIGARCH / TCCA 的 CFP 转载交叉核对；完整
证据链与所有仍标注 待核实 的条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 2026 周期此刻的位置（以核验日期为准）

MICRO 2026 的录用通知于 **2026 年 7 月 7 日**发出——正好在本包核验日期的前一天。
本包落在的"实时"工作是：

- **录用论文**：9 月 11 日 camera-ready，artifact evaluation 并行推进，然后是
  雅典现场（10 月 31 日 – 11 月 4 日）。
- **被拒论文**：按季度排布的四会替补格——HPCA 2027 截稿 **2026 年 7 月 24 日**
  （通知后仅 17 天）、ASPLOS 2027 第二轮 9 月 9 日、ISCA 2027 正文 11 月 17 日、
  MICRO 2027 回到四月初档期（具体日期 待核实）。
- **新项目**：现在就该搭评测栈——在这个领域，模拟器、baseline 与 sweep 队列才是
  日程表，写作是便宜的部分。

## 驱动本包建议的会议机制（2026 周期已核验）

- **截止时间用美东时间（EDT），不是 AoE**——摘要 3 月 31 日、正文 4 月 7 日，均为
  11:59 PM EDT；摘要注册是正文提交前一周的硬闸门。
- **11 页正文 + 不限页参考文献 + 完全禁止附录。** 没有补充材料 PDF 这一层：内容
  要么进正文、要么进匿名 artifact 仓库、要么删掉。
- **格式执法是双重的**：人工目检加自动检查，即使通过 HotCRP 格式检查仍可能因
  格式违规被拒。全文最小 9pt、必须带页码、模板几何不可改动。
- **每条参考文献必须列出全部作者**——条目里出现 "et al." 即格式违规，且该规则
  延续到 camera-ready。
- **两周合并的 rebuttal/revision 窗口**（2026 年为 6 月 3–17 日），长到足以补跑
  审稿人要求的实验；双盲义务贯穿全程，且行为规范条款明确覆盖 rebuttal 用语。
- **录用后 artifact evaluation + ACM badges**（2025 模式：Available 徽章要求
  Zenodo 级归档仓库；通过 AE 可免费获得两页 artifact appendix）。
- **首届 Industry Track**，为生产级证据定制了单独的评审流程。

## Skills

| Skill | 作用 |
| --- | --- |
| [`micro-topic-selection`](skills/micro-topic-selection/SKILL.md) | 做"机制驻留测试"（不提软件角色能否说清机制？），在 MICRO、ISCA、HPCA、ASPLOS、DAC/ICCAD、SC、MLSys 与 Industry Track 之间路由。 |
| [`micro-workflow`](skills/micro-workflow/SKILL.md) | 驾驭四月→雅典的周期钟，与按季度排布的四会替补格；倒排计划里评测栈才是关键路径。 |
| [`micro-writing-style`](skills/micro-writing-style/SKILL.md) | 搭四拍论证（characterization → insight → mechanism → accounting），在无附录的 11 页里做预算，让模拟数字始终标明是模拟数字。 |
| [`micro-related-work`](skills/micro-related-work/SKILL.md) | 扫五条文献带（含工业界披露），按结构与成本做差异化，引用前用 dblp 核验 venue 归属。 |
| [`micro-experiments`](skills/micro-experiments/SKILL.md) | 让主张匹配证据阶梯（trace 模型 → cycle-level 模拟 → RTL → FPGA → 硅片），调出产品级 baseline，用 geomean 汇报并做完整开销核算。 |
| [`micro-reproducibility`](skills/micro-reproducibility/SKILL.md) | 用逐 run 的 manifest 钉死模拟器 commit、配置、SimPoint 配方与功耗模型版本，日后直接变成 AE 包。 |
| [`micro-supplementary`](skills/micro-supplementary/SKILL.md) | 为一个**没有附录**的会议做内容分诊：11 页正文、不限页参考文献、匿名仓库，或删除清单。 |
| [`micro-artifact-evaluation`](skills/micro-artifact-evaluation/SKILL.md) | 围绕评审者的时间预算打包模拟 artifact（smoke/key/full 三档入口），处理 SPEC 授权问题，冲三枚 ACM badge。 |
| [`micro-submission`](skills/micro-submission/SKILL.md) | HotCRP 上传前终审：EDT 时钟、摘要闸门、页数与字号底线、全作者参考文献、artifact 链接匿名化或删除。 |
| [`micro-review-process`](skills/micro-review-process/SKILL.md) | 建模四月→七月的评审管线、"方法学取证"式的审稿文化、行为规范，以及 Industry Track 的独立评审。 |
| [`micro-author-response`](skills/micro-author-response/SKILL.md) | 把两周窗口当实验冲刺：给异议分类、补跑缺失实验、用带 manifest 的数字作答。 |
| [`micro-camera-ready`](skills/micro-camera-ready/SKILL.md) | 执行录用后的九周路径：仅增量的去匿名 diff、恢复致谢、与 AE 联动的 artifact appendix、双图书馆出版。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十条官方来源（URL + 2026-07-08 核验日期）、已核验事实清单、事实分级规则与显式的 待核实 登记。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口、书目权威库、兄弟会议日历，以及五道作者侧核验工序。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇 DOI 级核验的 MICRO 论文（1991–2014，其中三篇有 Test of Time 背书）作为贡献形状样板，附已查明的归属陷阱。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构的 dead-block 回收论文摘要与引言，按四拍论证重建，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享可复现工具包的适配器，外加六项通用工具查不出的模拟器/硬件专项检查。 |

## 安装与使用

作为 Claude Code plugin（本目录自带 marketplace manifest，可独立安装）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./MICRO-Skills
claude plugin install micro-skills
```

也可以直接使用文件——每个 `skills/micro-*/SKILL.md` 都是独立的指令文件，
frontmatter 的 description 说明触发时机。典型调用：

- "这篇 prefetcher 论文投 MICRO 还是 ASPLOS？" → `micro-topic-selection`
- "上传 HotCRP 前帮我过一遍 PDF" → `micro-submission`
- "审稿意见到了，窗口周三开" → `micro-author-response`
- "中了——排 camera-ready 和 artifact evaluation" → `micro-camera-ready`

## 包结构

```text
MICRO-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skills）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── micro-<topic>/SKILL.md  # 12 个 skills，一目录一技能
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 2026 周期锚点事实（历史快照，不是永久规则）

- **MICRO 2026 = 第 59 届 · 希腊雅典 · 2026 年 10 月 31 日 – 11 月 4 日。**
- 摘要 3 月 31 日 / 正文 4 月 7 日，均 11:59 PM **EDT**，站点
  `micro2026.hotcrp.com`；rebuttal/revision 6 月 3–17 日；通知 7 月 7 日；
  camera-ready 9 月 11 日。
- 版面：正文 ≤ 11 页（参考文献除外）；**禁止附录**；参考文献不限页且须列全作者；
  全文 ≥ 9pt；必须有页码；使用 MICRO 模板且不得压缩间距；目检 + 自动双重检查。
- 评审：全程双盲；artifact 链接匿名化或删除；投稿阶段不得有致谢；行为规范覆盖
  rebuttal。
- Artifact：录用后 AE + ACM badges（2025 页面已核验，2026 具体安排 待核实）；
  Available 徽章需 Zenodo/FigShare/Dryad 级归档。
- 社区坐标：MICRO Test of Time Award（2025 年授予 3D die-stacking 与 CACTI 6.0
  两篇）、MICRO Hall of Fame（8 篇及以上）、IEEE Micro Top Picks 遴选资格。

## 事实纪律

本包把三类陈述保持可区分：

1. **已核验的 2026 周期事实**——带日期或上限，可追溯到 source map 中的编号来源
   （11 页规则、EDT 截止、六月窗口）。
2. **推导/二手事实**——就地标注（1968 谱系是由第 59 届序号做的算术推断；审稿
   侧重描述是社区规范的综合，不是引用的评审表）。
3. **待核实条目**——只以待解问题的形式出现，绝不当作事实（2026 AE 日程、主席
   名单、camera-ready 页数、参会要求、MICRO 2027 日期）。

若发现任何 skill 把第 2、3 类内容写成第 1 类，按 bug 处理：对照在线官方页面修
正并更新 source map。

## 维护说明

- 本包所有数字都是 **2026 周期快照**。MICRO 每届重新决定版面、日期、track 与
  AE 安排——给下一周期建议前必须重开 `microarch.org/micro<NN>/`；注意 2026 年
  新设了 2025 年不存在的 Industry Track。
- source map 中的 待核实 登记就是债务清单：组织者名单、AE 日历、Industry Track
  截止、rebuttal 机制细节、camera-ready 页数、参会规则与 AI 署名政策。
- 会议领导层逐届轮换，本包任何内容都不应被当作常设编辑政策来引用。
- 新样板论文只能通过
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验
  流程进入——以 DOI 记录为准，不以记忆为准。

## 许可

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
