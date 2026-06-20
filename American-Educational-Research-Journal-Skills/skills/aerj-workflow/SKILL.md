---
name: aerj-workflow
description: Use as the entry point for any American Educational Research Journal (AERJ) manuscript. Routes to the right AERJ sub-skill based on where you are in the lifecycle and whether the manuscript's field-wide education-research fit is clear. It dispatches; it does not draft content.
---

# AERJ Workflow Router (aerj-workflow)

The orchestrator for an AERJ submission. Figure out the stage and the manuscript's **dominant education
research lens**, then send the user to the matching skill. AERJ is a **field-wide generalist** journal;
the router's first job is to make sure the paper is pitched to the whole field, not to a single
subfield. The old SIA/TLHD section split ended for new manuscripts in 2015.

## When to trigger

- Starting a new AERJ paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding whether the paper's policy/institutional, teaching/learning, development, or cross-cutting lens is clear
- Returning with a decision letter (route to `aerj-rebuttal`)

## First question: what is the dominant lens?

| Situation | Dominant lens | Then |
|-----------|---------------|------|
| Policy, governance, equity, organizations, institutions | Policy / institutional / organizational | normal pipeline below |
| Teaching, learning, instruction, human development | Teaching / learning / development | normal pipeline below |
| Sits across lenses | name the **dominant framing** | explain why the contribution travels across the field |

> The lens is about **topic and framing**, not method. Quantitative, qualitative, and mixed-methods
> work can all fit if the education-research contribution is broad enough.

## Routing map (stage → skill)

```text
Idea / fit / field-wide lens?    → aerj-topic-selection
Where does it sit in the field?  → aerj-literature-positioning
What frames the contribution?    → aerj-theory-and-framework
Is the design defensible?        → aerj-research-design
Are the analyses sound?          → aerj-data-analysis
Are the exhibits clear?          → aerj-tables-figures
Does it read for the field?      → aerj-writing-style
Reporting standards & data?      → aerj-transparency-and-data-policy
How will it be judged?           → aerj-review-process
Ready to submit?                 → aerj-submission
Got an R&R / decision?           → aerj-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-and-framework → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data-policy → review-process → submission → rebuttal`

Iterate: most papers loop framework ↔ design ↔ analysis several times before writing-style.

## Anti-patterns

- Treating AERJ like a narrow specialty journal — the contribution must reach the whole field
- Confusing **topic lens** with **method** (AERJ takes quantitative, qualitative, and mixed work)
- Forcing a quantitative template onto qualitative or mixed work (each is judged on its own terms)
- Skipping the reporting-standards / data step until acceptance

## Stage-to-risk routing table (AERJ-specific)

The router's value is catching the failure that kills a paper at *this* stage before it compounds.
Each row pairs the lifecycle stage with the AERJ-specific risk and where to send the user.

| Stage | The AERJ-specific risk here | Route to |
|-------|-----------------------------|----------|
| Idea | Subfield-only scope; unclear AERJ lens | aerj-topic-selection |
| Positioning | Talks to insiders, not the field | aerj-literature-positioning |
| Framework | Under-theorized; frame does no work | aerj-theory-and-framework |
| Design | Method-claim mismatch across quant/qual/mixed | aerj-research-design |
| Analysis | Nesting ignored; warrant not shown | aerj-data-analysis |
| Exhibits | Not self-contained; non-APA; not masked | aerj-tables-figures |
| Writing | Jargon untranslated; over-claiming | aerj-writing-style |
| Transparency | Reporting standard unmet; no data plan | aerj-transparency-and-data-policy |
| Decision | Treating R&R as acceptance | aerj-rebuttal |

## Worked routing vignette (illustrative)

A team arrives with a finished **mixed-methods study of a districtwide grading reform** and asks
"are we ready to submit?" The router does not jump to submission. It first checks the dominant lens
(the institutional reform framing needs to travel beyond one district), then surfaces that the
qualitative strand and the illustrative **0.15 SD** achievement estimate were never integrated — an
AERJ referee will flag two stapled papers. So the route is `aerj-research-design → aerj-data-analysis` for the joint
display *before* `aerj-submission`. Sequencing the integration fix first saves a likely review cycle.

## Lens-confusion failure mode and the fix

- *Routed by method.* → Re-route on topic and framing; quantitative, qualitative, and mixed designs can
  all fit. Confirm scope against the journal's current submission guidelines.
- *Skipped transparency until acceptance.* → Insert aerj-transparency-and-data-policy into the loop
  early; AERA reporting standards are easier to build in than to retrofit.

## Output format

```
【Stage】idea / positioning / framework / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Dominant lens】policy/institutional / teaching-learning / development / cross-cutting (and why)
【Route to】aerj-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — education-research data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AERJ URLs behind every fact in this pack
