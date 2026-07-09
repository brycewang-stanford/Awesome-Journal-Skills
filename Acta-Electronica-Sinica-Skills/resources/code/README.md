# 研究制品打包骨架 · 《电子学报》(Acta Electronica Sinica, AES)

《电子学报》(Acta Electronica Sinica, AES) 目前无强制的 artifact evaluation 徽章（**待核实**），
但主动、规范地开放代码与数据是提升外审信任度与论文长期影响力的加分项。本文件给出一个通用的
制品打包骨架，配合技能 `aes-artifact-evaluation` 与 `aes-reproducibility` 使用。

## 目录骨架

```
artifact/
├── README.md          # 环境、依赖、运行步骤、预期输出、数据来源（一页可跑通）
├── LICENSE            # 开源许可证（MIT / Apache-2.0 等）
├── env/
│   ├── requirements.txt   # 或 environment.yml
│   └── Dockerfile         # 可选，最利于复现
├── src/               # 源码，入口脚本清晰
├── data/              # 小数据直接放；大数据给下载脚本+校验和
├── scripts/
│   └── run_all.sh     # 一键复现论文主结果
└── results/           # 预期输出样例（图/表/日志）供比对
```

## README 必备要素

- 硬件/环境：CPU/GPU/FPGA、OS、语言与关键库版本、仿真工具版本（MATLAB/Vivado/HFSS 等）。
- 数据：来源、规模、划分、预处理、获取方式（外链+校验和）、授权与合规。
- 运行：从零到主结果的分步命令；预计运行时间。
- 对应关系：每个脚本对应论文的哪张图/表。
- 随机性：固定并说明随机种子；随机方法多次运行。

## 双盲期匿名要求

- 匿名托管仓库或匿名压缩包；README、LICENSE、提交历史、注释、路径不泄露作者/单位。
- 清除文件元数据中的身份信息。
- 录用后再替换为署名的正式公开仓库（见 `aes-camera-ready`）。

## 学科提示

- 信号/通信类：附随机种子、信噪比范围、蒙特卡洛次数、指标(SNR/BER)计算脚本。
- 集成电路类：HDL 源码、约束、综合与时序报告、器件与工具版本。
- 电磁/微波类：仿真工程、结构参数、网格设置、实测对比。

本骨架为通用建议，非《电子学报》官方要求；请以本刊官网最新说明为准。
