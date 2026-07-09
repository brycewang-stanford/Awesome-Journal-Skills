# RecSys Skills

面向 **ACM 推荐系统会议（ACM Conference on Recommender Systems, RecSys）** 论文的 12 个 agent
skills。RecSys 是推荐系统研究社区唯一的单一主题旗舰会议，本包聚焦真正决定 RecSys 录用结果的环节：
以推荐为中心的论文框架、诚实的 offline 与 online 评测对比、等预算（equal-budget）的 baseline
调参、防泄漏（leakage-aware）的数据划分、off-policy 与反事实（counterfactual）估计、会议专设的
Reproducibility track、论文内匿名代码发布、ACM 双栏 camera-ready，以及按 track 区分的项目日程。

RecSys 既不是通用机器学习会议，也不是信息检索会议。它的审稿人是一个内部紧密、且已深度吸收本领域
可复现性争论的社区，因此一篇能在这里获奖的论文，写法与投给 SIGIR、KDD、WSDM 或 TheWebConf 的论文
明显不同。本包把这种差异编码进 skills。

## 为什么需要 RecSys 专用包

通用的会议建议会错过 RecSys 审稿人真正奖励与惩罚的点：

- **是推荐，不是检索。** 贡献必须对推荐社区有意义——排序目标、用户/物品与 session 建模、反馈回路、
  曝光与公平、部署行为——而不仅仅是「能用于推荐」。
- **评测诚实是承重墙。** 在本领域的可复现性批评之后，审稿人把 baseline 调参、划分协议、指标选择
  当作「所报告增益是否真实」的代理信号。未调参的 baseline、序列数据上的随机划分、把 sampled
  指标当作 full-ranking 数字，都是可识别的 reject 模式。
- **offline 只是代理。** RecSys 独特地重视从 offline 指标到部署量的桥接——A/B test、off-policy
  估计（IPS / SNIPS / doubly robust）或 simulator——并奖励对这一差距诚实的论文。
- **专设 Reproducibility track。** 重复、反驳或重新界定既有结果，在这里是一等的、可发表的工作。
- **工业密度高。** 常设 Industry track 让带生产约束与线上证据的部署系统论文有真正归宿。

## 官方依据与访问方式

官方依据核验日期：**2026-07-09**。已对照 RecSys 2026 Call for Contributions、
`recsys.acm.org/recsys26` 系列页面、RecSys Best Paper Award 谱系、ACM Digital Library 论文集记录
与 dblp 核验。精确来源、逐条 URL 与访问日期见
[`resources/official-source-map.md`](resources/official-source-map.md)。

**访问方式说明：** 构建环境的网络网关对 `recsys.acm.org`、`recommender-systems.com`、
`dl.acm.org` 的直接抓取返回 HTTP 403。因此本包中每一条 RecSys 事实都是通过对这些官方页面的搜索
渲染结果核验，并与 ACM DL、dblp 以及逐字镜像 CFP 的邮件列表 Call 交叉核对。在依赖任何具体
deadline、页数或费用之前，请直接重新打开主 URL。

## 当前周期状态（截至 2026-07-09）

- RecSys 2026 是**第 20 届** ACM 推荐系统会议，地点 **美国明尼苏达州 Minneapolis**，主会期
  **2026 年 9 月 28 日至 10 月 2 日**（Doctoral Symposium 9 月 27 日，暂定）。
- 主 track 的摘要（4 月 14 日）、论文（4 月 21 日）与 rebuttal（6 月 4–9 日）截止日期均已**过期**。
  **主 track 通知日期为 2026 年 7 月 9 日——即今天**——因此对许多作者而言，当前阶段是 decision 与
  camera-ready，而不是投稿。
- Reproducibility 与 Industry track 同样在 7 月 9 日通知，camera-ready 为 2026 年 7 月 27 日。
- **R&P Notes 与 Demos**（截止 2026 年 7 月 15 日）仍开放。RecSys 2026 **取消了 Late-Breaking
  Results（LBR）track**，新增以 poster 形式呈现的 **Research & Practice（R&P）Notes**，并在主
  track 新增 **「Past, Present and Future」论文**类型。
