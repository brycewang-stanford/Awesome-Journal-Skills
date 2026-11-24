# ICDM Skills

面向 **ICDM——IEEE International Conference on Data Mining** 论文的 12 个 agent skills。
ICDM 是 IEEE 主办的 data mining 旗舰会议，覆盖数据挖掘算法、graph/pattern mining、
anomaly detection 与 applied analytics。本包围绕四条使 ICDM 策略区别于其 ACM、SIAM 兄弟
会议的结构性事实构建：

1. **Triple-blind 审稿，而非 double-blind。** 自 2011 年起，ICDM Research Track 同时隐藏
   作者与审稿人身份；姓名仅 PC Co-Chairs 可见，作者姓名在排名与录用确定后才披露。匿名必须
   贯穿**全文**，而不只是首页。
2. **单一、全包含的页数上限。** 采用 IEEE two-column 格式，**最多 10 页，包含参考文献与所有
   附录**——一切都算进这 10 页内，超长论文**不经评审直接拒稿**。没有单独的参考文献或附录页数
   预算。
3. **regular 转 short 的录用机制。** 所有论文都按 full paper 格式投稿；录用后被**指定为 Regular
   或 Short**。2026 年两种指定都保持 10 页上限，因此 "short" 只是指定而非强制压缩——但往届曾
   缩短 short paper，每届都要核对。
4. **2026 年新增的双轨划分。** 该届首次在 triple-blind Research Track 之外，运行
   **Applied Track（single-blind）** 与 CCC 赞助的 **Blue Sky Track**——因此匿名规则现在取决
   于所投 track。

官方依据核验日期 **2026-07-09**：ICDM 2026 官网（第 26 届，2026-11-12 至 15，东北大学，
中国沈阳）、Research 与 Applied Track 征稿、CCC Blue Sky Track 征稿、IEEE ICDM 获奖名录、
IEEE Xplore proceedings 与 dblp。主办域名在 2026-07-09 对自动抓取返回 403，故事实当时通过搜索
渲染核验（**2026-11-24** 已直接抓取**重新核验**征稿、重要日期、作者须知与委员会页面，删除了一个
并不存在的摘要截止日，并确认了 camera-ready 日期、chair 与复现清单），并与
dblp、获奖页交叉核对。精确来源、访问方式说明与所有 **待核实** 项见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 已核验的 2026 届锚点

| 事实 | 2026 取值 | 波动性 |
|---|---|---|
| 届次 | 第 26 届 IEEE ICDM，2026-11-12 至 15，东北大学，沈阳 | 每届变 |
| 截止 | 全文 2026-06-06（AoE），**无单独摘要截止**；通知 2026-08-16；camera-ready 2026-09-09 | 每届变 |
| 周期模型 | **单一截止**（无 KDD 式多 cycle） | 相对稳定 |
| 格式 | IEEE two-column，**含参考文献与附录共 10 页**；超长即不评审拒稿 | 每届变 |
| Research Track 审稿 | 自 2011 **triple-blind**（作者+审稿人皆隐藏，仅 PC Co-Chairs 可见） | 每届变 |
| Applied Track 审稿 | **single-blind**（2026 新增 track） | 每届变 |
| short-paper 机制 | 全部按 full paper 投；录用后指定为 **Regular 或 Short**，2026 年均为 10 页上限 | 每届变 |
| 投稿附加项 | 投稿时须填**复现清单**；审稿期间勿发布/宣传预印本（投稿前已发的可保留） | 每届变 |
| Rebuttal | 2026 征稿中**未描述**任何 rebuttal | 每届变 |
| 出版 | IEEE CS Press proceedings，收录于 IEEE Xplore 与 dblp；需现场报告（无法到场者参加指定线上 session 并提供录像备份），每篇论文都须做海报 | 每年变 |
| 主席（2026） | General：Claudia Plant、Xiaochun Yang；PC：Danai Koutra、Xiaofeng Gao | 每届变 |

ICDM 2026（2026-11-12 至 15，沈阳）已闭幕。截至 2026-11-24 未找到 ICDM 2027 官方网站或征稿
（聚合站称在 Brisbane，未核实），因此仍以 2026 规则作为标注清楚的先验；费用与未来可能的
rebuttal 仍在 source map 中标注 **待核实**。

## Skills

选会与规划：

- [`icdm-topic-selection`](skills/icdm-topic-selection/SKILL.md)：venue 契合判断，加上
  track 分叉（Research / Applied / Blue Sky），以及从 ICDM 六月截止视角出发对 KDD、SDM、
  CIKM、WSDM、WWW 与 ML 旗舰会的分流。
- [`icdm-workflow`](skills/icdm-workflow/SKILL.md)：单截止流水线——摘要到全文的偏移、到八月
  通知的漫长夏季等待，以及录为 short paper 的分支。

写作构建：

- [`icdm-writing-style`](skills/icdm-writing-style/SKILL.md)：ICDM 语域——data regime 先行、
  named-mechanism 纪律、可测量的 scale 措辞、discovery-validity 句式、triple-blind 安全的
  自引。
- [`icdm-related-work`](skills/icdm-related-work/SKILL.md)：面向历届 ICDM 与 IEEE data mining
  邻居的谱系定位、KDD/SDM/CIKM 误attribution 陷阱，以及对自身既往工作的匿名比较。
