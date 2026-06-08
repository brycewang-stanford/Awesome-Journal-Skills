"""
clean_panel.py —— 面板数据清洗模板（pandas）

对应 Stata 01_clean.do 的 Python 版。适合大规模微观数据（工业企业库、海关库、
税收调查）在内存外 / 分块处理后再进 Stata。原则同：原始只读、筛选留痕、缩尾可追溯。
"""
from __future__ import annotations
import numpy as np
import pandas as pd

RAW = "data/raw"
CLEAN = "data/clean"


def winsorize(s: pd.Series, lower: float = 0.01, upper: float = 0.99) -> pd.Series:
    """按分位双侧缩尾，缓解极端值。"""
    lo, hi = s.quantile(lower), s.quantile(upper)
    return s.clip(lower=lo, upper=hi)


def build_analysis_sample() -> pd.DataFrame:
    # 1. 读入与合并（明确合并键与匹配率）
    fin = pd.read_stata(f"{RAW}/firm_financials.dta")
    gov = pd.read_stata(f"{RAW}/governance.dta")
    df = fin.merge(gov, on=["stkcd", "year"], how="left", indicator=True)
    print("合并匹配率:", (df["_merge"] == "both").mean().round(3))
    df = df.drop(columns="_merge")

    # 2. 样本筛选（每步留痕）
    n0 = len(df)
    df = df[df["industry"] != "金融业"]
    df = df[~df["stknm"].str.contains("ST", na=False)]
    df = df.dropna(subset=["rd_invest", "treat"])
    print(f"样本筛选: {n0} → {len(df)}")

    # 3. 变量构造（公式 + 来源注释，对应变量定义表）
    df["size"] = np.log(df["asset"])          # 企业规模 = ln(总资产), CSMAR
    df["lev"] = df["debt"] / df["asset"]      # 资产负债率
    df["roa"] = df["ni"] / df["asset"]        # 总资产收益率

    # 交叠 DID：首次受处理年份（从不处理者设为 0）
    first = (df[df["treat"] == 1].groupby("stkcd")["year"].min()
             .rename("gvar"))
    df = df.merge(first, on="stkcd", how="left")
    df["gvar"] = df["gvar"].fillna(0).astype(int)

    # 4. 缩尾
    for v in ["rd_invest", "size", "lev", "roa"]:
        df[v] = winsorize(df[v])

    return df


if __name__ == "__main__":
    out = build_analysis_sample()
    out.to_stata(f"{CLEAN}/analysis.dta", write_index=False, version=118)
    print("analysis.dta 已生成, N =", len(out))
