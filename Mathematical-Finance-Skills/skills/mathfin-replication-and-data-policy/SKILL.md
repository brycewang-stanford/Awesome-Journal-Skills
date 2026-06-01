---
name: mathfin-replication-and-data-policy
description: Use when preparing Wiley data availability statements and reproducibility notes for a Mathematical Finance manuscript, especially when the paper has no empirical data but includes numerical experiments or illustrative code.
---

# Replication & Data Policy (mathfin-replication-and-data-policy)

## When to trigger

- The manuscript needs a Data Availability Statement
- Numerical experiments, simulations, or code accompany the theory
- The paper uses no data and you need the correct statement

## Policy stance

Wiley policy expects research articles to include a Data Availability Statement.
For this journal, that often means saying no empirical data were generated or
used. There is no journal-specific mandatory replication archive comparable to
empirical economics/finance data archives, but code for numerical illustrations
should be reproducible when included.

## Statement templates

### No data

```text
Data availability statement: No empirical data were generated or analysed in
support of this research.
```

### Numerical code only

```text
Data availability statement: The numerical code used to generate the illustrative
figures/tables is available at [repository/DOI]. No proprietary empirical data
were used.
```

### Public data, if unusually used

```text
Data availability statement: The data are publicly available from [source] at
[URL]. The code used for the numerical analysis is available at [repository/DOI].
```

## Reproducibility checklist

- Set and report random seeds.
- Record software, package, compiler, and LaTeX versions when relevant.
- Include scripts that regenerate each numerical exhibit.
- Make parameter values and discretization choices visible.
- Cite archived code with a DOI when feasible.

## Output format

```text
[Data status] no data / numerical code / public data / other
[Statement] ...
[Code archive] ...
[Missing reproducibility details] ...
[Next step] mathfin-submission
```
