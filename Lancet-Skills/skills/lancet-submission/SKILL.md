---
name: lancet-submission
description: Use as the final preflight before submitting to The Lancet — a complete checklist across importance, registration, reporting guideline + flow diagram, statistics, structured abstract, the Research in context panel, ethics/declarations/data-sharing, and required files. Bundles a checklist and a cover-letter template.
---

# Submission Preflight (lancet-submission)

## When to trigger

- The manuscript is "done" and you are about to upload.
- You want a single gate that confirms every other lancet-* skill's output landed.
- A revision is going back and you need to confirm nothing regressed.

## Master preflight checklist

### Importance & framing
- [ ] Clears the importance / global-relevance / practice-or-policy bar (`lancet-fit` rung ≥ 3).
- [ ] Equity/global-health angle articulated where relevant.
- [ ] Title declarative and specific; reflects design (e.g., "a randomised controlled trial").

### Registration & design
- [ ] Trial **registered prospectively**; registration number in the **abstract** and Methods.
- [ ] Protocol + pre-specified **SAP** available; primary outcome matches the registered one.
- [ ] RCT: randomisation, allocation concealment, blinding, ITT — described.

### Reporting guideline & flow diagram
- [ ] Correct EQUATOR guideline (CONSORT / STROBE / PRISMA / SPIRIT / ...) with completed checklist, page/line-mapped.
- [ ] **Flow diagram** present (CONSORT for RCT, PRISMA for review); numbers reconcile with Table 1 and analysis populations.

### Statistics
- [ ] Effect estimates with **95% CI**; exact P; absolute + relative effects (NNT where relevant).
- [ ] Pre-specified primary analysis; ITT primary + per-protocol sensitivity; missing-data handling.
- [ ] Multiplicity strategy for secondary endpoints; subgroups pre-specified + interaction tests.

### Structured abstract
- [ ] ≤300 words under **Background, Methods, Findings, Interpretation, Funding** (exact headings).
- [ ] Registration number in Methods; primary outcome with effect size + 95% CI; funder named.

### Research in context panel
- [ ] All three parts present (Evidence before / Added value / Implications).
- [ ] "Evidence before this study" documents a systematic search (databases + terms + dates).

### Figures & tables
- [ ] Table 1 baseline characteristics (no baseline P in an RCT).
- [ ] Kaplan–Meier with numbers at risk / forest plot / map — as the design warrants; CIs shown.

### Ethics, declarations & data
- [ ] Ethics approval + consent (all sites) + Declaration of Helsinki.
- [ ] **Declaration of interests** for all authors (ICMJE).
- [ ] **Role of the funding source** statement (funder role + data access + final responsibility to submit).
- [ ] **Data sharing statement** (ICMJE-compliant for trials).
- [ ] ICMJE author contributions (incl. who verified the data); SAGER sex/gender + equity reporting; PPI statement.

### References & required files
- [ ] References within budget (~30 for an Article), correct style; all in-text citations resolve.
- [ ] Main text (IMRaD + panel), abstract, tables, figures + legends, appendix/supplement.
- [ ] Reporting checklist; protocol/SAP; cover letter; authors/affiliations/ORCIDs; corresponding author.

## Final integrity sweep

- [ ] No over-claiming: causal language matches design; no superiority claim from a non-inferiority trial.
- [ ] All abstract / flow-diagram / Table 1 / text numbers reconcile.
- [ ] Registration number, ethics references, and any data-repository identifiers are correct and live.
- [ ] Headings are **Findings / Interpretation** (not Results / Conclusions).

## Templates

- `templates/checklist.md` — copyable preflight checklist.
- `templates/cover_letter_template.md` — clinical/global-importance cover-letter scaffold.

## Desk-reject patterns to clear before you upload

The Lancet declines most submissions without external review, so the preflight is really a pre-triage simulation. The editor reads the cover letter and abstract for one thing first: does this change clinical practice or public-health policy for a globally relevant problem. Then the submission system enforces the artifacts. Clear these before upload, because each is a fast bounce-back.