- [`icdm-experiments`](skills/icdm-experiments/SKILL.md)：mining 证据方案——task 定义、
  baseline、隔离机制的 ablation、scalability 曲线，以及针对评测 artifact 的 discovery-validity
  检查。
- [`icdm-reproducibility`](skills/icdm-reproducibility/SKILL.md)：triple-blind 规则内的可复现
  ——seed、config、compute，以及不泄露身份的匿名 artifact。

打包与投稿：

- [`icdm-artifact-evaluation`](skills/icdm-artifact-evaluation/SKILL.md)：为 triple-blind
  Research Track 构建匿名、清除历史的仓库，以及 Applied Track single-blind 规则如何改变可披露
  内容。
- [`icdm-supplementary`](skills/icdm-supplementary/SKILL.md)：在单一 10 页全包含上限内取舍
  ——正文、cap 内附录、外部匿名仓库的分配，以及 short-paper 压缩计划。
- [`icdm-submission`](skills/icdm-submission/SKILL.md)：截止前审计——track 与匿名规则、10 页
  全包含核查、triple-blind 清扫，以及对 AoE 截止的最后一周排序。

评审阶段与之后：

- [`icdm-review-process`](skills/icdm-review-process/SKILL.md)：triple-blind 机制、
  Accept / **录为 Short** / Reject 的结果空间、混合的 data-mining 审稿群体，以及无 rebuttal
  姿态。
- [`icdm-author-response`](skills/icdm-author-response/SKILL.md)：如何为可能完全没有 rebuttal
  的会议做准备，以及若存在 response 窗口如何在不破坏匿名下简洁作答。
- [`icdm-camera-ready`](skills/icdm-camera-ready/SKILL.md)：IEEE camera-ready、eCopyright、
  去匿名、现场报告，以及若被录为 short paper 的压缩路径。

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md)：每个官方 URL 及访问
  日期、访问方式说明、已核验事实清单与待核实登记。
- [`resources/external_tools.md`](resources/external_tools.md)：track 征稿、IEEE Xplore、获奖
  页、dblp 与每届作者检查项。
- [`resources/exemplars/library.md`](resources/exemplars/library.md)：经获奖名录核验的 ICDM
  范例（Isolation Forest、Fast RWR、隐式反馈 CF、PEGASUS、SLIM、DTW averaging），附
  KDD/CIKM/WSDM/SDM 误attribution 防护。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)：
  一个虚构的 before/after 改写，进入 ICDM 首页弧线：data regime → mechanism → baseline + scale
  → discovery validity。
- [`resources/code/README.md`](resources/code/README.md)：共享 ML-conference 可复现工具包的
  适配层，附 triple-blind artifact 提醒。

## 建议顺序

1. **选会**：`icdm-topic-selection`（venue 契合 + track 分叉），再 `icdm-workflow`（单截止
   日历与到八月的漫长等待）。
2. **构建**：`icdm-experiments` + `icdm-reproducibility`，同时用 `icdm-writing-style` 与
   `icdm-related-work` 写作。
3. **打包**：在截止周之前完成 `icdm-artifact-evaluation` 与 `icdm-supplementary`；随后按 10 页
   全包含上限做 `icdm-submission` 审计。
4. **等待与阅读**：用 `icdm-review-process` 读评审包；仅当该届提供 response 窗口时用
   `icdm-author-response`。
5. **出版**：录用后 `icdm-camera-ready`，并备好 short-paper 分支。

## 安装

本包以 Claude Code 插件形式发布。在本仓库根目录：

```bash
# 添加以本目录为根的 marketplace，再安装插件
claude plugin marketplace add ./ICDM-Skills
claude plugin install icdm-skills
```

也可让 agent 直接指向单个 `skills/icdm-*/SKILL.md`：每个 skill 自包含，在 frontmatter
description 中声明范围，并以结构化输出格式收尾，便于跨 skill 组合。

## 范围与免责声明

- 本包就 ICDM 投稿的**策略、结构与证据**给出建议，不是 CFP 本身：任何与当届官方指示冲突之处，
  以官方为准。
- 事实带日期。所有具体项均于 2026-07-09 依据 source map 核验，并于 2026-11-24 重新核验；不稳定项（截止、费用、chair、
  rebuttal 机制）以“每届变”或“待核实”表述，而非断言。
- 请勿将此处文字粘入论文。worked example 系刻意虚构，exemplar library 记录的是定位模式，而非
  可复用文句。

## 维护说明

- 上表每个带日期的事实都是 **2026 届锚点，而非规则**。ICDM 每届重设 track（Applied 与 Blue
  Sky 是 2026 新增）、各 track 审稿模型、页数处理、short-paper 机制与任何 response 政策。
- 涉及 deadline 的建议前，务必重开**对应 track** 的征稿——Research 与 Applied 现在匿名规则不同，
  “ICDM CFP” 在本会已属歧义。
- 标注 **待核实** 的事实（未来的 rebuttal 窗口、Applied camera-ready 日期冲突、费用、ICDM 2027）在作为
  事实告知作者前必须实时核验。
- 若征稿页与 IEEE Xplore 或委员会页冲突，以更新的官方指示为准并记录冲突。
