> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate CAR house style. No real-paper facts are stated, and no journal policy is
> invented — policy lives in [`../official-source-map.md`](../official-source-map.md). Corresponding
> skills: [`car-writing-style`](../../skills/car-writing-style/SKILL.md),
> [`car-contribution-framing`](../../skills/car-contribution-framing/SKILL.md), and
> [`car-literature-positioning`](../../skills/car-literature-positioning/SKILL.md).

# Worked Example: A CAR-Style Introduction (before → after)

This demonstrates the **front-loaded accounting introduction** required by `car-writing-style`
(open with the accounting question and why it matters; state the finding early rather than withholding
it; active voice; precise, consistent terminology) combined with `car-contribution-framing`
(state the contribution as a single falsifiable claim about *accounting*, matched to the research
tradition, with a credible practice/standard-setting implication) and `car-literature-positioning`
(join a live accounting conversation rather than gap-spot; defend the accounting locus against a
pure-finance reading).

**Illustrative paper (fictional):** *"Does Mandatory Segment Disclosure Discipline Internal Capital
Markets? Evidence from a Reporting-Standard Change."* Fictional setting: a reporting-standard amendment
that, in a fictional jurisdiction, forced diversified firms to report profit by operating segment on a
management-approach basis. The example is **archival / capital-markets** to match the dominant CAR
tradition; the same arc adapts to an experiment or analytical model (see `car-theory-development`).

---

## Before (buries the question and the finding — typical first-draft intro)

> The segment-reporting literature is large and has examined many aspects of disaggregated disclosure.
> Prior studies look at analyst forecasts, cost of capital, and proprietary costs. In this paper, we use
> a difference-in-differences design with firm and year fixed effects, entropy-balanced control firms,
> and standard errors clustered by firm, to study a change in segment-reporting requirements. We assemble
> a panel of diversified firms and estimate event-study specifications around the mandate. Segment
> disclosure is an important topic for standard-setters and investors. The remainder of the paper is
> organized as follows. Section 2 reviews the literature, Section 3 describes the sample, Section 4
> presents the research design, Section 5 reports results, Section 6 discusses robustness, and Section 7
> concludes.

**What's wrong (against `car-writing-style` / `car-contribution-framing` / `car-literature-positioning`):**

- **Mystery-novel intro** — the finding is withheld until the results, a named anti-pattern in
  `car-writing-style`.
- **Leads with method** ("we use a difference-in-differences design…") rather than the accounting
  question; the design is demoted-able detail, not the lead.
- **No predictions stated before results**, and no headline magnitude with units anywhere in the intro.
- **Gap-spotting / citation dumping** ("the literature is large… prior studies look at…") with no live
  conversation joined and no nearest neighbor distinguished — the `car-literature-positioning`
  anti-pattern.
- **Contribution absent**: no single claim about what we now understand differently about accounting, and
  no practice/standard-setting implication.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (CAR arc — accounting question + prediction + finding front-loaded, contribution early)

> **When a reporting standard forces diversified firms to disaggregate profit by operating segment, does
> the new disclosure discipline how those firms allocate capital internally — or merely change what
> outsiders see?** We find that mandatory segment-profit disclosure reduces cross-subsidization of
> underperforming segments: after the mandate, treated firms cut investment in segments with below-median
> returns by **3.2 percentage points** of segment assets relative to controls, and the reduction is
> concentrated where the newly disclosed segment was previously pooled out of view. *(accounting question +
> headline finding + units, in the first breath.)*
>
> Answering this cleanly is hard because firms do not disaggregate at random: a firm restructures or
> changes what it reports precisely when its internal capital market is already under pressure, so a naive
> before/after comparison conflates the disclosure with the conditions that prompted it. *(why it is
> hard — the identification problem, stated before the design.)*
>
> We exploit a reporting-standard amendment that compelled management-approach segment reporting for
> diversified firms above a size threshold, while leaving otherwise-similar firms below the threshold
> reporting as before. We compare treated firms to entropy-balanced control firms in a
> difference-in-differences design and show no differential pre-trends in segment investment before the
> mandate. *(setting, variation, and identification in one paragraph — design as a tool, not the lead.)*
>
> We predict, and find, that the effect is **larger where the disclosure is more binding**: among firms
> whose poorly performing segments had previously been aggregated into a residual "other" category, and
> among firms with weaker external monitoring before the mandate. *(directional, cross-sectional
> prediction stated before the result — the locus of theoretical content per `car-theory-development`.)*
>
> Our contribution is to identify a **real effect of financial-reporting disaggregation on internal
> capital allocation** — disclosure changes not only the firm's information environment but the
> allocation decision itself. This joins, and qualifies, the segment-disclosure conversation that has
> emphasized *outsiders'* information (analyst forecasts, cost of capital): we show the discipline can
> operate *inside* the firm, through managers anticipating that cross-subsidies will become visible.
> *(contribution as a single claim about accounting, stated early and relative to a specific prior view;
> accounting locus defended — this is a reporting effect, not a generic investment result.)* For
> standard-setters weighing disaggregation requirements, the implication is that the benefits of segment
> reporting may include **improved capital allocation**, not only improved outside transparency — a
> consequence the standard-setting debate has underweighted. *(credible standard-setting implication, tied
> to the actual result.)*
>
> The paper proceeds as follows. Section 2 develops the predictions and positions the contribution;
> Section 3 describes the mandate, sample, and design; Section 4 reports the main results and
> cross-sectional tests; Section 5 addresses identification threats. *(brief roadmap — no
> over-signposting.)*

---

## Why the "after" meets the CAR bar

Mapped to the skill checklists:

- **Question and finding front-loaded** — the accounting question and the headline magnitude (3.2 pp of
  segment assets) appear in the first paragraph, with units (`car-writing-style`: "open with the
  accounting question and why it matters; state the finding early").
- **Active voice, precise terminology** — *disclosure* vs. its real effect, *segment-profit* vs. residual
  aggregation, treated vs. entropy-balanced controls; construct and variable names are stated so they can
  stay identical across text, tables, and the code repository.
- **Prediction before result, with cross-sectional content** — the "more binding where previously pooled
  / weakly monitored" moderators carry the theoretical weight (`car-theory-development`), and are stated
  before the finding, not after.
- **Contribution as one falsifiable claim about accounting** — "a real effect of reporting disaggregation
  on internal capital allocation" — matched to the **archival** tradition (credibly identified evidence +
  the cross-sectional pattern that pins the mechanism), per `car-contribution-framing`.
- **Live conversation joined, accounting locus defended** — it qualifies the *outsider-information* view
  of segment disclosure rather than gap-spotting, and explicitly frames the result as a *reporting*
  effect, not a generic corporate-investment finding (`car-literature-positioning`).
- **Standard-setting implication tethered to the result** — improved capital allocation as an
  underweighted benefit of disaggregation, drawn from the actual finding, not hand-waved.
- **Method demoted to a tool** — the difference-in-differences design appears only where identification is
  discussed, never as the lead (avoids the shared "leading with the estimator" anti-pattern).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for real CAR papers (verified) whose
> introductions execute this arc across traditions, and [`../code/`](../code/) for the difference-in-
> differences / mechanism command chain referenced above. For abstract length, blinding, and reference
> style, defer to [`../official-source-map.md`](../official-source-map.md) and `car-writing-style` —
> invent no policy.
