# The Web Conference Skills（万维网大会技能包）

面向 **ACM Web Conference（WWW，万维网大会）** 投稿的 12 个 agent skills。WWW 是
Web 研究的旗舰会议——研究对象是 Web 本身：网页图、平台、在线市场、搜索系统、用户
行为与社会影响，自 1994 年 CERN 的 WWW1 起每年举办。本包围绕五个使 WWW 投稿策略
不同于 ML/数据挖掘兄弟会议的结构性事实组织：

1. **按主题 track 审稿。** 2026 届设十个 research tracks，各有自己的 track chairs
   与审稿人池；track 选择决定"谁来审、按什么证据标准审"，其分量不亚于选会本身。
2. **作者名单在 abstract 截止时冻结**，比正文截止早一周：此后不得增删或调整顺序；
   且每位作者在 research tracks 累计投稿不得超过 7 篇。
3. **单一 PDF、三个区域。** 2026 年规则：正文 8 页且必须自洽（审稿人可不读第 8 页
   之后的内容），References 与可选 Appendix 共享剩余空间，全文上限 12 页；没有独立
   的补充材料上传通道。
4. **"Web 原生性"门槛。** 本会标志性的拒稿理由是"看不出为什么这是一篇 WWW 论文"；
   贡献必须依赖链接结构、平台机制、真实用户行为或 web 规模约束——仅仅"在 web 数据
   上做了实验"是不够的。
5. **ACM 出版流程与 artifact 徽章。** 录用论文经 ACM e-rights 与 TAPS 进入 Digital
   Library，统一 12 页（其中 8 页正文）预算；随 camera-ready 提交存档仓库（带 DOI）
   可获 "Artifacts Available" 徽章。

官方依据核验日期：**2026-07-08**。已核验：WWW 2026 官网（第 35 届，迪拜，会期在
周期中途由 4 月改期至 2026 年 6 月 29 日 - 7 月 3 日）、Research Tracks CFP、
Important Dates 页、Short Papers 与 Web4Good 征稿、Artifact Badging 征稿、ACM DL
2025-2026 会议录记录、SIGWEB 场地公告与 IW3C2 会史。构建环境的网关阻断了对会议
域名的直接抓取，因此页面内容通过对官方 URL 的搜索引擎渲染核验，并与 ACM DL、dblp
交叉比对——完整的访问方式说明、来源清单与全部"待核实"条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 已核验的 2026 届锚点事实

| 事实 | 2026 届取值 | 波动性 |
|---|---|---|
| 届次 | 第 35 届，阿联酋迪拜；改期至 2026-06-29 至 07-03 | 每届 |
| Research tracks | 十个（从 Graph algorithms 到 Responsible Web） | 几乎每届重划 |
| 时间线 | 摘要 2025-09-30；全文 2025-10-07；rebuttal 11-24 至 12-01；通知 2026-01-13；camera-ready 2026-01-25（AoE，严格） | 每届 |
| 格式 | `\documentclass[sigconf, anonymous, review]{acmart}`；正文 8 页 + 参考文献 + 附录，总计 ≤ 12 页；前 8 页自洽 | 每届 |
| 作者规则 | abstract 截止即冻结名单；每人 ≤ 7 篇；LLM 不能署名作者 | 每届 |
| 投稿平台 | 2026 research tracks 用 EasyChair（2024-25 用 OpenReview；2026 Industry 用 OpenReview） | 每 track、每届 |
| 预印本 | 允许匿名 arXiv/SSRN 版本存在，但论文不得引用它 | 每届 |
| 同届后续通道 | Short papers（4 页含参考文献，11 月截止）与 Web4Good（11 月截止），均入主会议录 | 每届 |
| 出版 | ACM DL；录用论文统一 12 页/8 页正文；camera-ready 时可申请 Artifacts Available 徽章 | 每届 |
| 治理 | 2022 年起由 ACM/SIGWEB 与指导委员会管理；1994-2022 由 IW3C2 运营；2018 年更名 The Web Conference | 历史事实 |

除两位 general co-chairs 外的主席名单、rebuttal 具体机制、注册费、录取率与
ACM Open 费用金额均未能核实，已在 source map 中标注 **待核实**，绝不凭记忆断言。

## Skills 一览

选题与规划：

- [`webconf-topic-selection`](skills/webconf-topic-selection/SKILL.md) —— Web
  原生性检验、十个 track 的匹配、通道选择（长文/短文/Web4Good/Industry/
  workshop），以及向 WSDM、SIGIR、CIKM、KDD、ICWSM、WebSci 的分流。
- [`webconf-workflow`](skills/webconf-workflow/SKILL.md) —— 从秋季截稿到次年
  夏季开会的年度日历、按 abstract 截止倒排、同届 fallback 决策树，以及 2026 年
  改期带来的行程留余量教训。

论文构建：

- [`webconf-writing-style`](skills/webconf-writing-style/SKILL.md) —— 第一页的
  web 原生机制句、面向计算+社会科学混合评审组的写法、"形容词必须挂数字"、8 页
  压缩法。
