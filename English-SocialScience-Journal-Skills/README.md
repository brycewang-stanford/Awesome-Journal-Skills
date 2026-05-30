# English Social-Science Journal Skills

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Index](https://img.shields.io/badge/index-FT50%20%C2%B7%20UTD24%20%C2%B7%20top--5-1f6feb)](#)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

An opinionated agent skill stack for the **100 mainstream English-language economics / finance / management / accounting / marketing / operations / information-systems journals** on the parent repository's roadmap — every economics "top-5", the finance "top-3", the AOM / SMS management elite, and the FT50 / UTD24 / ABS 4★ venues.

This is the English-language sibling of [`Chinese-SocialScience-Journal-Skills`](../Chinese-SocialScience-Journal-Skills/). Like that bundle, it ships **one self-contained fit-and-house-style skill per journal**, plus `en-journal-workflow` for routing. Each journal skill helps answer: *is my manuscript on-target, how should it be framed, what method and evidence does this venue expect, and what official submission details must be re-checked?*

For the AEA flagship, a full lifecycle pack ships separately as `AER-skills` (the `aer-*` skills). The `american-economic-review` profile here is the quick fit layer that routes into it — exactly as the Chinese `economic-research` profile routes into the deep `Economic-Research-Journal-Skills` pack.

## Coverage

| Group | Count | Scope |
|---|--:|---|
| Economics | 50 | top-5 + AEJ family, JEL/JEP/REStat, the field flagships (econometrics, macro/monetary, labor, public, IO, trade, development, health, urban, enviro, law-and-economics), plus policy/review venues. |
| Finance | 13 | the top-3 (JF/JFE/RFS) plus the elite field journals (banking, intermediation, microstructure, corporate, international, empirical, mathematical finance). |
| Management / Strategy / Organization | 15 | AMJ/AMR/AMA/ASQ/SMJ/OrgSci, JOM, JMS, OS, Human Relations, HRM, JIBS, Research Policy, JBV, ETP. |
| Marketing | 6 | JM, JMR, Marketing Science, JCR, JCP, JAMS. |
| Accounting | 6 | TAR, JAR, JAE, RAST, CAR, AOS. |
| Operations & Information Systems | 10 | Management Science, OR, M&SOM, JOM-ops, POM; MISQ, ISR, JMIS, JAIS, IJOC. |

## Quick Start

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install english-socsci-journal-skills
/reload-plugins
```

Manual copy:

```bash
cp -R skills/* ~/.claude/skills/
# or for Codex
cp -R skills/* ~/.codex/skills/
```

## How to Use

Start with `en-journal-workflow` when the venue is uncertain — it classifies the manuscript by contribution type, method shape, discipline audience, and submission goal, then routes to the matching per-journal skill. If the target is already known, name the journal directly, for example: “Use `journal-of-finance` to assess this asset-pricing paper for JF.”

Every skill returns a fit verdict, method/evidence requirements, desk-reject risks, official-submission checks, and reroute suggestions.

## Skills

### Economics (50)

| Skill | Journal |
|---|---|
| `american-economic-review` | American Economic Review (AER) |
| `quarterly-journal-of-economics` | Quarterly Journal of Economics (QJE) |
| `journal-of-political-economy` | Journal of Political Economy (JPE) |
| `econometrica` | Econometrica |
| `review-of-economic-studies` | Review of Economic Studies (REStud) |
| `aer-insights` | AER: Insights |
| `aej-applied-economics` | AEJ: Applied Economics |
| `aej-macroeconomics` | AEJ: Macroeconomics |
| `aej-microeconomics` | AEJ: Microeconomics |
| `aej-economic-policy` | AEJ: Economic Policy |
| `journal-of-economic-literature` | Journal of Economic Literature (JEL) |
| `journal-of-economic-perspectives` | Journal of Economic Perspectives (JEP) |
| `review-of-economics-and-statistics` | Review of Economics and Statistics (REStat) |
| `journal-of-econometrics` | Journal of Econometrics |
| `journal-of-monetary-economics` | Journal of Monetary Economics |
| `journal-of-economic-growth` | Journal of Economic Growth |
| `journal-of-labor-economics` | Journal of Labor Economics |
| `journal-of-the-european-economic-association` | Journal of the European Economic Association (JEEA) |
| `the-economic-journal` | The Economic Journal (EJ) |
| `rand-journal-of-economics` | RAND Journal of Economics |
| `journal-of-international-economics` | Journal of International Economics |
| `journal-of-public-economics` | Journal of Public Economics |
| `journal-of-development-economics` | Journal of Development Economics (JDE) |
| `journal-of-economic-theory` | Journal of Economic Theory (JET) |
| `journal-of-money-credit-and-banking` | Journal of Money, Credit and Banking (JMCB) |
| `review-of-economic-dynamics` | Review of Economic Dynamics (RED) |
| `european-economic-review` | European Economic Review (EER) |
| `journal-of-human-resources` | Journal of Human Resources (JHR) |
| `international-economic-review` | International Economic Review (IER) |
| `experimental-economics` | Experimental Economics |
| `journal-of-applied-econometrics` | Journal of Applied Econometrics |
| `journal-of-business-and-economic-statistics` | Journal of Business & Economic Statistics (JBES) |
| `journal-of-health-economics` | Journal of Health Economics |
| `journal-of-environmental-economics-and-management` | Journal of Environmental Economics and Management (JEEM) |
| `journal-of-urban-economics` | Journal of Urban Economics |
| `games-and-economic-behavior` | Games and Economic Behavior (GEB) |
| `journal-of-law-and-economics` | Journal of Law and Economics |
| `journal-of-law-economics-and-organization` | Journal of Law, Economics, and Organization (JLEO) |
| `world-development` | World Development |
| `world-bank-economic-review` | World Bank Economic Review |
| `imf-economic-review` | IMF Economic Review |
| `annual-review-of-economics` | Annual Review of Economics |
| `brookings-papers-on-economic-activity` | Brookings Papers on Economic Activity (BPEA) |
| `economic-policy` | Economic Policy |
| `journal-of-risk-and-uncertainty` | Journal of Risk and Uncertainty (JRU) |
| `quantitative-economics` | Quantitative Economics |
| `the-econometrics-journal` | The Econometrics Journal |
| `econometric-theory` | Econometric Theory |
| `journal-of-economic-behavior-and-organization` | Journal of Economic Behavior & Organization (JEBO) |
| `journal-of-economic-geography` | Journal of Economic Geography |

### Finance (13)

| Skill | Journal |
|---|---|
| `journal-of-finance` | Journal of Finance (JF) |
| `journal-of-financial-economics` | Journal of Financial Economics (JFE) |
| `review-of-financial-studies` | Review of Financial Studies (RFS) |
| `review-of-finance` | Review of Finance |
| `journal-of-financial-and-quantitative-analysis` | Journal of Financial and Quantitative Analysis (JFQA) |
| `journal-of-financial-intermediation` | Journal of Financial Intermediation (JFI) |
| `journal-of-financial-markets` | Journal of Financial Markets (JFM) |
| `journal-of-banking-and-finance` | Journal of Banking & Finance (JBF) |
| `journal-of-corporate-finance` | Journal of Corporate Finance (JCF) |
| `journal-of-international-money-and-finance` | Journal of International Money and Finance (JIMF) |
| `mathematical-finance` | Mathematical Finance |
| `journal-of-empirical-finance` | Journal of Empirical Finance (JEF) |
| `financial-management` | Financial Management |

### Management / Strategy / Organization (15)

| Skill | Journal |
|---|---|
| `academy-of-management-journal` | Academy of Management Journal (AMJ) |
| `academy-of-management-review` | Academy of Management Review (AMR) |
| `academy-of-management-annals` | Academy of Management Annals (AMA) |
| `administrative-science-quarterly` | Administrative Science Quarterly (ASQ) |
| `strategic-management-journal` | Strategic Management Journal (SMJ) |
| `organization-science` | Organization Science |
| `journal-of-management-en` | Journal of Management (JOM) |
| `journal-of-management-studies` | Journal of Management Studies (JMS) |
| `organization-studies` | Organization Studies |
| `human-relations` | Human Relations |
| `human-resource-management` | Human Resource Management (HRM) |
| `journal-of-international-business-studies` | Journal of International Business Studies (JIBS) |
| `research-policy` | Research Policy |
| `journal-of-business-venturing` | Journal of Business Venturing (JBV) |
| `entrepreneurship-theory-and-practice` | Entrepreneurship Theory and Practice (ETP) |

### Marketing (6)

| Skill | Journal |
|---|---|
| `journal-of-marketing` | Journal of Marketing (JM) |
| `journal-of-marketing-research` | Journal of Marketing Research (JMR) |
| `marketing-science` | Marketing Science |
| `journal-of-consumer-research` | Journal of Consumer Research (JCR) |
| `journal-of-consumer-psychology` | Journal of Consumer Psychology (JCP) |
| `journal-of-the-academy-of-marketing-science` | Journal of the Academy of Marketing Science (JAMS) |

### Accounting (6)

| Skill | Journal |
|---|---|
| `the-accounting-review` | The Accounting Review (TAR) |
| `journal-of-accounting-research` | Journal of Accounting Research (JAR) |
| `journal-of-accounting-and-economics` | Journal of Accounting and Economics (JAE) |
| `review-of-accounting-studies` | Review of Accounting Studies (RAST) |
| `contemporary-accounting-research` | Contemporary Accounting Research (CAR) |
| `accounting-organizations-and-society` | Accounting, Organizations and Society (AOS) |

### Operations & Information Systems (10)

| Skill | Journal |
|---|---|
| `management-science` | Management Science |
| `operations-research` | Operations Research (OR) |
| `manufacturing-and-service-operations-management` | Manufacturing & Service Operations Management (M&SOM) |
| `journal-of-operations-management` | Journal of Operations Management (JOM-ops) |
| `production-and-operations-management` | Production and Operations Management (POM) |
| `mis-quarterly` | MIS Quarterly (MISQ) |
| `information-systems-research` | Information Systems Research (ISR) |
| `journal-of-management-information-systems` | Journal of Management Information Systems (JMIS) |
| `journal-of-the-association-for-information-systems` | Journal of the Association for Information Systems (JAIS) |
| `informs-journal-on-computing` | INFORMS Journal on Computing (IJOC) |

### Routing

| Skill | Role |
|---|---|
| `en-journal-workflow` | English econ / business journal routing workflow (not a journal) |

## Source Discipline

Editorial rules change. The bundled [`resources/source-basis.md`](resources/source-basis.md) records the ranking lists and source policy used for this expansion, and the deliberate omission of volatile facts (impact factors, acceptance rates, word limits, fees). Before final submission, always verify the live official author instructions on the publisher's own site or submission system.

> Naming note: the SAGE *Journal of Management* uses the slug `journal-of-management-en` because the plain `journal-of-management` is already used by the Chinese bundle for 《管理学刊》 — mirroring that bundle's own `-cn` disambiguation convention.
