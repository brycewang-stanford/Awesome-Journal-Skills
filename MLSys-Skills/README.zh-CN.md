# MLSys Skills

[English](README.md) | **简体中文**

面向 Conference on Machine Learning and Systems（MLSys）论文的 12 个 agent
skills。MLSys 是机器学习与计算机系统互相约束、互相塑造的交叉领域旗舰会议，本包覆盖
完整生命周期：判断项目是否属于真正的 ML-systems co-design、在 research track 与
industrial track 之间选道、构建能通过 systems 审稿人检验的评测、把论证压进 10 页
双栏正文、扛住该会异常短的 author response 窗口，以及把录用转化为
proceedings.mlsys.org 上的 camera-ready 发表和 Availability / Functional /
Reproducible 三种 artifact badge。

官方依据核验日期：2026-07-08。已核验 MLSys 2026 Call for Research Papers、首次设立
的 Industrial Track CFP、Call for Artifact Evaluations、dates 与 organizing
committee 页面、OpenReview conference group、proceedings 存档以及作者注册 FAQ。
每一条 cycle 相关事实的来源 URL 都记录在
[`resources/official-source-map.md`](resources/official-source-map.md)，无法在线核验
的条目在该文件中明确标注「待核实」，绝不臆测。

## MLSys 的独特之处

本包围绕该会的真实特质编写，而非泛泛的会议投稿建议：

- **双审稿文化。** 程序委员会混合了 ML 研究者与 systems / 体系结构 / 编译器背景的
  审稿人：论文既要命名一个可复用的 mechanism（systems 视角），又要证明优化不损害
  模型质量（ML 视角）。多个 skill 专门教你同时面向两种读者写作与答辩。
- **Benchmark 严谨性是身份标签。** MLPerf Training 方法论就发表在 MLSys 自己的
  proceedings 里；其测量文化——规定 workload、run rules、看尾延迟而非均值——就是
  审稿人套用的评测标准。
- **Badge 制 artifact evaluation。** 录用后由独立委员会实际运行你的代码，授予
  Availability、Functional、Reproducible 三种 badge，另设 Distinguished Artifact
  Award；为「他人重测」而打包是这里的一等公民技能。
- **被压缩的 rebuttal。** 2026 周期从 review 释出到 response 截止只有四天——在
  MLSys，rebuttal 策略本质上是一个调度问题。
- **2026 起的双 track。** Research track 要求新颖性、完全双盲；industrial track
  要求生产规模的系统设计与详尽 benchmark，明确不要求新颖性，且允许保留公司与产品
  名称。
- **性能主张要带四个坐标。** 吞吐、尾延迟、显存、成本必须同行出现；裸报 speedup
  会被当作营销话术。

## Skills

### 入场

- [`mlsys-topic-selection`](skills/mlsys-topic-selection/SKILL.md)：做 co-design
  双问测试，对照 OSDI/SOSP/NSDI/ASPLOS/ATC/EuroSys 与各大 ML 会议完成路由，选定
  research 或 industrial track，把贡献压缩成一句可检验的话。
- [`mlsys-experiments`](skills/mlsys-experiments/SKILL.md)：为 workload 代表性
  辩护，保证 baseline 调参预算对称，报告吞吐/尾延迟/显存/成本四坐标，用 ablation
  把收益归因到具体 mechanism。
- [`mlsys-writing-style`](skills/mlsys-writing-style/SKILL.md)：用实测瓶颈开篇、给
  技术起名、把评测组织成研究问题（必须包含「何时无效」与「代价是什么」两问），并
  压进 10 页双栏。
- [`mlsys-related-work`](skills/mlsys-related-work/SKILL.md)：覆盖散落多个 venue 的
  五条文献带，引用钉死版本号的开源系统，处理 arXiv 先行的相关工作，写出两种审稿
  文化都认可的 delta 陈述。

### 投稿与审稿

- [`mlsys-submission`](skills/mlsys-submission/SKILL.md)：核查 10 页正文、appendix
  单独上传、参考文献必须列全作者、允许挂 arXiv 的双盲规则、一稿多投的例外条款与
  desk-reject 触发点。
- [`mlsys-supplementary`](skills/mlsys-supplementary/SKILL.md)：在「审稿人无义务读
  appendix」的前提下切分正文与附录，把单独上传的附录组织成可审计结构，并对 trace
  与配置做匿名化。
- [`mlsys-reproducibility`](skills/mlsys-reproducibility/SKILL.md)：从驱动到互连
  完整钉死系统层环境，区分 ML 随机性与系统噪声，确定重复次数与方差报告方式，执行
  「全新机器」复现演练。
- [`mlsys-review-process`](skills/mlsys-review-process/SKILL.md)：理解 OpenReview
  流程、双文化审稿池、industrial track 的不同评审轴，以及录用决定真正取决于什么。
- [`mlsys-author-response`](skills/mlsys-author-response/SKILL.md)：执行四天响应
  时钟——零时刻分诊、最多两个来得及跑完的补充实验，以及针对经典 systems 审稿质疑
  的回复骨架。

### 录用之后

