# Simulated referee panel — "Training on the Margin: Lottery Evidence on the Earnings Returns to Sectoral Job Training"

*Inline panel: one agent played the AE, then each referee in turn, then the verifier. Each referee report was written before the next lens was taken up, but the referees may still anchor on each other. This is a rehearsal. It predicts the attack surface and a decision band, not an outcome.*

```text
【Venue / family】The Quarterly Journal of Economics (top-5 general interest) / form C, economics & finance journals (calibrated 2026-11-23)
【Desk-screen】send out in this rehearsal, but desk-reject risk HIGH: a skim-level editor will see the exclusion restriction waved away in §4.2
【Referee forms】R1 (identification): reject · R2 (contribution/general interest): major revision (borderline reject) · R3 (inference/robustness): major revision
【Verification】7 major concerns → kept 6 (5 distinct after merging R3-M2 into R1-M2) · downgraded 1 · dropped 0
【Decision band】reject (in current form). A revision could clear it in principle, but QJE rarely grants the round for a fundamental identification hole
【Decisive issues】(1) exclusion restriction violated by the $1,500 bonus and career navigator given to all winners (R1-M1);
  (2) treatment-dependent UI linkage, so the outcome sample is not randomized and sample counts do not reconcile (R1-M2 / R3-M2);
  (3) conclusion converts a complier LATE into a population ATE and a $640M scale-up claim (R2-M1)
```

---

## 0. Calibration (from the pack, not memory)

- **Bar.** QJE has about 1–4% acceptance, a ~60%+ desk-reject rate and ~2-week desk decisions by five Harvard editors (`Quarterly-Journal-of-Economics-Skills/resources/official-source-map.md`; `qje-referee-strategy`). Referees are typically two. The paper usually gets one substantive shot. "Fundamentals must be resolved before submission, not deferred to R&R."
- **Identification bar** (`qje-identification`, Branch B IV / Branch D RCT). Exclusion must be argued in three registers (theory, institutions, falsification). Report the reduced form and OLS. State the LATE/complier interpretation, with "the claim never exceeds what the design supports". Attrition analysis is required, with Lee bounds if attrition is differential. Use multiple-hypothesis adjustment. Weak-IV-robust inference (AR) whenever the first stage is not strong.
- **Robustness bar** (`qje-robustness`): selection and attrition come second on the priority ladder, right after identification threats.
- **Form C** (`review-forms.md`). Lenses: identification · contribution/general interest · inference/robustness.
- **Preflight** (`agent2-paperB.tex.preflight.json`): verdict NO-GO on mechanics, owned by the author and not re-litigated here. It found: `\cite{klinewalters2016}` with no bib entry (FAIL); a `[TODO: confirm the fall 2017 intake counts]` left in §2 (FAIL); uncited `ashenfelter1978`; Table 4 (`tab:het`) with no SE note; `fig:distribution` never referenced; a hand-incremented table counter; and the abstract's "19.4 percent" not matching the body. Note for the author: the body's 3,049/18,640 = 16.4% is right, so the abstract is the error. The panel treats these as known and fixable.

## 1. AE desk-screen

- **Scope / fit.** Returns to job training is a classic general-interest labour question. Sectoral training at scale by a public agency is policy-relevant and squarely within the editors' interests.
- **Variation named early.** §1 ¶3 says "admission lotteries … within center-by-intake-cohort strata". The first stage is very strong (effective F = 4,853). This passes the two-page skim.
- **Fatal-flaw scan.** Two items a skim-level editor is likely to catch:
  - §4.2: "lottery winners received a \$1,500 job-search bonus … and were assigned a dedicated career navigator for twelve months, whether or not they ultimately enrolled. Because the offer was randomly assigned, these features do not threaten identification". This conflates independence with exclusion.
  - §3: "The linkage rate is 89.6 percent for lottery winners and 81.3 percent for lottery losers".
- **Delta vs closest work.** The stated delta against WorkAdvance (Katz et al. 2022) is "larger cohorts, a public provider, and a longer follow-up" (§1 ¶6). That is a difference of setting. The general-interest lesson ("does sectoral training work at public scale?") is promised but not delivered as a test.
- **Desk-reject risk: high.** It is not a clear-cut desk reject, because the lottery, the administrative data and the 7-year follow-up are strong assets, and both flaws can be fixed before submission. Sent out in rehearsal to map the full attack surface.

