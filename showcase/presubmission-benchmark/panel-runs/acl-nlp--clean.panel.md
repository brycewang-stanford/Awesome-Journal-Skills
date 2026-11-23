# Simulated referee panel — agent3-paperA.tex (inline panel)

*A rehearsal, not a verdict. It predicts the attack surface and the likely decision band; it does not replace ARR review and makes no claim that the paper will be accepted.*

**Orchestration:** inline panel (one agent playing AE, three referees and the verifier in sequence; each referee report was written before the next lens was taken up, but the referees may still anchor on each other).

## Summary block

```text
【Venue / family】ACL 2027 via ACL Rolling Review (January 2027 cycle, submission 4 Jan 2027) / form B, the ARR review form (calibrated 2026-11-23 from ACL-Skills/resources/official-source-map.md, acl-review-process, acl-experiments, acl-related-work, acl-reproducibility, acl-submission)
【Desk-screen】send out — in scope (multilingual instruction-data selection, core *ACL topic), Limitations section present, anonymized repository; desk-reject risk LOW
【Referee forms】R1 (soundness/evaluation): Soundness 3 · Excitement 3.5 · Overall 3 · Conf 4
                R2 (excitement/novelty/positioning): Soundness 3.5 · Excitement 2.5 · Overall 3 · Conf 4
                R3 (reproducibility/responsible NLP): Soundness 3.5 · Excitement 3.5 · Overall 3.5 · Conf 3
【Verification】8 major concerns raised → kept 3 · downgraded 3 · dropped 2
【Decision band】Findings (Overall ≈ 3) as submitted; Conference (3.5–4) is reachable if the decisive issues are fixed before the January 2027 cycle
【Decisive issues (1–3)】
  1. §4 Evaluation (line 85), Table 2, §5 Significance (line 129): Yoruba is in none of the four benchmarks, so the 18-language and low-resource-tier claims cannot have been computed as described → acl-experiments
  2. §4 Models (line 79): Llama 2 (2023) is the only model family, which weakens generality and the "does this matter now?" test at ACL 2027 → acl-experiments
  3. §2 (line 43) and bib line 299–302: per-language quotas are credited to a reference that cannot be located, and contribution 3 leans on that same idea → acl-related-work
【Secondary issues】open-ended evaluation is thin (only the 6-language human eval); no reference-free QE baseline (e.g., CometKiwi); ρ was tuned for XQF only; no CI or test on the human-eval preference; the reward model and the 70B rater are not named; the per-language pool composition is not reported; the normalization argument on line 159 is circular; figures are still placeholders
【Author action plan】see the end of this file
【Calibration caveats】see the end of this file
```

---

## 1. Associate Editor desk-screen

**Calibration used.** ACL 2027 takes ARR packages from the January 2027 cycle or earlier. Venue SACs and PCs decide between main conference, Findings and reject (acl-review-process). Under form B, Findings is judged mainly on soundness and reproducibility, and Conference adds novelty and impact. acl-experiments sets the evidence bar: tuned baselines, seeds with deviation, significance for small deltas, human evaluation with agreement, contamination reasoning, an ablation for every credited component, quantitative error analysis, per-language reporting for multilingual claims, and "a well-prompted current LLM has become mandatory context".

**Scope and fit.** Selecting multilingual instruction data, with attention to low-resource languages, is core ACL material. It also touches the ACL 2027 theme track ("Homogenization and knowledge collapse in LLMs", which includes cross-lingual homogenization). The paper does not use that hook, although its Limitations section (line 216) raises the "push toward English-resembling content" risk itself.

**Fatal-flaw scan.** I found no fatal flaw. Contamination handling is careful: a 13-gram or character 25-gram scan against validation and test items, plus checks of benchmark training splits and the reward model's data (line 76). Baselines share the quota, budget and hyperparameters (lines 79, 82). The paper uses three seeds, paired bootstrap with Holm–Bonferroni, and a human evaluation with Krippendorff's α. One factual problem in evaluation coverage (Yoruba; see R1) needs a referee's attention but is not a desk-reject matter.

**Preflight.** Verdict GO. The only finding is an INFO that the Responsible NLP checklist is not in the file, and it is filed on the form. Referees do not spend time on mechanics.

