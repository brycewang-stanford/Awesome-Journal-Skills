# Simulated Referee Panel: paperX.tex → ACL 2027 (via ARR January 2027 cycle)

- **Configuration:** multi-agent, following `shared-resources/submission-readiness/simulated-referee.md` § Orchestration.
  - The AE ran the desk screen and the synthesis.
  - Three referee subagents worked independently, one lens each, on the ARR form (form B).
  - One adversarial verifier subagent checked the referees' major concerns.
- **Inputs given to each referee:** the manuscript path, the stage-0 preflight JSON, the calibrated venue bar, the form-B fields and its own lens. Referees were not shown each other's reports.
- **Status:** a rehearsal. This predicts the attack surface and the likely decision band, not an outcome.

---

## 0. Calibrated venue bar (given verbatim to all three referees)

> ACL 2027 via ARR, January 2027 cycle (submission January 4, 2027 AoE).
>
> - **Format and process:** long paper, 8 content pages. At least 3 reviewers, then an AC meta-review, then SACs/PCs decide Main, Findings or reject. Papers not selected for Main go automatically to Findings.
> - **What each band is judged on:** Findings is judged mainly on soundness and reproducibility. Main is additionally judged on novelty and impact.
> - **Evidence bar:** "a defensible measurement of a language capability with failure modes examined", not "beats the baseline once". Concretely:
>   - baselines tuned with equal care, including the strongest cheap or current baseline;
>   - breadth that matches the claim, with per-language results;
>   - significance tests on every claimed comparison, with multiple-comparison handling;
>   - multiple seeds;
>   - human evaluation that reports agreement, raters per item and pay;
>   - explicit contamination audits;
>   - an ablation for each credited component;
>   - a quantitative error analysis;
>   - every abstract and intro number traceable to the body.
> - **Required submission elements:** the Responsible NLP checklist (sections A–E) is mandatory. Incorrect or incomplete answers are desk-rejection grounds.
> - **Theme track:** homogenization and knowledge collapse in LLMs, including cross-lingual homogenization.
>
> Sources: ACL-Skills `resources/official-source-map.md` (re-verified 2026-11-23), `skills/acl-review-process`, `skills/acl-experiments`.

---

## 1. AE desk screen

**【Venue】** ACL 2027 Main/Findings via ARR. The bar is calibrated from the ACL-Skills source map and the acl-review-process and acl-experiments skills.

**Scope and interest.** The paper is squarely in scope: multilingual instruction-data selection, which also touches the 2027 cross-lingual homogenization theme. Interest is moderate to high, because translated instruction pools are standard practice and a cheap, reusable filter is useful.

**Fatal-flaw scan (mechanical, from preflight).** Submitted as-is, this is an ARR desk reject. The ARR CFP desk-rejects anonymity violations and papers without a Limitations section. The violations are:
- self-revealing prior work (l.43, "In our previous work … we showed … proposed per-language quotas");
- Acknowledgments naming a lab, an institution and a grant (l.218–219);
- a GitHub username that matches that lab (l.94);
- no Limitations section.

There is also an "Appendix ??" marker (l.85). The figure placeholders at l.153 and l.192 are not in the preflight but are equally a pre-deadline fix.

**Fatal-flaw scan (substantive).** Nothing makes the paper unreviewable. The AE read did flag several issues that a referee will find quickly:
- the abstract's contamination sentence (l.17) is contradicted by Setup l.76;
- the abstract's 7B number, 48.9, appears nowhere in the body, which says 47.5;
- the significance claim against IFD (l.129) does not follow from its own test.

**Closest work.** AlpaGasus and IFD, the English selectors used as baselines; the Aya and Bactrian-X resources; MT quality estimation and bitext filtering; and the authors' own prior per-language-quota work, which is not cited.

**【Desk-screen】**
- **Decision:** send out, conditional on the preflight FAILs being fixed before January 4, 2027.
- **Desk-reject risk as submitted today:** HIGH. The deciding reason is the anonymization breaches plus the missing Limitations section. Both are mechanical and fixable pre-deadline.
- **Desk-reject risk after the preflight fixes:** LOW.

---

## 2. Referee reports (independent, form B plus the referee template)

### Referee 1: Soundness / evaluation lens

**Scores at a glance:** Confidence 4 · Soundness 2 (Poor) · Excitement 2.5 · Overall 2.0 (Resubmit next cycle) · Recommendation: major revision.

**Paper summary.**

XQF scores each example in two ways:
- **round-trip consistency:** the minimum LaBSE cosine between the instruction and its NLLB round trip, and between the response and its round trip (l.57–61);
- **English-pivot quality:** a 1.3B reward model scores the English pivot (l.64).

Both scores are z-scored within each language and summed. XQF keeps the top ρ=30% of every language (l.67).

Setup:
- a 412K-example pool in 18 languages, six per resource tier (high, mid, low);
- Llama 2 7B and 13B, three seeds each;
- XCOPA, XStoryCloze, XNLI and MGSM.

Claimed results:
- XQF beats the full pool and four baselines at 30% retention, on every benchmark, at both scales;
- the low-resource tier gains 3.5 points;
- XQF is significant against the full pool in 13 of 18 languages after Holm correction, and is claimed to be significantly better than IFD;
- humans prefer XQF in 46.2% of comparisons versus 32.3% for the full pool.

**Strengths.**
- Every condition sees the same per-language quota (l.82).
- Three seeds, with mean±sd defined in the caption. All 12 Table 1 averages recompute exactly.
- Paired bootstrap with Holm–Bonferroni against the full pool.
- An ablation row for each credited component.
- A defect breakdown, a human-written vs translated analysis, and cost arithmetic that checks out (445 h ÷ 224 h ≈ 2 runs).
- Honest reporting of benchmark coverage (l.85).

**Weaknesses (decision-relevant first).**
1. The contamination statements contradict each other, and "affects all filtering methods equally" does not hold for a selection method.
2. The abstract's headline 7B number (48.9) appears nowhere in the body.
3. The significance claim against IFD rests on 7 uncorrected tests out of 18. There are no tests at 13B, against other baselines, or for the ablations.
4. The quota argument is circular, and the "no quota" ablation is confounded.
5. There are no per-language results. The comparison across tiers is confounded by which benchmarks cover each tier.
6. Baselines are tuned unequally, and cheap language-ID and pivot-rater baselines are missing.
7. Several mechanism and human-evaluation claims are unsupported, and the conclusion overclaims.

