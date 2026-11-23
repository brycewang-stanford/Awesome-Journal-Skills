# Simulated referee panel — agent3-paperB.tex (inline panel)

*A rehearsal, not a verdict. It predicts the attack surface and the likely decision band; it does not replace ICML review and makes no claim that the paper will be accepted.*

**Orchestration:** inline panel (one agent playing AE, three referees and the verifier in sequence; each referee report was written before the next lens was taken up, but the referees may still anchor on each other).

## Summary block

```text
【Venue / family】ICML 2027 (main track, contribution type "General"; abstracts 14 Jan, papers 22 Jan 2027) / form A, the NeurIPS-style OpenReview family, with ICML 2027 field names from ICML-Skills (soundness, presentation, significance, originality 1–4; overall 1–6; confidence 1–5) (calibrated 2026-11-23)
【Desk-screen】as uploaded: desk reject on mechanics (non-anonymized: author block, acknowledgements + grant, personal GitHub URL; no impact statement; TODO left in). On substance: HIGH first-stage-rejection risk because model selection uses the test split. The panel proceeds conditionally, assuming the preflight FAILs are fixed, to map the full attack surface. Desk-reject risk HIGH.
【Referee forms】R1 (soundness/evaluation): Sound 1 · Pres 2 · Sig 2 · Orig 2 · Overall 2 (Reject) · Conf 4
                R2 (novelty/positioning): Sound 2 · Pres 2 · Sig 2 · Orig 2 · Overall 3 (Borderline reject) · Conf 4
                R3 (clarity/reproducibility): Sound 2 · Pres 2 · Sig 2 · Orig 2 · Overall 2 (Reject) · Conf 3
【Verification】10 major concerns raised → kept 5 · downgraded 3 · dropped 2
【Decision band】Reject (Overall 2), with high risk of first-stage rejection by the AC
【Decisive issues (1–3)】
  1. §4 Model selection (line 98): configs and early stopping are chosen on TEST worst-group accuracy for every method, contradicting the "validation-only" claim (lines 17, 31–32, 49, 224) → icml-experiments
  2. §4 Hyperparameter search (line 95): 96-config search for GSA vs. untuned paper-default baselines, contradicting the "identical tuning budget" claim (lines 32, 49, 101) → icml-experiments
  3. §5 (line 136) + Conclusion (line 224): claims exceed evidence ("significantly" on Waterbirds with no test, "state of the art on all four", "uniformly superior", "general solution to distribution shift") → icml-writing-style / icml-experiments
【Secondary issues】missing closest work (EIIL, CnC, GEORGE, AFR); ablation budget asymmetry (Table 3: 24 configs vs. full GSA's 96); probe protocol (line 158); EMA under per-epoch projection resampling (lines 61, 101); seed-paired t-test only on two datasets; abstract 84.6% vs 82.8%; hyperparameter count ("one beyond its strength" ignores T_id); selected configs not reported
【Author action plan】see the end of this file
【Calibration caveats】see the end of this file
```

---

## 1. Associate Editor desk-screen

**Calibration used.** ICML 2027 has two-stage review: the AC decides whether a paper proceeds, an SAC confirms any first-stage rejection, and first-stage rejections arrive by 23 Feb 2027 (icml-review-process). Reviewers score soundness, presentation, significance and originality (1–4) and give an overall score (1–6). Under the Author Instructions, non-anonymized papers are automatically rejected, and both an impact statement and an AI Disclosure Statement are required (official-source-map rows 1, 3, 4). icml-experiments sets the bar: "current, strong, tuned" baselines, mechanism-isolating ablations, variance, leakage and split checks. On the AC-leverage map, soundness problems such as an "untuned baseline" or "leakage" are a "strong reject anchor; hard to rebut without new evidence".

