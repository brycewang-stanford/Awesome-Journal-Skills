# Simulated referee panel — "Paid on Time: Prompt-Payment Mandates, Trade Credit, and Supplier Investment"

*Inline panel: one agent played the AE, then each referee in turn, then the verifier. Each referee report was written before the next lens was taken up, but the referees may still anchor on each other. This is a rehearsal. It predicts the attack surface and a decision band, not an outcome.*

```text
【Venue / family】The Journal of Finance (AFA flagship, top-3 finance) / form C, economics & finance journals (calibrated 2026-11-23)
【Desk-screen】send out. Deciding reason: a general-interest corporate-finance policy question with a named staggered shock and a heterogeneity-robust estimator as the headline. Desk-reject risk: low–medium
【Referee forms】R1 (identification): major revision · R2 (contribution/fit): minor revision · R3 (inference/robustness): minor revision
【Verification】7 major concerns → kept 2 · downgraded 5 · dropped 0
【Decision band】major revision (revise and resubmit). A favourable R&R: both kept issues are re-estimations within the existing data
【Decisive issues】(1) sample defined on post-treatment revenue (R1-M1); (2) anticipation window lies in the reference year, not e = −2 (R1-M2)
```

---

## 0. Calibration (from the pack, not memory)

- **Bar.** JF accepts about 5% and desk-rejects about 33–45% (`Journal-of-Finance-Skills/resources/official-source-map.md`, AFA editor reports). Refereeing is single-blind. The handling editor screens on general interest and identification before assigning 2–3 referees (`jf-referee-strategy`).
- **Identification bar** (`jf-identification`): for a corporate/empirical paper, identification is the binding constraint. Staggered DiD needs a modern estimator (Callaway–Sant'Anna or Sun–Abraham), a Bacon decomposition, pre-trends, anticipation, confounders and economic magnitude. The battery goes in the Internet Appendix.
- **Robustness bar** (`jf-robustness`): 3–6 decisive checks in the body, at least one placebo, and few-cluster inference (wild bootstrap or RI).
- **Form C** (`review-forms.md`): a report to the authors (summary → contribution vs closest 3–5 papers → numbered main concerns → minor concerns) plus a confidential letter. Lenses: identification · contribution/general interest · inference/robustness.
- **Preflight** (`agent2-paperA.md.preflight.json`): verdict GO with no findings. Abstract 91 words (cap 100), disclosure statement present, citations and exhibits consistent. The panel spends nothing on mechanics. The page count is only estimated (~7 pp of source), so it must be confirmed on the compiled PDF with the Internet Appendix bundled.

## 1. AE desk-screen

- **Scope / fit.** Trade credit, financing constraints and corporate investment are core JF corporate finance. The policy angle (should regulators cap payment terms?) gives the general-interest hook the editor reads for in the first three pages.
- **Source of variation, named early.** §1 ¶2 says: "fourteen U.S. states adopted Prompt Supplier Payment Acts … Adoption was staggered across six cohorts." This passes the two-page skim test.
- **Fatal-flaw scan.** None found. The headline estimator is Callaway–Sant'Anna doubly robust with not-yet-treated controls (§4.1). The paper reports TWFE (−4.9), a Bacon decomposition (27% bad-comparison weight), Sun–Abraham (−6.5) and BJS (−7.1). It also reports adoption-timing predictors (Table 2), event-study pre-trends (Table 3, Figure 2), Rambachan–Roth bounds, a placebo on above-threshold firms, census-division × year FE and RI (§6). This is already at the `jf-identification` checklist.
- **Delta vs closest work.** Stated explicitly against Barrot (2016) and Barrot and Nanda (2020): private contracts across all industries, staggered US variation, and the full balance-sheet response (§1 ¶5).
- **Desk-reject risk: low–medium.** The residual risk is "reads like a JFE field paper". The general-interest framing in §1 ¶1 mitigates it. **Send out.**

---

## 2. Referee 1 — identification lens (form C)

**Report to the authors**

*Summary.* The paper studies fourteen state Prompt Supplier Payment Acts (2009–2019). The acts cap payment terms at 45 days for contracts between large buyers and in-state suppliers with revenue below $500M. The sample is 2,614 Compustat supplier firms (548 in adopting states), 2004–2022, and the estimator is Callaway–Sant'Anna with not-yet-treated controls. Adoption cuts receivable days by 6.8 (11.6%), cash by 0.9 pp, short-term debt by 1.1 pp, and raises investment by 2.4 pp of lagged capital (11.2%). The investment response is concentrated among SA-index-constrained firms.

*Contribution (identification angle).* The design is well above the median JF corporate submission. The authors anticipated the staggered-adoption critique and made a heterogeneity-robust estimator the headline. Two design choices still need correcting before the estimates can be read as clean ATTs.

*Main concerns*

**R1-M1 — The estimation sample conditions on a post-treatment outcome (revenue).**
- *Where:* §3 ¶1, "we keep firms with revenue below $500 million in their first sample year and drop firm-years in which revenue exceeds the threshold."
- *Why it matters:* Revenue responds to treatment. If PSPAs relax constraints and raise investment (the paper's own result, Table 3 col. 3), treated firms are more likely to grow past the nominal, unindexed $500M threshold after adoption, and their firm-years are then dropped. That attrition is differential by treatment status and timing. It changes the composition of the treated group in the post-period exactly where the ATT(g,t) are estimated. The direction of the bias is not obvious. For investment it plausibly attenuates, because fast growers leave. For receivable days and short-term debt it is unsigned. A nominal threshold held fixed over 2004–2022 also makes crossing mechanically more likely late in the sample, which loads onto later event times.
- *What would resolve it:* Define coverage on pre-adoption (baseline) revenue and keep firms after they cross, as an intent-to-treat sample. Report post-adoption threshold-crossing and Compustat-exit rates by treatment status. Show Table 3 on the baseline-defined sample, and on a balanced panel as a check.
- *Owner:* `jf-identification` (execution bridge: re-fit `callaway_santanna` on the baseline-defined sample). Secondary owner: `jf-robustness`.

**R1-M2 — The anticipation argument misplaces the enactment window. It falls in the reference year (e = −1), not in e = −2.**
- *Where:* §2 ¶2 says "the act took effect at the start of a fiscal year, six to nine months after enactment." §4.1 says event time is "relative to the year before adoption." §4.2 says "we … include event time e = −2, which spans the enactment window for most states, among the pre-period coefficients." The Table 3 note defines the pre-trend test as "e = −5 to −2." §5.2 confirms that e = 0 is "the effective year."
- *Why it matters:* If e = 0 is the effective year and enactment precedes it by 6–9 months, enactment falls in e = −1 (or e = 0) under any annual timing convention. It never falls in e = −2. The year normalized to zero is therefore the year most exposed to anticipation: buyers renegotiating ahead of the cap, or suppliers committing investment against expected liquidity. The joint pre-trend test (e = −5…−2) cannot detect that by construction. The paper's stated defence of no-anticipation does not hold as written. Any anticipation response contaminates the baseline for every post-period coefficient.
- *What would resolve it:* Re-estimate allowing one period of anticipation, with base period e = −2 (`anticipation = 1` in Callaway–Sant'Anna). Report the e = −1 coefficient for every outcome. Alternatively date treatment at enactment, as a robustness check. Correct the sentence in §4.2.
- *Owner:* `jf-identification` (execution bridge: `callaway_santanna` with anticipation = 1; `honest_did_from_result` on the re-based event study).

*Minor concerns*
1. *The placebo group is not untreated on the buyer side.* Above-threshold firms in adopting states (§6 ¶1) are plausibly large buyers subject to the cap when they buy from small in-state suppliers. Their receivable days are a clean placebo. Their investment is not. Say so, or use a placebo outcome such as payables days to show the buyer-side effect directly.
2. *Coverage mapping.* The statute covers "in-state suppliers" (§2). Treatment is assigned by 10-K headquarters state (§3). Explain how a contract with an out-of-state buyer is reached (choice-of-law, void waivers), or show heterogeneity by the share of in-state customers where the segment files allow it. The first stage (−6.8 days) shows the law binds on average, so this concerns interpretation, not validity.
3. *Spillover test scope.* IA.E tests only suppliers in *neighbouring* non-adopting states. Large buyers are national, so a buyer that lengthens terms for out-of-state suppliers would affect controls anywhere. Test buyer-linked controls (suppliers sharing a major customer with treated suppliers) via the Compustat customer segment files.
4. *Contemporaneous small-business credit policy.* The federal State Small Business Credit Initiative (2010–) was administered by states. Show that the adoption cohorts are not aligned with SSBCI program timing, or add it as a control in the timing regression (Table 2).
5. *Unbalanced panel and the CS estimator.* State how the unbalanced panel is handled (panel vs repeated-cross-section estimator, `allow_unbalanced_panel`). This interacts with R1-M1.

**Confidential letter to the editor.** I recommend major revision. The design is careful and the modern-DiD battery is already there. My concerns are a sample definition that conditions on post-treatment revenue and an anticipation argument that is internally inconsistent: enactment falls in the omitted year, not in e = −2. Both are re-estimations with the authors' existing data. I expect the receivable-days result to survive. The investment result is the one to watch. A revision can plausibly clear both.

```text
【Lens】identification
【One-line summary】State payment-term caps cut supplier receivable days ~7 days and raise constrained suppliers' investment, via CS staggered DiD.
【Recommendation】major
【Major concerns】R1-M1 post-treatment sample selection on revenue (§3 ¶1) · R1-M2 anticipation window = reference year e=−1, not e=−2 (§2 ¶2 vs §4.2)
【Minor concerns】placebo group is a buyer group; in-state coverage mapping; spillover test scope; SSBCI timing; unbalanced-panel handling
【What would move me to accept】Table 3 and Figure 2 re-estimated on a baseline-revenue sample with anticipation = 1, with the e = −1 coefficients reported.
```

---

## 3. Referee 2 — contribution / general-interest lens (form C)

**Report to the authors**

*Summary.* The question is whether capping the payment terms that large buyers impose relaxes small suppliers' financing constraints. The paper exploits staggered US state Prompt Supplier Payment Acts and traces the supplier balance sheet: receivables fall, cash and short-term debt fall, and investment rises, concentrated among constrained firms.

*Contribution relative to the closest work.*
- **Petersen and Rajan (1997); Klapper, Laeven, and Rajan (2012).** These establish who extends trade credit and why. The present paper takes the large-buyer/small-supplier asymmetry as its starting point.
- **Murfin and Njoroge (2015).** Large buyers stretching payables reduces small-supplier investment. This paper offers the regulatory mirror image, with cleaner variation.
- **Barrot (2016).** The French cap on payment terms and entry in trucking. Single-country, single-industry, entry margin.
- **Barrot and Nanda (2020).** QuickPay, government as buyer, employment margin.
- **Breza and Liberman (2017, JF), *not cited*.** Chile's regulation of large supermarket buyers' payment terms to small suppliers, with the organizational and relationship responses. This is the closest *private-buyer regulation* analogue.

The delta is real and stated clearly (§1 ¶5): private contracts across all industries, US staggered variation, and the full balance-sheet chain from receivables to investment. The policy question (should payment terms be capped?) is live in the US and EU, and it gives the paper the general-interest hook JF wants. I consider the contribution adequate for JF.

*Main concerns*

**R2-M1 — The closest regulatory analogue is missing from the positioning.**
- *Where:* §1 ¶5, "Our paper is closest to two studies of payment-term reforms." The reference list has no Breza and Liberman (2017).
- *Why it matters:* Breza and Liberman study a regulation of payment terms imposed by large private buyers on small suppliers, which is this paper's treatment, and show that buyers respond on other margins (relationship and organizational form). A JF referee in trade credit will raise it immediately. It also bears on whether US buyers responded by dropping covered suppliers.
- *What would resolve it:* Cite and position against it. State what the US setting adds: all industries, investment and financing outcomes, staggered variation.
- *Owner:* `jf-literature-positioning`.

**R2-M2 — No supplier-side outcomes for buyer offset margins (sales, margins, customer relationships).**
- *Where:* Table 3 has four outcomes (receivable days, cash, investment, short-term debt). §7 ¶2: "buyers that lose trade-credit financing may adjust prices, order volumes, or supplier choice."
- *Why it matters:* The abstract's policy conclusion, "Regulating payment terms relaxes financing constraints," invites the question whether buyers clawed back the transfer through prices, volumes or switching to out-of-state or above-threshold suppliers. Supplier sales, gross margin and major-customer terminations are observable in the data the paper already uses (Compustat; segment customer files, §3 ¶2).
- *What would resolve it:* Add sales, gross margin and the number or duration of major-customer relationships as outcomes, in the IA.
- *Owner:* `jf-robustness` / `jf-literature-positioning`.

*Minor concerns*
1. The phrase "a policy experiment that has received little attention" (§1 ¶2) should not suggest that payment-term regulation itself is unstudied, given the omission in R2-M1.
2. The conclusion's external-validity paragraph (§7 ¶2) is good. Put one sentence of it in the introduction so the editor sees that the authors know the sample is public firms.
3. The economic-magnitude translation (2.0% of assets released, §5.1) is useful. "Median firm" is paired with 1.08, which is the treated *mean* sales-to-assets in Table 1. Use the median or say "average".

**Confidential letter to the editor.** Minor revision on contribution grounds. The question is first-order for corporate finance and policy, and the delta over Barrot (2016) and Barrot and Nanda (2020) is explicit. The paper must engage Breza and Liberman (2017), and it would be stronger with buyer-offset outcomes. Neither threatens the core result.

```text
【Lens】contribution / general interest
【One-line summary】Regulatory mirror of Murfin–Njoroge: payment-term caps release supplier liquidity that constrained firms invest.
【Recommendation】minor
【Major concerns】R2-M1 Breza & Liberman (2017) omitted from "closest" set (§1 ¶5) · R2-M2 no sales/margin/relationship outcomes for buyer offset (Table 3; §7 ¶2)
【Minor concerns】"little attention" phrasing; external-validity sentence in intro; median vs mean in §5.1
【What would move me to accept】Positioning against Breza–Liberman plus an IA table on supplier sales, margins and customer-relationship terminations.
```

---

## 4. Referee 3 — inference / robustness lens (form C)

**Report to the authors**

*Summary.* As above. My focus is whether the estimates survive honest inference and reasonable specification choices.

*Assessment.* Inference is mostly well handled. Standard errors are clustered at the level of treatment assignment (state, 51 clusters, Table 3 note). Randomization inference over adoption dates is reported (IA.D, cited in §6 ¶2). The pre-trend test is complemented by Rambachan–Roth bounds (§6 ¶2). The specification checks that matter are in the body: division × year FE, the above-threshold placebo, excluding the 2009 cohort, and never-treated controls.

*Main concerns*

**R3-M1 — With only 14 treated clusters, state-clustered SEs can over-reject. The RI result should carry the inference in the body.**
- *Where:* Table 3 note, "Standard errors clustered by state of headquarters (51 clusters)." The 14 treated states are given in §2.
- *Why it matters:* With few treated clusters, cluster-robust SEs are anti-conservative (MacKinnon–Webb). The marginal results (cash −0.9 (0.4), short-term debt −1.1 (0.5), the Table 4 difference p = 0.04) are the ones at risk.
- *What would resolve it:* Report wild-cluster-bootstrap or RI p-values next to each Table 3/4 estimate.
- *Owner:* `jf-robustness` (execution bridge: `wild_cluster_bootstrap`).

**R3-M2 — The constraint mechanism rests on a single proxy split at the median.**
- *Where:* §3 ¶2 classifies firms as "financially constrained if their baseline size-age index (Hadlock and Pierce, 2010) is above the sample median." Table 4 Panel A gives a difference p = 0.04.
- *Why it matters:* The SA index is a function of size and age only, so "constrained" is "small and young". That group also differs in growth opportunities. The mechanism claim in the abstract leans on one proxy and a p-value near 0.05.
- *What would resolve it:* Alternative proxies (non-dividend payer, no credit rating, Whited–Wu, a text-based measure) and a continuous-interaction version.
- *Owner:* `jf-robustness`.

**R3-M3 — The investment result is fragile to parallel-trend violations (Rambachan–Roth breakdown 0.9), and the text does not discuss it.**
- *Where:* §6 ¶2, "the corresponding breakdown value for investment is 0.9."
- *Why it matters:* Investment significance is lost if post-adoption violations reach 90% of the largest pre-period violation. The headline investment number (2.4 pp) is less robust than the receivable-days result (breakdown 1.4).
- *What would resolve it:* Discuss it, show the investment pre-period coefficients in Figure 2 with the bounds, and report smoothness-restriction (Δ^SD) bounds as well.
- *Owner:* `jf-identification` (execution bridge: `honest_did_from_result`).

*Minor concerns*
1. Short-term debt is measured as "debt in current liabilities" (§3 ¶2, i.e., DLC), which includes the current portion of long-term debt. The interpretation as "repaying the working-capital lines" (§5.1) needs a revolver-specific measure (Capital IQ) or a caveat.
2. Several heterogeneity cuts are shown (2 splits × 2 outcomes, Table 4). Disclose that these were the pre-planned splits, or report sharpened q-values.
3. The 2019 cohort's post-period is 2019–2022 and includes COVID-era payment disruptions. Add a "drop 2020–2021" or "drop the 2019 cohort" robustness line next to the 2009-cohort exclusion (§6 ¶2).
4. Data availability (DAS) is consistent with the AFA policy. Hand-collected adoption dates will be shared, which is good.

**Confidential letter to the editor.** Minor revision. The inference is largely right. I would want the few-treated-cluster inference surfaced in the body, alternative constraint proxies for the mechanism, and an honest discussion of the investment breakdown value. None of this is likely to overturn the receivable-days result.

```text
【Lens】inference / robustness
【One-line summary】Clean CS-DiD with the right clustering; inference and mechanism need hardening for the marginal results.
【Recommendation】minor
【Major concerns】R3-M1 14 treated clusters, RI/wild bootstrap in body (Table 3 note) · R3-M2 single SA-index proxy (§3 ¶2, Table 4A) · R3-M3 investment breakdown 0.9 undiscussed (§6 ¶2)
【Minor concerns】DLC ≠ working-capital lines; heterogeneity multiplicity; COVID in 2019-cohort post-period
【What would move me to accept】RI/wild-bootstrap p-values in Tables 3–4, two more constraint proxies, and a discussed sensitivity plot for investment.
```

---

## 5. Verification pass (verifier, not a referee)

Each major concern was tested against the full text for being real, specific and addressable, and for whether the paper already answers it.

| ID | Verdict | Evidence (quoted) and reason |
|---|---|---|
| **R1-M1** post-treatment sample on revenue | **kept** | §3: "we keep firms with revenue below $500 million in their first sample year and drop firm-years in which revenue exceeds the threshold." Nothing in §6 or the IA list fixes the sample at baseline. The relocation and winsorization checks do not touch this. Real (revenue is post-treatment and the threshold is nominal over 18 years), specific (§3, every column of Tables 3–4), addressable (baseline-defined ITT sample). |
| **R1-M2** anticipation window misplaced | **kept** | §2: "took effect at the start of a fiscal year, six to nine months after enactment". §5.2: "3.1 days in the effective year" (so e = 0 is the effective year). §4.1: "relative to the year before adoption". §4.2: "include event time e = −2, which spans the enactment window." Enactment within 9 months before the start of e = 0 cannot lie in e = −2, so the stated defence is internally inconsistent and the omitted year is the exposed one. Addressable with anticipation = 1. Not dropped: no other passage handles it. |
| **R2-M1** Breza & Liberman omitted | **downgraded → minor** | Real: §1: "Our paper is closest to two studies of payment-term reforms", and the reference list has no Breza and Liberman. But the paper's stated delta (US, all industries, investment and financing chain) survives the omission. It is a positioning fix and does not threaten the conclusions. |
| **R2-M2** no buyer-offset outcomes | **downgraded → minor** | §7: "buyers … may adjust prices, order volumes, or supplier choice, and a full welfare assessment would weigh these costs." The limitation is disclosed, and the paper's claims concern supplier financing, not welfare. A price or volume clawback would lower supplier cash flow and work *against* the investment result, so it does not threaten the headline. A worthwhile IA addition. |
| **R3-M1** few treated clusters | **downgraded → minor** | §6: "randomization inference over adoption dates leave the conclusions unchanged (Internet Appendix Sections IA.C and IA.D)." The concern is largely answered, so it is not a major issue. What remains is a reporting request: put RI or wild-bootstrap p-values in the body tables for the marginal estimates. |
| **R3-M2** single constraint proxy | **downgraded → minor** | Real: §3: "financially constrained if their baseline size-age index … is above the sample median." But the mechanism pattern is internally coherent: Table 4 Panel A shows receivable days falling about equally (7.3 vs 6.1, p = 0.67) while investment diverges, which is the relevant falsification. Alternative proxies are an added robustness table, not a threat to the main result (in `qje-referee-strategy` triage terms, a robustness request rather than a fundamental). |
| **R3-M3** investment breakdown 0.9 | **downgraded → minor** | §6: "the corresponding breakdown value for investment is 0.9." The paper reports this transparently. The investment estimate is also significant under division × year FE (2.1, SE 0.9) and in each sample variant. The remedy is discussion plus an added bound, not new identification. |

**Tally:** 7 concerns raised as major (R1: 2, R2: 2, R3: 3); kept 2, downgraded 5, dropped 0.

---

## 6. AE synthesis

```text
【Venue】The Journal of Finance. ~5% acceptance, ~33–45% desk rejection; identification is the binding constraint for corporate papers (jf-identification, official-source-map 2026-11-23)
【Desk-screen】send out. General-interest policy question, named staggered shock, modern estimator as headline; desk-reject risk low–medium
【Decision band】major revision (revise and resubmit), favourable
【Decisive issues (1–2)】
  1. R1-M1. §3 sample drops firm-years once revenue exceeds the nominal $500M threshold, which conditions on a post-treatment outcome.
     Owner: jf-identification. Fix: define coverage on baseline revenue (ITT), keep crossers, report crossing/exit rates by treatment;
     re-fit callaway_santanna (execution bridge) and re-issue Tables 3–4.
  2. R1-M2. §4.2 places the enactment window in e = −2, but by §2 and §5.2 it falls in the omitted year e = −1, so the pre-trend test cannot detect anticipation.
     Owner: jf-identification. Fix: callaway_santanna with anticipation = 1 (base e = −2), report e = −1 coefficients, honest_did_from_result on the re-based event study; correct §4.2.
【Secondary issues】Breza & Liberman (2017) positioning (jf-literature-positioning); RI/wild-bootstrap p-values in body tables (jf-robustness → wild_cluster_bootstrap);
  alternative constraint proxies (jf-robustness); discuss investment breakdown 0.9 and add Δ^SD bounds (jf-identification → honest_did_from_result);
  buyer-offset outcomes (sales, margins, customer terminations) in IA; placebo group is a buyer group; DLC vs revolver; COVID in 2019-cohort window; in-state coverage mapping.
【Author action plan】
  1. Rebuild the sample on baseline revenue and re-run CS with anticipation = 1 (one pass fixes both decisive issues); re-issue Table 3, Table 4, Figure 2.
  2. Re-run honest DiD on the new event study; discuss the investment bound in §6.
  3. Add RI / wild-bootstrap p-values to Tables 3–4.
  4. IA: alternative constraint proxies; buyer-offset outcomes; buyer-linked spillover test.
  5. Add Breza & Liberman (2017) to §1 ¶5; fix "median firm" wording in §5.1.
  6. Compile the PDF with the bundled Internet Appendix and confirm ≤ 60 pp (preflight could only estimate pages from source).
【Calibration caveats】Inline panel, so referees may anchor on each other. The decisive issues are design-consistency points whose
  quantitative bite is unknown until re-estimated; if the re-estimates move little, this paper reads as a strong R&R. Whether the editor
  sees it as JF-general rather than JFE-field is the main judgment call the panel cannot settle.
```

```json
{"decision_band": "major revision", "kept_major_concerns": [{"id": "R1-M1", "lens": "identification", "location": "§3 ¶1 (sample construction); all columns of Tables 3–4", "concern": "The sample drops firm-years once revenue exceeds the nominal $500M threshold, conditioning on a post-treatment outcome and inducing differential attrition of fast-growing treated firms."}, {"id": "R1-M2", "lens": "identification", "location": "§2 ¶2, §4.1, §4.2 ¶3, Table 3 note, §5.2", "concern": "Enactment precedes the effective date by 6–9 months, so the anticipation window falls in the omitted reference year e = −1, not in e = −2 as §4.2 claims, and the e = −5…−2 pre-trend test cannot detect anticipation."}], "downgraded": [{"id": "R2-M1", "lens": "contribution", "location": "§1 ¶5; References", "concern": "Breza and Liberman (2017, JF) on Chilean regulation of large buyers' payment terms is omitted from the closest-work set.", "reason": "Positioning fix; the stated delta survives."}, {"id": "R2-M2", "lens": "contribution", "location": "Table 3; §7 ¶2", "concern": "No supplier sales, margin, or customer-relationship outcomes to detect buyer offset.", "reason": "Disclosed limitation; offset would work against the investment result."}, {"id": "R3-M1", "lens": "inference", "location": "Table 3 note; §6 ¶2", "concern": "Only 14 treated clusters; cluster-robust SEs may over-reject.", "reason": "RI over adoption dates already reported (IA.D); remaining ask is to show RI/wild-bootstrap p-values in body tables."}, {"id": "R3-M2", "lens": "inference", "location": "§3 ¶2; Table 4 Panel A", "concern": "Constraint mechanism rests on a single median split of the SA index.", "reason": "Robustness request; receivable-days falsification in Panel A already supports the mechanism."}, {"id": "R3-M3", "lens": "inference", "location": "§6 ¶2", "concern": "Investment Rambachan–Roth breakdown value of 0.9 is reported but not discussed.", "reason": "Transparently reported; investment survives division×year FE and sample variants; needs discussion, not new identification."}], "dropped": []}
```
