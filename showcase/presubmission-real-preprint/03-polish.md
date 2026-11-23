# Stage 3 — Prose polish (claim-to-evidence, first page, title/abstract)

Method: `shared-resources/submission-readiness/prose-polish.md`. House style comes from `AER-Insights-Skills/skills/aeri-writing-style`: lead with the result, magnitude and SE in sentences 1–2, abstract ≤ 100 words stating the result, minimal roadmap. **Every edit below is a suggestion.** None changes an estimate. Where a sentence's scope narrows, the narrowing is named. Derived figures (yen) are marked *[verify]*.

## Pass 1 — Claim-to-evidence audit

```
【Claim audit】16 claims · supported 9 · stronger-than-evidence 6 · unsupported 1 · contradicted 0
```

The "unsupported" claim is C14. It is not contradicted: §5's general claim simply has no evidence beyond this one setting.

| # | Claim (shortened) · location | Evidence | Strength | Minimal fix |
|---|---|---|---|---|
| C1 | "2025 Halving of Chinese Travel to Japan" · title | Fig. 1: −51.7%, Nov 2025–Aug 2026 vs a year earlier | supported | — |
| C2 | "we provide the first such evidence for the gig economy" · abstract | Related literature (p. 5): closest paper is Kurmann et al. (payroll, not gig) | stronger than evidence (novelty) | "to our knowledge, the first evidence on a spot labor market" |
| C3 | Posted wages fall "immediately and persistently… relative to others" · abstract | Table 1 col. 1 −0.272 (0.076); Fig. 3a blocks 0–4 at −0.26 to −0.37 | supported | Add the magnitude (see Pass 3) |
| C4 | "postings, hours, and employment show no robust change" · abstract | Table 1 col. 2: −1.086 (0.891), −1.031 (0.943), 0.041 (0.666) | supported. The wording is carefully calibrated; keep it | Optionally add "once seasonality is removed" |
| C5 | "Wages fall more for early morning and daytime shifts, when hotels and shops hire" · abstract | Table 1 cols. 3–6; Table A8: −0.080 (0.064) unweighted, −0.061 (0.029) weighted; hotel occupation not significant (§4.3, Fig. A4) | **stronger than evidence** (the "hotels" mechanism) | "The wage decline is larger for early-morning and daytime shifts." Drop the hotel attribution from the abstract |
| C6 | "Where each shift is priced anew, a services-trade shock lowers the price of labor in the hours it hits" · abstract | One platform, one shock; hour-specific result as in C5 | stronger than evidence (generality + C5) | "Where each shift is priced anew, the shock reaches workers through pay." |
| C7 | Timing "set by a decision of the Chinese government… allows a cleaner identification of causal effects" · p. 5 | Timing is external (§1 ¶3); exposure is not randomly assigned (§2.1) | stronger than evidence (timing ≠ exposure) | "…whose timing was set outside Japan, so that identification rests on cross-prefecture differences in pre-shock exposure." |
| C8 | 0.27% per pp; ≈1% at shares ≥ 2% · §1 ¶6, §4.1 | Table 1 col. 1; Table A7 (−0.011, −0.008) | supported | Add SE and yen (see Pass 2) |
| C9 | Establishment-level −0.17 · §1 ¶6, §4.4 | Table A4 col. 3 | supported | — |
| C10 | "In this market, a loss of visitors therefore reaches the price of labor at once." · §1 ¶6 | Fig. 3a block 0 | supported, conditional on D1 (minimum-wage timing) | Keep. Revisit after the D1 analyses |
| C11 | Early-morning/daytime 0.27 and 0.31; postings/hours early −1.8/−2.5 · §1 ¶7 | Table 1 cols. 3–4 | supported | — |
| C12 | "a loss of visitors reaches spot workers through the price offered for the shifts that tourism demands" · §1 ¶7 | As C5 | stronger than evidence | "…through the price offered, more so for the early-morning and daytime shifts in which tourism-facing businesses post most." |
| C13 | "This contrasts with Kurmann et al. (2026)" · §5 | Different outcome (posted vs realized wage); §1 ¶6 acknowledges this | stronger than evidence (comparability) | "Unlike realized wages in payroll data (Kurmann et al. 2026), posted wages for new work fall." |
| C14 | "geopolitical shocks to trade can leave employment unchanged and reach workers through pay" · §5 | Employment YoY 0.041 (0.666): the CI is wide and includes the level −1.33 | **unsupported as a general claim** | "…can reach workers through pay even when employment shows no detectable change in the short run." |
| C15 | Placebo: none of 500 as large · §4.4 | Appendix C.7, Fig. A6 | supported | — |
| C16 | IV: 1 pp loss of stays → −0.35% wage; first stage 0.77 · §4.4 | Table A10 (−0.353; first stage 77.0 per 100 pp; F = 216) | supported | Mention that the 2026 loss values use the redesigned survey (Appendix A note) |

