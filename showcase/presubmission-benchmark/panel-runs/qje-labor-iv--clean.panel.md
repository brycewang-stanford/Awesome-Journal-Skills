# Simulated Referee Panel — "Training on the Margin: Lottery Evidence on the Earnings Returns to Sectoral Job Training"

> **Inline panel** (one agent played the AE, three referees, and the verifier in turn; each
> referee report was written before the next lens was opened, but some anchoring is possible).
> A rehearsal, not a verdict: it predicts the attack surface and the decision band and does
> not stand in for real peer review.

Manuscript: `agent1-paperB.tex` (line numbers below refer to this file).
Preflight: `agent1-paperB.tex.preflight.json`, verdict **GO**, no findings. Anonymization was not checked; see Secondary issues.

---

## 【Venue / family】
The Quarterly Journal of Economics (top-5 general interest) / **form C** (economics: prose report to authors + confidential letter; reject · major revision · minor revision · accept). Calibrated 2026-11-23 from `Quarterly-Journal-of-Economics-Skills/resources/official-source-map.md` and the pack's skills:
- *Venue facts (source map):* Editor screening with possible rejection without review, otherwise usually two referees; ~2-week desk decisions; ~1–4% acceptance and ~60%+ desk rejection (secondary sources); manuscripts not anonymized (contributor names and word count on the first page); abstract ≤250 words with JEL codes; AER-style data policy with QJE Dataverse deposit and a cover letter flagging proprietary data.
- *Bar for this design:* `qje-referee-strategy` (identification hawk / "so what?" skeptic / mechanism doubter), `qje-identification` Branch B (IV) and Branch D (lottery/RCT), `qje-robustness`, `qje-submission`, and the shared `reviewer-objection-checklist` §2 (IV).

Lenses (family C): R1 identification · R2 contribution / general interest · R3 inference / robustness.

---

## 1. AE desk-screen

- **Scope / fit:** Labor and public policy with first-order stakes: whether publicly run, at-scale sectoral training raises earnings. QJE has published in this space, e.g. Crépon et al. (2013) and Kline and Walters (2016), both cited. In scope.
- **Two-page skim test (`qje-referee-strategy`):** Passes. The question (line 27), the lottery variation (line 31), and the headline estimate with first stage, effect size and OLS comparison (line 33) all sit on the first two pages.
- **Fatal-flaw scan:** None found.
  - Randomization is within 108 center × cohort strata (line 45), with balance p = 0.64 (Table 1).
  - Linkage is non-differential (0.4 pp, SE 0.3; line 51), with Lee bounds [2,610, 3,390].
  - The first stage is strong (effective F 4,853) and Anderson–Rubin sets are reported.
  - The Kitagawa test does not reject (line 102).
  - Pre-lottery quarterly earnings are flat (line 174).
  - Substitute training is handled with the Kline–Walters rescaling (line 230).
  - Every number spot-checked reconciles: 1,912/0.627 = 3,049; 3,049/18,640 = 16.4%; (0.627/0.009)² ≈ 4,853; 1,912/0.511 = 3,742; subgroup sizes and first stages aggregate to the pooled values; the quarterly gap of $480 × 4 matches the annual reduced form of $1,912.
- **Delta vs closest work:**
  - WorkAdvance (Katz et al. 2022) is the named comparator. The stated delta is a public provider, scale, larger cohorts and longer follow-up (line 37).
  - Year Up, Project QUEST and the Sectoral Employment Impact Study are not discussed.
  - The editor's question will be whether "the sectoral result replicates in a public program" is a broad enough lesson for QJE.

**Desk-screen decision: send out.** **Desk-reject risk: medium.** The design raises no credibility concerns. The risk is general interest: a clean confirmation of a known result in a new setting is the classic top-5 borderline, and the editor will know the sectoral-training literature intimately.

---

## 2. Referee reports (form C + pipeline template)

### Referee 1 — identification

**Report to the authors**

*1. Summary.* Using admission lotteries for 11,482 applicants to a statewide public sectoral training program (2012–2017, 108 strata), the paper instruments enrollment with the offer. The offer raises enrollment by 62.7 pp. Enrollment raises annual earnings in years 3–5 by $3,049 (16.4% of the complier control mean) and target-sector employment by 12.6 pp, after a first-year earnings loss of $1,670. OLS overstates the effect by about 60%.

