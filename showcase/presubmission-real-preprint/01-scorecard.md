# Stage 1 — Nine-dimension readiness scorecard

**Manuscript:** Otani and Yang, "Trade Tensions Meet the Gig Economy: Evidence from the 2025 Halving of Chinese Travel to Japan," arXiv:2611.21070v1 (CC BY 4.0). Read in full: LaTeX source `07_1_main_tourism_shock.tex` (532 lines), all ten table `.tex` files, the main-text figures, and the compiled PDF (39 pp.).
**Hypothetical target:** *American Economic Review: Insights*.
**Venue bar:** `AER-Insights-Skills/resources/official-source-map.md` (submission rules re-verified 2026-11-23) and the pack skills `aeri-topic-selection`, `aeri-identification`, `aeri-robustness`, `aeri-tables-figures`, `aeri-writing-style`, `aeri-replication-package`, `aeri-referee-strategy`, `aeri-submission`.
**Method:** `shared-resources/submission-readiness/readiness-checklist.md`. Dimension 7 uses the stage-0 preflight (`00-preflight.json`, `00-preflight-pdf.txt`).

Locations use the PDF numbering. Main text: §1 Introduction (pp. 2–5), §2 Data (2.1 Tourism, 2.2 Spot-work), §3 Empirical Strategy, §4 Results (4.1 DiD, 4.2 Event study, 4.3 Additional analysis, 4.4 Robustness), §5 Conclusion (p. 16). References are on pp. 17–18 and the Supplementary Appendix on pp. 19–39 (A Tourism data, B Spot-work data, C.1–C.8 additional analysis). There are five main-text exhibits: Fig. 1 (p. 3), Fig. 2 (p. 7), Table 1 (p. 11), Fig. 3 (p. 13) and Fig. 4 (p. 14).

---

```
【Venue】American Economic Review: Insights (rules verified 2026-11-23; bar: AER-Insights-Skills skills + source map)
【Scorecard】
  1 Fit & general interest ...... FLAG
  2 Contribution clarity ........ FLAG
  3 Identification / method ..... FLAG  (highest-priority FLAG; see the referee panel's D1)
  4 Robustness & inference ...... FLAG
  5 Exhibits self-contained ..... FLAG
  6 Exposition .................. FLAG
  7 Venue mechanics ............. FAIL
  8 Data & code ................. FLAG
  9 Pre-empted objections ....... FLAG
【Go / No-go】NO-GO. The deciding dimension is 7: the anonymization FAILs. These are mechanical and take about an hour to fix.
              After that, CONDITIONAL GO, with D1 (dimension 3) to be resolved before opening the portal.
【Desk-reject risk】medium. Scope and length are fine. The risk comes from the AER-level "importance" test and the small headline magnitude.
```

---

## 1 · Fit & general interest: FLAG

**For.** The paper is about one setting with one headline object: the posted-wage response to an abrupt, externally timed services-trade shock. That matches the "single-insight" shape `aeri-topic-selection` asks for. The shock is salient (Fig. 1: Chinese arrivals −51.7%; other origins +8% to +19%), the data are unusual (22.3 million postings; Appendix B, Table A3), and the question links trade, labor and gig work, which can draw general-interest readers (§1 ¶1).

**Against.** AER: Insights is "short, not minor" (`aeri-topic-selection`, Importance test). The headline magnitude is about 1% of the posted wage in prefectures with a Chinese share of 2% or more (§4.1; Table A7: −0.011 (0.002) and −0.008 (0.003)). At the mean posted wage of ¥1,150 (Appendix B), that is roughly ¥9–13 per hour. That figure is our arithmetic; the paper does not convert to yen anywhere. Because the main text never puts the magnitude in yen or welfare terms, a coeditor has to infer the importance.

**Owner:** `aeri-topic-selection` (importance test), `aeri-writing-style` (state the magnitude).

## 2 · Contribution clarity: FLAG

**For.** The closest paper is named, and the difference is stated twice. Kurmann et al. (2026) "find no significant change in the average hourly wage of employees" (§1 ¶6, p. 4). The paper itself observes "the posted wage of new work" (§1 ¶6; related-literature paragraph, p. 5). The canon is attributed to the correct venues (Autor–Dorn–Hanson AER 2013; Faber–Gaubert AER 2019; Hazell–Taska AER 2025; Dube et al. AER: Insights 2020).

**Against.**
- The contrast with Kurmann et al. is not like-for-like: posted wages of newly created shifts versus realized hourly wages of incumbents in small businesses. The paper notes that the margins differ (§1 ¶6) but still frames the result as a "contrast" (§5). The data include realized matched wages, which would make the comparison like-for-like.
- "First" appears three times (abstract; §1 ¶1; §5 ¶1) without "to our knowledge".

**Owner:** `aeri-literature-positioning`.

## 3 · Identification / method: FLAG (highest priority)

