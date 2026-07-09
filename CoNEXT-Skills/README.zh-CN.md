# ACM CoNEXT Skills

面向 **CoNEXT —— ACM International Conference on emerging Networking EXperiments and Technologies**
论文的 12 个 agent skills。CoNEXT 是 ACM SIGCOMM 的系统网络会议，自迁入 **PACMNET（Proceedings of
the ACM on Networking）** 后成为期刊式出版。本包覆盖一次 CoNEXT 投稿的完整流程：判断项目属于
CoNEXT 还是应投 SIGCOMM、NSDI、IMC 或 SIGMETRICS；构建能经受网络审稿人审视的测量与系统证据；在
**12 月**与**6 月**两个投稿周期之间选择；准备 double-anonymous 的 HotCRP 投稿；应对由原审稿人复审的
**one-shot “major” revision**；直到完成 PACMNET camera-ready 与获得可选的 ACM reproducibility 徽章。

官方依据核验日期：**2026-07-09**。已核验 CoNEXT 2026 的 call 与 Important Dates、CoNEXT 2025 CFP、
PACMNET 期刊与 editorial 页面、CoNEXT HotCRP 站点，以及 ACM reproducibility badging 政策。核验环境中
直接抓取 `conferences.sigcomm.org`、`dl.acm.org` 与 CFP 镜像返回 403，因此通过搜索引擎对精确 URL 的
渲染阅读官方页面，并与 ACM Digital Library（PACMNET editorial 与目录）、dblp CoNEXT proceedings、
RIPE RACI 转发的 CFP 交叉核对；完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 命名冲突提醒：“Conext” 亦为 Schneider Electric 逆变器等产品线，与本会议无关。本包只关于 ACM
> SIGCOMM 的 CoNEXT 会议，所有事实均不来自其他 “Conext”。

## CoNEXT 与同类会议的区别

以下会议机制（按 2026 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 SIGCOMM、NSDI、IMC 或
ML 会议转投作者最常犯的错误：

- **每年两个投稿截止日，一个会议。** CoNEXT 设 **12 月**与 **6 月**两个周期，共同汇入同一届年度
  会议与同一卷滚动的 PACMNET。CoNEXT 2026 的 12 月周期：注册 2025-12-05、投稿 2025-12-12、通知
  2026-03-31；6 月周期投稿 2026-06-05。选哪个周期是真实的策略决定，而非形式。
- **论文即期刊文章。** CoNEXT research paper 发表在 **PACMNET**，一本由 SIGCOMM 支持的 open-access
  ACM 期刊；录用论文排入**最近一期 PACMNET**（按周期命名，如 Vol 4 CoNEXT1 March 2026）。投稿按
  期刊稿件评审，同时获得会议报告席位。
- **one-shot “major” revision，由原审稿人复审。** 首轮决定为 Accept、**Reject** 或 **one-shot
  major revision**；后者附带优点总结与**最少必要修改**清单，作者约 **两个月**返修，随后由**原审稿
  人**决定录用与否。这是真正的期刊式 R&R，而非 rebuttal，且只有一次机会。
- **double-anonymous 的 SIGCOMM 式评审。** 两轮评审、在线讨论、**TPC meeting**，并对返修/有条件录用
  论文进行 **shepherding**，全程双盲 —— 承袭 SIGCOMM 的 public-review 与 shepherding 文化。
- **走 ACM `acmart` 路线。** long paper **≤16 页**（+参考文献不限 + 附录至多 4 页），short paper
  **≤10 页**（+参考文献不限 + 附录至多 2 页），使用 ACM `acmart` 模板 —— 不是 IEEE 双栏格式。
- **可复现性由委员会评定，徽章需 opt-in。** 单独的 **reproducibility committee** 授予**可选 ACM
  徽章**；须在**投稿截止前 opt-in**，并在录用后一周内提交一页 artifact 说明。
- **系统与测量的证据文化。** 真实 testbed、部署、trace 与可复现测量 —— 而非 leaderboard 分数 ——
  是网络审稿群体执行的社区规范。

## Skills