Numbers: every intro and abstract number we checked matches Table 1, Tables A4–A10 or Fig. 1. The preflight NUM-MISMATCH on "51.7 percent" is a false positive, because the value sits in Fig. 1's legend (REPORT.md).

## Pass 2 — First-page test (economics: first ~3 pages of the introduction)

```
【First-page test】question ✓ (¶1, p.2) · answer ~ (abstract direction only; the intro states it in ¶6, p.4)
                  magnitude ✗ (p.4, per-pp units only, no SE, no yen) · credibility ✓ (¶3–5, pp.2–4)
                  relevance ✓ (¶1–2)
```

**Proposed reordered opening paragraph.** Before: §1 ¶1, which ends on "whether the loss is absorbed through the price of labor or through the quantity of work." After (all numbers from the paper; yen derived, *[verify]*):

> Geopolitical tensions increasingly disrupt trade in services as well as goods. When China advised its citizens against travel to Japan on November 14, 2025, Chinese arrivals fell by about half within weeks while arrivals from other origins rose (Figure 1). Using every posting on Japan's largest spot-work platform, we find that posted hourly wages fell immediately and persistently in prefectures more dependent on Chinese visitors: by 0.27 percent per percentage point of the 2024 Chinese share of overnight stays (SE 0.076), or about 1 percent, roughly ¥11 an hour at the sample mean wage *[verify]*, in prefectures where that share was 2 percent or more. Postings, posted hours and matches show no robust change once seasonality is removed.

The existing ¶2 (the Kurmann et al. contrast) and ¶3–5 (shock, Fig. 1, design) then follow. The current ¶6 can shrink to its establishment-level and year-over-year content.

## Pass 3 — Title and abstract (AER: Insights house style)

House conventions (pack + source map):
- abstract ≤ 100 words, unstructured, stating the result;
- no title-length rule; descriptive "X: Evidence from Y" titles are common;
- JEL/keywords not required by the submissions page (2026-11-23), so they are optional portal metadata.

**Title.** The current title (16 words) is accurate: "Halving" is supported by Fig. 1.
- **Recommended (keep as is):** *Trade Tensions Meet the Gig Economy: Evidence from the 2025 Halving of Chinese Travel to Japan*. It already follows the "X: Evidence from Y" convention, and its main phrase is memorable.
- **Alternative 1 (names the outcome):** *Geopolitics and the Price of Gig Work: Evidence from China's 2025 Travel Advisory against Japan*. Puts the price margin, the insight, in the title.
- **Alternative 2 (declarative; only if D1 resolves cleanly):** *When Tourists Stop Coming, Spot Wages Fall: Evidence from China's 2025 Travel Advisory against Japan*.

**Abstract.** The current version is exactly 100 words, with no magnitude and with the hotel attribution (C5). Proposed version, 97 words (whitespace count), with no new numbers:

