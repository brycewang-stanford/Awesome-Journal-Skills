# 《通信学报》技能包（中文详版）· Journal on Communications (JOC) Skills

本文件是 [`README.md`](README.md) 的中文详版，面向准备向**《通信学报》(Journal on Communications,
JOC)** 投稿的作者与 agent，展开每个技能的定位、本刊事实基线与使用编排。《通信学报》由中国科学
技术协会主管、**中国通信学会(China Institute of Communications)** 主办，是通信学科的中文旗舰
**月刊**（每月 25 日出版），刊号 **CN 11-2102/TN**、**ISSN 1000-436X**。全篇中，《通信学报》与
Journal on Communications (JOC) 两个名称会反复并现，以保证工具在中英双语环境下都能命中本刊。

## 一、本刊事实基线（2026-07-09 核验）

| 项目 | 口径 | 来源/状态 |
|---|---|---|
| 主管 / 主办 | 中国科学技术协会 / 中国通信学会 | 官网、CNKI 双源一致 |
| 刊期 | 月刊，每月 25 日出版 | 官网、CNKI |
| 刊号 | CN 11-2102/TN；ISSN 1000-436X | CNKI/万方，多源一致 |
| 官网 / 投稿 | infocomm-journal.com/txxb；cbpt.infocomm-journal.com | 官网、投稿系统 |
| 邮箱 / 电话 | txxb@bjxintong.com.cn；010-53878169 等 | 官网投稿须知 |
| 学科方向 | 通信理论与技术、无线/移动通信、网络与交换、信息安全与密码、信号处理 | 官网栏目、CCF 目录 |
| 栏目 | 学术论文、技术报告、综述、短文 | 官网 |
| 篇幅 | 约 12000 字符（约 12 页）；综述可延至约 15 页 | 官网格式要求 |
| 查重红线 | 知网查重，与已发表论文重复率 > 20% 不予收录 | 官网投稿须知 |
| 费用 | 不收稿件处理费；审稿费 300 元/篇（初审通过后）；版面费 600 元/面（录用后按篇幅） | 官网投稿须知（以当期通知为准） |
| 审稿流程 | 初审→外审→终审（终审由编委会负责），约 1~3 个月 | 官网审稿流程；精确时长 **待核实** |
| 创刊年 / 影响因子 / 主编 | 1980 年 / 约 1.84 / 未确认 | 均 **待核实**（二手） |
| 收录 | EI、SA/INSPEC、CSA、JST、CSCD、北大核心 | 二手多源；当期状态 **待核实** |

> 凡 **待核实** 项，请在投稿前重新核对官网《投稿须知》《征稿启事》与 CBPT 投稿系统内当期通知。
> 详见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 二、12 个技能的定位

### 立项与规划
- **`jonc-topic-selection`（选题与栏目定位）**：判断稿件是否落在《通信学报》/Journal on
  Communications (JOC) 的通信学科版图内，避免投成宽电子学科（《电子学报》）或计算机综合刊
  （《计算机学报》）；据贡献选定学术论文/技术报告/综述/短文。
- **`jonc-workflow`（全流程）**：给出从选题、写作、投稿到修回、录用、见刊的时间线与技能调度。

### 写作
- **`jonc-writing-style`（中文写作规范）**：中英文结构式摘要、中英文关键词、中图分类号 TN、文献
  标识码、文章编号、量与单位、参考文献 GB/T 7714 与中文文献著录。
- **`jonc-related-work`（相关工作）**：以 delta 为主线组织通信领域文献综述，确立创新点。
- **`jonc-experiments`（实验设计）**：链路级/系统级仿真、信道模型、SNR-BER/吞吐/时延曲线、蒙特卡洛
  置信区间、公平基线与消融。

### 证据与材料
- **`jonc-reproducibility`（可复现性）**：固定仿真参数、信道实现、随机种子、数据集划分，提供复现包。
- **`jonc-supplementary`（补充材料）**：按"是否决定结论"划分正文与附录/多媒体附件。
- **`jonc-artifact-evaluation`（代码与数据可用性）**：讲清本刊无独立"制品徽章"制度的现状与稳妥做法。

### 投稿与评审
- **`jonc-submission`（投稿就绪审计）**：模板、行文次序、六件套、查重、栏目归属、退稿风险分诊。
- **`jonc-review-process`（审稿流程）**：三审制建模，逐环节列出作者可用的杠杆。
- **`jonc-author-response`（答复与修回）**：逐条回应外审与编委会意见、撰写修回说明与差异标注。
- **`jonc-camera-ready`（录用定稿）**：校样、缴费、版权、出版排期。

## 三、推荐使用顺序

选题(`topic-selection`) → 规划(`workflow`) → 写作(`writing-style` + `related-work` +
`experiments` + `reproducibility` + `supplementary`) → 投稿审计(`submission`) →
评审应对(`review-process` + `author-response`) → 录用收尾(`camera-ready`)；
`artifact-evaluation` 贯穿证据准备阶段按需调用。

## 四、免责声明

本包为独立编写的第三方写作辅助资料，非《通信学报》/Journal on Communications (JOC) 官方出品。所有
费用、周期、格式与收录信息以编辑部官网与 CBPT 投稿系统内当期公告为准；**待核实** 项请勿当作定论。
MIT License · © 2026 Bryce Wang。
