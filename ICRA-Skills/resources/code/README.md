# ICRA Robotics Reproducibility Code Adapter

This directory adapts the repo-level ML-conference methods kit for ICRA robotics
papers. It is not an econometrics kit and not a substitute for venue policy — it is
scaffolding for the artifact and evidence work described in
[`../../skills/icra-reproducibility/SKILL.md`](../../skills/icra-reproducibility/SKILL.md)
and [`../../skills/icra-artifact-evaluation/SKILL.md`](../../skills/icra-artifact-evaluation/SKILL.md).

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/review-artifact
```

## Robotics deltas the generic kit cannot check

The shared checker validates package hygiene (structure, seeds, environment
pinning). An ICRA artifact needs five additional checks the generic tooling knows
nothing about — do these by hand:

1. **Two-tier claim split** — the artifact must distinguish rerunnable results
   (simulation, training, log-replay analysis) from hardware-audit results
   (rosbags + protocol only); a `CLAIMS.md` mapping claims to commands or logs is
   the deliverable.
2. **Hardware specification ledger** — robot model/firmware, end effector,
   sensors, control rates, calibration residuals; the checker cannot know a
   missing firmware version invalidates a torque-residual result.
3. **Video-attachment compliance** — duration/size/container against the current
   cycle's specs, speed-change labels, and trial-ID correspondence between clips
   and released logs (see `icra-supplementary`).
4. **Anonymity of robotics media** — under the double-anonymous rule introduced
   in the 2026 cycle: lab-identifying scenery in frames, voice tracks, container
   metadata, and org-named URLs; script what you can:

```bash
ffprobe -v quiet -show_format video.mp4 | grep -i -E 'artist|author|comment'  # metadata leak check
pdfinfo paper.pdf | grep -i -E 'author|creator'                               # PDF metadata
grep -rn -i -E 'university|lab_name|github.com/<org>' review-artifact/ --include='*.md'
```

5. **ROS environment capture** — `rosdep`/lockfile or container recipe pinning the
   distro and key package versions; "ROS 2 Humble" alone is not a pinned
   environment.

Venue policy always comes from [`../official-source-map.md`](../official-source-map.md)
and the live year-site, never from this directory.
