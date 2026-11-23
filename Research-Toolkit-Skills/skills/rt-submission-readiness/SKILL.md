---
name: rt-submission-readiness
description: Use when an author is one revision away from submitting to a named journal or conference and wants the full pre-submission polish on the actual manuscript (.tex/.md/.docx/.pdf) — a deterministic preflight against the venue's verified rules (limits, anonymization, required statements, citations, exhibits, numbers, placeholders), the nine-dimension readiness scorecard, the venue-calibrated referee panel, a claim-to-evidence polish, the cover letter and statements the venue requires, and a re-run that shows what changed.
---

# Submission Readiness — the pre-submission pipeline (rt-submission-readiness)

The single entry point for polishing a paper before submission. It runs a fixed pipeline on
the author's real file and hands each stage's evidence to the next. Full documentation:
[`shared-resources/submission-readiness/README.md`](../../resources/shared/submission-readiness/README.md).

## When to trigger

- "We're submitting to <venue> next week — check it." / "Is this ready for <venue>?"
- Before paying a submission fee or opening the portal.
- After a revision, to confirm earlier problems are resolved and nothing new broke.
- If the venue is not chosen yet, run `rt-journal-match` first; if the empirical results
  are not final, run `rt-execution-bridge` first.

## Inputs to load

1. **The manuscript file** (ask for the path; prefer the PDF for exact page counts, the
   .tex/.docx source for everything else — running both is best).
2. **The target venue's pack**: its `README.md`, `*-submission`, `*-writing-style`,
   `*-referee-strategy` (or review-process) skills, and `resources/official-source-map.md`.
   If the pack is not installed, its rules are still in the preflight's compiled
   `venue-rules.json`; read the pack on GitHub for the qualitative bar.
3. Any execution artefacts (result handles, robustness output) from `rt-execution-bridge`.

## Locating the preflight

Run whichever path exists:

- **Installed plugin**: `python3 <this skill's base directory>/../../resources/preflight/preflight.py`
  (the base directory is shown when this skill loads).
- **Repository clone**: `python3 tools/preflight.py` from the repo root.

`--list-venues` shows the venues with machine-readable rules and their verification
dates. For a venue without rules, pass `--blind` if it is double-blind (anonymization
checks still run) or `--rules-block my-venue.json` with rules the author has read from
the venue's page. Python 3.9+, no packages; PDFs need `pdftotext` (poppler).

## The pipeline

| Stage | Do this | Output |
|---|---|---|
| **0 · Preflight** | `preflight.py <file> --venue "<venue>" --json > preflight.json` (add `--online` to check the references exist on Crossref) | Verdict GO / CONDITIONAL GO / NO-GO; every finding with location and owning skill; a *not checked* list |
| **1 · Scorecard** | Score the nine dimensions in [`readiness-checklist.md`](../../resources/shared/submission-readiness/readiness-checklist.md) on the manuscript, using `preflight.json` as dimension 7's evidence | PASS / FLAG / FAIL / UNKNOWN per dimension, citing §/table |
| **2 · Referee panel** | Run `rt-simulated-referee` on the venue family's review form ([`review-forms.md`](../../resources/shared/submission-readiness/review-forms.md)) | Verified major concerns, decision band, skill-mapped fixes |
| **3 · Polish** | Claim-to-evidence audit + first-page test + title/abstract house style ([`prose-polish.md`](../../resources/shared/submission-readiness/prose-polish.md)) | Ranked edit list, before → after, never changing numbers or scope silently |
| **4 · Letter & statements** | Per venue policy ([`cover-letter-and-disclosures.md`](../../resources/shared/submission-readiness/cover-letter-and-disclosures.md)) | Cover letter only if wanted; every required statement drafted from author-supplied facts |
| **5 · Re-run** | After the author revises: preflight + scorecard again on the new file | Resolved / still open / newly introduced |

