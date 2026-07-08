# NDSS Artifact & Reproducibility Code Adapter

Thin pointer from the NDSS pack to the repository-wide conference tooling. Policy stays in
the skills and in [`../official-source-map.md`](../official-source-map.md); reusable scripts
stay in the shared kit so packs never fork their own copies.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Running the smoke check on an NDSS artifact

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/ndss-artifact
```

The script audits package hygiene (structure, docs, runnability signals). It knows nothing
about security-venue policy, so treat a pass as necessary, never sufficient.

## What you must still check by hand for NDSS

- **Network traces carry identities.** Any pcap, flow log, zone snapshot, or crawl output in
  the artifact must be scrubbed or synthesized; IPs, domains, and hostnames de-anonymize
  both subjects and authors (`../../skills/ndss-reproducibility/SKILL.md`).
- **The live Internet is not a fixture.** Record the observation window, vantage points, and
  target-population snapshot, because nobody can re-run your measurement against July 2026
  (`../../skills/ndss-experiments/SKILL.md`).
- **Exploit material needs a gate.** Working attack code against unpatched systems should
  ship with access conditions and a disclosure-status note consistent with your Ethics
  Considerations section (`../../skills/ndss-artifact-evaluation/SKILL.md`).
- **Badge targeting is a choice.** NDSS artifact evaluation (run on the secartifacts
  platform; opt-in after conditional acceptance) grants Available, Functional, and
  Reproduced badges — decide which you are engineering for before packaging
  (`../../skills/ndss-artifact-evaluation/SKILL.md`).
- **Hardware-bound results need a fallback.** If the headline experiment needs testbed
  switches, SDRs, or IoT devices, provide recorded traces plus replay scripts so evaluators
  can exercise the pipeline without your lab.

This adapter is unrelated to the econometrics/Stata kits used by the journal packs in this
repository; nothing here should import them.
