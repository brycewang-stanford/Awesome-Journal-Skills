# ACM CCS Skills

面向 **ACM CCS（ACM Conference on Computer and Communications Security）** 论文的 12 个 agent
skills。CCS 是 SIGSAC 的旗舰会议，与 IEEE S&P、USENIX Security、NDSS 并称计算机安全"四大顶
会"。本包覆盖一个 CCS 周期的完整流程：判断安全贡献是否适合 CCS、构建能抵御审稿人攻击的证据、
准备匿名的 HotCRP 投稿、通过 ethics 与 responsible disclosure 门槛、熬过双周期评审与 rebuttal，
以及完成 ACM camera-ready 与可选的 artifact evaluation。

官方依据核验日期：**2026-07-08**。已核验 CCS 2026 Call for Papers、call for artifacts、
Cycle A 与 Cycle B 的 HotCRP 站点、CCS 2026 主页与组织页面、SIGSAC CCS Test-of-Time Award 页面，
以及 ACM Digital Library 的 CCS proceedings。核验环境下直接抓取 `www.sigsac.org` 返回 HTTP 403，
因此官方页面通过对精确 URL 的搜索引擎渲染阅读，并与 HotCRP 周期站点、ACM DL 和 dblp 交叉核对；
完整追溯（含所有 待核实 项）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## CCS 与同类会议的区别

以下 2026 周期机制驱动了大部分 skill 建议，也是来自其他安全会议或 ML/理论会议的作者最常踩的坑：

- **两个评审周期，一个会议。** CCS 每年在 HotCRP 上运行 Cycle A 与 Cycle B。一篇论文只进入一个
  周期；**第一周期被拒的论文当年不得再投**。选周期是策略决定，不是形式。
- **摘要注册强制且先行。** 标题、作者、摘要、topics 须在全文截止前约一周注册；没注册摘要就不能投。
- **硬性 12 页 ACM `sigconf` 正文。** 未改动的双栏 ACM 模板下 12 页，不含参考文献与标注清楚的
  appendix。压缩空白或改边距会触发 desk-reject。
- **匿名投稿，自引用第三人称。** 未正确匿名的论文可能不经评审直接拒。
- **ethics considerations 章节为必需**（涉及人类被试、用户数据或真实漏洞的工作）——2026 年为正文与
  参考文献之后的独立 appendix。IRB/ERB 批准既非必要也非充分。
- **决定不是二元的。** Accept、minor revision（本周期内修改）、reject。
- **录用后可选 artifact evaluation**，授予 ACM badge——Available、Functional、Reusable、Results
  Reproduced，印在论文首页。
- **审稿人具攻击性。** SIGSAC PC 会攻击你的 threat model，寻找让攻击变简单的假设，并要求 defense
  面对 adaptive attacker。

## Skills

- `ccs-topic-selection`：按 threat model 与贡献类型在 CCS、IEEE S&P、USENIX Security、NDSS、
  PETS、密码学会议之间选会——而非按声望。
- `ccs-workflow`：管理双周期年度日程——摘要注册、全文、rebuttal、通知、artifact evaluation、
  camera-ready，以及四大顶会的 deadline-hopping 日历。
- `ccs-writing-style`：把 threat model 放上首页，校准攻防主张，压缩进 12 页双栏 `sigconf`。
- `ccs-related-work`：覆盖四大顶会与专门会议文献，以及 CVE/advisory 记录，并保持自引匿名。
- `ccs-experiments`：构建攻击演示、adaptive-attack defense 评测，以及经验证的 measurement。
- `ccs-reproducibility`：将主张映射到证据，锁定版本与预算，诚实说明无法公开的 artifact。
- `ccs-supplementary`：按评审状态而非方便在 12 页正文与 appendix（含 ethics 章节）之间切分。
- `ccs-artifact-evaluation`：为 ACM badge ladder 打包攻击、防御与 measurement，每个核心结果一条命令。
- `ccs-submission`：HotCRP 终审——摘要注册、页数与模板、匿名清扫、ethics 章节、篇数上限、一稿多投。
- `ccs-review-process`：建模双周期流程、决定类别、ethics reviewer，以及作者杠杆所在。
- `ccs-author-response`：把异议映射到 threat model、证据、ethics，用匿名且有证据锚点的 rebuttal 回应。
- `ccs-camera-ready`：把录用转成正确的 ACM DL 条目——去匿名、rights form、badge 放置、disclosure
  时机与现场报告。

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md)：九个官方来源、URL 与访问
  日期、访问方法说明、已核验的 2026 事实、明确的 待核实 清单。
- [`resources/external_tools.md`](resources/external_tools.md)：官方入口与投稿前的作者自查项。
- [`resources/exemplars/library.md`](resources/exemplars/library.md)：六篇经元数据核验的 CCS 论文
  （四篇 Test-of-Time），跨六种贡献类型，附自查问题与防误标指南。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)：
  一个虚构 side-channel 摘要与引言按 CCS 首页结构重写，before → after。
