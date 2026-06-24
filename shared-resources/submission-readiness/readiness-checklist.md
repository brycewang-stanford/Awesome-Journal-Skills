# Submission-Readiness Checklist (run on the author's manuscript)

A venue-parameterized **go/no-go** the agent runs on the *user's* draft before submission.
It is the outward-facing analogue of the repo's internal `tools/quality_scorecard.py`:
where that scores packs, this scores a manuscript against a target venue's bar.

> **Mechanical/structural, not a verdict on quality.** This catches the avoidable desk
> rejects — out-of-scope, over the page limit, anonymization broken, no data/code plan,
> magnitude buried, identification undefended. The *substantive* "would referees buy it?"
> question is [`simulated-referee.md`](simulated-referee.md). Run this first; it is cheap.

## How to run

1. **Name the venue** (or get it from `journal-match`). Load the pack's skills and
   `resources/official-source-map.md`.
2. **Inspect the actual manuscript** — read the intro, the design section, the main
   exhibits, and the front matter. Do not score a paper you have not read; cite the
   section/table/page for every FLAG/FAIL.
3. **Score each dimension** PASS / FLAG / FAIL against the criteria below, pulling the
   venue-specific bar from the named skill and the mechanics from the source-map.
4. **Emit the scorecard** (format at the end): per-dimension status, an overall go/no-go,
   the ranked **blocking** gaps (FAILs), and the estimated desk-reject risk.

## Dimensions

| # | Dimension | PASS criterion | Authority (where the bar lives) |
|---|---|---|---|
| 1 | **Fit & general interest** | The question is in the venue's scope and pitched to its readership; the contribution type (new fact / mechanism / method / theory) is one the venue rewards | pack `*-topic-selection` / `*-contribution-framing` |
| 2 | **Contribution clarity** | The marginal contribution vs. the closest papers is stated in one sentence in the intro; canon attributed to the correct venues | pack `*-literature-positioning` |
| 3 | **Identification / method** | The source of variation is named in one sentence; the key assumption is defended and (where possible) tested; modern estimators used where required | pack `*-identification` / `*-methods` + [`reviewer-objection-checklist`](../empirical-methods/reviewer-objection-checklist.md) |
| 4 | **Robustness & inference** | The decisive checks are in the body; SE/clustering correct; multiple-testing addressed if many specs were mined; the search is disclosed | pack `*-robustness` / `*-data-analysis` + [`reporting-standards`](../empirical-methods/reporting-standards.md) |
| 5 | **Exhibits self-contained** | Each table/figure readable without the text; estimator + clustering in the note; **economic magnitude** in interpretable units, not just stars | pack `*-tables-figures` |
| 6 | **Exposition** | Question, answer, magnitude, and why-credible land in the first ~3 pages; no method-first opening; no buried headline | pack `*-writing-style` |
| 7 | **Venue mechanics** | Within page/word limit; spacing/font/anonymization correct; cover letter per policy; fee/APC known and budgeted | pack `resources/official-source-map.md` + `*-submission` |
| 8 | **Data & code / reproducibility** | The venue's data-and-code policy is satisfiable (master script, environment, README, disclosure plan for restricted data); replication package assembled | source-map data policy + the empirical-methods `code/` skeleton |
| 9 | **Pre-empted referee objections** | The 2–3 objections a referee will raise first each have a one-paragraph + one-exhibit answer ready | pack `*-referee-strategy` + the objection checklist |

## Scoring

- **PASS** — meets the bar; nothing to do.
- **FLAG** — meets the minimum but a referee will push; fixable, not blocking.
- **FAIL** — blocking; submitting as-is risks a desk reject or an easy referee kill.

**Go/no-go:** any FAIL on dimensions 1, 3, or 7 is a **no-go** (scope, identification, and
hard mechanics are the classic desk-reject triggers). FAILs elsewhere are fix-before-submit.

## Output format

```
【Venue】… (bar: pack skills + source-map, read live)
【Scorecard】
  1 Fit ............... PASS/FLAG/FAIL — note (§/table cited)
  2 Contribution ..... …
  … (dims 3–9)
【Go / No-go】GO / NO-GO — the deciding dimension(s)
【Blocking gaps (FAIL)】ranked; each with the fix + the pack skill that owns it
【Will-be-pushed (FLAG)】the referee-anticipation list
【Desk-reject risk】low / medium / high — why
```

## Hard rules

1. **Read the manuscript; cite locations.** No status without a §/table/page reference.
2. **Venue facts live; never from memory.** Page limits, fees, anonymization, and data
   policy come from the source-map at run time.
3. **No false green.** If you cannot verify a dimension (e.g. the draft wasn't provided),
   mark it `UNKNOWN`, not PASS.
4. **Map every FAIL/FLAG to the owning skill** so the author knows exactly where to go
   next (and can use that skill's execution bridge to actually fix it).
