# IPSN Skills

面向 **IPSN —— ACM/IEEE International Conference on Information Processing in Sensor Networks**
论文的 12 个 agent skills。IPSN 是 CPS-IoT Week 旗下的会议，是传感理论、端侧/TinyML 推理、定位与
网络化嵌入式系统交汇之处。本包覆盖一次 IPSN 投稿的完整流程：判断项目属于 **Information
Processing（IP）** 贡献还是 **Sensor Platforms, Tools and Design Methods（SPOTS）** 贡献；构建
能经受传感系统审稿人审视的真实部署与估计理论证据；准备 double-blind 的 HotCRP 投稿（ACM 模板）；
以及 —— 决定一切的事实 —— 将 IPSN 形态的论文导向其**继任会议**，因为 IPSN 已于 2025-2026 年并入
重组后的 **SenSys（Embedded AI and Sensing Systems）**。

官方依据核验日期：**2026-07-09**。已核验 IPSN 2024（第 23 届）research call 与 `ipsn.acm.org/2024`
页面、CPS-IoT Week 2024/2025/2026 站点、吸收 IPSN 的 SenSys 2025/2026 call、ACM Digital Library 与
IEEE Xplore 的 IPSN proceedings，以及 dblp。核验环境中直接抓取 `ipsn.acm.org`、`dl.acm.org`、
`dblp.org` 返回 403，因此通过搜索引擎对精确 URL 的渲染阅读官方页面，并与 ACM DL、IEEE Xplore、
dblp 及 CPS-IoT Week program 页交叉核对；完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> **必读状态提醒。** IPSN 以独立会议形式运行至 **IPSN 2024**（第 23 届，香港，CPS-IoT Week 2024）。
> 自 2025 年起，**SenSys、IPSN、IoTDI 合并**；自 2026 年，合并后的会议为 **ACM/IEEE International
> Conference on Embedded Artificial Intelligence and Sensing Systems（SenSys）**，仍在 CPS-IoT
> Week 内举办。**不存在独立的「IPSN 2026/2027」。** 本包传授 IPSN 的*传统与标准*，并把你导向这类
> 工作如今的投稿地。行动前请核验当前继任会议的 call。
>
> 命名冲突提醒：「IPSN」也是 WHO 的 *International Pathogen Surveillance Network* 与某 IEEE
> *IP-over-Sensor-Network* workshop —— 均非本 IPSN，本包事实不来自它们。

## IPSN 与同类会议的区别

以下机制（按 IPSN 谱系及其 2025/2026 继任会议核验）驱动了 skills 的大部分建议，也对应从 SenSys、
MobiSys、MobiCom 或纯信号处理会议转投作者最常犯的错误：

- **标志性双轨：IP 与 SPOTS。** IPSN 将投稿分为 **Information Processing（IP）轨** —— 算法、估计、
  信号处理、推理、学习、定位 —— 与 **Sensor Platforms, Tools and Design Methods（SPOTS）轨** ——
  硬件、嵌入式软件、工具、测量与真实部署。选轨会重塑审稿群体与证据标准。无同类旗舰有此划分。
- **它属于 CPS-IoT Week。** IPSN 与 **RTAS、HSCC、ICCPS**（及历史上的 IoTDI）在 CPS-IoT Week 下
  同址 —— 一个实时系统、混合系统与信息物理的邻里，而非 MobiSys/MobiCom 的移动计算圈，也非独立秋季
  的 SenSys。
- **ACM/IEEE 联合主办。** IPSN 由 **ACM SIGBED 与 IEEE** 主办；论文同时进入 **ACM Digital Library
  与 IEEE Xplore** —— 双出版方足迹影响版权表与元数据。
- **传感理论与系统并列。** 一篇 IPSN 论文可以是 Cramér-Rao 下界估计器、compressive-sensing 结果，
  或微控制器上的 TinyML 推理流水线 —— 名字里的「information processing」是实打实的，纯系统审稿人并非
  唯一读者。
- **ACM 模板双盲、≤12 页。** IPSN 2024 采用 **double-blind** 评审、**ACM Primary Article Template**
  （双栏、9 pt）、**≤12 页**（含图、表、参考文献），经 **HotCRP** 投稿，而非 OpenReview。
