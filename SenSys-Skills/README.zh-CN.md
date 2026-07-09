# SenSys Skills

面向 **SenSys —— ACM/IEEE International Conference on Embedded Artificial Intelligence and
Sensing Systems** 论文的 12 个 agent skills。SenSys 是 SIGMOBILE 体系下的旗舰会议，强调传感系统
的设计、实现，以及**在真实硬件与真实能量预算下的测量**。本包按 SenSys 实际的投稿流程组织，而这套
流程如今与所有兄弟会议都明显不同：从 2026 年起，SenSys **合并**了 IPSN 与 IoTDI，覆盖低功耗联网
传感、嵌入式系统、IoT 与端上 / 嵌入式 AI；采用**双截止日期、各自独立评审**的模型，第一截止日期被拒
的论文只有带**实质性修订**才能在第二截止日期重投；其证据标准用平台的语言书写——**每次操作的能耗、
占空比、端上延迟与内存、传感 ground truth、以及长期部署**。

官方依据核验日期：**2026-07-09**。已核验 `sensys.acm.org`（2026 与 2027）的主页与 Call for
Papers、各届 HotCRP 站点、SenSys artifact-evaluation 与 Test-of-Time 页面，以及 dblp /
ACM Digital Library（用于 exemplar 核验）。在核验环境中，直接抓取 `sensys.acm.org`、
`hotcrp.com`、`dblp.org` 均返回 **HTTP 403**，因此以下每条事实都通过搜索引擎对官方 URL 的渲染
读取并交叉核对；完整证据链（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## SenSys 与兄弟会议的不同

以下机制已按 2026 届与开放中的 2027 周期核验，驱动了大部分 skill 建议，也是从单截止日期会议或
ML / 理论会议转来的作者最常踩的坑：

- **合并后的更宽口径。** 从 2026 年起，SenSys、**IPSN**、**IoTDI** 合并为一个旗舰会议，定名
  *Embedded Artificial Intelligence and Sensing Systems*。过去分散在三份 CFP 的选题如今集中到
  一处——但评审文化仍是 systems-first：贡献必须**被实现并被测量**，而不是只做仿真或跑 benchmark。
- **每周期两个截止日期，各自独立成轮。** SenSys 设两个投稿截止日期，各自完整评审。第一截止日期被
  拒的论文只有携带**实质性修订与一份 "Response to Reviewers"**（把每条意见映射到具体改动）才能进入
  第二截止日期——重投是契约，而非换层漆。
- **能耗是头号指标。** SenSys 评审要求能耗/功耗配有**明确的测量方法**——source-meter、分流电阻或
  power monitor，标明采样率与 wake/sleep 边界——而不是 "lightweight"、"low-power" 这类形容词。
- **证据是物理的、部署的。** 真实 testbed、能量收集装置、长期部署与**诚实的传感 ground truth**是
  硬通货。单次运行或纯仿真的结果在这里会被视为评估不足。
- **端上 AI，就在端上测。** 合并后嵌入式 AI 论文在范围内——但要证明的是**量化模型大小、RAM/flash
  峰值、端上推理延迟**，而不是工作站上的离线准确率。
- **各届 HotCRP 上的 double-blind。** 投稿匿名，**artifact 链接也要匿名**（匿名化的
  GitHub/GitLab/Zenodo，绝不能出现实验室或公司域名）。
- **ACM artifact badges。** Artifact Evaluation Committee 授予三枚独立徽章——*Artifacts
  Available*、*Artifacts Evaluated — Functional*、*Results Reproduced*——印在论文上并录入 ACM DL。
- **SenSys Test-of-Time 奖**锚定经典（B-MAC、FTSP、CTP、Protothreads），是最干净的 venue-verified
  exemplar 来源。

## Skills

