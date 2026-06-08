# 引言改写示例 —— 《世界经济》房风格（before → after）

> **示意性、纯属虚构。** 下文的论文、机构、企业、数字、暴露度构造均为演示《世界经济》（The Journal
> of World Economy）引言房风格而**虚构**，不指向任何真实研究或真实结果。房风格仅来自本包
> `skills/` 各 SKILL（先读 [`jwe-fit-positioning`](../../skills/jwe-fit-positioning/SKILL.md)、
> [`jwe-topic-international`](../../skills/jwe-topic-international/SKILL.md)、
> [`jwe-transmission-channel`](../../skills/jwe-transmission-channel/SKILL.md)、
> [`jwe-identification`](../../skills/jwe-identification/SKILL.md)、
> [`jwe-heterogeneity`](../../skills/jwe-heterogeneity/SKILL.md)、
> [`jwe-data-sources`](../../skills/jwe-data-sources/SKILL.md)）。格式 / 体例细节以本包
> [`official-source-map.md`](../official-source-map.md) 为准。

《世界经济》要的是**开放经济中的因果**，不是做得很好的国内实证。一篇合格的引言必须在**前两段**
就把"为什么这是开放 / 国际问题"立住（[`jwe-fit-positioning`](../../skills/jwe-fit-positioning/SKILL.md)）：
现象先行、外生冲击锚在国际 / 制度性变动上、机制经一条可检验的**跨境渠道**传导、贡献写成"修正 /
扩展了国际经济学的某个判断"。下面用一个虚构的"美方加征关税 → 中国出口企业"的例子演示。

---

## ❌ Before（国内腔、效应捞针、识别靠"我们认为"）

> 近年来中美经贸摩擦加剧，对中国企业产生了重要影响。本文研究贸易摩擦对企业出口的影响。我们使用
> 2015—2020 年中国上市公司面板数据，将企业出口额对一个"贸易摩擦"虚拟变量回归，控制企业规模、
> 资产负债率、行业与年份固定效应，发现贸易摩擦显著抑制了企业出口（β = −0.12，p < 0.05）。本文
> 对理解外部环境变化、推动企业高质量发展具有重要的政策启示。

逐条诊断：

- **开放维度只是背景，不是问题本身**（[`jwe-fit-positioning`](../../skills/jwe-fit-positioning/SKILL.md)）。
  把"贸易摩擦"当成一个笼统虚拟变量，去掉"外部 / 开放"这层，文章仍是一篇"某冲击抑制了出口"的
  国内实证——本刊一句话标准是"去掉开放维度还成立吗"，这里成立，于是**不对口**。
- **没有可识别的因果问句**（[`jwe-topic-international`](../../skills/jwe-topic-international/SKILL.md)）。
  谁是处理 / 暴露组？暴露度该由**国际结构**（对美出口依赖、被加税 HS 产品占比）度量，而不是一个
  全样本通用的时间虚拟变量；反事实是什么也没交代。
- **识别策略不成立**（[`jwe-identification`](../../skills/jwe-identification/SKILL.md)）。
  "贸易摩擦"虚拟变量本质是 OLS + 时间冲击，外生性全靠"我们认为"；既没把关税锚在"由贸易伙伴
  决定、对个体外生"上，也没有平行趋势 / 事件研究 / 安慰剂。
- **机制缺位**（[`jwe-transmission-channel`](../../skills/jwe-transmission-channel/SKILL.md)）。
  外部冲击经由哪条**跨境渠道**（贸易 / 投资 / 金融 / 预期）传到出口？只字未提，"抑制了出口"
  是结论不是机制。
- **数据国际属性不足**（[`jwe-data-sources`](../../skills/jwe-data-sources/SKILL.md)）。
  上市公司面板看不到产品 - 目的国维度，分不了扩展 vs 集约边际、做不出对美暴露度——本刊审稿人对
  数据的"国际属性"尤为敏感。
- **贡献是套话**。"对……具有重要政策启示"既不指向谁、决定什么，也没说修正了国际经济学的哪个判断。

---

## ✅ After（现象先行、机制清晰、识别可辩护、开放维度立在前两段）