**Comments and typos.**
- l.76: the 412K count is in the wrong paragraph.
- l.79: say whether the 2,000 held-out instructions are excluded from training.
- l.149: "about 1.5 points" is actually +1.3 and +1.6.
- l.188: the mid tier also loses 0.8, not only the low tier.
- l.129 vs l.149: the high-tier gain is not significant in 5 of 6 languages, yet it matches the mid-tier gain.
- Tables 2 and 3 report no standard deviations.
- l.25: the claim that a global threshold removes low-resource data is never tested for AlpaGasus or IFD scores.

**Form-B additional fields.**
- **Limitations:** dependence on NLLB and LaBSE coverage; Llama 2 only; five languages rest on a single benchmark; no contamination audit.
- **Ethical concerns:** the annotator descriptions at l.91 and l.216 contradict each other, and pay is missing.
- **Reproducibility:** partial. The 70B rater and the 1.3B reward model are unnamed, and templates and per-language sample sizes are missing.
- **Datasets:** the release scope needs a license check.
- **Software:** promised.

**Major concerns.**

- **R1-M1: contamination handling is contradictory, and the "affects all methods equally" argument fails for selection.**
  - *Where:* Abstract l.17; Related Work l.49; Setup l.76 and l.85.
  - *Quotes:*
    - l.17: "All evaluation sets were deduplicated against the training pool before filtering."
    - l.49: "remove overlapping examples before any filtering is applied."
    - l.76: "We did not deduplicate the pool against the evaluation benchmarks … expect any such overlap … to affect all filtering methods equally."
  - *Mechanism:* each filter keeps a different 30%. XQF rewards cleanly translated items, so it may enrich for translated benchmark items. MGSM shows the largest gain.
  - *Fix:* run a 13-gram audit per benchmark and language; report the overlap within each filter's selection; rerun on decontaminated data; make all three statements agree.
  - *Owner skills:* acl-experiments, acl-writing-style.
- **R1-M2: the abstract's headline 7B number does not match the paper.**
  - *Quotes:* l.17 says "45.2 to 48.9"; l.32 and Table 1 (l.113) say 47.5.
  - *Mechanism:* 48.9 appears nowhere else. The abstract overstates the gain over the full pool by 60% (+3.7 vs +2.3) and doubles the apparent margin over IFD.
  - *Fix:* correct the abstract and add a numbers-traceability pass.
  - *Owner skill:* acl-writing-style.
- **R1-M3: the significance claim against IFD is invalid, and testing is applied selectively.**
  - *Quotes:*
    - l.88: "we control the family-wise error rate with the Holm--Bonferroni procedure".
    - l.129: "…without correction, XQF is significantly better in 7 languages; we therefore conclude that XQF significantly outperforms IFD across all languages."
  - *Mechanism:*
    - Seven uncorrected wins out of 18 cannot support "all languages", and the claim abandons the paper's own Holm procedure.
    - There are no tests against the other baselines, none at 13B, and none for the ablations.
    - Seed variance is collapsed before the bootstrap.
  - *Fix:*
    - apply Holm to every comparison, at both scales and for the ablations;
    - use a seed-aware bootstrap;
    - report a pooled confidence interval on the delta against IFD.
  - *Owner skill:* acl-experiments.
- **R1-M4: the quota analysis is circular, and the "no quota" ablation is confounded.**
  - *Quote:* l.159: "their within-language score distribution matches that of the retained high-resource examples once normalized … They are removed because raw consistency and quality scores are lower".
  - *Mechanism:*
    - After z-scoring, the distributions match by construction, so the comparison shows nothing.
    - A global threshold on summed per-language z-scores would keep about 30% of every language. The no-quota variant therefore apparently drops normalization as well, so neither the 1.2-point loss (l.188) nor the low-tier 37.4 isolates the quota.
  - *Fix:* define the global-threshold score; add a "per-language z-scores, global threshold" row; replace the argument with independent evidence, such as blind quality ratings or defect rates for the removed set.
  - *Owner skill:* acl-experiments.
- **R1-M5: aggregates hide per-language behavior, and the comparison across tiers is confounded by benchmark mix.**
  - *Quote:* l.85: "Japanese is covered only by MGSM, Burmese only by XStoryCloze, and Haitian Creole, Quechua and Tamil only by XCOPA".
  - *Mechanism:* the low tier is dominated by XCOPA, a two-way task, while the high tier mixes all four benchmarks. With no per-language table, a regression in one language can hide inside a tier average.
  - *Fix:* add a per-language × benchmark table; compare tiers within each benchmark; report per-language corrected p-values.
  - *Owner skill:* acl-experiments.
- **R1-M6: baselines are not tuned with equal care, and the strongest cheap baselines are missing.**
  - *Quotes:*
    - l.82: AlpaGasus-style rating "in its original language".
    - l.198: ρ is chosen for XQF only.
    - l.201: "responses partly or wholly in English (34%)".
  - *Mechanism:*
    - Every baseline runs at XQF's optimal ρ.
    - AlpaGasus is run in the setting the paper itself calls least reliable (l.25).
    - There is no language-ID filter and no QE-model baseline.
    - The 20% point is never reported.
  - *Fix:* sweep ρ for every baseline; add AlpaGasus on the pivot, language-ID plus heuristics, and QE baselines; report the held-out curve used to choose ρ.
  - *Owner skill:* acl-experiments.
- **R1-M7: mechanism claims in the analysis have no numbers behind them.**
  - *Where:* l.188 (per-tier attribution) and l.126 (the MGSM explanation).
  - *Fix:* report the ablation per tier and per benchmark; probe whether injected number corruption lowers the consistency score.
  - *Owner skill:* acl-experiments.
- **R1-M8: the human evaluation is underpowered as reported, compares against the wrong system, and describes its raters inconsistently.**
  - *Where:* l.91, l.162 and l.216 ("crowdworkers recruited on an online platform").
  - *Problems:* the comparison is against the full pool only, not IFD; there is no test; there are no per-language counts; 80% of items have a single rater; pay is missing.
  - *Fix:* add an XQF vs IFD arm; give per-language win/tie/loss counts with a sign test; report rater details and pay.
  - *Owner skills:* acl-experiments, acl-submission (checklist).
- **R1-M9: the conclusion overclaims beyond, and against, the evidence.**
  - *Quote:* l.212: "it will improve instruction tuning for any language and any base model, and it makes the collection of human-written multilingual instruction data unnecessary."
  - *Mechanism:* only one model family is tested, and XQF depends on NLLB and LaBSE coverage. The paper's own l.204 contradicts the "unnecessary" claim: XQF raises the human-written share from 32% to 41%, and human-only data reaches 46.0.
  - *Fix:* scope the conclusion to what was tested.
  - *Owner skill:* acl-writing-style.

