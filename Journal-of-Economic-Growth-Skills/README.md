<p align="center">
  <img src="assets/cover.svg" alt="Journal of Economic Growth — Agent Skills" width="200">
</p>

<h1 align="center">Journal of Economic Growth — Agent Skills</h1>

<p align="center">
  An opinionated, venue-specific agent skill stack for manuscripts targeted at the
  <strong>Journal of Economic Growth (JEG)</strong> — the specialist Springer Nature
  outlet for theoretical and empirical research in <strong>economic growth and dynamic
  macroeconomics</strong>.
</p>

<p align="center">
  <a href="README.zh-CN.md">中文文档</a>
</p>

---

## What this is

Twelve composable skills that walk a growth paper from idea to submission and
revision, each tuned to JEG's actual norms rather than generic advice. JEG is **not**
a general-interest economics journal: its scope is confined to growth and dynamic
macroeconomics — neoclassical and endogenous growth, human capital, fertility, the
demographic transition, trade-and-growth, financial development, migration,
technological change, the political economy of growth, and OLG models. It publishes
**both rigorous theory and careful empirics**, so these skills branch by paper type
throughout.

Edited by **Oded Galor** (Editor-in-Chief; Brown University and the Hebrew University
of Jerusalem) and published by **Springer Nature** (est. 1996, quarterly; ISSN
1381-4338 print / 1573-7020 electronic).

## Key venue facts baked into the skills

- **Submission** runs through the Springer Nature "Submit manuscript" portal
  (`submission.nature.com/new-submission/10887/3`) — *not* Editorial Express.
- **No submission/handling fee.** Hybrid journal; optional open access (Open Choice)
  carries an APC of GBP 3,090 / USD 4,590 / EUR 3,590 (current as of 2026-06-01;
  revised periodically — verify).
- **LaTeX preferred** (Springer Nature template), **Word (.docx) accepted**. An
  **editable source file is required at every submission and revision.**
- **References** are author-year in-text with an **APA 7th edition** reference list.
- **Title page** must carry the abstract (**150-250 words**), **4-6 keywords**, **JEL
  classification codes**, ORCID, corresponding-author email, and a
  **Statements/Declarations** section.
- **No stated manuscript word/length limit.**
- **Data Availability Statement** required (Springer Nature research data policy).
  There is **no AEA/Econometrica-style mandatory code archive or data editor** stated
  for JEG (待核实 — see source map).
- **Author Contribution** and **Competing Interest** declarations are entered in the
  portal at submission; **LLMs cannot be authors** and their use must be disclosed.
- **Peer-review model (single- vs double-blind) is not stated officially — 待核实.**

> Anything not confirmable on an official Springer page is flagged **待核实** in the
> skills and in [`resources/official-source-map.md`](resources/official-source-map.md).
> Re-verify volatile items (APC, editors, review model, word limit) before relying on them.

## The twelve skills

| Skill | Purpose |
|-------|---------|
| `jeg-workflow` | End-to-end map from idea to acceptance; routes to the other skills |
| `jeg-topic-selection` | Is the question a first-order *growth* question within JEG's scope? |
| `jeg-literature-positioning` | Place the paper across the theory/empirics growth literature |
| `jeg-identification-strategy` | Dual track: causal design (empirical) **or** assumptions/proofs/generality (theory) |
| `jeg-data-analysis` | Cross-country/panel growth estimation; or numerical calibration for theory |
| `jeg-tables-figures` | Convergence plots, transition paths, growth-regression tables |
| `jeg-contribution-framing` | State the marginal contribution to growth knowledge |
| `jeg-writing-style` | JEG house style: APA 7 author-year, abstract window, JEL codes |
| `jeg-replication-and-data-policy` | Springer Nature Data Availability Statement; theory vs empirics |
| `jeg-review-process` | What to expect from the Springer Nature editorial process |
| `jeg-submission` | Pre-submission preflight for the Springer Nature portal |
| `jeg-rebuttal` | Response-to-referees strategy on an R&R |

## How to use

Point your agent at the relevant `skills/jeg-<role>/SKILL.md`. Start with
`jeg-workflow` to orient, `jeg-topic-selection` early, and `jeg-submission` last.
Each skill is self-contained and names the JEG-specific facts it relies on.

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — every used fact, its official URL, accessed 2026-06-01, with 待核实 flags.
- [`resources/external_tools.md`](resources/external_tools.md) — data sources and software for growth empirics **and** theory.

## License

MIT — see [LICENSE](LICENSE). This is an independent aid; it is not affiliated with,
endorsed by, or published by the Journal of Economic Growth or Springer Nature.
