# Simulated referee panel — agent4-paperA.tex

**Inline panel** (one agent playing AE → R1 → R2 → R3 → verifier → AE in sequence; each
referee report was written before moving to the next lens, but the referees are not truly
independent). This is a rehearsal. It predicts where the paper will be attacked and a likely
decision band. It does not replace peer review or predict acceptance.

Paper: *Group-Spectrum Alignment: Suppressing Group-Specific Feature Directions for Robustness
to Subpopulation Shift* (GSA). A Ky Fan k-norm penalty on differences between trace-normalized
covariances of JTT-style error×class pseudo-groups, with group labels used only on validation.
Four benchmarks (Waterbirds, CelebA, MultiNLI, CivilComments), ResNet-50 / BERT-base, five
seeds, equal 24-config budget per method, worst-group validation selection.

---

## 【Venue / family】 ICML 2027 / form A (NeurIPS-style OpenReview form, ICML 2027 field names) — calibrated 2026-11-23

Calibration sources: `ICML-Skills/resources/official-source-map.md` (ICML 2027 CFP, Reviewer
Instructions read 2026-11-23); `icml-review-process`, `icml-experiments`, `icml-related-work`,
`icml-reproducibility`, `icml-submission`; `shared-resources/submission-readiness/review-forms.md` §A.

- Score fields (ICML 2027 Reviewer Instructions, source 7): **soundness, presentation,
  significance, originality** (each 1–4), **overall** (1–6), **confidence** (1–5). The ICML pack
  does not print the overall-scale labels. The labels below come from form A (6 Strong Accept · 5
  Accept · 4 Borderline accept · 3 Borderline reject · 2 Reject · 1 Strong Reject) and should be
  re-checked against the live ICML form.
- **Two-stage review is new for 2027.** An AC decides whether a paper proceeds, and a SAC must
  confirm any first-stage rejection. The first page and abstract therefore have to make the
  contribution clear to a single AC.
- Contribution type: **General** (method + empirical evaluation).
- What ICML reviewers attack (`icml-experiments`, `icml-review-process`): untuned or missing
  strong baselines, single-seed variance, test-set tuning, compute disclosure, and novelty
  against the closest NeurIPS/ICML/ICLR work. The soundness concern is the one an AC is most
  likely to quote in the meta-review.

**Preflight (stage 0):** verdict **GO**, no findings. Est. 6.9 pages (under the 8-page limit);
Impact Statement and AI Disclosure Statement are present; anonymized 4open.science link.
Referees do not repeat mechanics. (Note for the author: Figure 1 is still a `[Plot placeholder]`
box, which preflight did not flag. Render the real plot before submission.)

---

## 【Desk-screen (AE)】 **Send out** — desk-reject risk: **low**

- **Scope / fit.** Group robustness under subpopulation shift is core ICML territory, and the
  method is a representation-level regularizer with a clear mechanism.