**Mechanics (from preflight, NO-GO).** Six FAILs: ANON-AUTHOR (line 10), ANON-ACK (line 231, with a grant number), ANON-URL (personal GitHub, line 107), STMT-MISSING (impact statement), REF-MISSING (`hendrycks2019benchmarking`, line 23) and LEFTOVER-MARKER (TODO, line 219). Two FLAGs: Table 4 is unreferenced, and the abstract's 84.6% appears nowhere else. **Uploaded as-is, the paper would be rejected without review on anonymity alone.** All of these are fixable before 22 Jan 2027 and are not counted as substantive weaknesses below. The AI Disclosure Statement is present (line 228).

**Scope and fit.** Group robustness under subpopulation shift is squarely in ICML scope. A representation-level regularizer with a spectral argument suits the "General" contribution type.

**Fatal-flaw scan.** Line 98: "we select the configuration and the early-stopping epoch for every method by worst-group accuracy on the test split". This is a test-set leakage protocol, applied to the headline table. It contradicts the paper's own stated protocol and the Gulrajani & Lopez-Paz standard it claims to adopt (line 49). An AC can quote it as grounds for first-stage rejection.

**Closest work vs. delta.** The nearest work is JTT (error-set inference), DFR (last-layer retraining), Deep CORAL (full covariance alignment), and, not cited, methods that infer groups and then constrain the representation (EIIL, CnC). The delta is a Ky Fan top-k penalty on differences between pseudo-group covariances. The idea is plausible and cleanly stated. The evidence protocol is the problem.

**Desk-reject risk: HIGH** (mechanics certain; substance likely). Because this is a pre-submission rehearsal and every blocker can be fixed before the deadline, the panel proceeds and the result is conditional on the preflight fixes.

---

## 2. Referee reports

### Referee 1 — soundness / evaluation lens

**Form A (ICML 2027 fields)**

- **Summary.** GSA infers 2C pseudo-groups by crossing a briefly trained ERM model's errors with the class label (as in JTT). It then penalizes the Ky Fan k-norm of each pseudo-group's trace-normalized, randomly projected feature covariance minus the pooled covariance, under pseudo-group-balanced sampling. The paper reports mean WGA of 82.8 across Waterbirds, CelebA, MultiNLI and CivilComments vs. 80.9 for DFR and 81.7 for GroupDRO, plus ablations showing that error-based groups and the top-k restriction matter.
- **Strengths.** A clear, cheap mechanism (an r = 256 eigendecomposition, about 11% overhead; line 80). Informative ablations (random pseudo-groups, Frobenius, eigenvalues-only, no EMA, penalty off, oracle groups; Table 3). The penalty-off row isolates the regularizer from JTT-style balanced sampling (line 77). Five seeds with SD (Table 1).
- **Weaknesses.** The selection protocol leaks the test set. Tuning is asymmetric. The ablation budget is asymmetric. The mechanism probe is ambiguous.
- **Soundness** 1 (poor) · **Presentation** 2 · **Significance** 2 · **Originality** 2.
- **Questions.** (1) Re-run selection on validation WGA for all methods: does the ranking against DFR survive? (2) What is each baseline's performance under the same 96-config search? (3) Was the "GSA (full)" row of Table 3 tuned with 24 or 96 configs? (4) Was the background probe in §5 retrained on GSA features, using all features?
- **Limitations.** Partially addressed. The test-split protocol is not acknowledged as a limitation.
- **Overall** 2 (Reject) · **Confidence** 4 · **Ethics flag** none.

**Referee template**

