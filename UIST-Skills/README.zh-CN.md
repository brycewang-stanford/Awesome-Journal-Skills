# UIST Skills（中文说明）

面向 **UIST（ACM Symposium on User Interface Software and Technology）** 的 12 个 agent
skills。UIST 是 SIGCHI 社区的界面**系统**主场：新交互技术、使能硬件、toolkit 与创作环境，
以及让新交互成为可能的工程本身。本包覆盖一个 UIST 周期的完整弧线——检验 artifact 是否真的
就是贡献本体、为系统类主张设计匹配的评估、制作 demo 文化下近乎必需的 video figure、写好
5,000 字符 rebuttal，并完成带无障碍要求的 ACM TAPS camera-ready。

官方依据核验日期：**2026-07-08**。核验对象：UIST 2026 主页、Call for Participation、
Author Guide、organizers 页面，ACM Digital Library 的 UIST 2025 主会与 adjunct
proceedings 记录，dblp 会议索引，以及用于 Lasting Impact 谱系的 UIST awards/archive
页面。核验环境中对 `uist.acm.org` 的直接抓取返回 403，因此官方页面内容经由精确 URL 的
搜索引擎渲染读取，并与 ACM DL、dblp、SIGCHI 交叉核对；完整链路（含所有仍标注 待核实 的
条目）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## UIST 与姊妹会议的差异

- **Artifact 即贡献。** UIST 的门槛是一个能运行的界面系统，其新颖性是一种**能力**：
  用户从此能做到此前任何已发表系统都做不到的事。再严谨的"关于人的发现"也应改投 CHI 或
  CSCW——`uist-topic-selection` 把这条路由判断讲成显式流程。
- **Demo 文化就是评审文化。** Video figure（2026 年规格：≤ 3 分钟、1080p/4K、
  MP4/H.264）名义可选、实际近乎决定性——评审先看视频判断系统是否真实，再权衡文字。
- **硬页数上限 + PCS 流程。** 2026 年评审版采用双栏 `acmart`：标准论文 10 页、短论文
  5 页（参考文献与附录不计），超限直接 desk reject；投稿走 PCS，abstract 截止早于正文
  一周。
- **Rebuttal 会变成合同。** 5,000 字符的回应是 PC 决策的正式输入，且录用是有条件的——
  条件正是 rebuttal 里你自己承诺的修改。
- **一个社区、两个存档容器。** Papers 进主 proceedings；Demos 与 Posters（独立主席、
  独立截止）进 adjunct proceedings——被拒论文的系统有真实的回退车道，但同一工作只能投
  一个 adjunct track。
- **十年尺度的记忆。** Lasting Impact Award 回溯表彰 Sensing Techniques for Mobile
  Interaction（UIST 2000）、DiamondTouch（UIST 2001）、SHARK2（UIST 2004）这类论文——
  这是该会议对自身贡献门槛的官方注解。

## 十二个技能各管什么

| 技能 | 解决什么问题 |
| --- | --- |
| [`uist-topic-selection`](skills/uist-topic-selection/SKILL.md) | 跑"删去 artifact 还剩什么"测试，按贡献形态做 CHI-vs-UIST 判断，必要时改道 CSCW、IMWUT、TEI、ISMAR、IUI 或 TOCHI。 |
| [`uist-workflow`](skills/uist-workflow/SKILL.md) | 从三月底截止日倒排：feature freeze、评估窗口、视频制作周、rebuttal、条件录用、七月 camera-ready、十一月会议，风险逐项指定负责人。 |
| [`uist-writing-style`](skills/uist-writing-style/SKILL.md) | 写系统论文的叙事弧——先 walkthrough 后机制、实现细节带测量条件、用能力陈述替代最高级形容词——并塞进 10/5 页预算。 |
| [`uist-related-work`](skills/uist-related-work/SKILL.md) | 沿技术谱系、toolkit 祖先、商业实践三条线以能力差定位；在 DL/dblp 上核验 venue 归属；处理第三人称自引。 |
| [`uist-experiments`](skills/uist-experiments/SKILL.md) | 让评估匹配主张类型（技术、硬件、toolkit、pipeline），用分布刻画工作包络，避开"仪式性可用性研究"。 |
| [`uist-reproducibility`](skills/uist-reproducibility/SKILL.md) | 维护三本台账——构建（元件、固件、魔法常数）、测量（每个数字的协议）、研究——并写诚实的可得性声明。 |
| [`uist-supplementary`](skills/uist-supplementary/SKILL.md) | 按主张写视频分镜、达标 2026 规格、对画面与音轨匿名化，并决定补充材料还装什么。 |
| [`uist-artifact-evaluation`](skills/uist-artifact-evaluation/SKILL.md) | 先为"五分钟匿名怀疑者"打包代码、toolkit、硬件设计文件，再为公开复用重新打包——在一个没有 badge 委员会的 venue。 |
| [`uist-submission`](skills/uist-submission/SKILL.md) | PCS 终审：abstract/正文双截止、页数闸门、匿名 acmart 选项、重叠稿附件规则、机械化排查、截止周排程。 |
| [`uist-review-process`](skills/uist-review-process/SKILL.md) | 建模评审管线——PC 加外审同时读论文与视频、rebuttal、PC 会议、条件录用——被拒后在 adjunct 回退、修复重投、改道三个出口间选择。 |
| [`uist-author-response`](skills/uist-author-response/SKILL.md) | 按期望价值分配 5,000 字符，用能力差回应新颖性质疑，并维护一份塞得进 +10% 版面余量的承诺台账。 |
| [`uist-camera-ready`](skills/uist-camera-ready/SKILL.md) | 兑现 rebuttal 合同，走 TAPS/APTARA 流程并为每个图、子图、表格写 alt text，去匿名化，定稿视频，尽早启动 Detroit 行程。 |

