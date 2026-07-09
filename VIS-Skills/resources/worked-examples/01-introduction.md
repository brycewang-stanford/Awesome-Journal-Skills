> **Illustrative teaching example.** The paper, system, study, and every number below are
> **fictional** and exist only to demonstrate IEEE VIS house style. No real-paper facts, projects,
> or results are stated, and no policy is invented. Corresponding skills:
> [`vis-writing-style`](../../skills/vis-writing-style/SKILL.md),
> [`vis-topic-selection`](../../skills/vis-topic-selection/SKILL.md), and
> [`vis-experiments`](../../skills/vis-experiments/SKILL.md).

# Worked Example: A VIS-Style Abstract + Introduction (before → after)

This demonstrates the **VIS first-page arc** from `vis-writing-style`:
**data-and-task problem → why existing representations are inadequate → contribution (technique
and/or finding) → evidence matched to the contribution type → what changes for people analyzing
data** — with the VIS expectations that the contribution is a *visualization* contribution, every
**encoding is justified by task**, and the **evaluation matches the claim** (a perceptual claim needs
a controlled study, not an accuracy number).

The framing also reflects `vis-topic-selection`: VIS is strongest when the lesson is about **how
people visually represent, interact with, and reason about data** — here, whether a new encoding
lets analysts read a specific pattern faster — rather than a modeling or rendering result whose
data-analysis task is incidental (which would route to ML or SIGGRAPH), and when the paper could not
simply be re-labeled as a CHI interaction study without loss.

**Illustrative paper (fictional):** *"BandGlyph: A Task-Justified Encoding for Reading Uncertainty
Trends in Ensemble Time Series."* Fictional contribution: an encoding for uncertainty bands in
ensemble forecasts, evaluated in a controlled study against the conventional spaghetti plot.

---

## Before (buries the visualization contribution — typical first-draft abstract + intro)

> **Abstract.** Visualization is essential for data analysis. We present BandGlyph, a beautiful new
> way to show ensemble time series using a novel glyph and a modern color scheme. Our interactive
> system is fast and intuitive, and users in our evaluation liked it, showing the promise of glyph
> design for uncertainty visualization.
>
> **Introduction.** Ensemble data is everywhere. Many tools show it with line charts. In this paper
> we design a new glyph with an attractive gradient and build an interactive system, and we evaluate
> it by asking users whether they found it useful, showing positive feedback. Section 2 covers
> related work, Section 3 our design, Section 4 the system, Section 5 the evaluation, Section 6
> concludes.

**What's wrong (against `vis-writing-style` / `vis-topic-selection` / `vis-experiments`):**

- **No data-and-task problem on the first page** — it leads with "visualization is essential" and an
  aesthetic claim, not a task an analyst recognizes. VIS wants the task-grounded contribution up
  front.
- **Design by aesthetics.** "Beautiful," "attractive gradient," "modern color scheme" — no encoding
  is justified by a task, and color may not even be CVD-safe. This is the fastest VIS reject.
- **Evaluation mismatched to the claim.** "Users liked it" is a preference anecdote, not evidence
  that the encoding helps read uncertainty trends — the actual claim. A perceptual claim needs a
  controlled study with effect sizes.
- **Contribution type unclear** — is this a technique, a system, or a study? The paper never commits,
  so no evidence standard is met.
- **No open-materials posture** — no mention of stimuli, data, code, or a video, which a VIS reviewer
  looks for immediately.
- **Over-signposted roadmap** substituting for an argument.

---

## After (VIS arc — task problem → inadequacy → contribution → matched evidence → what changes)

