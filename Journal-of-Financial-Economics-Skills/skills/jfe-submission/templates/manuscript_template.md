# JFE Manuscript Skeleton

A structural template for a Journal of Financial Economics submission (Elsevier; ISSN
0304-405X). Adapt the proportions to your paper (corporate finance vs. asset pricing).
JFE submission norms to honor: **abstract <= 100 words**, **double-spaced, 12-pt+,
>= 1-inch margins**, **author-date references**, online appendix **appended to the end of
the main file**, and a **code + non-proprietary-data** deposit to Mendeley Data at
acceptance. Confirm all current rules on jfinec.com before submitting.

---

## Title page (SEPARATE file — not in the anonymized manuscript)

> Title
> Authors, affiliations, contact email (corresponding author marked)
> Acknowledgments
> Funding / grant disclosures
> Prior-presentation note (conferences / seminars / working-paper series)

## Conflict-of-interest disclosure statements (SEPARATE single PDF)

> One statement per author, all gathered in one PDF and uploaded separately; state
> "nothing to disclose" explicitly where that applies. Required again at resubmission.

## Anonymized manuscript

### Abstract (<= 100 words, result-forward)
State, within JFE's 100-word limit: the question, the setting/design, the headline finding
(with direction and rough magnitude), and why it matters. Lead with the result, not
the literature. Every word must earn its place at 100 words.

JEL Classification: ...
Keywords: ...; ...; ...

---

### 1. Introduction
- Para 1: the question and why it matters.
- Para 2: what you do (setting, design, data) — concretely.
- Para 3: what you find — headline result with magnitude.
- Para 4: why it is credible — one or two sentences on identification/inference.
- Para 5: the contribution, stated explicitly relative to the closest 3–5 papers.
- (Optional) brief roadmap.

### 2. Related literature and contribution
- Organize by the 2–4 debates the paper enters, not chronologically.
- For the closest papers: what they show / where they stop / your difference.
- Engage the theory you test or are motivated by.
- Answer "isn't this already known?" directly.

### 3. Institutional setting / hypotheses (as applicable)
- Corporate finance: describe the shock/rule/setting that provides identifying variation.
- Asset pricing: state the economic mechanism and the testable prediction.

### 4. Data and variable construction

#### 4.1 Sample
Population, time period, every filter, and how filters could induce selection.

#### 4.2 Variable definitions

| Role                | Variable | Definition (source, timing, transformation) |
|---------------------|----------|----------------------------------------------|
| Dependent           |          |                                              |
| Key independent     |          |                                              |
| Controls            |          |                                              |
| Instruments / FE    |          |                                              |

State winsorization/trimming rules here.

### 5. Empirical design / identification
- Corporate finance: the design (natural experiment / RDD / IV / matching+DID), the
  identifying assumption, and the estimating equation.
- Asset pricing: portfolio construction (sorting variable, breakpoints, weighting),
  the estimator (Fama–MacBeth / GMM), and the benchmark factor models.
- State the standard-error treatment (cluster dimensions / Newey–West / Shanken).

### 6. Results

#### 6.1 Main result
Baseline estimates; interpret economic magnitude, not only significance.

#### 6.2 Identification evidence
Parallel trends / first-stage strength / discontinuity / manipulation test.

#### 6.3 Mechanism / channel
Evidence on *why* the effect arises; tests that distinguish your channel.

#### 6.4 Robustness (headline checks)
The 3–6 most decisive checks; point to the Internet Appendix for the rest.

#### 6.5 Ruling out alternative explanations
For each rival story, the test that distinguishes it from yours.

### 7. Conclusion
Restate the contribution, the limits of what you can claim, and what it implies for
theory, empirical work, or practice. Do not overclaim.

---

## References
- Every in-text citation appears here and vice versa.
- **Author-date (name-year)** style per the JFE guide.
- Attribute the canon correctly: Jensen & Meckling (1976), Fama & French (1993, 2015), and Banz (1981) are JFE; Carhart (1997) is *Journal of Finance*.

## Internet Appendix (appended to the end of the main manuscript file, per JFE practice)
- Proofs and derivations.
- Secondary robustness (alternative measures, subsamples, extra cluster levels, wild bootstrap).
- Granular variable-construction details.
- Additional / "untabulated" results referenced in the main text.
- Numbered in its own series (Table IA.1, Figure IA.1, ...), self-contained, matching the main text's reporting conventions.

## Replication package (JFE data-and-code-sharing policy)
- For papers originally submitted on/after 1 July 2021: **code and non-proprietary data are mandatory** at acceptance, deposited to **Mendeley Data** (or a domain repository) and linked from ScienceDirect.
- Document the access path for restricted data (CRSP, Compustat, etc.); request any exemption in the **cover letter** of the initial submission.
