# Stage 2 — Referee panel (inline panel)

> **This is an inline panel.** One agent played the AE, three referees and the verifier in turn, following `shared-resources/submission-readiness/simulated-referee.md`. The referees may therefore anchor on each other. The multi-agent run (separate referee and verifier subagents) is the stronger gauntlet. **This is a rehearsal, not a verdict.** It predicts the attack surface and the decision band. It does not predict acceptance or rejection.

**Form:** C, economics journals (`review-forms.md`). Each referee writes a report to the authors (summary → contribution against the closest papers → numbered main concerns → minor concerns) and a confidential letter to the editor. Each concern also gets `owner_skill` and `evidence` fields.

**Calibration (from `AER-Insights-Skills`, source map re-verified 2026-11-23):**
- A general-interest AEA journal for AER-quality insights conveyed briefly.
- **First decisions after review are reject or conditional accept; there is no traditional R&R.** A conditional accept normally comes with about an 8-week window and no second referee round (editorial-policy page; `aeri-referee-strategy`).
- Hard caps: **7,000 words minus 200 per exhibit, at most 5 exhibits, each ≤ 1 page, abstract ≤ 100 words**. Over-cap papers are returned unreviewed.
- **Anonymized submission** under the AEA's three-year author-anonymization RCT (launched fall 2026): author details go in a separate "title page" PDF, and self-citations are by name. The editorial-policy page still describes single-blind review.
- AEA style: no significance asterisks.
- Strictness setting: top-general-interest. Referees therefore ask both "is it credible?" and "should a non-specialist economist care?" (`aeri-topic-selection`: "short, not minor").

**Referee inputs:** the full manuscript (tex + PDF) and `00-preflight.json`. Mechanics are excluded from the reports. The anonymization FAILs are an author to-do, not a weakness of the science.

---

## Associate Editor — desk screen

- **In scope?** Yes. Trade × labor × gig work with one headline object (posted-wage response), and it fits the caps: five exhibits, ≈ 5,050 words in AEA scope against a 6,000 cap.
- **General interest?** Plausible but not self-evident. The shock is salient: Chinese arrivals fell 51.7% while other origins rose (Fig. 1). The "price, not quantity" message reaches beyond Japan. However, the headline magnitude is about 1% of a gig wage (Table A7), which the paper does not translate into yen or welfare.
- **Fatal flaw scan?** None. The design is transparent, the wage break in Fig. 3a is sharp, and the robustness set is broad (Appendix C).
- **Decision:** **send out.** **Desk-reject risk: medium.** The deciding reason is importance and magnitude, not credibility.

---

## Referee 1 — identification / method skeptic

**【Lens】** Identification.

**【Summary as I read it】** The paper uses China's November 14, 2025 advisory against travel to Japan as a common-timing shock. It compares 47 prefectures by their 2024 Chinese share of overnight stays in a continuous-dose DiD on a prefecture-week panel of spot-work postings (§3, eq. 2; 72 weeks; 3,384 cells). The posted hourly wage falls by 0.27% per percentage point of share (Table 1 col. 1: −0.272, SE 0.076). The fall starts in the first four-week block and persists (Fig. 3a). Quantities fall in levels but not year over year (Table 1 col. 2).

**【Contribution vs closest papers】** Kurmann, Lalé and Martin (2026, JIE) use realized payroll outcomes. Greaney and Kiyota (2026) and Ahn, Greaney and Kiyota (2022) study boycott effects on tourism demand. Hazell and Taska (2025) study the rigidity of new-hire wages. The novel element here is the posted price on a spot market at weekly frequency. That is a real delta, conditional on the wage result being causal.

**【Recommendation】** At AER: Insights: *reject in current form*. This is major-revision-equivalent at a journal with R&R; conditional accept becomes plausible if M1 is resolved before submission.

**【Main concerns】**

**M1 — Minimum-wage revision timing may load on the exposure measure.**
- **Where:** §3 ¶2; fn. 11; Appendix C.2; Table A5 col. 5; Fig. 3a.
- **Concern:** The paper states that the 2025 revisions "took effect between October 2025 and early 2026, at different dates across prefectures" (C.2). Suppose high-share prefectures (the large cities) revised early, around the reference block, and low-share prefectures revised during the post period. Then low-share prefectures' posted wages would rise mechanically after November, producing a negative Share × Post coefficient with no tourism effect at all.
- **Why it matters:** The log-minimum-wage control assumes a common, linear pass-through. Pass-through on a platform where many postings sit near the floor is likely nonlinear and concentrated in the weeks just after a hike. That is the subject of Kanayama, Miyaji and Otani (2026), which the paper cites (on the same platform). When weeks-since-revision dummies are added, the estimate falls 44%, to −0.152 (0.067) (Table A5 col. 5). The pre-period wage coefficients sit at about −0.13 to −0.16 in blocks −5 to −3 before returning to ≈ 0 in the reference block (Fig. 3a). That pattern fits a reference period distorted by early revisions.
- **What would resolve it:**
  - (a) A 47-point figure plotting each prefecture's 2025 revision effective week against its Chinese share.
  - (b) An outcome net of the floor: log(posted wage) − log(prefecture minimum wage), or the analysis restricted to postings above, say, 110% of the minimum wage.
  - (c) An event study with revision-week dummies, using a pre-period average as the reference instead of a single block.
  - (d) Moving the within-prefecture-week band contrast (Table A8), which absorbs every prefecture-week shock including minimum wages, into the main text.