**Closest work vs. delta.** The nearest prior work is English selection (AlpaGasus, IFD, LIMA), translation QE (round-trip, LaBSE) and per-language quotas (credited to Quillfeather & Brambleton 2024). The delta is to combine round-trip consistency with pivot-language reward scoring, normalize within each language and apply quotas, all for instruction data. The combination is reasonable but incremental, so excitement rather than soundness will decide Conference vs Findings.

**Desk-reject risk: LOW → send out.**

---

## 2. Referee reports

### Referee 1 — soundness / evaluation lens

**Form B**

- **Paper Summary.** XQF scores each instruction example by round-trip translation consistency (LaBSE cosine after an NLLB round trip, min over instruction and response) and by a reward model applied to the English pivot. It z-normalizes both within each language and keeps the top 30% of each language. On a 412K, 18-language pool, Llama 2 7B/13B fine-tuned on the XQF subset beat the full pool (45.2→47.5, 50.4→52.6) and four quota-matched filters across XCOPA, XStoryCloze, XNLI and MGSM. Gains concentrate in the low-resource tier (+3.5).
- **Summary of Strengths.** (i) A fair comparison design: every filter retains 30% per language and hyperparameters are tuned once on the full-pool condition and shared (lines 79, 82). If anything this favors the full pool. (ii) Real contamination auditing before filtering (line 76). (iii) Three seeds with SD in every cell (Table 1), and per-language paired bootstrap with Holm correction, reported honestly, including the weaker result against IFD (4/18 languages; line 129). (iv) Ablations cover each credited component (Table 3), plus a retention curve chosen on held-out pool instructions (line 198). (v) A quantitative error analysis of the bottom decile, with categories and a top-decile contrast (line 201).
- **Summary of Weaknesses (decision-relevant first).** (1) Evaluation coverage does not match the 18-language claim: Yoruba appears in none of the four benchmarks. (2) Evaluation of what instruction tuning is for (open-ended responses) rests on a 6-language human study. (3) One model family.
- **Comments/Suggestions/Typos.** See the minor concerns.
- **Soundness:** 3 (Acceptable). **Excitement:** 3.5. **Overall Assessment:** 3 (Findings); 3.5 if M1 is resolved. **Reviewer Confidence:** 4.
- **Reproducibility:** 4. **Ethical concerns:** none beyond what the Ethics Statement already handles.

**Referee template**

```text
【Lens】soundness / evaluation
【One-line summary】Within-language-normalized round-trip + pivot-reward filtering with per-language quotas beats quota-matched English-centric filters on four multilingual benchmarks for Llama 2 7B/13B.
【Recommendation】Findings (3), Conference reachable
【Major concerns】
  R1-M1 — Yoruba has no benchmark coverage, so the per-language and tier results are not computable as described.
     where: §4 Evaluation, line 85 ("Each of our 18 languages is covered by at least one benchmark"); Table 2 caption, line 133 ("tiers average six languages each"); §5 Significance, line 129 ("13 of 18 languages", "4 of 18 ... all of them low-resource"); abstract, line 17.
     why: The standard releases of XCOPA (et, ht, id, it, qu, sw, ta, th, tr, vi, zh), XStoryCloze (ar, en, es, eu, hi, id, my, ru, sw, te, zh), XNLI (15 languages, no yo) and MGSM (bn, de, en, es, fr, ja, ru, sw, te, th, zh) contain no Yoruba. The low-resource tier average, the 18-language Holm family and the "all low-resource" significance statement therefore either use a Yoruba score from an undisclosed source or misstate their denominator. The headline low-resource claim (+3.5) rests on this tier.
     fix: Name the source of Yoruba scores (e.g., an added Yoruba benchmark such as AfriXNLI/AfriMGSM), or recompute Table 2 and the Holm family over 17 evaluated languages and correct line 85, the Table 2 caption and the abstract. Report the per-language block (acl-experiments: "report the per-language block"), including which benchmarks cover each language, since ht/qu/ta rest on XCOPA alone and ja on MGSM alone.
     owner: acl-experiments
  R1-M2 — Instruction-tuning quality is measured mostly with zero-shot classification and short-answer benchmarks.
     where: §4 Evaluation, line 85; §5 Human evaluation, line 162.
     why: XCOPA, XStoryCloze and XNLI largely measure base-model capabilities. The paper's motivation (responses drifting into English, mangled responses; lines 23, 201) concerns generation quality, which only the 6-language human study measures.
     fix: Add a multilingual open-ended evaluation (an LLM judge validated against the existing human labels) across all 18 languages.
     owner: acl-experiments
  R1-M3 — The retention rate may have been tuned on the benchmarks.
     where: §6 "How much to keep", line 198.
     why: If ρ = 0.3 were picked on the test benchmarks, the main comparison would be optimistic.
     fix: Report the selection procedure.
     owner: acl-experiments
【Minor concerns】
  - ρ = 0.3 is XQF's optimum (line 198). Baselines are evaluated only at that budget; a retention curve for IFD (the strongest baseline) would show whether XQF wins at the baselines' own best budget.
  - Human evaluation (line 162): give per-language counts and a CI or sign test for the 46.2 vs 32.3 preference. Prompts written by annotation team leads (line 91) could favor some response styles; say so.
  - The bootstrap averages predictions over seeds (line 88), so seed variance does not enter the per-language test; state this as a choice.
  - Line 159, "their within-language score distribution matches ... once normalized", is true by construction of the z-scoring and is not evidence that the removed examples are good. Use the manual-inspection protocol of line 201 on globally-removed low-resource examples instead.
  - Figures 1 and 2 are placeholders in the source (lines 153, 192); the curve values are given in text only.
【What would move me to accept (Conference)】M1 resolved with a corrected per-language table, plus an open-ended multilingual evaluation for all languages.
```