**Minor concerns.**
- Small mismatches between text and tables.
- The inspection protocol at l.201: blinding, sample size, agreement.
- 13B has no tier breakdown, ablation or human evaluation.
- Step counts under a fixed epoch count are not given.
- The English constant *c*.
- The unnamed models.
- Third-person credit for the prior quota work.

**What would move me.**
- **To Findings:** fix M1–M5 and M9.
- **To Main:** additionally M6, M8 and one current base model.

---

### Referee 2: Novelty / contribution lens

**Scores at a glance:** Confidence 4 · Soundness 2.5 · Excitement 2 · Overall 2.0 (Resubmit next cycle) · Recommendation: major revision (Findings-level once fixed).

**Paper summary.** XQF combines round-trip consistency (NLLB plus LaBSE) with English-pivot reward-model quality, both z-scored per language, and keeps a 30% quota per language. On a 412K pool in 18 languages with Llama 2 7B and 13B, it beats the full pool and four baselines. The 7B average goes from 45.2 to 47.5, and 13B from 50.4 to 52.6. The low-resource tier gains 3.5 points.

**Strengths.**
- A real problem, documented concretely in the defect audit (l.201).
- A cheap design with reusable pivots (l.207).
- A fair budget across conditions, and random selection falls below the full pool.
- Useful ablations and a useful analysis of human-written vs translated data.
- Holm correction against the full pool, seeds, and a human evaluation that includes low-resource languages.

**Weaknesses (decision-relevant first).**
1. The delta over prior work is overstated and partly misattributed: the quota comes from the authors' own prior work, and consistency filtering is standard.
2. The strongest cheap baselines are missing: source-side QE, language ID, a pivot rater, and newer selection methods.
3. The claims exceed the evidence: 48.9 vs 47.5, "across all languages", and the conclusion.
4. The contamination statements contradict each other.
5. Timeliness: Llama 2 only, classification and math benchmarks only, and single-benchmark coverage for low-resource languages.

**Comments and typos.** The "Appendix ??" marker, fig:rate, and the uncited conneau2020xlmr. XLM-R language sampling is relevant to positioning the quota.

**Form-B additional fields.**
- **Best paper:** not applicable.
- **Limitations:** NLLB and LaBSE coverage; English-centric helpfulness norms imposed through an HH-RLHF reward model on pivots. The ethics claim at l.216 is not backed by l.201.
- **Ethics:** the annotator descriptions are inconsistent, pay is missing, and the Aya release needs a license check. Not a blocker.
- **Reproducibility:** 3. The reward model and the 70B rater are unnamed, and the appendix is missing.
- **Datasets:** 2.
- **Software:** 3.

**Major concerns.**

- **R2-M1: the delta over the closest prior work is misattributed, and contribution 3 is not new to this paper.**
  - *Quotes:*
    - l.43: "In our previous work on translated web corpora, we showed that a single global quality threshold removes low-resource languages disproportionately and proposed per-language quotas…"
    - l.33: contribution 3 presents the quota's necessity as a finding.
    - l.46: the paper calls round-trip translation and multilingual embeddings "established tools".
  - *Mechanism:*
    - The prior quota paper is uncited, so reviewers cannot judge the delta.
    - Consistency filtering is standard bitext-filtering practice. This point comes from the referee's outside knowledge: LASER/LaBSE filtering, round-trip QE, CCNet/MADLAD per-language thresholds.
    - Every baseline also gets the quota (l.82), so the real delta is the scoring function alone.
  - *Fix:* cite the prior work in the third person, state the precise delta, cite the filtering lineage, and rewrite contributions 1 and 3.
  - *Owner skill:* acl-related-work.
- **R2-M2: the strongest cheap and closest baselines are absent.**
  - *Where:* l.82, l.201, l.27, l.76.
  - *Missing baselines:*
    - source-side reference-free QE such as CometKiwi (the English source exists for the 281K translated items);
    - a language-ID filter (wrong-language responses are 34% of the defects);
    - AlpaGasus on the pivot (to isolate the idea at l.27);
    - per-method budgets (ρ was chosen for XQF);
    - post-2024 selection methods (outside knowledge).
  - *Fix:* add these three baselines at a matched budget, sweep ρ per method, and add one newer selection method.
  - *Owner skills:* acl-experiments, acl-related-work.
- **R2-M3: the headline claims are larger than, or contradict, the evidence.**
  - *Problems:*
    - 48.9 (l.17) vs 47.5 (l.32, l.113);
    - "any language / any base model / … unnecessary" (l.212) is contradicted by l.204;
    - the abstract's "survive correction … in 13 of 18 languages" is a result against the full pool only, yet it is placed next to "outperforming four filtering baselines".
  - *Fix:* correct the number, attribute the 13/18 result to the full-pool comparison, and replace the conclusion sentence.
  - *Owner skill:* acl-writing-style.
- **R2-M4: "outperforms IFD" is supported neither statistically nor by the human evaluation.**
  - *Where:* l.129 (7 of 18 uncorrected tests); l.91 (human evaluation against the full pool only).
  - *Margins:* +1.4 at 7B, +1.3 at 13B, +0.3 in the high tier.
  - *Fix:* apply Holm to the IFD and AlpaGasus comparisons; add an IFD arm to the human evaluation.
  - *Owner skill:* acl-experiments.
- **R2-M5: the contamination statements contradict each other, and differential retention could explain the delta.**
  - *Where:* l.17, l.49, l.76.
  - *Fix:* run a 13-gram check; report overlap per selected subset; use decontaminated benchmarks.
  - *Owner skills:* acl-experiments, acl-reproducibility.
- **R2-M6: significance and timeliness for ACL 2027, and an evaluation that does not match the claimed scope.**
  - *Where:* l.79 (Llama 2 only); l.85 (classification and math benchmarks; 4 of 6 low-resource languages on a single benchmark).
  - *Fix:* add a current multilingual base model and an open-ended multilingual instruction-following evaluation; report results per language.
  - *Owner skills:* acl-experiments, acl-topic-selection.
- **R2-M7: an English-centric homogenization risk, and a missed theme opportunity.**
  - *Where:* l.64 (an HH-RLHF reward model on English pivots); l.216 claims an analysis of culturally specific removals that l.201 does not contain.
  - *Fix:* annotate removed vs retained native examples for culturally specific content; discuss in Limitations.
  - *Owner skills:* acl-topic-selection, acl-writing-style.