- **owner_skill:** `aeri-identification`. Execution bridge: `honest_did_from_result`; `did`/`feols` with revision-week dummies.

**M2 — What β identifies under a concentrated, non-linear dose.**
- **Where:** §3; Appendix C.3; Tables A6–A7; §2.1 eq. 1; Appendix A.
- **Concern:** Three prefectures span most of the share's range (Osaka 10.0%, Kyoto 8.0%, Tokyo 7.7%; median 0.9%). Table A7 shows no effect at 1–2%, −1.1% at 2–3%, and −0.8% at 3% or more; the paper says the linear fit "overstates the decline in the prefectures with the highest shares." Under Callaway, Goodman-Bacon and Sant'Anna (2024), a TWFE dose coefficient is a weighted average of marginal responses and needs a stronger parallel-trends assumption to be causal.
- **Measurement:** The numerator counts only facilities with 10 or more employees, while the denominator counts all facilities (§2.1). That error is likely correlated with hotel size and urbanity.
- **Fix:** Make the binned contrast the headline magnitude, state the estimand explicitly, and show that the per-pp estimate is robust to an exposure measure with a consistent facility scope where the data allow.
- **owner_skill:** `aeri-identification`.

**M3 — A labor-supply alternative.**
- **Where:** §1 ¶7; §4.3; Appendix C.6.
- **Concern:** A rise in spot-work supply in exposed prefectures would also lower posted wages. For example, hotel and retail employees who lose regular hours might turn to the platform. The paper says the hour-of-day pattern favors demand (§1 ¶7). But displaced tourism workers would likely supply exactly those early-morning and daytime hours. Appendix C.6 covers *incumbent* platform workers only.
- **Fix:** New-worker registrations or first matches by prefecture; applications per posting; fill rates and time-to-fill. The data record timestamps for posting and matching (§2.2).
- **owner_skill:** `aeri-robustness`.

**【Minor】**
- Concurrent China–Japan measures in the same weeks, beyond travel: list any and argue that they are orthogonal to the share.
- The 2026 survey redesign (Appendix A) affects Fig. 2c and the IV's loss measure (Table A10). Show the IV with the November–December 2025 loss only, before the redesign.
- Report a joint pre-trend test for Fig. 3a. The paper does report one for worker outcomes (Table A9).

**【What would move me to accept】** M1 (a)–(c) showing that the wage effect survives an outcome measured relative to the floor, together with a headline stated as the binned contrast.

**【Confidential letter to the editor】** The setting and data are excellent, and the wage break is visually sharp. My recommendation hinges on whether the staggered 2025 minimum-wage revisions, timed partly around the reference block, are correlated with Chinese exposure. The authors' own Table A5 shows that the estimate nearly halves once revision timing is controlled. A pre-submission fix is feasible with data the authors already hold. Without it I would lean reject at AER: Insights.

---

## Referee 2 — contribution / fit / literature

**【Lens】** Contribution and general interest.

**【Summary】** A clean natural experiment showing that a sudden loss of Chinese tourists lowered posted spot-work wages in exposed prefectures, with no robust quantity response. The paper argues that this contrasts with US evidence based on payroll data.

**【Contribution vs closest papers】** Kurmann et al. (2026) is the benchmark. Gonzalez and Surovtseva (2025) study short-run tourism shocks and employment. Dube et al. (2020, AER: Insights) study monopsony on online platforms. The new piece is the margin observed: posted prices of new work at high frequency.

**【Recommendation】** *Borderline: conditional accept is possible if importance is argued; otherwise reject.*

**【Main concerns】**

**M1 — Importance and magnitude are not made explicit.**
- **Where:** abstract; §1 ¶6; §4.1; Table A7.
- **Concern:** The headline is "0.27 percent per percentage point" (§1 ¶6), which works out to about 1% of the wage in exposed prefectures. The main text never converts this to yen per hour, a share of tourism-sector labor cost, or a comparison with the same autumn's minimum-wage increases. AER: Insights asks for AER-level importance in a short paper (`aeri-topic-selection`).
- **Fix:** One sentence of magnitude in the first paragraph. One back-of-envelope estimate of the earnings loss to spot workers in exposed prefectures (posted labor hours × wage change), using Table A3 means.
- **owner_skill:** `aeri-topic-selection` + `aeri-writing-style`.