- **artifact 与部署文化，且有专门奖项。** IPSN 设 **Best Paper Award** 与 **Best Research Artifact
  Award**；真实部署（桥梁、建筑、野生动物、工厂）是原生贡献形态，而非附属。
- **合并是最大的 live 事实。** 本包最高杠杆的作用，是阻止你追逐一个已不再举办的会议，并让你带着
  IP/SPOTS 的直觉投向它的继任会议。

## Skills

| Skill | 作用 |
| --- | --- |
| [`ipsn-topic-selection`](skills/ipsn-topic-selection/SKILL.md) | 判定 IP 轨 vs SPOTS 轨，并在 IPSN 谱系（今 SenSys）与 CPS-IoT Week 邻居（RTAS/ICCPS/HSCC）、MobiSys/MobiCom、INFOCOM 或信号处理期刊之间选路。 |
| [`ipsn-workflow`](skills/ipsn-workflow/SKILL.md) | 从 CPS-IoT Week 日历倒排，经合并感知的路由、双盲投稿、部署后勤、artifact 奖项与 camera-ready。 |
| [`ipsn-writing-style`](skills/ipsn-writing-style/SKILL.md) | 构建传感系统骨架：首页给出真实传感问题、诚实的端到端系统或估计器论断、ground-truth 方法学、能耗/时延/精度预算。 |
| [`ipsn-related-work`](skills/ipsn-related-work/SKILL.md) | 覆盖传感网络 lane（IPSN/SenSys/MobiCom/MobiSys/INFOCOM + 信号处理会议），写 delta-first 定位，保持自引双盲。 |
| [`ipsn-experiments`](skills/ipsn-experiments/SKILL.md) | 让证据匹配论断形态：真实 testbed 与部署、ground-truth 仪器化、能耗/时延测量、端侧/TinyML profiling、估计理论 baseline。 |
| [`ipsn-reproducibility`](skills/ipsn-reproducibility/SKILL.md) | 构建硬件/嵌入式 artifact 所需的可复现故事：固件、板级文件、traces、标定，以及物理系统诚实的可复现层级。 |
| [`ipsn-supplementary`](skills/ipsn-supplementary/SKILL.md) | 按决策重要性划分 ≤12 页正文与 artifact/appendix，并给出 demo/poster 与数据集发布路径。 |
| [`ipsn-submission`](skills/ipsn-submission/SKILL.md) | HotCRP 终审：IP-vs-SPOTS 选轨、ACM 模板与 12 页预算、硬件论文的双盲清扫、desk-reject 分诊 —— 导向当前继任 call。 |
| [`ipsn-review-process`](skills/ipsn-review-process/SKILL.md) | 建模流程 —— 双盲、按轨 TPC、rebuttal、Best Research Artifact 评选 —— 及其与 SenSys 返修模型和 OpenReview 会议的差异。 |
| [`ipsn-author-response`](skills/ipsn-author-response/SKILL.md) | 撰写双盲 rebuttal，在 ground truth、baseline、部署真实性与能耗核算上回应传感系统审稿人而不泄露身份。 |
| [`ipsn-artifact-evaluation`](skills/ipsn-artifact-evaluation/SKILL.md) | 为硬件+软件 artifact 争取 ACM 徽章与 IPSN Best Research Artifact Award：固件、数据集、DOI 存档、防评审失败的文档。 |
| [`ipsn-camera-ready`](skills/ipsn-camera-ready/SKILL.md) | 去匿名、补全 ACM/IEEE 双出版元数据（CCS、ORCID、DOI、IEEE PDF eXpress）、永久化数据集链接、通过双出版方生产检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 带 URL 与访问日期的来源；已核验 IPSN 谱系与合并事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口（IPSN 存档、CPS-IoT Week、继任 SenSys、ACM DL、IEEE Xplore）与网关阻断时的交叉核对来源。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 三篇经存档核验的 IPSN 论文，覆盖 IP、SPOTS 与部署形态，附自检问题与同类混淆防护。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构「微控制器上 TinyML」研究的摘要与引言按 IPSN 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的 IPSN 硬件/固件/部署检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./IPSN-Skills
claude plugin install ipsn-skills
```

也可直接使用文件：每个 `skills/ipsn-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这是 IP 轨还是 SPOTS 轨？IPSN 的工作现在投哪？” → `ipsn-topic-selection`
- “按 IPSN 双盲 ACM 模板规则审我的稿” → `ipsn-submission`
- “审稿意见来了 —— 起草关于 ground truth 与能耗的 rebuttal” → `ipsn-author-response`
- “把这套固件+数据集 artifact 准备到 Best Research Artifact Award 标准” → `ipsn-artifact-evaluation`

