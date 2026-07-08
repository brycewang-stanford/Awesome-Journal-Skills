# CSCW Skills（中文说明）

面向 **CSCW — ACM SIGCHI Conference on Computer-Supported Cooperative Work and
Social Computing**（计算机支持的协同工作与社会计算会议）的 12 个 agent skills。
CSCW 是研究技术如何塑造和支持群体、社区、组织与协作实践的核心 venue。本包覆盖一篇
CSCW 论文的完整生命周期：判断"群体"是否真正是分析单位、设计方法多元的证据、进入
期刊化审稿管线、在同一批审稿人手中完成 Revise-and-Resubmit，最终拿到 PACMHCI 期刊
文章加会议报告。

官方依据核验日期：**2026-07-08**。已核验 CSCW 2026 官网与 Call for Papers、CSCW
2027 起的 rolling CFP、CSCW 2026 审稿流程 FAQ 与各轮决定的官方 blog、ACM CSCW
Medium 官方公告、ACM Digital Library 的 PACMHCI CSCW track，以及 dblp。核验环境中
`cscw.acm.org` 与 `dl.acm.org` 的直接抓取被拦截（HTTP 403），因此官方页面内容通过
搜索引擎对精确 URL 的渲染读取，并与 ACM DL、dblp、SIGCHI 活动页交叉核对；完整证据
链与全部 待核实 条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## CSCW 与兄弟 venue 的关键差异

CSCW 长着会议的外形，运转着期刊的内核 —— 而且正在结构性地变成期刊。以下经核验的
机制驱动了各 skill 中的建议：

- **论文即期刊文章。** 录用论文发表于 **PACMHCI（Proceedings of the ACM on
  Human-Computer Interaction）** 的 CSCW 专属 issue（例如 Vol. 8：CSCW1 2024 年
  4 月 209 篇，CSCW2 2024 年 11 月 171 篇），而非独立的会议论文集。
- **Revise-and-Resubmit 是主干道。** 最后一个固定周期中，进入外审的论文有 66.2%
  收到 R&R，且修改稿返回**同一批审稿人**。说服工具是 response letter，不是
  rebuttal 文本框。
- **截稿日已经消失。** 2025 年 5 月 14 日（PCS 平台）是最后一个固定截稿；CSCW
  2027 起采用 **rolling 投稿**，经 Manuscript Central
  （mc.manuscriptcentral.com/pacmhci）提交，由编辑委员会运作 —— 主编为 Amy
  Bruckman 与 Eric Gilbert —— 决定约在投稿后 3-4 个月返回。
- **篇幅是一种主张，不是上限。** 没有页数限制；取而代之的是审查带（约
  5,000-12,000 词），且"篇幅与贡献不相称"本身就是明确的 desk-reject 理由。
- **方法多元是真实的。** 访谈、民族志、痕迹数据分析、问卷、部署实验与理论文章都
  在此发表，各按其自身传统的严谨标准评判 —— venue 自己的 Lasting Impact Award
  获奖名单横跨所有这些方法。
- **被研究的社区是利益相关者。** 匿名化有两层（作者层与田野/社区层），数据发布由
  知情同意范围与社区暴露风险约束，而非可复现性至上。

## Skills

| Skill | 用途 |
| --- | --- |
| [`cscw-topic-selection`](skills/cscw-topic-selection/SKILL.md) | 运行分析单位测试，在 CHI、ICWSM、DIS、GROUP、TOCHI、FAccT 之间做路由决策。 |
| [`cscw-workflow`](skills/cscw-workflow/SKILL.md) | 规划期刊化战役：rolling 投稿时机、R&R 产能预算、会议年份倒推。 |
| [`cscw-writing-style`](skills/cscw-writing-style/SKILL.md) | 让每个论断停在群体层面，命名可复用概念，处理参与者引语，为词数辩护。 |
| [`cscw-related-work`](skills/cscw-related-work/SKILL.md) | 编织四条文献线，按年代正确引用 CSCW（proceedings vs PACMHCI），经受同审稿人复读。 |
| [`cscw-experiments`](skills/cscw-experiments/SKILL.md) | 设计方法多元的证据 —— 访谈、民族志、痕迹、问卷、部署 —— 各守其传统的严谨。 |
| [`cscw-reproducibility`](skills/cscw-reproducibility/SKILL.md) | 在无法共享处建立可审计性：codebook、决策日志、痕迹管线台账、诚实的可用性声明。 |
| [`cscw-supplementary`](skills/cscw-supplementary/SKILL.md) | 在正文、附录、补充材料间分配内容；清除文档/压缩包/数据抽样中的身份；按轮次留版本。 |
| [`cscw-artifact-evaluation`](skills/cscw-artifact-evaluation/SKILL.md) | 用社区保护测试打包 artifact：引语反搜、连接攻击、社区暴露、ETHICS.md。 |
| [`cscw-submission`](skills/cscw-submission/SKILL.md) | 核实当前投稿通道，审计两层匿名，检查词数带，执行上传前序列。 |
| [`cscw-review-process`](skills/cscw-review-process/SKILL.md) | 解读决定阶梯、R&R 基础比率、rolling 编辑委员会，以及每个月的沉默意味着什么。 |
| [`cscw-author-response`](skills/cscw-author-response/SKILL.md) | 跨方法传统分诊审稿要求，撰写同一批审稿人会复读的逐点 response letter。 |
| [`cscw-camera-ready`](skills/cscw-camera-ready/SKILL.md) | 运行录用后的双轨：PACMHCI 生产（条件、去匿名、TAPS）与会议报告。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个官方来源（URL + 核验日期）、已核验事实、明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，以及上传前的五个作者侧核查步骤。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经核验的 CSCW 论文 —— 四篇 Lasting Impact Award 得主加一篇 PACMHCI 时代锚点 —— 覆盖多种方法。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构的审核团队研究：摘要与引言从个体用户框架重建为群体框架的前后对照。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享可复现性工具包的适配器，仅适用于计算部分，并注明它检查不了什么。 |