*2. Contribution vs closest work.* The lottery is a strong design for the question. The paper reports the right IV battery: reduced form, OLS, Montiel Olea–Pflueger effective F, Anderson–Rubin sets, the Kitagawa test, complier means, and Abadie distributional tests.

*3. Main concerns.* **None that I consider major.**
- *Independence* is supported by within-strata randomization and balance (Table 1, joint p = 0.64), plus flat pre-lottery earnings (line 174).
- *Exclusion* is argued institutionally (no stipend or placement attached to the offer) and with falsification tests: no effect on UI claims or on lottery-quarter earnings (line 100).
- *Monotonicity* is plausible, and the Kitagawa test does not reject (line 102).
- The substitute-training issue is correctly framed as a question of estimand, not an exclusion violation. The Kline–Walters bound (line 230) is derived correctly: with β_S ≥ 0, β_P ≥ RF/0.627.

*4. Minor concerns.*
- (a) **Track assignment.** The offer "reserved a seat in a specific track" (line 45), but the draw is at the center × cohort level. Clarify whether applicants chose a track before the draw and whether offer rates varied by track within strata. Add track to the Table 1 balance test and show robustness to center × cohort × track strata (`qje-identification`).
- (b) **Unit of observation.** Some losers "reapplied" (line 45). State whether the 11,482 are unique persons or applications. If a person appears in more than one lottery, use the first application or cluster by person (`qje-identification`).
- (c) **First stage on the analysis sample.** Table 3 reports effective F = 4,853 for N = 11,161, which is identical to the full-sample first stage in Table 2, column 1 (N = 11,482). Report the first stage on the linked sample explicitly (`qje-tables-figures`).
- (d) **Waitlist mechanics.** Explain how waitlisted losers were ordered: by lottery rank or first come, first served. This determines who the 8.9% always-takers among losers are (line 112).
- (e) **Distance IV (§5.2, line 234).** As external-validity evidence it is weak. The exclusion restriction for distance is much less credible than for the lottery, and its compliers differ. Complement it with a complier-characteristics reweighting of the lottery LATE toward the 2018–19 applicant population (`qje-robustness`).

*5. What would move me to accept.* The clarifications in (a)–(d). Nothing in the design needs to be rebuilt.

**【Recommendation】minor revision**

**Confidential letter to the editor (R1).** This is as clean an IV design as one sees: an administrative lottery with a strong first stage, balance, non-differential attrition, falsification tests and weak-IV-robust inference. I found no identification problem that threatens the headline. Whether the paper is QJE-level is a question of general interest, not credibility, and I leave it to the editor. From an identification standpoint, minor revision.

---

### Referee 2 — contribution / general interest

**Report to the authors**

*1. Summary.* Lottery-based evidence that a public, at-scale sectoral training program raises earnings by 16% three to five years out, through entry into the targeted sectors, with the largest gains for low prior earners.

*2. Contribution vs the closest 3–5 papers.*
- **Katz, Roth, Hendra and Schaberg (2022):** WorkAdvance, the only sectoral comparator cited.
- **Year Up (Fein and Hamadyk 2018 and follow-ups)**, **Project QUEST (Roder and Elliott 2019)**, and the **Sectoral Employment Impact Study (Maguire et al. 2010)**: the other RCTs of sectoral programs. Not discussed. Verify the citations before adding them.
- **Card, Kluve and Weber (2018):** ALMP meta-analysis. Cited.
- **Kline and Walters (2016):** substitutes in program evaluation. Cited and used.
- **Crépon et al. (2013):** displacement. Cited.

The delta is a public provider, scale, longer follow-up and the substitute-training adjustment. That delta is real and policy-relevant, because the scale-up question is the open one. It is stated, not exploited.

*3. Main concerns.*

