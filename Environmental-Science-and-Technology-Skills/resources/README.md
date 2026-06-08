# ES&T Resources

Action-oriented resources for the Environmental Science & Technology (ES&T) skill pack. The `skills/`
give advice; this directory lets an agent **act** — model an ES&T-style abstract/introduction and
benchmark against verified exemplars. Pair these with the relevant `skills/est-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper **abstract + introduction** in ES&T house style — environmental significance first, headline magnitude with units, methods rigor (controls, mass balance, QA/QC) signaled in prose, and the mandatory TOC/abstract graphic described. Illustrative **fictional** paper; no real policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified ES&T papers** (DOI `10.1021/es...` or `10.1021/acs.est...`) organized by method × topic, with an explicit sibling-confusion guard (ES&T ≠ ES&T Letters / ACS ES&T Water / ACS ES&T Engineering / ES:P&I / Water Research). Design positioning only — no fabricated numbers. |
| [`official-source-map.md`](official-source-map.md) | **ES&T-specific policy & facts:** ACS Publishing Center / ACS Paragon Plus submission, article types & word caps, the mandatory TOC graphic, data-availability/deposition policy, ACS style, and the official URLs behind every fact in this pack. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | External tools and services referenced by the pack — analytical QA/QC, fate/transport and LCA models, structure-drawing and mapping tools, reference managers, and public-deposition repositories. |

## Scope note: no econometrics code kit vendored

This is an **environmental chemistry / engineering** journal (ACS). The shared causal-inference /
econometrics **code kit** used by the economics packs (Stata + Python DID/IV/RDD/DML pipeline) is
**deliberately NOT vendored here** — it is not the empirical idiom of ES&T. The discipline-appropriate
craft for ES&T (study design with controls and mass balance, analytical QA/QC, honest uncertainty,
reproducible master scripts, public data deposition) lives in the pack's
[`../skills`](../skills/) — see
[`est-study-design`](../skills/est-study-design/SKILL.md),
[`est-data-analysis`](../skills/est-data-analysis/SKILL.md), and
[`est-reporting-and-reproducibility`](../skills/est-reporting-and-reproducibility/SKILL.md) — and the
tooling is indexed in [`external_tools.md`](external_tools.md).

## Suggested workflow

1. Scope and frame with [`../skills/est-topic-selection`](../skills/est-topic-selection/SKILL.md)
   (the environmental-significance test) and
   [`../skills/est-writing-style`](../skills/est-writing-style/SKILL.md); model the abstract +
   introduction on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Design and analyze with rigor via
   [`../skills/est-study-design`](../skills/est-study-design/SKILL.md) (controls, replication, mass
   balance, QA/QC) and [`../skills/est-data-analysis`](../skills/est-data-analysis/SKILL.md) (honest
   uncertainty, censored-data handling); build exhibits and the TOC graphic with
   [`../skills/est-figures-and-tables`](../skills/est-figures-and-tables/SKILL.md).
3. Benchmark against verified ES&T papers in [`exemplars/library.md`](exemplars/library.md) — match your
   method × topic and pressure-test the "so what for the environment?" question.
4. Confirm article type, word caps, the TOC-art mandate, and submission/data policy in
   [`official-source-map.md`](official-source-map.md); tool up from
   [`external_tools.md`](external_tools.md).
