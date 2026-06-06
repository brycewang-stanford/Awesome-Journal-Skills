# 实证研究外部工具与资源

本文档整理了向《经济研究》投稿实证研究论文时可能需要的外部工具、数据资源和辅助软件。

## 一、数据资源

### 常用微观数据库
| 数据库 | 来源 | 适用研究领域 |
|--------|------|-------------|
| 国泰安（CSMAR） | 深圳希施玛数据科技有限公司 | 公司金融、治理、财务报表 |
| Wind | 万得信息技术股份有限公司 | 金融市场、债券、基金 |
| 中国研究数据服务平台（CNRDS） | 北京博科恒辉科技有限公司 | 公司创新、专利、ESG |
| 中国工业企业数据库 | 国家统计局 | 工业企业生产、出口 |
| 中国海关数据库 | 海关总署 | 贸易、进口出口 |
| 全国税收调查数据库 | 国家税务总局 | 税收、企业经营 |
| 中国家庭金融调查（CHFS） | 西南财经大学 | 家庭金融、消费、房产 |
| 中国健康与养老追踪调查（CHARLS） | 北京大学 | 健康、养老、劳动 |
| 中国家庭追踪调查（CFPS） | 北京大学 | 社会、经济、教育 |

### 宏观数据库
| 数据库 | 来源 | 适用研究领域 |
|--------|------|-------------|
| 中国统计年鉴 | 国家统计局 | 宏观经济 |
| 世界银行WDI | World Bank | 国际比较 |
| OECD数据库 | OECD | 国际比较 |

### 政策类数据
| 数据源 | 说明 | 获取方式 |
|--------|------|----------|
| 金税工程 | 税收征管数字化 | 税收调查数据 |
| 工商企业注册 | 企业成立、注销 | 天眼查、企查查 |
| 专利数据库 | 中国专利 | 国家知识产权局 |
| 政府采购数据 | 政府采办 | 中国政府采购网 |

## 二、统计软件

### Stata
- **推荐版本**：Stata 17/18 SE
- **常用包**：
  - `reghdfe`：高维固定效应回归（面板基准首选）
  - **交叠 DID（异质性稳健，2019 后必备）**：`csdid`（Callaway-Sant'Anna）、`did_imputation`（Borusyak-Jaravel-Spiess）、`did2s`（Gardner）、`eventstudyinteract`（Sun-Abraham）、`did_multiplegt_dyn`（de Chaisemartin-D'Haultfœuille）、`bacondecomp`（Goodman-Bacon 分解）
  - **IV**：`ivreg2` + `ranktest`（KP rk F）、`weakivtest`（有效 F）、`weakiv`（AR 稳健推断）、`ivreg2h`（Lewbel）
  - **RDD**：`rdrobust`、`rdbwselect`、`rddensity`（CJM 操纵检验）
  - **DML**：`ddml` + `pystacked`、`pdslasso`
  - **稳健性**：`boottest`（少聚类 wild bootstrap）、`acreg`（Conley 空间 SE）、`psacalc`（Oster 边界）、`winsor2`（缩尾）
  - **机制**：直接用 `reghdfe` 跑 D→M（**不要用 `sgmediation` 中介三步法**，见江艇 2022 / er-mechanism）
  - **匹配/合成控制**：`psmatch2`、`synth`、`synth_runner`
  - **制表**：`estout`（esttab，三线表导出）

### Python
- **常用库**：
  - `pandas`：数据处理
  - `numpy`：数值计算
  - `statsmodels`：计量经济模型
  - `scikit-learn`：机器学习（PSM等）
  - `matplotlib`/`seaborn`：可视化

### R
- **常用包**：
  - `dplyr`/`tidyr`：数据处理
  - `lme4`/`plm`：面板数据
  - `ivmodel`：工具变量
  - `rdrobust`：断点回归
  - `MatchIt`：倾向得分匹配

### MATLAB
- 适用于DSGE等理论模型