- **R2-M1 — Positioning and benchmarking against the sectoral RCT literature are thin.**
  - *Where:* §1, line 27 ("has produced more encouraging results \citep{katz2022}") and line 37 ("Relative to the WorkAdvance demonstration studied by \citet{katz2022}, our setting involves larger cohorts, a public provider, and a longer follow-up").
  - *Why it matters:* At a top-5 journal the "so what?" referee asks what we learn beyond four existing sectoral RCTs. The paper does not benchmark its 16.4% effect against Year Up, Project QUEST or WorkAdvance, so the reader cannot tell whether public provision at scale delivers smaller, similar or larger returns. That comparison *is* the scale-up lesson. Nor does the paper use its own variation (nine centers, 12 cohorts, varying oversubscription) to say anything about how returns vary with scale or local demand.
  - *Fix:* A benchmarking table or figure of effect sizes and follow-up horizons across the sectoral RCTs. A contribution paragraph naming them. If feasible, heterogeneity by center size or cohort size and by local sector demand, as direct evidence on the scale question.
  - *Owner:* `qje-literature-positioning` / `qje-topic-selection`.

- **R2-M2 — The mechanism claim goes beyond what UI data can show.**
  - *Where:* §4.4, line 215: "The program moves compliers into full-time, credentialed jobs rather than adding hours at their previous wage." Abstract, line 18: "by moving them into higher-paying jobs."
  - *Why it matters:* UI wage records report quarterly earnings and employer industry (line 49), not hours, wages or credentials held on the job. A shift in the earnings distribution from $5–15k to $20–35k is consistent with higher wages *or* with more quarters and hours worked. The sector-switching evidence (target-sector employment +12.6 pp against total employment +4.1 pp) is persuasive. The "full-time, not more hours" part is not identified.
  - *Fix:* Decompose the earnings effect into quarters employed and earnings per employed quarter. Add employer-level pay (for example AKM-style firm premia estimated from the UI data) to test the "higher-paying jobs" channel. Reword line 215 to match what is shown.
  - *Owner:* `qje-theory-model` (mechanism test) / `qje-writing-style`.

*4. Minor concerns.*
- (a) **Cost-benefit arithmetic (line 238).** Break-even "within about four years" does not obviously follow from the reported numbers. The target is cost plus forgone earnings: 6,800 + 1,670 = 8,470. Years 3–4 at about $3,049 each give about $6,100. Year 2 contains the crossover quarter (Q6), so its gain is well below $2,370. Break-even therefore looks closer to five years. Show the calculation.
- (b) **Policy value.** An MVPF-style calculation would sharpen the general-interest payoff. It should include the fiscal externality from taxes and UI, and the substitute-training cost saved, since losers are 11.6 pp more likely to take other public training.
- (c) The abstract sentence on weak-IV-robust sets is uninformative with F ≈ 4,853. Use the space for the scale-up lesson (`qje-writing-style`).

*5. What would move me to accept.* A clear benchmarking of returns against the sectoral RCTs, and a mechanism section that claims only what the data show.

**【Recommendation】major revision**

**Confidential letter to the editor (R2).** The design is excellent and the result is credible. My concern is whether the paper delivers a lesson beyond "sectoral training works when a public agency runs it." Benchmarking against the existing RCTs, together with any evidence on how returns vary with scale, would turn a replication into a scale-up paper. A revision can plausibly clear this. Whether it reaches QJE's general-interest bar is the editor's judgment.

---

### Referee 3 — inference / robustness

**Report to the authors**

*1. Summary.* As above. My focus is precision, specification sensitivity, multiplicity and reproducibility.

*2. Contribution.* I defer to the other reports. The headline is precisely estimated: the AR set is [1,852, 4,252] and the Lee bounds are [2,610, 3,390].

*3. Main concerns.*

- **R3-M1 — The prior-earnings heterogeneity is headlined without a multiplicity adjustment.**
  - *Where:* Abstract, line 18 ("Returns are largest for applicants with low prior earnings"); line 35; Table 4 Panel B ("$p$-value for equality = 0.02", line 200); conclusion, line 238.
  - *Why it matters:* Three heterogeneity dimensions are tested (sex, prior earnings, track) and one rejects, at p = 0.02. A Bonferroni adjustment across the three gives about 0.06. The split also uses *prior-year* earnings, which the Ashenfelter dip (line 174) depresses for recent job losers. "Low prior earnings" may therefore partly mean "recent negative shock" rather than persistently low earnings.
  - *Fix:* Report Romano–Wolf or Bonferroni-adjusted p-values across subgroups. Repeat the split on multi-year baseline earnings (e.g., years −3 to −2). Describe the result as heterogeneity "consistent with" the claim, unless it survives.
  - *Owner:* `qje-robustness` → execution bridge: `romano_wolf`.

