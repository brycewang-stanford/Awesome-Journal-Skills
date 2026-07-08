# INTERSPEECH Skills（中文说明）

面向 **Interspeech** 论文的 12 个 agent skills。Interspeech 是 **ISCA（International
Speech Communication Association，国际语音通讯协会）** 的年度旗舰会议——注意不要与
同缩写的计算机体系结构会议混淆。它是覆盖面最广的语音学术会议：语音识别（ASR）、
语音合成与音色转换、说话人与语种识别、语音学与韵律、口语对话、语音健康、语音资源
等方向在同一个技术程序里评审。本包覆盖完整年度周期：选会定位、严格的 4 页格式、
CMT 投稿与截稿后的 paper-update 窗口、rebuttal、ISCA Archive camera-ready、音频
artifact，以及会议现场。

官方依据核验日期：**2026-07-08**。核验对象：Interspeech 2026（悉尼）官网的 Call for
Papers、Submission Policy、Registration 页面；Interspeech 2025 政策页（作为最近先
例）；ISCA Archive；ISCA 的 upcoming-conference 与奖项页面；以及 ASSTA 的 2026 CFP
镜像。核验环境的网关拦截了对 ISCA 及会议域名的直接抓取，因此官方页面内容经由精确
URL 的搜索引擎渲染读取并交叉比对；完整证据链（含所有 待核实 条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## Interspeech 与相邻会议的关键差异

- **4 页正文，没有附录。** 常规论文为 4 页内容 + 1 页（仅限参考文献与致谢）。
  不存在被评审的补充材料——决定录用的证据必须全部放进 4 页。2026 年新设
  **Long Paper track**（据报道：8 页 + 2 页文献，目标录用率低于 30%）。
- **Paper-update 窗口。** 在主流会议中独一无二：截稿后约一周内（2026 年为
  2 月 25 日截稿 → 3 月 4 日更新截止）可以更新 PDF，但元数据冻结——这是官方
  许可的校对通道，不是延期。
- **评审人会"听"论文。** 合成、转换、增强类论文的音频 demo 页会被当作证据
  消费——同时也是最常见的匿名泄漏点。
- **双匿名 + 匿名期。** 自 2025 年起，从截稿前一个月到决定公布期间，禁止在网上
  （含 arXiv）发布非匿名版本。
- **开放获取、无版面费。** 所有论文进入 ISCA Archive（isca-archive.org），DOI
  前缀 `10.21437`；成本模型是注册费——且至少一位作者完成注册，论文才会进入
  会议论文集。
- **混合评审团。** 语音学家与工程师在相邻领域评审；论文必须同时经得起
  "显著性检验在哪里"和"错误分析在哪里"两类读者的追问。

## Skills 一览

| Skill | 用途 |
| --- | --- |
| [`interspeech-topic-selection`](skills/interspeech-topic-selection/SKILL.md) | 用"模态测试"（换成纯文本 transcript 后主张是否仍成立）判断适配度，并在 Interspeech、ICASSP、ASRU/SLT、Odyssey、SSW、ACL 系与语音期刊之间路由。 |
| [`interspeech-workflow`](skills/interspeech-workflow/SKILL.md) | 管理年度时钟：冬季截稿、update 窗口、春季 rebuttal、6 月决定、注册与论文集的绑定、9 月会议，并为每个阶段指定负责人。 |
| [`interspeech-writing-style`](skills/interspeech-writing-style/SKILL.md) | 在 4 页内实现"一遍读取"：带数字的摘要、基于 diff 的方法描述、协议一句话化，以及诚实的压缩顺序。 |
| [`interspeech-related-work`](skills/interspeech-related-work/SKILL.md) | 覆盖五条文献线（ISCA Archive 谱系、IEEE 姊妹会、challenge 体系、ML/NLP 交叉、语料库论文），并避开 venue 误标注陷阱。 |
| [`interspeech-experiments`](skills/interspeech-experiments/SKILL.md) | 按任务惯例匹配指标（WER、MOS/CMOS、EER/minDCF、PESQ/STOI），基线锚定公开 recipe，对正确的随机性来源做显著性检验。 |
| [`interspeech-reproducibility`](skills/interspeech-reproducibility/SKILL.md) | 钉住五个漂移通道：语料版本、文本规范化、trial list、主观测试协议、随机种子——并连"量尺"（打分脚本）一起发布。 |
| [`interspeech-supplementary`](skills/interspeech-supplementary/SKILL.md) | 管理三层货架：4 页正文、文献页、可选附件；策划评审人真正会打开的音频样例页。 |
| [`interspeech-artifact-evaluation`](skills/interspeech-artifact-evaluation/SKILL.md) | 打包音频 demo、recipe 与 checkpoint：评审期匿名、录用后永久公开，附语料许可链与说话人同意的合规检查。 |
| [`interspeech-submission`](skills/interspeech-submission/SKILL.md) | 投稿前 CMT 终审：4+1 格式与 PDF 校验器、含 demo 页的匿名清查、领域与元数据策略、update 窗口计划。 |
| [`interspeech-review-process`](skills/interspeech-review-process/SKILL.md) | 建模按 area 组织的评审管线、年轻的 rebuttal 能撬动什么、oral/poster 分配逻辑、奖项与拒稿信解码。 |
| [`interspeech-author-response`](skills/interspeech-author-response/SKILL.md) | 面向科学/工程混合评审组，只用 4 页已提交记录作答，按对方"方言"回应，写给 meta-reviewer 看。 |
| [`interspeech-camera-ready`](skills/interspeech-camera-ready/SKILL.md) | 把录用转化为正确的 ISCA Archive 条目：去匿名顺序、注册绑定、DOI 元数据、带音频备份方案的报告准备。 |