**For.**
- The source of variation is stated in one sentence: "This unevenness is the source of identifying variation in our design" (§1 ¶4, p. 3).
- Shock timing is externally set (§1 ¶3), and exposure is fixed in 2024 (§2.1, eq. 1).
- The design is a single-timing continuous-dose DiD, so the staggered-TWFE bias problem does not arise (§3, eq. 2).
- The wage event study (Fig. 3a) shows a sharp break at block 0.
- Controls target known coincident shocks: other-origin shares × Post, the log minimum wage, and Kinki × Expo (§3 ¶2).

**Why FLAG, not PASS.**
1. **Minimum-wage revision timing.** The paper states that the 2025 revisions "took effect between October 2025 and early 2026, at different dates across prefectures" (Appendix C.2, p. 28). Adding weeks-since-revision dummies cuts the wage estimate from −0.272 (0.076) to −0.152 (0.067) (Table A5, col. 5). The paper keeps the larger estimate as the baseline because the dummies "also absorb part of the change after the advisory" (fn. 11). That argument holds only if revision timing is unrelated to Chinese exposure, and the paper never shows this.
2. **Pre-period dip and reference block.** In Fig. 3a the wage coefficients for blocks −5 to −3 lie at about −0.13 to −0.16. The reference block (Oct 20–Nov 9, 2025; fn. 10) falls in the month when the earliest revisions took effect. No joint pre-trend test or HonestDiD bound is reported for the headline.
3. **Continuous-dose interpretation.** Table A7 shows the response is not linear in the share (none at 1–2%, −1.1% at 2–3%, −0.8% at 3% or more). Appendix C.3 says the linear fit "overstates the decline" at the top. A referee aware of Callaway, Goodman-Bacon and Sant'Anna (2024) will ask which causal parameter β represents.

None of these is fatal. The estimate survives every specification the paper reports. Still, item 1 is the objection most likely to decide a reject-or-conditional-accept outcome. Under the checklist a FAIL here would mean NO-GO; it stays a FLAG because the paper's own robust estimate (−0.15) is still significant and its sign does not change.

**Owner:** `aeri-identification` (execution bridge: `honest_did_from_result`, an event study with revision-week dummies, and a revision-date × share cross-tab).

## 4 · Robustness & inference: FLAG

**For.** The paper reports a broad set of checks:
- prefecture clustering, plus a mixed placebo over fake dates and permuted shares (none of 500 placebo wage coefficients exceeds the actual one; Appendix C.7, Fig. A6);
- leave-out of Osaka, Kyoto and Tokyo (−0.264 to −0.342; Table A6);
- 130 regions (−0.29; Table A4) and establishment × occupation units (−0.170; Table A4);
- a year-over-year specification (−0.350; Table 1 col. 2);
- an IV on the realized loss of stays (first-stage F = 216; Table A10).

**Gaps.**
- Table A7's binned estimates rest on 6–8 prefectures per bin, yet report SEs as small as 0.002. Cluster-robust SEs with so few treated clusters can over-reject, and no wild-cluster bootstrap or randomization-inference p-value is given for the bins.
- There are many outcome × band × occupation cells: 4 × 6 in Table 1, plus 15 occupations × 3 outcomes in Fig. A4. The paper does not name wage as the primary outcome or adjust the heterogeneity cells for multiple testing.

**Owner:** `aeri-robustness`.

## 5 · Exhibits self-contained: FLAG

**For.** Notes state the unit, sample, clustering and CI level (e.g., Table 1 note; Fig. 3 note: "90 percent confidence interval… clustered by prefecture"). Five main-text exhibits is exactly the budget.

**Against.**
- **Significance asterisks** appear in Table 1 ("*, **, *** denote significance at 10, 5, 1 percent") and in every appendix table. AEA style says no asterisks (`aeri-tables-figures`; style guide per the source map). Preflight does not check this.
- **Units.** The event-study y-axes read "Coefficient on Share" (Figs. 3, 4), and the Table 1 note never says that −0.272 means "percent per percentage point of the Chinese share". Readers have to work this out from §4.1. Table A9's note already does it correctly ("Coefficients for outcomes in logs are percent changes per percentage point").
- **Exhibit budget.** Fig. 2 uses one of five exhibit slots on largely descriptive material: maps, hexagons, and shift-start distributions. Meanwhile the within-prefecture-week band contrast (Table A8), which carries the mechanism, sits in the appendix.

**Owner:** `aeri-tables-figures`.

## 6 · Exposition: FLAG

The question is in ¶1 (p. 2). The answer with a magnitude first appears in ¶6 (p. 4): "a prefecture whose Chinese share is one percentage point higher posts wages about 0.27 percent lower". That is in per-percentage-point units, with no SE, after the data and design paragraphs. `aeri-writing-style` asks for "the headline result with its magnitude and uncertainty" in sentences 1–2. The abstract (exactly 100 words) states the direction but no number. Details are in `03-polish.md`.

**Owner:** `aeri-writing-style`.

## 7 · Venue mechanics: FAIL

From preflight (`00-preflight-*.txt`), with our adjudication. False positives and misses are in REPORT.md.

