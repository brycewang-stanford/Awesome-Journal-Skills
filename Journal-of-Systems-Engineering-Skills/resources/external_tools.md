# 外部工具与复现选择

工具必须跟随研究主线，不得为了“显得复杂”而堆叠软件。

| 任务 | 推荐工具 | 最小交付 |
|---|---|---|
| 线性/混合整数优化 | Pyomo、JuMP、Gurobi/CPLEX/HiGHS | 模型文件、求解器版本、容差、时间限制、实例与日志 |
| 元启发式/路径问题 | Python/Julia/MATLAB | 伪代码、随机种子、多次重复、基线、收敛轨迹、规模梯度 |
| 博弈与比较静态 | SymPy/Mathematica/Maple + 数值脚本 | 均衡条件、符号推导说明、边界扫描，不以软件输出代替证明 |
| 复杂网络 | NetworkX、igraph、NetLogo | 构网规则、拓扑统计、初始状态、重复次数、干预策略 |
| 离散事件/系统动力学 | SimPy、AnyLogic、Vensim | 事件逻辑/方程、校准来源、预热期、终止准则、情景表 |
| 预测/机器学习 | scikit-learn、statsmodels、PyTorch | 时间切分、预处理管道、防泄漏、基准、样本外指标 |
| 空间/面板/金融实证 | R、Stata、Python | 数据字典、识别假设、聚类层级、诊断与替代规格 |
| MBSE/工程追溯 | SysML/KARMA、OSLC、Simulink | 架构版本、接口、追溯矩阵、模型到仿真的可执行链 |

涉及现代因果推断时，优先调用仓库共享
[execution-with-mcp](../../shared-resources/empirical-methods/execution-with-mcp.md)；
它不适用于纯优化、解析博弈、MBSE 或网络扩散模型。

## 禁止做法

- 只报告“算法更优”，不说明实例、基线、预算和随机波动。
- 用训练集结果充当样本外预测。
- 把求解器返回 `optimal` 当作理论证明。
- 删除失败实例或只展示最佳随机种子。
- 在无法分享原始数据时不提供变量构造、来源和受限访问路径。
