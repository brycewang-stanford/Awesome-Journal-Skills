<!-- SYNTHETIC BENCHMARK FIXTURE: fictional paper, data and authors. -->

# Paid on Time: Prompt-Payment Mandates, Trade Credit, and Supplier Investment

Avery L. Quillon and Tobias R. Venn

Avery L. Quillon is with the Department of Finance, Lakemont University. Tobias R. Venn is with the Carroway School of Business, Eastmere University. We thank seminar participants at Lakemont University and the Eastmere Corporate Finance Workshop for helpful comments. Corresponding author: Avery L. Quillon, aquillon@lakemont.example.

## Abstract

Between 2009 and 2019, fourteen U.S. states adopted Prompt Supplier Payment Acts that cap the payment terms large buyers can impose on smaller suppliers. Using a staggered difference-in-differences design covering 2,614 public supplier firms, we find that adoption shortens receivable days by 6.8 days (11.6%) and raises investment by 2.4 percentage points of capital (11.2%). The investment response is concentrated among financially constrained suppliers, and the freed liquidity substitutes for cash holdings and short-term bank debt. Regulating payment terms relaxes financing constraints for suppliers with limited access to external capital.

**Keywords:** trade credit; payment terms; supplier financing; staggered difference-in-differences; corporate investment

**JEL Codes:** G31, G32, G38

## 1. Introduction

Trade credit is one of the largest sources of short-term financing for nonfinancial firms, and it flows disproportionately from small suppliers to large customers. Large buyers routinely extend payment terms well beyond two months, and the suppliers that finance these receivables are often the firms least able to raise outside funds (Petersen and Rajan, 1997; Klapper, Laeven, and Rajan, 2012). Murfin and Njoroge (2015) show that when large buyers stretch payables, small suppliers cut investment, consistent with trade credit acting as a costly transfer of liquidity from constrained to unconstrained firms. This raises a policy question that legislatures in the United States and Europe have repeatedly debated: should regulators cap the payment terms that large buyers can impose, and does doing so change how suppliers finance themselves and invest?

We answer this question using a policy experiment that has received little attention. Between 2009 and 2019, fourteen U.S. states adopted Prompt Supplier Payment Acts (PSPAs). These statutes cap payment terms at 45 days for contracts between buyers and in-state suppliers with annual revenue below $500 million, and they impose statutory interest on late payment. Adoption was staggered across six cohorts, and the timing reflected legislative calendars and the diffusion of a model act rather than local economic conditions. We combine the adoption dates with Compustat data on 2,614 public supplier firms between 2004 and 2022, of which 548 are headquartered in adopting states. Our design compares supplier firms in adopting states with firms in states that have not yet adopted, before and after adoption.

PSPAs had large effects on supplier balance sheets. Adoption shortens receivable days by 6.8 days, an 11.6% decline relative to the pre-adoption mean. The liquidity released by faster collection is redeployed: cash holdings fall by 0.9 percentage points of assets, short-term bank debt falls by 1.1 percentage points of assets, and investment rises by 2.4 percentage points of lagged capital, an 11.2% increase. The investment response is concentrated among financially constrained suppliers, whose investment rises by 3.9 percentage points, compared with 0.8 percentage points among unconstrained suppliers. Receivable days fall most for suppliers that depend on a few large customers, the firms over which buyers held the most bargaining power before adoption.

Two features of the setting support a causal interpretation. First, adoption timing is unrelated to lagged state economic growth, unemployment, small-business employment, or the average receivable days of in-state suppliers. Second, event-study estimates show no differential trends in any outcome before adoption, including in the year between enactment and the effective date, and the effects on receivable days appear in the first year the cap binds and grow as legacy contracts roll over.

Our paper is closest to two studies of payment-term reforms. Barrot (2016) studies the 2008 French reform that capped payment terms at sixty days and shows that shorter terms lowered entry barriers in the trucking industry. Barrot and Nanda (2020) study QuickPay, which accelerated federal payments to small government contractors, and find positive employment effects concentrated in tight local labor markets. Relative to these papers, we exploit staggered, state-level variation in a mandate that applies to private buyer-supplier contracts across all industries, and we trace the full balance-sheet response of suppliers, from receivables to cash, short-term debt, and investment. We also contribute to the literature on how financing constraints shape liquidity management (Almeida, Campello, and Weisbach, 2004) by showing that a regulatory change in the terms of trade credit, rather than a change in the supply of bank credit, moves constrained firms' investment.