---

## 2. Referee 1 — identification lens (form C)

**Report to the authors**

*Summary.* The sample is 11,482 applicants to oversubscribed centres of a statewide sectoral training programme (2012–2017), lotteried within 108 centre × intake strata. The offer raises enrolment by 62.7 pp. The 2SLS estimates are +\$3,049 per year in years 3–5 (16.4% of the complier control mean), +4.1 pp employment, +12.6 pp target-sector employment and −\$1,670 in year 1. AR sets are close to the Wald intervals. Returns are larger for low prior earners.

*Assessment.* The randomization is credible: strata fixed effects are included, balance holds (joint p = 0.64), and the pre-period quarterly earnings are flat between arms (§5.3). The problem is that what is randomized is not enrolment alone, and the analysis sample is not the randomized sample.

*Main concerns*

**R1-M1 — The exclusion restriction is violated by design. The offer bundles a cash bonus and a 12-month career navigator with the seat.**
- *Where:* §4.2 ¶2: "lottery winners received a \$1,500 job-search bonus, paid when they returned the signed offer letter, and were assigned a dedicated career navigator for twelve months, whether or not they ultimately enrolled. Because the offer was randomly assigned, these features do not threaten identification, and we interpret the 2SLS estimate as the return to program enrollment."
- *Why it matters:* Random assignment delivers independence, not exclusion. A navigator whose job is placement plausibly raises employment and earnings on its own, including for winners who never enrol (never-takers) and for compliers beyond what training does. The bonus affects job-search and labour supply in year 1. The Wald ratio ρ/π then attributes the effect of the whole bundle to enrolment and inflates the per-enrollee "return". With π = 0.627, a direct offer effect of, say, \$300 per year on everyone moves β by about \$480. The Kitagawa (2015) test (§4.2 ¶3) does not help: it detects violations that break the testable inequalities, not a uniform direct effect of Z on Y.
- *What would resolve it:* (a) Re-label the estimand as the effect of the offer package (ITT/RF), with enrolment-scaled estimates as an upper bound. (b) Use navigator-contact and bonus records to show the channel's first stage among non-enrollees. (c) Report outcomes of winners who did not enrol relative to an estimable never-taker benchmark. (d) Bound β under plausibly-exogenous direct effects (Conley–Hansen–Rossi). (e) Exploit any cohorts or centres where the bonus or navigator was absent or differed.
- *Owner:* `qje-identification` (Branch B exclusion "in three registers"; execution bridge: `ivreg` + sensitivity via `sensitivity` / plausibly-exogenous bounds).

**R1-M2 — Linkage to UI records depends on treatment, so the outcome sample is no longer randomized.**
- *Where:* §3 ¶2: "The linkage rate is 89.6 percent for lottery winners and 81.3 percent for lottery losers, because winners' program intake forms collected verified identifiers. … restrict the analysis to linked applicants."
- *Why it matters:* Selection into the outcome sample is caused by the offer, an 8.3 pp differential. Losers who link are positively selected on identifier quality, which is plausibly correlated with formal-sector attachment and earnings. Balance (Table 1) is shown for all 11,482 applicants, not for the linked sample. The paper cites Lee (2009) in §1 but never applies it.
- *Sample counts do not reconcile.* 0.896 × 5,214 + 0.813 × 6,268 ≈ 9,768 linked applicants, yet the outcome sample is 11,161 (§3 ¶2; Tables 2–4). Either the rates or the counts are wrong.
- *What would resolve it:* Reconcile the counts. Show balance and the first stage in the linked sample. Report Lee bounds for the main outcomes. Re-link losers using the agency's other identifiers. Show that the result holds in strata with near-equal linkage.
- *Owner:* `qje-identification` (Branch D: attrition, Lee bounds); secondary owner `qje-robustness` (selection & sample).

*Minor concerns*
1. *OLS vs 2SLS gap interpretation.* §5.2 says "the naive comparison overstates the return by about 60 percent" because of selection. But OLS compares enrollees (compliers plus always-takers) with non-enrollees (compliers plus never-takers), so the gap mixes selection and effect heterogeneity. Soften, or decompose using κ-weighting.
2. *Monotonicity.* Losers could enrol from the waitlist or by reapplying (§2). Explain why no applicant enrols *because* they lost, for instance by reapplying to a preferred track. Probably fine.
3. *In-state UI coverage.* Out-of-state, federal and self-employment earnings are coded zero (§3). If navigator help or credentials raise out-of-state mobility differentially, earnings are mismeasured by arm. Discuss, or use NDNH/IRS data if available.