| Skill | 作用 |
| --- | --- |
| [`sensys-topic-selection`](skills/sensys-topic-selection/SKILL.md) | 判断贡献是否是合并后 SenSys 认可的**已实现、可测量的传感/嵌入式系统**，把移动网络、纯 ML、信号处理的错配分流到 MobiCom、MobiSys、ML 会议或 DSP 会议。 |
| [`sensys-workflow`](skills/sensys-workflow/SKILL.md) | 按双截止日期日历规划、确认某截止日期对应哪一届，倒排让部署与能耗测量放得下，并安排"重投带修订"路径。 |
| [`sensys-writing-style`](skills/sensys-writing-style/SKILL.md) | 在 ACM 双栏页面内搭建 传感痛点 → 机制 → 测得行为 的叙事，用能耗数字与分布替代形容词。 |
| [`sensys-related-work`](skills/sensys-related-work/SKILL.md) | 梳理 传感/嵌入式/IoT/端上 AI 各条线，用 dblp/ACM DL 核 venue 以避开 MobiCom/NSDI/IPSN 误引，并做匿名安全的自引。 |
| [`sensys-experiments`](skills/sensys-experiments/SKILL.md) | 设计真实硬件评估：能耗与低功耗测量、testbed 与部署真实性、传感 ground truth、端上延迟/内存与诚实 baseline。 |
| [`sensys-reproducibility`](skills/sensys-reproducibility/SKILL.md) | 保留能耗、硬件、固件与 ground-truth provenance 以跨 testbed 复现，并尽早决定哪些 trace 与固件可以公开。 |
| [`sensys-supplementary`](skills/sensys-supplementary/SKILL.md) | 在正文、不限量的 references/appendices 与 HotCRP 字段之间安排内容，并让 response-to-reviewers 包不占正文。 |
| [`sensys-artifact-evaluation`](skills/sensys-artifact-evaluation/SKILL.md) | 为 AEC 打包：选择三枚 ACM 徽章中的哪些、为没有你 testbed 的评审者提供 hardware-optional 路径、以及证明可用的 smoke run。 |
| [`sensys-submission`](skills/sensys-submission/SKILL.md) | 最终审查：正确的 HotCRP 站点与截止日期、AoE 时刻、12/6 页双栏检查、含硬件/部署泄露的匿名扫查、以及适用时的重投契约。 |
| [`sensys-review-process`](skills/sensys-review-process/SKILL.md) | 解读双截止日期模型的结果空间——拒稿、下一截止日期"重投带修订"、录用——以及评审预期如何塑造修订。 |
| [`sensys-author-response`](skills/sensys-author-response/SKILL.md) | 把 response-to-reviewers 当作对"必改项"的契约来执行，并安排系统类修订通常需要的补充实验。 |
| [`sensys-camera-ready`](skills/sensys-camera-ready/SKILL.md) | 交付去匿名的双栏终稿、完成 ACM 版权与元数据、协调 artifact 徽章、规划现场报告与 demo。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 官方来源（URL 与访问日期）、已核验事实清单、access-method 说明（三站点直取均 403）与显式的 待核实 登记。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，加上五道作者侧核验（轮次/时钟、格式、匿名、重投、artifact/部署）。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇 venue-verified 的 SenSys Test-of-Time 论文，覆盖五类贡献，每篇带 self-check，并附 directed-diffusion / Glossy / TinyDB 误引护栏。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构的 batteryless 分类器论文的摘要与引言，重写为 SenSys 测得行为 叙事，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 通向共享复现套件的适配器，加上通用工具无法检查的 SenSys 专属项（能耗核算、硬件 provenance、传感 ground truth、端上占用）。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace 清单的独立插件）：

```bash
# 在仓库克隆中执行
claude plugin marketplace add ./SenSys-Skills
claude plugin install sensys-skills
```

或直接使用文件：每个 `skills/sensys-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。常见调用：

- "这是 SenSys 还是 MobiCom 的论文？" → `sensys-topic-selection`
- "我们冲哪个截止日期？重投需要什么？" → `sensys-workflow`
- "评审出来了——可以带修订重投" → `sensys-author-response`
- "上传 HotCRP 前审一遍 PDF" → `sensys-submission`

## 2026-27 锚点事实（带日期快照，非永久规则）

- **SenSys 2026**（首个合并版）于 **2026 年 5 月 11-14 日在法国 Saint-Malo** 举办，程序已完成，
  proceedings 已入 ACM DL。
- **SenSys 2027** 定于 **2027 年 5 月 10-13 日在美国纽约市**，经 `sensys27.hotcrp.com` 投稿；
  **第一轮截止为 June 6, AoE**。第二轮截止与通知日期在核实前记为 待核实。
- 格式（2027）：full **≤ 12 页**、short **≤ 6 页**，**references 与 appendices 不限量**且在页数
  上限之外；HotCRP 上 **double-blind**，artifact 链接匿名。
- Artifact evaluation 提供三枚 **ACM 徽章**；**SenSys Test-of-Time** 奖锚定经典。

## 事实纪律

全包始终区分三类陈述：

1. **已核验的周期事实**——可溯源到 source map 编号来源（合并、双截止日期模型、12/6 页格式、
   June 6 第一轮截止）。
2. **转述事实**——仅由单一渲染承载并如实标注（如 2026 具体子截止日期、2027 通知时点）。
3. **待核实 项**——显式标注并以问句表述（第二轮截止、2026/2027 chairs、模板几何、
   ethics/AI-use 措辞）。

在 skills 任何位置把第 2、3 类当作第 1 类呈现即为 bug，须对照官方页面修正。

## 维护说明

- 以上日期均为 **2026-27 快照**。SenSys 每届重写规则，且每周期两个截止日期——涉及 deadline 时须重开
  当年 CFP 与对应 HotCRP `/deadlines` 页。
- 截止是 **AoE**，逐位作者换算，切勿沿用旧的本地换算。
- **合并口径**是新变化——重新确认你的贡献仍应投 SenSys，而非其社区带着不同预期加入合并的另一会议。
- Chairs 每届轮换，2026/2027 委员会姓名未能干净取得——署名前请查委员会页。
- 新增 exemplar 必须通过
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的 venue 核验流程；传感
  领域最著名的论文最常被错分到 MobiCom、NSDI、IPSN。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