```text
【Lens】soundness / evaluation
【One-line summary】JTT-style pseudo-groups + Ky Fan top-k covariance-difference penalty; +1.9 WGA over DFR on four benchmarks.
【Recommendation】reject (Overall 2)
【Major concerns】
  R1-M1 — Model selection on the test split.
     where: §4 "Model selection", line 98 ("we select the configuration and the early-stopping epoch for every method by worst-group accuracy on the test split"). Contradicted by the abstract, line 17 ("needs group labels only on the validation split"); contribution 2, line 32 ("validation-only model selection"); §2, line 49 ("selection uses only a validation split"); §3.1, line 55; Conclusion, line 224 ("validation-only model selection"); and the Table 3 caption, line 165 ("selected on validation worst-group accuracy").
     why: Every Table 1 number is an optimistically biased test-set maximum over configurations and epochs. GSA has 96 configurations to maximize over and the baselines have one (R1-M2), so the bias also favors GSA unequally. The sensitivity statement (line 214, "The validation-selected setting coincides with the best test setting") is uninterpretable under this protocol.
     fix: Re-select every method on validation WGA (the standard JTT/DFR protocol; for DFR, the half of validation not used for retraining) and report test WGA once. Correct every protocol statement so the paper is internally consistent.
     owner: icml-experiments
  R1-M2 — Asymmetric tuning budget.
     where: §4 "Hyperparameter search", line 95 ("We tune GSA with a random search of 96 configurations ... For the baselines we use the hyperparameters reported in their original papers without further tuning"). Contradicted by contribution 2, line 32 ("under an identical tuning budget"); §2, line 49 ("all methods share the same search budget"); and line 101 ("including the tuning budget for every baseline").
     why: The 1.9-point margin over DFR (and 0.6 on Waterbirds) is within what an untuned-baseline gap typically produces. Original-paper hyperparameters were set for those papers' epoch counts and pipelines, while line 89 fixes "the same ... number of training epochs per dataset" for all methods. icml-experiments: "Re-tune the baseline with matched budget, report the search protocol."
     fix: Give JTT, LfF and DFR the same 96-config random search (or report GSA at the baselines' budget), selected on validation.
     owner: icml-experiments
  R1-M3 — The ablation compares a 96-config GSA against 24-config variants.
     where: Table 3 caption, line 165 ("Each variant is tuned with the same 24-configuration budget"); Table 3 row "GSA (full)", 92.4±0.6 / 76.3±0.7, identical to Table 1 (lines 126, 172).
     why: The key mechanism claim (contribution 3, line 33; "Frobenius ... recovers almost none of the gain", line 190) compares a full method apparently tuned with 4× the budget against its variants.
     fix: Re-tune GSA (full) under the same 24 configs as the variants, or give every variant 96, and state which.
     owner: icml-experiments
  R1-M4 — The mechanism probe may not support "removes linearly decodable background information".
     where: §5 "What the penalty changes", line 158 ("on GSA features the same probe reaches 61.2%").
     why: If "the same probe" is the ERM-trained probe applied to GSA features, a drop shows only that the directions moved, not that the information is gone. Projecting onto only "those two directions" also ignores information relocated elsewhere.
     fix: Retrain a probe on GSA features using the full penultimate representation and report its accuracy.
     owner: icml-experiments
  R1-M5 — The gain over JTT may come from balanced sampling, not the penalty.
     where: §5 Main comparison, line 134.
     why: GSA keeps JTT-style group-balanced sampling.
     fix: Isolate the penalty.
     owner: icml-experiments
【Minor concerns】
  - Line 61 + line 101: P is "resampled at the start of each epoch", but the EMA covariance (momentum 0.9) is only initialized during the single warm-up epoch. After each resample, the EMA mixes covariances expressed in different random bases. State whether the EMA is reset or re-warmed every epoch.
  - The Ky Fan norm is non-differentiable at repeated singular values. Say how ties are handled (subgradient).
  - Abstract (line 17): "adds one hyperparameter beyond its strength". T_id ∈ {1, 2, 5} is also tuned (line 95), as are r, the momentum and the warm-up length.
  - Report the selected (λ, k, T_id) per dataset. The "1.3× ERM on all four benchmarks" claim (line 80) depends on T_id relative to 5-epoch text training.
  - Backbones (ResNet-50, BERT-base) are benchmark-standard, but one modern backbone (e.g., a ViT or CLIP encoder) would strengthen significance.
【What would move me to accept】Validation-only selection for all methods with matched tuning, with GSA still ahead of DFR on at least the text datasets.
```