| Item | Status | Evidence |
|---|---|---|
| Anonymized manuscript | **FAIL** | Author block with names, emails and affiliations (tex l. 81–84; PDF p. 1). Title footnote with thanks, grants and data-provider thanks (tex l. 80). PDF metadata `Author = Suguru Otani; Chang Yang`. All three must go to a separate "title page" PDF, and the PDF properties must be cleared. |
| Word count | PASS (our count) | Main text ≈ 5,050 words in AEA scope (body + footnotes, excluding exhibits and their notes). Preflight's 5,565–5,691 also counts about 540 words of exhibit notes. Cap with 5 exhibits = 7,000 − 5 × 200 = **6,000**, so the margin is ≈ 950 words. Confirm with the AEA word-count PDF. |
| Exhibits ≤ 5, each ≤ 1 page | PASS (our check) | Exactly five (Figs. 1–4, Table 1), each on one page (pp. 3, 7, 11, 13, 14). Preflight does not check this rule. |
| Abstract ≤ 100 words | PASS, at the limit | Preflight: 100 words. The AEA counter may treat "spot-work" and "services-trade" differently. The 97-word rewrite in `03-polish.md` leaves headroom. |
| Supplementary Appendix | FLAG | Bound into the same PDF (pp. 19–39). The AEA count *includes* in-paper appendices, so upload it as a separate, anonymized Supplemental Appendix PDF. |
| No significance asterisks | FLAG | Table 1 and Tables A2, A4–A10 (see dimension 5). |
| Disclosure statement | Portal item | One Disclosure Statement PDF per coauthor, uploaded separately. It must not appear in the anonymized manuscript. Preflight's STMT-MISSING FAIL is misframed (REPORT.md). |
| AI-use description | Portal item | Required at submission when AI was used. The source contains a commented-out AI declaration (tex l. 275–277). Draft in `04-letter-and-statements.md`. |
| Citations ↔ references | PASS | 24 `\bibitem`s, all cited. Crossref did not resolve two items, both grey literature: a RIETI DP and an arXiv preprint. One of the two flags is a parser split error (REPORT.md). |
| Number traceability | PASS | The "51.7 percent" NUM-MISMATCH is a false positive: the number is in Fig. 1's raster legend, and the figure note points to it (tex l. 118). |
| Fee | UNKNOWN | Depends on AEA membership and income band (US$300 / 200 / 0 for nonmembers, US$200 / 100 / 0 for members; US$15 per typeset page if accepted). The authors must choose the band. |

**Owner:** `aeri-submission`.

## 8 · Data & code / reproducibility: FLAG

The tourism inputs are public: JNTO arrivals and the JTA Overnight Travel Statistics Survey (§2.1). The labor data are "confidential posting- and contract-level records from Timee" (§2.2, fn. 2). The AEA policy permits restricted data with an access route, public documentation and runnable code (`aeri-replication-package`). The manuscript has no data-availability statement and no access route for a replicator. This does not block submission but is required before acceptance.

**Owner:** `aeri-replication-package`.

## 9 · Pre-empted referee objections: FLAG

**Pre-empted well:**
- seasonality (year-over-year, Table 1 col. 2);
- the Osaka Expo (Kinki × Expo);
- substitution toward other origins (Table A2 triple difference; other-origin controls);
- top-3 leverage (Table A6);
- composition (establishment FE, Table A4);
- few clusters (placebo, C.7).

**Not pre-empted:**
- minimum-wage revision timing versus exposure (disclosed in fn. 11 and C.2, not resolved);
- a labor-*supply* alternative: workers displaced from tourism jobs entering the platform in exposed prefectures, a group the incumbent analysis in C.6 does not cover;
- posted versus realized wages and fill rates;
- the hotel-occupation null (Fig. A4) set against the "hours when hotels hire" mechanism.

AER: Insights has no R&R round (`aeri-referee-strategy`), so these objections need answers before submission.

**Owner:** `aeri-referee-strategy` → `aeri-identification` / `aeri-robustness`.

---

## Blocking gaps (FAIL), ranked

1. **Anonymization (dimension 7).** Remove the author block, title footnote and PDF metadata, and build the "title page" PDF. Owner: `aeri-submission`. About one hour.

## Will be pushed (FLAG): referee-anticipation list

1. Minimum-wage revision timing versus Chinese share (dimension 3) → `aeri-identification`.
2. Importance and magnitude in yen; a like-for-like contrast with Kurmann et al. (dimensions 1, 2) → `aeri-topic-selection`, `aeri-literature-positioning`.
3. Mechanism claims calibrated to Table A8 and Fig. A4 (dimensions 6, 9) → `aeri-writing-style`.
4. Few-cluster inference for the bins; naming the primary outcome (dimension 4) → `aeri-robustness`.
5. Asterisks and units in exhibits; a better use of the Fig. 2 slot (dimension 5) → `aeri-tables-figures`.
6. A restricted-data access statement (dimension 8) → `aeri-replication-package`.
