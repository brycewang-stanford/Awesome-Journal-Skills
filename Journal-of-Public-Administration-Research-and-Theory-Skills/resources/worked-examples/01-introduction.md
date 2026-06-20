> **Illustrative teaching example.** The paper, agency, intervention, and every number below are
> **fictional** and exist only to demonstrate JPART house style. No real agency, program, or finding is
> stated. Corresponding skills:
> [`jpart-writing-style`](../../skills/jpart-writing-style/SKILL.md),
> [`jpart-topic-selection`](../../skills/jpart-topic-selection/SKILL.md),
> [`jpart-theory-building`](../../skills/jpart-theory-building/SKILL.md), and
> [`jpart-research-design`](../../skills/jpart-research-design/SKILL.md).

# Worked Example: A JPART-Style Introduction (before → after)

This demonstrates the **JPART introduction bar** from `jpart-writing-style` and `jpart-theory-building`:
by the end of the introduction the reader knows the **public-management theory at stake, the mechanism,
the design, the headline result, and the implications for theory** — JPART's own abstract template asks
for exactly that arc. The funnel is **theoretical puzzle → why it matters for PA theory → why it is hard
to identify → setting & design → headline finding with the mechanism → contribution (extends/tests a PA
theory) → brief roadmap**, with JPART's distinctive demand that the contribution be *theoretical* (not a
program-evaluation result) and that the PA-specific threats (common-method bias, selection) be confronted.

**Illustrative paper (fictional):** *"When Clarity Motivates: Goal Ambiguity, Public Service Motivation,
and Frontline Performance."* Fictional setting: a public benefits agency that rolled out a goal-clarity
protocol to **different field offices in different months**, creating staggered within-agency variation.
(Theory: PSM × goal-ambiguity; method: staggered field experiment on real caseworkers. Chosen because it
*tests* a long-asserted PSM mechanism with a credible design — see the Perry exemplars in
[`../exemplars/library.md`](../exemplars/library.md).)

---

## Before (empirics-first, atheoretical — typical first draft)

> The literature on public service motivation is vast, and many studies link PSM to performance. In this
> paper, we use a staggered difference-in-differences design with the Callaway and Sant'Anna (2021)
> estimator to study a goal-clarity protocol introduced across the field offices of a benefits agency. We
> assemble a caseworker-month panel and estimate event-study specifications. Performance is an important
> outcome in public administration. Section 2 reviews the PSM literature, Section 3 describes our data,
> Section 4 presents the empirical strategy, Section 5 reports results, Section 6 discusses robustness, and
> Section 7 concludes.

**What's wrong (against `jpart-writing-style` / `jpart-theory-building`):**

- **Atheoretical framing.** It promises a correlation, not a theory move. JPART's whole bar is a
  **public-management theory contribution** — the named anti-pattern in `jpart-topic-selection`
  ("a finding with no mechanism").
- **Leads with method** ("we use a staggered DID design with Callaway–Sant'Anna") instead of the theory
  and mechanism — the `jpart-writing-style` anti-pattern of burying the contribution.
- **No mechanism and no implications for theory.** "Performance is an important outcome" is throat-clearing;
  the reader never learns *why* clarity would interact with PSM.
- **PA-specific threats ignored.** Nothing on common-method bias or selection — the first objections a JPART
  referee raises (`jpart-research-design`).
- **Over-signposted seven-section roadmap** padding the word count that JPART caps (the limit counts the
  abstract, tables, *and* references — `jpart-writing-style`).

---

## After (JPART arc — theory + mechanism + result, implications stated early)