**Minor concerns.**
- The circular argument at l.159.
- The global-threshold claim is attributed to English filters (l.25) without being tested on them.
- The MGSM mechanism is untested.
- The models are unnamed.
- The annotator descriptions.
- The asymmetry for English examples.
- The held-out curve used to choose ρ is not shown.
- The cost trade-off: XQF scoring costs about 5× IFD for a 1.4-point gain.

**What would move me.**
- **To Findings:** honest positioning; QE, language-ID and pivot-rater baselines with tuned budgets and Holm correction; a contamination check; a corrected abstract and conclusion.
- **To Main:** additionally a current base model, an open-ended evaluation, and the cultural-content analysis.

---

### Referee 3: Clarity / reproducibility / ethics lens

**Scores at a glance:** Confidence 4 · Soundness 2.5 · Excitement 3 · Overall 2 (Resubmit next cycle) · Recommendation: major revision (Findings-level once fixed).

**Paper summary.** XQF combines NLLB/LaBSE round-trip consistency with a 1.3B reward-model score on the English pivot, both z-scored per language, and keeps the top 30% per language. On a 412K pool in 18 languages with Llama 2 7B and 13B, it beats the full pool and four baselines. Low-resource languages gain 3.5 points, the quota is shown to be necessary, and a 6-language human evaluation is included.

**Strengths.**
- A real and clearly diagnosed problem (l.25).
- A simple, reusable method (l.207).
- Direct tests of the central design choice.
- Seeds with standard deviations, a stated Holm procedure, candid coverage disclosure, an error taxonomy, and cost comparisons.

**Weaknesses (decision-relevant first).**
1. Three contradictory accounts of contamination handling.
2. An abstract number (48.9) that is untraceable.
3. Inconsistent human-evaluation and annotator descriptions, with the information needed for checklist D missing.
4. A data release described inconsistently, with no licenses (checklist B).
5. The method cannot be reimplemented from the text.
6. Claims that the paper's own evidence contradicts.
7. Placeholder figures.

**Comments and typos.**
- The 412K count sits in the wrong paragraph.
- Add a per-language pool-size table.
- Define "averaging predictions over seeds".
- Tables 1 and 2 use different aggregation schemes.
- l.188: the mid tier also drops.
- The 20% retention point is missing.
- l.159 is tautological.
- The MGSM consistency evidence is missing.
- The inspection protocol is missing.
- Standard deviations are missing for several results.
- Say whether perplexity and IFD were recomputed at 13B.
- l.57: use `\text{English}`.

**Form-B additional fields.**
- **Limitations:** a bias against culturally specific and code-switched content, built into the consistency score (l.61); NLLB coverage; one model family.
- **Ethical concerns:** yes. Flag for the Ethics Advisory Committee: human-subject disclosures are missing and the redistribution plan is unclear.
- **Reproducibility:** 2.
- **Datasets:** 2.
- **Software:** 3.

**Major concerns.**

- **R3-M1: three mutually contradictory accounts of decontamination.**
  - *Where:* l.17, l.49, l.76; "held out" at l.85 and l.32.
  - *Mechanism:* a misleading-answer risk on checklist C, plus differential retention of translated benchmark-style items (XStoryCloze, XNLI and MGSM are themselves translations).
  - *Fix:* make one statement that is true everywhere; run the 13-gram check; report contamination within each filter's selection; re-run Table 1.
  - *Owner skills:* acl-experiments, acl-writing-style.
- **R3-M2: the abstract's headline 7B result is untraceable** (48.9 vs 47.5).
  - *Fix:* correct it and audit every abstract and intro number.
  - *Owner skill:* acl-writing-style.
- **R3-M3: the human evaluation's annotator descriptions contradict each other, and the information checklist D asks for is missing.**
  - *Where:* l.91 ("native-speaker annotators … team leads") vs l.216 ("crowdworkers recruited on an online platform").
  - *Missing:* the number of annotators, pay, consent, IRB, demographics and guidelines.
  - *Other problems:* 80% of items are single-rated; α = 0.61 is called "typical"; there are no per-language counts or tests; prompts were written by the annotators' own team leads, which raises an independence question.
  - *Fix:* reconcile the descriptions; add the full disclosure; add a per-language win/tie/loss table with tests; release the prompts and judgments.
  - *Owner skills:* acl-reproducibility, acl-experiments.
- **R3-M4: the data release is contradictory, with no licenses and no PII screening.**
  - *Where:* l.94 ("selected example identifiers") vs l.216 ("The selected examples will be released in full, including the human-written native-language examples").
  - *Fix:* specify the release scope; add a license and intended-use table; describe PII screening.
  - *Owner skills:* acl-artifact-evaluation, acl-reproducibility.
- **R3-M5: the method cannot be reimplemented from the text.**
  - *Gaps:*
    - the reward model is unnamed (l.64), and so is the 70B rater (l.82);
    - the English *c* is "set to the language mean", which makes z-scoring a constant undefined (l.61, l.67);
    - long-text handling for NLLB and LaBSE is not described;
    - the metric used on the 2,000 held-out instructions is undefined (l.79, l.198);
    - the optimizer, chat template and loss masking are missing;
    - evaluation details and MGSM decoding are missing;
    - the hardware and total compute are not given.
  - *Fix:* add a reproducibility appendix covering all of these.
  - *Owner skill:* acl-reproducibility.
- **R3-M6: claims that the paper's own evidence contradicts.**
  - *Where:*
    - l.129: the IFD claim;
    - l.212: the conclusion, against l.204;
    - l.216: the ethics statement points to an analysis of culturally specific removals that is not in l.201, while l.61 says the consistency score penalizes "untranslatable fragments".
  - *Fix:* Holm-correct the IFD comparison; scope the conclusion; run a real cultural-content analysis or correct the ethics statement.
  - *Owner skills:* acl-writing-style, acl-experiments.
- **R3-M7: both figures are placeholders** (l.153, l.192), and the 20% point is unreported.
  - *Fix:* render real figures.
  - *Owner skills:* acl-experiments, acl-camera-ready.

**Minor concerns.** The pool-size table; the seed-averaging definition; the aggregation note; the mid-tier drop; the tautology at l.159; the inspection protocol; standard deviations; whether 13B baseline subsets were recomputed; third-person citation of the prior work; checklist E.

**What would move me.**
- **To Findings:** fix M1–M5 with a clean contamination check.
- **To Main:** additionally, the IFD advantage survives correction and the method transfers beyond Llama 2.

