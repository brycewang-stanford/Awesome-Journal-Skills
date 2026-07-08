# PLDI Skills

面向 **PLDI（ACM SIGPLAN Conference on Programming Language Design and
Implementation）** 论文的 12 个 agent skills。PLDI 是 SIGPLAN 在语言设计、
编译器、程序分析、运行时、程序综合与验证工具方向的旗舰会议。本包覆盖一次完整的
PLDI 投稿战役：判断论文的决定性证据是否真的是"实现 + benchmark"形态、按照
SIGPLAN 自己发布的 Empirical Evaluation Guidelines 构建评测、通过 HotCRP 的
double-blind 投稿与短促的二月 author response、把录用论文以 **PACMPL Issue
PLDI** 期刊文章形式出版，并在录用后的 artifact evaluation 中通过 Zenodo 存档
拿到 Functional / Reusable / Available 徽章。

官方依据核验日期：**2026-07-08**。核验对象包括 PLDI 2026（第 47 届）Call for
Papers、pldi26.sigplan.org 的 research-papers / research-artifacts /
important-dates / organizing-committee 页面、SIGPLAN 博客的 "PLDI will join
PACMPL" 公告、ACM Digital Library 的 PACMPL 页面，以及 SIGPLAN Empirical
Evaluation Guidelines。核验环境中对 `sigplan.org` 与 `pldi26.sigplan.org` 的
直接抓取返回 403，因此官方页面内容通过对准确 URL 的搜索引擎渲染读取，并与
ACM DL、dblp 交叉核对；完整的来源链与所有仍标注"待核实"的条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## PLDI 在结构上的特殊之处

以下五条经核验的机制驱动了本包中的大部分建议，也解释了从 ML 会议或软件工程
venue 转来的作者最常犯的错误：

- **一个"出版期刊的会议"。** 自 PLDI 2023 起，录用论文以 PACMPL（Proceedings
  of the ACM on Programming Languages）Issue PLDI 形式出版（Vol 7 = 2023、
  Vol 8 = 2024、Vol 9 = 2025），与 POPL、OOPSLA、ICFP 同属一本 Gold Open
  Access 期刊。评审仍是会议节奏，产出却是期刊文章，引用也要用期刊格式。
- **每年只有一个 11 月截稿。** PLDI 2026 论文截稿为 2025 年 11 月 13 日，经
  HotCRP（`pldi2026.hotcrp.com`）提交；author response 为 2026 年 2 月
  17-21 日，notification 3 月 5 日，会议 6 月 15-19 日在美国科罗拉多州
  Boulder 举行。错过 11 月就是等一年。
- **格式红线有明文罚则。** 正文文本不超过 20 页（参考文献除外），使用单栏
  `acmsmall` 版式（10 pt 字号、12 pt 行距），该格式为兼容 PACMPL 而定 ——
  偏离格式的明文后果是 **summary rejection**。
- **有牙齿的 artifact 文化。** artifact evaluation 在论文录用后进行；徽章为
  Functional、Reusable、Available；Available 徽章要求把完整 artifact 存档到
  Zenodo 并获得 DOI，而 Zenodo 的版本机制使 artifact 没有 camera-ready
  截止日期。徽章会印在 PACMPL 文章上。
- **成文的测量标准。** SIGPLAN Empirical Evaluation Guidelines（Blackburn、
  Hauswirth、Berger、Hicks、Krishnamurthi，2018）给了审稿人一页 checklist：
  claim 清晰、对比得当、benchmark 选择有原则、数据分析充分 —— 本包教你在
  审稿人拿起它之前先自己过一遍。

其他已核验事实：double-blind 评审已实行多年；最多 10% 的录用论文可评为
Distinguished Paper（PLDI 2025 为 89 篇中的 6 篇）；PACMPL 的 APC 为 400 美元
（SIGPLAN 补贴，无力支付者由 SIGPLAN 代付），且 ACM 自 2026 年 1 月 1 日起
全面开放获取；领导层逐届轮换（2026：General Chair Bor-Yuh Evan Chang，
Program Chair Manu Sridharan）。核验日 PLDI 2027 网站仍是占位页 —— 其截稿
日期属于"待核实"，不能默认为"2026 年 11 月"。

## 12 个 Skills

选题与写作：

- [`pldi-topic-selection`](skills/pldi-topic-selection/SKILL.md)：检验论文
  证据是否为"实现 + benchmark"形态，在 PACMPL 家族内部（POPL / OOPSLA /
  ICFP，同一期刊、不同评审群体）或向外（ASPLOS、CGO、CAV、ICSE/FSE、系统
  venue）改道。
- [`pldi-writing-style`](skills/pldi-writing-style/SKILL.md)：首页四问
  （难点案例、洞见句、实现基座、头条数字）、贯穿全文的 running example
  纪律，以及 claim ledger。
- [`pldi-related-work`](skills/pldi-related-work/SKILL.md)：逐条引用写出
  技术差量、覆盖 SIGPLAN 家族近几届、PACMPL 时代的期刊格式引用，以及用
  dblp 核验 venue 归属（LLVM、CompCert、RustBelt 都是经典陷阱）。

证据构建：