**Confidential letter to the editor.** Reject in current form. The lottery is real and the data are excellent. But the headline parameter, the return to enrolment, is not identified as stated, because the offer includes a cash bonus and a 12-month career navigator that reach non-enrollees. The outcome sample is also selected by treatment through differential UI linkage. Both are fixable in principle (re-label the estimand, bound, re-link), but they are fundamentals that should be fixed before a QJE submission, not in revision.

```text
【Lens】identification
【One-line summary】Lottery IV for sectoral training at a public provider: +$3,049/yr in years 3–5.
【Recommendation】reject
【Major concerns】R1-M1 exclusion violated by bonus + navigator (§4.2 ¶2) · R1-M2 treatment-dependent linkage; counts don't reconcile (§3 ¶2)
【Minor concerns】OLS–2SLS gap ≠ selection only; monotonicity via reapplication; in-state UI coverage
【What would move me to accept】An estimand the bundle supports (ITT plus bounded β), Lee-bounded results on a reconciled linked sample with linked-sample balance.
```

---

## 3. Referee 2 — contribution / general-interest lens (form C)

**Report to the authors**

*Summary.* As above. The pitch is that lottery evidence shows sectoral training works when run at scale by a public agency, not only in nonprofit demonstrations.

*Contribution relative to the closest work.*
- **LaLonde (1986); Heckman, LaLonde, and Smith (1999); Card, Kluve, and Weber (2018).** These document small, slow-building average ALMP effects. The paper's motivation is correctly drawn from them.
- **Schochet, Burghardt, and McConnell (2008), Job Corps.** Experimental, public, large, with short-lived effects. A natural comparison for "public at scale" that the paper cites but does not engage.
- **Katz, Roth, Hendra, and Schaberg (2022), WorkAdvance.** The paper's main comparator.
- **Not cited.** The sectoral RCT evidence that defines the frontier: Project QUEST, Year Up, Per Scholas and the Sectoral Employment Impact Study (Maguire et al.; Roder and Elliott; Fein and Hamadyk). Also Heckman, Hohmann, Smith, and Khoo (2000, QJE) on substitution bias in the JTPA experiment, which is exactly the issue §5.1 addresses via Kline and Walters (2016). That citation is itself missing from the bibliography (preflight).

*Main concerns*

**R2-M1 — The conclusion claims a population ATE and a statewide scale-up the design cannot support, and the promised displacement discussion never appears.**
- *Where:* §6 ¶2: "Because the lotteries randomize access, our estimate of \$3,049 per year is the average return to training for unemployed workers in the state. Scaling the program to the roughly 210,000 workers who file UI claims in the state each year would therefore raise aggregate annual earnings by about \$640 million, and similar programs would deliver comparable returns in other states." Also §1 ¶6: "gains for participants can come partly at the expense of nonparticipants \citep{crepon2013}, a point we return to in the conclusion". The conclusion contains no such discussion.
- *Why it matters:* (i) β is a LATE for compliers among *applicants* to *oversubscribed* centres who pass a skills screen (§2). It is not the ATE for all UI claimants, most of whom would never apply. (ii) The \$640M figure (3,049 × 210,000) assumes no displacement and constant returns at roughly 20× the programme's scale. Crépon et al. (2013), which the paper cites, shows that displacement can be first-order in exactly this setting. (iii) "Other states" is unsupported. At QJE the general-interest case is precisely "does it work at scale?", so an untested scale claim is a central weakness, not a stylistic one.
- *What would resolve it:* Restate the conclusion as a complier LATE and characterize compliers (κ-weighting, Abadie 2002). Use the variation in offer rates across the 108 strata (28–67%, §2) and cohort sizes to test for displacement of losers within centre-sector labour markets. Delete or explicitly bound the aggregate extrapolation.
- *Owner:* `qje-writing-style` (claims ≤ design) + `qje-identification` ("LATE / external-validity interpretation stated explicitly"); displacement test under `qje-robustness`.