---

## 3. Adversarial verification

The verifier read the full manuscript and tried to refute each major concern against the text. Verdicts follow.

| id | verdict | decisive line(s) | reason |
|---|---|---|---|
| R1-M1 | **kept** | l.17 "All evaluation sets were deduplicated against the training pool before filtering."; l.49 "remove overlapping examples before any filtering"; l.76 "We did not deduplicate the pool against the evaluation benchmarks … affect all filtering methods equally"; l.85 "held out from the pool" | There are three contradictory accounts. "Equally" fails because each filter keeps a different 30%. MGSM enrichment is a hypothesis, but a legitimate one. Cluster A. |
| R1-M2 | **kept** | l.17 "from 45.2 to 48.9"; l.32 "from 45.2 to 47.5"; l.113 XQF Avg 47.5; l.126 "47.5" | 48.9 appears nowhere else, and the gain is overstated by 60%. Cluster B. |
| R1-M3 | **kept** | l.88 "Holm–Bonferroni"; l.129 "without correction, XQF is significantly better in 7 languages; we therefore conclude … across all languages" | The conclusion contradicts its own evidence and drops the declared procedure. There are no tests against other baselines, at 13B, or for the ablations, and seed variance is collapsed. Cluster C. |
| R1-M4 | **kept** | l.159 "matches … once normalized"; "removed because raw … scores are lower"; l.67; l.179–180 | (a) The distributions match by construction. (b) The no-quota variant apparently also drops normalization, so the 1.2-point loss and the 37.4 are not isolated to the quota. Cluster I. |
| R1-M5 | **kept** | l.85 "Burmese only by XStoryCloze … Haitian Creole, Quechua and Tamil only by XCOPA"; l.133 (tier table only) | There are no per-language scores, and the benchmark-mix confound across tiers is never addressed. Cluster H. |
| R1-M6 | **kept** | l.82 "Every filter retains 30%"; "in its original language"; l.25 "least reliable"; l.198; l.201 "(34%)" | ρ is tuned only for XQF, AlpaGasus runs in the setting the paper calls least reliable, and language-ID and QE baselines are missing. The sub-claim about training hyperparameters fails, since they are shared (l.79). Cluster F. |
| R1-M7 | **downgraded** | l.188; l.170–180 (Avg only); l.126 "consistent with"; l.201 "(22%)" | Real, but these claims are secondary. The MGSM claim is hedged and partly supported by the 22% number-corruption rate. |
| R1-M8 | **kept** | l.91 "trained on XQF data and on the full pool"; "random 20% … annotated twice"; l.216 "crowdworkers"; l.162 (no counts) | There is no IFD arm, no test, no counts, no pay disclosure, and most items have a single rater. The two descriptions are in strong tension rather than a strict contradiction. Cluster E. |
| R1-M9 | **kept** | l.212; l.204 "32% … 41%"; "46.0" | Contradicted by the paper's own evidence. Easy to fix. Cluster D. |
| R2-M1 | **downgraded** | l.43; l.46 "established tools"; l.31; l.82 | The paper concedes both the prior quota (l.43) and the established tools (l.46). The uncited prior work is mostly an anonymity issue. Giving baselines the same quota is sound design. What remains is contribution framing, and the lineage argument relies on outside knowledge. |
| R2-M2 | **kept** | l.82; l.76 "281K machine-translated"; l.201 "34%" | Duplicate of R1-M6. The sub-claim about post-2024 methods is speculative. Cluster F. |
| R2-M3 | **kept** | l.17 "outperforming four filtering baselines … survive correction … 13 of 18"; l.129; l.212; l.204 | The 13/18 result is against the full pool only, yet sits next to the baseline claim. Duplicates R1-M2 and R1-M9. Clusters B and D. |
| R2-M4 | **kept** | l.129; l.91; l.112–113, l.119–120; l.141–142 | The margins of +1.4, +1.3 and +0.3 are confirmed, and the claim is unsupported. Cluster C. |
| R2-M5 | **kept** | l.17, l.49, l.76 | Duplicate of R1-M1. Cluster A. |
| R2-M6 | **kept** | l.79 "Llama 2 7B and 13B"; l.85 "rest on a single benchmark"; l.212 "any base model" | The evidence base is thin for the claim. "4 of 6 low-resource languages on a single benchmark" is confirmed. Partly answered: the human evaluation (l.91) covers open-ended prompts. The timeliness argument relies on outside knowledge. Clusters D and H. |
| R2-M7 | **downgraded** | l.64; l.216 "we report what XQF removes"; l.201; l.204 "41%" | The ethics-pointer gap is real. The homogenization harm is speculative, and l.204 points the other way. A missed theme opportunity is not a defect. Duplicate of R3-M6 (part). Cluster G. |
| R3-M1 | **kept** | l.17, l.49, l.76, l.85, l.32 | Duplicate of R1-M1. Cluster A. |
| R3-M2 | **kept** | l.17 vs l.32 and l.113 | Duplicate of R1-M2. Cluster B. |
| R3-M3 | **kept** | l.91 "Prompts were written … by the annotators' team leads"; "20%"; l.162 "α of 0.61, typical"; l.216 | The checklist-D gaps and the independence question are real. The 0.667 threshold comes from outside knowledge. Duplicate of R1-M8. Cluster E. |
| R3-M4 | **downgraded** | l.94 "selected example identifiers"; l.216 "released in full, including the human-written native-language examples" | The contradiction is real, and licenses and PII screening are missing. These are checklist and housekeeping items, not soundness. |
| R3-M5 | **kept** | l.64 (unnamed reward model); l.82 (unnamed 70B rater); l.61 "set c to the language mean" with z_ℓ(c) at l.67; l.79; l.198; l.207 | The core component is unnamed, and z-scoring a constant is undefined. Three sub-claims fail: l.85 does state the scoring; l.207 gives per-run hours; the circularity of ρ selection is speculative. |
| R3-M6 | **kept** | l.129; l.212 vs l.204; l.216 vs l.201; l.61 "untranslatable fragments" | Every sub-claim is real. Duplicates R1-M3, R1-M9 and R2-M7. Clusters C, D and G. |
| R3-M7 | **downgraded** | l.153 and l.192 placeholders; l.159 "38% … 47% … 3% … 11%"; l.198 sweep values | The key numbers are stated in the text. The only remaining issue is the missing 20% point, which is minor. |

