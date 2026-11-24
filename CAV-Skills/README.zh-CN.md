# CAV 技能包

面向 **CAV——国际计算机辅助验证会议（International Conference on Computer Aided
Verification）** 投稿的十二个 agent 技能。CAV 是硬件与软件系统的计算机辅助形式化分析领域的旗舰会议。
本技能包覆盖一次 CAV 投稿的完整流程：判断一个课题是否适合 CAV，还是应投向 TACAS、FMCAD、VMCAI、某个
PL 会议或期刊；在 CAV 2027 的**三个投稿类别**（常规论文 Regular、工具论文 Tool、应用/工业经验/案例
研究论文 Application / Industrial Experience / Case Study）之间做选择；构建能经受审稿人
审计的验证实验（固定基准集版本、公平基线、可核验的证明见证）；通过带**早期拒稿过滤**与 rebuttal 的
**两阶段评审**；争取 **AEC 制品徽章**（自 CAV 2027 起工具论文必须参加）；并完成 **Springer LNCS** 定稿。

官方依据于 **2026-11-24 重新核实**：直接抓取 `conferences.i-cav.org/2027/` 上 CAV 2027 的征稿启事、
Artifact Evaluation、组委会、注册与会议录页面。本技能包现描述 **CAV 2027**（第 39 届，荷兰阿姆斯特丹，
2027 年 7 月 19-23 日）。较早的事实（CAV 2026 征稿启事、SIGPLAN 对第 38 届 CAV 的公告、FLoC 2026、
CAV 2024 与 CAV 2025 的 Springer LNCS 会议录、dblp）于 2026-07-09 在 `i-cav.org` 返回 403 时通过搜索
引擎渲染核对；完整取证记录（含仍标注 待核实 的条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## CAV 与同类会议的不同之处

以下经 CAV 2027 周期核实的会议机制，驱动了各技能中的大部分建议——也是从 ACM 期刊型 SE 会议、PL 会议或同类
形式化方法会议转来的作者最常犯的错误：

- **Springer LNCS——既非 ACM 期刊，也非 IEEE。** CAV 论文是 `llncs` 文档类的单栏 LNCS 章节
  （CAV 2025 = LNCS 15931-15934，开放获取；CAV 2027 会议录安排尚未公布）。不要把 `acmart` 或 IEEEtran 的双栏习惯带过来。
- **三个类别，且工具论文是一等公民。** 常规论文与**工具**论文（各 18 页）与**应用/工业经验/案例研究**
  论文（10 页）并列；每位作者最多 5 篇投稿。在标准基准上可用的验证工具是 CAV 认可的贡献形态，而非附属品。
- **部分双盲。** 仅常规论文需**匿名**；工具论文与应用类论文为**单盲**——因为隐藏工具身份的工具论文
  无法评审。此划分较为特殊，且在 2026 与 2027 之间发生了变化，每周期都要核实。
- **带早期拒稿的两阶段评审。** 第一阶段每篇论文获两条评审，最弱者被早期拒绝；仅存活者获得另两条评审与
  **rebuttal**。论文可能在 rebuttal 出现之前就被拒。
- **制品评估：工具论文必须参加，其余可选。** 专门的 **AEC** 通过冒烟测试与完整评审两个阶段颁发
  **Available / Functional / Reusable** 徽章。工具论文的制品在论文评审期间评估，至少获得 Functional
  徽章论文才能录用；其他类别在通知之后进行，录用**不以**其为条件。作者在投稿时声明制品意向。
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
| [`cav-submission`](skills/cav-submission/SKILL.md) | 投稿系统终审：类别选择、LNCS 页数限制、各类别匿名规则、工具论文必交制品与制品意向、桌拒风险分诊。 |
| [`cav-review-process`](skills/cav-review-process/SKILL.md) | 建模评审流水线——两阶段评审、早期拒稿、rebuttal、工具论文的 AEC 门槛——以及作者杠杆所在。 |
| [`cav-author-response`](skills/cav-author-response/SKILL.md) | 撰写第二阶段 rebuttal：以可核验证据回应可靠性、基准公平性与新颖性质疑，同时保持匿名。 |
| [`cav-artifact-evaluation`](skills/cav-artifact-evaluation/SKILL.md) | 为 AEC 打包：Available / Functional / Reusable，冒烟测试 + 完整评审两阶段，DOI 归档、基准、种子与见证。 |
| [`cav-camera-ready`](skills/cav-camera-ready/SKILL.md) | 去匿名，完成 Springer LNCS 元数据与开放获取版权，将制品链接永久化，并交接 AEC 徽章。 |

## 资源

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十九个来源（含 URL 与访问日期）；已核实的 CAV 2027 事实与 CAV 2026 历史；访问方式说明；明确的 待核实 清单；机器可读规则块。 |
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

## 2027 周期锚定事实（快照，非永久规则）

- CAV 2027 为**第 39 届**：**荷兰阿姆斯特丹**（KIT），**2027 年 7 月 19-23 日**（主会 7 月 21-23 日），
  首次在荷兰举办。程序主席（兼大会主席）：**Marieke Huisman、Joost-Pieter Katoen**。制品评估主席：
  **Tim Quatmann、Tom van Dijk**。
- 论文截止 **2027 年 1 月 20 日**（AoE）；早期拒稿通知 **3 月 4 日**；工具论文制品注册 **3 月 8 日**
  （提交 3 月 11 日）；作者回应 **4 月 5-8 日**；录用通知 **4 月 23 日**；非工具论文制品注册
  **4 月 26 日**；定稿 **5 月 18 日**。
- 类别与页数（LNCS，不含参考文献与附录）：常规 **18 页**（匿名）；工具 **18 页**（单盲，制品必交）；
  应用/工业经验/案例研究 **10 页**（单盲）。定稿分别为 20 / 20 / 12 页。每位作者最多 5 篇。
- 出版：**Springer LNCS**。评审：**两阶段**并含 rebuttal。制品：**AEC**（单盲），徽章
  **Available / Functional / Reusable**；工具论文必须参加（至少 Functional），其余受邀且非决定性。
- 历史：CAV 2026（第 38 届）于 2026 年 7 月 26-29 日在里斯本作为 FLoC 2026 的一部分举行，设四个类别
  （短工具、短应用论文各 10 页），所有类别的制品评估均为可选。

## 事实纪律

本技能包区分三类陈述，并在各技能中保持其可辨识：

1. **已核实的 2027 事实**——带有日期/页数，且可追溯到来源图中的编号来源（如三个类别、两阶段评审、
   工具论文必交制品、三种 AEC 徽章）。
2. **转述事实**——仅通过二级渲染阅读并如实标注（如 2026-07-09 读取的 CAV 2026 历史条目）。
3. **核对时不可确认的条目**——明确标注 待核实（如 CAV 2027 的 HotCRP 链接、CAV 2027 LNCS 卷号与开放
   获取安排、完整 PC 名单、注册费）。

若任何陈述以第 1 类口吻呈现第 2 或第 3 类材料，应视为缺陷并对照实时官方页面修正。

## 维护说明

- 以上每个日期与页数都是**周期快照**。CAV 每届都会重新决定其结构——包括类别集合、匿名矩阵、制品规则、两阶段评审
  时点（2026 与 2027 之间均有变化）——故每年先核实再行事。
- CAV 无常任主编，也无面向作者的按篇 APC；主席逐届轮换，LNCS 会议录为开放获取。每周期确认开放获取的
  经费安排。
- 添加范例论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核实流程——熟悉的工具名
  并不能证明其发表于 CAV（Z3 属 TACAS，IC3 属 VMCAI，CBMC 属 TACAS）。

## 许可

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
