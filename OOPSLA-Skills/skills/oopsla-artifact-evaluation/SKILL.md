---
name: oopsla-artifact-evaluation
description: Use when packaging an artifact for an accepted OOPSLA paper under the SPLASH artifact-evaluation track — surviving the kick-the-tires phase, earning the Functional and Reusable badges, depositing a Zenodo snapshot with a DOI for Available, and aligning artifact claims with the paper's Data-Availability Statement.
---

# OOPSLA Artifact Evaluation

SPLASH runs a unified artifact-evaluation track for its research papers; the
2026 edition used a **two-phase** process — an opening *kick-the-tires* pass
where evaluators check the artifact builds and starts at all, then the full
evaluation — awarding **Functional** (documented, complete enough to
exercise), **Reusable** (Functional plus organization and documentation that
support reuse by others), and **Available** (a snapshot deposited on Zenodo
with a DOI), with Available strongly encouraged for every passing artifact
absent licensing or privacy constraints. Per-cycle dates and submission
mechanics live on the current track page (待核实 each cycle).

## Design for the kick-the-tires failure mode

Most artifacts that miss a badge die in the first hour of a stranger's time:
a build that assumes your machine. The discipline is to treat the evaluator
as a hostile fresh VM.

```text
Golden-path contract (put this at the top of README.md):
  1. Requirements: OS/arch, RAM, disk, expected wall-clock time
  2. One command to build (container image or pinned toolchain)
  3. One command for a 10-minute smoke result mapped to a named claim
  4. One command per paper table/figure, each with expected output range
  5. What may legitimately differ on other hardware, and by how much
```

Dry-run the contract yourself on a machine that has never seen the project —
laptop-hosted paths, private registries, and license-gated dependencies are
the classic silent breakers.

## Badge strategy

| Badge | What actually earns it | Cheap mistakes that forfeit it |
| --- | --- | --- |
| Functional | Inventory + docs sufficient to exercise the artifact; results consistent with the paper | Missing inputs; undocumented flags; claims that need hardware you didn't disclose |
| Reusable | Clear structure, extension points, explained internals — a stranger could build *on* it | A working but opaque tarball; hard-coded paths; no guidance beyond replication |
| Available | Zenodo (or equivalent archival) deposit with DOI | GitHub-only "archive" (mutable, not archival); DOI minted after the camera-ready statement was frozen |

Reusable is where OOPSLA-style artifacts differentiate: language
implementations, calculi mechanizations, and corpus studies are exactly the
artifacts other groups extend, so structure the repository as a tool, not as
a paper appendix.

## Claim-to-artifact mapping

Evaluators read the paper's claims against what the artifact demonstrates.
Build the mapping explicitly and reuse it in three places: the artifact
README, the evaluation submission form, and the paper's Data-Availability
Statement (`oopsla-submission` requires the statement; `oopsla-camera-ready`
updates it with the final DOI).

- Every quantitative table/figure → a script that regenerates it.
- Every qualitative claim ("scales to", "handles all of") → a named test or
  corpus directory that witnesses it.
- Every claim the artifact *cannot* support (proprietary benchmark, cluster
  scale) → an explicit exclusion with justification, declared up front rather
  than discovered by the evaluator.

## Scope and timing notes

- Artifact evaluation is tied to acceptance rounds; papers accepted in Round 1
  and Round 2 flow through the process in different windows — read the track
  page for the round you were accepted in.
- Zenodo deposits are versioned: mint the DOI early, then publish updated
  versions as evaluation feedback lands; the DOI in the published article
  should resolve to the final version.
- Anonymity is over at this stage, but the *paper's* review-time supplement
  and the artifact must not contradict each other (`oopsla-supplementary`).

## Output format

```text
[Phase readiness] kick-the-tires dry-run: pass / failures listed
[Badge targets] Functional / +Reusable / +Available, with gaps per badge
[Claim map] <n claims mapped / m unmapped — list unmapped>
[Deposit] Zenodo DOI status + version plan
[Statement sync] Data-Availability Statement consistent: yes/no
```
