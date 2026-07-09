# CAV 技能包

面向 **CAV——国际计算机辅助验证会议（International Conference on Computer Aided
Verification）** 投稿的十二个 agent 技能。CAV 是硬件与软件系统的计算机辅助形式化分析领域的旗舰会议。
本技能包覆盖一次 CAV 投稿的完整流程：判断一个课题是否适合 CAV，还是应投向 TACAS、FMCAD、VMCAI、某个
PL 会议或期刊；在 CAV 的**四个投稿类别**（常规论文 Regular、短工具论文 Short Tool、短应用论文 Short
Application、工业经验报告与案例研究 Industrial Experience & Case Study）之间做选择；构建能经受审稿人
审计的验证实验（固定基准集版本、公平基线、可核验的证明见证）；通过带**早期拒稿过滤**与 rebuttal 的
**两阶段评审**；争取 **AEC 制品徽章**；并完成 **Springer LNCS 开放获取**的定稿。

官方依据核对于 **2026-07-09**：CAV 2026 的征稿启事与 Artifact Evaluation 页面、SIGPLAN 对第 38 届
CAV 的公告、FLoC 2026 站点、CAV 2024 与 CAV 2025 的 Springer LNCS 会议录，以及 dblp。在核验环境中直接
抓取 `i-cav.org` 与 `sigplan.org` 返回 403，因此官方页面通过对确切 URL 的搜索引擎渲染阅读，并与
Springer LNCS 和 dblp 交叉核对；完整取证记录（含仍标注 待核实 的条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## CAV 与同类会议的不同之处

以下经 2026 周期核实的会议机制，驱动了各技能中的大部分建议——也是从 ACM 期刊型 SE 会议、PL 会议或同类
形式化方法会议转来的作者最常犯的错误：

- **Springer LNCS 开放获取——既非 ACM 期刊，也非 IEEE。** CAV 论文是 `llncs` 文档类的单栏 LNCS 章节，
  开放获取出版（CAV 2025 = LNCS 15931-15934）。不要把 `acmart` 或 IEEEtran 的双栏习惯带过来。
- **四个类别，且工具论文是一等公民。** 常规论文（18 页）与短**工具**论文、短**应用**论文、**工业经验
  报告与案例研究**（各 10 页）并列。在标准基准上可用的验证工具是 CAV 认可的贡献形态，而非附属品。
- **部分双盲。** 常规论文与应用论文需**匿名**；工具论文与工业论文**不匿名**——因为隐藏工具身份的工具
  论文无法评审。此划分较为特殊，每周期都要核实。
- **带早期拒稿的两阶段评审。** 第一阶段每篇论文获两条评审，最弱者被早期拒绝；仅存活者获得另两条评审与
  **rebuttal**。论文可能在 rebuttal 出现之前就被拒。
- **可选、非决定性的制品评估。** 专门的 **AEC** 通过冒烟测试与完整评审两个阶段颁发 **Available /
  Functional / Reusable** 徽章，且在通知之后进行。录用**不以**制品评估为条件；作者在投稿时声明制品意向。
- **验证领域特有的证据文化。** 固定基准集版本（SV-COMP、SMT-COMP、HWMCC、VNN-COMP）、资源限额相同的
  公平基线、考虑超时的 cactus/scatter 报告，以及可核验的证明见证，都是审稿群体所执行的社区规范。

## 技能列表

| 技能 | 作用 |
| --- | --- |
| [`cav-topic-selection`](skills/cav-topic-selection/SKILL.md) | 在 CAV 与同类会议（TACAS、FMCAD、VMCAI、IJCAR、POPL/PLDI、期刊）之间选路，并选定类别（常规/工具/应用/工业）。 |
| [`cav-workflow`](skills/cav-workflow/SKILL.md) | 从截止日期倒排年度周期，贯穿两阶段评审、rebuttal、AEC 制品评估与 LNCS 定稿。 |
| [`cav-writing-style`](skills/cav-writing-style/SKILL.md) | 以验证贡献及其保证开篇；定理与证明的纪律；可证伪的基准论断；明确的适用范围。 |
| [`cav-related-work`](skills/cav-related-work/SKILL.md) | 覆盖各验证子领域，写以差异为先的定位，将工具/基准谱系归到正确会议，必要时保持自引匿名。 |
| [`cav-experiments`](skills/cav-experiments/SKILL.md) | 让证据匹配论断：标准基准、公平且版本固定的基线、相同资源限额、考虑超时的报告、可靠性交叉核验与见证。 |
| [`cav-reproducibility`](skills/cav-reproducibility/SKILL.md) | 固定基准版本、工具版本、限额、随机种子与硬件；提供可核验的证明证书；保持论文与制品一致。 |
| [`cav-supplementary`](skills/cav-supplementary/SKILL.md) | 在正文与可选附录/制品之间划分内容——审稿人无需阅读附录，故决定性内容必须留在正文。 |
| [`cav-submission`](skills/cav-submission/SKILL.md) | 投稿系统终审：类别选择、LNCS 页数限制、各类别匿名矩阵、制品意向、桌拒风险分诊。 |
| [`cav-review-process`](skills/cav-review-process/SKILL.md) | 建模评审流水线——两阶段评审、早期拒稿、rebuttal、可选非决定性 AEC——以及作者杠杆所在。 |
| [`cav-author-response`](skills/cav-author-response/SKILL.md) | 撰写第二阶段 rebuttal：以可核验证据回应可靠性、基准公平性与新颖性质疑，同时保持匿名。 |
| [`cav-artifact-evaluation`](skills/cav-artifact-evaluation/SKILL.md) | 为 AEC 打包：Available / Functional / Reusable，冒烟测试 + 完整评审两阶段，DOI 归档、基准、种子与见证。 |
| [`cav-camera-ready`](skills/cav-camera-ready/SKILL.md) | 去匿名，完成 Springer LNCS 元数据与开放获取版权，将制品链接永久化，并交接 AEC 徽章。 |