- [`pldi-experiments`](skills/pldi-experiments/SKILL.md)：把 benchmark 套件
  当论证来选、用最强配置作 baseline、为每个机制设计 ablation，并同时报告
  运行时、编译时间与内存三种"货币"。
- [`pldi-reproducibility`](skills/pldi-reproducibility/SKILL.md)：把 SIGPLAN
  checklist 落到实践：warmup 制度、30 次重复与方差报告、锁定工具链版本、
  跨平台限定 claim、用脚本而非散文记录协议。
- [`pldi-supplementary`](skills/pldi-supplementary/SKILL.md)：哪些内容留在
  20 页正文、哪些进 appendix、哪些进匿名代码包，以及压缩包的匿名清扫。

流程推进：

- [`pldi-submission`](skills/pldi-submission/SKILL.md)：HotCRP 操作、格式与
  页数红线、工具类论文的身份泄漏扫描，以及 summary-rejection 分诊表。
- [`pldi-review-process`](skills/pldi-review-process/SKILL.md)：实现者型 PC
  如何读论文、从截稿到 PACMPL 出版的逐阶段管线，以及 Distinguished Paper
  机制。
- [`pldi-author-response`](skills/pldi-author-response/SKILL.md)：四类意见的
  分诊（soundness 永远第一）、不引入新贡献的边界，以及五天窗口内可用的
  response 骨架。
- [`pldi-workflow`](skills/pldi-workflow/SKILL.md)：从 11 月截稿倒排计划，
  并管理长尾：2 月 response、3 月决定、春季 artifact evaluation、6 月报告。

录用之后：

- [`pldi-camera-ready`](skills/pldi-camera-ready/SKILL.md)：把去匿名做成
  diff、PACMPL 元数据与 ORCID、开放获取费用处理，以及文章 / artifact /
  报告三条时钟的协调。
- [`pldi-artifact-evaluation`](skills/pldi-artifact-evaluation/SKILL.md)：
  徽章阶梯、十分钟 smoke test、claim 到脚本的映射表，以及 Zenodo 存档。

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md)：
  12 条带日期的官方来源、已核验事实清单与"待核实"登记表。
- [`resources/exemplars/library.md`](resources/exemplars/library.md)：从
  DART（2005）到带徽章的 PACMPL 时代论文（2023）共 5 篇经 venue 核验的
  范文，附常见误归属陷阱。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)：
  一篇虚构编译器论文的首页从"产品发布腔"改写为 PLDI 论证弧线。
- [`resources/external_tools.md`](resources/external_tools.md)：HotCRP、
  PACMPL、dblp、Zenodo、acmart 与 Empirical Evaluation Guidelines 的入口，
  附作者侧检查项。
- [`resources/code/README.md`](resources/code/README.md)：把仓库级共享方法
  工具包改造成可拿徽章的 PL artifact 脚手架。

## 一次 PLDI 战役的推荐路线

1. **截稿前 12 周以上（夏末）：** 先跑 `pldi-topic-selection`；如果 claim 的
   动词是"我们证明"，现在就去讨论 POPL，不要拖到 10 月。用
   `pldi-experiments` 锁定 benchmark 套件与 baseline。
2. **前 8 周：** 用脚本固化测量协议（`pldi-reproducibility`），让论文数字与
   未来的 artifact 无法分叉；按 `pldi-writing-style` 的首页四问开始写作。
3. **最后一个月：** 关闭 claim ledger、做 related-work 差量审计、组装补充
   材料并完成匿名清扫，最后对照 `pldi-submission` 的 summary-rejection
   分诊表再上传 HotCRP。
4. **二月：** 在五天窗口内执行 response 剧本 —— soundness 质疑最优先、
   用章节与行号作引证、绝不引入新贡献。
5. **录用当周：** 立即启动 artifact 打包（`pldi-artifact-evaluation`），
   再做 camera-ready 的 diff 式去匿名与 PACMPL 元数据
   （`pldi-camera-ready`），并把六月的报告放进某个人的日历。

## 本包纠正的常见误解

- "PLDI 出版会议论文集" —— 2023 年起不再如此；引用要写 PACMPL 的卷 / 期 /
  文章号，且在把一篇 PACMPL 论文称为 PLDI 论文之前先看 *issue* 名。
- "期刊版式意味着页数宽松" —— 20 页正文红线的明文后果是 summary
  rejection，与期刊形态无关。
- "artifact 是可选的加分项" —— 徽章会印在文章上，评估在 notification 之后
  立即开始，Available 徽章要求 Zenodo 的 DOI 存档而非 GitHub 链接。
- "一张大幅加速表就是评测" —— SIGPLAN 的成文 checklist 要求 claim、对比、
  benchmark 选择理由与方差报告，审稿人会逐条对照。

## 维护说明

- 上文所有带日期的事实都是 **2026 届的快照**，且多数经由搜索渲染读取（直接
  抓取被 403 拦截）；在给出任何截稿、页数或徽章建议之前，务必打开当届官方
  页面。
- PLDI 2027 的日期、地点与截稿在 2026-07-08 尚未公布，不要把"大约 11 月"
  外推成建议；请查
  https://conf.researchr.org/home/pldi-2027 与 SIGPLAN announcements 页面。
- 各届的 chairs、HotCRP 实例、AE 机制、response 窗口与开放获取条款都会轮换
  或演化；易变项清单见 source map。
