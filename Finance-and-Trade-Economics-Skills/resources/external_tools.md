# 财经实证研究外部工具与资源

本文档整理了向《财贸经济》投稿实证研究论文时可能需要的外部工具、数据资源和辅助软件，侧重财政、税收、金融、贸易、流通、消费等财经研究场景。

## 一、数据资源

### 企业 / 金融微观数据（财经核心数据）
| 数据库 | 来源 | 适用研究领域 |
|---|---|---|
| CSMAR 国泰安 | 深圳希施玛 | 上市公司财务、公司金融、税负、投资 |
| WIND 万得 | 万得资讯 | 金融市场、宏观、债券、基金、行情 |
| CNRDS 中国研究数据服务平台 | CNRDS | 上市公司治理、ESG、专利、文本 |
| RESSET 锐思 | 北京聚源 | 股票、债券、财务、基金 |
| 中国工业企业数据库 | 国家统计局 | 制造业企业、生产率、进入退出 |
| 中国海关贸易数据库 | 海关总署 | 出口企业、产品-目的地、贸易政策 |
| 中国税务年鉴 / 税收征管数据 | 国家税务总局 | 税制改革、征管、税负 |

### 居民 / 消费微观调查
| 数据库 | 来源 | 适用研究领域 |
|---|---|---|
| 中国家庭金融调查（CHFS） | 西南财经大学 | 居民资产、负债、消费、金融行为 |
| 中国家庭追踪调查（CFPS） | 北京大学 | 居民收入、消费、储蓄、教育 |
| 中国健康与养老追踪调查（CHARLS） | 北京大学 | 养老、健康、社会保障 |
| 北京大学数字普惠金融指数 | 北大数字金融研究中心 | 数字金融、普惠、区域 |

### 宏观 / 区域与制度数据
| 数据源 | 说明 | 获取方式 |
|---|---|---|
| CEIC 中国经济数据库 | 宏观、财政、金融、贸易高频指标 | CEIC |
| 中国财政年鉴 / 中国金融统计年鉴 | 财政收支、货币金融存量 | 国家统计局 / 财政部 / 央行 |
| 中国城市 / 县域统计年鉴 | 城市 / 县域面板 | 国家统计局 |
| 樊纲—王小鲁市场化指数 | 省级市场化、要素市场、法治环境 | 公开报告 / 数据库 |
| 财税 / 金融 / 贸易政策文件 | 改革试点批次、实施时点 | 部委官网、政策文件整理 |

## 二、统计软件

### Stata
- **推荐版本**：Stata 17/18 SE/MP
- **常用包**：
  - `didregress` / `csdid` / `did_multiplegt`：交叠 / 连续处理 DID
  - `eventstudyinteract`：Sun-Abraham 事件研究
  - `bacondecomp`：Goodman-Bacon 分解
  - `reghdfe`：高维固定效应（企业 / 城市 / 行业×年）
  - `ivreg2` / `ivreghdfe`：工具变量（处理政策内生）
  - `rdrobust` / `rddensity`：断点回归 + 密度检验
  - `ddml` / `pdslasso`：双重机器学习 / 后选择推断
  - `medsem` / `causalmed`：中介 / 因果中介
  - `winsor2`：缩尾处理

### Python
- **常用库**：
  - `pandas` / `numpy`：数据处理与数值计算
  - `linearmodels`：面板与 IV 估计
  - `statsmodels`：计量模型
  - `DoubleML` / `econml`：双重机器学习 / 异质处理效应
  - `scikit-learn`：机器学习学习器（DML 的 nuisance 估计）
  - `matplotlib` / `seaborn`：可视化

### R
- **常用包**：
  - `dplyr` / `tidyr`：数据处理
  - `fixest`：高维固定效应 + 交互
  - `did`（Callaway-Sant'Anna）/ `didimputation`：现代 DID
  - `rdrobust` / `rddensity`：断点回归
  - `DoubleML`：双重机器学习
  - `mediation`：因果中介

## 三、识别策略辅助工具

### 现代交叠 DID（处理 staggered 偏误）
- `csdid` / `did`（Callaway-Sant'Anna）
- `eventstudyinteract`（Sun-Abraham）
- `did_multiplegt`（de Chaisemartin-D'Haultfœuille）
- `bacondecomp`（坏比较权重诊断）

### 工具变量与弱工具
- `ivreghdfe` / `ivreg2`
- `weakivtest`、Anderson-Rubin 检验（弱工具稳健 CI）
- Bartik / 份额移动工具的诊断

### 断点回归
- `rdrobust`（最优带宽）
- `rddensity`（McCrary 密度检验，防主体操纵分组）

### 双重机器学习 / 稳健推断
- `ddml`、`pdslasso`（Stata）、`DoubleML`、`econml`（Python）
- 交叉拟合 + Neyman 正交；多学习器稳健性

### 合成控制
- `synth` / `synth_runner`（Stata）、`Synth` / `tidysynth`（R）

## 四、数据处理与可视化

- **数据清洗**：Stata（面板）、Python pandas（大规模）、R dplyr
- **科研图表**：ggplot2、matplotlib、Origin
- **事件研究 / 森林图**：`coefplot`（Stata）、`ggplot2`（R）
- **空间 / 地理分布图**：QGIS、`sf` + `ggplot2`
- **流程 / 机制路径图**：Draw.io、ProcessOn、Visio

## 五、学术写作辅助

### 文献管理
| 工具 | 说明 |
|---|---|
| Zotero | 开源免费，插件丰富 |
| EndNote | 商业软件，期刊格式支持多 |
| NoteExpress | 国内用户多，中文期刊格式友好 |

### 参考文献格式
《财贸经济》采用本刊统一格式，Zotero / EndNote 可自定义样式；具体格式以官网投稿须知为准。

### 查重检测
- 知网查重（中文期刊认可）

## 六、投稿与协作

### 系统要求
- 浏览器：Chrome、Firefox、Edge
- 文档格式：DOC / DOCX
- 在线投审稿系统 + 匿名评审（投稿系统入口 `cmjj.ajcass.com`，具体以官网为准）

### 扩展资料格式
- 附录：Word 文档
- 数据：Excel / Stata dta / CSV
- 代码：Stata .do/.ado、Python .py、R .R

### 版本控制与云存储
- Git + GitHub / Gitee（代码管理）
- 坚果云 / 百度网盘（数据备份与分享）

## 七、注意事项

1. **数据合规**：使用商业数据库遵守使用协议，微观个体信息严格脱敏
2. **政策内生处理**：财税 / 金融 / 贸易政策的投放常非随机，识别时必须正面处理内生性与预期效应
3. **时间逻辑**：面板要保证机制变量在处理之后、结果之前测量，不用未来信息
4. **代码注释**：实证代码详细注释，便于审稿核查与录用后提交
5. **数据来源点名**：变量来源精确到数据库 / 统计，自行整理的交代口径与样本量（数据来源不透明是本刊退稿雷区）

## 八、常用网站

| 网站 | 用途 |
|---|---|
| 中国社会科学院财经战略研究院（NAES） | 主办单位 |
| 《财贸经济》投稿系统（cmjj.ajcass.com） | 投稿（网址以官网为准） |
| 国家税务总局 / 财政部 / 中国人民银行 | 财税金融政策与统计 |
| 海关总署 | 贸易数据与政策 |
| CNKI | 中文文献检索 |
| Web of Science / Google Scholar | 国际文献检索 |
| NBER / SSRN | 工作论文与预印本 |