## 安装与使用

作为 Claude Code 插件（本目录是带自有 marketplace manifest 的独立插件）：

```bash
# 在仓库克隆内
claude plugin marketplace add ./CSCW-Skills
claude plugin install cscw-skills
```

也可直接使用文件：每个 `skills/cscw-*/SKILL.md` 都是独立的指令文件，frontmatter
中的 `description` 说明触发时机。典型调用：

- "这个协作研究该投 CSCW 还是 CHI？" → `cscw-topic-selection`
- "收到 Revise and Resubmit 了，帮我规划修改" → `cscw-author-response`
- "审计我访谈研究的方法部分" → `cscw-experiments`
- "这个社区数据集能公开吗？" → `cscw-artifact-evaluation`

## 包结构

```text
CSCW-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── cscw-<topic>/SKILL.md # 12 个 skill，每目录一个
└── resources/
    ├── README.md             # 资源导览 + 建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 共享工具包适配器
```

## 建议路线

1. **研究开始前** —— 对项目核心论断运行 `cscw-topic-selection`：如果没有任何
   集体能诚实地补全"we show that ___"，这个包刚帮你省下一年。用
   `cscw-experiments` 设计证据，含伦理与引语政策。
2. **写作期间** —— `cscw-writing-style` 管群体层面的行文与篇幅辩护，
   `cscw-related-work` 管按年代正确的文献定位，worked example 作前后对照镜子。
3. **上传前** —— 完整走一遍 `cscw-submission`，从通道核实开始（平台在 2026 年
   换了），配合 `cscw-supplementary` 打包。
4. **在管线中** —— 用 `cscw-review-process` 解读决定与沉默；R&R 到来时用
   `cscw-author-response`（大概率会来：上一个已核验周期的基础比率是 66.2%）。
5. **录用之后** —— `cscw-camera-ready` 处理双轨，`cscw-artifact-evaluation`
   处理公开发布。

## 2026 年锚点事实（历史快照，不是永久规则）

- **CSCW 2026：** 美国犹他州盐湖城，**2026 年 10 月 10-14 日**（Marriott City
  Creek Center）。CSCW 2025 在挪威卑尔根，2025 年 10 月 18-22 日。
- **最后一个固定周期（对应 CSCW 2026）：** 2025 年 5 月 14 日 12:00 EDT 截稿
  （PCS）→ Revise-for-External-Review 重投 2025 年 9 月 16 日 → 首轮决定 2025 年
  11 月（33.8% 终局决定，66.2% R&R）→ R&R 重投 2026 年 1 月 13 日 → 最终决定
  2026 年 3 月下旬（录用 152 篇，拒稿 44 篇）。
- **Rolling 模式（CSCW 2027 起）：** 无截稿日；Manuscript Central
  （mc.manuscriptcentral.com/pacmhci）；编辑委员会制，主编 Amy Bruckman 与 Eric
  Gilbert；约 3-4 个月出决定；发表于 PACMHCI；受邀在下一届会议报告。
- **格式：** 单栏 ACM 投稿模板；无页数上限；5,000-12,000 词审查带；匿名评审，
  需删除作者姓名、机构与可识别的基金信息。

## 事实纪律

全包区分三类陈述并保持可辨认：

1. **已核验事实** —— 带日期并可追溯到 source map 中的编号来源（如 2025 年 5 月
   周期的统计、rolling 平台）。
2. **转述事实** —— 仅见于二手渲染，均已标注。
3. **核验时无法确认的条目** —— 标注 待核实，且写成待解决的问题而非事实（如
   rolling 的 track 名单、会议年份分配的截止点、TAPS 细节、注册要求）。

若发现任何 skill 把第 2、3 类内容写成了第 1 类，请视为 bug，并对照官方页面修复。

## 维护说明

- CSCW 的 rolling 模式明确处于**软启动**阶段，其机制（平台、节奏、track 结构、
  issue 分配）可能在数月内调整。给出任何时限敏感建议前，先重开
  cscw.acm.org/rolling.html。
- 本包中的固定周期事实是用于校准的**历史锚点**，不是现行规则 —— 2025 年 5 月
  周期不会再出现。
- 新增范文时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程；按年代正确引用（proceedings vs PACMHCI）是核验的一部分。
- 主编与编委会构成会更换；引用人名前请重新核实。

## 许可

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