| Pre-triage failure | Where it surfaces | Pre-upload fix |
|--------------------|-------------------|----------------|
| Not practice/policy-changing for a broad, global audience | Cover letter + abstract Interpretation | Re-run `lancet-fit`; if rung < 3, reroute to a family title |
| Trial not prospectively registered | Methods + abstract | Disclose timing honestly; if retrospective, flag it explicitly |
| Wrong abstract headings | Structured abstract | Use Findings / Interpretation / Funding, not Results / Conclusions |
| No CONSORT/PRISMA flow diagram | Figures | Add the diagram; reconcile every number |
| Missing role-of-funding / data-sharing statement | Declarations | Add both; ICMJE data-sharing is mandatory for trials |
| Research in context panel absent or search-free | Main text | Build the three-part panel on a documented search |

## Cover-letter pitch: the one load-bearing paragraph

The Lancet editor wants the practice/policy claim in the first lines, calibrated to the design. State the clinical or public-health problem, the single most important finding with its effect and 95% CI, and what guideline or decision it changes — for whom, and where (the global-relevance hook). Do not pad with adjectives; editors discount "novel" and "important" unless the numbers carry them.

## Worked micro-example (illustrative numbers — not real data)

A hypothetical pragmatic, cluster-randomised trial of a community health-worker intervention to improve hypertension control across districts in three low- and middle-income countries.

```
Preflight verdict (illustrative):
  Fit: rung 4 (establishes a scalable public-health intervention) -> GO
  Registration: prospective, ISRCTN in abstract + Methods -> OK
  Reporting: CONSORT-Cluster + flow diagram, page/line-mapped -> OK
  Abstract: 296 words; headings Background/Methods/Findings/Interpretation/Funding -> OK
  Primary outcome in Findings: BP control 38.1% vs 27.4%,
    adjusted risk difference 10.6 pp (95% CI 7.2-14.0), NNT ~10 (illustrative)
  Panel: Evidence-before search (MEDLINE+Embase+Global Index Medicus, dates+terms) -> OK
  Declarations: role-of-funding + data-sharing + SAGER -> OK
  Cover-letter pitch: "scalable, equity-focused, policy-relevant in LMIC primary care"
  VERDICT: GO
```

Every other lancet-* skill's output has a line on this sheet; the preflight passes only when each lands, the numbers reconcile across abstract/diagram/Table 1, and the cover letter states the policy change in one sentence.

## Reviewer / editor-pushback patterns and the venue-specific fix

- *"Global-health relevance / equity not addressed."* → Add the equity framing (PROGRESS-Plus, LMIC generalisability) in Interpretation and the cover letter; re-check `lancet-fit`.
- *"Trial not prospectively registered."* → Disclose registration timing transparently; if retrospective, flag it — the editor may decline, so address it head-on.
- *"Primary outcome differs from the registered one."* → Reconcile to the registered outcome or explain the dated change explicitly (see `lancet-study-design`).
- *"Reporting checklist incomplete."* → Complete and page/line-map the EQUATOR checklist before upload; confirm any current file-format requirement against the journal's author guidelines.

## Output format

```
【Blocking gaps】 [...]  (must fix before upload)
【Warnings】 [...]       (should fix)
【Files ready】 main / abstract / panel / figures+tables / reporting checklist / protocol+SAP / cover letter / declarations
【Verdict】 GO / NO-GO + the top 3 fixes
【Next】 submit | lancet-rebuttal (after decision)
```

## Anti-patterns

- **Do not** upload a trial that lacks prospective registration without flagging it.
- **Do not** submit an RCT without a CONSORT flow diagram or a review without a PRISMA one.
- **Do not** skip the role-of-the-funding-source or data-sharing statements.
- **Do not** rely on memory; run the checklist top to bottom.