**R2-M2 — The delta is a difference of setting, and the closest sectoral RCTs are not engaged.**
- *Where:* §1 ¶6: "Relative to the WorkAdvance demonstration … our setting involves larger cohorts, a public provider, and a longer follow-up." The references omit Project QUEST, Year Up, Per Scholas and Heckman et al. (2000).
- *Why it matters:* Several RCTs already report large, persistent earnings gains from sectoral training (some with 6–11-year follow-ups). Without them, the reader cannot tell whether "public provider" changes the answer. Showing that it does is the only way the paper becomes QJE-general rather than a solid field-journal evaluation.
- *What would resolve it:* Engage those papers quantitatively. Benchmark the \$3,049 against their effects per dollar of cost. Frame the contribution around something only this setting can show: public delivery, scale and capacity variation, and substitution with other public training.
- *Owner:* `qje-literature-positioning` / `qje-topic-selection`.

*Minor concerns*
1. *Cost–benefit timing.* §6 ¶1 says gains exceed cost plus forgone earnings "within about four years". Cost is \$6,800 + \$1,670 = \$8,470. Year-2 gains are partial (overtaking in quarter 6), and years 3–4 add about \$6,100, so breakeven is closer to year 5. No discounting is applied. Show the cumulative calculation.
2. *Mechanism wording.* "full-time, credentialed jobs rather than adding hours" (§5.3) cannot be read off UI records, which report earnings, not hours or credentials. Soften, or use credential records.
3. *Heterogeneity framing.* The abstract headlines larger returns for low prior earners. Pre-application earnings are subject to the Ashenfelter dip (Ashenfelter 1978, uncited per preflight), so a split on the prior year partly sorts on transitory shocks. Split on earnings 2–3 years before application as well.

**Confidential letter to the editor.** Major revision, bordering on reject on general-interest grounds. The data and lottery are valuable. But the paper's QJE case (public sectoral training at scale) is asserted rather than tested, the conclusion over-extrapolates a complier LATE to all UI claimants and other states, and the closest sectoral RCT literature is absent. A rewrite around a scale/displacement test could make it general-interest.

```text
【Lens】contribution / general interest
【One-line summary】First lottery evidence on a public, at-scale sectoral training programme.
【Recommendation】major (borderline reject)
【Major concerns】R2-M1 LATE→population ATE + $640M scale-up; displacement promised, absent (§6 ¶2; §1 ¶6) · R2-M2 setting-only delta; closest sectoral RCTs and Heckman et al. (2000) missing (§1 ¶6)
【Minor concerns】breakeven ~year 5 not 4; hours/credential claim from UI; Ashenfelter-dip heterogeneity split
【What would move me to accept】A displacement/scale test using strata offer-rate variation, a complier-LATE conclusion, and quantitative positioning against QUEST / Year Up / Per Scholas.
```

---

## 4. Referee 3 — inference / robustness lens (form C)

**Report to the authors**

*Summary.* As above. My focus is inference, sample accounting and robustness.

*Assessment.* The main lottery inference is fine. Individual-level randomization within strata justifies heteroskedasticity-robust SEs (§4.3). The first stage is overwhelming. The AR sets are appropriately reported (Table 3). The specification checks in §5.1 are sensible: without covariates, years 3–7, and reapplicants counted as untreated. The Kline–Walters rescaling for substitute training is a strength.

*Main concerns*

**R3-M1 — The external-validity IV (distance) is weak, yet it is reported with conventional inference.**
- *Where:* §5.2: "Each additional 10 kilometers of distance reduces enrollment by 1.1 percentage points (standard error 0.6). The 2SLS estimate … is \$9,840 (standard error 4,310), statistically significant at the 5 percent level using conventional standard errors, which suggests that the returns to training at non-oversubscribed centers are, if anything, larger."
- *Why it matters:* The first-stage t is about 1.8 (F ≈ 3.4), far below any weak-IV threshold. §4.3 itself warns that "conventional 2SLS inference can be misleading when instruments are weak". The AR set will be very wide and plausibly unbounded. The point estimate (3× the lottery estimate) is what weak-IV bias toward OLS looks like (OLS = \$4,870, with bias also from residential sorting). Distance exclusion within commuting zones is defended with only two controls. The "if anything, larger" external-validity conclusion is unsupported.
- *What would resolve it:* Report the effective F and the AR set. If it is uninformative, say so, or drop the exercise. Alternatively replace it with a reweighting of lottery compliers to the 2018–2019 applicant covariates.
- *Owner:* `qje-identification` (Branch B weak-IV; execution bridge: `effective_f_test` + `anderson_rubin_ci`).