- [`resources/code/README.md`](resources/code/README.md)：共享可复现工具包的适配器，加上通用工具无法
  完成的 CCS 专属检查。

## 安装与使用

作为 Claude Code 插件（本目录是带 marketplace manifest 的自包含插件）：

```bash
# 在仓库克隆中
claude plugin marketplace add ./ACM-CCS-Skills
claude plugin install acm-ccs-skills
```

或直接使用文件：每个 `skills/ccs-*/SKILL.md` 都是独立指令文件，frontmatter 的 `description`
告诉 agent 何时触发。典型调用：

- "这个 side-channel 结果该投 CCS 还是 S&P？" → `ccs-topic-selection`
- "按 CCS 投稿规则审查我的稿子" → `ccs-submission`
- "评审意见来了——帮我规划 rebuttal" → `ccs-author-response`
- "把我的 exploit 打包做 artifact evaluation" → `ccs-artifact-evaluation`

## 目录结构

```text
ACM-CCS-Skills/
├── .claude-plugin/          # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                # 英文说明
├── README.zh-CN.md          # 本文件
├── LICENSE                  # MIT
├── assets/cover.svg         # 封面
├── skills/
│   └── ccs-<topic>/SKILL.md # 12 个 skill，每个一个目录
└── resources/
    ├── README.md            # 资源导览 + 建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md       # 共享可复现工具包适配器
```

## 建议流程

1. **动笔前**——先跑 `ccs-topic-selection`；若 threat model 不适合 CCS，本包已为你省下一个周期。
   浏览 exemplars library，看看经久不衰的 CCS threat model 长什么样。
2. **构建时**——把 `ccs-experiments` 与 `ccs-reproducibility` 放在代码旁；adaptive-attack 三件套与
   版本锁定越早装越省事，deadline 周再补代价更高。
3. **写作时**——正文用 `ccs-writing-style`，正文/appendix/ethics 切分用 `ccs-supplementary`，对四大
   顶会与 CVE 记录的定位用 `ccs-related-work`；对照 worked example 的 before/after。
4. **Deadline 周**——尽早注册摘要，然后完整跑 `ccs-submission`，含匿名、模板检查与 ethics 章节。
5. **投稿后**——用 `ccs-review-process` 把握时间预期，评审意见到达时用 `ccs-author-response`，录用后
   用 `ccs-camera-ready` 与可选的 `ccs-artifact-evaluation`，被拒则做四大顶会 re-routing。

## 事实纪律

本包区分三类陈述，且 skill 保持它们可辨：

1. **已核验的 2026 周期事实**——带日期/上限，且追溯到 source map 中带编号的来源（如 12 页正文、双周期结构、
   ACM badge 集合）。
2. **转述事实**——仅见于二手来源并如此标注（如 CCS 2026 Program Co-Chairs，来自组织页面渲染）。
3. **核验时无法确认的项**——明确标 待核实 并以待解决问题呈现，绝不当作事实（如 AI/LLM 政策、camera-ready
   页数、CCS 2027 主办城市）。

若发现 skill 中把第 2、3 类材料当作第 1 类陈述，视为 bug，对照官方页面修正。

## 2026 锚点事实（历史快照，非永久规则）

- CCS 2026：**荷兰海牙，2026 年 11 月 15-19 日**。
- Cycle A：摘要注册 **1 月 7 日**，全文 **1 月 14 日**，rebuttal **3 月 17-20 日**，通知
  **2026 年 4 月 9 日**。
- Cycle B：摘要注册 **4 月 22 日**，全文 **4 月 29 日**，rebuttal **6 月 29 日-7 月 1 日**，通知
  **2026 年 7 月 17 日**。camera-ready 据报 **2026 年 8 月 21 日**。所有截止均为 AoE。
- 格式：未改动的 ACM `sigconf` 双栏模板 · 正文 **12 页**，不含参考文献、标注清楚的 appendix 与补充材料。
- 匿名投稿 · 强制摘要注册 · ethics considerations appendix · 每作者每周期最多 **7 篇** ·
  第一周期被拒当年不得再投。
- 可选 artifact evaluation 与 ACM badge；录用论文发表于 ACM Digital Library。
- 截至 2026-07-08，**两个 2026 截止日期均已过**；把日历当模板，待 CCS 2027 CFP 发布后再读
  （主办城市当时仍在 steering committee 选定中）。

## 维护说明

- 上述每个日期与上限都是 **2026 周期快照**；涉及 deadline 的建议前，请重新打开当年
  `sigsac.org/ccs/CCS<year>` CFP 与该周期的 HotCRP 站点。
- 2026-07-08 无法实时核验的项在 source map 中标为 待核实——尤其是 AI/LLM 政策、rebuttal 格式、
  minor-revision 机制、camera-ready 页数、2026 General Chairs、CCS 2027 主办城市。确认前不得当作事实。
- CCS 的 chairs 与政策每届重设，且 Cycle A 与 Cycle B 可能不同；把期刊包沿用的"编辑连续性"假设视为错误。
- 新增 exemplar 论文时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程——著名的安全成果未必就是 CCS 论文。

## License

MIT，见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