- **Fatal-flaw scan.** None found. The model-selection protocol is stated explicitly (§4 "Model
  selection": "no test-set quantity influences any choice"). The tuning budget is equal across
  methods (§4 "Hyperparameter search"). Five seeds with mean ± SD are reported (Table 1). The
  test-set sensitivity grid is labelled "for analysis only" (§6). The paper avoids overclaiming:
  it says "we do not claim an improvement" on Waterbirds (§5).
- **Delta vs. closest work.** As written, the delta is "use inferred groups to constrain the
  representation, not to reweight examples" (§1 ¶3, §2 ¶2). The AE flags for R2 that the paper
  treats the whole label-free family as reweighting or last-layer methods. Representation-level
  methods with inferred groups exist, so this delta needs checking.
- **First-stage (AC) legibility.** Good. The abstract states the setting, the mechanism, the cost
  and the headline number, and it names the baseline the comparison rests on.

---

## 【Referee 1 — soundness / evaluation】

**Form A**
- *Summary.* GSA infers 2C pseudo-groups from a briefly trained ERM model's errors. It then
  penalizes the sum of the top-k singular values of each pseudo-group's normalized
  (random-projected, EMA) feature covariance minus the pooled covariance, with balanced
  pseudo-group sampling. Mean worst-group accuracy (WGA) rises from 61.5 (ERM) to 82.8, compared
  with 80.9 for DFR and 81.7 for GroupDRO, which uses training group labels.
- *Strengths.* Explicit and fair protocol: equal 24-config random search for every method,
  worst-group validation selection, test evaluated once per seed (§4). Five seeds with SDs on
  every main and ablation cell (Tables 1–2). Margins are reported honestly per dataset:
  Waterbirds is within noise and is not claimed (§5). The ablation design isolates the penalty
  well, because the "penalty off, balanced sampling" row (86.1 / 72.9) separates the regularizer
  from JTT-style sampling. Compute is disclosed (2,900 accelerator-hours, single 40GB device).
- *Weaknesses.* (i) The baseline set stops at DFR (ICLR 2023). The stronger label-free methods
  that are now standard rows in this literature are absent (see M1). (ii) The significance test
  pairs by seed across independently trained methods. (iii) The mechanism probe is narrower
  than the claim drawn from it.
- *Scores.* Soundness **3** · Presentation **3** · Significance **3** · Originality **3** ·
  Overall **5 (Accept)**, conditional on M1 · Confidence **4**.
- *Questions.* (1) How does GSA compare with SSA, CnC and AFR under your protocol? (2) Do the
  MultiNLI/CivilComments p-values survive an unpaired Welch test? (3) Does a full-dimensional
  linear probe on GSA features still decode the background?
- *Limitations.* Adequately addressed (§7: dependence on error-based inference, validation
  labels, single-attribute benchmarks, class scaling).

**Referee template**
- 【Lens】 soundness / evaluation
- 【One-line summary】 A top-k spectral penalty on pseudo-group covariance differences improves
  label-free worst-group accuracy over DFR by 1.9 points on average, under a clean, equal-budget
  protocol.
- 【Recommendation】 accept (minor-to-moderate revision)
- 【Major concerns】
  - **R1-M1 — Baseline set omits the stronger post-2021 label-free methods.** *Where:* Abstract
    ("exceeds the strongest baseline that also avoids training group labels (DFR) by 1.9
    points"); §4 "Baselines" (ERM, LfF, JTT, DFR + GroupDRO reference); Table 1. *Why it
    matters:* SSA (Nam et al., ICLR 2022), Correct-N-Contrast (Zhang et al., ICML 2022) and AFR
    (Qiu et al., ICML 2023) work in the same validation-labels-only regime and report WGA in the
    same range as DFR on these four benchmarks. Whether DFR is "the strongest baseline" therefore
    decides how significant the 1.9-point margin is. *Fix:* add SSA, CnC and AFR under the same
    24-config budget and selection rule, or explain each exclusion. *Owner:* `icml-experiments`
    (baselines), with `icml-related-work`.
  - **R1-M2 — Paired t-test pairs by seed across independently trained methods.** *Where:* §4
    "Statistical reporting" ("two-sided paired t-test across seeds, pairing runs by seed"); §5
    "p < 0.01" on the text datasets. *Why:* seed index *i* for DFR and for GSA share no randomness
    that makes them a natural pair, so pairing can understate the variance. *Fix:* report a
    Welch test or a bootstrap over seeds, and give the CelebA test as well. *Owner:*
    `icml-experiments`.
  - **R1-M3 — The mechanism probe does not support "removes linearly decodable background
    information".** *Where:* §5 "What the penalty changes" ("on GSA features the same probe
    reaches 61.2%"). *Why:* the probe uses only the projection onto the two ERM directions, and
    "the same probe" may mean the ERM-trained weights were applied to GSA features. The
    background could simply have moved to other directions. *Fix:* retrain a full-dimensional
    linear probe on GSA features and report it. *Owner:* `icml-experiments`.
- 【Minor concerns】 Selected λ = 0.3 exactly, although the random search samples λ continuously
  on [0.01, 3] (§4, Table 3 caption); say whether λ was rounded or the grid was discrete.
  Published DFR on MultiNLI (≈74.7) is above your 73.4; comment on the reproduction gap.
  Majority-group accuracy is claimed to drop no more than under JTT (§5 "Where the gains come
  from") with no exhibit; add a per-group appendix table.
- 【What would move me to a clear accept】 M1 resolved with GSA still ahead or tied on average.

---

## 【Referee 2 — novelty / positioning】

**Form A**
- *Summary.* A representation-level regularizer for subpopulation shift that aligns only the
  top-k eigen-directions of pseudo-group covariance differences. Its novelty lies in the Ky Fan
  restriction (vs. CORAL-style full alignment) and in using inferred groups to define a
  constraint rather than weights.
- *Strengths.* The Ky Fan / top-k idea is clean, cheap (one 256×256 eigendecomposition per
  pseudo-group), and is directly tested against Frobenius (CORAL-style) and eigenvalue-only
  variants (Table 2). Relating the method to CORAL, JTT, DFR and GroupDRO as special cases (§3.4)
  is helpful. The paper is honest that the gains are concentrated on the text datasets.
- *Weaknesses.* Positioning is incomplete in a way that affects the stated delta (M1). The
  "nuclear norm is too blunt" claim is not what the ablation tests (M2).
- *Scores.* Soundness **3** · Presentation **3** · Significance **3** · Originality **2** ·
  Overall **4 (Borderline accept)** · Confidence **4**.
- *Questions.* (1) How does GSA differ mechanistically from Correct-N-Contrast, which also
  constrains the representation using ERM-inferred groups? (2) How does it differ from EIIL,
  which infers environments and applies an invariance penalty? (3) Was k = r ever run?
- *Limitations.* Yes, addressed.

**Referee template**
- 【Lens】 novelty / positioning
- 【One-line summary】 A clean spectral twist on covariance alignment across inferred groups. The
  novelty claim is framed against reweighting methods, but the representation-level label-free
  methods it should be framed against are missing.
- 【Recommendation】 major → borderline accept
- 【Major concerns】
  - **R2-M1 — Closest representation-level, inferred-group prior work is not cited, and the
    label-free family is described inaccurately.** *Where:* §1 ¶2 ("Methods that avoid training
    group labels, such as LfF and JTT, infer which examples are hard ... and upweight them ...
    Reweighting ... places no direct constraint on what the representation encodes"); §1 ¶3
    ("We take a complementary approach and regularize the representation itself"); §2 ¶2. *Why
    it matters:* Correct-N-Contrast (Zhang et al., ICML 2022) uses ERM-inferred groups to train
    the representation with a contrastive alignment loss. EIIL (Creager et al., ICML 2021) infers
    environments and imposes an invariance penalty. GEORGE (Sohoni et al., NeurIPS 2020) clusters
    representations to infer subgroups. Following the `icml-related-work` novelty table, "known
    trick rebranded" and "authors seem unaware of X" are reject anchors on originality unless the
    delta is restated. *Fix:* cite these works and add a delta paragraph: what GSA does that CnC
    and EIIL do not (top-k second-order alignment vs. pairwise contrastive or IRM-style
    gradients), backed by a head-to-head row (shared with R1-M1). *Owner:* `icml-related-work`.
  - **R2-M2 — The claim about nuclear norm (k = r) is not what the ablation tests.** *Where:* §3.4
    ("If k equals ... r, the Ky Fan norm becomes the nuclear norm ... our ablations show that this
    is too blunt"). Table 2 tests the Frobenius norm, and Table 3 stops at k = 16 of r = 256.
    *Fix:* add a k = r row or reword the claim to Frobenius. *Owner:* `icml-writing-style`.
- 【Minor concerns】 Spectral decoupling (Pezeshki et al. 2021, same paper as the cited gradient
  starvation work) is a natural label-free regularizer baseline to mention. All citations are
  from 2023 or earlier, so for an ICML 2027 submission add a freshness sweep (2024–2026 group
  robustness, foundation-model features). The abstract says GSA "adds one hyperparameter beyond
  its strength", but §4 searches both k and T_id.
- 【What would move me to accept】 A delta paragraph plus a CnC/SSA/AFR comparison showing GSA
  keeps a margin, or at least a distinct regime (text datasets) where it wins.

---

## 【Referee 3 — clarity / reproducibility】

**Form A**
- *Summary.* As above. This review focuses on whether a skeptical reader could re-implement GSA
  and regenerate Table 1.
- *Strengths.* Anonymized code, config files and per-seed results (§4 "Code"). Exact epochs,
  optimizers, batch sizes, feature layer, warm-up and projection dimension are given. Compute
  and hardware are disclosed. The DFR backbone is tied to the selected ERM checkpoint. The
  Impact Statement makes an appropriately modest claim about fairness.
- *Weaknesses.* One under-specified detail in the core estimator (M1). Baseline search ranges
  appear only in released configs. The cost claim is loosely stated.
- *Scores.* Soundness **3** · Presentation **3** · Significance **3** · Originality **3** ·
  Overall **5 (Accept)** · Confidence **3**.
- *Questions.* (1) When P is resampled each epoch, are the EMA covariances reset? (2) Which
  T_id was selected per dataset?
- *Limitations.* Yes.

**Referee template**
- 【Lens】 clarity / reproducibility
- 【One-line summary】 Reproducibility package and protocol are well above the ICML median, with
  one ambiguity in the covariance estimator.
- 【Recommendation】 accept
- 【Major concerns】
  - **R3-M1 — The EMA covariance estimate and the per-epoch resampling of P may be
    incompatible.** *Where:* §3.3 ("P ... is a fixed random Gaussian projection with r = 256,
    resampled at the start of each epoch. Estimates are updated from each mini-batch with an
    exponential moving average (momentum 0.9)") and §4 ("The penalty is switched on after one
    warm-up epoch, during which the moving-average covariances are initialized"). *Why:* after
    each resample, the EMA mixes covariances expressed in two different projected bases, so
    early-epoch penalty values are not well defined. A re-implementer cannot tell whether the
    EMA is reset. *Fix:* state the reset rule (or that P is fixed) and confirm the ablation
    numbers use it. *Owner:* `icml-reproducibility`.
- 【Minor concerns】 Put the per-method search ranges in an appendix, not only in configs
  (`icml-reproducibility`: "hyperparameters undocumented" pushback). "About 1.3× ERM on all four
  benchmarks" (§3.5) does not obviously fit an up-to-5-epoch identification run against 5-epoch
  text training versus 100-epoch Waterbirds training; give per-dataset factors and the selected
  T_id. The Figure 1 caption says "error and correct pseudo-groups", while the text describes the
  error pseudo-group only. Figure 1 is still a placeholder.
- 【What would move me further】 Already near accept; M1 clarification.

---

## 【Verification】 (verifier tries to refute each major concern against the text)

| ID | Verdict | Evidence / reason |
|---|---|---|
| R1-M1 | **kept (merged with R2-M1)** | Real: §4 lists only "ERM; LfF; JTT; and DFR ... We also report GroupDRO". The abstract asserts DFR is "the strongest baseline that also avoids training group labels". No SSA, CnC or AFR appears anywhere in the text or bibliography. Specific: names the table, the claim and the methods. Addressable: rows under the existing protocol. Same root cause as R2-M1 (incomplete map of label-free methods), so both are scored as one kept concern. |
| R2-M1 | **kept** | Real: §1 ¶2 says the label-free methods "infer which examples are hard ... and upweight them", and the only representation-preserving alternative named is DFR's last layer. §1 ¶3 claims regularizing the representation as the complementary angle. CnC, EIIL and GEORGE are absent from the bibliography (checked all 19 entries). Specific (§1 ¶2–3, §2 ¶2) and addressable (citation, delta paragraph, comparison row). Not decision-reversing on its own, because the Ky Fan restriction remains distinct, but it is the issue most likely to lower the originality and significance scores. |
| R1-M2 | **downgraded → minor** | Real: §4 "pairing runs by seed". It is not decision-relevant, though. For MultiNLI the margin is 2.9 with SDs 0.7/0.8 (Table 1), so an unpaired Welch t ≈ 2.9/√((0.49+0.64)/5) ≈ 6.1, p < 0.001, and CivilComments gives a similar figure. The paper does not claim significance on Waterbirds or CelebA. The conclusion stands under the correct test. |
| R1-M3 | **downgraded → minor** | Real, but the claim is qualified: §5 says "removes linearly decodable background information *concentrated in a few directions*, consistent with the motivation". It is supporting evidence, not a headline claim. A full-dimensional probe is a small, worthwhile addition, not a validity threat. |
| R2-M2 | **downgraded → minor** | Real: §3.4 says "our ablations show that this is too blunt" of the nuclear norm, but Table 2 tests the Frobenius norm and Table 3 stops at k = 16. The intended point (full-spectrum alignment underperforms) is supported by the Frobenius row, so this is a wording fix. |
| R3-M1 | **downgraded → minor** | Real and specific (§3.3 + §4 quoted above). Impact is bounded: with momentum 0.9, a stale term's weight falls below 1% after ~44 steps, a small fraction of an epoch at batch size 32–64 on these datasets. It is a reproducibility clarification, not a threat to the reported numbers. |

**Summary:** 6 major concerns raised → **kept 1** (R2-M1, with R1-M1 merged into it) ·
**downgraded 4** (R1-M2, R1-M3, R2-M2, R3-M1) · **dropped 1** (R1-M1, which is a duplicate of
R2-M1 and was merged rather than dropped on the merits).

---

## 【Referee forms】
- **R1** (soundness/evaluation): Soundness 3 · Presentation 3 · Significance 3 · Originality 3 · Overall 5 · Conf 4
- **R2** (novelty/positioning): Soundness 3 · Presentation 3 · Significance 3 · Originality 2 · Overall 4 · Conf 4
- **R3** (clarity/reproducibility): Soundness 3 · Presentation 3 · Significance 3 · Originality 3 · Overall 5 · Conf 3

## 【Decision band】 **Lean-accept** (form A: Accept / Borderline accept, overall ≈ 4–5)

The likely review pattern is **supportive, with one positioning objection**. The AC-quotable
issue is the missing comparison with CnC, SSA and AFR. On the `icml-review-process` leverage map
this is a soundness/originality anchor, but it can be answered in a 5,000-character rebuttal with
a table. Nothing in the paper is a soundness reject anchor: there is no test-set tuning, no
untuned baselines, and no single-seed results.

## 【Decisive issues (1–3)】
1. **Missing closest label-free, representation-level work and baselines (R2-M1 ⊕ R1-M1).**
   *Location:* Abstract; §1 ¶2–3; §2 ¶2; §4 "Baselines"; Table 1. *Why it decides:* the
   significance claim ("+1.9 over the strongest label-free baseline") and the originality claim
   ("regularize the representation itself", as opposed to reweighting) both depend on the
   neighbors that are left out. *Owner:* `icml-related-work` (delta paragraph) + `icml-experiments`
   (baselines). *Fix:* cite CnC, EIIL, GEORGE, SSA and AFR. Run SSA, CnC and AFR under the
   existing 24-config, worst-group-validation protocol with five seeds and add them to Table 1.
   Rewrite §1 ¶2 so the label-free family is not described as reweighting-only. If GSA does not
   lead on average, narrow the claim to the regime where it does (lexical spurious attributes /
   text datasets, which §5 already argues).

(No second decisive issue. The remaining items are long-tail.)

## 【Secondary issues】
- Significance test: replace seed-pairing with Welch or a bootstrap over seeds, and report CelebA (R1-M2; `icml-experiments`).
- Full-dimensional probe on GSA features (R1-M3; `icml-experiments`).
- Nuclear-norm vs. Frobenius wording in §3.4, or add k = r (R2-M2; `icml-writing-style`).
- EMA reset rule when P is resampled (R3-M1; `icml-reproducibility`).
- Hyperparameter count in the abstract (k and T_id); per-dataset cost factors and selected T_id; baseline search ranges in an appendix; exact λ grid (`icml-reproducibility`).
- Per-group accuracy table backing the majority-group claim in §5 (`icml-experiments`).
- Literature freshness to 2024–2026, and possibly a foundation-model backbone row; §7 already concedes the two-backbone scope (`icml-related-work`).
- Render Figure 1 (currently a placeholder) (`icml-submission`).

## 【Author action plan】 (ordered)
1. **Baselines + positioning (decisive):** add SSA, CnC and AFR rows under the shared protocol, and write the delta paragraph using the `icml-related-work` template → update abstract and §1 claims to match the new Table 1.
2. **Statistics:** Welch or bootstrap tests for all four datasets (`icml-experiments`).
3. **Mechanism:** full-dimensional probe and per-group table, which can go in an appendix (`icml-experiments`).
4. **Precision edits:** §3.4 nuclear/Frobenius, the hyperparameter count, the EMA reset rule, per-dataset cost (`icml-writing-style`, `icml-reproducibility`).
5. **Mechanics:** render Figure 1, then rerun preflight on the compiled PDF (exact page count) (`icml-submission`).
6. Prepare a rebuttal-ready table of the new baselines for the first 5,000-character round (`icml-author-response`).

## 【Calibration caveats】
- This was an inline panel. The referees were played in sequence by one agent, so some anchoring is possible.
- Literature claims (CnC, SSA, AFR, EIIL and their reported ranges) come from the reviewer's field knowledge, not from the manuscript. The author should confirm current numbers before relying on them.
- Overall-score labels come from form A; the ICML 2027 Reviewer Instructions confirm only the 1–6 scale. The per-paper review count for 2027 is unverified (Peer Review FAQ is a placeholder).
- This is a rehearsal. It gives a decision band, not an acceptance probability.

```json
{"decision_band": "lean-accept (ICML form A: Accept / Borderline accept, overall ~4-5)", "kept_major_concerns": [{"id": "R2-M1", "lens": "novelty/positioning (merged with R1-M1 soundness/evaluation)", "location": "Abstract; §1 ¶2-3; §2 ¶2; §4 Baselines; Table 1", "concern": "The closest label-free representation-level methods with inferred groups (Correct-N-Contrast, EIIL, GEORGE) and stronger validation-labels-only baselines (SSA, AFR) are neither cited nor compared, so the 'strongest baseline (DFR) +1.9' significance claim and the 'regularize the representation rather than reweight' novelty claim are not yet established."}], "downgraded": [{"id": "R1-M2", "lens": "soundness/evaluation", "location": "§4 Statistical reporting; §5 Main comparison", "concern": "Paired t-test pairs independently trained methods by seed index; conclusion survives an unpaired Welch test given 2.9/2.7-point margins with SD<=0.9."}, {"id": "R1-M3", "lens": "soundness/evaluation", "location": "§5 What the penalty changes", "concern": "Linear probe restricted to two ERM directions does not show background information is removed from the full GSA representation; claim is qualified and supporting only."}, {"id": "R2-M2", "lens": "novelty/positioning", "location": "§3.4 Relation to existing objectives; Tables 2-3", "concern": "Claim that the nuclear norm (k=r) is 'too blunt' is attributed to ablations that test Frobenius and k<=16 only; wording fix."}, {"id": "R3-M1", "lens": "clarity/reproducibility", "location": "§3.3; §4 Implementation details", "concern": "EMA covariance estimates mix bases when the projection P is resampled each epoch and no reset rule is stated; bounded impact at momentum 0.9."}], "dropped": [{"id": "R1-M1", "lens": "soundness/evaluation", "location": "Abstract; §4 Baselines; Table 1", "concern": "Missing SSA/CnC/AFR baselines — duplicate of R2-M1, merged into it rather than dropped on the merits."}]}
```
