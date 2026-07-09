# ICASSP Skills

面向 **ICASSP —— IEEE 声学、语音与信号处理国际会议（IEEE International Conference on
Acoustics, Speech and Signal Processing）** 投稿的 12 个 agent skills。ICASSP 是 **IEEE 信号处理
学会（IEEE Signal Processing Society, SPS）** 的旗舰会议，覆盖面刻意很宽：语音与音频只是其中一个
方向，整个 program 还包括图像与视频、通信与雷达、传感器阵列、估计与检测理论，以及面向信号的机器
学习。本包覆盖完整年度流程 —— 选会与路由、IEEE 4+1 版式、CMS 平台的 single-blind 投稿、近年新增的
rebuttal、IEEE Xplore camera-ready、与任务匹配的评测，以及会议现场。

官方依据核验日期：**2026-07-09**。已核验 ICASSP 2026（Barcelona）的 paper kit 与投稿页面
（`cmsworkshops.com`、`2026.ieeeicassp.org`）、ICASSP 2027（Toronto）的 call、IEEE 信号处理学会
站点，以及用于 exemplar 核验的 dblp / IEEE Xplore。多个官方主页面被核验环境的 gateway 拦截（HTTP
403），因此通过搜索引擎对精确 URL 的渲染结果阅读，并相互交叉核对、与 dblp 对照。完整链路（含全部
仍标记为 待核实 的条目）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## ICASSP 与邻近会议的不同之处

以下机制驱动了各 skill 的建议 —— 也是从 double-blind 的 ML 会议、或从语音社区自己的 Interspeech
转投而来的作者最常犯的错：

- **Single-blind，而非匿名。** 投稿 PDF **必须**包含作者列表。这里的失败模式是作者信息*缺失*，而不是
  身份泄露 —— 与 OpenReview、ISCA 类会议正好相反。
- **4 页正文 + 1 页参考文献。** 常规论文为 4 页正文（含正文、图、参考文献），可选第 5 页**只能**放
  参考文献、经费致谢与 Compliance-with-Ethical-Standards 声明。**没有送审的 appendix**；决定录用的
  内容必须落在这 4 页上。
- **投稿用 CMS，而非 CMT。** ICASSP 使用 Conference Management Services（`cmsworkshops.com`），并按
  **EDICS** 主题类别路由 —— 这是 SPS 的真实指纹，区别于 Interspeech 使用的 Microsoft CMT。
- **现在有 rebuttal。** ICASSP 历史上*没有* author response；近几届新增了简短的 rebuttal 窗口（2026：
  据报道开放至约 2025-12-22）。不要默认它每届都有 —— 请核实。
- **9 月的时钟。** 投稿截止在秋季（ICASSP 2026：2025-09-17），与 Interspeech 的 2 月截止相差数月 ——
  这常常是语音论文选会的决定性因素。
- **其他发表路径。** **OJSP-ICASSP** 通道（8+1 页，在 IEEE Open Journal of Signal Processing 上开放
  获取发表，现场报告但不进 proceedings）与 **SPS 期刊报告** 选项（报告近期已录用的 SPS 期刊论文，不再
  评审）与标准通道并列。此外还有 Signal Processing **Grand Challenges**。
- **Proceedings 进 IEEE Xplore。** camera-ready 需通过 PDF eXpress 校验并签 IEEE 电子版权表；由注册作者
  现场（oral 或 poster）报告。

## ICASSP 与 Interspeech 的路由决策

由于语音只是 ICASSP 的一个方向，本包显式讲授这一取舍（见
[`skills/icassp-topic-selection`](skills/icassp-topic-selection/SKILL.md)）：

| 维度 | ICASSP（IEEE SPS） | Interspeech（ISCA） |
| --- | --- | --- |
| 范围 | 全部信号处理；语音是其中一个方向 | 仅语音与口语语言 |
| 匿名 | Single-blind（含作者列表） | Double-anonymous，含匿名期 |
| 截止 | 9 月 | 2 月下旬 |
| 平台 | CMS（`cmsworkshops.com`） | Microsoft CMT |
| 出版 | IEEE Xplore | ISCA Archive（开放获取） |

若贡献是**信号处理方法**、语音只是其一个应用实例，投 ICASSP；若贡献以**口语语言**为核心，投
Interspeech。

## Skills

