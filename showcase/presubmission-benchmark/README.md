# Pre-submission benchmark: does the polishing pipeline catch what it should?

The repository claims its pre-submission pipeline catches the problems that get papers
desk-rejected or sent back. This directory is the evidence. It plants known defects in
realistic manuscripts and measures what the pipeline catches. It also runs the same
pipeline on clean controls to measure false alarms. Every misjudgment is reported,
including the ones the checker cannot fix.

- **Fixtures**: six synthetic manuscripts for six venue families: JF, QJE, ICML, ACL,
  JAMA, and 《经济研究》 (in Chinese). They cover Markdown and LaTeX inputs, each has
  12 planted defects (8 mechanical + 4 substantive), and each has a clean twin. See
  [`tools/tests/fixtures/manuscripts/`](../../tools/tests/fixtures/manuscripts/README.md).
- **Stage 0, deterministic preflight** (`tools/preflight.py`): scored on all 12 copies.
  The mechanical result is asserted in CI by `tools/tests/test_preflight.py`.
- **Stage 2, referee panel** (`rt-simulated-referee`): six blinded runs. Each run got one
  seeded copy and one clean copy from *different* venues under neutral file names, with
  no way of telling which was which. All outputs are committed in
  [`panel-runs/`](panel-runs/), next to the
  [blinding key](panel-runs/BLINDING-KEY.json) and the
  [brief the runs received](panel-runs/PANEL-BRIEF.md).

Full numbers and every miss: **[RESULTS.md](RESULTS.md)**.

**运行日期 / Run date:** 2026-11-23. Venue rules come from the source maps re-verified
that day, the fixtures are at their committed versions, and the panel runs used
Claude Opus 5.5.

## Reproduce

```bash
python3 -m unittest tools.tests.test_preflight -v      # mechanical contract (CI)
python3 tools/preflight.py tools/tests/fixtures/manuscripts/jf-corporate-did/manuscript.md --venue jf-skills
```

The panel runs are model output, so a re-run will not reproduce them word for word. To
re-run the panel, give an agent [`panel-runs/PANEL-BRIEF.md`](panel-runs/PANEL-BRIEF.md)
plus a seeded or clean copy built from a fixture's `defects.json`, and grade the result
against that manifest.

## 运行备注 / Run notes: what this benchmark does not show

- **Synthetic papers are easier than real ones.** The defects are planted one paragraph
  at a time, and some leave contradictions elsewhere in the paper that make them easier
  to spot. Real flaws are more diffuse. For a run on a real paper, see
  [`../presubmission-real-preprint/`](../presubmission-real-preprint/README.md).
- **Six fixtures is a small sample.** The rates are indicative, with wide uncertainty.
- **The panel runs were inline.** One agent played every referee, which is the cheaper
  of the two configurations the protocol allows. The recommended multi-agent panel runs
  independent referees and should do at least as well. That is untested here.
- **The maintainer agent did the grading.** The grading rules are in RESULTS.md and the
  raw panel outputs are committed, so anyone can re-grade.
