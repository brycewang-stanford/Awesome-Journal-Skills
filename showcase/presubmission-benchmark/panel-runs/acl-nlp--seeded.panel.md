# Simulated referee panel — agent4-paperB.tex

**Inline panel** (one agent playing AE → R1 → R2 → R3 → verifier → AE in sequence; each
referee report was written before moving to the next lens, but the referees are not truly
independent). This is a rehearsal. It predicts where the paper will be attacked and a likely
decision band. It does not replace peer review or predict acceptance.

Paper: *Keep the Consistent Ones: Cross-Lingual Quality Filtering for Multilingual Instruction
Tuning* (XQF). The score is round-trip (NLLB → English → NLLB) LaBSE consistency plus an English
reward-model score on the pivot, each z-scored within language, with a fixed 30% quota per
language. The pool is 412K examples in 18 languages (Aya + Bactrian-X). Models are Llama 2 7B/13B
with three seeds. Evaluation uses XCOPA, XStoryCloze, XNLI and MGSM, plus a pairwise human
evaluation in six languages.

---

## 【Venue / family】 ACL 2027 via ACL Rolling Review / form B (ARR review form) — calibrated 2026-11-23

Calibration sources: `ACL-Skills/resources/official-source-map.md` (ARR CFP, sustainable
reviewing, Responsible NLP checklist and ACL 2027 call re-verified 2026-11-23);
`acl-review-process`, `acl-experiments`, `acl-related-work`, `acl-reproducibility`,
`acl-submission`; `review-forms.md` §B.

- Route: **ARR January 2027 cycle (submission January 4, 2027 AoE)**, then commitment to ACL
  2027. The commitment date is still TBA. Papers not selected for the main conference are
  automatically considered for **Findings of ACL** (ACL 2027 call, row 4c).
- Form B fields: Soundness (1–5, half-points) · Excitement (1–5) · **Overall: 5 Award ·
  4 Conference · 3 Findings · 2 Resubmit next cycle · 1.5 Resubmit after next cycle · 1 Do
  not resubmit** · Confidence. Findings is judged mainly on soundness and reproducibility.
  Conference also requires novelty and impact.
- What ARR reviewers attack (`acl-experiments`): contamination reasoning, significance testing
  applied only to the comparison that wins, averaging over languages that hides regressions,
  claimed language coverage, tuned current-LLM context, human evaluation with agreement and pay
  reported, and checklist-to-paper consistency (`acl-reproducibility`).
- ACL 2027 theme track: "Homogenization and knowledge collapse in LLMs". The paper is not
  submitted to it; noted only for context.

**Preflight (stage 0): verdict NO-GO.** FAILs: **ANON-SELFCITE** (line 43, "In our previous
work"), **ANON-ACK** (line 218, lab name and grant number), **ANON-URL** (line 94, personal
GitHub), **STMT-MISSING Limitations**, **LEFTOVER-MARKER** ("Appendix ??", line 85). FLAGs:
uncited `conneau2020xlmr`; Figure `fig:rate` never referenced. INFO: Responsible NLP checklist
not in the file. Under the ARR CFP, a missing Limitations section or a de-anonymized PDF is
**desk-rejected at intake**. The panel treats these as stage-0 fixes and does not count them as
substantive weaknesses, except where a mechanical item also has substantive content (the prior
work behind the self-citation, R2-M1).

---

## 【Desk-screen (AE)】 **As submitted: desk reject (mechanics). After stage-0 fixes: send out.** Desk-reject risk: **high** as is, **low** once the preflight FAILs are fixed

- **Scope / fit.** Multilingual instruction-data selection is squarely in ACL scope and relevant
  to low-resource NLP.
- **Fatal-flaw scan (substantive).** Two red flags need referees:
  1. **Contamination statement contradicts itself.** The abstract says "All evaluation sets were
     deduplicated against the training pool before filtering". §4 "Contamination check" says "We
     did not deduplicate the pool against the evaluation benchmarks".
  2. **Significance inference against the strongest baseline.** §5 concludes "XQF significantly
     outperforms IFD across all languages" from 7 of 18 *uncorrected* tests.

  Neither is a desk-reject reason under ARR (which desk-rejects on policy, not merit), but either
  could sink the review package.
