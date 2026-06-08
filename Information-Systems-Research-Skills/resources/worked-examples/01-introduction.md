> **Illustrative teaching example.** The paper, platform, and every number below are **fictional** and
> exist only to demonstrate ISR house style. No real-paper facts are stated; no real platform or policy
> is described. Corresponding skills:
> [`isr-writing-style`](../../skills/isr-writing-style/SKILL.md),
> [`isr-contribution-framing`](../../skills/isr-contribution-framing/SKILL.md),
> [`isr-topic-selection`](../../skills/isr-topic-selection/SKILL.md), and
> [`isr-theory-development`](../../skills/isr-theory-development/SKILL.md).

# Worked Example: An ISR-Style Introduction (before → after)

This demonstrates the **ISR introduction arc** that `isr-writing-style` and `isr-contribution-framing`
require: **front-load the IS contribution** — phenomenon → *why the IT artifact makes it an IS question*
→ the gap/tension in a **named IS conversation** → what you do → what you find → the **intradisciplinary
bridge** — written so a behavioral, economic, design-science, *and* organizational reader can all follow
it. Unlike a general-economics intro, the ISR bar is **IT-artifact centrality** and **sociotechnical
co-determination**, not just a clean headline number.

**Illustrative paper (fictional):** *"When the Algorithm Explains Itself: Explanation Affordances and
Seller Effort on a Two-Sided Marketplace."* Fictional setting: a digital marketplace that, in different
regions at different times, switched on a feature showing third-party sellers *why* the ranking algorithm
placed their listing where it did.

> **Note on the code kit.** The econometric skeleton in [`../code/`](../code/) (staggered DiD, IV, RDD,
> DML) is **supporting infrastructure** for the empirical genre here — it executes the identification once
> the IS argument is set. In ISR the lead is the *IT artifact and the sociotechnical mechanism*; the
> estimator is demoted to a tool, exactly as in the "after" below.

---

## Before (buries the IS contribution — typical first-draft intro)

> Two-sided platforms have been studied extensively across information systems, economics, and marketing.
> Many papers examine seller behavior, ranking, and pricing. In this paper, we use a Callaway and
> Sant'Anna (2021) staggered difference-in-differences estimator to study the effect of an algorithmic
> transparency feature on a large marketplace. We assemble a region-by-month panel and estimate
> event-study specifications, supplemented with an instrumental-variables robustness check. Platform
> governance is an important topic for managers and regulators. Section 2 reviews the literature, Section 3
> describes the data, Section 4 presents the empirical strategy, Section 5 reports results, and Section 6
> concludes.

**What's wrong (against `isr-writing-style` / `isr-contribution-framing` / `isr-topic-selection`):**

- **Buried lede / leads with method** ("we use a Callaway and Sant'Anna estimator") — a named anti-pattern;
  the IS contribution surfaces only in the results, if at all.
- **No "why is this an *IS* question?"** The IT artifact (the explanation feature) is treated as wallpaper —
  swap it for any policy change and the sentence survives, which `isr-topic-selection` flags as weak fit.
- **No named IS conversation.** "Studied extensively across IS, economics, and marketing" names no stream
  the paper changes; the contribution is left for the reader to reconstruct.
- **No sociotechnical framing and no intradisciplinary bridge** — the move ISR prizes most.
- **No mechanism.** A decorated correlation ("effect of a feature") with no theorized process.
- **Throat-clearing** ("studied extensively," "an important topic") and an **over-signposted roadmap**
  doing the argument's job.

---

## After (ISR arc — IS contribution front-loaded, IT artifact load-bearing, bridge named)