**R3-M2 — The estimation sample and the 2SLS inputs come from different samples.**
- *Where:* Table 2 col. 1 has the first stage on N = 11,482 (all applicants). Table 3 has 2SLS on N = 11,161 but reports "Effective first-stage F 4,853", which is (0.627/0.009)², the all-applicant first stage. Every 2SLS coefficient equals Table 2's linked-sample RF divided by 0.627 (e.g., 1,912/0.627 = 3,049).
- *Why it matters:* The reported 2SLS appears to divide a linked-sample reduced form by a full-sample first stage. Under differential linkage (R1-M2) the linked-sample first stage differs, so β and its SE are mis-computed, and the reported F is not the estimation-sample F.
- *What would resolve it:* Estimate the first stage, F and 2SLS on the same (linked) sample, report both, and reconcile N with the stated linkage rates.
- *Owner:* `qje-robustness` (selection & sample) / `qje-replication-package` (sample accounting).

**R3-M3 — Multiple outcomes and subgroups without adjustment or a pre-analysis plan.**
- *Where:* Tables 3–4: four outcomes and three heterogeneity dimensions. The only significant difference is prior earnings (p = 0.02, Table 4 Panel B), and it is headlined in the abstract.
- *Why it matters:* With three heterogeneity tests, a Bonferroni-adjusted p is about 0.06. No pre-analysis plan is referenced.
- *What would resolve it:* Romano–Wolf or sharpened q-values across outcomes and subgroups, plus a statement on pre-specification.
- *Owner:* `qje-robustness` (execution bridge: `romano_wolf`).

*Minor concerns*
1. Cohorts lotteried in 2016–2017 have years 3–5 in 2019–2022 (COVID). Show the main estimate excluding pandemic quarters, or by cohort.
2. The year-3–7 robustness (§5.1) uses a different cohort mix. Report the years 3–5 estimate on that same subsample so the two are comparable.
3. The substitute-training bound (§5.1) relies on substitute training having nonnegative returns. Cite evidence for the specific substitute programmes, given the mixed ALMP literature the paper itself reviews.
4. The online appendix is referenced (Appendix C) but not included. QJE expects an extensive appendix in the same submission PDF.

**Confidential letter to the editor.** Major revision. The lottery inference is sound. But the external-validity IV is weak and reported with conventional SEs, contrary to the paper's own §4.3, and the 2SLS appears to combine a linked-sample reduced form with a full-sample first stage. Combined with the differential-linkage problem, I am not confident the reported β and SE are those of a well-defined estimation sample.

```text
【Lens】inference / robustness
【One-line summary】Strong lottery first stage; sample accounting and the secondary IV are the weak points.
【Recommendation】major
【Major concerns】R3-M1 weak distance IV with conventional inference (§5.2) · R3-M2 2SLS mixes samples (Tables 2–3) · R3-M3 multiple testing (Tables 3–4)
【Minor concerns】COVID in outcome window; years 3–7 cohort comparability; substitute-training returns; appendix missing
【What would move me to accept】Same-sample first stage/F/2SLS with reconciled N, AR set for the distance IV (or drop it), adjusted p-values.
```

---

## 5. Verification pass (verifier, not a referee)