## 资源

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十一个来源（含 URL 与访问日期）；已核实的 2026 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方页面、SV-COMP/SMT-COMP/SMT-LIB 基准参考，以及网关拦截直接抓取时的交叉核对来源。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经存档核实的 CAV 论文，覆盖多种贡献形态（技术、算法、SMT 求解器工具论文、新领域、框架），并附同类会议防混淆护栏。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构的组合 SMT 论文摘要与引言，按 CAV 结构重写的 before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 对接共享的复现包工具，并补充 CAV 专有检查（基准溯源、种子、资源限额、证明见证）。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace 清单的自包含插件）：

```bash
# 从仓库克隆目录执行
claude plugin marketplace add ./CAV-Skills
claude plugin install cav-skills
```

或直接使用文件：每个 `skills/cav-*/SKILL.md` 都是独立的指令文件，其 frontmatter 中的 `description`
告诉 agent 何时触发。典型调用：

- “这是 CAV 论文，还是应投 TACAS/FMCAD？” → `cav-topic-selection`
- “按 CAV 常规论文规则审查我的草稿” → `cav-submission`
- “我们过了第一阶段——规划 rebuttal” → `cav-author-response`
- “把这个求解器准备好去拿 AEC 徽章” → `cav-artifact-evaluation`

## 2026 周期锚定事实（历史快照，非永久规则）

- CAV 2026 为**第 38 届**：**葡萄牙里斯本**，**2026 年 7 月 26-29 日**，作为 **FLoC 2026**（第 9 届
  联合逻辑会议）的一部分。程序主席：**Anthony W. Lin、Eva Darulova、Philipp Rümmer**。
- 论文截止 **2026 年 1 月 28 日**（AoE）；第一轮（早期拒稿）暂定结果 **约 3 月 4 日**；作者回应
  **3 月 30 日 - 4 月 2 日**；录用通知 **4 月 17 日**；制品注册 **4 月 22 日**。
- 类别与页数（LNCS，不含参考文献与附录）：常规 **18 页**（匿名）；短工具 **10 页**（不匿名）；短应用
  **10 页**（匿名）；工业经验与案例研究 **10 页**（不匿名）。
- 出版：**Springer LNCS**，**开放获取**。评审：**两阶段**并含 rebuttal。制品：**AEC**，徽章
  **Available / Functional / Reusable**，受邀且非决定性。

## 事实纪律

本技能包区分三类陈述，并在各技能中保持其可辨识：

1. **已核实的 2026 事实**——带有日期/页数，且可追溯到来源图中的编号来源（如四个类别、两阶段评审、LNCS
   开放获取出版、三种 AEC 徽章）。
2. **转述事实**——仅通过二级渲染阅读并如实标注（如各类别的精确匿名矩阵、暂定的 3 月 4 日第一轮日期）。
3. **核对时不可确认的条目**——明确标注 待核实（如 2026 投稿系统是 EasyChair 还是 HotCRP、是否有单独的
   摘要截止、定稿日期、完整的 PC/AEC 名单）。

若任何陈述以第 1 类口吻呈现第 2 或第 3 类材料，应视为缺陷并对照实时官方页面修正。

## 维护说明

- 以上每个日期与页数都是**周期快照**。CAV 每届都会重新决定其结构——包括类别集合、匿名矩阵、两阶段评审
  时点——故每年先核实再行事。
- CAV 无常任主编，也无面向作者的按篇 APC；主席逐届轮换，LNCS 会议录为开放获取。每周期确认开放获取的
  经费安排。
- 添加范例论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核实流程——熟悉的工具名
  并不能证明其发表于 CAV（Z3 属 TACAS，IC3 属 VMCAI，CBMC 属 TACAS）。

## 许可

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
