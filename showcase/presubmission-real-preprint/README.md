# Real preprint, full pipeline: arXiv:2611.21070 → AER: Insights (hypothetical)

The benchmark next door uses synthetic papers with planted defects. This case runs
`rt-submission-readiness` end to end on a **real public preprint**, to show what the
pipeline produces for an actual author and where it is still wrong.

- **Paper:** Suguru Otani and Chang Yang, "Trade Tensions Meet the Gig Economy: Evidence from the
  2025 Halving of Chinese Travel to Japan", arXiv:2611.21070, licensed
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Source and PDF:
  <https://arxiv.org/abs/2611.21070>. Only short excerpts are quoted here; the paper
  itself is not redistributed.
- **Target venue:** *American Economic Review: Insights*. This is our choice for the
  demonstration. The authors have not said where they will submit, and nothing here is a
  statement about their plans.
- **Inputs:** the arXiv LaTeX source (with `\input` tables and `.bbl`) and the arXiv PDF.

**运行日期 / Run date:** 2026-11-23. AER: Insights rules come from the source map that
was re-verified the same day. Stages 1–4 were run by Claude Opus 5.5 following the
skill as written.

## Files

| Stage | File |
|---|---|
| 0 · Preflight, as run | [`00-preflight-tex-as-run.txt`](00-preflight-tex-as-run.txt) · [`00-preflight-pdf-as-run.txt`](00-preflight-pdf-as-run.txt) · [`00-preflight-pdf-online-as-run.txt`](00-preflight-pdf-online-as-run.txt) · [`00-preflight-as-run.json`](00-preflight-as-run.json) |
| 0 · Preflight, after the fixes this run prompted | [`00-preflight-tex.txt`](00-preflight-tex.txt) · [`00-preflight-pdf.txt`](00-preflight-pdf.txt) · [`00-preflight-pdf-online.txt`](00-preflight-pdf-online.txt) · [`00-preflight.json`](00-preflight.json) |
| 1 · Readiness scorecard | [`01-scorecard.md`](01-scorecard.md) |
| 2 · Referee panel (inline, form C) | [`02-referee-panel.md`](02-referee-panel.md) |
| 3 · Prose polish | [`03-polish.md`](03-polish.md) |
| 4 · Cover letter and statements | [`04-letter-and-statements.md`](04-letter-and-statements.md) |
| Summary + preflight feedback | **[`REPORT.md`](REPORT.md)** |

## 运行备注 / Run notes

- **What this run changed.** It found five things wrong with `preflight.py` that the
  synthetic benchmark had not. The worst was a silent false green: the AEA exhibit cap
  and the 200-words-per-exhibit deduction were never tested, yet *not checked* was
  empty. It also found a misframed FAIL for a statement that must be a separate upload,
  a missed significance-asterisk rule, a PDF reference-splitting bug, and Crossref
  "misses" that were working papers. All were fixed in the same release; the table in
  [`REPORT.md`](REPORT.md) maps each one to its fix. The *-as-run* files keep the
  original output, so the before and after can be compared.
- **The panel is inline.** One agent played every referee, so its concerns may be
  correlated. Its decision band is a rehearsal, not a prediction.
- **Arithmetic marked [verify].** The yen-per-hour conversion in stage 3 is the
  reviewer's arithmetic from the paper's own numbers, not the authors' figure.
- **Constructive intent.** The paper is careful work with a clean natural experiment.
  The critique aims to show what a pre-submission check surfaces, not to grade the
  authors.
