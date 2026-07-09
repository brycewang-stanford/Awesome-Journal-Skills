# 外部工具清单 · 《通信学报》(Journal on Communications, JOC)

面向《通信学报》(Journal on Communications, JOC) 通信学科长文的写作、仿真、查重与制图工具。工具为
中立建议，本刊不指定或背书任何商业软件；一切格式以官方模板与投稿须知为准。

## 一、写作与排版

| 工具 | 用途 | 备注 |
|---|---|---|
| LaTeX（CTeX/XeLaTeX）+ 本刊模板 | 中文长文排版、公式、参考文献 | 中文需 ctex/xeCJK；参考文献按 GB/T 7714 |
| Word + 本刊模板 | 不熟悉 LaTeX 者的替代方案 | 从官网下载中心取模板 |
| JabRef / Zotero | 文献管理与 BibTeX | 配 GB/T 7714 样式（gbt7714 宏包） |
| 中文断字/标点检查 | 全半角、量与单位规范 | 数字与单位间空格、量符号用斜体 |

## 二、通信仿真与数值实验

| 工具 | 用途 |
|---|---|
| MATLAB（Communications / 5G Toolbox） | 链路级/系统级仿真、信道模型、BER/吞吐曲线 |
| NS-3 / OMNeT++ | 网络协议与系统级仿真（路由、MAC、拥塞） |
| Python（NumPy/SciPy/CommPy） | 调制解调、信道编码、蒙特卡洛仿真 |
| Sionna / GNU Radio | 基于神经网络的物理层、软件无线电原型 |
| Wireshark / Mininet | 网络流量分析与 SDN 实验 |

## 三、信息安全与密码实验

| 工具 | 用途 |
|---|---|
| OpenSSL / PyCryptodome | 密码原语与协议实现 |
| ProVerif / Tamarin | 安全协议形式化验证 |
| Scapy | 协议构造与攻击流量复现 |

## 四、查重与合规

| 工具 | 用途 | 备注 |
|---|---|---|
| 知网(CNKI)学术不端检测系统 AMLC | 本刊官方查重口径 | 与已发表论文重复率 **> 20% 不予收录** |
| 自查：Turnitin/维普（辅助） | 投前预估 | 最终以知网口径为准 |

## 五、制图与数据可视化

| 工具 | 用途 |
|---|---|
| Matplotlib / TikZ / PGFPlots | 矢量曲线图（SNR-BER、CDF、吞吐-时延） |
| Origin / Visio | 系统框图、协议时序图 |
| draw.io | 网络拓扑与流程图 |

## 六、检索与信息源

| 工具 | 用途 |
|---|---|
| CNKI / 万方 / 维普 | 中文文献与本刊往期 |
| IEEE Xplore / dblp | 英文对照文献 |
| CCF 推荐中文科技期刊目录 | 定位与兄弟刊分工 |

> 提示：仿真类实验务必固定随机种子、信道实现与参数表（见 `jonc-reproducibility`），并在正文给出
> 蒙特卡洛次数与置信区间，以经受《通信学报》/Journal on Communications (JOC) 外审对统计严谨性的
> 检验。