### Referee 2 — novelty / positioning lens

**Form A (ICML 2027 fields)**

- **Summary.** As R1. The paper positions GSA as the first label-free method that constrains what the representation encodes, as opposed to reweighting (JTT, LfF) or last-layer retraining (DFR).
- **Strengths.** The motivation for top-k vs. Frobenius alignment is clear (line 74). The connection to CORAL and the nuclear-norm limit is honest (line 77). The text-dataset story (lexical spurious features living in few directions; line 136) is a testable, interesting hypothesis.
- **Weaknesses.** The closest label-free representation-level work is missing, and claims are overstated in §5 and §7.
- **Soundness** 2 · **Presentation** 2 · **Significance** 2 · **Originality** 2.
- **Questions.** (1) How does GSA differ from EIIL (inferred environments + an invariance penalty) and from CnC (error-based groups + representation-level contrastive alignment)? (2) Do the Waterbirds and CelebA gains over DFR survive a test? (3) Do published DFR numbers on these benchmarks differ from your re-run?
- **Limitations.** Mostly addressed (line 219). The Conclusion contradicts them (line 224).
- **Overall** 3 (Borderline reject) · **Confidence** 4.

**Referee template**

```text
【Lens】novelty / positioning
【One-line summary】Infer groups from errors, then align top-k covariance directions; claimed as a new, representation-level, label-free alternative to reweighting.
【Recommendation】borderline reject (Overall 3)
【Major concerns】
  R2-M1 — Missing closest work undercuts the framing of the delta.
     where: §1, line 25 ("Reweighting changes which examples the model attends to but places no direct constraint on what the representation encodes"); §2, lines 42–46; Related Work omits the methods below.
     why: Label-free group robustness already includes methods that infer groups and then constrain the representation. EIIL (Creager et al., 2021) infers environments and applies an invariance penalty. Correct-n-Contrast (Zhang et al., 2022) uses an ERM model's errors to define groups and applies a contrastive loss to the representation. GEORGE (Sohoni et al., 2020) clusters representations into pseudo-groups. AFR (Qiu et al., 2023) is a strong recent last-layer variant. Feature/covariance alignment across groups or domains (e.g., Fishr, CORAL in DomainBed) is also closer than Deep CORAL alone. The claim that label-free methods only reweight is therefore inaccurate, and the originality delta must be argued against CnC and EIIL specifically. icml-related-work: "This is a known trick rebranded" → cite, state the differing mechanism, move the delta to page 1.
     fix: Add these to Related Work with a mechanism-level delta paragraph. Add CnC (and ideally AFR) as baselines under the same protocol.
     owner: icml-related-work (+ icml-experiments for the baseline rows)
  R2-M2 — Claims exceed the evidence.
     where: §5, line 136 ("On Waterbirds, GSA also significantly outperforms DFR by 0.6 points, establishing a new state of the art on all four benchmarks; GSA is therefore uniformly superior to DFR"); Conclusion, line 224 ("it provides a general solution to distribution shift ... domain generalization, covariate shift and label shift without modification, making dedicated robustness methods for those settings unnecessary").
     why: (a) No test is reported on Waterbirds (the t-test, line 104 and line 136, covers only MultiNLI and CivilComments), and 0.6 points is within one SD (92.4±0.6 vs 91.8±0.7). (b) "State of the art on all four" is false by the paper's own Table 1: GroupDRO is higher on MultiNLI (77.1 vs 76.3; line 139), and the comparison set is four 2020–2023 baselines. (c) "Uniformly superior" contradicts line 134 ("The 1.9-point margin over DFR is not uniform across datasets"). (d) Domain generalization, covariate shift and label shift are never evaluated, and the Limitations (line 219) say multi-attribute shifts are not covered.
     fix: Delete the SOTA, "uniformly superior" and general-solution sentences. Report a test (or CIs) for every dataset and scope claims to subpopulation shift with a single known spurious attribute.
     owner: icml-writing-style (claims) + icml-experiments (tests)
【Minor concerns】
  - §1, line 23: the Hendrycks & Dietterich citation is irrelevant to subpopulation shift and missing from the bibliography (preflight REF-MISSING). Drop it.
  - Positioning of gradient starvation (line 46) is suggestive only. Either test it or soften it.
  - Lead with the text-dataset finding (largest, significant gains), which is the most original empirical claim.
【What would move me to accept】A precise delta vs. CnC/EIIL with a CnC baseline, scoped claims, and (from R1) a clean protocol.
```

