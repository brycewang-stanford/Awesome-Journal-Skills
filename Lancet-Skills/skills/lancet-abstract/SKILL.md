---
name: lancet-abstract
description: Use to write The Lancet's structured abstract — ≤300 words under the exact headings Background, Methods, Findings, Interpretation, Funding — leading with the clinical question, reporting the primary outcome with effect size and 95% CI, citing the registration number, and naming the funder.
---

# Structured Abstract (lancet-abstract)

## When to trigger

- The design, reporting, and statistics are settled (do this late).
- The abstract is unstructured prose, over 300 words, or uses the wrong headings.
- The abstract uses "Results" and "Conclusions" — The Lancet uses **Findings** and **Interpretation**.
- The registration number or funder is missing from the abstract.

## The Lancet's five mandatory headings

The Lancet uses a structured abstract of **≤300 words** (confirm the exact cap in the current author guidelines) under these specific headings — and the wording of two of them is distinctive:

1. **Background** — the clinical/public-health problem and the specific question. One or two sentences.
2. **Methods** — design, setting (and countries, for multi-country trials), participants and eligibility, intervention/exposure and comparator, primary outcome, analysis population (ITT), and the **trial registration number** (e.g., ClinicalTrials.gov NCTxxxxxxxx; ISRCTN).
3. **Findings** *(not "Results")* — recruitment dates and numbers analysed; the **primary outcome with effect size and 95% CI** (absolute and relative where relevant); key secondary outcomes; principal harms/adverse events.
4. **Interpretation** *(not "Conclusions")* — what the findings mean for practice or policy, calibrated to the design; the single most important takeaway. No "more research is needed" as the whole message.
5. **Funding** — name the **funder(s)** (and "none" if unfunded). The Lancet requires the funding source in the abstract.

## Concrete template

```
Background  [The clinical/public-health problem and the specific question this study answers.]

Methods  We did a [design: e.g., multicentre, double-blind, randomised, placebo-controlled
trial] in [n] centres in [countries]. [Eligible participants were ...]. We randomly assigned
participants ([ratio]) to [intervention] or [comparator] [stratified by ...]. The primary
outcome was [outcome] in the [intention-to-treat] population. This trial is registered with
[registry], [number].

Findings  Between [date] and [date], we [screened/enrolled n and] assigned [n] participants
([n] to intervention, [n] to comparator). [Primary outcome] occurred in [n/N (%)] versus
[n/N (%)] (absolute difference [x%, 95% CI a–b]; [relative measure e.g. HR/RR/OR x.x,
95% CI a–b]; p=[exact]). [Key secondary outcome.] [Principal harms: serious adverse events
in n (%) vs n (%).]

Interpretation  [What this means for practice or policy, calibrated to the design — the
single most important, globally relevant takeaway.]

Funding  [Funder name(s); or "None".]
```

## Hard constraints

- [ ] ≤ ~300 words (confirm current cap; treat 300 as the ceiling).
- [ ] Exact headings: **Background, Methods, Findings, Interpretation, Funding** — "Findings" not "Results", "Interpretation" not "Conclusions".
- [ ] **Registration number** present (in Methods).
- [ ] Primary outcome reported with **effect size + 95% CI** (absolute and relative where applicable), not P alone.
- [ ] **Funder named** (or "None").
- [ ] Numbers in the abstract match the flow diagram and Table 1.

## What an editor reads in the abstract at triage

Because The Lancet rejects most submissions without external review, the abstract is the triage document. The editor scans Background and Interpretation for the practice- or policy-changing claim, then checks Methods for the registration number and Findings for the primary outcome carried as an effect with its 95% CI, not a bare P. The distinctive **Findings** and **Interpretation** headings signal whether the authors know the venue at all; the wrong headings are an immediate tell. An Interpretation that ends on "more research is needed" forfeits the one sentence that could have earned a review.

| Abstract element the editor checks | Pass condition | Common miss |
|------------------------------------|----------------|-------------|
| Headings | Background/Methods/Findings/Interpretation/Funding, exact | "Results"/"Conclusions" used |
| Registration | Number present in Methods | Omitted or only in the main text |
| Primary outcome | Effect + 95% CI (absolute and relative) | P value alone |
| Interpretation | One practice/policy takeaway, design-calibrated | "More research is needed" |
| Funding | Funder named (or "None") | Left blank |

## Worked micro-example (illustrative numbers — not real data)

A hypothetical multi-country RCT of a single-dose oral therapy versus placebo for a high-burden condition, primary outcome cure at 28 days.

```
Findings (illustrative):
  "Between March 1, 2022, and Aug 31, 2023, we randomly assigned 1 980 participants
   (990 to therapy, 990 to placebo). Cure at 28 days occurred in 743/990 (75.1%)
   versus 614/990 (62.0%) (absolute difference 13.1 percentage points,
   95% CI 9.0-17.2; risk ratio 1.21, 95% CI 1.13-1.30; p<0.0001; NNT ~8, illustrative).
   Serious adverse events occurred in 22 (2.2%) versus 19 (1.9%)."
Methods: "...registered with ClinicalTrials.gov, NCTxxxxxxxx."
Interpretation: one sentence on the global-health practice change, not "more research is needed."
```

The primary outcome carries an absolute difference, a relative risk, and an NNT — all with 95% CIs — and the registration number sits in Methods, so the abstract passes the editor's first read.

## Output format

```
【Headings correct?】 Background / Methods / Findings / Interpretation / Funding — exact? yes/no
【Word count】 N ≤ 300
【Registration number in Methods?】 yes/no
【Primary outcome with effect size + 95% CI?】 yes/no + the numbers
【Funder named?】 yes/no
【Findings/abstract numbers reconcile with flow diagram + Table 1?】 yes/no
【Drafted abstract】 the five-section abstract, filled
【Next】 lancet-writing
```

## Anti-patterns

- **Do not** label the sections "Results" / "Conclusions" — use Findings / Interpretation.
- **Do not** omit the registration number or the funder.
- **Do not** report only a relative effect (HR/OR/RR) when an absolute effect is informative.
- **Do not** end Interpretation on "further research is needed" as the sole message — state the practice/policy implication.