**Tally:** 18 kept, 5 downgraded, 0 dropped, out of 23 concerns. The verifier's own summary said "19 kept / 24 concerns"; that is a counting slip, and the AE recount from the table gives 18 / 23.

**Duplicate clusters.**
- **A. Contamination contradiction:** R1-M1, R2-M5, R3-M1.
- **B. Abstract 48.9 and the headline:** R1-M2, R3-M2, R2-M3 (part).
- **C. IFD significance:** R1-M3, R2-M4, R3-M6 (part).
- **D. Conclusion overclaim:** R1-M9, R2-M3 (part), R3-M6 (part), R2-M6 (part).
- **E. Human evaluation and disclosure:** R1-M8, R3-M3, R2-M4 (part).
- **F. Missing or under-tuned baselines:** R1-M6, R2-M2.
- **G. Ethics pointer and cultural content:** R2-M7, R3-M6 (part).
- **H. Per-language results and single-benchmark tiers:** R1-M5, R2-M6 (part).
- **I. Quota ablation and novelty:** R1-M4, R2-M1 (part), R3-M7 (part).

**Arithmetic the verifier checked.**
- **Table 1:** all 12 averages recompute exactly.
- **XQF over IFD:** +1.4 at 7B, +1.3 at 13B, +0.3 in the high tier.
- **Low-tier gain:** +3.5, confirmed.
- **No-quota variant by tier:** −4.7 low, −0.8 mid, +0.3 high.
- **Two averaging schemes:** tier means (47.87, 45.63) differ from benchmark averages (47.5, 45.2), as expected because they weight languages and benchmarks differently.
- **Human evaluation:** the shares sum to 100%.
- **Human-written share:** 131K/412K = 31.8%.
- **Scoring-cost break-even:** 445 h ÷ 224 h ≈ 1.99 runs.
- **ρ sweep:** no 20% value is given.

---

## 4. AE synthesis

**【Venue】** ACL 2027, Main or Findings, via the ARR January 2027 cycle.
- Findings is judged on soundness and reproducibility; Main adds novelty and impact.
- Calibrated from ACL-Skills `official-source-map.md` (re-verified 2026-11-23), `acl-review-process` and `acl-experiments`.

**【Desk-screen】**
- **As submitted:** desk reject. Desk-reject risk is HIGH because of anonymity breaches (l.43 self-citation, l.218–219 Acknowledgments with lab, institution and grant, l.94 GitHub username) and the missing Limitations section. All of these are mechanical and fixable before January 4, 2027.
- **After the preflight fixes:** send out, with LOW desk-reject risk.

**Score pattern.**

| | Soundness | Excitement | Overall |
|---|---|---|---|
| R1 | 2 | 2.5 | 2.0 |
| R2 | 2.5 | 2 | 2.0 |
| R3 | 2.5 | 3 | 2.0 |

All three referees independently said "resubmit next cycle; Findings once fixed". The three highest-weight clusters (A, B, C) were each raised by all three referees, and all survived verification.

**【Decision band】** **Major revision.** In ARR terms that is Overall ≈ 2.0: resubmit, with a credible path to Findings (3.0) and an outside chance of Main.

- **Not reject:** the method is sensible, the main table is internally consistent (all averages recompute), and every decisive issue is fixable with analyses on existing checkpoints plus honest rewording.
- **Not minor:** a reader cannot currently tell whether the evaluation was contaminated, the abstract misreports the headline result, and the claimed superiority over the strongest baseline rests on an invalid test. As the paper stands, these three points fail the Findings soundness bar.

**【Decisive issues】**

1. **Contamination: contradictory statements and an untested differential-retention risk** (cluster A: R1-M1, R2-M5, R3-M1).
   - The abstract (l.17) and Related Work (l.49) say the pool was deduplicated against the evaluation sets. Setup (l.76) says it was not, and argues that overlap "affect[s] all filtering methods equally".
   - That argument does not hold for a selection method: XQF retains a different 30%, one biased toward cleanly translated items, and MGSM, XStoryCloze and XNLI are themselves translated.
   - **Fix (acl-experiments, then acl-writing-style):**
     1. Run the 13-gram overlap audit that l.49 describes, per benchmark and language.
     2. Report the overlap rate in the full pool and in each filter's selected subset.
     3. Rerun Table 1 on decontaminated data, or on the overlap-free evaluation items.
     4. Make l.17, l.49, l.76, l.85 and l.32 state the same, true procedure.
2. **The headline claims exceed the evidence** (clusters B, C, D: R1-M2, R1-M3, R1-M9, R2-M3, R2-M4, R3-M2, R3-M6).
   - The abstract's 48.9 should be 47.5.
   - "Significantly outperforms IFD across all languages" (l.129) rests on 7 uncorrected tests out of 18 and abandons the Holm procedure declared at l.88.
   - The abstract's "survive correction … 13 of 18" refers only to the comparison against the full pool.
   - The conclusion's "any language and any base model … human-written data unnecessary" (l.212) is contradicted by l.204.
   - **Fix (acl-writing-style for the text; acl-experiments for the tests):**
     1. Correct 48.9 to 47.5 and run a numbers-traceability pass.
     2. Holm-correct XQF against every baseline, at both 7B and 13B and for the ablation rows, using a seed-aware paired bootstrap.
     3. Report what survives, per tier, and replace "across all languages" with it.
     4. Attribute the 13/18 result to the full-pool comparison.
     5. Scope the conclusion to the tested setting: one model family, 18 languages covered by NLLB and LaBSE.
3. **The margin over the strongest practical alternatives is not established, and the quota ablation is confounded** (clusters F, I: R1-M6, R2-M2, R1-M4).
   - ρ was tuned for XQF only.
   - AlpaGasus is run in the original language, which the paper itself calls least reliable.
   - There is no language-ID filter, even though wrong-language responses are the top defect at 34%.
   - There is no source-side QE baseline.
   - The no-quota row apparently also drops normalization.
   - The quota-justification argument at l.159 is circular.
   - **Fix (acl-experiments):**
     1. Add baselines at the matched 30% per-language budget: language-ID plus heuristics, CometKiwi-style QE on (English source, translation), and the 70B rater applied to the English pivot.
     2. Sweep ρ for IFD and AlpaGasus as well.
     3. Add the row "per-language z-scores with a global threshold".
     4. Replace the l.159 argument with independent quality evidence on the globally removed low-resource examples.

**【Secondary issues】** These are kept, but they do not move the band on their own.