## 资源文件

| 文件 | 提供什么 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个官方来源（URL + 核验日期）、已核验的 2026 周期事实、访问方式说明与显式 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 在线官方入口，以及作者侧五道核验流程（track/日历、格式、视频、匿名、camera-ready）。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 六篇经 DL/dblp 核验的 UIST 论文（2000-2023，其中四篇获 Lasting Impact Award），各配自检问题与 venue 核验配方。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构的电触觉手套论文：摘要与引言从"动机散文"重写为能力 → 机制 → 证据的 UIST 弧线。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享 ML 会议工具包的适配层，外加它做不了的五项 UIST 专属检查（视频规格、硬件重建、测量协议等）。 |

## 安装方式

本目录本身就是一个带 marketplace 清单的 Claude Code 插件，可单独安装：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./UIST-Skills
claude plugin install uist-skills
```

不装插件也能用：每个 `skills/uist-*/SKILL.md` 自成一体，靠 frontmatter 里的
`description` 决定何时触发。举几个典型问法：

- "这个系统投 UIST，还是把研究部分投 CHI？" → `uist-topic-selection`
- "帮我按论文主张排视频分镜" → `uist-supplementary`
- "评审意见到了，周四开 rebuttal 窗口" → `uist-author-response`
- "条件录用了，TAPS 那边要什么？" → `uist-camera-ready`

## 目录布局

```text
UIST-Skills/
├── .claude-plugin/           # 插件与 marketplace 清单（登记全部 12 个技能）
├── README.md                 # English edition
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT 许可
├── assets/cover.svg          # 封面图
├── skills/
│   └── uist-<主题>/SKILL.md  # 十二个技能，每个独占一个目录
└── resources/
    ├── README.md             # 资源导览
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 复现工具包适配说明
```

## 按阶段使用

1. **立项时**——先跑 `uist-topic-selection`：如果删去 artifact 后剩下的是关于人的发现，
   及早改道 CHI 能省下一年；再用 exemplars library 校准野心。
2. **构建期**——尽早安装 `uist-reproducibility` 的三本台账和 `uist-experiments` 的
   证据计划；测量 harness 在截止月很难补装。
3. **写作与拍摄**——正文用 `uist-writing-style`，新颖性论证用 `uist-related-work`，
   视频用 `uist-supplementary`，对照 worked example 的前后版本。
4. **截止周**——对将要上传 PCS 的最终文件完整跑一遍 `uist-submission`（含 abstract
   截止）。
5. **评审季**——用 `uist-review-process` 读懂意见，rebuttal 周用
   `uist-author-response`，然后进入 `uist-camera-ready` 或 adjunct 回退车道。

## 2026 周期锚点事实（历史快照，不是永久规则）

- UIST 2026 是第 **39** 届：**美国密歇根州底特律（GM Renaissance Center），2026 年
  11 月 2-5 日**；Doctoral Symposium 于 11 月 2 日线下举行。
- Papers 时间线：abstract **3 月 24 日**、正文 **3 月 31 日**（11:59 pm AoE）、
  rebuttal **5 月 28 日 - 6 月 5 日**（≤ 5,000 字符）、通知 **6 月 27 日**、
  camera-ready **7 月 24 日**。
- 格式：双栏 `acmart`（评审版 `[sigconf,review,anonymous]`），正文 **标准 10 页 /
  短文 5 页**（参考文献与附录不计），超限 desk reject，camera-ready 可增 10%。
- Video figure：≤ 3 分钟、1080p 或 4K、MP4/H.264、匿名，"可选但强烈鼓励"。
- 匿名规则：自引用第三人称并保留完整文献信息；与本稿重叠较大的既往投稿需附匿名副本作为
  补充材料。
- 出版：主 proceedings 经 ACM TAPS（APTARA 无障碍标注），每个图、子图、表格必须有
  alt text。UIST 2025（第 38 届）在釜山举行（2025-09-28 至 10-01），proceedings DOI
  10.1145/3746059，adjunct 10.1145/3746058。

## 事实分级

包内所有陈述被划成三个等级，且在行文中保持可辨认：

1. **已核验的 2026 周期事实**——带日期/上限，可追溯到 source map 的编号来源。
2. **转述事实**——仅见于二手来源并如实标注（如 Sikuli 的最佳学生论文奖出自作者简历）。
3. **核验时无法确认的条目**——显式标注 待核实，只写成待解决的问题（adjunct 截止、注册
   规则、AI 使用政策、PCS 文件上限、开放获取条款等）。

任何把第 2、3 级材料写成第 1 级口吻的句子都算缺陷，应对照在线官方页面订正。

## 维护说明

- 上述全部日期与上限都是 **2026 届快照**；UIST 每届重发 CFP 与 Author Guide，且近年
  改过篇幅规则——给出任何截止敏感建议前先重开 `uist.acm.org/<year>/`。
- 各类主席逐届轮换（2026 委员会记录在 source map），不要把人名或 track 配置带入下一届。
- source map 中的 待核实 清单必须先对照在线页面解决，才能作为事实输出。
- 新增 exemplar 须执行 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的 DL/dblp 核验配方，并注意主会与 adjunct proceedings 的区分。

## 许可

本包以 MIT 许可发布（见 [`LICENSE`](LICENSE)）；英文版说明在 [`README.md`](README.md)。
