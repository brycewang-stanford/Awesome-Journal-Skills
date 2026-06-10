---
name: geb-replication-and-data-policy
description: Use when planning data and code sharing for a Games and Economic Behavior (GEB) manuscript. GEB encourages but does NOT mandate a replication archive — unlike AER/Econometrica/JAE — so this skill helps you share well voluntarily and avoid assuming requirements that do not exist here.
---

# Replication & Data Policy (geb-replication-and-data-policy)

## When to trigger

- You have experimental data, simulation code, or solver inputs and are unsure what GEB requires
- You assumed GEB has a mandatory data archive (it does not) and are budgeting effort accordingly
- You want to make a theory paper's numerical examples reproducible
- An accepted-stage checklist is being assembled

## The GEB data policy — encouraged, not required

This is a **meaningful distinction** for a journal that publishes experimental work: GEB does **not** operate a mandatory data/code replication archive comparable to the AEA journals (AEJ/AER), Econometrica, or the JAE Data Archive. GEB follows Elsevier's **"encourages and enables"** research-data stance (Option C): authors are *invited* to deposit data and code in a repository (e.g., **Mendeley Data**, free and open access), to include a **data-availability statement**, or to publish a **Data Brief** — but deposit is **not a condition of publication**. Do not assume a required openICPSR-style archive; verify the current wording on the Guide for Authors (some details here are 待核实 — drawn from secondary sources).

Even though it is optional, sharing well is good practice and pre-empts referee doubts about your experiment or computation.

## What to prepare (voluntarily, but recommended)

### For experimental papers
- **Raw and cleaned data** plus the analysis scripts that produce every table and figure.
- **Experiment code** (oTree / z-Tree) and the **instructions** shown to subjects.
- A **README** describing variables, sessions, treatments, and how to run the pipeline.
- An **IRB / ethics** note where applicable.

### For theory papers with computation
- The **scripts and solver inputs** (e.g., Gambit files, `nashpy`/Python notebooks) that generate every numerical example, figure, and counterexample.
- **Pinned versions** and **reported seeds** so examples regenerate deterministically.
- A short README mapping each script to the corresponding result in the paper.

### Statement and deposit
- Add a **data-availability statement** even when depositing voluntarily.
- Deposit on a stable repository (Mendeley Data, Zenodo, or OSF) and cite it.
- Disclose any **generative-AI** use in the dedicated declaration section (separate from data policy, but part of the same transparency package).

## Anti-patterns

- Assuming GEB will block publication without a deposited archive (it will not)
- ...but also shipping an experiment with no reproducible analysis path
- Numerical examples with no seeds or pinned versions, so referees cannot regenerate them
- A data file with no README or variable documentation
- Confusing GEB's optional policy with the mandatory archives of AER/Econometrica/JAE


## Reproducibility pass for Games and Economic Behavior

Use this as a second-pass capability check. First lock the primitives, equilibrium concept, comparative statics, and proof or experiment boundary; then test whether the manuscript addresses game theorists who ask what the model teaches beyond a clever example.

- **Primary move:** Name data, code, environment, disclosure limits, and archive/deposit route; unresolved proprietary or ethics barriers must be explicit.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JET for theory abstraction, Theoretical Economics for compact theory contribution, Experimental Economics for experiment-first designs; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Paper type】experimental / computational-theory / pure-theory
【GEB requirement】sharing encouraged, NOT mandatory (verify wording)
【Prepared】data + code + README + (exp) instructions/IRB? [Y/N each]
【Reproducible computation】seeds + pinned versions + run_all? [Y/N / NA]
【Deposit plan】Mendeley Data / Zenodo / OSF + availability statement? [Y/N]
【Next step】geb-review-process or geb-submission
```
