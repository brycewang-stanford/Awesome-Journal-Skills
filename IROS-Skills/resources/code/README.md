# IROS Robotics Reproducibility Code Adapter

This directory points IROS authors to the repo-level ML-conference methods kit as a starting
scaffold. It is not an econometrics kit and it is not an ML-benchmark kit; it is a lightweight
artifact/reproducibility scaffold that must be **extended with robotics-specific checks**, because a
passing software smoke test says nothing about whether a robot behaved.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/repro-package
```

Run this only as a smoke check on the code/config layer. It cannot verify the five things IROS
reviewers actually weigh.

## Five robotics-specific checks the shared script cannot make

1. **Hardware ledger.** Robot platform, sensors (make/model/firmware), actuators, onboard compute, and
   power budget — the embodiment the result depends on. A repo that runs proves nothing about the robot.
2. **Trial protocol.** Number of trials, the success criterion stated before running, the reset
   procedure between trials, and randomization of start conditions.
3. **Failure record.** A failure taxonomy with counts, not just the success rate; unreported failures
   and hidden resets are the classic IROS reliability inflation.
4. **Sim-to-real accounting.** Which numbers are simulation, which are real, and the measured gap — never
   an implied zero.
5. **Log capture.** Rosbag or equivalent time-stamped logs for representative runs, so a claim about a
   trajectory or contact force is auditable rather than asserted.

Venue-specific policy still comes from [`../official-source-map.md`](../official-source-map.md), the
current official CFP, and the IROS skills for experiments, reproducibility, supplementary material
(the video), and submission.
