# COLT Skills

面向 COLT（Annual Conference on Learning Theory，学习理论年会）论文的 12 个 agent
skills。COLT 是纯学习理论的 theorem-first 顶级会议，覆盖 statistical learning、
online learning 与 bandits、优化理论、RL theory 与 lower bounds，由 Association
for Computational Learning 主办，录用论文发表于 PMLR（Proceedings of Machine
Learning Research）。

COLT 在结构上与大型实证类 ML 会议差异很大，本包围绕这些差异构建，而不是套用通用
会议模板：

- **证明就是 artifact。** COLT 没有 artifact-evaluation track、没有 reproducibility
  checklist、也没有实验要求；论文凭定理被录用，替代 artifact review 的是审稿人对
  证明的逐行核验。
- **单一 PDF、附录不限页。** 2026 周期允许正文 12 页 PMLR 格式（references 不计），
  references 与 appendix 不限页数，全部装进同一个 PDF——因此附录架构本身是一等
  写作问题。
- **双匿名 + 知情 Area Chair。** 审稿人看不到作者姓名，但 AC 知道；在 rebuttal
  期间，AC 可应审稿人请求、在其认为必要时向该审稿人披露作者身份。
- **CMT 而非 OpenReview。** 2025 与 2026 两个周期均通过 Microsoft CMT 投稿，只有
  一个 AoE 截稿日（第 39 届为 2026-02-04；会议 2026-06-29 至 07-03，圣迭戈）。
- **Open problems 传统。** COLT 在正式 proceedings 中发表简短、可引用的
  open-problem 短文；提出一个参数化精确的好问题本身就是被认可的贡献形式。

官方依据核验日期：2026-07-08。已核验 learningtheory.org 的 COLT 2026 Call for
Papers 与会议页面、CMT 入口链接，以及 PMLR 卷页（v247 = COLT 2024、v291 = COLT
2025）。核验当日直接抓取官网被网络网关拦截，故所有事实经由上述官方页面的搜索
摘录完成核验；无法钉死的信息一律标注 待核实，绝不硬写。完整来源表见
`resources/official-source-map.md`。

## Skills

投稿流水线：

- `colt-submission`：核查 CMT 就绪、12 页 PMLR 正文、单 PDF 组装、双匿名格式、
  parallel-submission 禁令，以及 AoE 截稿前一周的有序检查。
- `colt-supplementary`：设计 PDF 内不限页的证明附录——正文/附录切分、restatable
  环境的定理复述、引理排序、便于审稿人核验的结构。
- `colt-workflow`：从唯一截稿日倒排项目日历，设置定理冻结与独立证明核验里程碑，
  贯穿 rebuttal、decision 与 camera-ready。

数学质量：

- `colt-reproducibility`：落实"可重推导"标准——完整证明、量词与常数纪律、外部
  引用结果的前提核查、假设编号记账。
- `colt-artifact-evaluation`：在这个没有 artifact track 的会议上，用核验台账
  （verification ledger）替代 artifact review；兼述少数带数值内容论文的代码规范。
- `colt-experiments`：先判断 COLT 论文是否需要任何数值内容，再为确有必要的情形
  设计诚实的 rate 曲线、separation 与 phase-transition 插图。

写作与定位：

- `colt-writing-style`：执行 theorem-first 叙事弧——形式化设定先于结果、informal/
  formal 定理成对出现、technique 段落、12 页预算分配。
- `colt-related-work`：跨 COLT/ALT 谱系、CS theory、ML 会议 theory track、统计学
  文献与 open problems 五条线，搭建量化的 known-vs-new 对照台账，并守住当年的
  重叠投稿规则。
- `colt-topic-selection`：检验结果是否 COLT 形状，对比 ALT、STOC/FOCS、NeurIPS/
  ICML/AISTATS、JMLR 与统计期刊的路由选择，含 open-problem 短文这一投稿载体。

评审与出版：

- `colt-review-process`：建模评审管线——理论专家审稿、correctness 优先的打分、
  知情 AC 的匿名设计、单轨会议的录用含义。
- `colt-author-response`：针对证明正确性、紧致性与技术新颖性三类质疑起草
  rebuttal，给出盒内自包含的修复与"损害可控"的让步。
- `colt-camera-ready`：产出 PMLR 出版版本——去匿名、rebuttal 承诺台账、编号
  稳定性、arXiv 版本对齐与引用元数据。

## 快速上手

可作为 Claude Code 插件安装（本目录自带 marketplace 清单，是自包含插件），也可
直接让 agent 读取 `skills/<name>/SKILL.md`。

新项目的典型顺序：

