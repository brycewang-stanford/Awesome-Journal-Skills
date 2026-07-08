# SOSP Systems-Artifact Code Adapter

This directory routes SOSP authors to the repo-level ML-conference methods kit and
documents where an operating-systems artifact outgrows it. The shared kit assumes an
accuracy-centric ML paper whose environment is a Python lockfile; a SOSP artifact is
frequently the environment itself — a patched kernel, a modified scheduler, an
interposed I/O path — evaluated after acceptance by the sysartifacts committee
rather than during review.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/sosp-artifact
```

Treat the checker as a structural smoke test only — it validates package hygiene,
not whether a claim reproduces on someone else's silicon.

## SOSP-specific overlays

- **Pin below userspace.** Record kernel base commit plus the full patch stack,
  microcode, firmware, boot cmdline (mitigations, isolcpus, hugepages), and NIC
  details for every run — baseline runs included. The capture script in
  [`../../skills/sosp-reproducibility/SKILL.md`](../../skills/sosp-reproducibility/SKILL.md)
  generates these files mechanically.
- **Tier the claims for sysartifacts.** Split experiments into anyone-can-run
  (container/VM, minutes), provided-hardware (testbed profiles, reservations), and
  documented-only (proprietary traces, unobtainable gear), following
  [`../../skills/sosp-artifact-evaluation/SKILL.md`](../../skills/sosp-artifact-evaluation/SKILL.md).
  Badge targets attach to tiers, not to the repo as a whole.
- **Write the claims map first.** Evaluators reproduce claims, not scripts: for each
  paper figure, state the expected trend and numeric tolerance ("within 10% of
  Fig. 7's shape; absolutes vary with hardware").
- **Remember the clock.** SOSP artifact evaluation begins days after the July
  notification and runs opposite the shepherded camera-ready — packaging done
  pre-submission is packaging you will not owe in August.

Venue policy always comes from [`../official-source-map.md`](../official-source-map.md)
and the live sysartifacts call, never from this adapter.