> **When a marketplace algorithm starts telling sellers *why* it ranked them, do sellers respond by
> improving their listings — or by gaming the disclosed signals?** We show that switching on an
> explanation affordance raises measured listing quality by 18% among third-party sellers, but the gain is
> concentrated in the signals the algorithm reveals and absent elsewhere — evidence that *algorithmic
> transparency reshapes effort by redirecting it, not just increasing it.* *(phenomenon + headline finding +
> why it is an IS question, in the first breath — the IT artifact is the subject of the sentence.)*
>
> This is an information-systems question because the **explanation affordance is the mechanism, not the
> setting**: the same disclosure on a different ranking technology — one that surfaced different features —
> would move seller effort to different margins. The phenomenon is **sociotechnical**: a technical
> affordance (what the model exposes) and a social response (how sellers reallocate scarce effort)
> co-determine the outcome. *(IT-artifact centrality + sociotechnical framing, stated plainly.)*
>
> We engage a tension between two IS conversations that rarely speak. The **design-science / explainable-AI**
> stream treats explanation as a transparency good that builds trust and improves decisions; the
> **platform-governance and information-economics** stream warns that any disclosed signal becomes a target
> sellers optimize against (a digital analog of "teaching to the test"). We bridge them: explanation is
> *both* — it informs and it is gamed — and which dominates depends on the artifact's design.
> *(named IS conversations + the intradisciplinary bridge ISR prizes, stated early.)*
>
> We exploit the staggered regional rollout of the explanation feature, comparing each region to
> not-yet-treated regions and verifying no differential pre-trends in listing quality before activation.
> *(identification named only after the IS argument — the estimator is a tool, per the code kit.)* Listing
> quality rises **18%** on disclosed dimensions, with effects that grow over the three months after
> activation and are flat before it; on non-disclosed dimensions the effect is a precise zero, and we trace
> the redirection to sellers reallocating effort toward exactly the features the explanation surfaces.
> *(headline finding restated with the mechanism, not just an average effect.)*
>
> Our contribution to IS is to reframe **algorithmic explanation as an incentive technology, not only an
> information good**: by making the ranking legible, the platform changes *what sellers optimize*, so
> explanation design is governance design. *(contribution front-loaded, relative to a specific prior view —
> as `isr-contribution-framing` requires, and echoing the ~500-word cover-letter statement.)* This
> connects an economic logic (disclosed signals as contractible targets) to a design-science logic
> (explanation affordances as artifacts), and it implies that **any system exposing its own decision logic —
> credit-scoring explanations, content-moderation appeals, search-ranking disclosures — should be evaluated
> partly by which behaviors it makes worth gaming.** *(broad lesson that travels, kept inside IS.)*
>
> The paper proceeds as follows. Section 2 develops the affordance-and-incentives mechanism; Section 3
> describes the rollout and identification; Section 4 reports the redirection result and mechanism evidence.
> *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the ISR bar

Mapped to the skill checklists:

- **IS contribution front-loaded** — the first paragraph states the phenomenon, the finding, and *why it is
  an IS question*; the contribution ("explanation as an incentive technology") is stated early, not left to
  the discussion (`isr-writing-style`: intro front-loads the IS contribution; `isr-contribution-framing`:
  state it in the "we show that…" sentences).
- **IT-artifact centrality** — the explanation affordance is the subject and the mechanism; the explicit
  counterfactual ("a different ranking technology would move effort to different margins") passes the
  `isr-topic-selection` test *would the prediction change if the technology were different?*
- **Sociotechnical co-determination** — a technical affordance and a social effort-response jointly produce
  the outcome, not a generic effect dressed in platform data.
- **Intradisciplinary bridge named in plain language** — design-science/XAI ↔ platform-governance/
  information-economics, the silo-bridging move ISR values over a single-paradigm increment
  (`isr-theory-development`, `isr-contribution-framing`).
- **Mechanism, not a decorated correlation** — effort *redirection* (disclosed vs. non-disclosed margins)
  is theorized a priori and tested, satisfying `isr-theory-development`'s "explicit mechanism + boundary
  conditions," with the level of analysis (the seller) named.
- **Method demoted to a tool** — the staggered-DiD identification and the no-pre-trends check appear only
  where the design is introduced, never as the lead; the [`../code/`](../code/) skeleton executes it. This
  is the ISR ordering: IS argument first, estimator second.
- **Genre is explicit** — an archival/quasi-experimental empirical paper (per `isr-methods`), so the design
  discipline is identification + parallel-trends evidence, routed through the shared
  [reviewer-objection-checklist](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
  and [reporting-standards](../../../shared-resources/empirical-methods/reporting-standards.md).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** ISR papers
> whose intros execute this arc across the behavioral, archival, analytical, and design-science genres, and
> [`../code/`](../code/) for the staggered-DiD command chain that the empirical genre above leans on as
> supporting infrastructure.