**M2 — The contrast with Kurmann et al. is not like-for-like.**
- **Where:** §1 ¶6; related literature (p. 5); §5.
- **Concern:** The paper writes that it finds "instead" that the posted wage falls (p. 5), and §5 calls this a contrast. The outcomes differ: posted wages of new shifts versus realized hourly wages of incumbents. The paper's own establishment-level estimate is −0.170 (Table A4 col. 3) against −0.272 at the prefecture level. That suggests about a third of the aggregate decline reflects which jobs are posted.
- **Fix:** Report the realized wage of *filled* shifts and a composition-fixed wage (establishment × occupation FE) as co-headline numbers. Then the "price vs quantity" contrast compares like with like.
- **owner_skill:** `aeri-literature-positioning`.

**M3 — Mechanism claims run ahead of the evidence, and the paper carries more than one idea.**
- **Where:** abstract; §1 ¶7; §4.3; Table A8; Fig. A4.
- **Concern:** The abstract says wages fall more "when hotels and shops hire". However:
  - the hotel-occupation wage decline "is not significant" (§4.3; Fig. A4);
  - restaurant staff, whose shifts cluster in the evening (Fig. 2d), do show a significant decline, while the evening-band wage does not (Table 1 col. 5);
  - the within-prefecture band contrast is significant only when weighted (Table A8: −0.080 (0.064) unweighted; −0.061 (0.029) weighted).
- **Fix:** Present the hour-of-day pattern as suggestive, or make the weighted Table A8 contrast the in-text mechanism exhibit, in place of Fig. 2, and narrow the wording.
- **owner_skill:** `aeri-writing-style` + `aeri-tables-figures`.

**【Minor】**
- Write "to our knowledge, the first" in all three places where "first" appears.
- The general claim in §5 that geopolitical shocks "can leave employment unchanged" goes beyond a year-over-year employment estimate of 0.041 (SE 0.666, Table 1 col. 2). The CI includes the levels estimate of −1.33.

**【Confidential letter to the editor】** The paper is timely and well executed, and its central message is easy to state. My worry is whether a ~1% posted-wage response on one platform clears the AER-level importance bar. The authors can strengthen this with a magnitude translation and a like-for-like wage comparison. I would view it more favorably as an AER: Insights paper if the mechanism section were cut back to what Table A8 supports.

---

## Referee 3 — robustness / inference / reproducibility

**【Lens】** Robustness, inference, and reproducibility.

**【Recommendation】** *Conditional accept, with required changes, if R1-M1 is answered.*

**【Main concerns】**

**M1 — Few-cluster inference for the binned and leave-out estimates.**
- **Where:** Tables A6–A7.
- **Concern:** The bins contain 6–8 prefectures each (Table A7), yet SEs are as small as 0.002 (2–3% bin). Cluster-robust variance with few treated clusters is known to understate uncertainty. The mixed placebo (Appendix C.7) covers only the linear coefficient.
- **Fix:** Wild-cluster restricted bootstrap or randomization-inference p-values for the Table A7 bins and the Table A6 col. 5 estimate.
- **owner_skill:** `aeri-robustness`.

**M2 — Primary outcome and multiplicity.**
- **Where:** Table 1 (4 outcomes × 6 columns); Fig. A4 (15 occupations × 3 outcomes).
- **Fix:** Declare the posted wage as the primary outcome. Label the band and occupation results exploratory, or report sharpened q-values for them.
- **owner_skill:** `aeri-robustness`.

**M3 — Restricted-data replication route.**
- **Where:** §2.2 fn. 2.
- **Concern:** The data are confidential Timee records. AEA policy requires an access route, documentation, and code that runs on the restricted data before acceptance.
- **Fix:** A data-availability statement now. Ask Timee whether the aggregated prefecture-week panel (3,384 cells) can be deposited.
- **owner_skill:** `aeri-replication-package`.

**【Minor】**
- Table 1's employment column stops at February 9, 2026 (12 post weeks). Say this in the abstract's quantity claim, or add a "short-run" qualifier.
- The night column has 3,364 observations; note the missing cells.
- Fig. 3 notes say "from column (1) of Table 1", but these are event-study estimates. Rephrase as "same specification as".

**【Confidential letter】** The robustness set is unusually thorough for a short paper. My concerns are about inference with few clusters and the replication route, and both can be fixed. My recommendation depends on Referee 1's minimum-wage concern.

---

## Adversarial verification

Each major concern was tested as **real** (the paper does or omits this, with a quoted line), **specific** (section, table and mechanism named) and **addressable** (the author can act on it).