### Referee 2 — excitement / novelty / positioning lens

**Form B**

- **Paper Summary.** As above. The claimed contributions are the XQF filter, gains over English-centric filters at a fixed budget, and the finding that per-language quotas are necessary for low-resource gains.
- **Summary of Strengths.** A practical, cheap-to-reuse recipe (translations are reusable across models; line 207). A clear framing of why English-centric filters fail in translated data (line 25). Honest reporting of where the gain over IFD is and is not significant (line 129). The shift toward human-written data (line 204) is an interesting side result.
- **Summary of Weaknesses.** (1) Generality is shown only on a 2023 base model family. (2) The novelty is a combination of known components, and the one component credited to prior work cites a source I cannot locate. (3) The nearest QE-based alternative is not compared.
- **Soundness:** 3.5. **Excitement:** 2.5 (Interesting but incremental as framed). **Overall Assessment:** 3 (Findings). **Reviewer Confidence:** 4.
- **Best paper justification:** n/a.

**Referee template**

```text
【Lens】excitement / novelty / positioning
【One-line summary】A combination of round-trip QE, pivot-language reward scoring and per-language quotas, applied to multilingual instruction data.
【Recommendation】Findings (3)
【Major concerns】
  R2-M1 — Only one, dated base-model family.
     where: §4 Models, line 79 ("We fine-tune Llama 2 7B and 13B"); Conclusion, line 212; Limitations, line 216.
     why: For an ACL 2027 paper (Aug 2027), Llama 2 is about four years old and English-centric. Current open bases have much stronger multilingual pretraining, and data-selection gains often shrink as the base improves. acl-experiments flags the "does this matter now?" review. The generality claim ("Selecting multilingual instruction data requires methods that respect differences between languages", line 212) needs at least one current multilingual base.
     fix: Repeat the main comparison (full pool, IFD, XQF) on one current multilingual base model at 7–8B, or narrow the claims to Llama 2.
     owner: acl-experiments
  R2-M2 — The per-language quota principle is credited to an unverifiable reference, and contribution 3 rests on it.
     where: §2, line 43 ("\citet{quillfeather2024quota} argue ... and propose per-language quotas; we adopt the same principle"); bibliography, lines 299–302 ("Proceedings of the Example Workshop on Multilingual Data Curation"); contribution 3, line 33.
     why: I cannot find this paper or venue. Reviewers check citations in their own subfield (acl-related-work, "Red flags"). ARR forbids leaning on materials reviewers cannot access, and a fabricated-looking citation damages trust in the whole bibliography. If the source is real, contribution 3 confirms prior work rather than discovering something new, and the novelty claim must be recast.
     fix: Replace it with a verifiable citation of record (Anthology entry) or remove it. Then restate contribution 3 as an empirical confirmation for instruction data, with credit to the actual prior work.
     owner: acl-related-work
  R2-M3 — The obvious QE baseline is missing.
     where: §2 "Translation quality estimation", line 46; §4 Baselines, line 82.
     why: For Bactrian-X (281K of the 412K examples, line 76) the English source is known. A reference-free QE model scoring source vs. translation (e.g., CometKiwi) is the field-standard way to detect bad translations, and is cheaper than an NLLB round trip. The paper distinguishes its goal in words (line 46) but never compares against it.
     fix: Add a QE-filter baseline on the translated portion, under the same quota.
     owner: acl-experiments / acl-related-work
【Minor concerns】
  - Freshness: no multilingual data-selection or translated-instruction-filtering work after 2024 is discussed. Run the acl-related-work freshness sweep (last two *ACL rounds).
  - Positioning hook: the ACL 2027 theme (cross-lingual homogenization) fits the paper's own concern that translatability-based filtering homogenizes content (line 216). A short analysis of the diversity of retained content would raise excitement.
  - The AlpaGasus-style baseline rates in the original language (line 82) while XQF scores the English pivot. A pivot-rated AlpaGasus row would separate "pivot scoring" from "which rater".
【What would move me to accept (Conference)】A current base model showing the gain persists; a clean, verifiable positioning of the quota idea; a QE baseline.
```

