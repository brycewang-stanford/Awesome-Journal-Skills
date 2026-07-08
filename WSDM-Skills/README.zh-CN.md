# WSDM Skills（中文说明）

面向 **WSDM——ACM International Conference on Web Search and Data Mining**（发音
同 "wisdom"）投稿的 12 个 agent skills。WSDM 是网络搜索与数据挖掘方向规模小、
录取率低、传统上单轨（single-track）的冬季会议，由 ACM 的 SIGIR、SIGKDD、
SIGMOD、SIGWEB 四个 SIG 联合主办。本包围绕四个使 WSDM 策略不同于其"大型邻居"
的结构性事实构建：

1. **每年只有一个截稿，且没有 rebuttal。** 论文在每年 8 月提交（近年经
   EasyChair），约十周后直接收到结果，中间没有作者答辩环节——这一做法至少自
   2017 年就有文献记载。提交的 PDF 就是全部辩护材料，因此本包把"预写 rebuttal"
   当作一种写作纪律，而不是比喻。
2. **附录计入页数上限。** 2026 年规则为正文 9 页，**含**图表与附录；只有参考
   文献和必写的伦理考量（ethical considerations）小节不计页（2025 年为 8 页 +
   参考文献与伦理共享的 2 页）。没有无限附录，也未核实到独立补充材料通道——
   在文中引用的匿名代码仓库是唯一的"溢出空间"。
3. **带实验依据的混合盲审。** 对 PC 与 Senior PC 双盲，Associate Chair 可见
   作者元数据用于利益冲突核查——这一设计源自 2017 年在 WSDM 会议上开展、发表
   于 PNAS 的单盲/双盲对照实验。
4. **"practical yet principled" 的证据文化。** PC 由学界 IR/挖掘研究者与工业界
   搜索/推荐/广告科学家混合组成；胜出的论文同时具备行为数据的扎实根基、
   有偏差意识的评测与部署现实感。录取率约六分之一（2025 年：600+ 投稿中
   录取 100+）。

官方依据核验日期：**2026-07-08**。核验对象包括 WSDM 2026 官网与长文/短文 CFP
（第 19 届，美国博伊西，2026-02-22 至 02-26）、WSDM 2025 CFP 与 SIGWEB 会议报告
（第 18 届，德国汉诺威）、已上线的 WSDM 2027 官网（第 20 届，中国香港，
2027-02-15 至 02-19）、ACM Digital Library 论文集记录、dblp 与会议官方公告。
核验时部分官方域名被网络网关拦截，具体核验方法、全部来源 URL 与所有 待核实
条目见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 已核验锚点

| 事实 | 核验值 | 波动性 |
|---|---|---|
| 届次 | 2025：18 届，汉诺威，3/10-14 · 2026：19 届，博伊西，2/22-26 · 2027：20 届，香港，2/15-19 | 每届 |
| 2026 截稿 | 摘要 2025-08-07、正文 2025-08-14（AoE），EasyChair；通知列为 2025-10-23 | 每届 |
| 2026 页数 | ≤9 页且含附录；参考文献与伦理小节不计 | 每届 |
| 格式 | ACM `acmart`；2025 CFP 记载 `[sigconf,anonymous,review]` | 每届 |
| 盲审 | PDF 匿名；对 PC/SPC 双盲；AC 可见元数据查 COI | 每届 |
| 审稿配置 | 每篇 ≥3 份 PC 审稿 + Senior PC；历来无 rebuttal | 每届 |
| 伦理小节 | 必写、不计页，需讨论社会影响与缓解措施 | 每届 |
| 短文轨道 | 2026 年系列首设，9 月截稿，每人最多 10 篇 | 每届 |
| 录取率 | 2025：600+ 中录 100+（约 16-17%） | 每届 |
| 出版 | ACM DL（WSDM '26 DOI 10.1145/3773966）；四 SIG 联合主办 | 相对稳定 |

WSDM 2027 的 CFP 截稿、camera-ready 规则、费用与主席名单在核验时无法确认，
在来源地图中一律标注 待核实，绝不臆测。

## Skills

选路与规划：

- [`wsdm-topic-selection`](skills/wsdm-topic-selection/SKILL.md)：双门测试
  （网络/社交数据必须是研究对象本身；practical 与 principled 缺一不可）、
  2026 CFP 范围（含 "Search with Foundation Models"），以及对 SIGIR、KDD、
  WWW、CIKM、RecSys、ICWSM 的分流。
- [`wsdm-workflow`](skills/wsdm-workflow/SKILL.md)：单年度周期——从 8 月截稿
  倒排里程碑、9 月短文"泄压阀"、备用入口（demo、WSDM Cup、博士生论坛、
  Industry Day）与邻居会议的拒稿接力链。

写作与证据：

- [`wsdm-writing-style`](skills/wsdm-writing-style/SKILL.md)：行为事实开篇、
  无 rebuttal 场景下的"自足式"行文、WSDM 特有的句级警示词表、伦理小节写法、
  单轨听众的跨子领域可读性。