| Concern | Verdict | Reason |
|---|---|---|
| R1-M1 minimum-wage timing | **kept (decisive)** | Real: the paper itself reports the revision window (C.2) and the drop to −0.152 (Table A5 col. 5). The paper's defense (fn. 11) assumes revision timing is orthogonal to exposure but does not show it. Specific and addressable: the authors hold the revision dates. The paper does partly address the issue through Table A8's prefecture × week FE, but that design identifies only the band *difference*, not the level. |
| R1-M1 sub-point: pre-period dip | **kept, merged into R1-M1** | Visible in Fig. 3a, blocks −5 to −3. The CIs include zero, so it is evidence of sensitivity, not of a violated trend. |
| R1-M2 dose interpretation | **downgraded → secondary** | The paper already reports bins (A7) and leave-outs (A6) and openly says the linear fit overstates the top group. What remains is a framing and estimand fix. |
| R1-M3 labor supply | **kept, downgraded → secondary** | Partly answered by the hour-of-day pattern (§1 ¶7) and incumbent hours (C.6). The new-entrant margin is untested. The test can be run on data the paper already describes. |
| R2-M1 importance and magnitude | **kept (decisive for this venue)** | Real: no yen or welfare translation appears anywhere in the main text. AER: Insights' explicit importance test makes this decision-relevant. Addressable through text and a back-of-envelope estimate. |
| R2-M2 Kurmann contrast | **kept, merged into D2** | Real: "we find instead" (p. 5) and the contrast in §5. The paper acknowledges the margin difference in §1 ¶6, so the concern is the framing and the missing realized-wage number, not an error. |
| R2-M3 mechanism overclaim | **kept (decisive, cheap)** | Real: the hotel wage is not significant (§4.3) and the unweighted band difference is not significant (A8 col. 1). Fixable mostly by narrowing claims (stage 3). |
| R3-M1 few-cluster bins | **kept → secondary** | Real (A7 SEs with 6–8 clusters per bin). Not decisive: the linear estimate already has placebo support (C.7). |
| R3-M2 multiplicity | **downgraded → minor** | The wage is de facto the headline throughout, and the heterogeneity results are framed as additional analysis. |
| R3-M3 replication route | **kept → submission-package item** | Required before acceptance, not at the first decision. |
| (dropped) "no clustering correction for 47 clusters" | **dropped** | The paper already supplements the clustered SEs with a mixed placebo (C.7: none of 500 exceeds). |
| (dropped) "Expo end confounds Osaka/Kyoto" | **dropped** | Already controlled (Kinki × Expo, §3 ¶2), and the estimate is unchanged (A5 cols. 3–4). |

---

## AE synthesis

```text
【Venue】AER: Insights (calibrated from AER-Insights-Skills + source map, rules verified 2026-11-23)
【Desk-screen】send out; desk-reject risk medium (importance and magnitude, not credibility)
【Decision band】AER: Insights decides reject or conditional accept only. As written, the panel
               centres on REJECT (major-revision-equivalent at an R&R journal). Conditional accept
               is a realistic band if D1 is resolved and D2–D3 are fixed BEFORE submission.
               This is a rehearsal and makes no prediction of the actual outcome.
【Decisive issues】
  D1  Minimum-wage revision timing vs exposure (R1-M1). Table A5 col. 5 halves the estimate.
      Show the revision-week × share relationship, an outcome net of the floor, and an event
      study with revision dummies and a pooled pre-period reference.
      → aeri-identification (execution bridge: honest_did_from_result; feols/did)
  D2  Importance: magnitude in yen and earnings, plus a like-for-like wage comparison with
      Kurmann et al. (realized filled-shift wage; composition-fixed wage) (R2-M1, R2-M2)
      → aeri-topic-selection + aeri-literature-positioning + aeri-writing-style
  D3  Mechanism claims narrowed to what Table A8 col. 2 and Fig. A4 support; consider
      swapping Fig. 2 for the band-contrast exhibit (R2-M3)
      → aeri-writing-style + aeri-tables-figures
【Secondary】dose estimand and binned headline (R1-M2); new-entrant supply test (R1-M3);
            wild-bootstrap/RI for bins (R3-M1); restricted-data statement (R3-M3)
【Author action plan】1 D1 analyses (data in hand) → 2 rewrite abstract and ¶1 with magnitude (D2)
                     → 3 narrow mechanism claims (D3) → 4 secondary items → 5 mechanics (anonymize, split appendix)
【Calibration caveats】Inline panel (anchoring risk). Importance judgments at AER: Insights vary by
                      coeditor. Whether the minimum-wage revision timing actually correlates with the
                      share is unknown to the panel; if it does not, D1 resolves quickly in the authors' favor.
                      The fallback venue if rejected (aeri-referee-strategy) would be an AEJ (Applied or
                      Policy) or a field journal in international or labor economics.
```