## 三、识别策略辅助工具

### 合成控制法
- `synth`：Stata合成控制
- `Synth`：R实现

### 交叠DID（异质性稳健估计量）
- `csdid`（Callaway-Sant'Anna 2021）/ `did_imputation`（BJS 2024）/ `did2s`（Gardner 2022）
- `eventstudyinteract`（Sun-Abraham 2021）/ `did_multiplegt_dyn`（dCDH）
- `bacondecomp`（Goodman-Bacon 2021 分解，诊断 TWFE 偏误）
- 详见 `resources/code/stata/03_did_modern.do`

### 空间计量
- `spatreg`：空间回归
- `MATLAB Spatial Econometrics Toolbox`

### 模糊断点回归
- `rdrobust`（推荐）
- `rddensity`：密度检验

## 四、数据处理与可视化

### 数据清洗
- Excel/WPS（基础处理）
- Stata（面板数据清洗）
- Python pandas（大规模数据）
- R dplyr（数据整理）

### 图形制作
- **科研图表**：Origin、ggplot2、matplotlib
- **流程图**：Visio、Draw.io、ProcessOn
- **思维导图**：XMind、MindMaster

### LaTeX排版
- TeX Live / MacTeX（发行版）
- TeXstudio / VS Code + LaTeX Workshop（编辑器）
- Overleaf（在线协作）

## 五、学术写作辅助

### 文献管理
| 工具 | 说明 |
|------|------|
| Zotero | 开源免费，插件丰富 |
| EndNote | 商业软件，期刊格式支持多 |
| Mendeley | Elsevier出品 |
| NoteExpress | 国内用户多 |

### 参考文献格式
《经济研究》采用**著者—出版年制**（非顺序编码制）：正文夹注（作者，年份[，页码]），文末中文文献在前、外文在后，各按姓氏拼音/字母排序。Zotero/EndNote 可自建该样式（参考 APA/Chicago author-date 改造），切勿套用 GB/T 7714 顺序编码（`[1][2]`）。详见 er-submission 与 official-source-map.md。

### 查重检测
- 知网查重（期刊认可）
- Turnitin（英文论文）
- iThenticate（英文论文）

### 语言润色
- 语法检查：Grammarly
- 中文学术润色：意得辑、AJE
- 英文SCI/EI润色：American Journal Experts

## 六、投稿系统相关

### 系统要求
- 浏览器：Chrome、Firefox、Edge（IE 8.0以下不支持）
- 文档格式：DOC/DOCX（Word）
- 文件大小：通常不超过10MB

### 扩展资料格式
- 附录：Word文档
- 数据：Excel/Stata dta/Dbf/CSV
- 代码：Stata .do/.ado、Python .py、R .R

## 七、其他工具

### 版本控制
- Git + GitHub/Gitee（代码管理）
- Overleaf（LaTeX协作）

### 云存储
- 百度网盘（国内分享）
- Google Drive（国际）
- 坚果云（同步+分享）

### 思维导图与笔记
- Obsidian（Markdown笔记）
- Notion（知识管理）
- Roam Research（双向链接）

### 时间管理
- Trello（项目管理）
- Todoist（任务管理）

## 八、常用网站

| 网站 | 用途 |
|------|------|
| https://erj.ajcass.com | 期刊官网 |
| https://erj.ajcass.com/Admin/user/login | 投稿系统 |
| CNKI | 文献检索 |
| Web of Science | 国际文献 |
| Google Scholar | 文献检索 |
| SSRN | 预印本 |
| RePEc | 经济学科研 |

## 九、注意事项

1. **数据合规**：使用数据库时遵守使用协议，不要大批量下载
2. **代码注释**：实证研究代码应详细注释，便于审稿核查
3. **版本管理**：保留完整的代码和数据版本，便于修改
4. **备份**：重要数据和代码定期备份
5. **匿名处理**：投稿前确保数据中无个人信息