- **Human evaluation and annotator disclosure** (cluster E: R1-M8, R3-M3).
  - Setup describes "native-speaker annotators … team leads" (l.91); the Ethics Statement says "crowdworkers recruited on an online platform" (l.216).
  - Pay, consent, IRB, rater counts and demographics are missing, so checklist D cannot be answered truthfully. Incorrect checklist answers are desk-rejection grounds.
  - The only comparison is against the full pool, not IFD; there is no test; 80% of items have a single rater.
  - Owner skills: acl-reproducibility for the disclosure; acl-experiments for adding an IFD arm and a per-language sign test.
  - **This is the highest-priority secondary item.**
- **Reimplementability** (R3-M5).
  - The reward model and the 70B rater are unnamed, and the English *c*/z-score rule is undefined.
  - Long-text handling, the selection metric for ρ, and the training and evaluation protocol are missing, as are hardware and total compute.
  - Owner skill: acl-reproducibility, via an appendix.
- **Per-language reporting** (R1-M5, R2-M6).
  - There is no per-language × benchmark table.
  - The low-tier +3.5 rests on XCOPA and XStoryCloze for 4 of 6 languages.
  - Llama 2 is the only model family, and there is no automatic open-ended evaluation.
  - Owner skills: acl-experiments; acl-topic-selection for the case for timeliness.

**Downgraded items worth doing anyway:**
- Third-person citation of the prior quota work, and rewriting contributions 1 and 3 around the actual delta (R2-M1, acl-related-work).
- Reconciling the release scope, with a license and PII table (R3-M4, acl-artifact-evaluation).
- Making the ethics pointer at l.216 match l.201, ideally with a cultural-content analysis that would also engage the 2027 homogenization theme (R2-M7, acl-topic-selection).
- Per-tier ablation numbers and an MGSM number-corruption probe (R1-M7).
- Rendering real figures and adding the 20% ρ point (R3-M7, acl-camera-ready).

**【Author action plan】** Ordered so the decisive issues come first.

1. **Preflight FAILs, before anything else** (acl-submission).
   - Anonymize l.43 (third person), l.94 (an anonymous mirror) and l.218–219 (delete the Acknowledgments).
   - Add the Limitations section.
   - Resolve the "Appendix ??" marker, the unreferenced fig:rate, the uncited conneau2020xlmr, and the figure placeholders.
2. **Contamination audit and rerun** (acl-experiments), then unify the statements (acl-writing-style). *Decisive issue 1.*
3. **Statistics** (acl-experiments): a Holm-corrected, seed-aware paired bootstrap for XQF against each baseline, at 7B and 13B and for the ablations. Then rewrite l.17, l.32, l.129 and l.212 to match what survives (acl-writing-style). *Decisive issue 2.*
4. **Baselines and quota ablation** (acl-experiments): language ID, CometKiwi QE, the pivot rater, ρ sweeps per baseline, the "z-score + global threshold" row, and independent quality evidence for l.159. *Decisive issue 3.*
5. **Human evaluation**: reconcile the annotator descriptions; disclose recruitment, pay, consent, IRB and demographics (acl-reproducibility); add an IFD arm and per-language tests (acl-experiments).
6. **Reproducibility appendix** (acl-reproducibility) and a per-language × benchmark table (acl-experiments).
7. **For a Main-track bid:** one current multilingual base model, an open-ended multilingual instruction-following evaluation, and a cultural-content analysis of what XQF removes (acl-experiments, acl-topic-selection).

**【Calibration caveats】**
- This is a rehearsal, not a prediction of acceptance.
- The ARR form fields and scales come from `review-forms.md` (read 2026-11-23). The ACL source map marks the exact current form as 待核实 (not yet verified), so re-check the live form.
- Several concerns lean partly on the referees' outside knowledge rather than the text: CometKiwi, post-2024 selection methods, the Krippendorff 0.667 threshold, and the Bactrian-X license. The verifier discounted these sub-claims.
- Concerns were filed independently, so one defect was often filed by several referees. The 18 kept concerns collapse to about 8 underlying issues (clusters A–I).
- Real ARR panels vary. A reviewer with a strong engineering focus may weight the useful-and-cheap angle more and land at 2.5–3. The band would only move up if the contamination audit came back clean and the claims were scoped.