> 2018 年美方对约半数自华进口商品分批加征关税，但冲击在中国出口企业间高度不均：有的企业当季就把
> 订单转向第三国市场，有的则在一年内持续丢失对美份额。**差异的关键不在企业是否"涉外"，而在其
> 出口篮子有多大比例落在被加税的 HS 产品 - 美国市场组合上**——即企业层面的**关税暴露度**。然而既
> 有研究多把贸易摩擦当作一个全样本的时间冲击，掩盖了暴露度的横截面差异，也就回答不了"关税究竟
> 经由哪条渠道、传到哪个贸易边际"这一开放经济的核心问题。
>
> 我们把美方加税视为一次**对中国企业外生**的制度性冲击：税目与时点由美方单边决定，单个中国企业
> 无从影响（[`jwe-identification`](../../skills/jwe-identification/SKILL.md)）。借助企业 - HS 产品 -
> 目的国层面的海关微观数据（[`jwe-data-sources`](../../skills/jwe-data-sources/SKILL.md)），我们用
> **初期产品 - 市场份额 × 美方加税幅度**构造企业级暴露度（shift-share 思路），以加税前的暴露度差异
> 识别因果，并按现代 shift-share 推断报告份额外生性、Rotemberg 权重来源与 exposure-robust 标准误。
>
> 我们进一步指认**贸易渠道**为主传导：冲击先压低对美集约边际（量、价），随后通过**贸易转向**抬高
> 对非美市场的扩展边际（新进入的产品 - 目的国对）（[`jwe-transmission-channel`](../../skills/jwe-transmission-channel/SKILL.md)）。
> 异质性沿**国际经济学意义的维度**切分：一般贸易 vs 加工贸易、对美出口依赖高 vs 低、可替代目的国
> 多 vs 少——预期高暴露、低可替代、加工贸易企业受创更深、转向更难
> （[`jwe-heterogeneity`](../../skills/jwe-heterogeneity/SKILL.md)）。
>
> 读完本引言，读者已掌握：现象（关税冲击在企业间高度不均）、识别（外生加税 × 初期暴露度 + 现代
> shift-share 推断）、机制（贸易渠道下的市场转向，落在具体贸易边际上）、以及开放维度为何在前两段
> 即已立住而非结尾硬贴（[`jwe-fit-positioning`](../../skills/jwe-fit-positioning/SKILL.md)）。
>
> 本文的贡献是把"贸易摩擦抑制出口"这一笼统判断，**修正**为"关税沿暴露度异质地重塑企业的贸易边际
> 与目的国结构"：对国际贸易文献，它给出市场转向的微观证据与边界条件；对政策，它把着力点从"是否
> 受摩擦影响"转向"哪些暴露结构最脆弱、转向空间在哪"。

为什么这样写有效：

- **现象先行、开放维度立在前两段**——以"冲击在企业间不均"开场，暴露度由**国际结构**（对美 HS 产品
  份额）度量，去掉开放维度文章即不成立（[`jwe-fit-positioning`](../../skills/jwe-fit-positioning/SKILL.md)、
  [`jwe-topic-international`](../../skills/jwe-topic-international/SKILL.md)）。
- **识别可辩护**——外生冲击锚在美方单边加税上，配 shift-share 暴露度并正面回应 GPSS / BHJ / AKM
  现代推断批评，预先堵住审稿人最高频的攻击点（[`jwe-identification`](../../skills/jwe-identification/SKILL.md)）。
- **机制是跨境渠道、落在贸易边际上**——指认贸易渠道，给出"集约下压 → 扩展转向"的可检验链条，而非
  "抑制了出口"的叙事（[`jwe-transmission-channel`](../../skills/jwe-transmission-channel/SKILL.md)）。
- **异质性切在国际经济学维度**——加工 vs 一般贸易、对美依赖、可替代目的国，每一维都有事前理论预期，
  且方向与主渠道自洽（[`jwe-heterogeneity`](../../skills/jwe-heterogeneity/SKILL.md)）。
- **贡献写成对国际经济学判断的"修正 / 扩展"**，并落到对外开放政策层面，而非"有重要启示"。
- 复现：海关库的跨年匹配、中间商剔除、暴露度构造须可复现，契合本刊自 2023 年第 10 期起的数据 /
  代码公开政策（[`jwe-data-sources`](../../skills/jwe-data-sources/SKILL.md)）。

---

> **格式与体例提示**：以上仅演示引言的论证骨架。中英文标题、内容提要（约 400—500 字）、关键词
> （约 5—6 个）、脚注（页下注）与文末参考文献体例、双向匿名（正文不得出现作者身份信息）、JEL /
> 中图分类号是否强制等，一律以本包 [`official-source-map.md`](../official-source-map.md) 标注的
> 核实状态与官网最新《投稿须知》为准；标「待核实」者勿写死。