### Referee 3 — clarity / reproducibility lens

**Form A (ICML 2027 fields)**

- **Summary.** As R1.
- **Strengths.** Code, configs and per-seed results are promised in a repository (line 107; it must be anonymized). Compute is disclosed (2,900 accelerator-hours, single 40GB device; line 101). Implementation details per dataset are given (line 101).
- **Weaknesses.** Method details are ambiguous (projection resampling vs. EMA), inference is thin, and numbers are inconsistent (abstract 84.6 vs. Table 1 82.8).
- **Soundness** 2 · **Presentation** 2 · **Significance** 2 · **Originality** 2.
- **Questions.** (1) Is the EMA reset when P is resampled? (2) How are seeds "paired" across different methods? (3) What are the selected hyperparameters per dataset?
- **Limitations.** Present but containing a TODO (preflight).
- **Overall** 2 · **Confidence** 3.

**Referee template**

```text
【Lens】clarity / reproducibility
【One-line summary】As R1.
【Recommendation】reject (Overall 2), mainly from the protocol issues R1 also sees
【Major concerns】
  R3-M1 — The method as written may be inconsistent: covariance EMA across per-epoch projection resampling.
     where: §3.3, line 61 ("a fixed random Gaussian projection with r = 256, resampled at the start of each epoch. Estimates are updated ... with an exponential moving average (momentum 0.9)"); line 101 ("The penalty is switched on after one warm-up epoch, during which the moving-average covariances are initialized").
     why: An EMA of P_t Σ P_tᵀ carried across epochs with different P_t mixes incompatible bases. A reimplementation following the text could behave differently from the authors' code.
     fix: State whether P is fixed or whether the EMA is re-initialized each epoch, and add pseudocode.
     owner: icml-reproducibility
  R3-M2 — Statistical inference is thin and selectively applied.
     where: §4 "Statistical reporting", line 104 ("two-sided paired t-test across seeds, pairing runs by seed"); §5, line 136.
     why: The test is run only for the DFR comparison and only reported for two datasets. "Pairing by seed" across two different methods is not a natural pairing unless seeds fix data order and initialization. n = 5 per arm.
     fix: Report 95% CIs for all Table 1 cells (or a test per dataset), and explain the pairing or use an unpaired/Welch test.
     owner: icml-experiments
  R3-M3 — Compute and cost are not disclosed.
     where: whole paper.
     why: ICML expects hardware and training-cost transparency.
     fix: Add a compute table.
     owner: icml-reproducibility
【Minor concerns】
  - Abstract (line 17) says 84.6% where Table 1 and contribution 2 (line 32) say 82.8 (preflight NUM-MISMATCH); the abstract's own "+1.9 over DFR" implies 82.8.
  - Table 4 (sensitivity) is never referenced (preflight). It is also test-set analysis; label it as such in the caption.
  - Figure 1 is a placeholder (line 152).
  - Baseline implementation sources (official code vs. re-implementation) are not stated (line 92).
  - Datasets: give the WILDS CivilComments group definition used (coarse 4-group vs. 16-group) and the MultiNLI negation word list.
【What would move me to accept】A clean, consistent protocol (R1), pseudocode resolving the EMA question, and CIs throughout.
```

---

