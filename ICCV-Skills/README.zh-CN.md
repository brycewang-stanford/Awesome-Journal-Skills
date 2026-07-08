# ICCV Skills（中文说明）

面向 **ICCV（IEEE/CVF International Conference on Computer Vision）** 的 12 个 agent
skills。ICCV 是计算机视觉领域的国际旗舰会议，**每两年一届、只在奇数年举办**——本包
正是围绕这个节奏组织的：投 ICCV 的决定是一个两年期承诺，因此选会、三月初的单一截稿、
五月的 rebuttal 周、作者审稿义务，以及错过之后转投 CVPR / ECCV 的退路，被当作一场
完整战役来处理，而不是一串表格。

官方依据核验日期：**2026-07-08**。核验对象包括 ICCV 2025 Call for Papers、Dates、
Author Guidelines、Reviewer Guidelines、2025 年 **Changes** 页面（该届流程改革的官方
公告）、Submission Checklist、ICCV 2025 OpenReview group、CVF open access、CVF
upcoming-conferences 列表与 PAMI-TC 奖项页面。核验环境无法直接抓取
`iccv.thecvf.com` 与 `tc.computer.org`（HTTP 403），故官方页面内容通过对精确 URL 的
搜索引擎渲染读取，并与 OpenReview、dblp、CVF、官方会议账号公告交叉核对。完整来源
链、访问日期、"仅为报道"级事实与全部 **待核实** 条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

**周期状态：** ICCV 2025（檀香山，2025 年 10 月 19–23 日）是最近一届已完成的会议，
提供本包全部已核验锚点。ICCV 2027 已宣布在**香港，2027 年 10 月 2–8 日**举办，但
截至核验时未发布任何 CFP、截稿或政策页面——2027 届的一切流程细节均为待核实。

## 本包围绕的核心事实（2025 届已核验）

- **两年一届（奇数年）。** 错过截稿，下一届 ICCV 在两年之后；理性的退路阶梯经过
  CVPR（每年 11 月截稿）与 ECCV（偶数年春季截稿）。多个 skills 显式处理这个三角。
- **一次性上传。** 自 2025 年起，正文与补充材料**同日**提交（2025 年 3 月 7 日，
  11:59pm **HST**，注意时区），此前 3 月 3 日完成注册。传统的"补充材料缓冲周"已不存在。
- **每位作者都要审稿。** 不是"符合条件的作者"，而是全部作者（视觉社区新人或圈外者
  可豁免）；每位作者最多注册 25 篇投稿。
- **有实际执行记录的惩罚。** 2025 年程序主席因 25 名审稿人严重不负责（一句话审稿、
  LLM 生成审稿、答非所问）而 desk-reject 了他们署名的 29 篇论文，其中 12 篇原本会被
  接收。
- **规模。** 11,239 篇有效投稿，2,699 篇接收，接收率 24%；Highlight 与 oral 为更高
  层级（具体数字属报道级，未经官方页面复核）。
- **五月的一页纸。** 5 月 9 日放出评审，5 月 10–16 日提交一页 PDF rebuttal（官方模板、
  禁链接、禁附件）；六月下旬出结果，十月开会——这四个月的跑道，本包建议花在 artifact
  发布与跨国参会筹备上。
- **出版。** CVF open access（免费）+ IEEE Xplore（record 版本）；无作者端费用；
  主席团逐届轮换。ICCV 最佳论文奖为 **Marr Prize**，其获奖谱系（Mask R-CNN 2017、
  Swin 2021、ControlNet 2023、BrickGPT 2025）在选题 skill 中被用作品味信号。
- **2025 年新事物：Findings workshop**——接收从 ICCV 2025 主会被拒或撤回、但技术上
  扎实的论文，是拒稿后的一个新出口，已纳入拒稿应对策略。

## Skills 一览

- [`iccv-topic-selection`](skills/iccv-topic-selection/SKILL.md)：判断项目是否值得
  支付两年期的机会成本；以日历优先的方式在 CVPR/ECCV/WACV/期刊之间路由；用 Marr
  Prize 谱系校准"ICCV 式贡献"。
- [`iccv-workflow`](skills/iccv-workflow/SKILL.md)：奇数年战役管理：前一年秋天的
  CVPR-vs-ICCV 分叉、三月截稿、五月 rebuttal、六月决定、含签证筹备的十月参会计划、
  错过后的阶梯。
- [`iccv-writing-style`](skills/iccv-writing-style/SKILL.md)：为国际化的通才审稿人
  写作：机制先行、8 页（含图表）的版面市场、按"一页纸可辩护"来定claims 尺度。
- [`iccv-related-work`](skills/iccv-related-work/SKILL.md)：跨越两届之间的 CVPR/ECCV
  周期做定位；三月截稿附近的 concurrent 礼仪；自引与"不得引用自己公开代码库"规则；
  三大会归属核对。