The rest of the paper proceeds as follows. Section 2 describes the institutional setting. Section 3 describes the data. Section 4 presents the empirical strategy. Section 5 reports the main results, Section 6 examines robustness, and Section 7 concludes.

## 2. Institutional Background

In 2007, a working group of state commercial-law commissioners circulated a model Prompt Supplier Payment Act. The model act has three core provisions. First, any contract between a buyer with more than 500 employees and an in-state supplier with annual revenue below $500 million may not specify payment terms longer than 45 days from receipt of a conforming invoice. Second, payments made after the statutory deadline accrue interest at the state's statutory judgment rate plus two percentage points. Third, clauses waiving these protections are void. The model act thus resembles the payment-term caps studied by Barrot (2016) for France and the accelerated federal payments studied by Barrot and Nanda (2020), but it applies to private contracts across all industries.

Fourteen states adopted versions of the model act between 2009 and 2019. Figure 1 shows the timing: two states adopted in 2009, three in 2011, three in 2013, two in 2015, two in 2017, and two in 2019. Thirty-six states and the District of Columbia had not adopted by the end of our sample. Internet Appendix Section IA.A lists each state's statutory citation, enactment date, and effective date. In every adopting state the act took effect at the start of a fiscal year, six to nine months after enactment, and applied to contracts entered into or renewed after the effective date. Because many supply contracts are renewed annually, the cap binds gradually as legacy contracts roll over.

**Figure 1: Adoption of Prompt Supplier Payment Acts, 2009–2019**

*Number of states whose PSPA takes effect in each year, by adoption cohort; non-adopting states shown as a separate bar.*

Legislative histories suggest that adoption timing was driven by the sequence in which state commercial-code committees took up the model act, by biennial legislative calendars, and by the order in which state bar associations endorsed it. We test this formally in Section 4.

## 3. Data and Sample

Our sample starts from all firms in the Compustat North America annual file between 2004 and 2022. We exclude financial firms (SIC codes 6000–6999) and utilities (SIC codes 4900–4999), and firms without a valid U.S. headquarters state. Because Compustat reports only the current headquarters location, we assign each firm-year the headquarters state reported on the cover page of that year's 10-K filing. To focus on firms covered by the acts, we define coverage on pre-adoption revenue: we keep firms with revenue below $500 million in their first sample year, provided that year precedes the effective date of their headquarters state's act, and we retain all of their later firm-years even if revenue subsequently exceeds the threshold. Sample membership therefore cannot respond to adoption, and because some covered firms later outgrow the threshold and lose protection, our estimates are intent-to-treat effects of baseline coverage. Internet Appendix Section IA.B reports threshold-crossing rates by treatment status. The final sample contains 2,614 firms and 23,870 firm-years; 548 firms are headquartered in states that adopt a PSPA.

We measure four outcomes. Receivable days equal accounts receivable divided by sales, multiplied by 365. Cash holdings equal cash and short-term investments divided by total assets, an outcome that has trended upward for U.S. firms over our period (Bates, Kahle, and Stulz, 2009). Investment equals capital expenditures divided by lagged net property, plant, and equipment. Short-term debt equals debt in current liabilities divided by total assets. We winsorize all ratios at the 1st and 99th percentiles. We classify firms as financially constrained if their baseline size-age index (Hadlock and Pierce, 2010) is above the sample median, and as customer-concentrated if the share of sales to customers disclosed as major customers in the Compustat segment files is above the sample median. Internet Appendix Section IA.B gives detailed variable definitions.

Table 1 reports summary statistics for 2004–2008, before the first act took effect. Firms in adopting and non-adopting states are similar: normalized differences are below 0.06 for every variable, well under the 0.25 threshold commonly used to flag imbalance. The typical sample firm collects receivables in about 58 days and holds about 17% of its assets in cash.

**Table 1: Summary Statistics Before the First Adoption (2004–2008)**