1. `colt-topic-selection` → 这是 COLT 论文、open-problem 短文，还是投错了会？
2. `colt-workflow` → 以当年截稿日为锚，倒排定理冻结与核验日期。
3. `colt-reproducibility` + `colt-artifact-evaluation` → 先关闭核验台账，再打磨
   文字。
4. `colt-writing-style` + `colt-supplementary` + `colt-related-work` → 成文；参照
   `resources/worked-examples/01-introduction.md` 与
   `resources/exemplars/library.md`。
5. `colt-submission` → 对照当年 CFP 做最终审计。
6. `colt-review-process` + `colt-author-response` → rebuttal 阶段。
7. `colt-camera-ready` → PMLR 出版与大会报告。

## 目录结构

```text
COLT-Skills/
├── .claude-plugin/           plugin.json 与 marketplace.json（声明 12 个 skills）
├── assets/cover.svg          封面图
├── resources/
│   ├── README.md             资源索引与建议工作流
│   ├── official-source-map.md  已核验来源、访问日期与 待核实 清单
│   ├── external_tools.md     官方链接与"禁止推断"规则
│   ├── exemplars/library.md  经 PMLR 核验的 COLT 论文（结果类型 × 技术）
│   ├── worked-examples/01-introduction.md  虚构的首页改写示例
│   └── code/README.md        共享 ML 会议代码工具包的适配说明
└── skills/colt-*/SKILL.md    12 个技能
```

## 事实纪律

- 本包中以事实口吻陈述的内容均于 2026-07-08 对照官方来源核验，并带有该锚定日期；
  当日无法核验的信息——2026 届 program chairs 姓名、通知与 camera-ready 日期、
  2026 届 open problems track、注册与报告义务、2026 届 PMLR 卷号——在技能文本与
  来源表中一律标注 待核实。
- COLT 每届随新 CFP 重新发布全部规则。请把 2026 事实当作历史锚点：任何涉及
  deadline 的行动前，务必重开 learningtheory.org 与当年 CFP，冲突处以官方现行
  文本为准。
- 示例论文逐篇匹配到 PMLR 卷页；exemplars 库同时记录了被排除的条目，以及导致
  venue 张冠李戴的 PMLR 卷号陷阱。

## 与姊妹会议包的区别

- 相对 **NeurIPS/ICML/ICLR 各包**：这里没有 reproducibility checklist、artifact
  badge 或 benchmark 审计流程——COLT 根本没有这些机制。本包的
  `colt-artifact-evaluation`、`colt-reproducibility` 与 `colt-experiments` 教的是
  真正的替代物：核验台账、可重推导审计、以及仅作插图用途的数值内容。
- 相对 **AISTATS 包**：AISTATS 论文在 checklist 制度下平衡定理与实验；COLT 论文
  只靠定理立足，附录在同一 PDF 内不限页，所以本包的写作、附录与评审技能围绕
  证明架构展开，而非理论-实验配对。
- 相对 **Computer-Science-Conference-Skills 中的 COLT 简版条目**：那份 roster
  文件用一页回答"COLT 是否是对的会"；本包覆盖该问题之后（或之中）的完整生命
  周期，并附带按周期核验的事实。

## 常见问题

- **COLT 要求实验吗？** 不要求。多数 COLT 论文没有实验；见 `colt-experiments`
  对"是否需要数值内容"的判定表。
- **附录会被审吗？** 附录在同一 PDF 内、属于被审记录；审稿人是否细读取决于正文
  的 proof overview 是否说服了他们。见 `colt-supplementary`。
- **可以同时投期刊吗？** 2026 规则明确禁止：COLT 在审期间不得投期刊，与
  proceedings 会议的实质重叠平行投稿同样被禁。见 `colt-submission`。
- **审稿人知道我是谁吗？** 默认不知道（双匿名），但 AC 知道，且在 rebuttal 期间
  可应审稿人请求向其披露。见 `colt-review-process`。
- **Open problem 短文值得写吗？** 若问题能完全形式化、易方向已证明、且能说清
  标准技术为何失效，它是被社区认可的贡献载体。见 `colt-topic-selection`。

## 维护说明

- 每个周期重新确认投稿系统（COLT 历史上更换过系统；2025-2026 使用 CMT）。
- 修改任何技能前，先对照新 CFP 复查页数规则、匿名机制、rebuttal 形式与重叠投稿
  条款。
- 更新示例论文时，须确认 PMLR 卷落地页写明 Conference on Learning Theory——
  PMLR 卷号在多个会议间交错。
- 每年新 CFP 发布后，把 `resources/official-source-map.md` 的核验日期与 待核实
  清单整体滚动一次，再回填各技能中的周期性事实。