## 3. Verification pass (verifier, not a referee)

| ID | Concern | Verdict | Evidence / reason |
|---|---|---|---|
| R1-M1 | Test-split model selection contradicts claimed validation-only selection | **kept** | Line 98: "we select the configuration and the early-stopping epoch for every method by worst-group accuracy on the test split". Against line 49: "selection uses only a validation split"; line 32: "validation-only model selection"; line 224: "Under a shared tuning budget and validation-only model selection". Real, specific, addressable (re-select on validation). **Fatal-flaw grade.** |
| R1-M2 | 96-config GSA search vs. untuned baselines | **kept** | Line 95: "For the baselines we use the hyperparameters reported in their original papers without further tuning". Against line 32: "under an identical tuning budget" and line 49: "all methods share the same search budget". Line 101 ("including the tuning budget for every baseline") does not cure it; it contradicts line 95. Real, specific, addressable. |
| R1-M3 | Ablation budget asymmetry (24 configs vs. 96-config full GSA) | **kept** | Table 3 caption, line 165: "Each variant is tuned with the same 24-configuration budget". The "GSA (full)" row, 92.4±0.6 / 76.3±0.7 (line 172), equals Table 1 (line 126), which came from the 96-config search (line 95). No text says the full row was re-tuned at 24. Real, specific, addressable. It undercuts contribution 3, so kept as major, though secondary to M1–M2. |
| R1-M4 | Probe protocol ambiguous | **downgraded** | Line 158: "on GSA features the same probe reaches 61.2%". "Same probe" could mean the same probing protocol (retrained), so the concern is an ambiguity rather than a demonstrated error. Real and addressable, but it does not move the decision. → minor (clarify and add a full-feature retrained probe). |
| R1-M5 | Gain over JTT may come from balanced sampling | **dropped** | Answered by the paper. Line 77: "our implementation keeps JTT-style group-balanced sampling, so that the comparison with the penalty-off variant ... isolates the contribution of the penalty". Table 3, line 177: penalty off 86.1 / 72.9 vs. full 92.4 / 76.3. |
| R2-M1 | Missing closest label-free representation-level work (EIIL, CnC, GEORGE, AFR) | **kept** | Line 25: "Reweighting ... places no direct constraint on what the representation encodes". The bibliography (lines 235–318) contains no EIIL, CnC, GEORGE or AFR entries. Real (omission), specific (§1 line 25, §2), addressable (cite, add a delta paragraph, add a CnC baseline). |
| R2-M2 | Overclaims at line 136 and line 224 | **kept** | Line 136: "significantly outperforms DFR by 0.6 points, establishing a new state of the art on all four benchmarks; GSA is therefore uniformly superior". Table 1: MultiNLI GroupDRO 77.1 > GSA 76.3. Line 136 restricts the t-test to MultiNLI and CivilComments. Line 134: "not uniform across datasets". Line 224: "general solution to distribution shift", with no DG, covariate or label-shift experiments anywhere. Real, specific, addressable (delete/scope and add tests). |
| R3-M1 | EMA across per-epoch projection resampling | **downgraded** | Real: line 61 says P is "resampled at the start of each epoch" with EMA momentum 0.9, and line 101 describes initialization only in "one warm-up epoch". But code is released (line 107) and the issue is a specification gap, not shown to change results. → minor (state the reset rule, add pseudocode). |
| R3-M2 | Thin, selective inference; seed pairing | **downgraded** | Real (line 104 restricts the test to the DFR comparison; line 136 reports p only for two datasets). Its decision-relevant part, the unsupported "significantly" on Waterbirds, is already carried by kept R2-M2. The rest (CIs everywhere, pairing explanation) is a reporting fix. → minor. |
| R3-M3 | Compute not disclosed | **dropped** | Answered in the text. Line 101: "All runs use a single 40GB accelerator; the full experimental grid ... took about 2,900 accelerator-hours". Line 80 gives per-step overhead (≈11%) and 1.3× ERM. |