| ID | Verdict | Evidence (quoted) and reason |
|---|---|---|
| **R1-M1** exclusion violated by bonus + navigator | **kept** | §4.2: "received a \$1,500 job-search bonus … and were assigned a dedicated career navigator for twelve months, whether or not they ultimately enrolled. Because the offer was randomly assigned, these features do not threaten identification." Random assignment does not imply exclusion. No passage measures or bounds the direct channel, and the Kitagawa test (§4.2 ¶3) is not informative about a uniform direct effect. Real, specific (§4.2; every 2SLS estimate), addressable (re-label the estimand, bounds, navigator records). |
| **R1-M2** treatment-dependent linkage | **kept** | §3: "89.6 percent for lottery winners and 81.3 percent for lottery losers, because winners' program intake forms collected verified identifiers … restrict the analysis to linked applicants." Table 1 balance is on 11,482 applicants, not the linked sample. Lee (2009) is cited only in §1. The arithmetic 0.896×5,214 + 0.813×6,268 ≈ 9,768 ≠ 11,161 confirms an accounting problem. Real, specific, addressable. |
| **R2-M1** LATE → population ATE, \$640M, displacement promised but absent | **kept** | §6: "our estimate of \$3,049 per year is the average return to training for unemployed workers in the state … would therefore raise aggregate annual earnings by about \$640 million, and similar programs would deliver comparable returns in other states." §1: "a point we return to in the conclusion". The conclusion has no displacement discussion. Real, specific, addressable (rewrite plus a strata offer-rate displacement test). |
| **R2-M2** setting-only delta; closest sectoral RCTs missing | **kept** | §1: "our setting involves larger cohorts, a public provider, and a longer follow-up." The bibliography has 15 entries, none on QUEST, Year Up or Per Scholas, and no Heckman et al. (2000). At QJE the general-interest delta is decision-relevant (`qje-referee-strategy`: the "so what?" skeptic), so it is kept as major, though it is secondary to the identification issues. |
| **R3-M1** weak distance IV, conventional inference | **kept** | §5.2: "reduces enrollment by 1.1 percentage points (standard error 0.6) … statistically significant at the 5 percent level using conventional standard errors". This contradicts §4.3: "conventional 2SLS inference can be misleading when instruments are weak". It supports a substantive claim (returns "if anything, larger" elsewhere). Real, specific, addressable. Not decisive, because it is a secondary exercise. |
| **R3-M2** 2SLS mixes samples | **kept (merged into R1-M2 in synthesis)** | Table 2 col. 1 has N = 11,482. Table 3 has N = 11,161 with "Effective first-stage F 4,853" = (0.627/0.009)². 1,912/0.627 = 3,049 exactly, which would hold only if the linked-sample first stage were identical to the full-sample one despite an 8.3 pp linkage gap. Real and specific. It shares a root cause and a fix with R1-M2. |
| **R3-M3** multiple testing | **downgraded → minor** | Real: Table 4 has three p-values for equality (0.55, 0.02, 0.60), with no adjustment. But the main effects are very strong (t ≈ 5 for earnings, 11 for target-sector employment), so the adjustment only affects the heterogeneity headline. Reporting fix: adjust, or soften the abstract sentence. |

*Also reviewed and not raised as major:* the abstract/body 19.4% vs 16.4% mismatch, the missing Kline–Walters bib entry and the TODO marker are preflight items already flagged. Cost–benefit timing and the hours wording are minor (R2 minors 1–2).

**Tally:** 7 major concerns raised (R1: 2, R2: 2, R3: 3); kept 6 (R3-M2 merged with R1-M2, leaving 5 distinct issues), downgraded 1, dropped 0.

---

## 6. AE synthesis