> How do geopolitical shocks to services exports reach local labor markets? China's November 2025 advisory against travel to Japan halved Chinese arrivals. Using every posting on Japan's largest spot-work platform, we find that where Chinese guests made up 2 percent or more of 2024 overnight stays, posted hourly wages fell by about 1 percent relative to prefectures below 1 percent, immediately and persistently. Postings, hours, and matches show no robust change once seasonality is removed. The wage decline is larger for early-morning and daytime shifts. Where each shift is priced anew, the shock reaches workers through pay.

Changes:
- states the magnitude, sample frame and comparison (Table A7; §1 ¶6);
- removes the unsupported "first" (C2) and the hotel mechanism (C5);
- narrows the final sentence's generality (C6);
- scope narrowed: "in the hours it hits" → "through pay".

Re-check the count with the AEA word counter.

## Pass 4 — Consistency and clarity

```
【Consistency】
- "employment" (Table 1, Fig. 3d) = "completed matches of the postings made in the week" (§2.2). Readers
  will hear "employment" as a headcount. Use "matches (employment)" at first use and "matches" in the abstract.
- Exposure is called "Chinese share", "Share", "Chinese tourism exposure measure" (§1 ¶4) and "treatment
  intensity" (§1 ¶5). Use "Chinese share" throughout and "Share" only in exhibit labels.
- "spot work" / "gig work" / "spot labor market": fine as a deliberate hierarchy. Define once in §1
  ("spot work, a form of gig work") and keep it fixed.
- Units: coefficients are already percent per pp, because the share is a fraction and outcomes are logs.
  Say so in the Table 1 note and relabel the Fig. 3/4 y-axes "Percent change per pp of Chinese share"
  (the Table A9 note already does this).
- Cross-reference: Fig. 2's note says the shift bands are those "of Section 4.3", but they are defined in
  §3 (Table A8's note correctly says §3). Point both to §3.
- Fig. 3/4 notes: "from column (1) of Table 1" → "same specification as column (1) of Table 1".
```

## Ranked edit list

| Rank | Location | Before → After | Reason | Owner |
|---|---|---|---|---|
| 1 | Abstract | 100-word version → 97-word version above | Magnitude in the abstract; C2, C5, C6 | `aeri-writing-style` |
| 2 | §1 ¶1 | Opening question → result-first paragraph above | First-page test: answer and magnitude | `aeri-writing-style` |
| 3 | §5 last sentence | "can leave employment unchanged and reach workers through pay" → "can reach workers through pay even when employment shows no detectable change in the short run" | C14 | `aeri-writing-style` |
| 4 | §1 ¶7 last sentence; §4.3 | "the shifts that tourism demands" → "more so for the early-morning and daytime shifts in which tourism-facing businesses post most". Add one sentence acknowledging the hotel-occupation null (Fig. A4) and the unweighted Table A8 result | C5, C12; D3 | `aeri-writing-style` |
| 5 | Related literature (p. 5); §5 | "we find instead" / "This contrasts with" → "Unlike realized wages in payroll data…, posted wages for new work fall" | C13; D2 | `aeri-literature-positioning` |
| 6 | Related literature (p. 5) | "allows a cleaner identification of causal effects" → C7 rewrite | C7 | `aeri-identification` |
| 7 | Table 1 and all appendix tables | Delete asterisks and the asterisk sentence in the notes; add "Coefficients are percent changes per percentage point of the Chinese share." | AEA style; units | `aeri-tables-figures` |
| 8 | Figs. 3–4 y-axes | "Coefficient on Share" → "Percent change per pp of Chinese share" | Self-contained exhibits | `aeri-tables-figures` |
| 9 | Abstract, §1 ¶1, §5 ¶1 | "the first" → "to our knowledge, the first" (if kept anywhere) | Novelty claim | `aeri-literature-positioning` |
| 10 | Throughout | "employment" → "matches (employment)" at first use | Terminology | `aeri-writing-style` |
