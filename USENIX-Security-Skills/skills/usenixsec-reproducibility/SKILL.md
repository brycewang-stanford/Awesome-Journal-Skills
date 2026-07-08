---
name: usenixsec-reproducibility
description: Use when strengthening reproducibility for a USENIX Security Symposium paper — writing the mandatory Open Science appendix, deciding what can and cannot be shared (exploit code, vulnerable-device data, human-subjects material), and making measurement, attack, and defense results independently regenerable.
---

# USENIX Security Reproducibility

Since the '26 cycle, USENIX Security has made openness a structural requirement:
every submission carries an **Open Science appendix** stating where the artifacts
behind the paper live, and acceptance is later conditioned on that availability
verifying (Phase-1 AE). This skill covers the appendix itself and the underlying
engineering that makes the statement true. Policy text is per-cycle — reread the
current CFP section before relying on wording.

## The Open Science appendix is a contract, not a caption

Reviewers read it during evaluation; the AEC enforces it after acceptance. It
should answer, concretely:

- **What exists**: code, datasets, configurations, analysis notebooks, hardware
  designs — enumerated, not gestured at.
- **Where**: resolvable locations (anonymized mirrors at submission; permanent,
  ideally DOI-backed archives in the final paper).
- **What is withheld and why**: the policy accepts justified omission, and security
  work legitimately generates a lot of it.

```latex
\section*{Open Science}
All scanner source code, the analysis pipeline, and the aggregated measurement
tables (Sections 4--6) are available at \url{<anonymized-archive>} and will be
deposited with a DOI upon publication. The raw scan captures contain
per-endpoint identifying data for still-unpatched hosts and are withheld;
Appendix~B documents the aggregation procedure so the tables can be
regenerated from an independent scan. The 214 disclosure emails are withheld
as human-subjects correspondence; templates are included.
```

## Withholding decisions that hold up

| Material | Default posture | Acceptable justification pattern |
|---|---|---|
| Attack/PoC code | Share, targeted at a bundled testbed | Weaponizable against unpatched population → share after patch window, state the date |
| Vulnerability details | Share post-disclosure | Coordinated disclosure incomplete → embargo with timeline in the Ethical Considerations appendix |
| Scan/measurement raw data | Share aggregated | Raw data identifies vulnerable hosts or users → aggregate + publish the aggregation code |
| User-study transcripts | Withhold; share instruments | IRB/consent scope → release codebooks, surveys, and quantitative summaries |
| Malware corpora | Hashes + provenance | Redistribution illegal or dangerous → document acquisition path others can follow |
| Vendor-provided datasets | As NDA allows | Contract limits → say so and provide synthetic or public-subset substitutes |

Two disciplines make these defensible: decide them **at experiment time** (retrofit
justifications read as excuses), and always ship the *procedure* even when the
*data* stays closed — an independent team with their own vantage point should be
able to re-derive your tables.

## Determinism engineering for security experiments

Security results are unusually time- and environment-coupled. Pin what you can and
timestamp what you cannot:

- **The internet moves.** Record scan dates, target-list snapshots, and blocklist
  versions; a reproduction in 2027 measures a different network than 2026 did.
- **Fuzzing and probabilistic attacks**: fix seeds where the harness allows, and
  report distributions over repeated campaigns (count, median, IQR) rather than a
  best run; state the compute budget per campaign.
- **ML-based pipelines** (classifiers, LLM-assisted analysis): pin model versions
  and weights; a hosted-API dependency is a reproducibility hole — snapshot outputs
  and say so.
- **Version-sensitive exploits**: record exact kernel/firmware/browser builds, and
  keep the vulnerable version archived in the artifact since upstream will patch.

```bash
# Capture the environment fingerprint alongside every experiment run
{ date -u +%FT%TZ; uname -srmo; git rev-parse HEAD;
  sha256sum targets.txt config.yaml; pip freeze | sort; } > runs/$(date +%s).env
```

## Paper-side reporting that reviewers check

- Every headline number traces to a script in the artifact; the claims table in
  the artifact README (see `usenixsec-artifact-evaluation`) is the index.
- Ranges and repetition counts for stochastic results; single-run numbers flagged
  as such.
- Dataset construction fully specified: collection window, filters, dedup rules,
  ground-truth labeling procedure and inter-rater agreement where humans labeled.
- Negative-result honesty: configurations where the attack fails or the defense
  costs too much belong in the paper, and reviewers at this venue notice absence.

## Reverify each cycle

- Exact Open Science appendix requirements and page allowance in the current CFP.
- Whether availability verification remains acceptance-conditional ('27 待核实).
- Current AEC guidance on acceptable archives and anonymized hosting.

## Output format

```text
[Inventory] artifacts enumerated: code / data / configs / instruments
[Open items] each withheld artifact + justification + procedure substitute
[Determinism] seeds, environment fingerprints, time-coupling documented
[Trace] headline claims ↔ regeneration scripts: n/m covered
[Appendix draft] Open Science text ready: yes / gaps listed
```