### Referee 3 — reproducibility / responsible-NLP lens

**Form B**

- **Paper Summary.** As above.
- **Summary of Strengths.** An anonymized repository with filtering code, selected IDs and evaluation scripts (line 94). Training hyperparameters and their selection protocol are stated (line 79). Compute costs are given per stage (line 207). The Ethics Statement covers annotator pay, consent, the IRB exemption, PII scrubbing and licensing (line 220). A substantive Limitations section (line 216).
- **Summary of Weaknesses.** Several components are under-identified: the reward model, the 70B rater, the evaluation templates, and the per-language pool sizes.
- **Soundness:** 3.5. **Excitement:** 3.5. **Overall Assessment:** 3.5. **Reviewer Confidence:** 3.
- **Reproducibility:** 4 (could mostly reproduce; some parameters underspecified). **Datasets / Software:** 3 (IDs released, not a new dataset).

**Referee template**

```text
【Lens】reproducibility / responsible NLP
【One-line summary】As R1.
【Recommendation】between Findings and Conference (3.5)
【Major concerns】
  R3-M1 — Pretraining contamination of the base model is not addressed.
     where: §4 Contamination check, line 76.
     why: Translated benchmarks (XNLI, XStoryCloze, MGSM) may be in Llama 2 pretraining data.
     fix: Discuss.
     owner: acl-reproducibility
  R3-M2 — Key scoring components are not identified.
     where: §3.2, line 64 ("a 1.3B-parameter reward model trained on public English helpfulness preference data"); §4 Baselines, line 82 ("an open 70B chat model"); §4 Evaluation, line 85 ("a fixed zero-shot instruction template").
     why: Neither the reward model, the 70B rater nor the prompt templates are named, so neither the XQF quality score nor the strongest LLM-rating baseline can be rebuilt from the paper (acl-reproducibility, prompted-LLM disclosure floor).
     fix: Name the model checkpoints and versions, and give verbatim prompts, decoding settings and parsing rules in an appendix.
     owner: acl-reproducibility
【Minor concerns】
  - Report per-language pool sizes (Bactrian-X sample size and Aya counts per language, line 73). Quotas make the language mix of every condition depend on them.
  - Give the selected 20% duplicate-annotation counts per language for the human study (line 91) and the number of annotators per language.
  - Responsible NLP checklist: answer C (seeds, budget, search) and D (pay, consent) with section pointers. The paper supports both (lines 79, 207, 220).
  - Licenses: state Bactrian-X's and Aya's licenses explicitly in the paper, not only "under their original licenses" (line 220).
【What would move me to accept】Named models and prompts in an appendix; per-language pool table.
```

---

## 3. Verification pass (verifier, not a referee)

Each major concern is tested against the text with three filters: real, specific, addressable.

