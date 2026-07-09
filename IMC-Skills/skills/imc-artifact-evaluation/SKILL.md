---
name: imc-artifact-evaluation
description: Use when preparing an ACM IMC artifact for release, covering the artifact-availability declaration, post-acceptance availability shepherding, DOI-issuing dataset archives, documenting measurement provenance and vantage points, Community Contribution Award eligibility, and the difference between the anonymized review artifact and the public release.
---

# IMC Artifact Evaluation

Use this for IMC's artifact and dataset story. Unlike venues with a separate badge-granting
committee, IMC's mechanism is centered on an **availability declaration** at submission plus
**shepherding after acceptance** to ensure the promised data, code, or platform actually becomes
available. The venue-defining incentive is the **Community Contribution Award**, which exists to
honor a released dataset, tool, or open platform. Whether IMC also awards formal ACM
reproducibility badges in a given edition is **待核实** — confirm on the current call.

## Two artifacts, two audiences

- **Review artifact (at submission):** anonymized for the reviewers — no owner strings, testbed or
  AS identifiers, probe-account IDs, cluster paths, or lab-domain links. It backs the paper's
  claims during double-blind review.
- **Public release (after acceptance):** de-anonymized, licensed, permanently archived. This is
  what the shepherd checks, what the camera-ready cites, and what the Community Contribution Award
  evaluates.

## The availability declaration, delivered

At submission you declared **full / partial / none**. After acceptance, the shepherd holds you to
it:

| Declared | What the shepherd expects | Common failure caught |
|---|---|---|
| Full | The dataset/tool/platform, publicly retrievable and documented | Link promised, never published; broken archive |
| Partial | The shareable subset + a stated reason for the rest | "Partial" used to avoid work; unclear what is shared |
| None | A specific, legitimate justification (proprietary/privacy/legal) | Vague "on request"; no reason given |

"Available on request" is **not** availability. If law or privacy blocks release, say precisely
why and, where possible, release a derived/aggregated safe version.

## What a strong measurement dataset release contains

```text
[Data]        the measured dataset itself (or a documented, privacy-safe derivative)
[Schema]      a documented schema/dictionary: every field, unit, and its meaning
[Provenance]  vantage points (locations, ASes, probe types), measurement dates and durations,
              target lists with capture dates, tool versions, sampling and rate limits
[Method]      the collection scripts/tooling and how to re-run the *method* (data will differ)
[Ethics]      the privacy/anonymization applied to the release; disclosure status
[License]     an explicit open license (e.g., CC-BY for data, OSI license for code)
[Archive]     a DOI-issuing repository (Zenodo, figshare, Software Heritage) or a durable
              community archive — not a personal homepage
```

## Reproducibility for a moving Internet

Measurement data cannot be re-collected identically — the Internet changes. So the release must
make the **captured data** and its **provenance** the reproducible core, and the **method**
re-runnable to produce *new* comparable data. Ship the analysis scripts that turn the released data
into the paper's figures; a number in the PDF that no script regenerates from the released data is
the contradiction a shepherd (and a reader) will flag.

## Community Contribution Award eligibility

The award recognizes an outstanding dataset, source-code distribution, open platform, or service
to the community. To be eligible, the data/code/tool must be **publicly available and usable by
the time of the camera-ready deadline** — not "coming soon." Aim for it by making the release:

- **Usable by a stranger:** documented schema, a README, and a runnable example.
- **Durable:** a DOI and a maintenance/versioning note.
- **Reusable:** an open license and, for platforms, an access path others can actually use.

## Worked vignette: releasing a longitudinal scan dataset

A paper contributes a two-year scan of a protocol's deployment. For a strong, award-eligible
release: publish the per-scan records with a documented schema; include vantage-point and timing
metadata for every scan; apply and document IP/host anonymization consistent with the Ethics
section; ship the analysis notebooks that regenerate each figure from the released data; deposit in
a DOI-issuing archive with a CC-BY license; and state honestly which raw captures cannot be shared
for privacy reasons and what safe derivative replaces them.

## Calibration

- Availability is judged at **camera-ready** time for the award and during **shepherding** for the
  accepted paper — plan the release before, not after, acceptance.
- Whether formal ACM badges are offered, and the exact shepherding process, vary by edition —
  confirm on the current call (**待核实**).

## Output format

```text
[Artifact role] anonymized review artifact / public release
[Declaration] full / partial / none (+ justification)
[Contents] <data/schema/provenance/method/ethics/license/archive>
[Reproducibility] scripts regenerate figures from released data? yes/no
[Award eligibility] public + usable by camera-ready? yes/no
[Fixes before release] <ordered list>
```