*4. Minor concerns.*
- (a) **Outliers.** The text does not say whether earnings are top-coded or winsorized. Show robustness of the mean effect to winsorizing at the 99th percentile and to a log or rank outcome (`qje-robustness`).
- (b) **UI coverage.** UI records miss federal jobs, self-employment and 1099 contract work, which may matter most for the IT track. Discuss the likely direction of the bias.
- (c) **Specification curve.** Covariates in or out and outcome windows are already reported (line 228). Add a panel varying the enrollment-window definition, D within 12 versus 24 months.
- (d) **Replication.** The data are confidential (line 244). The DAS is appropriate. The QJE data policy also requires the cover letter to flag the proprietary data and describe the access route (`qje-replication-package`).

*5. What would move me to accept.* Multiplicity-adjusted heterogeneity and the outlier and specification robustness in the appendix.

**【Recommendation】minor revision**

**Confidential letter to the editor (R3).** The main estimate is precise and robust, and the inference is correct for individual-level randomization within strata. My only substantive point is that the subgroup result in the abstract is not adjusted for multiplicity. That is a framing fix, not a threat to the paper. Minor revision.

---

## 3. Verification pass (verifier, not a referee)

Each major concern was tested against the manuscript text for being **real**, **specific**, and **addressable**.

| ID | Verdict | Evidence / reason |
|---|---|---|
| R2-M1 | **downgraded** | Real: the only sectoral comparator is Katz et al. (2022) (lines 27, 37), and the paper never benchmarks magnitudes against prior sectoral estimates. But the paper does state an explicit delta at line 37 ("larger cohorts, a public provider, and a longer follow-up") and a second contribution on substitutes (line 37, Kline–Walters). The missing benchmarking is a positioning addition that does not threaten any conclusion. Whether the paper is general-interest enough is an editorial judgment that no revision can settle, so it belongs in the desk-screen risk, not in a major concern → minor. |
| R2-M2 | **downgraded** | Real: line 215 says "rather than adding hours at their previous wage," while line 49 confirms the UI data contain earnings and industry, not hours. The supporting mechanism evidence, sector switching (Table 3, columns 2–3), stands. Only the hours/credential sentence is unsupported. The fix is a decomposition table plus rewording → minor. |
| R3-M1 | **downgraded** | Real: line 200 reports Panel B p = 0.02 among three tested dimensions, with no adjustment, and the abstract (line 18) features it. The headline earnings, employment and target-sector effects all have p < 0.01 and do not depend on it. The fix is an adjusted p-value and softer wording → minor. |

**Summary:** 3 major concerns raised → **kept 0 · downgraded 3 · dropped 0**. No concern was dropped as a misreading. All three are real, but none threatens the paper's conclusions.

---

## 4. AE synthesis

**【Desk-screen】** Send out. Desk-reject risk is **medium**, entirely on general interest (a sectoral-training result confirmed at public scale), not on credibility.

**【Referee forms】**
- R1 (identification): minor revision. No major concerns.
- R2 (contribution / general interest): major revision. Two majors raised, both downgraded on verification.
- R3 (inference / robustness): minor revision. One major raised, downgraded.

**【Verification】** 3 majors → kept 0 · downgraded 3 (positioning addition, mechanism overclaim in one sentence, subgroup multiplicity) · dropped 0.

**【Decision band】** **Minor revision**, conditional on the editor judging the paper general-interest. The design, inference and reconciliation of the numbers are clean, and no verified concern threatens the conclusions. The binding QJE risk sits at the editor's desk (general interest), not in the referee reports.

**【Decisive issues (1–3)】** There are no decisive *major* concerns. The three items most likely to move a QJE editor are:

1. **Scale-up positioning and magnitude benchmarking (R2-M1, downgraded).**
   - *Location:* §1, lines 27 and 37.
   - *Why it matters here:* This is what converts a clean replication into a general-interest scale-up result, the lever on the medium desk risk.
   - *Owner:* `qje-literature-positioning` / `qje-topic-selection`.
   - *Fix:* Add a benchmarking exhibit against WorkAdvance, Year Up, Project QUEST and SEIS. Add heterogeneity by center or cohort scale and local sector demand.