Stop early when it pays: a preflight NO-GO on a hard rule (over the page limit, broken
anonymity) is fixed before spending a referee panel on the paper. Scope down when asked:
"just the mechanics" is stage 0 + dimension 7; "would referees buy it" is stage 2.

## Decision contract

| Result | Meaning | Required next action |
|---|---|---|
| `GO` | No FAIL in preflight or scorecard, venue mechanics verified, panel band at least major revision with no unaddressed decisive issue. | Submit; keep the panel's FLAG list for the response letter. |
| `CONDITIONAL GO` | No desk-reject trigger, but FLAGs or verified minor concerns remain. | Fix or explicitly justify each; rerun stage 5 on the changed sections. |
| `NO-GO` | Any preflight FAIL, any scorecard FAIL on fit / identification / mechanics, an unverifiable required venue rule, or a panel desk-reject. | Route each blocking item to its owning skill; rerun before opening the portal. |

`UNKNOWN` is never upgraded to PASS: name the missing evidence (e.g. "exact page count —
compile the PDF and rerun") and the smallest artefact that resolves it.

## Worked run (abridged)

```text
$ python3 tools/preflight.py draft.tex --venue icml
【Mechanical verdict】NO-GO  (4 FAIL · 2 FLAG)
FAIL  ANON-AUTHOR   [front matter] Author block is not anonymized: 'J. Roe, Example University …'
FAIL  STMT-MISSING  Impact / broader-impact statement is required by the venue but was not found
FAIL  ANON-URL      [line 212] Non-anonymous link https://github.com/jroe/gsa presented as the authors' own code
FAIL  LEFTOVER-MARKER [line 388] Placeholder left in the text: '… (TODO: add ImageNet-scale experiment) …'
FLAG  NUM-MISMATCH  [line 41] '84.6' in the abstract does not appear in any table …
【NOT checked】exact page count (source format; estimated ~8.4 pages) — compile to PDF and rerun
```

The scorecard then marks dimension 7 FAIL from these four findings, and the panel (form A)
returns: decisive issue R1 "hyperparameters selected on the test split (§5.1)", owner
`icml-experiments`. Verdict NO-GO; after fixes, stage 5 shows 4 FAIL → 0, the
NUM-MISMATCH resolved, and R1 answered with a validation-only re-run.

## Hard rules

1. **Run the program before reading for mechanics.** Counts, anonymity, references,
   numbering and number traceability come from preflight, not from eyeballing.
2. **Read the manuscript; cite locations** for every judgement-based status.
3. **Venue facts from the compiled rules and source map**, never from memory; quote the
   rules' verification date to the author.
4. **No false green** — preflight's *not checked* items and anything unverifiable stay
   `UNKNOWN`.
5. **Map every FAIL/FLAG to its owning skill** (and execution bridge where empirical).
6. **A pre-check, not a verdict** — never say the paper will be accepted.

## Output format

```text
【Venue】… (rules verified YYYY-MM-DD; pack …)
【Stage 0 · Preflight】NO-GO / CONDITIONAL GO / GO — n FAIL · n FLAG; not checked: …
【Stage 1 · Scorecard】1 Fit … · 2 Contribution … · … · 9 Objections … (each PASS/FLAG/FAIL/UNKNOWN, § cited)
【Stage 2 · Panel】band …; decisive issues R1–R3 with owners
【Stage 3 · Polish】claims audited n; unsupported k; top edits …
【Stage 4 · Letter & statements】cover letter: required/optional/discouraged → drafted/skipped; statements drafted: …
【Overall】GO / CONDITIONAL GO / NO-GO — deciding items
【Fix order】1 … 2 … 3 … (blocking first; each with owner skill)
【Re-run】after fixes: python3 … preflight.py <revised file> --venue …
```

Next: `rt-simulated-referee` (stage 2 detail), `rt-desk-reject-risk` (desk-screen focus),
`rt-response-to-referees` after a real decision.