- **Delta vs. closest work.** Round-trip consistency combined with pivot quality is a plausible
  delta. The per-language quota is attributed to the authors' own prior paper (§2 ¶2), so the AE
  sends the novelty split to R2.

---

## 【Referee 1 — soundness / evaluation】

**Form B**
- *Paper Summary.* XQF filters a translated-heavy multilingual instruction pool by round-trip
  consistency and English-pivot reward, both normalized within language, keeping 30% per
  language. It reports +2.3 (7B) and +2.2 (13B) average points over the full pool, beats four
  filters at equal budget, and shows its largest gains on low-resource languages.
- *Summary of Strengths.* Three seeds with SDs in Table 1. All baselines get the same
  per-language quota, which is fair and isolates the scoring function. Random < full pool rules
  out a pure "less data" effect. Holm–Bonferroni is used for the full-pool comparison. The
  ablations isolate each component (Table 3). The human evaluation is blind and reports α = 0.61.
- *Summary of Weaknesses* (decision-changing first): contamination handling is contradicted
  within the paper (M1). The claim of superiority over IFD rests on an invalid multiple-testing
  inference (M2). Claimed language coverage fails for at least one low-resource language, which
  undercuts the tier result (M3). The abstract headline number does not match the paper (M4).
- *Soundness* **2** · *Excitement* **2.5** · *Overall* **2 (Resubmit next cycle)** ·
  *Confidence* **4**.
- *Reproducibility:* partial (unnamed 70B rater and reward model; single zero-shot template).
  *Ethics:* human evaluation pay and consent are not reported.

**Referee template**
- 【Lens】 soundness / evaluation
- 【One-line summary】 A sensible filter whose headline evidence has three integrity problems:
  contamination, multiple testing and language coverage.