## 目录结构

```text
IPSN-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── ipsn-<topic>/SKILL.md # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `ipsn-topic-selection`；IP-vs-SPOTS 选轨与合并路由是最能改变结果的两个决定。
   浏览 exemplars 看 IP 轨理论论文、SPOTS 轨平台论文与真实部署长什么样。
2. **构建证据时** —— 让 `ipsn-experiments` 与 `ipsn-reproducibility` 贴着 testbed；采集期记录的
   ground truth、能耗 trace 与标定无法事后补救。
3. **写作时** —— 用 `ipsn-writing-style` 对照 worked example 打磨正文，用 `ipsn-supplementary`
   划分正文/artifact/数据集，用 `ipsn-related-work` 跨传感 lane 做 delta-first 定位。
4. **截止周** —— 先核验继任 call 的注册截止日，再用 `ipsn-submission` 对终稿 PDF、选轨与双盲清扫
   逐项过审。
5. **投稿后** —— 用 `ipsn-review-process` 校准，用 `ipsn-author-response` 应对 rebuttal，随后
   `ipsn-artifact-evaluation` 与 `ipsn-camera-ready` —— 若结果不利，则用 `ipsn-topic-selection`
   的路由表改投。

## 谱系与继任锚点事实（历史快照，非永久规则）

- **IPSN 2024** 为**第 23 届** ACM/IEEE International Conference on Information Processing in
  Sensor Networks：**香港**，属 **CPS-IoT Week 2024**（2024 年 5 月 13-16 日）。双盲、**ACM Primary
  Article Template**、**≤12 页**（含全部内容），经 HotCRP（`ipsn2024.hotcrp.com`）。两轨：**IP** 与
  **SPOTS**。奖项：**Best Paper** 与 **Best Research Artifact**。这是**最后一届独立 IPSN**。
- **合并：** SenSys、IPSN、IoTDI 合并；**SenSys 2025**（CPS-IoT Week 2025，Irvine）为首个合并事件，
  自 2026 年会议为 **SenSys —— ACM/IEEE International Conference on Embedded Artificial Intelligence
  and Sensing Systems**。**SenSys 2026** 在 **CPS-IoT Week 2026**（法国圣马洛，2026 年 5 月 11-14 日；
  投稿截止 2025-11-13 AoE，双盲）举办。截至 2026-07-09，IPSN 谱系工作的 live 下一目标是随后一届
  SenSys（**下一个确切截止日 待核实**）。
- **出版：** 历史上为 ACM DL + IEEE Xplore。合并会议中，常规技术论文进入 **ACM** proceedings，
  demo/poster 进入 **IEEE** proceedings（按届核验）。

## 事实纪律

本包区分三类陈述，skills 保持其可区分：

1. **已核验谱系/继任事实** —— 带日期/预算并追溯 source map 编号来源（如 IPSN 2024 的 12 页双盲 ACM
   格式、IP/SPOTS 双轨、SenSys 合并与 SenSys 2026 的 2025-11-13 截止日）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如具体组委名单、部分奖项历史）。
3. **核验期不可确定项** —— 明确标为 待核实（如下一届继任会议截止日、是否存在 IPSN「Test of Time」
   奖、各轨录用率、任何生成式 AI 披露政策）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与预算都是**快照**，且 IPSN 作为独立会议已在 2024 后终止 —— 建议前务必重新核验当前继任
  会议（SenSys）的 call。
- IPSN **无常任 editor-in-chief**；领导层每届轮换，为 CPS-IoT Week、ACM SIGBED 与 IEEE 下的 General
  与各轨 Program Chairs。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 熟悉的
  传感网络工具名并不能证明该论文发表于 IPSN（许多在 SenSys、MobiCom 或 NSDI）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