| Skill | 作用 |
| --- | --- |
| [`conext-topic-selection`](skills/conext-topic-selection/SKILL.md) | 在 CoNEXT 与同类会议（SIGCOMM、NSDI、IMC、SIGMETRICS、MobiCom、HotNets）之间选路，用贡献形态、证据成熟度，以及决定性的“两周期哪个更近”。 |
| [`conext-workflow`](skills/conext-workflow/SKILL.md) | 从 12 月或 6 月截止日倒排两周期年度计划，经注册、one-shot revision 窗口、可复现徽章、PACMNET camera-ready 与报告。 |
| [`conext-writing-style`](skills/conext-writing-style/SKILL.md) | 构建网络系统骨架：首页给出网络问题与部署语境、论断绑定测量、`acmart` 篇幅纪律。 |
| [`conext-related-work`](skills/conext-related-work/SKILL.md) | 覆盖网络文献 lane，对 SIGCOMM/NSDI/IMC 写 delta-first 定位，并保持自引匿名。 |
| [`conext-experiments`](skills/conext-experiments/SKILL.md) | 让证据匹配论断形态：真实 testbed 与部署、诚实 baseline、测量统计、trace provenance、防污染的 ML-for-networking ablation。 |
| [`conext-reproducibility`](skills/conext-reproducibility/SKILL.md) | 构建可复现网络证据：钉死 trace 与配置、可运行 artifact，以及委员会所需的一页说明。 |
| [`conext-supplementary`](skills/conext-supplementary/SKILL.md) | 按决策重要性划分正文、附录预算与 artifact —— 决定录用的证据不得藏于附录或仓库。 |
| [`conext-submission`](skills/conext-submission/SKILL.md) | HotCRP 终审：选对周期及其注册步骤、`acmart` 篇幅、双盲清扫、可复现 opt-in、desk-reject 分诊。 |
| [`conext-review-process`](skills/conext-review-process/SKILL.md) | 建模流程 —— 双盲、两轮评审、讨论、TPC meeting、one-shot major revision、shepherding —— 及作者杠杆点。 |
| [`conext-author-response`](skills/conext-author-response/SKILL.md) | 撰写两轮：初审 rebuttal 与把每条“最少必要修改”映射到 tracked edit、供原审稿人复审的 one-shot 回复信。 |
| [`conext-artifact-evaluation`](skills/conext-artifact-evaluation/SKILL.md) | 经 reproducibility committee 把录用论文的包转化为可选 ACM 徽章，从 opt-in 到一页说明到防评审者踩坑的复用文档。 |
| [`conext-camera-ready`](skills/conext-camera-ready/SKILL.md) | 系统去匿名、补全 PACMNET 期刊元数据、把 artifact 链接永久化、通过对应期号的 ACM 生产检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2026 cycle 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 经网络核验的 CoNEXT 论文（覆盖多种贡献形态），附自检问题与同类会议防混淆提示。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构拥塞控制研究的摘要与引言按 CoNEXT 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的 CoNEXT 专用检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./CoNEXT-Skills
claude plugin install conext-skills
```

也可直接使用文件：每个 `skills/conext-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这篇该投 CoNEXT 还是 SIGCOMM/NSDI/IMC？” → `conext-topic-selection`
- “该投 12 月还是 6 月周期？” → `conext-workflow`
- “按 CoNEXT CFP 规则审我的稿” → `conext-submission`
- “拿到 one-shot major revision —— 规划回复信” → `conext-author-response`
- “把 artifact 准备到 ACM 可复现徽章标准” → `conext-artifact-evaluation`

## 目录结构

```text
CoNEXT-Skills/
├── .claude-plugin/              # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                    # 英文说明
├── README.zh-CN.md              # 本文件
├── LICENSE                      # MIT
├── assets/cover.svg             # 封面
├── skills/
│   └── conext-<topic>/SKILL.md  # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `conext-topic-selection`；CoNEXT 与 SIGCOMM、NSDI 高度重叠，且两周期日历常使
   *最近的诚实截止日*成为决定因素。浏览 exemplars 看 CoNEXT 贡献长什么样。
2. **构建证据时** —— 让 `conext-experiments` 与 `conext-reproducibility` 贴着 testbed；采集期钉死的
   trace 与配置无法事后重建，且徽章 opt-in 在投稿时截止。
3. **写作时** —— 用 `conext-writing-style` 对照 worked example 打磨正文，用 `conext-supplementary`
   划分正文/附录/artifact，用 `conext-related-work` 做 delta-first 定位。
4. **截止周** —— 在 `conext-workflow` 选定周期，在较早截止日前完成注册，再用 `conext-submission`
   对终稿 PDF 与 artifact 逐项过审。
5. **投稿后** —— 用 `conext-review-process` 校准预期，用 `conext-author-response` 应对 rebuttal 与
   one-shot major-revision 回复信，随后 `conext-artifact-evaluation` 与 `conext-camera-ready` ——
   若结果不利，则用 `conext-topic-selection` 的路由表改投。

## 2026 周期锚点事实（历史快照，非永久规则）

- CoNEXT 2026 为**第 22 届**：**荷兰乌得勒支，2026 年 12 月 7-11 日**，ACM SIGCOMM 主办，论文入
  **PACMNET**。
- **12 月周期：**注册 2025-12-05、投稿 2025-12-12、early-reject 2026 年 2 月、通知 2026-03-31、
  camera-ready 2026-04-30、入 2026 年 6 月 PACMNET 期。Major-revision 路径：返修 2026-05-29、
  重投 2026-06-05、camera-ready 2026-07-31。**6 月周期：**投稿 2026-06-05。
- 出版：**PACMNET**，open access。评审：**double-anonymous**，两轮 + TPC meeting。决定：Accept /
  Reject / **one-shot major revision**。模板：**ACM `acmart`**；long ≤16 页（+参考文献 + 附录 ≤4），
  short ≤10 页（+参考文献 + 附录 ≤2）。经委员会评定的可选 **ACM 可复现徽章**，投稿前 opt-in。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026 cycle 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如 PACMNET 出版、
   两周期日期、one-shot revision、徽章 opt-in 规则）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如超出 live 组委页面确认范围的组委名单）。
3. **核验期不可确定项** —— 明确标为 待核实（如 2026 精确页数、各周期 HotCRP URL、PACMNET 文章是否
   附 public review、全年录用率）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。CoNEXT 每届重定结构 —— 包括两周期日期与 revision 机制 —— 每年
  先核验两周期日历。
- CoNEXT 无常任会议 editor-in-chief，chairs 每届轮换；PACMNET 的 Editorial Board 是期刊侧连续性。
  即便**出版物**是期刊，也不要对会议**人**做期刊式连续性假设。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 熟悉的工具名
  并不能证明该论文发表于 CoNEXT（许多网络经典发表在 SIGCOMM、NSDI 或 IMC）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