```json
{
  "configuration": "multi-agent",
  "venue": "ACL 2027 via ARR (January 2027 cycle)",
  "desk_screen": {"as_submitted": "desk reject (anonymity breaches l.43/l.94/l.218-219 + missing Limitations)", "desk_reject_risk_as_submitted": "high", "after_preflight_fixes": "send out", "desk_reject_risk_after_fixes": "low"},
  "referee_scores": {"R1": {"soundness": 2, "excitement": 2.5, "overall": 2.0}, "R2": {"soundness": 2.5, "excitement": 2, "overall": 2.0}, "R3": {"soundness": 2.5, "excitement": 3, "overall": 2.0}},
  "decision_band": "major revision",
  "decisive_issue_clusters": ["A: contamination contradiction (R1-M1,R2-M5,R3-M1)", "B+C+D: headline claims exceed evidence - abstract 48.9, uncorrected IFD significance, conclusion overclaim (R1-M2,R1-M3,R1-M9,R2-M3,R2-M4,R3-M2,R3-M6)", "F+I: missing/under-tuned baselines and confounded quota ablation (R1-M6,R2-M2,R1-M4)"],
  "kept_major_concerns": [
    {"id": "R1-M1", "lens": "soundness/evaluation", "location": "Abstract l.17; Related Work l.49; Setup 'Contamination check' l.76; l.85", "concern": "Contamination statements contradict each other (deduplicated vs 'We did not deduplicate'); the 'affects all filtering methods equally' argument is invalid for a selection method that may retain translated benchmark items differentially."},
    {"id": "R1-M2", "lens": "soundness/evaluation", "location": "Abstract l.17 vs Intro l.32 vs Table tab:main l.113", "concern": "Abstract reports 7B average 45.2 -> 48.9; the body and Table 1 give 47.5; 48.9 is untraceable and overstates the gain by ~60%."},
    {"id": "R1-M3", "lens": "soundness/evaluation", "location": "Statistical testing l.88; Results 'Significance' l.129", "concern": "'Significantly outperforms IFD across all languages' rests on 7/18 uncorrected tests and abandons the declared Holm procedure; no tests vs other baselines, at 13B, or for ablations; seed variance collapsed."},
    {"id": "R1-M4", "lens": "soundness/evaluation", "location": "Method l.67; 'Why a quota is needed' l.159; Table tab:ablation l.180; Table tab:tiers l.143; l.188", "concern": "Quota justification is circular (z-scored distributions match by construction) and the no-quota ablation appears to also drop per-language normalization, so the quota's effect is not isolated."},
    {"id": "R1-M5", "lens": "soundness/evaluation", "location": "Evaluation l.85; Table tab:tiers; Abstract '+3.5'", "concern": "No per-language results; cross-tier gains are confounded by benchmark mix (low tier mostly XCOPA/XStoryCloze-only)."},
    {"id": "R1-M6", "lens": "soundness/evaluation", "location": "Baselines l.82; l.198; l.201; l.25", "concern": "Baselines not tuned with equal care: rho tuned only for XQF; AlpaGasus run in original language the paper calls least reliable; no language-ID or QE baseline despite 34% wrong-language defects."},
    {"id": "R1-M8", "lens": "soundness/evaluation", "location": "Human evaluation l.91, l.162; Ethics l.216", "concern": "Human eval compares only to the full pool (not IFD), has no significance test or per-language counts, 80% single-rated, pay missing, and annotator descriptions (native speakers/team leads vs crowdworkers) conflict."},
    {"id": "R1-M9", "lens": "soundness/evaluation", "location": "Conclusion l.212 vs Analysis l.204", "concern": "Conclusion claims XQF improves 'any language and any base model' and makes human-written data 'unnecessary'; one model family tested and l.204 shows XQF up-weights human data (32%->41%), human-only reaches 46.0."},
    {"id": "R2-M2", "lens": "novelty/contribution", "location": "Baselines l.82; l.27; l.76; l.201", "concern": "Closest cheap baselines absent: source-side reference-free QE on the 281K translated items, language-ID filter, AlpaGasus on the English pivot, per-method budget tuning."},
    {"id": "R2-M3", "lens": "novelty/contribution", "location": "Abstract l.17; l.32; Table 1; Conclusion l.212; l.204", "concern": "Headline claims exceed evidence: 48.9 vs 47.5; abstract juxtaposes '13 of 18 survive correction' (vs full pool only) with 'outperforming four baselines'; conclusion overclaims."},
    {"id": "R2-M4", "lens": "novelty/contribution", "location": "Results 'Significance' l.129; Human eval l.91, l.162", "concern": "'Outperforms IFD' unsupported statistically (7/18 uncorrected) and by human eval (full pool only); margins are small (+1.4/+1.3; +0.3 high tier)."},
    {"id": "R2-M5", "lens": "novelty/contribution", "location": "Abstract l.17; l.49; l.76", "concern": "Contradictory contamination statements; differential retention could explain part of the delta over baselines (dup of R1-M1)."},
    {"id": "R2-M6", "lens": "novelty/contribution", "location": "Models l.79; Evaluation l.85; Table tab:tiers", "concern": "Only Llama 2 (2023) at ACL 2027; classification/math benchmarks for an instruction-tuning claim; 4 of 6 low-resource languages rest on a single benchmark."},
    {"id": "R3-M1", "lens": "clarity/reproducibility/ethics", "location": "Abstract l.17; l.49; l.76; l.85; l.32", "concern": "Three mutually contradictory accounts of decontamination; 'held out' unverified; checklist-C misleading-answer risk (dup of R1-M1)."},
    {"id": "R3-M2", "lens": "clarity/reproducibility/ethics", "location": "Abstract l.17 vs l.32 vs Table 1 l.113", "concern": "Abstract 7B number 48.9 not traceable to the body (dup of R1-M2)."},
    {"id": "R3-M3", "lens": "clarity/reproducibility/ethics", "location": "Human evaluation l.91, l.162; Ethics l.216", "concern": "Annotator descriptions contradict; no pay, consent, IRB, annotator count, demographics or guidelines (Responsible NLP checklist D unanswerable); 80% single-rated; no per-language tests; prompt authorship by annotators' team leads."},
    {"id": "R3-M5", "lens": "clarity/reproducibility/ethics", "location": "Method l.61-67; Setup l.79, l.82; l.198; l.207", "concern": "Not reimplementable: reward model and 70B rater unnamed; English c 'set to the language mean' makes z-scoring undefined; long-text handling, rho-selection metric, optimizer/template/loss masking, hardware/total compute missing."},
    {"id": "R3-M6", "lens": "clarity/reproducibility/ethics", "location": "l.129; Conclusion l.212 vs l.204; Ethics l.216 vs l.201, l.61", "concern": "Claims contradicted by the paper's own evidence: uncorrected IFD claim, conclusion overclaim, and an ethics statement pointing to a culturally-specific-content analysis that l.201 does not contain."}
  ],
  "downgraded": [
    {"id": "R1-M7", "lens": "soundness/evaluation", "location": "Ablations l.188; Main results l.126", "concern": "Per-tier mechanism claims lack per-tier ablation numbers; MGSM/number-corruption mechanism untested.", "reason": "Real but secondary; MGSM claim is hedged and partly supported by the 22% number-corruption rate at l.201."},
    {"id": "R2-M1", "lens": "novelty/contribution", "location": "Related Work l.43, l.46; Contributions l.31, l.33", "concern": "Per-language quota is the authors' own uncited prior work presented as contribution 3; consistency filtering is established practice.", "reason": "Paper concedes both at l.43/l.46; uncited prior work is mainly the anonymity (preflight) issue; shared quota across baselines is sound design; residue is contribution framing plus outside-knowledge lineage."},
    {"id": "R2-M7", "lens": "novelty/contribution", "location": "Pivot quality l.64; Ethics l.216; l.201", "concern": "English HH-RLHF reward model on pivots imposes English-centric norms; ethics statement points to a cultural-content analysis that does not exist; theme opportunity missed.", "reason": "Ethics-pointer gap is real (dup of R3-M6 part) but the homogenization harm is speculative (l.204 shows native data up-weighted) and a missed theme opportunity is not a defect."},
    {"id": "R3-M4", "lens": "clarity/reproducibility/ethics", "location": "Code and data l.94; Ethics l.216", "concern": "Release scope contradictory (identifiers vs 'released in full'); no licenses or PII screening (checklist B).", "reason": "Real, but a checklist/housekeeping item rather than a soundness issue."},
    {"id": "R3-M7", "lens": "clarity/reproducibility/ethics", "location": "Fig. fig:retention l.153-154; Fig. fig:rate l.192-193; l.198", "concern": "Both figures are placeholders; 20% retention point unreported.", "reason": "Key numbers are stated in the text (l.159, l.198); residual is the missing 20% point and draft rendering, which are minor."}
  ],
  "dropped": []
}
```
