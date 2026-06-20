"""
clean_panel.py —— Panel-data cleaning template (pandas)

The Python counterpart of Stata 01_clean.do. Suited to large-scale micro data
that is processed out-of-core / in chunks before entering Stata. Same principles:
raw is read-only, filters are recorded, winsorization is traceable.
"""
from __future__ import annotations
import numpy as np
import pandas as pd

RAW = "data/raw"
CLEAN = "data/clean"


def winsorize(s: pd.Series, lower: float = 0.01, upper: float = 0.99) -> pd.Series:
    """Two-sided winsorization by quantile to mitigate outliers."""
    lo, hi = s.quantile(lower), s.quantile(upper)
    return s.clip(lower=lo, upper=hi)


def build_analysis_sample() -> pd.DataFrame:
    # 1. Read and merge (state merge keys and match rate)
    main = pd.read_stata(f"{RAW}/main.dta")
    extra = pd.read_stata(f"{RAW}/extra1.dta")
    df = main.merge(extra, on=["id", "year"], how="left", indicator=True)
    print("merge match rate:", (df["_merge"] == "both").mean().round(3))
    df = df.drop(columns="_merge")

    # 2. Sample filters (record each step)
    n0 = len(df)
    df = df[df["category"] != "excluded_group"]
    df = df[~df["name"].str.contains("FLAG", na=False)]
    df = df.dropna(subset=["Y", "treat"])
    print(f"sample filtering: {n0} -> {len(df)}")

    # 3. Variable construction (formula + source notes, per the variable-definition table)
    df["size"] = np.log(df["asset"])          # Size = ln(total assets)
    df["lev"] = df["debt"] / df["asset"]      # Leverage ratio
    df["roa"] = df["ni"] / df["asset"]        # Return on assets

    # Staggered DID: first treated period (never-treated set to 0)
    first = (df[df["treat"] == 1].groupby("id")["year"].min()
             .rename("gvar"))
    df = df.merge(first, on="id", how="left")
    df["gvar"] = df["gvar"].fillna(0).astype(int)

    # 4. Winsorize
    for v in ["Y", "size", "lev", "roa"]:
        df[v] = winsorize(df[v])

    return df


if __name__ == "__main__":
    out = build_analysis_sample()
    out.to_stata(f"{CLEAN}/analysis.dta", write_index=False, version=118)
    print("analysis.dta generated, N =", len(out))