| ID | Concern | Verdict | Evidence / reason |
|---|---|---|---|
| R1-M1 | Yoruba not covered by any benchmark; 18-language and tier claims mis-specified | **kept** | Line 85: "Each of our 18 languages is covered by at least one benchmark." Line 73 lists Yoruba among the six low-resource languages. None of the four cited benchmarks (XCOPA, XStoryCloze, XNLI, MGSM; lines 85, 294–312) includes Yoruba, and the paper names no other evaluation source. The Table 2 caption (line 133) says "tiers average six languages each". **Real, specific, addressable**, and it bears on the headline low-resource claim. |
| R1-M2 | Benchmarks under-measure generation quality | **downgraded** | Real, but the paper partly answers it with the 6-language blind human study (lines 91, 162; α = 0.61) and states the gap in Limitations (line 216: "we do not measure long-form generation quality ... in most languages"). Worth doing, but it does not overturn the conclusions. → minor. |
| R1-M3 | ρ tuned on benchmarks | **dropped** | Answered in the text. Line 198: "The optimum was chosen on the held-out pool instructions, not on the benchmarks." Line 79: hyperparameters chosen "using a held-out set of 2,000 pool instructions". |
| R2-M1 | Single, dated model family (Llama 2) | **kept** | Line 79: "We fine-tune Llama 2 7B and 13B". Line 216 concedes it ("All models come from one family, Llama 2"). Conceding a limitation is not penalized as a soundness flaw (ARR checklist guidance), but it does limit the generality and excitement that decide Conference vs Findings. Specific and addressable (one extra base model). Kept as an **excitement/band-deciding** concern, not a soundness one. |
| R2-M2 | Unverifiable citation for per-language quotas; contribution 3 overlap | **kept** | Lines 299–302: "Quillfeather, A. and Brambleton, T. (2024). Per-language quotas for quality filtering of translated corpora. In *Proceedings of the Example Workshop on Multilingual Data Curation*." The venue name reads as a placeholder. Line 43: "we adopt the same principle". Line 33 claims the quota's necessity as a contribution. Real (the bibliography entry as written cannot be verified), specific, addressable (replace or verify, recast contribution 3). |
| R2-M3 | No reference-free QE baseline (e.g., CometKiwi) | **downgraded** | Real: line 82 lists no QE baseline. But line 46 states a different target ("not to score the translation system but to decide whether an instruction-response pair is still coherent"), and Table 3's "Consistency score only" row (46.6) gives partial evidence on the consistency component. A useful extra row, not decision-moving. → minor. |
| R3-M1 | Base-model pretraining contamination unaddressed | **dropped** | Answered on line 76: "The base model's pretraining data cannot be audited, but every condition shares the same base model, so pretraining contamination cannot favor one filter over another." That argument suffices for a comparison between filters. |
| R3-M2 | Reward model, 70B rater and templates unnamed | **downgraded** | Real (lines 64, 82, 85 give descriptions, not identifiers), but the code and selected IDs are released (line 94), so the XQF subset itself can be reproduced. An appendix fix, not a threat to the conclusions. → minor. |

**Tally:** 8 major concerns raised → **kept 3** (R1-M1, R2-M1, R2-M2) · **downgraded 3** (R1-M2, R2-M3, R3-M2) · **dropped 2** (R1-M3, R3-M1).

I also re-derived the numbers in passing, and none failed. Every Avg in Table 1 equals the mean of its four benchmark cells. The ablation deltas match the text (−0.6 without normalization, −1.2 without the quota; line 188). The human-eval shares sum to 100. The 1,647 removed examples are 0.4% of the pre-scan pool. The cost-recovery claim holds: 445 h of scoring vs. about 224 h saved per filtered 7B run (line 207), so roughly two runs.

---

## 4. AE synthesis