```text
【Venue】The Quarterly Journal of Economics. ~1–4% acceptance, ~60%+ desk rejection, ~2-week desk screen; fundamentals must be fixed
  pre-submission (qje-referee-strategy; official-source-map 2026-11-23)
【Desk-screen】sent out in rehearsal; desk-reject risk HIGH (the §4.2 exclusion sentence and §3 linkage rates are visible on a skim)
【Decision band】reject (in current form)
【Decisive issues (1–3)】
  1. R1-M1. Exclusion restriction: the offer bundles a $1,500 bonus and a 12-month navigator for all winners, so 2SLS does not identify the return to enrolment.
     Owner: qje-identification (Branch B, exclusion in three registers). Fix: re-label as the offer-package ITT/RF; use navigator and bonus records to show
     the channel among non-enrollees; plausibly-exogenous (Conley–Hansen–Rossi) bounds on β; exploit any centre/cohort variation in the bundle.
     Execution bridge: ivreg + sensitivity.
  2. R1-M2 + R3-M2. Treatment-dependent UI linkage (89.6% vs 81.3%), N that does not reconcile (≈9,768 implied vs 11,161 reported), and a 2SLS
     that divides a linked-sample RF by a full-sample first stage. Owner: qje-identification (Branch D attrition) + qje-robustness.
     Fix: reconcile counts; linked-sample balance and first stage; Lee bounds; re-link losers; same-sample 2SLS with its own effective F and AR set.
     Execution bridge: ivreg / effective_f_test / anderson_rubin_ci on the linked sample.
  3. R2-M1. The conclusion turns a complier LATE into "the average return … for unemployed workers in the state", plus a $640M statewide and
     cross-state scale-up, while the promised displacement discussion is absent. Owner: qje-writing-style + qje-identification (claims ≤ design).
     Fix: complier characterization (κ-weighting); displacement test from the 28–67% strata offer-rate variation; drop or bound the extrapolation.
【Secondary issues】R2-M2 positioning against QUEST / Year Up / Per Scholas and Heckman et al. (2000) (qje-literature-positioning);
  R3-M1 weak distance IV, report AR or drop (qje-identification → anderson_rubin_ci); multiple-testing adjustment (qje-robustness → romano_wolf);
  breakeven timing; hours/credential wording; Ashenfelter-dip split; COVID window; in-state UI coverage; missing online appendix.
  Mechanics (preflight NO-GO): abstract 19.4% → 16.4%; klinewalters2016 bib entry; TODO marker; tab:het SE note; fig:distribution reference; table counter.
【Author action plan】
  1. Clear preflight FAILs (bib entry, TODO) and the abstract number.
  2. Rebuild the linked sample: reconcile N, linked-sample balance, same-sample first stage and 2SLS, Lee bounds (issue 2).
  3. Re-frame the estimand around the offer bundle and bound β against direct navigator/bonus effects (issue 1).
  4. Rewrite the conclusion to the complier LATE; add the strata-level displacement test (issue 3). This also builds the QJE "at scale" case (R2-M2).
  5. Report AR for the distance IV or cut §5.2's claim; adjust for multiple testing; add the appendix to the submission PDF.
【Calibration caveats】Inline panel. Whether the exclusion problem is fatal depends on facts not in the manuscript (navigator take-up by
  non-enrollees; whether the bonus varied). If navigator use by non-enrollees is negligible, issue 1 shrinks to a disclosure-and-bound fix and the
  band could move to major revision. The linkage count discrepancy may be a typo; it still has to be reconciled before submission.
```

```json
{"decision_band": "reject", "kept_major_concerns": [{"id": "R1-M1", "lens": "identification", "location": "§4.2 ¶2 (exclusion restriction); all 2SLS estimates in Tables 3–4", "concern": "Lottery winners received a $1,500 bonus and a 12-month career navigator regardless of enrollment, so the offer affects earnings outside enrollment and 2SLS does not identify the return to enrollment; the paper wrongly argues randomization makes this harmless."}, {"id": "R1-M2", "lens": "identification", "location": "§3 ¶2 (linkage); Table 1", "concern": "UI linkage is treatment-dependent (89.6% winners vs 81.3% losers), so the analysis sample is not randomized, balance is not shown on it, no Lee bounds are reported, and the stated rates imply ~9,768 linked applicants, not the 11,161 used."}, {"id": "R2-M1", "lens": "contribution", "location": "§6 ¶2; §1 ¶6", "concern": "The conclusion presents a complier LATE from oversubscribed-center applicants as the average return for all unemployed workers and extrapolates a $640M statewide (and cross-state) gain, ignoring displacement that the introduction promised to discuss."}, {"id": "R2-M2", "lens": "contribution", "location": "§1 ¶6; References", "concern": "The contribution over WorkAdvance is a difference of setting, and the closest sectoral RCTs (Project QUEST, Year Up, Per Scholas) and Heckman et al. (2000) on substitution bias are not engaged."}, {"id": "R3-M1", "lens": "inference", "location": "§5.2 (distance IV)", "concern": "The external-validity distance IV has a first-stage t of about 1.8 (F≈3.4) yet is reported with conventional significance and used to claim larger returns elsewhere, contradicting the paper's own weak-IV stance in §4.3."}, {"id": "R3-M2", "lens": "inference", "location": "Table 2 col. 1 vs Table 3 (N, effective F); merged with R1-M2", "concern": "The 2SLS estimates equal the linked-sample reduced form divided by the full-sample first stage (F=4,853 from N=11,482), so β, its SE and the reported F are not those of a single estimation sample."}], "downgraded": [{"id": "R3-M3", "lens": "inference", "location": "Tables 3–4; abstract", "concern": "Multiple outcomes and three heterogeneity dimensions without adjustment; the headlined low-earner difference (p=0.02) is ~0.06 after Bonferroni.", "reason": "Main effects very strong; affects only the heterogeneity headline; reporting fix."}], "dropped": []}
```
