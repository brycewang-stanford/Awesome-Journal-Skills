---
name: jama-writing-style
description: Use when tightening prose and removing spin from a JAMA manuscript to match the journal's clinical house style and the AMA Manual of Style. Polishes language and framing; it does NOT change the analysis or the reported numbers.
---

# Writing Style & House Style (jama-writing-style)

## When to trigger

- Prose is verbose, hedged, or jargon-heavy for a general clinician audience
- The Conclusions overstate the data ("spin")
- Observational findings are written with causal verbs
- Late-stage polish before submission, after design/stats/exhibits are settled

## House-style essentials (AMA Manual of Style)

- JAMA follows the **AMA Manual of Style**. Conform numbers, units, abbreviations, statistical notation, and reference format to it — verify current rules in the manual / author instructions.
- **SI units** with conventional units as needed; define every abbreviation at first use; avoid undefined acronyms.
- **Person-first, non-stigmatizing language** (e.g., "patients with diabetes," not "diabetics"); report and justify race/ethnicity and sex/gender per current JAMA guidance.
- Exact p-values (P = .04, not P < .05); leading zeros omitted for p-values per AMA convention; estimates always paired with 95% CIs.
- Active voice and short sentences where possible; the IMRaD structure (Introduction, Methods, Results, Discussion).

## Avoiding "spin"

Spin is language that makes results sound better than the data support. JAMA reviewers and editors actively police it.

| Spin pattern                                            | Fix                                                       |
|---------------------------------------------------------|-----------------------------------------------------------|
| Null primary outcome, upbeat conclusion                 | State the primary result plainly; do not pivot to secondaries |
| Secondary/post hoc outcome framed as main finding       | Foreground the pre-specified primary outcome              |
| "Trend toward significance" for a non-significant result | Report the estimate + CI; avoid the phrase                |
| Causal verbs ("reduced," "caused") for observational data | Use associational verbs ("was associated with")           |
| "Safe and well tolerated" beyond what harms data show   | Report harms quantitatively; calibrate the claim          |
| Over-generalizing beyond the studied population         | Bound the conclusion to the sample/setting                |

## Discussion structure JAMA expects

1. Brief statement of the principal findings (tied to the primary outcome).
2. Comparison with prior evidence; how this study adds.
3. Possible mechanisms / explanations (without overreach).
4. **Limitations** — candid, specific (bias, generalizability, power, missing data).
5. Conclusions and clinical relevance, proportionate to the evidence.

## How JAMA editors read for spin and clarity

At the Journal of the American Medical Association, manuscript editors and the AMA Manual of Style copy desk hold prose to a general-clinician readability standard and treat unsupported optimism as a fixable defect. The bar: a non-specialist clinician reads the Conclusions, knows what changes at the bedside, and trusts the wording does not exceed the data. Recurring fixes: Conclusions warmer than the Results get rewritten to the primary outcome; stigmatizing labels become person-first; a leading-zero "p=0.043" becomes exact P = .04 with the 95% CI; causal verbs on a cohort become "was associated with"; and generic limitations name the specific bias, population bound, and missing data.

## Worked micro-example: de-spinning a conclusion (illustrative)

Vignette (illustrative): a prospective cohort, N = 12,500 adults, finds a dietary pattern associated with lower incident heart failure; adjusted hazard ratio 0.88 (95% CI, 0.79-0.98).

- Spun draft: "Adopting this diet reduces heart failure and should be recommended for all adults."
- JAMA-calibrated rewrite: "Greater adherence was associated with lower incident heart failure (adjusted HR, 0.88; 95% CI, 0.79-0.98); whether the association is causal requires randomized evaluation."

The rewrite swaps the causal verb for associational language, keeps the estimate with its CI, and bounds the recommendation.

## Reviewer pushback and the fix

- "Conclusions overstate the data (spin)." Fix: tie the headline to the primary outcome; if null, say so and do not pivot to a secondary.
- "Clinical bottom line not actionable." Fix: end the Discussion with one restrained sentence on what a clinician should now do.

Calibration anchors (hedge where uncertain): person-first language, exact-P / no-leading-zero notation, and estimate-plus-CI pairing are durable AMA conventions; reference-formatting and race/ethnicity rules evolve — confirm against the latest AMA Manual of Style.

## Checklist

- [ ] Abstract, Results, and Conclusions agree numerically and in tone
- [ ] Conclusion is bounded by the primary outcome; no spin
- [ ] Observational findings use associational language
- [ ] Harms reported quantitatively before any "safe/tolerated" claim
- [ ] Abbreviations defined at first use; SI units; AMA statistical notation
- [ ] Person-first, non-stigmatizing language; race/sex reported per guidance
- [ ] A specific, candid Limitations paragraph is present
- [ ] Reference format follows AMA style (verify current rules)

## Anti-patterns

- Spin: a positive-sounding conclusion over a null primary outcome
- Causal language for an observational association
- "Trend toward significance" / "marginally significant"
- Burying limitations or making them generic ("as with all studies…")
- Jargon and undefined acronyms that exclude a general clinician reader
- Tone in the abstract that the body does not support

## Output format

```
【Spin found】none / instances: ...
【Causal-vs-associational language correct】yes / fixes: ...
【Harms calibrated】yes / no
【Limitations specific】yes / no
【AMA style conformance】numbers/units/abbrev/refs: ...
【Next skill】jama-cover-letter
```