```text
【Venue】ACL 2027 via ARR (January 2027 cycle) — form B; Findings is judged on soundness + reproducibility, Conference adds novelty/impact (review-forms.md B; acl-review-process)
【Desk-screen】send out; desk-reject risk LOW (preflight GO; Limitations present; anonymized repo)
【Decision band】Findings (Overall ≈ 3) as submitted; Conference plausible after fixes
【Decisive issues】
  1. Evaluation coverage vs. the 18-language claim (R1-M1). Yoruba is in none of XCOPA, XStoryCloze, XNLI or MGSM, yet line 85 says all 18 languages are covered, Table 2 averages "six languages" per tier, and §5 runs an 18-language Holm family. A multilingual-NLP reviewer will catch this, and it is the kind of confident factual error that pulls a meta-review's Soundness to 3.
     owner: acl-experiments → add a Yoruba evaluation source or recompute over 17 languages; publish a per-language × benchmark coverage table and the per-language score block.
  2. Generality on a current base model (R2-M1). The single 2023 family caps Excitement, which is what separates Conference from Findings.
     owner: acl-experiments → rerun full pool / IFD / XQF on one current multilingual 7–8B base (three seeds; the cached translations make this cheap, line 207).
  3. Positioning of the quota idea (R2-M2). The prior-work citation for per-language quotas cannot be verified, and contribution 3 depends on it.
     owner: acl-related-work → verify or replace the citation (Anthology-first), recast contribution 3 as confirmation for instruction data, run the freshness sweep.
【Secondary issues】open-ended multilingual evaluation (LLM judge calibrated on the existing human labels); CometKiwi-style QE baseline on the translated portion; IFD retention curve; CI/sign test for the human preference; name the reward model, the 70B rater and the prompts; per-language pool table; rewrite the circular argument on line 159; render Figures 1–2.
【Author action plan】(ordered)
  1. acl-experiments — resolve Yoruba coverage; correct line 85, the Table 2 caption, §5 and the abstract; add the per-language appendix table.
  2. acl-experiments — one current multilingual base model for the main comparison (Table 1 subset + Table 2).
  3. acl-related-work — fix the quota citation, recast contribution 3, run the freshness sweep; optionally frame against the ACL 2027 homogenization theme.
  4. acl-experiments — QE baseline + IFD retention curve + LLM-judge open-ended evaluation (secondary).
  5. acl-reproducibility — name the models and prompts, add the pool-composition table, and fill checklist sections C/D with pointers.
  (No econometric execution bridge applies; these are re-runs and re-scores of cached model outputs.)
【Calibration caveats】Inline panel, so the referees may anchor on each other. The Yoruba finding rests on the standard public language lists of the four benchmarks; if the authors used an extended release, the fix is disclosure rather than recomputation. The Llama 2 concern is a judgment about ACL 2027 reviewer expectations, not a rule. ARR outcomes depend heavily on reviewer assignment, so treat the band as indicative.
```

```json
{"decision_band": "Findings (ARR Overall ~3); Conference reachable after fixes", "kept_major_concerns": [{"id": "R1-M1", "lens": "soundness/evaluation", "location": "§4 Evaluation line 85; Table 2 caption line 133; §5 Significance line 129; abstract line 17", "concern": "Yoruba is not covered by any of the four benchmarks (XCOPA, XStoryCloze, XNLI, MGSM), so the claim that all 18 languages are evaluated, the six-language low-resource tier average and the 18-language Holm-corrected significance counts cannot be computed as described."}, {"id": "R2-M1", "lens": "excitement/novelty", "location": "§4 Models line 79; Conclusion line 212; Limitations line 216", "concern": "All results use a single, dated base-model family (Llama 2 7B/13B), so the generality of the gains on current multilingual base models is unshown, which caps excitement for an ACL 2027 main-conference paper."}, {"id": "R2-M2", "lens": "excitement/novelty", "location": "§2 line 43; contribution 3 line 33; bibliography lines 299-302", "concern": "The per-language quota principle is credited to an unverifiable reference (Quillfeather and Brambleton 2024, 'Example Workshop'), and contribution 3 rests on that idea, so both the citation and the novelty claim need repair."}], "downgraded": [{"id": "R1-M2", "lens": "soundness/evaluation", "location": "§4 Evaluation line 85; §5 Human evaluation line 162", "concern": "Instruction-tuning quality is measured mainly with classification/short-answer benchmarks; partly answered by the 6-language human study and Limitations line 216."}, {"id": "R2-M3", "lens": "excitement/novelty", "location": "§2 line 46; §4 Baselines line 82", "concern": "No reference-free QE baseline (e.g., CometKiwi) on the translated portion; useful but not decision-moving given line 46 and the consistency-only ablation."}, {"id": "R3-M2", "lens": "reproducibility", "location": "§3.2 line 64; §4 lines 82, 85", "concern": "Reward model, 70B rater and prompt templates are not identified; appendix fix, code and selected IDs are released (line 94)."}], "dropped": [{"id": "R1-M3", "lens": "soundness/evaluation", "location": "§6 line 198", "concern": "Retention rate tuned on benchmarks; refuted by line 198 ('chosen on the held-out pool instructions, not on the benchmarks')."}, {"id": "R3-M1", "lens": "reproducibility", "location": "§4 line 76", "concern": "Base-model pretraining contamination unaddressed; refuted by line 76 (shared base model cannot favor one filter)."}]}
```