> **Abstract.** Analysts reading ensemble forecasts must judge how *uncertainty itself* trends over
> time — is the spread widening before a critical date? — yet the conventional spaghetti plot
> encodes spread only implicitly in line density, forcing a slow, error-prone visual integration. We
> contribute **BandGlyph**, an encoding that maps ensemble spread to a position-and-length channel
> (chosen because the task is ordered magnitude comparison, where position/length dominate color and
> area) and preserves individual-member tracing on demand. In a **preregistered within-subjects study
> (N justified by an a-priori power analysis)**, participants judged spread-trend direction more
> accurately and faster with BandGlyph than with a tuned spaghetti-plot baseline (effect sizes with
> 95% CIs in §6); we report the one task where the baseline was competitive. Stimuli, anonymized
> responses, the analysis notebook, and a system video are in the supplemental materials. *(task →
> inadequacy → encoding justified by task → matched controlled evidence → honest limitation — all on
> the first page.)*
>
> **Introduction.** *(¶1 — the data-and-task problem, first breath.)* When a meteorologist reads an
> ensemble forecast, the decision often hinges not on the mean path but on **how the spread evolves**
> — whether uncertainty is growing toward a landfall window. The visualization question is therefore
> not "can we draw the ensemble?" but **"which encoding lets an analyst read the *trend in spread*
> quickly and correctly?"**
>
> *(¶2 — why existing representations are inadequate.)* The spaghetti plot draws every member, so
> spread is encoded only as **line density** — a channel humans integrate poorly and slowly, and one
> that clutters as the ensemble grows. Summary bands show spread but discard member identity, which
> analysts need to trace scenarios. Neither directly supports the ordered-magnitude-comparison task
> that the trend judgment demands.
>
> *(¶3 — contribution, stated as a visualization claim.)* We make two contributions. First,
> **BandGlyph**, an encoding that maps spread to position-and-length — the channels most effective
> for ordered magnitude — while keeping member tracing available through interaction. Second, a
> **controlled study** of how accurately and quickly analysts read spread trends with BandGlyph
> versus the conventional plot.
>
> *(¶4 — evidence matched to the contribution type, each claim paired.)* Because the claim is about
> *perception of a trend*, the evidence is a preregistered controlled experiment: real ensemble
> stimuli (archived); a trend-direction task from an established task taxonomy; an a-priori power
> analysis fixing N; accuracy and completion time as measures; and effect sizes with confidence
> intervals comparing BandGlyph to a tuned baseline (§6). The palette is CVD-safe and the figures
> read in grayscale.
>
> *(¶5 — limitations and what changes for analysis.)* We state the bound plainly: BandGlyph is
> designed for spread-trend reading and, as our results show, does **not** beat the spaghetti plot
> for tracing a single named member — we recommend the interaction for that subtask rather than the
> glyph. The payoff for practice is concrete: forecasters can read the growth of uncertainty at a
> glance where they previously integrated it by eye. Section 2 positions the work; Section 3 gives
> the encoding and its task rationale; Sections 4-6 the system and the study; limitations are
> discussed alongside the results, not deferred. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the VIS bar

Mapped to the skill checklists:

- **Visualization contribution on the first page** — the abstract and ¶1 pose a data-and-task problem
  and an encoding question before any system detail (`vis-writing-style`: "lead with the
  visualization contribution").
- **Every encoding justified by task** — spread is mapped to position/length *because* the task is
  ordered magnitude comparison, stated explicitly, not chosen for looks (`vis-writing-style`: the
  design-rationale discipline).
- **Evaluation matched to the contribution type** — the claim is perceptual, so the evidence is a
  preregistered controlled study with effect sizes and CIs, not "users liked it" (`vis-experiments`:
  match evidence to the contribution type).
- **Right venue, remove-the-visualization test passes** — delete the encoding-and-task core and no
  paper remains, so it is a VIS contribution, not a CHI interaction study or a rendering result
  (`vis-topic-selection`).
- **Open materials by default** — stimuli, anonymized responses, the analysis notebook, and a video
  are in the supplement, matching VIS's Open Practices and double-blind expectations
  (`vis-reproducibility`, `vis-supplementary`).
- **Honest limitation** — the one task where the baseline wins is stated up front, pre-empting the
  reviewer's over-claiming objection (`vis-writing-style`: report limitations honestly).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified IEEE VIS /
> TVCG papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for VIS-specific submission policy and the
> journal-integrated two-phase cycle.