- [`mlsys-camera-ready`](skills/mlsys-camera-ready/SKILL.md)：去匿名化且不留残迹，
  在拿到雇主批准后恢复生产环境细节，兑现 rebuttal 承诺，并统筹 artifact 截止与
  作者保留票注册窗口。
- [`mlsys-artifact-evaluation`](skills/mlsys-artifact-evaluation/SKILL.md)：诚实
  选定目标 badge，按评审者可获得的硬件对主张分层，用钉死系统层的容器打包，并在
  匿名评审窗口内保持响应。
- [`mlsys-workflow`](skills/mlsys-workflow/SKILL.md)：以 GPU 时间为关键路径，从
  十月截稿倒排年度周期，预先约定 response 周协议，指派五顶责任帽子。

## Skills 的串联方式

一个典型的 research track 项目按以下顺序使用本包：

1. **路由**：`mlsys-topic-selection` 做 co-design 测试与 track 决策；若结论是
   「route elsewhere」，就此打住，省下一年。
2. **设计证据**：在烧 GPU 时之前，`mlsys-experiments` 先锁定 workload、baseline 与
   四坐标报告口径；`mlsys-reproducibility` 同步搭好测量框架与环境钉死——事后补装
   意味着整个 sweep 重跑。
3. **写作**：`mlsys-writing-style` 塑造第一页与 RQ 式评测结构；`mlsys-related-work`
   完成五条文献带定位；`mlsys-supplementary` 切分正文与单独上传的附录。
4. **提交**：`mlsys-submission` 执行合规与 desk-reject 审计；`mlsys-workflow` 从第
   1 步起就在跟踪节点与责任人。
5. **答辩**：`mlsys-review-process` 解读审稿包；`mlsys-author-response` 执行四天
   时钟。
6. **交付**：录用后 `mlsys-camera-ready` 与 `mlsys-artifact-evaluation` 并行推进，
   共用同几周和大体同一批人。

Industrial track 项目一步都不能省：只是把新颖性论证换成设计方法论深度，并增加一位
内部审批责任人（见 `mlsys-workflow`）。

## 适用对象

- 正在纠结系统成果该投 MLSys 还是 OSDI/ASPLOS/NSDI 的研究组——以及如果答案是
  MLSys，需要改什么。
- 考虑（2026 年新设的）industrial track 的工业团队：那里的门槛是 benchmark 与
  方法论深度，而非新颖性。
- 已经拿到录用、正面对 1 月底到 4 月初 camera-ready / artifact evaluation / 注册
  三线并行的作者。
- 代表以上任何人起草、审计或答辩的 agent——source map 会帮它分清哪些事实已核验、
  哪些是「待核实」。

## Resources

| 资源 | 用途 |
| --- | --- |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构摘要/引言的改写示范：从产品发布口吻改成 MLSys 弧线——实测瓶颈 → 洞察 → 命名机制 → 带范围的收益 → 诚实的代价。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经核验的 MLSys 本会范文（FlexFlow/SOAP、MLPerf Training、FedProx、transformer 推理扩展、AWQ），并列出误归属陷阱（vLLM、PipeDream、FlashAttention 都不是 MLSys 论文）。 |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 每条 2026 周期事实的来源 URL 与访问日期，以及明确的「待核实」清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 直达链接：两份 CFP、AE call、dates 页、OpenReview group、proceedings 存档、注册 FAQ。 |
| [`resources/code/README.md`](resources/code/README.md) | 把仓库级 ML 会议可复现工具包适配到系统层环境钉死与 badge 分层打包的说明。 |

## 已核验的 2026 周期锚点（复用前必须替换）

- 第九届会议，2026 年 5 月 18-22 日，Hyatt Regency Bellevue；2018 年以 SysML 之名
  创办于 Stanford，2020 年 Austin 届起改名 MLSys。
- 截稿 2025 年 10 月 30 日；review 释出 2026 年 1 月 12 日；author response 截止
  1 月 16 日；通知 1 月 25-26 日。
- 投稿格式：双栏、正文 10 页（参考文献不计入），每条文献列出全部作者；appendix
  不限长度、与正文同时但单独上传，审稿人无义务阅读。
- 双盲评审但允许同时挂 arXiv；industrial track 隐去作者姓名但可保留公司身份。
- Artifact evaluation：2026 年 3 月 8 日前提交，评审窗口 3 月 8 日至 4 月 8 日；
  badge 为 Availability、Functional、Reproducible，另设 Distinguished Artifact
  Award。
- 领导层（每届轮换）：General Chair Luis Ceze；Program Chairs Zhihao Jia 与
  Aakanksha Chowdhery。无 APC；proceedings.mlsys.org 开放获取。

## 维护说明

- 任何涉及 deadline 的建议前，必须重开 mlsys.org、两份 CFP、AE call 与 OpenReview
  group——MLSys 每个周期都在重构其征稿结构，industrial track 至今只运行过一届。
- Camera-ready 页数限制、到场报告义务、AI 使用政策，以及 MLSys 2027 的全部信息在
  2026-07-08 均无法核验，已标注「待核实」——重查之前不要让 agent 把它们当作事实
  输出。
- 本包中所有 2026 日期与页数都是描述该会形态的历史锚点，绝不能当作下一周期的
  规则使用。
