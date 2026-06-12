---
name: ectheory-replication-and-data-policy
description: Use to handle reproducibility and the supplementary-material file for an Econometric Theory (ET) paper — ET has no mandatory data/code archive (theory journal); the relevant policy is the voluntary online Supplementary Material for already-reviewed proofs, derivations, and simulation evidence.
---

# Reproducibility & Supplementary Material (ectheory-replication-and-data-policy)

## When to trigger

- Long proofs/derivations exceed the 50-page Article ceiling and need a home
- You want your Monte Carlo results to be reproducible and your code clean
- Preparing the final-manuscript files and unsure what ET requires vs forbids in the Supplement
- Wondering whether ET has a formal data/code deposit requirement (it does not — see below)

## ET's reality: no mandatory archive, a Supplementary-Material policy

Unlike empirical economics journals, ET is **theory-focused and states no mandatory formal
data/code/replication archive** on its author-instructions pages (recorded as **ABSENT** as of
2026-06-01; **待核实**). Note: the JAE Data Archive belongs to a *different* journal (*Journal of
Applied Econometrics*) and **does not apply** to ET. What ET does operate is a **voluntary online
Supplementary Material policy**:

- Only **critical, already-reviewed** material may be posted online with the article — long
  mathematical derivations, supporting lemmas, and extra tables/figures.
- It is submitted with the **final manuscript** as a **separate, clearly labeled file**.
- It is **not copyedited or typeset**.
- It **may not introduce new, unseen material** — everything in it must have gone through review.

This is the standard ET route for the long technical proofs and simulation overflow that do not fit
in the main paper under the **50-page** ceiling.

## Building the Supplement well

- Make it a **self-contained** document (compiles independently) that shares the main paper's
  assumption numbering and notation, so cross-references resolve.
- Put here: complete proofs of auxiliary lemmas, lengthy derivations, additional Monte Carlo DGPs
  and tables, and robustness simulations — all already part of what referees saw.
- Do **not** smuggle new theorems, new claims, or unreviewed results into the Supplement.

## Reproducible computation (good practice, not a deposit mandate)

- Keep one runnable script per table/figure (or a master script) regenerating all simulation output.
- Fix and report random seeds; record replication counts, sample sizes, and the full DGP.
- Pin the computational environment (package/version notes) so results regenerate.
- A clean, reproducible numerical appendix builds referee trust even absent a formal archive.

## Checklist

- [ ] Confirmed ET has no mandatory data/code archive; not budgeting for a deposit step (待核实)
- [ ] Overflow proofs/derivations placed in a separate, clearly labeled Supplement file
- [ ] Supplement contains only already-reviewed material; no new results introduced
- [ ] Supplement is self-contained and shares main-paper notation/numbering
- [ ] Simulation code runnable; seeds, reps, and DGP reported
- [ ] Main Article respects the 50-page ceiling; overflow lives in the Supplement

## Anti-patterns

- Assuming an AEA/JAE-style mandatory archive applies to ET (it does not)
- Introducing a new theorem or claim only in the non-reviewed Supplement
- A Supplement that cannot be read without the main paper's lost context
- Non-reproducible simulations (unreported seeds / replication counts)
- Padding the main Article past 50 pages instead of using the Supplement

## What belongs where: a theory-venue routing table

With no mandatory data/code archive, the reproducibility decision is mostly *where each piece of technical
content lives*.

| Content | Main Article | Online Supplement | Forbidden |
| --- | --- | --- | --- |
| Main theorem + proof sketch | yes | — | — |
| Long proof of an auxiliary lemma | sketch only | full proof | — |
| Extra Monte Carlo DGPs / robustness tables | headline result | overflow tables | — |
| A brand-new theorem not yet refereed | — | — | yes (no new results) |

The hard rule: the Supplement carries only **already-reviewed** material and ships as a separate labeled
file with the final manuscript. Confirm conventions against the author guidelines (mandatory archive
recorded ABSENT as of 2026-06-01; 待核实).

## Worked vignette and the reproducibility fixes

A paper proves a uniform convergence rate. Its maximal-inequality proof (Lemma 2) and full size/coverage
grid exceed the page ceiling and move to a self-contained Supplement reusing the paper's numbering. Ship one
master script that regenerates every cell with the environment pinned:

```text
# reproducibility manifest accompanying the simulation Supplement
seed_master = 314159          # reported in table notes
reps        = 20000           # per design cell
n_grid      = [100,200,400,800]
p_grid      = [5,10,25,50]    # dimension growing with n
software    = R 4.4.x; packages: <list with versions>
mapping     = each table -> the script block that produces it
```

This builds referee trust, not a deposit mandate — there is no AEA/JAE-style archive obligation at ET. The
fixes: "the auxiliary proof is missing" → include it in the reviewed Supplement during the review round, not
for the first time post-review; "simulations not reproducible" → add the manifest above and a
table-to-script mapping; "Supplement unreadable on its own" → make it compile independently against the
numbered theorems.

## Output format

```
【Archive requirement】none mandatory at ET (待核实)
【Supplement】separate labeled file, already-reviewed only? [Y/N]
【Self-contained】shares notation/numbering? [Y/N]
【No new material】confirmed? [Y/N]
【Reproducibility】seeds + reps + DGP + env recorded? [Y/N]
【Next step】ectheory-review-process
```
