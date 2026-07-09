> **Illustrative teaching example.** The paper, method, setting, and every number below
> are **fictional** and exist only to demonstrate WACV house style. No real-paper facts,
> datasets, or results are stated, and no policy is invented. Corresponding skills:
> [`wacv-writing-style`](../../skills/wacv-writing-style/SKILL.md),
> [`wacv-topic-selection`](../../skills/wacv-topic-selection/SKILL.md), and
> [`wacv-experiments`](../../skills/wacv-experiments/SKILL.md).

# Worked Example: A WACV Applications-Track First Page (before → after)

This demonstrates the **WACV first-page arc** for an **Applications-track** paper:
**real-world constraint → why existing methods break under it → the system/method →
comparative evidence under that constraint → why it belongs at an applications venue** —
written so a **Round 1** reviewer can decide *Accept* rather than *Revise and Resubmit*.
The two-round model rewards a first page that pre-empts the obvious revision request: if
the reviewer's first question ("does this hold under the deployment constraint you claim?")
is already answered on page one, the paper skips the Round 2 lap.

**Illustrative paper (fictional):** *"Low-Light Crop-Row Segmentation for Battery-Powered
Field Robots."* Fictional system: a segmentation model that must run under 2 W on a
microcontroller-class device in pre-dawn field light.

---

## Before (leads with the model, hides the constraint)

> **Abstract.** Semantic segmentation is a fundamental problem in computer vision. We
> propose a new lightweight network that combines an efficient backbone with a novel
> attention module and achieves strong results on an agricultural dataset, outperforming
> prior methods. Our approach is fast and accurate.
>
> **Introduction.** Segmentation has been widely studied, with many architectures proposed.
> Applying it to agriculture is important for automation. In this paper we design a compact
> model and evaluate it on crop images, showing it works well. Section 2 covers related
> work, Section 3 the method, Section 4 experiments.

**What's wrong (against `wacv-writing-style` / `wacv-topic-selection` / `wacv-experiments`):**

- **No real-world constraint on the first page** — "fast and accurate" is not the 2 W,
  pre-dawn, microcontroller reality that makes this an *applications* contribution.
- **Wrong track framing** — pitched as a generic "novel attention module" (an
  Algorithms-track claim) while the actual value is deployment under constraint; a reviewer
  routes it to the wrong lens and asks for a revision.
- **No comparative assessment under the constraint** — "outperforming prior methods" with
  no power budget, no on-device latency, no low-light robustness numbers, no variance.
- **Invites a Revise-and-Resubmit** — the reviewer's first question (does it hold at 2 W in
  the dark?) is unanswered, which is exactly the gap that sends a paper to Round 2.

---

## After (WACV applications arc — constraint → gap → system → comparative evidence → fit)

> **Abstract.** Field robots that weed autonomously must segment crop rows **before
> sunrise, on battery, under a 2 W compute budget** — a regime where accurate segmentation
> networks are too heavy and efficient ones lose the low-contrast row boundaries that
> matter. We present a crop-row segmentation system that holds boundary accuracy at **2 W
> on a microcontroller-class device in sub-10-lux light**, by pairing a constraint-aware
> backbone with a low-light contrast-normalization front end trained on paired dawn/day
> captures. Against three efficient-segmentation baselines re-tuned to the same 2 W budget,
> our system keeps boundary F1 within a small margin of a 15 W model while the baselines
> degrade sharply below 20 lux; we report on-device latency, wattage, and boundary F1 with
> standard deviations over 5 field sessions and 3 seeds. *(constraint → gap → system →
> comparative evidence under the constraint → all on the first page.)*
>
> **Introduction.** *(¶1 — the deployment constraint, first breath.)* A battery-powered
> weeding robot has a few pre-dawn hours and a **2 W compute envelope**; segmentation that
> assumes a GPU or daylight is not an option. The applications question is not "can we
> segment crop rows" but "can we segment them **within this envelope, in this light**."
>
> *(¶2 — gap: why existing methods break under the constraint, each named.)* Heavy
> segmentation networks exceed the power budget outright. Efficient networks fit the budget
> but were tuned on **daylight** benchmarks and lose low-contrast row boundaries below ~20
> lux. Generic low-light enhancement adds latency the 2 W budget cannot spare and is tuned
> for human-visible quality, not boundary preservation. *(each prior line gets a specific
> failure under the stated constraint, not a vague "prior work is limited.")*
>
> *(¶3 — the system + the honest scope.)* Our front end normalizes contrast using paired
> dawn/day captures so boundaries survive, and the backbone is searched **under the 2 W
> constraint** rather than shrunk after the fact. We claim the result for **row-crop
> segmentation at dawn on microcontroller-class hardware**; we do not claim a general
> low-light or general-segmentation win. *(scope stated plainly, per WACV's applications
> bar that the claim match the demonstrated domain.)*
>
> *(¶4 — comparative evidence, matched to the constraint.)* We compare against three
> efficient baselines **re-tuned to the same 2 W budget and the same low-light data**, not
> to their daylight defaults, and against a 15 W reference as an upper bound. We report
> boundary F1, on-device latency, and measured wattage, each with standard deviations over
> 5 field sessions and 3 seeds; the power meter and device are named in Section 4.
> *(comparative assessment under the real constraint, with uncertainty — the
> applications-track review criterion.)*
>
> *(¶5 — why it is a WACV applications paper + roadmap.)* The contribution is a segmentation
> system that **survives a named deployment envelope**, evaluated as it would be deployed —
> the applications-first question WACV exists to review. Section 2 states the constraint and
> baselines; Section 3 the system; Section 4 the field evaluation. *(brief roadmap, no
> over-signposting.)*

---

## Why the "after" meets the WACV bar

Mapped to the skill checklists:

- **Constraint on the first page** — the 2 W, sub-10-lux, microcontroller envelope leads
  the abstract and ¶1 (`wacv-writing-style`: put the real-world constraint, not the module,
  first).
- **Right track** — framed as an **Applications-track** systems contribution with
  comparative assessment, so it is reviewed under the lens that fits it, not the algorithmic
  novelty lens (`wacv-topic-selection` track test).
- **Comparative assessment under the constraint** — baselines re-tuned to the *same* budget
  and light, plus an upper-bound reference (`wacv-experiments`: matched-condition fairness).
- **No overclaiming** — scope limited to dawn row-crop segmentation on named hardware, with
  standard deviations over field sessions and seeds, not "fast and accurate."
- **Pre-empts the Round 2 lap** — the reviewer's first revision question is answered on page
  one, which under WACV's two-round model is the difference between *Accept* and *Revise and
  Resubmit* (`wacv-review-process`, `wacv-author-response`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, verified WACV
> papers**, and [`../official-source-map.md`](../official-source-map.md) for the two-round
> model and WACV-specific submission policy.