- [`webconf-related-work`](skills/webconf-related-work/SKILL.md) —— 三十年 WWW
  会议录中的谱系定位、与兄弟会议的对照句、venue 归属卫生检查、"自家预印本不得
  引用"规则。
- [`webconf-experiments`](skills/webconf-experiments/SKILL.md) —— 主张-证据
  契约、数据集来源与新鲜度、时间/流行度/重复三类泄漏、对称调参基线、何时必须有
  在线或用户实验。
- [`webconf-reproducibility`](skills/webconf-reproducibility/SKILL.md) —— web
  数据的"冻结/衰减/不可重放"三态模型、快照固定、确定性审计与时间切分诚实性。

打包与投稿：

- [`webconf-supplementary`](skills/webconf-supplementary/SKILL.md) —— 三容器
  模型（8 页正文 / PDF 尾部 / 外部 artifact）、参考文献与附录的零和空间、匿名
  链接模式。
- [`webconf-artifact-evaluation`](skills/webconf-artifact-evaluation/SKILL.md)
  —— Artifacts Available 徽章标准、DOI 存档仓库、受限 web 数据的分级共享、抗
  失效打包。
- [`webconf-submission`](skills/webconf-submission/SKILL.md) —— 截稿前审计：
  作者名单冻结、track 申报、7 篇上限、页面分区算术、EasyChair 档案与匿名清扫。

审稿阶段与其后：

- [`webconf-review-process`](skills/webconf-review-process/SKILL.md) —— track
  内双盲审稿、四个反复出现的决策问题、流水线日期，以及从拒稿意见读出分流信号。
- [`webconf-author-response`](skills/webconf-author-response/SKILL.md) —— 一周
  rebuttal：审稿人立场分类、回应"web 契合度"质疑、小而诚实的新证据、与 8 页
  正文预算相容的 camera-ready 承诺。
- [`webconf-camera-ready`](skills/webconf-camera-ready/SKILL.md) —— 12 天窗口：
  去匿名清扫、e-rights 与 TAPS、ACM Open 核查、注册，以及随行的 artifact 徽章
  申请。

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) ——
  全部来源 URL 与访问日期、已核验事实清单、访问方式说明与待核实登记表。
- [`resources/external_tools.md`](resources/external_tools.md) —— 官方网站、
  会议录、平台链接与每届必查项。
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 五篇
  经会议录核验的 WWW 论文（LINE、NCF、VAE-CF、HAN、Twitter 测量研究）及
  KDD/SIGIR/UAI 误归属防护清单。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  —— 虚构论文的摘要+引言改写示范：web 原生第一页弧线。
- [`resources/code/README.md`](resources/code/README.md) —— 共享 ML 会议可复现
  工具包的适配说明，外加爬取清单与链接衰减核算等 web 特有实践。

## 建议使用顺序

1. **选路**：`webconf-topic-selection`（先 web 原生性、后 track），用
   `webconf-workflow` 排日历。
2. **构建**：`webconf-experiments` + `webconf-reproducibility`，同步用
   `webconf-writing-style` 与 `webconf-related-work` 写作。
3. **打包**：`webconf-supplementary` 与 `webconf-artifact-evaluation`，最后跑
   `webconf-submission` 审计——作者名单与平台档案务必在 abstract 截止前敲定。
4. **应答**：先 `webconf-review-process` 读懂意见，再 `webconf-author-response`
   写 rebuttal。
5. **出版**：`webconf-camera-ready`，artifact 徽章随 camera-ready 一并提交。

## 安装

```bash
# 在仓库根目录执行
claude plugin marketplace add ./The-Web-Conference-Skills
claude plugin install the-web-conference-skills
```

也可直接把任一 `skills/webconf-*/SKILL.md` 作为独立指令文件使用；每个 skill 在
frontmatter 中声明适用范围，并以结构化输出块结尾，便于彼此组合。

## 范围与免责声明

- 本包提供的是 WWW 投稿的**策略、结构与证据**建议，不是 CFP 本身；与当届官方
  页面冲突时，一律以官方页面为准。
- 所有具体数字均为 **2026 届锚点**（核验于 2026-07-08）；2026 届自己就在周期内
  改了会期，足证波动性。行动前请重开当届官网核对每个截止日期、页数与费用。
- 本包任何文字都不应粘贴进论文。示例论文是刻意虚构的；范文库记录的是定位模式，
  不是可引用的结果。

## 维护说明

- 每届重查 track 清单——几乎每年重划，特设 track（如 2026 的 Web4Good）时有
  时无。
- 每届、每 track 重查投稿平台：research tracks 曾在 2025 与 2026 之间从
  OpenReview 切换到 EasyChair。
- source map 中标注"待核实"的条目（主席、费用、rebuttal 机制、录取率、ACM Open
  条款）在向作者陈述前必须实时核验。
- 来源冲突时，以最新的当届官方页面或主席直接沟通为准，并在 source map 中记录
  冲突与访问日期。
