# PNAS Nexus Skills（PNAS Nexus 技能包）

<p align="center">
  <img src="assets/cover.svg" alt="PNAS Nexus 封面卡" width="300">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-PNAS%20Nexus-0b3d68)](https://academic.oup.com/pnasnexus)
[![Access](https://img.shields.io/badge/open%20access-gold%20OA-ffd166)](https://academic.oup.com/pnasnexus/pages/what-makes-pnas-nexus-unique)
[![Scope](https://img.shields.io/badge/scope-multidisciplinary-1f6feb)](https://academic.oup.com/pnasnexus/pages/about)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **PNAS Nexus** 投稿的智能体技能包。PNAS Nexus 是 **PNAS 的完全开放获取（gold OA）综合性姊妹刊**，由
**牛津大学出版社（OUP）** 代表 **美国国家科学院（NAS）** 出版。

本包是"有主张的"，**并非把旗舰刊 PNAS 的包换个名字**。PNAS Nexus 是一本**不同的期刊**，规则也不同；本技能栈
正是编码了这些差异：**金色开放获取 + 文章处理费（APC）** 的商业模式与 **CC BY / CC BY-NC 许可证**选择；**没有
Direct/Contributed（NAS 院士代投）投稿通道**（所有稿件走统一的编辑指派同行评议）；从 **PNAS 转投 PNAS Nexus
的 transfer 通道**（评审意见随稿转移）；横跨**生物/健康/医学、物理科学与工程、社会与政治科学**的**宽口径**；
**以页数计的篇幅预算**与明确的**文章类型**（Research Report、Brief Report、Perspective、Review、Registered
Reports）；必备的 **50–120 词 Significance Statement**；**≤250 词单段、无小标题**的摘要；**正文内的
Materials and Methods**；**强制性**的数据/代码存放政策（含原始图像留存与撤稿条款）；以及**投稿阶段对参考文献
格式不作硬性要求**。

> ⚠️ **PNAS Nexus ≠ 旗舰刊 PNAS。** 若你要投的是 *Proceedings of the National Academy of Sciences*
> （带 Direct/Contributed 通道的混合式旗舰刊），请改用姊妹包 [PNAS-Skills](../PNAS-Skills/)。两刊的主编、
> 商业模式、投稿流程、篇幅规则与参考文献风格都不同——切勿混用其事实。

---

## 为什么要单独做 PNAS Nexus 包？

| 约束维度       | PNAS Nexus                                                   | 含义                                                        |
|----------------|--------------------------------------------------------------|-------------------------------------------------------------|
| 商业模式       | **完全金色开放获取**；收取 **APC**（通过 OUP 的按地区/类型个性化计算器定价） | 投稿前先**实时确认 APC**、查减免/Read&Publish，并选定许可证 |
| 投稿通道       | **无** —— 没有 Direct vs Contributed；统一编辑指派同行评议（≥2 名评审） | NAS 院士在此**无法"代投"**                                   |
| 从 PNAS 进入   | **Transfer/级联**：被 PNAS 拒稿的扎实工作可转投，**评审意见随之带过** | 当拒稿原因是契合度而非科学性时，值得接受                    |
| 收录口径       | 宽、且明确鼓励跨学科；编委会横跨 NAS + NAE + NAM             | 为**另一个分部**的读者而写                                   |
| Significance Statement | **50–120 词**（注意**下限**），面向广义读者          | 过短同样不合规，不只是过长才不合规                          |
| 摘要           | **≤250 词**，单段，**无小标题**                               | 至少量化一个结果                                            |
| 篇幅           | **以页数计**（Research Report 建议 6 页 / 上限 12 页 ≈ 4000 词、50 条文献、4 个图表），按类型不同 | 图注、表注、摘要、significance 都计入页数 |
| 方法位置       | **Materials and Methods 保留在正文**                          | 不能只放在 Supporting Information                           |
| 数据与代码     | **强制**在发表时存入公共仓库；留存原始图像；用 `[dataset]` 标注引用；不合规可被拒稿/撤稿 | 边做边搭建存放包                                            |
| 参考文献       | **投稿时任何可读风格均可**                                    | 投稿阶段不必硬套某家格式——干净、完整、可对应即可            |

通用"科研写作"包——以及旗舰刊 PNAS 包——都不会编码这些刊物特定约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install pnas-nexus-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/awesome-journal-skills.git
cd awesome-journal-skills/PNAS-Nexus-Skills

mkdir -p ~/.claude/skills && cp -R skills/pnasnexus-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/pnasnexus-* ~/.codex/skills/
```

### 第一条提示词

```
用 pnasnexus-workflow 告诉我，针对投往 PNAS Nexus 的稿件，下一步该用哪个技能。
```

---

## 默认工作流

```text
pnasnexus-fit            （过宽口径/跨学科门槛；判断是否接受 PNAS transfer）
        ▼
pnasnexus-openaccess     （APC、减免/Read&Publish、CC BY vs CC BY-NC —— 尽早做）
        ▼
pnasnexus-writing        （文章类型、页数预算、分类、正文内方法）
        ▼
pnasnexus-figures        （在图表元素预算内确定展示项）
        ▼
pnasnexus-statistics     （严谨性 + 可复现；Registered Reports）
        ▼
pnasnexus-data           （强制数据/代码存放 + 原始图像留存）
        ▼
pnasnexus-significance   （50–120 词 Significance Statement —— 高价值）
        ▼
pnasnexus-abstract       （≤250 词单段摘要 —— 打磨）
        ▼
pnasnexus-citation       （参考文献 —— 投稿时格式自由；务求干净）
        ▼
pnasnexus-submission     （投稿前自检 + cover letter）
        ▼
pnasnexus-rebuttal       （评审之后）
```

`pnasnexus-workflow` 是路由器——根据你当前所处阶段告诉你接下来用哪个技能。

---

## 技能一览

| 技能                    | 用途                                                                             |
|-------------------------|----------------------------------------------------------------------------------|
| `pnasnexus-workflow`    | 路由器——决定下一步调用哪个子技能                                                  |
| `pnasnexus-fit`         | 宽口径/跨学科门槛；PNAS Nexus vs 旗舰 PNAS vs 领域刊；**PNAS transfer** 判断       |
| `pnasnexus-openaccess`  | **金色 OA + APC + CC BY/CC BY-NC 许可证**（取代旗舰刊的投稿通道选择）              |
| `pnasnexus-significance` | 必备的 **50–120 词 Significance Statement**，面向广义读者                         |
| `pnasnexus-abstract`    | **≤250 词**单段、无小标题摘要；与 significance 区分                               |
| `pnasnexus-writing`     | **文章类型** + **以页数计的预算**、分类、**正文内方法**                            |
| `pnasnexus-figures`     | 图表元素预算、尺寸、展示原始数据、色盲友好、原始图像留存                          |
| `pnasnexus-statistics`  | 效应量 + 置信区间 + n + 检验；重复；可复现；**Registered Reports**                |
| `pnasnexus-data`        | **强制**数据/代码存放、原始图像、登录号/DOI、`[dataset]` 标注                      |
| `pnasnexus-citation`    | 参考文献——**投稿时格式自由**；一致、完整、可对应                                   |
| `pnasnexus-submission`  | 完整投稿前自检清单 + cover letter 模板（含 transfer 与 OA）                        |
| `pnasnexus-rebuttal`    | 决定信分诊、实验排序、逐条回复（含从 PNAS 带过来的评审意见）                       |

### 资源

- [`resources/official-source-map.md`](resources/official-source-map.md) —— 权威事实底稿（主编、APC、许可证、篇幅、政策），带访问日期与"待核实"标记
- [`resources/external_tools.md`](resources/external_tools.md) —— OA/APC 页面、存放仓库、报告规范、图/统计工具、PNAS Nexus 官方页面
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— **真实、经网络核实的 PNAS Nexus 论文**（`10.1093/pnasnexus/…` DOI），覆盖三个分部，含姊妹刊混淆护栏
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— Significance Statement + 摘要的 before→after（虚构教学示例）
- [`skills/pnasnexus-submission/templates/checklist.md`](skills/pnasnexus-submission/templates/checklist.md) —— 完整投稿前自检清单
- [`skills/pnasnexus-submission/templates/cover_letter_template.md`](skills/pnasnexus-submission/templates/cover_letter_template.md) —— cover letter 脚手架

---

## 与旗舰刊 PNAS 的差异

| 维度           | PNAS Nexus                                   | 旗舰刊 PNAS（[PNAS-Skills](../PNAS-Skills/)） |
|----------------|----------------------------------------------|-----------------------------------------------|
| 出版方         | **牛津大学出版社**（代表 NAS）                | NAS / PNAS                                     |
| 获取模式       | **完全金色 OA + APC**                         | 混合（订阅 + 可选 OA）                         |
| 投稿通道       | **无**（统一编辑指派）                        | **Direct vs Contributed**（NAS 院士）          |
| 进入路径       | **从 PNAS transfer**（评审意见随转）          | 无                                             |
| Significance Statement | **50–120 词**（含下限）              | ≤120 词                                        |
| 篇幅           | **以页数计**、按类型（6 页 / 上限 12 页）     | 页数/字符预算                                  |
| 参考文献       | **投稿时任何可读风格**                        | 投稿即须编号、按出现顺序                       |

旗舰刊 PNAS 请见姊妹包 [PNAS-Skills](../PNAS-Skills/)。

---

## 免责声明

本包为独立、社区构建的技能包，**未**获牛津大学出版社、美国国家科学院、*PNAS* 或 *PNAS Nexus* 的关联、背书或
出品。其中所有指标（词数/页数、数量上限、费用、许可证选项、政策规则）反映写作时（**访问日期 2026-06-23**）公开
的作者指南，并在 [`resources/official-source-map.md`](resources/official-source-map.md) 中附来源记录——投稿前
**务必对照当前的 [PNAS Nexus 作者指南](https://academic.oup.com/pnasnexus/pages/general-instructions)** 核实。
**APC 金额按地区/类型个性化**，**必须在 OUP 计算器中实时确认**；OUP 不公布固定刊例（公开第三方数据库口径不一，
约 **US$2,200–4,200**），实际计费金额按地区/类型而异，且可能被减免或豁免。主编会轮换，投稿时请再核实在任主编。

---

## 许可证

MIT