2. **Mechanism wording and decomposition (R2-M2, downgraded).**
   - *Location:* Line 215 and abstract, line 18.
   - *Owner:* `qje-theory-model` / `qje-writing-style`.
   - *Fix:* Split the effect into quarters employed and earnings per employed quarter, add employer pay premia, and reword the hours claim.
3. **Multiplicity on the headlined subgroup (R3-M1, downgraded).**
   - *Location:* Table 4 Panel B (line 200); abstract.
   - *Owner:* `qje-robustness` → `romano_wolf`.
   - *Fix:* Report adjusted p-values and a split on multi-year baseline earnings, and soften the abstract.

**【Secondary issues】**
- **Identification clarifications (R1 minors):** track versus strata, unique persons versus applications, the first stage on the linked sample, waitlist ordering, and complier reweighting to strengthen the distance-IV external-validity section.
- **Policy arithmetic:** break-even "within about four years" (line 238) appears closer to five on the reported numbers. Show the calculation and consider an MVPF that includes the substitute-training cost offset.
- **Outcome robustness:** winsorizing or log outcomes, and the direction of any bias from UI coverage gaps.
- **Mechanics the preflight did not check (owner `qje-submission`):**
  - The title page reads "Anonymous Authors" (line 11), and the disclosure statement says disclosures are "provided separately to preserve anonymity" (line 248). QJE's instructions require contributor names, the corresponding author's address and email, and the total word count on the first page, so do not anonymize. Funding and acknowledgments go in an asterisk footnote on the title.
  - A cover letter should flag the confidential UI and program data under the QJE data policy.

**【Author action plan】**
1. De-anonymize the first page and add the word count. Prepare the data-policy cover letter (`qje-submission`).
2. Add the benchmarking exhibit and rewrite the contribution paragraph around the scale-up lesson. Exploit center and cohort scale variation if feasible (`qje-literature-positioning`, `qje-topic-selection`).
3. Add the earnings decomposition and employer pay premia, and reword line 215 and the abstract (`qje-theory-model`, `qje-writing-style`).
4. Run `romano_wolf` on the subgroups and the multi-year-baseline split, and soften the heterogeneity claim (`qje-robustness`).
5. Make the R1 clarifications (track, reapplicants, linked-sample first stage, waitlist) and add complier reweighting to §5.2 (`qje-identification`, `qje-robustness`).
6. Show the break-even arithmetic and add an MVPF (`qje-writing-style`). Stage the replication package (`qje-replication-package`).

**【Calibration caveats】**
- This was an inline panel, so the referees may share blind spots.
- Real first-round QJE decisions are rarely "minor". The band reflects the verified concern set, not the base rate. The realistic distribution is bimodal: a general-interest reject at the desk or editor stage, or an R&R that asks mainly for the positioning and mechanism additions above.
- The acceptance and desk-reject figures for QJE come from secondary sources in the pack's source map.
- The added citations (Year Up, Project QUEST, SEIS, Hendren and Sprung-Keyser's MVPF) are from memory and should be verified before they go into the manuscript.

---

```json
{"decision_band": "minor revision", "kept_major_concerns": [], "downgraded": [{"id": "R2-M1", "lens": "contribution/general interest", "location": "§1 lines 27, 37", "concern": "Positioning relies on a single sectoral comparator (WorkAdvance) with no magnitude benchmarking against Year Up / Project QUEST / SEIS and no use of center/cohort scale variation to deliver the scale-up lesson; an addition, not a threat to conclusions."}, {"id": "R2-M2", "lens": "contribution/general interest", "location": "§4.4 line 215; abstract line 18", "concern": "Claims compliers move into full-time credentialed jobs 'rather than adding hours', which UI earnings/industry records cannot identify; sector-switching evidence stands, so a decomposition plus rewording fixes it."}, {"id": "R3-M1", "lens": "inference/robustness", "location": "Table 4 Panel B line 200; abstract line 18; line 238", "concern": "Headlined prior-earnings heterogeneity (p = 0.02) is one of three tested dimensions with no multiplicity adjustment and uses Ashenfelter-dip-affected prior-year earnings; main effects unaffected."}], "dropped": []}
```
