# ICDE Artifact Code Adapter

ICDE weighs the **availability** of your supplemental material when scoring the paper, so the
artifact you attach in Microsoft CMT is graded evidence, not an afterthought. This directory does
not ship a database benchmark of its own; it forwards you to the collection's shared
reproducibility scaffold and then tells you how to read that scaffold through data-systems eyes.

## The one command

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/icde-supplement
```

That is a **smoke check** — it confirms your package has a README, an entry script, and a legible
layout. It knows nothing about ICDE policy, single-blind rules, or whether your baselines were
fair. Treat a clean exit as "the box opens," not "the artifact is good."

## Where the shared kit lives

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Reading the kit as a data-engineer

The scaffold speaks ML-conference language; translate it before you rely on it. Its "experiment
matrix" is your **workloads × baselines × scale-factor grid**. Its "seeds" cover your **data
generators and workload shuffles**, not just any learned component. Its README-and-entry-script
expectations line up with the `run_all.sh` / `run_small.sh` and claims-map pattern taught in
[`../../skills/icde-artifact-evaluation/SKILL.md`](../../skills/icde-artifact-evaluation/SKILL.md).

## The two things the script cannot see

1. **Single-blind means you keep your name.** ICDE supplements are not anonymized — leave author
   identity and commit history in place. Do not spend effort scrubbing a repository the process
   expects to be attributed; see
   [`../../skills/icde-submission/SKILL.md`](../../skills/icde-submission/SKILL.md).
2. **Runs is not the same as fair.** The checker cannot tell whether competitors were tuned,
   whether the storage device was disclosed, or whether each figure traces to a logged run. That
   judgment lives in [`../../skills/icde-reproducibility/SKILL.md`](../../skills/icde-reproducibility/SKILL.md).

When tooling and policy disagree, policy wins: the binding rules are in
[`../official-source-map.md`](../official-source-map.md) and the live ICDE call, not in any exit
code.
