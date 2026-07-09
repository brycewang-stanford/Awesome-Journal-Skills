---
name: edbt-author-response
description: Use when drafting EDBT author responses across the two turns of a cycle — the short author-feedback reply on the initial reviews, and the in-cycle revise-and-resubmit change letter that maps every reviewer request to a concrete revision re-read by the original reviewers under the OpenProceedings process.
---

# EDBT Author Response

Use this after EDBT reviews are released. An EDBT cycle has **two distinct speaking turns**, and
conflating them is a common mistake: a short **author-feedback** reply on the initial reviews, and —
if you receive a **revise** — a full **change letter** accompanying a revised paper that the
original reviewers re-read **within the same cycle**. The revision, not the letter, carries the
argument.

## Triage (both turns)

- Answer what affects the decision: significance of the data-management contribution, technical
  soundness, evaluation fairness (real workloads, tuned baselines, realistic scale),
  reproducibility, and clarity.
- Use evidence that already exists or that the revision will concretely add — never a vague promise.
- Correct factual misreadings first; a reviewer who misread a figure or a configuration is often
  persuadable.
- If the cycle is double-blind (**待核实** per cycle), keep every word anonymous — no tool/repository
  names or affiliations that reveal identity.

## Turn 1 — the author-feedback reply

Short and decision-focused. One decision-critical point per reviewer beats an exhaustive reply.
Concede what is true, correct what is misread, and point to exactly where the answer lives in the
submitted paper or artifact. Do not paste large new result tables the reviewers cannot yet verify;
signal what the revision will add if a *revise* follows.

## Turn 2 — the revise-and-resubmit change letter (the distinctive EDBT move)

A *revise* is a genuine in-cycle re-read. The letter is a **change ledger**: for every reviewer
request, either make the change and show it, or decline it with a reason.

```text
[R1.1] Reviewer request (quoted briefly)
       -> Action: DONE  | added the tuned <baseline> at 8-128 workers, §5.2, Table 3
       -> Where: §5.2, Table 3; artifact/exp/rq2/
[R1.2] Reviewer request
       -> Action: DECLINED (with reason) | the requested workload is not publicly redistributable;
          added a comparable public workload and stated the limit in §5.4
[R2.1] Reviewer request
       -> Action: PARTIAL | extended the scaling study to 128 workers; the 1024-worker run is
          beyond the cluster we can access this cycle and is noted as future work
```

The rule that turns a revise into an acceptance: **no silent omissions.** A request that is neither
done nor explicitly declined is what the second read punishes. Because the same reviewers re-read the
paper, the letter should let them find each change in seconds — quote the request, name the action,
point to the section, table, and artifact path.

## Reviewer pushback patterns (database-systems flavor)

| Pushback | What it signals | EDBT-ready response |
|---|---|---|
| "The baseline is not tuned / not the strongest" | Soundness doubt about the comparison | Re-run with an equal, documented configuration; report the new numbers, or justify the choice |
| "This scale is unrealistic / too small" | External-validity limit | Extend to realistic workloads and cluster sizes, or scope the claim and name the limit |
| "I cannot tell how the mechanism works" | Reproducibility / clarity gap | Add the missing algorithm/parameter detail; make it reimplementable |
| "The artifact does not run / is missing" | Reproducibility gap | Fix and re-upload the package; describe the run path in the letter |
| "Overlaps prior work X" | Novelty/delta doubt | Sharpen the delta sentence; add the missing comparison |
| "The measurement methodology is unsound" (E&A) | Core-contribution doubt | For an Experiments & Analysis paper this is decision-critical — fix the methodology, not just the prose |

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- Length and format norms for both turns vary by cycle; confirm the current CMT instructions before
  sending.
- Fit the revision to the **in-cycle window** — the revised paper is scored *within* the cycle, so
  scope the changes to what can genuinely be finished and verified in time.
- The PC discussion decides; write the letter as evidence for an advocate, and make the revised
  paper — not the letter — carry the argument.

## Output format

```text
[Turn] author-feedback reply / revise-and-resubmit change letter
[Priority issue] <reviewer concern>
[Decision dimension] significance / soundness / evaluation / reproducibility / clarity
[Change ledger] <request -> DONE/PARTIAL/DECLINED + where in paper/artifact>
[In-cycle feasibility] <can the revision be completed and verified before the revised-paper deadline?>
```
