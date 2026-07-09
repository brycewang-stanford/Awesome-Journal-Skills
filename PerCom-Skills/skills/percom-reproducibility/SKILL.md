---
name: percom-reproducibility
description: Use when strengthening IEEE PerCom reproducibility and open-data evidence for human-subjects sensing, covering the dataset-availability statement, de-identified datasets with IRB/consent handling, sensing provenance (devices, sampling, labeling), cross-subject reproducibility, honest degrees of reproducibility, and consistency between what the paper says and what the dataset contains.
---

# PerCom Reproducibility

Use this before submission and again before camera-ready. In pervasive computing, reproducibility
turns on **the sensing data**: a PerCom result is only as trustworthy as the dataset behind it, how
it was collected, and whether it generalizes across people. The goal is that a competent reader
could rebuild your pipeline and reach your conclusions — and, where ethics permit, on your actual
data.

## Evidence map

- Map each recognition/system claim and reported number to a **verifiable location** — a paper
  section, a table generated from logged data, or a script in the artifact.
- For recognizers, give enough of the features, model, hyperparameters, and **evaluation split**
  (leave-one-subject-out / leave-one-session-out) that a reader could re-run it.
- For datasets, report subjects and their selection, sensors and placement, sampling rates,
  labeling protocol and inter-annotator agreement, and preprocessing (filtering, windowing,
  normalization).
- Keep the **dataset-availability statement** truthful and specific: what is shared, where it will
  live after acceptance, and — if something cannot be shared — exactly why (privacy, IRB, consent).
- Keep the paper and the dataset **consistent**: a number in the PDF that no script reproduces from
  the released data is the contradiction reviewers read as carelessness.

## Dataset-availability statement audit

| Claim in the paper | Weak availability answer | PerCom-ready answer |
|---|---|---|
| "We collected data from N participants" | "Dataset available on request" | De-identified dataset + datasheet, or a documented restricted-access path with the ethics reason |
| "Our recognizer generalizes across users" | "Code will be released" | Runnable pipeline with a **LOSO** reproduction script and a README demo |
| "We labeled activities" | Nothing about protocol | Labeling protocol, annotator agreement, and the label files |
| "We deployed in a smart space" | "Testbed is proprietary" | Sensor list, placement, and sampling; simulated/sample data if the raw cannot ship |

"Available on request" reads as *not available*; convert every such line into a concrete,
de-identified dataset or an explicit, justified exception with a request path.

## Sensing provenance floor

```text
[Devices]    device models + firmware, sensor types, sampling rates, placement on body/space
[Labels]     labeling protocol, who labeled, inter-annotator agreement, label schema
[Preprocess] filtering, windowing, normalization, resampling -- the exact pipeline, not prose
[Splits]     leave-one-subject-out / session-out defined so a reader reproduces the same folds
[Ethics]     IRB/approval status, consent scope, and the de-identification performed
[Compute]    hardware, training time, number of runs so a reader can size a reproduction
[Randomness] seeds for any stochastic step; say what is and is not deterministic
```

## Degrees of reproducibility (state the one you achieved)

- **Turnkey:** one documented command regenerates each table/figure (including the LOSO result)
  from released data.
- **Scripted:** scripts exist but require documented manual steps or restricted-data access.
- **Descriptive:** prose detailed enough that a competent reader could rebuild the pipeline.

For PerCom, aim turnkey for anything a reviewer might rerun quickly (inference on a bundled sample,
a plot from logged features); full raw human-subjects data may stay **scripted with restricted
access** when consent/IRB forbids public release — but say so honestly rather than promising
turnkey behavior that cannot legally run.

## Vignette: a wearable HAR study

Consider a study collecting wrist-IMU data from participants doing daily activities. Its
reproducibility spine: the collection protocol and device/sampling details; the de-identified
extracted dataset with a datasheet; the labeling protocol with annotator agreement; the feature and
model code; the **leave-one-subject-out** evaluation scripts that regenerate the F1 table; and one
honest sentence about the parts (raw video used for labeling, re-identifiable timestamps) that
cannot be shared and why.

## Consistency and camera-ready pass

- Before submission: every scored number traces to the artifact; the availability statement matches
  reality; the review package is anonymized (no testbed, lab, or owner strings).
- Before camera-ready: swap anonymized links for a permanent, DOI-issuing, de-identified deposit
  (IEEE DataPort / Zenodo), and align the statement with what you actually release
  (`percom-artifact-evaluation`).

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Dataset availability] concrete / vague / restricted-with-reason / missing
[Provenance gaps] <devices / labels / preprocessing / splits / ethics / seeds / compute>
[Cross-subject reproduction] LOSO script present and matching the paper? yes/no
[Reproducibility level] turnkey / scripted / descriptive, stated honestly
[Paper fixes] <must appear in the PDF>
[Dataset fixes] <additions before release>
```
