# External Tools & Data Sources for JPP&M Work

Resources that recur in marketing-and-public-policy research. Availability and access terms change; verify each before building a design around it.

## Regulatory and policy sources

| Source | Use |
|--------|-----|
| Regulations.gov | live rulemakings, comment periods, agency dockets — find the contested margin |
| Federal Register | rule texts and effective dates for evaluation timelines |
| FTC reports, cases, and Green Guides | deception/unfairness enforcement record; substantiation standards |
| FDA labeling rules and guidance (food, tobacco, drugs) | mandated-format specifics for realistic stimuli |
| CFPB research reports and consumer complaint database | financial-marketing harms and outcome measures |
| State AG actions / NAD-CARU self-regulation decisions | sub-federal and self-regulatory enforcement variation |
| OECD / WHO / EU DG-SANTE policy trackers | cross-country policy variation for comparative designs |

## Data for evaluation and field designs

| Source | Use |
|--------|-----|
| NielsenIQ / Circana (via Kilts Center) scanner panels | purchase outcomes around labeling, tax, and marketing-restriction rollouts |
| Ad-spend archives (Vivvix/Kantar-type) | firm strategic response: spend shifts around regulation |
| BRFSS, NHANES, PATH (tobacco) | population health behaviors for public-health-marketing outcomes |
| Survey of Consumer Finances; CFPB Making Ends Meet | financial well-being outcomes |
| ICPSR and agency public-use files | archived evaluation datasets |
| Prolific / CloudResearch with quota screening | policy-target samples for experiments (screen for the protected population) |

## Software and method aids

- **Stata**: `csdid`, `did_multiplegt`, `eventstudyinteract` (staggered DiD); `rdrobust`, `rddensity` (RDD); `synth`/`synth_runner`; `boottest` (wild cluster). See the vendored kit in [`code/`](code/).
- **R**: `did`, `fixest`, `HonestDiD`, `rdrobust`, `tidysynth`; `metafor` for meta-analysis of label/warning effects.
- **Experiments**: G*Power for a priori power; AsPredicted/OSF for pre-registration; PROCESS or `lavaan` where a mechanism layer supports the policy claim.
- **Text/records**: comment-letter scraping from Regulations.gov for stakeholder-position analysis.

## Method notes

- For policy evaluations, archive the policy-timing ledger (adoption, effective, enforcement dates per jurisdiction) alongside the code; reviewers will ask.
- Keep a raw-to-analysis data lineage and a table-reproduction script even though first-submission deposits may not be mandatory — the revision will demand them faster than you can rebuild.
- For vulnerable-population studies, document recruitment, consent, and compensation decisions as part of the methods audit trail.
- Cross-pack references: [`../../shared-resources/empirical-methods/reporting-standards.md`](../../shared-resources/empirical-methods/reporting-standards.md) and [`../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
