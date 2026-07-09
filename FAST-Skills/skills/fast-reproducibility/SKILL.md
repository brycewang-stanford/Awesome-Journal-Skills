---
name: fast-reproducibility
description: Use when strengthening USENIX FAST reproducibility and open-science evidence, covering device and firmware provenance, device-state disclosure, trace availability and replay, claim-to-evidence mapping, honest degrees of reproducibility on hardware that ages and varies, and consistency between what the paper says and what the artifact contains.
---

# FAST Reproducibility

Use this before submission and again before camera-ready. FAST's storage results live on **real
hardware that ages, throttles, and varies part-to-part**, so reproducibility here is a distinct
craft from software-only venues: a reader reproducing your work needs to know not just the code but
the *device, its firmware, and its state*. The goal is that a competent reader with comparable
hardware could rebuild your evidence and reach your conclusions.

## Evidence map

- Map each claim and reported number to a **verifiable location** — a paper section, a table
  generated from a logged run, or a script in the artifact.
- For a system, give enough of the design, parameters, mkfs/mount options, and build environment
  that a reader could rebuild and run it.
- For measurements, report the **device provenance** (models, firmware, interface), the **host**
  (CPU, RAM, kernel), and the **device state** (steady-state/aged, fill, TRIM) — the storage-only
  provenance that software artifacts omit.
- Keep the **availability statement** truthful and specific: what code and traces are shared, where
  they will live after acceptance, and — if something cannot be shared — exactly why.
- Keep the paper and the artifact **consistent**: a bytes-written or latency number in the PDF that
  no script in the artifact regenerates is the contradiction reviewers read as carelessness.

## Availability statement audit

| Claim in the paper | Weak answer | FAST-ready answer |
|---|---|---|
| "We evaluate on SSDs A, B, C" | "Standard SSDs" | Exact models, capacities, and **firmware versions** in a testbed table |
| "Driven by trace T" | Trace named, not shared | Archived trace (or documented access) + the replay script and its settings |
| "We reduce write amplification" | Estimated in prose | Device-counter (SMART/log) dumps + the script that computes WA from them |
| "Steady-state results" | Unstated preconditioning | The preconditioning/aging protocol as a runnable script |
| "Our system is available" | "Code on request" | Anonymized, buildable code with a README and a small runnable demo |

"Available on request" is treated as *not available*; convert every such line into a concrete,
anonymized artifact or an explicit, justified exception (e.g. drives under NDA, privacy-limited
production traces).

## Provenance pinning

```text
[Devices]   model, capacity, interface, FIRMWARE version; host CPU/RAM, kernel, mkfs/mount options
[State]     preconditioning/aging protocol, fill level, TRIM/discard; FOB vs. steady-state disclosed
[Traces]    archive the replayed trace or document access; ship the replay tool + timing settings
[Workloads] YCSB/filebench/fio job files with exact parameters and seeds
[Compute]   run duration and repeats; note thermal/throttling conditions that affect timing
[Counters]  how bytes-written / WA / GC were read from the device, so a reader can re-derive them
```

## Degrees of reproducibility (state the one you achieved)

- **Turnkey:** one documented command regenerates a table/figure from logged data (best for
  analysis and plots).
- **Scripted-on-hardware:** scripts run end-to-end but require **comparable devices** and time
  (endurance runs, aging, long trace replays); document the hardware and expected runtime.
- **Descriptive:** prose and provenance detailed enough that a reader with the right hardware could
  rebuild the pipeline (acceptable for results that need specific or proprietary devices).

For FAST, aim turnkey for anything that runs from logged data, and be honest that device-bound
results are **scripted-on-hardware**: state which drives, which firmware, and how long. Promising
turnkey behavior that silently needs a specific SSD is worse than stating the hardware dependency.

## The hardware-variance caveat (state it plainly)

Storage numbers are device- and firmware-specific; a reader on a different drive should expect the
*trend*, not the exact factor. Say so, report **per device** rather than one blended number where it
matters, and bound generalization — this is not a weakness to hide but the honest storage posture
reviewers reward.

## Vignette: a file-system aging study

Consider a study whose results depend on a fragmented, aged volume. Its reproducibility spine: the
**aging workload as a runnable script** (so the fragmentation state is reconstructable), the exact
**mkfs/mount options and kernel**, the device models and firmware, the measurement scripts that read
from the device and file-system counters, and the analysis notebooks that turn logs into the paper's
figures — plus one honest sentence about which numbers require the specific drives used.

## Consistency and camera-ready pass

- Before submission: every scored number traces to the artifact; the availability statement matches
  reality; the artifact is anonymized (no owner strings, hostnames, cluster paths, or personal trace
  URLs).
- Before camera-ready: swap anonymized links for a permanent, licensed, DOI-issuing archive
  (Zenodo/figshare/Software Heritage) and align the statement with the USENIX artifact badges you are
  pursuing (`fast-artifact-evaluation`).

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Availability] concrete / vague / missing
[Provenance gaps] <device+firmware / device state / trace archival / counters / seeds>
[Reproducibility level] turnkey / scripted-on-hardware / descriptive, stated honestly
[Hardware dependency] <which results need which drives/firmware, stated?>
[Paper fixes] <must appear in the PDF>
[Artifact fixes] <additions before upload>
```