| Variable | Adopting states: mean | Adopting states: SD | Non-adopting states: mean | Non-adopting states: SD | Normalized difference |
|---|---|---|---|---|---|
| Receivable days | 58.4 | 31.2 | 57.1 | 30.8 | 0.04 |
| Cash/assets (%) | 17.3 | 15.9 | 18.0 | 16.4 | -0.04 |
| Investment (%) | 21.5 | 19.7 | 20.8 | 19.1 | 0.04 |
| Short-term debt/assets (%) | 6.2 | 7.4 | 6.0 | 7.1 | 0.03 |
| Total assets ($ million) | 182.6 | 141.3 | 176.9 | 138.5 | 0.04 |
| Sales/assets | 1.08 | 0.62 | 1.05 | 0.60 | 0.05 |
| Book leverage (%) | 22.4 | 18.9 | 21.7 | 18.5 | 0.04 |
| Firm age (years) | 17.8 | 11.6 | 18.3 | 12.0 | -0.04 |
| Number of firms | 548 | | 2,066 | | |

*Notes:* The sample contains Compustat firms with pre-adoption (baseline) revenue below $500 million, excluding financials and utilities. Adopting states are the fourteen states that adopt a PSPA between 2009 and 2019. The normalized difference is the difference in means divided by the square root of the average of the two group variances. This table reports descriptive statistics only and contains no estimated coefficients.

## 4. Empirical Strategy

### 4.1 Estimator

