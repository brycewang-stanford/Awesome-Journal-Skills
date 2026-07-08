---
name: cscw-experiments
description: Use when designing or auditing the empirical work behind a CSCW paper — interview and ethnographic rigor, trace and log analysis, surveys, deployments, and mixed methods — matching each method's own validity standard and the ethics of studying real communities.
---

# CSCW Empirical Work

"Experiments" is the wrong word for most CSCW evidence, and that is the point.
The venue is deliberately methods-pluralist: interview studies, ethnography,
large-scale trace analysis, surveys, field deployments, controlled experiments, and
mixed designs all publish here — **each judged by its own tradition's standard of
rigor, not by a quantitative default.** The commonest reviewing disaster is a paper
that borrows a method without its discipline.

## Rigor, by method family

| Method | What rigor means here | What reviewers flag |
| --- | --- | --- |
| Interviews | Purposeful sampling with a rationale; saturation or a defended stopping rule; a described analysis process (coding approach, memoing, disagreement handling) | "We interviewed 12 people and themes emerged" with no analytic trail |
| Ethnography / field observation | Duration and depth of engagement; researcher's relationship to the setting; thick description that earns the interpretation | Drive-by observation labeled ethnography |
| Trace / log analysis | Construct validity (does the log field measure the practice claimed?); an identification strategy for any causal wording; robustness to platform quirks (bots, deleted content, API sampling) | Correlational results narrated causally; metrics inherited from the platform unexamined |
| Surveys | Instrument provenance or validation; sampling frame vs. claimed population; nonresponse handling | Convenience sample generalized to "users" |
| Deployments / experiments | Genuine group-level conditions; power analysis where inference is statistical; contamination between conditions addressed | N = groups treated as N = individuals |
| Mixed methods | An explicit integration logic — which strand leads, which bounds, where they may disagree | Two mini-studies stapled together, each too thin to stand |

Two pluralism rules cut across all rows:

- **Do not apply one tradition's checklist to another's method.** Demanding
  inter-rater reliability statistics from an interpretivist analysis, or accepting
  vibes in place of identification from a causal claim, are the same category of
  error. State *which* tradition your analysis works in, then meet that tradition
  fully.
- **Qualitative sample sizes are justified by purpose, not by envy.** Twenty-four
  well-chosen moderators can ground a concept; two million log rows cannot rescue a
  construct that measures the wrong thing.

## Group-level design decisions

- **Unit of analysis and unit of observation must be named separately.** You may
  observe individuals (interviewees, accounts) while claiming about collectives
  (teams, communities); the analysis section must say how the aggregation is
  licensed.
- **Sample communities, not just people.** For multi-community studies, describe
  how communities were chosen and what variation the set covers — community
  selection is the qualitative analogue of a sampling frame.
- **Time matters.** Cooperative practices are rhythms (shift rotations, release
  cycles, norm renegotiations). A snapshot design should say what it cannot see.

## Ethics as design, not paperwork

CSCW evidence usually comes from real communities with stakes in the findings.
Reviewers read the ethics description as part of the method:

- State IRB/ethics-review status and the consent posture for each data source —
  including whether "public" trace data was treated as fair game and why that is
  defensible for *this* community.
- Plan quote handling at design time: verbatim quotes from small or hostile-scrutiny
  communities can be reverse-searched; commit to paraphrase or alteration policies
  and disclose them.
- Consider the community's exposure, not only the individual's: naming a small
  community can harm it even with every user anonymized (see
  `cscw-artifact-evaluation` for release-time handling).

## Evidence-plan skeleton

```text
[Claim]        <the group-level finding this study must support>
[Tradition]    interpretivist / positivist / computational / mixed (lead strand: ___)
[Observation]  who or what is observed, at what unit and timescale
[Aggregation]  how individual observations license collective claims
[Validity]     the ONE threat most likely to sink this design + mitigation
[Ethics]       consent posture per data source; quote policy; community exposure
[Stop rule]    what tells you data collection is done
```

Draft this skeleton before collecting anything; paste the filled version into the
methods section as its outline. Under Revise and Resubmit, new data collection is
often infeasible — a design that anticipates the obvious objection is the cheapest
insurance the journal model offers.

Method norms are stable venue culture; submission-mechanics facts elsewhere in this
pack carry the 2026-07-08 access date and should be re-verified independently.