**Tally:** 10 major concerns raised → **kept 5** (R1-M1, R1-M2, R1-M3, R2-M1, R2-M2) · **downgraded 3** (R1-M4, R3-M1, R3-M2) · **dropped 2** (R1-M5, R3-M3).

I also re-derived the numbers in passing. Every "Mean WGA" in Table 1 is the mean of its four cells (GSA 82.775 → 82.8; DFR 80.9; GroupDRO 81.675 → 81.7). The per-dataset margins over DFR (0.6 / 1.3 / 2.9 / 2.7) and the average-accuracy drops (2.5, 3.8) match the text, and every sensitivity statement on line 214 matches Table 4. The only numeric inconsistency is the abstract's 84.6, which preflight already flags.

---

## 4. AE synthesis

```text
【Venue】ICML 2027 main track, form A with ICML 2027 fields (icml-review-process; source map rows 1, 3, 7)
【Desk-screen】as uploaded → rejected without review (anonymity FAILs: author block line 10, acknowledgements/grant line 231, personal GitHub line 107; missing impact statement; TODO line 219). After the preflight fixes → HIGH first-stage-rejection risk because of the test-split selection protocol (line 98)
【Verification】10 major concerns → kept 5 · downgraded 3 · dropped 2
【Decision band】Reject (Overall 2), with high first-stage-rejection risk; not salvageable by rebuttal because it needs new runs
【Decisive issues】
  1. Test-split model selection for every method (R1-M1; line 98), contradicting five protocol statements in the paper. This is the AC-quotable soundness anchor. No rebuttal can fix it without re-running selection.
     owner: icml-experiments → re-select configs and epochs on validation WGA for every method (DFR: the held-out validation half); report test once; rewrite lines 17/32/49/55/98/224 so the protocol is stated once and consistently.
  2. Asymmetric tuning (R1-M2; line 95 vs lines 32/49/101). The 1.9-point headline margin cannot be separated from a tuning gap. The same flaw recurs inside the ablation (R1-M3: 96-config full GSA vs 24-config variants in Table 3).
     owner: icml-experiments → equal random-search budget (96 configs, validation-selected) for JTT, LfF, DFR and every Table 3 variant, or report GSA at the baselines' budget.
  3. Claims exceed evidence, and positioning misses the closest work (R2-M2 + R2-M1). "Significantly"/"SOTA on all four"/"uniformly superior" (line 136) and "general solution to distribution shift" (line 224) are contradicted by the paper's own table and scope. The framing that label-free methods only reweight (line 25) ignores CnC and EIIL.
     owner: icml-writing-style + icml-related-work → delete or scope the claims; add tests or CIs for every dataset; add a CnC/EIIL delta paragraph and a CnC baseline under the corrected protocol.
【Secondary issues】probe protocol (retrain on full GSA features); EMA vs per-epoch projection resampling (state reset rule, add pseudocode); CIs and an explained pairing for the t-test; report selected (λ, k, T_id); fix the hyperparameter-count claim; abstract 84.6 → 82.8; reference Table 4 and label it test-set analysis; render Figure 1; one modern backbone if compute allows.
【Author action plan】(ordered)
  0. icml-submission — clear every preflight FAIL first: anonymize the author block, delete the acknowledgements and grant, move the code to an anonymized mirror (branch frozen after the deadline), add an impact statement before the references, delete the TODO, fix or drop the hendrycks citation, fix the abstract number.
  1. icml-experiments — re-run selection on validation for all methods with matched tuning budgets (Table 1 and Table 3). Decide only after seeing whether the DFR margin survives; if it survives only on the text datasets, reframe the paper around that finding.
  2. icml-related-work — EIIL / CnC / GEORGE / AFR positioning; add a CnC baseline.
  3. icml-writing-style — scope every claim to the evidence (line 136, line 224, abstract).
  4. icml-reproducibility — pseudocode, EMA/projection rule, selected hyperparameters, CIs, baseline implementation sources.
  (No econometric execution bridge applies; these are ML re-runs. Estimated cost: the paper's own 2,900 accelerator-hour grid suggests matched baseline tuning is roughly a comparable additional budget, so plan it against the 22 Jan 2027 deadline.)
【Calibration caveats】Inline panel, so referees may anchor on each other. Because the corrected protocol may shrink or erase the margin, the eventual band after fixes is genuinely uncertain: a clean re-run could move this to borderline (Overall 3–4) if the text-dataset gains survive. The missing-work list reflects the label-free group-robustness literature as of the panel's knowledge. Re-run the icml-related-work freshness sweep before submission.
```