- [`wsdm-related-work`](skills/wsdm-related-work/SKILL.md)：接入 WSDM 自己的
  研究谱系（点击模型、无偏 LTR、序列推荐、推荐的离策略 RL、社区发现），
  机制级对比句，以及经 dblp 核验的 venue 归属。
- [`wsdm-experiments`](skills/wsdm-experiments/SKILL.md)：四象限证据（效果、
  效度、效率、鲁棒性）、时间切分与候选集口径、基线的新近性与调参对等、
  隔离机制的消融、线上证据的 attested 表述。
- [`wsdm-reproducibility`](skills/wsdm-reproducibility/SKILL.md)：行为数据的
  来历记录、切分 manifest、显式命名偏差模型、种子与方差纪律，以及
  rerunnable / rebuildable / attested 三档诚实阶梯。

打包与投稿：

- [`wsdm-artifact-evaluation`](skills/wsdm-artifact-evaluation/SKILL.md)：给
  审稿人十分钟可读的匿名仓库、专有日志的发布阶梯、公开基准镜像、WSDM Cup
  数据集与基础模型版本钉死。
- [`wsdm-supplementary`](skills/wsdm-supplementary/SKILL.md)：在"9 页含附录的
  正文 / 不计页的参考文献与伦理 / 引用的仓库"三个容器间做分诊，压缩战术与
  页数预算工作表。
- [`wsdm-submission`](skills/wsdm-submission/SKILL.md)：摘要-正文相隔一周的
  节奏、页数算术、混合盲审下的匿名化，以及 desk-reject 暴露面表格。

审稿阶段与之后：

- [`wsdm-review-process`](skills/wsdm-review-process/SKILL.md)：从 bidding 到
  10 月通知的流水线、"谁能看到什么"及其 2017 PNAS 实验渊源、审稿人构成解读
  与录取率算术。
- [`wsdm-author-response`](skills/wsdm-author-response/SKILL.md)：无 rebuttal
  会议上的作者沟通——异议清单法（objection inventory）、极少数正当的联系
  主席事由、拒稿后的分叉执行。
- [`wsdm-camera-ready`](skills/wsdm-camera-ready/SKILL.md)：先办 ACM e-rights
  再改稿、TAPS 式生产、CCS concepts、把去匿名当作编辑工序，以及二月参会的
  签证与披露审批。

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md)：11 个
  来源及访问日期、被拦截域名的核验方法披露、已核验事实清单与 待核实 登记。
- [`resources/external_tools.md`](resources/external_tools.md)：官方站点、
  EasyChair 说明、ACM DL/dblp 链接与逐届复查清单。
- [`resources/exemplars/library.md`](resources/exemplars/library.md)：5 篇经
  DOI 核验的 WSDM 论文（Craswell 2008、Yang & Leskovec 2013、Joachims 2017、
  Tang & Wang 2018、Chen 2019）及误归属防护表。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)：
  虚构论文的 before/after 重写，收束于无 rebuttal 的关键一招——把最强的
  异议写成论文的第 3 节。
- [`resources/code/README.md`](resources/code/README.md)：共享 ML 会议可复现
  工具包的适配说明，附 WSDM 特有注意点。

## 建议顺序

1. **选路**：`wsdm-topic-selection`，再用 `wsdm-workflow` 铺年度时钟与接力链。
2. **构建**：`wsdm-experiments` + `wsdm-reproducibility` 出证据，
   `wsdm-writing-style` + `wsdm-related-work` 成文。
3. **打包**：`wsdm-artifact-evaluation` 与 `wsdm-supplementary` 须早于截稿周，
   最后跑 `wsdm-submission` 审计。
4. **聪明地等待**：用 `wsdm-review-process` 理解流程；`wsdm-author-response`
   的工作在此会议全部发生在截稿之前。
5. **出版**：录用走 `wsdm-camera-ready`；被拒则执行 `wsdm-workflow` 预先画好
   的接力链。

## 安装

本包以 Claude Code plugin 形式发布。在本仓库根目录：

```bash
claude plugin marketplace add ./WSDM-Skills
claude plugin install wsdm-skills
```

也可直接让 agent 读取单个 `skills/wsdm-*/SKILL.md`——每个 skill 的 frontmatter
声明触发范围，结尾附结构化输出块，便于串联。

## 范围与免责

- 本包提供 WSDM 投稿的策略、证据与写作建议，不是 CFP 本身；与当届官方说明
  冲突时，一律以官方为准。
- 所有带日期的事实均为 2026-07-08 核验的"届次锚点"，不是规则；无法核验的
  条目在来源地图中标注 待核实，绝不硬编码。
- worked example 是刻意虚构的教学材料，范文库记录的是定位模式；两者都不含
  可直接粘入论文的语句。

## 维护说明

- 每年 8 月前重新核验：截稿日期、页数上限及计页口径、EasyChair 实例、伦理
  小节措辞、短文轨道与 AI 政策——以上各项在 2025 与 2026 之间至少变过一次。
- 2027 周期核验时已上线但被网关拦截无法直读，其 CFP 页面是最优先要重开的。
- 每年向范文库补充两篇最近届次的论文（附 DOI）。
- 英文版见 [`README.md`](README.md)；事实变更时两份 README 须同步修改。