> **Does telling public employees exactly what is expected of them unlock their motivation — or does
> clarity matter only for those who already care?** We show that a goal-clarity protocol raises frontline
> performance, but that the gain is concentrated among caseworkers high in public service motivation (PSM):
> clarity and motivation are **complements, not substitutes**. *(theoretical puzzle + headline finding in
> the first breath — a claim about a PA mechanism, not a program-evaluation number.)*
>
> Why this matters for public-administration theory: PSM theory has long predicted that motivated public
> employees perform better, but a recurring puzzle is *when* that motivation translates into performance.
> If goal ambiguity is the binding constraint that keeps PSM from showing up in output, then a feature
> managers can set — clarity — governs whether motivation pays off, and "low performance" of motivated
> employees may be an artifact of ambiguous tasks rather than weak motivation. *(the theory stake, framed
> for any PA scholar — `jpart-topic-selection` theory-contribution test.)*
>
> Identifying this cleanly is hard for two reasons. First, motivated employees may sort into clearer roles,
> so a cross-sectional correlation between clarity and performance would confound the protocol with
> selection. Second, if clarity and performance are both self-reported, common-method bias alone could
> manufacture the result. *(why it is hard — the PA-specific threats named plainly, per
> `jpart-research-design`.)*
>
> We exploit an agency that introduced the clarity protocol in different field offices in different months,
> for administrative reasons unrelated to local performance trends, and we measure performance with
> **administrative case-resolution records** rather than self-reports. The staggered timing lets us compare
> each office to not-yet-treated offices with a heterogeneity-robust difference-in-differences estimator,
> and we verify no differential pre-trends. *(setting & design in one paragraph; the estimator is named only
> as a tool, and the objective outcome defuses common-method bias.)*
>
> Clarity raises case resolution by **9%** on average, but by **17%** among high-PSM caseworkers and a
> precise **near-zero** among low-PSM caseworkers — and the gap opens only after the protocol arrives, never
> before. The mechanism is **not** simple effort: high-PSM caseworkers reallocate effort toward the cases
> the clarified goals prioritize, consistent with motivation being *channeled* by clarity rather than
> *created* by it. *(headline finding restated with the mechanism and a ruled-out rival — the
> `jpart-research-design` adjudication move.)*
>
> Our contribution is to show that **PSM and goal clarity are complements**: motivation is a latent
> resource that ambiguous tasks leave stranded, and a manageable design choice releases it. This *tests and
> bounds* a core PSM claim — motivated employees perform better **conditional on** low goal ambiguity — and
> reframes goal ambiguity from a background nuisance into a moderator that public managers control.
> *(contribution stated early as a *theory* move another PA scholar can import — `jpart-theory-building`
> portability test.)*
>
> The paper proceeds as follows. Section 2 develops the PSM × ambiguity argument and its observable
> implications; Section 3 presents the field-experimental design and the performance results; Section 4
> examines the effort-channeling mechanism and scope conditions. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the JPART bar

Mapped to the skill checklists:

- **Theory leads, mechanism is named** — the first lines state a PA theory move (PSM × clarity as
  complements) and the mechanism (motivation channeled, not created), satisfying `jpart-theory-building`
  and the abstract template (theory → … → implications for theory).
- **It tests/bounds a theory, not a program** — the contribution is framed as a conditional PSM claim a PA
  scholar can import, passing the `jpart-topic-selection` theory-contribution test (and steering clear of
  JPAM's program-evaluation lane).
- **PA-specific threats confronted up front** — selection (sorting into clear roles) and common-method bias
  are named, and the design defeats both (staggered timing + an **administrative** outcome), exactly the
  `jpart-research-design` adjudication move.
- **Method demoted to a tool** — the heterogeneity-robust staggered estimator appears only where the design
  is discussed; the estimator choice follows the modern-staggered-DiD guidance in [`../code/`](../code/).
- **Respects the cap** — three roadmap sections not seven, minimal jargon, framing legible to any PA reader
  within the JPART word limit (`jpart-writing-style`: ~12,000 words including abstract, tables, references).

> Next: stress-test the design with the shared
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
> and report results to the shared
> [`../../../shared-resources/empirical-methods/reporting-standards.md`](../../../shared-resources/empirical-methods/reporting-standards.md);
> benchmark the framing against verified real JPART papers in
> [`../exemplars/library.md`](../exemplars/library.md); and adapt the staggered-DiD command chain in
> [`../code/`](../code/).