- [`iccv-experiments`](skills/iccv-experiments/SKILL.md)：固定日期下的证据设计：
  benchmark 漂移审计、基础模型时代的公平性台账、机制隔离式 ablation、"证伪实验先跑"
  的排程。
- [`iccv-reproducibility`](skills/iccv-reproducibility/SKILL.md)：在没有强制表格的
  前提下通过"两年可核查"测试：配方台账、基础模型协议固定、方差诚实、主动的算力披露。
- [`iccv-supplementary`](skills/iccv-supplementary/SKILL.md)：同日截稿下把补充材料
  当并行工作流生产：内容分工、压缩包特有的匿名泄漏、七分钟可导航结构。
- [`iccv-artifact-evaluation`](skills/iccv-artifact-evaluation/SKILL.md)：按封存
  规则打包审稿期代码；把六月到十月的跑道花在达到本会"基础设施级"标准的发布上。
- [`iccv-submission`](skills/iccv-submission/SKILL.md)：投稿终审：注册与 profile、
  三个上限（页数、每人投稿数、rebuttal 长度）、匿名与 embargo 扫描、最后 48 小时分诊。
- [`iccv-review-process`](skills/iccv-review-process/SKILL.md)：建模评审管线及其
  "牙齿"：全员审稿、2025 年执行结果、审稿人 LLM 禁令、决定层级、拒稿后的 Findings
  选项。
- [`iccv-author-response`](skills/iccv-author-response/SKILL.md)：把 5 月 10–16 日
  变成生产排程，把一页纸变成论证预算：什么放得下、什么该让步、什么走保密渠道。
- [`iccv-camera-ready`](skills/iccv-camera-ready/SKILL.md)：交付 CVF + IEEE Xplore
  双渠道的最终版本：去匿名作为改写工序、rebuttal 承诺逐条对账、arXiv 同步、十月
  跨国参会。

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md)：14 个来源
  的核验链，含访问方式披露与待核实清单。
- [`resources/external_tools.md`](resources/external_tools.md)：官方入口与作者端
  五道核验工序。
- [`resources/exemplars/library.md`](resources/exemplars/library.md)：7 篇经场馆
  核验的 ICCV 论文，按年代排成时间序列（SIFT → Mask R-CNN → CycleGAN → Swin →
  ControlNet → SAM → BrickGPT），附三大会误归属防呆清单。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)：
  虚构三维重建论文首页的 before → after 改写与迁移清单。
- [`resources/code/README.md`](resources/code/README.md)：共享 ML 会议可复现性
  工具包的适配器，外加 5 项 ICCV 专属检查。

## 安装与使用

```bash
# 在仓库克隆目录内
claude plugin marketplace add ./ICCV-Skills
claude plugin install iccv-skills
```

也可以直接把每个 `skills/iccv-*/SKILL.md` 当独立指令文件使用。典型触发：

- "这个工作压到 ICCV 2027 还是 11 月投 CVPR？" → `iccv-topic-selection` + `iccv-workflow`
- "三月截稿前做一次投稿审计" → `iccv-submission`
- "评审出了，一周内交 rebuttal" → `iccv-author-response`
- "中了，六月到十月该干什么？" → `iccv-camera-ready` + `iccv-artifact-evaluation`

## 目录结构

```text
ICCV-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json（声明 12 个 skills）
├── README.md                  # 英文说明
├── README.zh-CN.md            # 本文件
├── LICENSE                    # MIT
├── assets/cover.svg           # 封面（双年轨道图案）
├── skills/
│   └── iccv-<topic>/SKILL.md  # 12 个 skills，每个一个目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 事实纪律

本包的陈述分三级并全程可区分：（1）**已核验的 2025 届事实**，可追溯到来源表编号
（统一截稿与 HST 时区、8 页含图表上限、全员审稿规则、29 篇 desk-reject 的执行结果、
24% 接收率）；（2）**报道级事实**，二手来源一致但未经官方页面复核（263 篇
Highlight、约 0.56% 的 oral 比例、六月下旬决定的精确日期、CVF 页面列出的 2027 主席
名单）；（3）**待核实条目**，以开放问题表述（2025 camera-ready 细节、补充材料体积
上限、参会义务，以及 2027 届的全部流程）。若发现某个 skill 把 2/3 级材料当 1 级
陈述，视为 bug，请对照官方页面修正。

## 维护说明

- 下一个真正的更新时点是 **iccv.thecvf.com/Conferences/2027** 上线之时：截稿链与
  时区、页数上限、补充材料机制、审稿义务措辞、rebuttal 形式、Findings 是否延续，都
  需要重新核验。
- 2025 届的流程改革发布在专门的 Changes 页面；找 2027 届的对应页面是信息密度最高的
  第一步。
- 层级统计与执法数字是"周期事件"而非常量，引用时只用新周期自己的数字。
- 新增 exemplar 必须走 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  底部的场馆核验流程——CVPR/ICCV/ECCV 是视觉文献里最容易被张冠李戴的三个会。

## 许可

MIT，见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md).