## Resources 一览

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 10 个来源（URL + 核验日期）、已核验的 2026 事实、仅见于二手来源的条目、待核实清单、网关访问方式说明。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口 + 作者侧五道核验流程 + 页面冲突处理规则。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 经 ISCA Archive 核验的 5 篇范文（Conformer、SpecAugment、ECAPA-TDNN、Tacotron、SUPERB），含 DOI、自检问题与误标注防护清单。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构流式 ASR 论文首页：从 NLP 味道的初稿改写为 Interspeech"一遍读取"形态的前后对照。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享 ML 会议可复现性工具包的适配器 + 5 项语音特有的人工检查。 |

## 安装与使用

作为 Claude Code 插件（本目录自带 marketplace 清单）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./INTERSPEECH-Skills
claude plugin install interspeech-skills
```

也可直接使用文件：每个 `skills/interspeech-*/SKILL.md` 都是独立的指令文件，其
frontmatter `description` 描述触发时机。典型用法：

- "这篇 speech-LLM 论文投 Interspeech 还是 EMNLP？" → `interspeech-topic-selection`
- "帮我把稿子压到 4 页且不丢主张" → `interspeech-writing-style`
- "投稿前查一遍 demo 页有没有泄露身份" → `interspeech-artifact-evaluation`
- "录用了，去悉尼之前要做什么？" → `interspeech-camera-ready`

## 包结构

```text
INTERSPEECH-Skills/
├── .claude-plugin/                 # plugin.json + marketplace.json（声明 12 个 skills）
├── README.md                       # 英文说明
├── README.zh-CN.md                 # 本文件
├── LICENSE                         # MIT
├── assets/cover.svg                # 封面（声波图案）
├── skills/
│   └── interspeech-<topic>/SKILL.md  # 12 个 skills，一目录一技能
└── resources/
    ├── README.md                   # 资源导览与建议路径
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md              # 共享可复现性工具包适配器
```

## 建议使用路径

1. **动笔之前**——先跑 `interspeech-topic-selection` 做模态测试与领域路由；
   再翻 [`resources/exemplars/library.md`](resources/exemplars/library.md)，
   校准"录用形态"在你的任务线里长什么样。
2. **搭建证据期**——把 `interspeech-experiments` 与 `interspeech-reproducibility`
   放在代码库旁边用：指标-任务对照、显著性检验、五个漂移通道，都是越早装配
   越便宜的东西。
3. **写作期**——`interspeech-writing-style` 管正文的 4 页压缩，
   `interspeech-related-work` 管定位与引用卫生，`interspeech-supplementary`
   管音频样例页；对照 worked example 的前后改写检查首页。
4. **截稿周**——`interspeech-submission` 从格式、匿名、CMT 元数据到
   update 窗口计划全量过一遍；`interspeech-artifact-evaluation` 清查 demo 页
   与仓库的身份泄漏。
5. **投稿之后**——`interspeech-review-process` 校准各阶段预期；rebuttal 窗口
   开启时用 `interspeech-author-response`；6 月放榜后按结果走
   `interspeech-camera-ready`（含注册绑定与报告准备）或转入 2027 修订计划。

## 2026 周期锚点（历史快照，非永久规则）

- Interspeech 2026：**澳大利亚悉尼，2026 年 9 月 27 日 – 10 月 1 日**，与 ASSTA
  联合主办；主题 **"Speaking Together"**。
- 2026 管线：投稿系统开放 1 月 17 日 · 论文截稿 **2 月 25 日** · paper-update
  截止 **3 月 4 日** · rebuttal 据报道为 4 月 24 日 – 5 月 1 日（待核实）· 通知
  **6 月 5 日** · camera-ready **6 月 19 日** · 早鸟注册截止 **7 月 15 日** ·
  标准注册截止 8 月 16 日。
- 格式：常规论文 4 页内容 + 1 页文献/致谢；Long Paper track 为 2026 年新设
  （参数据报道，待核实）。
- 论文集：ISCA Archive，开放获取，DOI 前缀 10.21437，无作者费用。
- 后续届次：**Interspeech 2027，巴西圣保罗，2027 年 8 月 29 日 – 9 月 2 日**
  （首次在南美举办）；Interspeech 2028，美国圣安东尼奥。

## 事实纪律

全包区分三类陈述并保持可辨识：

1. **已核验的 2026 周期事实**——可追溯到 source map 编号来源（2 月 25 日截稿、
   6 月 19 日 camera-ready、悉尼会期）。
2. **据报道的事实**——仅见于二手渲染并如实标注（rebuttal 窗口、Long Paper 参数、
   2026 委员会名单）。
3. **待核实条目**——核验时未能确认，一律以问题而非事实的口吻表述（附件大小上限、
   评审表措辞、AI 使用政策、全部 2027 规则）。

若发现任一 skill 把第 2/3 类内容写成第 1 类，请视为 bug，对照官方页面修复。

## 维护说明

- 上述每个日期都是**悉尼周期快照**。ISCA 各届由轮换的本地委员会与 Technical
  Program Chairs 运营；tracks、rebuttal、投稿系统都不会自动延续到圣保罗 2027。
- 本包在网关受限环境下核验（依赖渲染而非直接抓取）；每个周期的第一项维护任务
  是直接打开主要 URL 并刷新
  [`resources/official-source-map.md`](resources/official-source-map.md)。
- 新增范文必须按 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的流程对照 ISCA Archive 核验——语音领域的名篇散落在
  ICASSP/NeurIPS/ICML/LREC 各处，venue 误标注是本领域的特征性错误。

## 许可证

MIT——见 [`LICENSE`](LICENSE)。英文说明见 [`README.md`](README.md)。
