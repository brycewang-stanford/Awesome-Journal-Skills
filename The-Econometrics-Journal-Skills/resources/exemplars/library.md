# The Econometrics Journal — Exemplars Library (theme × contribution)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked against
> Oxford Academic's Econometrics Journal article pages (`academic.oup.com/ectj/...`) and corroborated
> on RePEc/EconPapers (`ect/emjrnl` or `wly/emjrnl`) to confirm it actually appeared in **The
> Econometrics Journal** (Oxford University Press on behalf of the Royal Economic Society; DOIs of the
> form `10.1111/ectj...` or `10.1111/j.1368-423X...`), with year, volume/issue, and page range. Papers
> that could not be fully verified as EctJ were **omitted** — this is deliberately a short, clean list
> (6 verified) rather than a long, uncertain one.
>
> **Sibling-confusion guard.** The Econometrics Journal is **NOT** the *Journal of Econometrics*
> (Elsevier), *Econometrica* (Econometric Society / Wiley, DOI `10.3982/ECTA...`), *Econometric Theory*
> (Cambridge UP), or the *Journal of Business & Economic Statistics* (JBES, Taylor & Francis). Every
> entry's `10.1111/ectj` or `10.1111/j.1368-423X` DOI and OUP/RES imprint were confirmed precisely to
> avoid attributing a sibling-journal paper to EctJ.
>
> **Use principle (zero hallucination):** this file gives **contribution positioning only**. It does
> not reproduce or invent theorems, simulation numbers, or coefficients — read the original on Oxford
> Academic before citing any result. For EctJ-specific policy and scope, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **theme × contribution** is closest to yours, then study how that paper makes a
*compact, leading-case* methodological advance carry **direct applied value** — the EctJ bar (see
[`../../skills/ectj-topic-selection/SKILL.md`](../../skills/ectj-topic-selection/SKILL.md) and
[`../../skills/ectj-contribution-framing/SKILL.md`](../../skills/ectj-contribution-framing/SKILL.md)).
For each, ask the self-check question before claiming your paper is "EctJ-shaped." Model your
introduction on [`../worked-examples/01-introduction.md`](../worked-examples/01-introduction.md).

---

## By theme

### Cluster-robust inference / bootstrap (inference method)

- **MacKinnon & Webb, "The wild bootstrap for few (treated) clusters," The Econometrics Journal 2018, 21(2):114–135.**
  DOI `10.1111/ectj.12107`. Verified: `academic.oup.com/ectj/article-abstract/21/2/114/5078969`
  (corroborated `econpapers.repec.org/RePEc:wly:emjrnl:v:21:y:2018:i:2:p:114-135`).
  - **Why it is an exemplar:** a sharp finite-sample failure mode (cluster-robust t and the standard
    wild cluster bootstrap break with very few treated clusters) and a concrete inference fix — a
    leading-case method with obvious applied payoff for anyone running clustered DID-style designs.
  - **Self-check:** does your inference method target a failure applied researchers actually hit, and
    show the fix on a realistic design rather than only in simulation?

### Weak-instrument-robust inference (test inversion / confidence sets)

- **Davidson & MacKinnon, "Confidence sets based on inverting Anderson–Rubin tests," The Econometrics Journal 2014, 17(2):S39–S58.**
  DOI `10.1111/ectj.12015`. Verified: `academic.oup.com/ectj/article/17/2/S39/5056440`
  (corroborated `ideas.repec.org/a/wly/emjrnl/v17y2014i2ps39-s58.html`).
  - **Why it is an exemplar:** takes a workhorse weak-IV procedure (inverting the AR test) and
    characterises *when its confidence sets mislead* — a precise, leading-case clarification of a tool
    applied IV researchers use directly.
  - **Self-check:** does your contribution clarify the behaviour of a method practitioners already run,
    rather than introduce a tool no one disputes?

### Quantile regression for panel data (estimator + identification)

- **Canay, "A simple approach to quantile regression for panel data," The Econometrics Journal 2011, 14(3):368–386.**
  DOI `10.1111/j.1368-423X.2011.00349.x`. Verified: `academic.oup.com/ectj/article/14/3/368/5060937`
  (corroborated `ideas.repec.org/a/ect/emjrnl/v14y2011i3p368-386.html`).
  - **Why it is an exemplar:** identifies a fixed-effects quantile model under a transparent
    location-shift restriction and delivers an estimator simple enough to be used — compact theory
    with immediate applied uptake (the canonical "small idea, wide use" EctJ paper).
  - **Self-check:** is your identifying restriction stated plainly and your estimator simple enough
    that applied researchers will actually adopt it?

### Dynamic-panel GMM identification (weak instruments)