| Skill | 作用 |
| --- | --- |
| [`icassp-topic-selection`](skills/icassp-topic-selection/SKILL.md) | 找出信号处理 primitive，并做 ICASSP-vs-Interspeech（及 ICIP/EUSIPCO/WASPAA/SPS 期刊/ML）路由。 |
| [`icassp-workflow`](skills/icassp-workflow/SKILL.md) | 跑年度时钟 —— 9 月截止、冬季 rebuttal、春季通知、Xplore camera-ready、5 月会议 —— 并分配 owner 与通道。 |
| [`icassp-writing-style`](skills/icassp-writing-style/SKILL.md) | 首页给出机制与任务匹配的 metric，并压进 IEEE 4+1 双栏、无送审 appendix 的版式。 |
| [`icassp-related-work`](skills/icassp-related-work/SKILL.md) | 在 SPS 期刊、IEEE 会议、兄弟会议与 ML 会议间定位，single-blind 下正常引用，避免张冠李戴。 |
| [`icassp-experiments`](skills/icassp-experiments/SKILL.md) | 让 metric 匹配任务规律（WER、SI-SDR、EER/minDCF、PSNR/SSIM、BER、RMSE），锚定强 baseline，扫工作条件。 |
| [`icassp-reproducibility`](skills/icassp-reproducibility/SKILL.md) | 交付评分 ruler，固定数据集版本与前端设置，控制随机性，使主结果可重建。 |
| [`icassp-supplementary`](skills/icassp-supplementary/SKILL.md) | 管理三层货架 —— 4 页正文、参考文献页、可选公开发布/多媒体 —— 并保持正文自洽。 |
| [`icassp-artifact-evaluation`](skills/icassp-artifact-evaluation/SKILL.md) | 打包代码、划分、scorer、checkpoint 与演示媒体（single-blind 下从一开始即可公开），即便没有 artifact badge。 |
| [`icassp-submission`](skills/icassp-submission/SKILL.md) | 最终 CMS 审核：4+1 与 PDF eXpress、single-blind 作者块检查、EDICS、伦理声明、9 篇上限与 desk-reject 触发。 |
| [`icassp-review-process`](skills/icassp-review-process/SKILL.md) | 建模 SPS 技术委员会流程、EDICS 路由、简短 rebuttal、oral/poster 分配，以及如何解读结论。 |
| [`icassp-author-response`](skills/icassp-author-response/SKILL.md) | 在简短 rebuttal 窗口内，基于 4 页记录回应本领域专家审稿人，面向委员会决策。 |
| [`icassp-camera-ready`](skills/icassp-camera-ready/SKILL.md) | 把录用转成正确的 IEEE Xplore 条目：PDF eXpress、IEEE 版权表、在录用范围内整合审稿意见、注册。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个来源（含 URL 与访问日期）；已核验的 2026 事实底座；ICASSP 2027 关口；待核实清单；gateway 访问方式说明。 |
| [`resources/external_tools.md`](resources/external_tools.md) | CMS 平台、IEEE Xplore、SPS 站点，以及五道作者侧核验流程与冲突规则。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 六篇经 dblp/IEEE-Xplore 核验的 ICASSP exemplar（Deep-RNN ASR、LAS、LibriSpeech、Deep Clustering、CNN 音频、x-vectors），含 self-check 与张冠李戴防护。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构的阵列处理（DOA）首页，从泛 ML 草稿改写成 ICASSP 的“机制 + metric”形态。 |
| [`resources/code/README.md`](resources/code/README.md) | 通向共享 ML 会议可复现套件的适配器，外加五项信号处理专属的测量检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是带自己 marketplace manifest 的自包含插件）：

```bash
# 从仓库克隆目录运行
claude plugin marketplace add ./ICASSP-Skills
claude plugin install icassp-skills
```

也可直接使用文件 —— 每个 `skills/icassp-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。常见调用：

- “这篇语音论文该投 ICASSP 还是 Interspeech？” → `icassp-topic-selection`
- “把我的阵列处理草稿压进 IEEE 四页” → `icassp-writing-style`
- “分离任务我报的 metric 对吗？” → `icassp-experiments`
- “录用了 —— IEEE Xplore camera-ready 要什么？” → `icassp-camera-ready`

## 包结构

```text
ICASSP-Skills/
├── .claude-plugin/                 # plugin.json + marketplace.json（12 个 skill）
├── README.md                       # 英文说明
├── README.zh-CN.md                 # 本文件
├── LICENSE                         # MIT
├── assets/cover.svg                # 封面（波形 + 频谱）
├── skills/
│   └── icassp-<topic>/SKILL.md     # 12 个 skill，各一目录
└── resources/
    ├── README.md                   # 资源指南 + 建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md              # 共享复现套件适配器
```

## 2026/2027 锚点事实（快照，非永久规则）

- **ICASSP 2026：Barcelona, Spain, 2026-05-04 至 05-08**（第 51 届），主题“Where Signals Meet
  Intelligence”；投稿截止 2025-09-17；rebuttal 据报道至约 2025-12-22。
- **ICASSP 2027：Toronto, Canada, 2027-05-16 至 05-21**；full-paper 截止据报道**约 2026-09-16 ——
  截至 2026-07-09 是下一个主要关口**（在 2027 CFP 可直接读取前标记为 待核实）。
- 版式：4 页正文 + 1 页可选的参考文献/致谢/伦理页。
- 评审：CMS 平台上的 single-blind；EDICS 路由；无送审 appendix。
- 出版：IEEE Xplore proceedings；另有 OJSP-ICASSP 与 SPS 期刊报告两条替代路径。

## 事实纪律

全包始终区分三类陈述：

1. **已核验的 2026 届事实** —— 可追溯到 source map 中带编号的来源（4+1 版式、single-blind、CMS 平台、
   9 篇上限）。
2. **据报道事实** —— 仅见于二手渲染并如此标注（rebuttal 窗口日期、ICASSP 2027 的 9 月截止）。
3. **待核实条目** —— 核验时未定，以问句表述、绝不作为事实（2027 精确日期、任何 AI 使用政策、未来是否
   回到 double-blind 或是否保留 rebuttal）。

若某 skill 把第 2/3 类当作第 1 类陈述，视为 bug，对照当前官方页面修正。

## 维护说明

- 上述每个日期都是**快照**。ICASSP 每年由新的本地委员会重建；从 Barcelona 2026 到 Toronto 2027 没有
  任何东西自动延续 —— 日期、rebuttal、平台细节都不例外。
- 本包在受 gateway 限制的访问下核验（渲染，而非直接抓取）；每届首要维护任务是直接重开主 URL 并刷新
  [`resources/official-source-map.md`](resources/official-source-map.md)。
- 新增 exemplar 必须按 [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的
  方法在 dblp `conf/icassp/` 上核验 —— 信号处理的名篇散落在 ICASSP、Interspeech、ICIP、EUSIPCO 与
  SPS 期刊之间，张冠李戴是这里最典型的错误。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
