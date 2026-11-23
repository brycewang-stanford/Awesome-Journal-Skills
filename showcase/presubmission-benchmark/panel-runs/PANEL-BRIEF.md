# Referee-panel benchmark run — agent brief

You are acting as the pre-submission pipeline of the Awesome-Journal-Skills repository
(<repo>), stage 2: the simulated referee panel. You will review
TWO independent manuscripts, each targeted at a named venue. Treat each as a real author's draft.

Rules for this run:
- Do NOT open anything under `tools/tests/` or any file named `defects.json`, `KEY.json`, or
  anything in a directory named `bench-key` — that would invalidate the run. Do not use git log/diff.
- Do not edit any repository file. Write outputs only to the paths given below.

For EACH manuscript:
1. Read the protocol: `shared-resources/submission-readiness/simulated-referee.md` and the venue
   family's form in `shared-resources/submission-readiness/review-forms.md`; read the target pack's
   `resources/official-source-map.md` and its referee-strategy / review-process / identification /
   methods / submission skills (pack directory given below) to calibrate the bar.
2. Read the manuscript IN FULL, and its stage-0 preflight report (`<manuscript>.preflight.json`) so
   you do not spend the report on mechanics.
3. Run the panel INLINE (you play each role in turn; write each referee's report before reading the
   next lens's concerns): AE desk-screen → 3 referees with the family's three lenses, each filling the
   family's form + major/minor concerns with §/table/line evidence and owning skill → a verification
   pass where you try to refute every major concern against the text (kept / downgraded / dropped,
   with the quoted line) → AE synthesis (decision band in the family vocabulary, 1–3 decisive issues).
4. Calibrate honestly: a strong paper can come back with no major concerns. Do not invent problems
   to look rigorous, and do not soften real ones.

Write the full panel output for each manuscript to `<manuscript path>.panel.md`, using the output
format in `Research-Toolkit-Skills/skills/rt-simulated-referee/SKILL.md`, and end the file with a
machine-readable block:

```json
{"decision_band": "...", "kept_major_concerns": [{"id": "R1-M1", "lens": "...", "location": "...", "concern": "one sentence"}], "downgraded": [...], "dropped": [...]}
```

Report back: for each manuscript, the decision band and the one-line list of kept major concerns.
