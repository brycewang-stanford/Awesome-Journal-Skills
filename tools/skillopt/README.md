# SkillOpt-adapted behavioral optimizer for journal skills

A small, repo-local adaptation of **Microsoft SkillOpt**
(<https://github.com/microsoft/SkillOpt>) for the journal skill packs in this
repository.

SkillOpt treats a skill's markdown as the *trainable state* of a frozen agent and
improves it through a disciplined loop:

```text
rollout  →  reflect  →  bounded edit (add / delete / replace)  →  VALIDATION GATE  →  keep or reject
```

The defining rule is the **validation gate**: a candidate edit is accepted *only
when it strictly improves a held-out validation score*. This is what separates
SkillOpt from "ask a strong model to rewrite the skill" — the rewrite has to
*earn* its way in by measurably making an agent answer real tasks better.

## Why this complements `tools/quality_scorecard.py`

The repo already has a strong **static** scorecard. It measures the *shape* of a
skill — substance units, trigger phrasing, presence of resources, structure — and
rates most packs ~92–94/100. That is necessary but **blind to behavior**: a skill
can score 94/100 and still (a) state a wrong fact, (b) omit the one number the
researcher needs, or (c) over-hedge a verified fact into uselessness. Static
scoring cannot catch any of those, because none of them change the skill's shape.

`skillopt` adds the missing axis: **does an agent actually answer a real
researcher's question better when armed with this skill?** It is *behavioral* and
*ground-truth-anchored*, where the scorecard is structural.

| | `quality_scorecard.py` | `tools/skillopt` |
|---|---|---|
| Measures | shape of the skill | behavior of an agent using the skill |
| Signal | substance / trigger / resources / structure | held-out answer quality vs. verified ground truth |
| Catches | thin bodies, weak triggers, missing assets | wrong facts, missing numbers, mis-calibrated hedging |
| Gate | report-only | **accept edit iff held-out score strictly improves** |

Use both. The scorecard keeps shape healthy; SkillOpt keeps *answers* correct.

### Relationship to `tools/skillopt_gate.py`

A sibling tool, `tools/skillopt_gate.py`, is a **deterministic proxy gate**: it
snapshots the repo's audit signals (counts, hard checks, score floors, warning and
clone counts) and rejects any edit that regresses them — cheap enough to run on
*every* edit to *every* pack. This `tools/skillopt` harness is its **behavioral
counterpart**: the model-rollout validation the proxy gate stands in for when a
rollout is too expensive to run everywhere. They compose — run the deterministic
gate on all edits as a safety net, and this behavioral gate on the
fact-sensitive skills where *answer correctness* (not just repo shape) is what
moves.

## The loop, concretely

For a target skill `S` with a held-out validation set `V` (realistic researcher
queries the skill text never sees):

1. **Rollout (baseline).** A *rollout* subagent is given **only** `S` + a query
   from `V` and produces an answer. It is blind to the ground truth.
2. **Judge.** A *judge* subagent scores the answer 0–100 against
   [`rubric.md`](rubric.md) using the query's **ground-truth fact sheet**. The
   judge is blind to which skill version produced the answer.
3. **Reflect → bounded edit.** The optimizer proposes a small add/delete/replace
   grounded **only in verified facts** (the pack's `official-source-map.md` +
   primary sources). No invented facts ever enter a skill.
4. **Rollout (candidate).** Re-run step 1 with the edited skill `S'`.
5. **Validation gate.** Accept `S'` only if its judge score on the held-out set
   **strictly exceeds** `S`'s. Otherwise the edit goes to the **rejected-edit
   buffer** (recorded, not applied) and `S` is kept.

The subagents are spawned with the `Agent` tool; the orchestrator records every
rollout, score, and gate decision in a per-skill ledger under `ledger/`.

## Files

```text
tools/skillopt/
├── README.md                      # this file — the method
├── rubric.md                      # the behavioral judge rubric (0–100)
├── report.py                      # summarize ledgers; --check enforces the gate invariant
├── validation/
│   └── hlr-submission.md          # held-out queries + verified ground-truth fact sheet
└── ledger/
    └── hlr-submission.json        # rollout scores, edits, accept/reject decisions
```

## Running the report

```bash
python3 tools/skillopt/report.py            # human-readable summary of every ledger
python3 tools/skillopt/report.py --json     # machine-readable
python3 tools/skillopt/report.py --check     # exit 1 if any APPLIED edit failed its gate
```

`--check` is an integrity guard: it fails if a ledger ever records an *applied*
edit whose post-edit score did not strictly beat the baseline. It encodes the one
rule SkillOpt cannot bend — **no edit ships unless it won its validation gate.**

## Scope & honesty notes

- **Ground truth only.** Every accepted edit traces to the pack's
  `official-source-map.md` (re-verified 2026-06-21) and/or a primary source.
  SkillOpt optimizes *wording and coverage*; it never licenses inventing facts.
- **Demo scope.** The first run optimizes `Harvard-Law-Review-Skills/hlr-submission`
  end-to-end (full rollout + gate). Verified factual corrections it surfaces
  (submission portal, word limits, anonymization, Bluebook edition) are then
  *transferred* to sibling HLR skills that shared the same errors — transfers are
  marked as such in the ledger, since they inherit an already-gated fact rather
  than running their own full loop.
- **The judge is an LLM.** Scores are estimates, not ground truth. The gate uses
  *strict improvement on the same rubric and queries* so that judge noise cancels
  in the before/after comparison rather than being treated as an absolute grade.