- 【Recommendation】 reject in the current form (resubmit next cycle)
- 【Major concerns】
  - **R1-M1 — Contamination: the paper contradicts itself, and the "affects all methods
    equally" assumption is untested.** *Where:* Abstract ("All evaluation sets were deduplicated
    against the training pool before filtering"); §2 "Evaluation contamination" ("we measure
    n-gram overlap ... and remove overlapping examples before any filtering is applied"); §4
    "Contamination check" ("We did not deduplicate the pool against the evaluation benchmarks
    ... we expect any such overlap to be small and to affect all filtering methods equally").
    *Why it matters:* the four benchmarks are themselves translations of English NLP data (COPA,
    StoryCloze, MNLI, GSM8K), and the pool is mostly translations of English collections. A
    filter that keeps examples which round-trip cleanly can retain translated benchmark-like
    items *at a different rate* than random or IFD selection. The largest gain is on MGSM (§5,
    15.0 → 18.3), which is where GSM8K-style leakage would show up. *Fix:* run the 13-gram
    overlap scan the paper describes, report overlap counts per benchmark and per filter
    selection, retrain on the decontaminated pool (or show that overlap is zero), and correct
    the abstract. *Owner:* `acl-experiments` (contamination and validity controls) +
    `acl-reproducibility` (contamination auditing).
  - **R1-M2 — "Significantly outperforms IFD across all languages" rests on uncorrected tests
    significant in 7 of 18 languages.** *Where:* §5 "Significance" ("running a separate paired
    bootstrap test at p < 0.05 in each of the 18 languages without correction, XQF is
    significantly better in 7 languages; we therefore conclude that XQF significantly
    outperforms IFD across all languages"); compare §4 "Statistical testing" (Holm–Bonferroni
    across 18 languages). *Why:* it abandons the paper's own correction protocol for exactly the
    comparison that matters for a Conference claim (`acl-experiments`: "Running the significance
    test only on the comparison that wins"). It also infers "all languages" from 7 of 18. The
    tier table shows XQF ≈ IFD in high-resource languages (53.9 vs. 53.6). *Fix:* apply Holm to
    the IFD comparison and report the corrected count. Restate the claim as "significantly
    better in k languages (concentrated in mid/low tiers), never worse", or add a pooled
    item-level test across languages. *Owner:* `acl-experiments` (statistical floor).
  - **R1-M3 — Claimed language coverage is false for Yoruba, and the low-resource tier rests on
    thin coverage.** *Where:* §4 "Evaluation" ("Each of our 18 languages is covered by at least
    one benchmark (per-language coverage is listed in Appendix ??)"); Table 2 caption ("Each
    language's score is the mean over the benchmarks covering it; tiers average six languages
    each"); §5 "Significance" (13 of 18). *Why:* none of XCOPA, XStoryCloze, XNLI or MGSM
    includes Yoruba, so the low-resource tier average and the 18-language significance count
    include a language with no evaluation items. Haitian Creole, Quechua and Tamil appear only in
    XCOPA, so the headline "+3.5 low-resource" rests mostly on one 500-item-per-language
    benchmark and a two-benchmark Swahili/Telugu signal. *Fix:* publish the per-language coverage
    table. Add a Yoruba benchmark (e.g., a Belebele- or AfriXNLI-style set) or drop Yoruba from
    the automatic-evaluation claims. Report the tier averages over the languages actually
    covered, with per-language rows. *Owner:* `acl-experiments` (evaluation design: breadth must
    match the claim).
  - **R1-M4 — The abstract's 7B headline number does not match the paper.** *Where:* Abstract
    ("improves the average held-out score of Llama 2 7B from 45.2 to 48.9"); §1 contribution 2
    and Table 1 report **47.5**. *Why:* the abstract states a 3.7-point gain where the paper
    shows 2.3, about 60% larger, in the sentence most readers rely on. *Fix:* correct it to 47.5
    and re-check every abstract number against the tables. *Owner:* `acl-writing-style`.
  - **R1-M5 — The argument that removed low-resource examples "are not worse" is circular.**
    *Where:* §5 "Why a quota is needed" ("their within-language score distribution matches that
    of the retained high-resource examples once normalized"). *Why:* z-scored distributions
    have mean 0 and SD 1 in every language by construction. *Fix:* use an independent quality
    signal, such as a human sample of globally removed low-resource examples. *Owner:*
    `acl-experiments`.
- 【Minor concerns】 A single fixed zero-shot template, with no prompt-paraphrase sensitivity
  (`acl-experiments` statistical floor for prompted results). Baselines are run only at XQF's
  optimal ρ = 0.3. The "held-out pool instructions" criterion for choosing ρ is not defined. The
  human evaluation compares against the full pool, not IFD, and gives no per-language test. The
  MGSM explanation ("consistency score detects corrupted numbers") is asserted, not shown.
- 【What would move me to Findings / Conference】 M1–M3 resolved with the gains intact after
  decontamination and corrected testing.

---

## 【Referee 2 — novelty / excitement / positioning】

**Form B**
- *Paper Summary.* As R1. This review asks what is new relative to English data selection, the
  authors' own per-language-quota work, and translation quality estimation.
- *Summary of Strengths.* A real practical problem: most multilingual instruction data is
  translated. Using an English pivot to make a single reward model usable across languages is a
  neat idea. The finding that XQF shifts the mix toward human-written data without being told
  which examples are translated (41% vs. 32%) is interesting. Cost is discussed concretely.
- *Summary of Weaknesses.* Much of the "quota is necessary" contribution comes from the authors'
  prior work (M1). The consistency score is never compared with standard translation QE (M2).
  The model set is dated for ACL 2027 (M3).
- *Soundness* **2.5** · *Excitement* **2.5** · *Overall* **2.5** (between Resubmit and
  Findings) · *Confidence* **4**.

**Referee template**
- 【Lens】 novelty / excitement / positioning
- 【One-line summary】 The round-trip + pivot scorer is the new part. The quota is not, and the
  scorer is not compared with the QE methods it effectively replaces.
- 【Recommendation】 major (resubmit next cycle)
- 【Major concerns】
  - **R2-M1 — The per-language quota and the global-threshold failure are prior work, but the
    paper presents them as contributions.** *Where:* §2 ¶2 ("we showed that a single global
    quality threshold removes low-resource languages disproportionately from translated corpora
    and proposed per-language quotas; here we extend our own approach"); §1 contribution 3 ("the
    per-language quota is necessary for this"); §1 ¶2 and §5 "Why a quota is needed". *Why it
    matters:* once the quota is credited to prior work, the delta reduces to the scoring function.
    The Conference-vs-Findings judgment then depends on whether that scorer is better than
    alternatives (see M2). If the cited workshop is archival, ARR's dual-submission and
    10%-text-reuse rules also apply. *Fix:* rewrite the contribution list so the quota is
    inherited (cited in the third person, as the preflight requires) and the new contributions
    are round-trip consistency and pivot scoring plus the analysis. Declare the workshop's
    archival status. *Owner:* `acl-related-work` (self-citation and overlap declarations).
  - **R2-M2 — No translation-quality-estimation baseline; the QE lane is uncited.** *Where:* §2
    "Translation quality estimation" ("Round-trip translation and multilingual sentence
    embeddings are established tools ...", with no citation); §4 "Baselines" (random,
    perplexity, AlpaGasus-style, IFD). *Why:* the consistency component is a reference-free QE
    proxy. The obvious competitor is a standard QE model (e.g., COMET-Kiwi-style) applied to
    instruction/response pairs. For the 281K Bactrian-X examples, the English source exists, so
    source-side QE needs no round trip. Without that comparison, the claim that round-trip
    consistency is the right signal is untested. *Fix:* add a QE-filter baseline at the same
    quota, cite the QE literature, and explain when round-trip is preferable (e.g., Aya
    human-written data with no English source). *Owner:* `acl-related-work` + `acl-experiments`
    (baselines).
  - **R2-M3 — Only Llama 2 (2023) base models for an ACL 2027 submission.** *Where:* §4 "Models
    and training". *Why:* `acl-experiments` "does this matter now?". Current multilingual base
    models may be less sensitive to translation noise. *Fix:* add one current multilingual base
    model at 7–8B, or scope the claim and say so in Limitations. *Owner:* `acl-experiments`.
- 【Minor concerns】 Related work stops at 2024. Add a freshness sweep of 2024–2026 multilingual
  data-selection and translated-instruction work (`acl-related-work` freshness pressure). The
  AlpaGasus-style baseline rates in the original language, while XQF rates the English pivot;
  the "quality only" ablation partly covers this, so say so. The ethics statement's diversity
  concern (removing culturally specific material) is not measured.
- 【What would move me to Findings / Conference】 Findings: M1 rewrite plus R1's fixes.
  Conference: XQF also beats a QE baseline and holds on a current model.

---

## 【Referee 3 — clarity / reproducibility / ethics】

**Form B**
- *Paper Summary.* As above. This review focuses on whether the Responsible NLP checklist could
  be answered truthfully and whether the claims stay within the evidence.
- *Summary of Strengths.* Compute figures for scoring and training are given, and the breakeven
  arithmetic checks out (445 h scoring vs. 0.7 × 320 h saved per 7B run ≈ 2 runs). The defect
  taxonomy of the bottom decile (§6) is concrete. Selected IDs and scripts are promised.
- *Summary of Weaknesses.* The conclusion overclaims beyond, and against, the paper's own
  evidence (M1). Human-evaluation reporting is incomplete for checklist section D (M2). Key
  models are unnamed and data licensing is not stated (M3).
- *Soundness* **2.5** · *Excitement* **3** · *Overall* **2.5** · *Confidence* **3**.
- *Ethical concerns:* yes, minor. Crowdworker pay and consent are not reported, and native-language
  human-written data is to be redistributed with no license statement.

**Referee template**
- 【Lens】 clarity / reproducibility / ethics
- 【One-line summary】 A reasonably documented pipeline, but the conclusion and the
  human-evaluation reporting would not pass a checklist-consistency read.
- 【Recommendation】 major
- 【Major concerns】
  - **R3-M1 — The conclusion makes a universal claim that the paper's own results contradict.**
    *Where:* §7 ("Because XQF is language-agnostic, it will improve instruction tuning for any
    language and any base model, and it makes the collection of human-written multilingual
    instruction data unnecessary"). *Contradicting evidence:* §6 "Human-written versus translated
    data" (XQF raises human-written data from 32% to 41% of the selection; the human-only subset
    beats the full pool, 46.0 vs. 45.2); the experiments cover two models of one family and 18
    languages (§4); Yoruba has no benchmark (R1-M3). *Why:* ARR soundness asks whether the claims
    are supported. This one is not, and it argues against collecting the very data the paper
    shows to be valuable. *Fix:* delete it and scope the conclusion to the tested models,
    languages and pool composition. Put the scope limits in the (currently missing) Limitations
    section. *Owner:* `acl-writing-style` (claims calibration) + `acl-submission` (Limitations).
  - **R3-M2 — Human-evaluation reporting is incomplete and internally inconsistent.** *Where:* §4
    "Human evaluation" ("native-speaker annotators ... Prompts were written ... by the
    annotators' team leads") vs. Ethics ("crowdworkers recruited on an online platform"). No pay,
    consent, IRB status, rater count per language, or per-language result. *Why:* Responsible NLP
    checklist section D, where misleading answers are desk-rejectable. *Fix:* report the
    recruitment channel, pay, consent and ethics review, raters per item, and per-language
    preferences with CIs. *Owner:* `acl-reproducibility` (checklist D).
  - **R3-M3 — Reproducibility gaps in the scoring models and in data licensing.** *Where:* §3.2
    ("a 1.3B-parameter reward model trained on public English helpfulness preference data", not
    named); §4 "Baselines" ("an open 70B chat model", not named); §4 "Evaluation" (template not
    given). Ethics says "selected examples will be released in full", while §4 says "selected
    example identifiers". Aya and Bactrian-X licenses are not stated. *Fix:* name model versions,
    give the prompts and decoding settings verbatim (`acl-reproducibility` prompt-disclosure
    block), resolve the release statement, and state licenses (checklist B). *Owner:*
    `acl-reproducibility`.
- 【Minor concerns】 The 300-example defect inspection (§6) gives no annotator or agreement
  information. The length-correlation statement (r = 0.08) should give n and the method.
  "Krippendorff's α 0.61, typical" needs a citation for "typical".

---

## 【Verification】 (verifier tries to refute each major concern against the text)

| ID | Verdict | Evidence / reason |
|---|---|---|
| R1-M1 | **kept** | Real: abstract, "All evaluation sets were deduplicated against the training pool before filtering"; §2, "we ... remove overlapping examples before any filtering is applied"; §4, "We did not deduplicate the pool against the evaluation benchmarks". No other passage reconciles these. Specific: three locations and a differential-selection mechanism. Addressable: run the scan and retrain. **Decisive**, because it decides whether the reported gains can be trusted at all. |
| R1-M2 | **kept** | Real: §5, "without correction, XQF is significantly better in 7 languages; we therefore conclude that XQF significantly outperforms IFD across all languages", against the §4 Holm protocol. Specific and addressable (reanalysis only). **Decisive** for the claim over the strongest baseline. |
| R1-M3 | **kept** | Real: §4 asserts full coverage but points to "Appendix ??". The text has nothing that refutes the concern, and the public language lists of XCOPA (11), XStoryCloze (11), XNLI (15) and MGSM (11) do not include Yoruba. Table 2's "tiers average six languages each" therefore cannot hold for the low tier as described. Addressable. **Decisive** for the low-resource headline (+3.5), which is the paper's main selling point. |
| R1-M4 | **kept** (not decisive) | Real: abstract "45.2 to 48.9" vs. §1 "45.2 to 47.5" and Table 1 XQF 7B Avg = 47.5 (recomputed: (60.4+63.5+47.8+18.3)/4 = 47.5). Trivial to fix, but it misstates the headline result and so counts as a soundness item, not a typo. |
| R1-M5 | **downgraded → minor** | Real (z-normalized distributions match by construction). It supports the quota motivation only, and the quota's value is shown independently by Table 2 and Table 3 (no-quota rows). |
| R2-M1 | **kept** | Real: §2 ¶2, "In our previous work ... proposed per-language quotas; here we extend our own approach". Contribution 3 and §5 "Why a quota is needed" still present quota necessity as a finding of this paper. Distinct from the preflight ANON-SELFCITE (that covers the voice; this covers contribution overlap). Addressable by rewriting the contributions. |
| R2-M2 | **kept** | Real: §2 QE paragraph has no citation; §4 baselines contain no QE filter. Specific (the mechanism is source-side QE on Bactrian-X, which has English originals). Addressable. Decides Conference vs. Findings more than reject vs. Findings. |
| R2-M3 | **downgraded → minor** | Real (§4: Llama 2 7B/13B only). It limits scope but does not invalidate the comparison among filters on the models tested; a Limitations statement is an acceptable remedy. |
| R3-M1 | **kept** (not decisive) | Real: §7 quote above. It is contradicted by §6 (41% human-written in the selection; human-only 46.0 > full pool 45.2) and by the two-model scope. The fix is easy (delete or scope), but an unsupported universal claim counts against ARR soundness. |
| R3-M2 | **downgraded → minor** | Real (inconsistent recruitment description; pay and consent missing). This is a reporting and checklist-D fix that does not change any result. It becomes a desk-reject risk only if the checklist is answered inconsistently, so keep it on the action list. |
| R3-M3 | **downgraded → minor** | Real (unnamed reward model and 70B rater; release wording mismatch; no licenses). Reproducibility documentation that can be fixed without new experiments. |

**Summary:** 11 major concerns → **kept 7** (R1-M1, R1-M2, R1-M3, R1-M4, R2-M1, R2-M2,
R3-M1) · **downgraded 4** (R1-M5, R2-M3, R3-M2, R3-M3) · **dropped 0**.

---

## 【Referee forms】
- **R1** (soundness/evaluation): Soundness 2 · Excitement 2.5 · Overall 2 (Resubmit next cycle) · Conf 4
- **R2** (novelty/excitement): Soundness 2.5 · Excitement 2.5 · Overall 2.5 · Conf 4
- **R3** (clarity/reproducibility/ethics): Soundness 2.5 · Excitement 3 · Overall 2.5 · Conf 3

## 【Decision band】 **Resubmit next cycle** (ARR Overall ≈ 2–2.5; below the Findings bar as submitted). As submitted with the preflight FAILs, it would be **desk-rejected** at ARR intake.

Package reading (`acl-review-process`): the meta-review would very likely endorse R1-M1 and
R1-M2. A package with "one detailed negative review and a meta-review that endorses the
objection rarely survives commitment". The designed path is to fix the problems and resubmit in
a later cycle, not to commit this package to ACL 2027. If the January 4, 2027 deadline is the
target, the decisive fixes are reanalysis plus one decontaminated retraining. That is feasible,
but only if the retraining runs before the deadline.

## 【Decisive issues (1–3)】
1. **Contamination contradiction (R1-M1).** *Location:* Abstract vs. §2 "Evaluation
   contamination" vs. §4 "Contamination check". *Why it decides:* the paper states both that it
   deduplicated and that it did not. The untested "affects all methods equally" assumption is
   exactly what a selective filter can break, especially on MGSM, where the largest gain sits.
   *Owner:* `acl-experiments` + `acl-reproducibility`. *Fix:* n-gram overlap scan of the pool
   against all four benchmarks (all languages and the English sources). Report overlap per
   filter's selected subset, remove the overlap, retrain at least the 7B main conditions, and
   make the abstract, §2 and §4 agree.
2. **Invalid significance claim over IFD (R1-M2).** *Location:* §5 "Significance". *Why it
   decides:* beating the strongest baseline is the paper's claim to more than Findings, and the
   inference drops the paper's own Holm protocol. *Owner:* `acl-experiments`. *Fix:*
   Holm-corrected per-language bootstrap against IFD plus a pooled test. Restate the claim as
   the corrected count and the tiers where it holds.
3. **Evaluation coverage behind the low-resource headline (R1-M3).** *Location:* §4
   "Evaluation" ("Appendix ??"); Table 2; abstract "+3.5". *Why it decides:* Yoruba has no
   benchmark, three other low-resource languages have only XCOPA, and the paper's main selling
   point is low-resource gains. *Owner:* `acl-experiments`. *Fix:* per-language coverage table,
   a Yoruba evaluation set (or drop Yoruba from the automatic-evaluation claims), and tier
   averages recomputed over the languages actually covered.

## 【Secondary issues】
- Abstract 7B number 48.9 → 47.5 (R1-M4; `acl-writing-style`).
- Quota credited to prior work; contributions rewritten; workshop archival status declared (R2-M1; `acl-related-work`).
- QE baseline and QE citations (R2-M2; `acl-related-work` + `acl-experiments`). This is the issue that separates Findings from Conference after the decisive fixes.
- Scope the §7 conclusion; move the limits into the required Limitations section (R3-M1; `acl-writing-style`, `acl-submission`).
- Human-evaluation reporting: pay, consent, recruitment, per-language CIs (R3-M2; `acl-reproducibility` checklist D).
- Named reward and rater models, verbatim prompts and templates, licenses, release-statement consistency (R3-M3; `acl-reproducibility` checklist B/C).
- Circular "not worse" argument (R1-M5); current-model row or scope statement (R2-M3); prompt-template sensitivity; baselines at other ρ.

## 【Author action plan】 (ordered)
0. **Stage-0 mechanics first (preflight NO-GO):** third-person self-citation, remove the acknowledgments and grant, use an anonymized code mirror (anonymous.4open.science), **add a substantive Limitations section**, fill "Appendix ??", cite or remove `conneau2020xlmr`, reference Figure `fig:rate`, complete the Responsible NLP checklist (`acl-submission`, `acl-reproducibility`). Any one of the first four is an ARR desk reject.
1. **Decontaminate and retrain** (D1) → `acl-experiments` / `acl-reproducibility`: overlap scan → per-filter overlap table → retrain 7B conditions → fix abstract, §2 and §4.
2. **Reanalyse significance** (D2) → `acl-experiments`: Holm against IFD, pooled test, restated claim.
3. **Fix evaluation coverage** (D3) → `acl-experiments`: coverage table, Yoruba set or exclusion, recomputed tiers.
4. **Claims hygiene** → `acl-writing-style`: abstract number, conclusion scope, contribution list (quota → prior work).
5. **Strengthen the Conference case** → `acl-related-work` + `acl-experiments`: QE-filter baseline; optionally one current multilingual base model.
6. **Checklist consistency sweep** → `acl-reproducibility`: sections B (licenses), C (models, prompts, compute), D (human evaluation), E (AI assistance, currently not stated at all).
7. Rerun preflight and this panel before the ARR January 4, 2027 deadline. If D1's retraining cannot finish in time, target a later cycle rather than submitting a package that will carry R1-M1 into commitment.

## 【Calibration caveats】
- This was an inline panel. The referees were played in sequence by one agent, so some anchoring is possible.
- R1-M3 relies on the public language lists of the four benchmarks (external fact) because the paper's coverage appendix is a placeholder. If the authors evaluate Yoruba on a fifth set not mentioned in the text, the concern narrows to "undisclosed benchmark".
- The ARR form fields follow `review-forms.md` §B, read 2026-11-23. The pack marks the exact score scales in force for current cycles as 待核实 (unverified).
- This is a rehearsal. It gives a decision band, not an acceptance probability.

```json
{"decision_band": "Resubmit next cycle (ARR Overall ~2-2.5, below Findings as submitted; desk reject at intake until preflight FAILs are fixed)", "kept_major_concerns": [{"id": "R1-M1", "lens": "soundness/evaluation", "location": "Abstract; §2 Evaluation contamination; §4 Contamination check", "concern": "The paper states both that evaluation sets were deduplicated against the pool and that they were not, and it assumes without testing that any overlap affects all filters equally, although a selective filter can retain translated benchmark-like items at a different rate (largest gain on MGSM)."}, {"id": "R1-M2", "lens": "soundness/evaluation", "location": "§5 Significance (vs §4 Statistical testing)", "concern": "The claim that XQF 'significantly outperforms IFD across all languages' rests on uncorrected per-language tests significant in only 7 of 18 languages, abandoning the paper's own Holm-Bonferroni protocol."}, {"id": "R1-M3", "lens": "soundness/evaluation", "location": "§4 Evaluation ('Appendix ??'); Table 2; Abstract '+3.5'", "concern": "The claim that every language is covered by a benchmark is false for Yoruba (none of XCOPA/XStoryCloze/XNLI/MGSM covers it), and three other low-resource languages have only XCOPA, so the low-resource tier average and the 13/18 significance count are ill-defined or thin."}, {"id": "R1-M4", "lens": "soundness/evaluation", "location": "Abstract vs §1 contribution 2 and Table 1", "concern": "The abstract reports the 7B average rising to 48.9, but the paper and Table 1 give 47.5, overstating the headline gain (3.7 vs 2.3 points)."}, {"id": "R2-M1", "lens": "novelty/excitement", "location": "§2 ¶2; §1 contribution 3; §5 Why a quota is needed", "concern": "The per-language quota and the global-threshold failure were proposed in the authors' own prior work, yet they are presented as contributions of this paper, so the real delta (the round-trip plus pivot scorer) is not isolated."}, {"id": "R2-M2", "lens": "novelty/excitement", "location": "§2 Translation quality estimation; §4 Baselines", "concern": "The consistency score is a reference-free QE proxy, but no translation-QE filter baseline (e.g., COMET-Kiwi-style or source-side QE on Bactrian-X's English originals) is compared, and the QE paragraph cites no QE work."}, {"id": "R3-M1", "lens": "clarity/reproducibility/ethics", "location": "§7 Conclusion (vs §6 Human-written versus translated data)", "concern": "The conclusion claims XQF will improve instruction tuning for any language and base model and makes human-written multilingual data unnecessary, which the paper's own results (human data enriched to 41%, human-only subset beating the full pool, two Llama 2 models) contradict."}], "downgraded": [{"id": "R1-M5", "lens": "soundness/evaluation", "location": "§5 Why a quota is needed", "concern": "The argument that removed low-resource examples are not worse is circular because z-normalized distributions match by construction; the quota is supported independently by Tables 2-3."}, {"id": "R2-M3", "lens": "novelty/excitement", "location": "§4 Models and training", "concern": "Only Llama 2 7B/13B (2023) models for an ACL 2027 submission; a scope limitation addressable in Limitations or with one current model."}, {"id": "R3-M2", "lens": "clarity/reproducibility/ethics", "location": "§4 Human evaluation vs Ethics Statement", "concern": "Human-evaluation recruitment is described inconsistently (native-speaker annotators vs crowdworkers), with no pay, consent, IRB or per-language results (checklist D)."}, {"id": "R3-M3", "lens": "clarity/reproducibility/ethics", "location": "§3.2; §4 Baselines/Evaluation; Ethics Statement", "concern": "The reward model and 70B rater are unnamed, prompts/templates are not given, the release statement conflicts (full examples vs identifiers), and data licenses are unstated."}], "dropped": []}
```
