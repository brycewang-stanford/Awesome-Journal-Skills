---
name: icse-artifact-evaluation
description: Use when preparing an artifact for the ICSE Artifact Evaluation track after paper acceptance, covering the ACM badge system (Available, Reusable, Results Reproduced/Replicated), evaluator-proof packaging, archival requirements, open licensing, and the January-window timeline anchored to recent cycles.
---

# ICSE Artifact Evaluation

ICSE's artifact track is a *post-acceptance, opt-in* evaluation: once the
paper is in, you submit the artifact to a separate committee that awards ACM-
standard badges printed on the published paper. It is the formal payoff of the
verifiability work done at review time — if `icse-reproducibility` was
followed, this skill is mostly packaging and paperwork.

## The badge system, as ICSE runs it

Verified against the ICSE 2026 artifact-evaluation track (read 2026-07-08;
ICSE follows the ACM artifact review and badging standard):

| Badge | Who applies | What evaluators check |
|---|---|---|
| **Artifacts Available** | Authors of papers accepted to Research, SEIP, NIER, SEIS, Doctoral Symposium, Demonstrations | Artifact is permanently archived in a public, DOI-issuing repository — not a personal GitHub, which can be deleted or rewritten |
| **Artifacts Reusable** (Evaluated) | Same tracks | Quality "significantly exceeds minimal functionality": careful documentation, structure that supports reuse and repurposing by others |
| **Results Reproduced / Replicated** | Authors of *prior published* SE work | Independent obtainment of the paper's results, per the ACM definitions |

Two structural notes. First, Available is about *archival*, Reusable about
*quality* — a beautifully engineered artifact on a transient URL fails the
first, a DOI'd tarball nobody can run fails the second; aim for both. Second,
the Reproduced/Replicated badges are a lane for already-published work, which
is also how your artifact gets *used*: build it expecting a stranger to
attempt exactly that next year.

## Timeline anchor

ICSE 2026 ran artifact registration on January 8 and submission on
January 15, 2026 — weeks after final paper decisions (December 18 in the
2027-cycle calendar) and months before the conference. The 2027 dates were
unposted at check time (待核实 at the ICSE 2027 artifact-evaluation page).
Planning consequence: the artifact deadline lands in the first working days
of January, so the package must be effectively done before the holidays.

## From review package to badge submission

The anonymized review-time package needs five upgrades:

1. **De-anonymize deliberately** — restore names, affiliations, the real
   license holder, and the citation file; re-point links from the anonymizing
   host to the permanent home.
2. **Archive with a DOI** — deposit in a DOI-issuing archive (Zenodo-class,
   institutional repository); record the DOI in the paper's availability
   statement before the camera-ready freezes (`icse-camera-ready`).
3. **License openly** — the ICSE AE guidance encourages open-source licenses
   (MIT, Apache-2.0, GPL) for code and open-data licenses (CC-BY, CC0) for
   data; a package with no license is legally unusable and evaluators notice.
4. **Write for the evaluator's clock** — a stranger, on their own machine,
   with a review load. Provide a container or exact environment recipe, a
   smoke test in minutes, and the full runs' costs stated honestly up front.
5. **Document for reuse, not just replay** — the Reusable bar is repurposing:
   how to run on *new* subjects, extend the benchmark, or swap the model —
   one section each in the README.

## The evaluator-proof README

```markdown
# Artifact for "<paper title>" (ICSE 20XX, paper #NNN)

## Claims supported
Table 3 (RQ1), Fig. 5 (RQ2) fully reproducible below.
Table 6 requires 40 GPU-hours; cached outputs + verification script provided.

## Kick the tires (10 min, laptop)
docker load < artifact.tar && ./smoke_test.sh   # expected output shown below

## Full reproduction
./reproduce_all.sh   # ~6 h CPU; per-table scripts listed in scripts/

## Reusing beyond the paper
- New subject program: docs/add_subject.md
- Different model backend: docs/swap_model.md

## Requirements / License / Citation
```

The claims-supported section is the trust anchor: state plainly which paper
results the artifact does and does not cover, and give a cached-output
verification path for anything expensive. Evaluators reward honesty about
coverage and punish discovering gaps themselves.

## Scoping what the artifact claims

Badge submissions fail more often from over-claiming than under-building.
Declare a claims scope narrower than the paper if that is the truth: "the
artifact reproduces RQ1 and RQ2; RQ3's industrial dataset is excluded under
NDA, and we include the analysis scripts plus synthetic sample data so the
pipeline itself is checkable." Evaluators can only award what they can
verify, and a scoped-honest artifact that fully delivers its scope reads
better than an everything-artifact with two broken paths. Match the scope
statement to the paper's Data Availability section — a mismatch between the
two is the first thing a careful evaluator diffs.

## Failure modes that cost badges

- **Bit-rot between acceptance and January**: dependency drift breaks the
  build; freeze a container image the week of acceptance.
- **Undeclared network/credential needs**: an artifact that must call a paid
  API mid-evaluation stalls; cache responses and make live calls optional.
- **Doc-code mismatch** after camera-ready edits changed table numbers —
  re-run the claims map against the final paper, not the submission.
- **Repository-instead-of-archive**: linking GitHub `main` where the badge
  requires an immutable DOI deposit.

## Reverify each cycle

Track list, badge set, deadlines, and submission form are set by each year's
AE chairs; the ACM badging vocabulary is the stable layer. Confirm the 2027
call before promising badge scope to coauthors — and note the badge is opt-in:
absence of one on a published ICSE paper signals nothing about its authors,
only about their January.

## Output format

```text
[Badges targeted] Available / Reusable / (Reproduced-Replicated for prior work)
[Archival] DOI minted? license file? citation file?
[Evaluator path] smoke-test minutes; full-run cost; cached-output coverage
[Reuse docs] new-subject and extension guides present?
[Deadline plan] frozen container by <date>; submission by the January window
```