- **Bun & Windmeijer, "The weak instrument problem of the system GMM estimator in dynamic panel data models," The Econometrics Journal 2010, 13(1):95–126.**
  DOI `10.1111/j.1368-423X.2009.00299.x`. Verified: `academic.oup.com/ectj/article-abstract/13/1/95/5059803`
  (corroborated `econpapers.repec.org/article/ectemjrnl/v_3a13_3ay_3a2010_3ai_3a1_3ap_3a95-126.htm`).
  - **Why it is an exemplar:** diagnoses *why* a heavily-used estimator (system GMM) can be weakly
    identified, tying a concentration-parameter argument to a practical warning — leading-case theory
    that changes how applied panel work is specified.
  - **Self-check:** does your identification result explain a failure of a method in wide applied use,
    not just a special case of academic interest?

### Cross-section dependence in large panels (asymptotic theory + estimator)

- **Chudik, Pesaran & Tosetti, "Weak and strong cross-section dependence and estimation of large panels," The Econometrics Journal 2011, 14(1):C45–C90.**
  DOI `10.1111/j.1368-423X.2010.00330.x`. Verified: `academic.oup.com/ectj/article-abstract/14/1/C45/5060343`
  (corroborated `econpapers.repec.org/article/ectemjrnl/v_3a14_3ay_3a2011_3ai_3a1_3ap_3ac45-c90.htm`).
  - **Why it is an exemplar:** formalises *weak vs strong* cross-section dependence and shows when a
    practical estimator (CCE) stays valid — a definitional/asymptotic advance pinned to an estimator
    applied macro-panel researchers use.
  - **Self-check:** does your asymptotic framework deliver an estimator (or validity condition) an
    applied researcher can act on, not just a taxonomy?

### Diagnostic testing in panels (test statistic, finite-sample correction)

- **Pesaran, Ullah & Yamagata, "A bias-adjusted LM test of error cross-section independence," The Econometrics Journal 2008, 11(1):105–127.**
  DOI `10.1111/j.1368-423X.2007.00227.x`. Verified: `academic.oup.com/ectj/article-abstract/11/1/105/5063500`
  (corroborated York / Cambridge faculty publication pages).
  - **Why it is an exemplar:** a single, closed-form bias correction to a standard LM test that fixes
    its finite-sample over-rejection — exactly the compact, immediately-usable diagnostic EctJ favours.
  - **Self-check:** is your test correction cheap, closed-form, and a drop-in replacement for a
    statistic practitioners already report?

---

## By theme (each cell is a verified EctJ paper above)

| Theme | Verified EctJ exemplar | Year / vol(issue) : pages | Contribution type |
| --- | --- | --- | --- |
| Cluster-robust bootstrap inference | MacKinnon & Webb, "Wild bootstrap for few (treated) clusters" | 2018, 21(2):114–135 | Inference method |
| Weak-IV robust confidence sets | Davidson & MacKinnon, "Inverting Anderson–Rubin tests" | 2014, 17(2):S39–S58 | Test inversion / CIs |
| Panel quantile regression | Canay, "Quantile regression for panel data" | 2011, 14(3):368–386 | Estimator + identification |
| Dynamic-panel GMM identification | Bun & Windmeijer, "Weak instrument problem of system GMM" | 2010, 13(1):95–126 | Identification result |
| Cross-section dependence in large panels | Chudik, Pesaran & Tosetti, "Weak and strong cross-section dependence" | 2011, 14(1):C45–C90 | Asymptotic theory + estimator |
| Panel diagnostic testing | Pesaran, Ullah & Yamagata, "Bias-adjusted LM test" | 2008, 11(1):105–127 | Test statistic / correction |

---

## Omitted for lack of full verification (do not attribute to EctJ without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking:

- **Pesaran, "General Diagnostic Tests for Cross Section Dependence in Panels"** — surfaced widely as a
  CESifo / Cambridge / IZA **working paper** (2004), not a confirmed EctJ article page. The closely
  related *journal* contribution that **is** verified in EctJ is Pesaran, Ullah & Yamagata (2008),
  listed above. The working-paper title is omitted to avoid misattribution.
- Any candidate whose only hits were on `journalofeconometrics`/Elsevier, `econometricsociety.org` /
  `10.3982/ECTA...` (*Econometrica*), Cambridge UP *Econometric Theory*, or Taylor & Francis *JBES*
  pages was excluded by the sibling-confusion guard, regardless of topical fit.

Before adding any new paper to this library, confirm it on `academic.oup.com/ectj` (article page with
volume/issue and a `10.1111/ectj` or `10.1111/j.1368-423X` DOI) and update the access-date header.
When in doubt, omit.