- 前瞻规划：把每条 2026 事实都当作历史锚点，RecSys 2027 站点开放后再重新核验。

## Skills

- `recsys-topic-selection`：判断项目是否真属于推荐，路由 RecSys 与 SIGIR、KDD、WSDM、TheWebConf、
  UAI、CHI、通用 ML venue，并选定 RecSys track。
- `recsys-submission`：核查 track 选择、ACM 双栏正文页数（附录计入页数预算）、日志与部署系统名的
  匿名、论文内匿名 repository，以及 desk-reject 触发点。
- `recsys-writing-style`：改写为推荐优先的首页、诚实的 offline-online 框架、等预算 baseline 主张、
  防泄漏措辞与 8 页双栏压缩。
- `recsys-related-work`：面向推荐子领域与正确的邻近 venue 定位，把经典方法引用到其真实 venue，并
  保持双盲。
- `recsys-experiments`：设计 offline 与 online 评测：temporal 划分、等预算调参、full-ranking 与
  sampled 指标、off-policy 估计、A/B test 与 bias 处理。
- `recsys-reproducibility`：补强数据集/划分/调参/种子报告，避免 sampled 指标失真，并按
  Reproducibility track 组织带诚实分歧分析的复现研究。
- `recsys-artifact-evaluation`：把代码、数据集、划分、checkpoint 与 logged propensities 打包为
  论文内匿名 repository 或录用后公开归档。
- `recsys-supplementary`：在正文、计入页数预算的附录、匿名 repository 之间拆分材料，让证据落到
  审稿人真正会用的位置。
- `recsys-review-process`：解释双盲模型（3 名 PC 加 1 名 Senior PC）、rebuttal 阶段、审稿优先级与
  ACM Digital Library 出版。
- `recsys-author-response`：撰写简短的 rebuttal 叙述，锚定已提交证据，回应关于调参、泄漏与
  offline-online 差距的常见质疑。
- `recsys-camera-ready`：准备 ACM 双栏 camera-ready、版权表、元数据、去匿名、公开 artifact 发布、
  注册与报告。
- `recsys-workflow`：从选会到摘要、论文、repository、rebuttal、decision、camera-ready、报告做项目
  管理，含各 track 日期与倒排偏移。

## Resources

- [`resources/README.md`](resources/README.md)：行动导向资源索引。
- [`resources/official-source-map.md`](resources/official-source-map.md)：逐条 URL、访问方式说明与
  仍易变清单。
- [`resources/external_tools.md`](resources/external_tools.md)：官方链接与 RecSys 原生复现框架
  （Elliot、RecBole、LensKit、Cornac、RecPack）。
- [`resources/exemplars/library.md`](resources/exemplars/library.md)：按贡献类型整理的 6 篇经网络
  核验的 RecSys 论文，并附对 SIGIR / KDD / WWW / UAI 的同类混淆防护。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)：
  一份虚构的、RecSys 风格的摘要与引言 before-to-after 改写。
- [`resources/code/README.md`](resources/code/README.md)：接入共享 ML 会议可复现性工具，构建可再生
  的 top-N 排序 pipeline。

## 建议流程

1. 用 `recsys-topic-selection` 与 `recsys-writing-style` 做路由与定框。
2. 用 `recsys-experiments`、`recsys-reproducibility` 与 code adapter 压力测试证据。
3. 用 `recsys-artifact-evaluation` 与 `recsys-supplementary` 打包，再用 `recsys-submission` 审核。
4. 审稿后用 `recsys-review-process` 与 `recsys-author-response`；录用后用 `recsys-camera-ready`。
   全程用 `recsys-workflow` 控制日程。

## 维护说明

- 涉及 deadline 的建议前，务必重新打开当年官方页面；2026 的 track 组成已相较 2025 发生变化。
- 本包中的 RecSys 2026 事实是历史锚点，不应被当成永久规则。
- 页数预算、附录计入预算规则、参考文献额度、track 组成、rebuttal 窗口、camera-ready 日期、注册与
  报告要求都可能逐年变化。
- 每条事实都带 URL 与 2026-07-09 访问日期，或标注 待核实；更新时请保持这一纪律。