```json
{"decision_band": "Reject (ICML Overall 2); high first-stage-rejection risk; desk reject as uploaded on anonymity mechanics", "kept_major_concerns": [{"id": "R1-M1", "lens": "soundness/evaluation", "location": "§4 Model selection line 98 (vs. abstract line 17, contribution line 32, §2 line 49, §3.1 line 55, Conclusion line 224, Table 3 caption line 165)", "concern": "Configurations and early-stopping epochs for every method are selected on test-split worst-group accuracy, which leaks the test set and contradicts the paper's repeated claim of validation-only model selection."}, {"id": "R1-M2", "lens": "soundness/evaluation", "location": "§4 Hyperparameter search line 95 (vs. lines 32, 49, 101)", "concern": "GSA receives a 96-configuration random search while baselines use untuned original-paper hyperparameters, contradicting the claimed identical tuning budget and confounding the 1.9-point margin over DFR."}, {"id": "R1-M3", "lens": "soundness/evaluation", "location": "Table 3 caption line 165; Table 3 row line 172 vs. Table 1 line 126", "concern": "The ablation compares the 96-config-tuned full GSA (numbers identical to Table 1) against variants tuned with only 24 configurations, so the top-k-vs-Frobenius mechanism claim is budget-confounded."}, {"id": "R2-M1", "lens": "novelty/positioning", "location": "§1 line 25; §2 lines 42-46; bibliography", "concern": "The closest label-free, representation-level group-robustness methods (EIIL, Correct-n-Contrast, GEORGE, AFR) are neither cited nor compared, and the framing that label-free methods only reweight is inaccurate."}, {"id": "R2-M2", "lens": "novelty/positioning", "location": "§5 line 136; Conclusion line 224", "concern": "Claims of a significant Waterbirds gain (no test, within one SD), state of the art on all four benchmarks (GroupDRO is higher on MultiNLI), uniform superiority (contradicted by line 134) and a general solution to all distribution shift (never evaluated) exceed the evidence."}], "downgraded": [{"id": "R1-M4", "lens": "soundness/evaluation", "location": "§5 line 158", "concern": "Ambiguous whether the background probe was retrained on GSA features; clarify and add a full-feature retrained probe."}, {"id": "R3-M1", "lens": "clarity/reproducibility", "location": "§3.3 line 61; §4 line 101", "concern": "EMA covariance carried across per-epoch projection resampling is underspecified; state the reset rule and add pseudocode."}, {"id": "R3-M2", "lens": "clarity/reproducibility", "location": "§4 line 104; §5 line 136", "concern": "Seed-paired t-test applied only to the DFR comparison on two datasets; add CIs everywhere and explain pairing (decision-relevant part carried by R2-M2)."}], "dropped": [{"id": "R1-M5", "lens": "soundness/evaluation", "location": "§5 line 134", "concern": "Gain over JTT may be balanced sampling; refuted by line 77 and Table 3 penalty-off row (86.1/72.9 vs 92.4/76.3)."}, {"id": "R3-M3", "lens": "clarity/reproducibility", "location": "whole paper", "concern": "Compute not disclosed; refuted by line 101 (single 40GB accelerator, ~2,900 accelerator-hours) and line 80."}]}
```