Because PSPAs were adopted in six cohorts and their effects may build over time and differ across cohorts, a static two-way fixed effects regression would use already-treated firms as controls for later adopters and can place negative weights on some cohort-period effects (Goodman-Bacon, 2021; de Chaisemartin and D'Haultfœuille, 2020; Baker, Larcker, and Wang, 2022). We therefore estimate group-time average treatment effects, ATT(g, t) = E[Y_t(g) - Y_t(0) | G = g], for each adoption cohort g and year t, using the doubly robust estimator of Callaway and Sant'Anna (2021) and Sant'Anna and Zhao (2020). The comparison group consists of firms headquartered in states that have not yet adopted by year t, and the covariates are baseline firm size, book leverage, sales-to-assets, and two-digit SIC industry. We aggregate the ATT(g, t) into an overall effect that weights cohorts by their number of firms, and into event-time effects for e = -5, ..., 6, where e = 0 is the year the act takes effect and the reference period is e = -2 (Section 4.2). For comparison, the static two-way fixed effects estimate for receivable days is -4.9, and a Goodman-Bacon (2021) decomposition attributes 27% of its weight to comparisons that use earlier adopters as controls. The interaction-weighted estimator of Sun and Abraham (2021) and the imputation estimator of Borusyak, Jaravel, and Spiess (2024) yield -6.5 and -7.1 days, respectively (Internet Appendix Section IA.C).

### 4.2 Identifying Assumptions

Identification requires that, absent adoption, outcomes of supplier firms in adopting states would have evolved in parallel with those of firms in not-yet-adopting states, conditional on the baseline covariates. The main threat is that states adopted PSPAs in response to deteriorating conditions for local suppliers. Table 2 reports linear probability models of adoption in year t for states that have not yet adopted. Neither lagged state GDP growth, the unemployment rate, the small-business share of employment, nor the average receivable days of in-state suppliers predicts adoption, individually or jointly, and adding the governor's party does not change this conclusion.

**Table 2: Predictors of PSPA Adoption Timing**

| | (1) | (2) |
|---|---|---|
| State GDP growth (t-1) | 0.21 | 0.18 |
| | (0.34) | (0.35) |
| Unemployment rate (t-1) | -0.15 | -0.12 |
| | (0.29) | (0.31) |
| Small-business employment share (t-1) | 0.06 | 0.05 |
| | (0.09) | (0.10) |
| Average supplier receivable days (t-1) | 0.02 | 0.02 |
| | (0.04) | (0.04) |
| Democratic governor | | 0.74 |
| | | (0.81) |
| Year fixed effects | Yes | Yes |
| Observations (state-years at risk) | 742 | 742 |
| R-squared | 0.04 | 0.05 |
| Joint test p-value, economic variables | 0.58 | 0.61 |

*Notes:* The sample contains state-years from 2004 to 2019 for the 50 states and the District of Columbia; states exit the sample after their PSPA takes effect. The dependent variable equals 100 if the state's PSPA takes effect in year t and 0 otherwise. Explanatory variables are measured in percent or days. Standard errors clustered by state are in parentheses. None of the coefficients is significant at the 10% level.

Two further assumptions matter. First, there must be no anticipation before the reference period. We date treatment at the effective date, but because enactment preceded the effective date by six to nine months, enactment falls in event year e = -1, when buyers and suppliers could already respond. We therefore allow one year of anticipation: every ATT(g, t) uses e = -2, the last year before enactment, as its base period (anticipation of one period in the Callaway and Sant'Anna, 2021, framework), and we report the e = -1 coefficient as a direct test for anticipatory responses. Second, adoption should not change outcomes for control firms. If large buyers responded to a PSPA by lengthening terms for suppliers in other states, our estimates would overstate the effect. Internet Appendix Section IA.E shows that receivable days of suppliers in non-adopting states do not change when a neighboring state adopts.

## 5. Results

### 5.1 Main Effects

Table 3 reports the overall effect of PSPA adoption on the four outcomes. Adoption shortens receivable days by 6.8 days (standard error 1.7). Relative to the pre-adoption mean of 58.4 days among treated firms, this is an 11.6% decline. For the median firm, with a sales-to-assets ratio of 1.08, collecting receivables 6.8 days sooner releases liquidity equal to about 2.0% of total assets.

Suppliers use the released liquidity in three ways. Cash holdings fall by 0.9 percentage points of assets (standard error 0.4), a 5.2% decline, consistent with a lower precautionary need for cash when receivables are collected faster and more predictably. Short-term debt falls by 1.1 percentage points of assets (standard error 0.5), a 17.7% decline, consistent with suppliers repaying the working-capital lines that financed their receivables. Investment rises by 2.4 percentage points of lagged capital (standard error 0.8), an 11.2% increase relative to the pre-adoption mean of 21.5%.

**Table 3: Effects of PSPA Adoption on Supplier Balance Sheets**

| | (1) Receivable days | (2) Cash/assets | (3) Investment | (4) Short-term debt/assets |
|---|---|---|---|---|
| PSPA adoption | -6.8*** | -0.9** | 2.4*** | -1.1** |
| | (1.7) | (0.4) | (0.8) | (0.5) |
| Pre-adoption mean, treated firms | 58.4 | 17.3 | 21.5 | 6.2 |
| Implied change (%) | -11.6 | -5.2 | 11.2 | -17.7 |
| Pre-trend joint test p-value | 0.71 | 0.52 | 0.64 | 0.47 |
| Treated firms | 548 | 548 | 548 | 548 |
| Firms | 2,614 | 2,614 | 2,614 | 2,614 |
| Firm-years | 23,870 | 23,870 | 23,870 | 23,870 |

*Notes:* Each column reports the overall average effect of PSPA adoption on the outcome indicated, estimated as described in Section 4.1 on Compustat firm-years from 2004 to 2022. Cash, investment, and short-term debt are measured in percentage points. The base period is e = -2, the year before enactment, allowing one year of anticipation (Section 4.2). The pre-trend test is a joint Wald test that the event-time coefficients for e = -5 to -3 are all zero. Standard errors clustered by state of headquarters (51 clusters) are in parentheses. \*, \*\*, and \*\*\* denote significance at the 10%, 5%, and 1% levels.

### 5.2 Dynamics

Figure 2 plots event-time estimates for receivable days and investment. Before enactment, the coefficients are small and statistically indistinguishable from zero; the joint test p-values are 0.71 for receivable days and 0.64 for investment. In the anticipation year e = -1, between enactment and the effective date, the estimates are -0.4 days (standard error 1.1) for receivable days and 0.2 percentage points (standard error 0.7) for investment, so we find no evidence that buyers or suppliers responded before the cap took effect. After adoption, receivable days fall by 3.1 days in the effective year, by 5.9 days in the first full year, and by 7.4 days in the second year, stabilizing at about 8.2 days from the third year onward. This gradual pattern matches the roll-over of annual supply contracts. Investment responds with a lag: the estimate is 0.6 percentage points in the effective year, 2.5 in the second year, and 3.3 in the fourth year. Estimates beyond the third year exclude the 2019 cohort, which we observe for only three post-adoption years.

**Figure 2: Dynamic Effects of PSPA Adoption on Receivable Days and Investment**

*Event-time point estimates with 95% confidence intervals for e = -5 to 6, where e = 0 is the year the act takes effect; the reference period is e = -2, the year before enactment, and e = -1 is the anticipation year; left panel receivable days, right panel investment.*

### 5.3 Heterogeneity and Mechanism

If PSPAs matter because they relax financing constraints, the investment response should be concentrated among suppliers that cannot easily replace trade-credit financing with outside funds. Panel A of Table 4 confirms this prediction. Receivable days fall by similar amounts for constrained and unconstrained suppliers (7.3 and 6.1 days), but investment rises by 3.9 percentage points among constrained suppliers and by an insignificant 0.8 percentage points among unconstrained suppliers; the difference is significant (p = 0.04). The same liquidity shock thus produces an investment response only where external finance is costly.

Panel B splits suppliers by customer concentration. Before adoption, suppliers that depend on a few large customers have the least bargaining power over payment terms. Receivable days fall by 9.7 days for customer-concentrated suppliers and by 3.6 days for other suppliers (p = 0.04 for the difference), which indicates that the cap binds most where buyer power was greatest.

**Table 4: Heterogeneity by Financial Constraints and Customer Concentration**

| | (1) Receivable days | (2) Investment |
|---|---|---|
| *Panel A: Financial constraints* | | |
| Constrained suppliers | -7.3*** | 3.9*** |
| | (2.1) | (1.2) |
| Unconstrained suppliers | -6.1*** | 0.8 |
| | (1.9) | (0.9) |
| p-value, difference | 0.67 | 0.04 |
| *Panel B: Customer concentration* | | |
| High customer concentration | -9.7*** | 3.1*** |
| | (2.4) | (1.1) |
| Low customer concentration | -3.6** | 1.5 |
| | (1.8) | (1.0) |
| p-value, difference | 0.04 | 0.28 |

*Notes:* Each cell reports the overall average effect of PSPA adoption estimated as in Table 3 within the indicated subsample. Constrained suppliers have a baseline size-age index above the sample median; high customer concentration denotes a baseline major-customer sales share above the sample median. Investment is measured in percentage points. Standard errors clustered by state of headquarters are in parentheses. \*, \*\*, and \*\*\* denote significance at the 10%, 5%, and 1% levels.

## 6. Robustness

The main alternative explanation for our results is that adoption coincided with state-specific economic shocks that independently affected supplier balance sheets. We address this concern in two ways. First, we add census-division-by-year fixed effects, so that adopting states are compared only with non-adopting states in the same region and year. The estimates are -6.2 days (standard error 1.8) for receivable days and 2.1 percentage points (standard error 0.9) for investment. Second, we run a placebo test on firms headquartered in adopting states whose pre-adoption revenue exceeds the $500 million coverage threshold. These firms face the same local economic conditions but are not protected by the acts. Their receivable days change by -0.7 days (standard error 1.5) and their investment by 0.3 percentage points (standard error 0.8), neither significant.

Our results are also robust to alternative samples and comparison groups. Excluding the 2009 cohort, whose post-period overlaps with the financial crisis, yields -6.5 days and 2.2 percentage points. Using only never-adopting states as controls yields -7.0 days and 2.5 percentage points. Dropping firms that relocate their headquarters during the sample, changing the winsorization threshold, and randomization inference over adoption dates leave the conclusions unchanged (Internet Appendix Sections IA.C and IA.D). Finally, because insignificant pre-trend tests can have low power (Roth, 2022), we apply the relative-magnitude bounds of Rambachan and Roth (2023). The effect on receivable days remains significant unless post-adoption violations of parallel trends exceed 1.4 times the largest pre-adoption violation; the corresponding breakdown value for investment is 0.9.

## 7. Conclusion

Prompt Supplier Payment Acts shortened the time small and mid-sized public suppliers wait to be paid, and suppliers used the released liquidity to reduce cash holdings and short-term debt and, when financially constrained, to invest more. The results indicate that payment terms imposed by large buyers bind on the investment of constrained suppliers, and that regulating those terms can relax financing constraints.

Our estimates have limits. They describe public suppliers below the coverage threshold before adoption, which are larger and less constrained than the private firms that make up most covered suppliers, so the effects for the typical covered firm may be larger. They capture supplier-side responses only; buyers that lose trade-credit financing may adjust prices, order volumes, or supplier choice, and a full welfare assessment would weigh these costs against the supplier gains. Studying the buyer-side and general-equilibrium consequences of payment-term regulation is a natural next step.

## Data Availability Statement

Compustat data are available from S&P Global through Wharton Research Data Services under license and cannot be redistributed by the authors. The hand-collected PSPA enactment and effective dates, the statutory citations, and all code that reproduces the tables and figures will be provided to the Journal's Data Editor and published in the Supplementary Information upon acceptance, in accordance with the AFA Data and Code Sharing Policy.

## Disclosure Statement

Avery L. Quillon: I have nothing to disclose. Tobias R. Venn: I have nothing to disclose. This research received no external funding.

## References

Almeida, Heitor, Murillo Campello, and Michael S. Weisbach, 2004, The cash flow sensitivity of cash, *Journal of Finance* 59, 1777–1804.

Baker, Andrew C., David F. Larcker, and Charles C. Y. Wang, 2022, How much should we trust staggered difference-in-differences estimates? *Journal of Financial Economics* 144, 370–395.

Barrot, Jean-Noël, 2016, Trade credit and industry dynamics: Evidence from trucking firms, *Journal of Finance* 71, 1975–2016.

Barrot, Jean-Noël, and Ramana Nanda, 2020, The employment effects of faster payment: Evidence from the federal Quickpay reform, *Journal of Finance* 75, 3139–3173.

Bates, Thomas W., Kathleen M. Kahle, and René M. Stulz, 2009, Why do U.S. firms hold so much more cash than they used to? *Journal of Finance* 64, 1985–2021.

Borusyak, Kirill, Xavier Jaravel, and Jann Spiess, 2024, Revisiting event-study designs: Robust and efficient estimation, *Review of Economic Studies* 91, 3253–3285.

Callaway, Brantly, and Pedro H. C. Sant'Anna, 2021, Difference-in-differences with multiple time periods, *Journal of Econometrics* 225, 200–230.

de Chaisemartin, Clément, and Xavier D'Haultfœuille, 2020, Two-way fixed effects estimators with heterogeneous treatment effects, *American Economic Review* 110, 2964–2996.

Goodman-Bacon, Andrew, 2021, Difference-in-differences with variation in treatment timing, *Journal of Econometrics* 225, 254–277.

Hadlock, Charles J., and Joshua R. Pierce, 2010, New evidence on measuring financial constraints: Moving beyond the KZ index, *Review of Financial Studies* 23, 1909–1940.

Klapper, Leora, Luc Laeven, and Raghuram Rajan, 2012, Trade credit contracts, *Review of Financial Studies* 25, 838–867.

Murfin, Justin, and Ken Njoroge, 2015, The implicit costs of trade credit borrowing by large firms, *Review of Financial Studies* 28, 112–145.

Petersen, Mitchell A., and Raghuram G. Rajan, 1997, Trade credit: Theories and evidence, *Review of Financial Studies* 10, 661–691.

Rambachan, Ashesh, and Jonathan Roth, 2023, A more credible approach to parallel trends, *Review of Economic Studies* 90, 2555–2591.

Roth, Jonathan, 2022, Pretest with caution: Event-study estimates after testing for parallel trends, *American Economic Review: Insights* 4, 305–322.

Sant'Anna, Pedro H. C., and Jun Zhao, 2020, Doubly robust difference-in-differences estimators, *Journal of Econometrics* 219, 101–122.

Sun, Liyang, and Sarah Abraham, 2021, Estimating dynamic treatment effects in event studies with heterogeneous treatment effects, *Journal of Econometrics* 225, 175–199.

## Internet Appendix

Internet Appendix for "Paid on Time: Prompt-Payment Mandates, Trade Credit, and Supplier Investment." This appendix is bundled at the end of the submitted PDF and does not count toward the page limit.

- Section IA.A: Statutory citations, enactment dates, and effective dates of each state's PSPA.
- Section IA.B: Sample construction and variable definitions.
- Section IA.C: Additional robustness checks.
- Section IA.D: Randomization inference over adoption dates.
- Section IA.E: Spillovers to suppliers in neighboring non-adopting states.
