---
name: devpsych-open-science-and-transparency
description: Use when meeting Developmental Psychology's (APA) open-science and transparency expectations under the Transparency and Openness Promotion (TOP) guidelines — data and materials sharing with persistent identifiers, preregistration, sample-size justification, and JARS-consistent disclosure — with the ethical handling of data from minors and vulnerable populations. Prepares compliance; it does not waive requirements.
---

# Open Science & Transparency (devpsych-open-science-and-transparency)

Developmental Psychology has adopted the **Transparency and Openness Promotion (TOP)** guidelines, so a
submission is judged partly on **disclosure, data/materials availability, and preregistration**. The
developmental twist is that much data come from **minors and vulnerable populations**, so "share
everything" is tempered by **consent scope, confidentiality, and re-identification risk** — handled as a
justified, documented constraint, not silent opacity. Build this early, not at acceptance.

## When to trigger

- Building data/materials deposits and the data-availability statement
- Deciding whether and how to share data collected from children/vulnerable groups (and what to withhold)
- Linking a preregistration and reporting its status under JARS
- A reviewer or editor flagged transparency, reproducibility, or sample-size justification

## What TOP-style transparency asks (verify current wording on the official page)

1. **Data and materials availability.** Make data, analysis scripts, and materials available where
   ethically possible, with a **data-availability statement**; constraints (consent scope, minors'
   confidentiality, IRB limits) must be **stated and justified**, with an access path where feasible.
2. **Persistent identifiers (DOIs).** Use repositories that mint DOIs (OSF, ICPSR, Databrary, Dataverse,
   Zenodo) — not transient personal links. **Databrary** is purpose-built for sharing developmental video
   and identifiable data under permission.
3. **Preregistration.** Preregister confirmatory developmental hypotheses and the analysis plan; report
   the status honestly and keep confirmatory/exploratory consistent end to end (JARS).
4. **Sample-size justification.** Provide an explicit basis for N (power for the change parameter,
   precision, or a decision rule) — required reporting, not a nicety (see `devpsych-study-design`).
5. **JARS disclosure.** All exclusions, conditions, measures, and how sample size was determined.

## Build-it-right checklist

- [ ] **Data** deposited with a **DOI** and a **data dictionary/codebook** (or a justified exemption)
- [ ] **Analysis scripts** deposited; results regenerate in a fresh session
- [ ] **Materials** (tasks, stimuli, coding manuals) deposited with a DOI where licensing allows
- [ ] **Preregistration** linked (anonymized for masked review); confirmatory/exploratory consistent
- [ ] **Data-availability statement** drafted, stating what is shared and what is restricted, and why
- [ ] **Sample-size justification** reported (power for the change parameter)
- [ ] Minors'/vulnerable-population data handled per consent and IRB; identifiable material via a
      permission-based archive (e.g., Databrary) or de-identified with documented limits
- [ ] Shared links **anonymized** for the masked submission

## Sharing data from minors — do it honestly

- If full open data are not ethical (consent did not cover broad sharing, video is identifiable, IRB
  restricts redistribution), state **what** is restricted, **why**, and **how** others can access or
  approximate it — restricted-access archives (ICPSR, Databrary), de-identified extracts, synthetic data,
  or code release. Unjustified opacity counts against the paper; a documented constraint does not.

## Data-availability statement — worked draft (illustrative)

For the three-wave effortful-control package; confirm current required wording on the official page.

```
Data availability: De-identified trial-level data and analysis scripts for
  all three waves are openly available at OSF (DOI 10.XXXX/osf.io/abcde),
  with a codebook. Identifiable observational video is shared under
  permission via Databrary (DOI 10.XXXX/...), consistent with consent and IRB.
Materials: Task scripts and the effortful-control coding manual are deposited
  (DOI 10.XXXX/osf.io/fghij).
Preregistration: Hypotheses, the invariance-test plan, and the growth model
  were preregistered before wave-3 analysis (osf.io/pqrst).
Constraints: Raw video cannot be openly posted (identifiability, minors);
  access is available to authorized researchers via Databrary.
```

## Transparency-readiness decision table

| Situation | Editorial read | What to deposit / state |
|-----------|----------------|-------------------------|
| De-identified tabular data + scripts | expected baseline | DOIs for data, materials, scripts + run log |
| Identifiable child video/audio | constraint accepted if justified | permission-based archive (Databrary) + access path |
| Consent did not cover broad sharing | partial sharing | de-identified extract + restricted-access path; say so |
| Secondary/large panel (NICHD, ECLS) | acceptable with provenance | cite source, version; share derivation scripts |
| "Available on request" | reads as non-compliant | replace with a persistent DOI / restricted archive |

## Reviewer / editor pushback and the venue fix

- "No DOI, just a personal link" → swap every transient link for a persistent identifier or a restricted
  archive before the masked submission.
- "Statement says open but the repo is empty" → deposit first, draft the statement from live DOIs.
- "How can children's video be shared?" → use Databrary/permission-based access; state the path, do not
  post identifiable material openly.
- "No sample-size justification" → add the power/precision rationale for the change parameter.

## Anti-patterns

- Treating data/materials sharing as optional or "available on request"
- Posting identifiable data from minors openly (a confidentiality breach), or refusing all sharing with
  no justification
- Personal/transient links instead of DOIs / restricted archives
- Omitting the sample-size justification
- Identifying author info in OSF/Databrary links during masked review

## Output format

```
【Open data】deposited + DOI + data dictionary (or justified restriction)? [Y/N]
【Open materials】deposited + DOI? [Y/N]
【Analysis scripts】deposited + fresh-session reproducible? [Y/N]
【Preregistration】linked (anonymized) + consistent with reporting? [Y/N/NA]
【Data-availability statement】drafted (what is shared / restricted / why)? [Y/N]
【Minors' data】handled per consent/IRB via permission-based access? [Y/N/NA]
【Sample-size justification】reported? [Y/N]
【Next】devpsych-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — OSF, ICPSR, Databrary, Dataverse, Zenodo, preregistration templates
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — TOP guidelines, data policy, and JARS
