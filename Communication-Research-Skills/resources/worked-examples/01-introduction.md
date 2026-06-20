> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate *Communication Research* (CR) house style. No real-paper facts are stated,
> and no policy is invented here — for venue rules see
> [`../official-source-map.md`](../official-source-map.md). Corresponding skills:
> [`../../skills/commres-writing-style/SKILL.md`](../../skills/commres-writing-style/SKILL.md),
> [`../../skills/commres-topic-selection/SKILL.md`](../../skills/commres-topic-selection/SKILL.md), and
> [`../../skills/commres-theory-building/SKILL.md`](../../skills/commres-theory-building/SKILL.md).

# Worked Example: A Communication-Research-Style Introduction (before → after)

CR is SAGE's **quantitative, social-scientific** communication journal. The introduction is judged not
by platform novelty but by whether it builds — from theory and prior findings — to **explicit,
numbered hypotheses** that test a **communication mechanism** with valid measurement. This example
demonstrates that arc from this pack's skills:

**communication question → why prior work leaves it open → construct & mechanism → numbered
hypotheses → design that tests them → headline finding with effect size → tested mechanism →
boundary condition** — with the CR rules that the **contribution is front-loaded**, the intro reaches
**numbered hypotheses**, prose is **argument-first**, and results are reported in **APA** with effect
sizes (`commres-writing-style`). The bar is a **tested mechanism**, not a bare effect
(`commres-topic-selection`, `commres-theory-building`).

**Illustrative paper (fictional):** *"Corrective Cues: How Visible Peer Fact-Checking Shapes Onward
Sharing of Misinformation."* Fictional setting: a preregistered online message experiment with a
validated correction-detection measure.

---

## Before (descriptive draft — no mechanism, no hypotheses)

> Misinformation on social media has been studied extensively. In this paper we focus on peer
> fact-checking on Platform X. We ran an experiment and also collected a large dataset of posts, which
> we analyzed using a fine-tuned transformer classifier to detect corrections. We find that corrections
> are associated with changes in sharing (p < .05). Misinformation is an important problem for society.
> Section 2 reviews the literature, Section 3 describes our procedure, Section 4 reports the results.

**What's wrong (against `commres-writing-style`, `commres-topic-selection`, `commres-theory-building`):**

- **Platform-bound and method-led.** It leads with "Platform X" and a classifier before stating any
  communication question — a `commres-topic-selection` anti-pattern.
- **No mechanism, no hypotheses.** "Associated with changes in sharing (p < .05)" is a bare effect with
  a significance star; CR requires a **mediator/moderator** and **numbered hypotheses**, with results in
  effect-size terms.
- **No measurement warrant.** The automated measure is asserted, not validated against human coding.
- **Throat-clearing and an over-signposted roadmap** that spend scarce words against the 45-page limit.

---

## After (CR arc — builds to hypotheses, tests a mechanism, reports effect sizes)

> **When ordinary users publicly correct a misleading post, does the correction reduce onward sharing of
> the false claim — and through what communication process?** Most evidence treats fact-checking as a
> message aimed at the *misinformed individual*, leaving open whether its real work is
> **audience-directed and normative**: telling onlookers that sharing the claim risks social disapproval.
> *(communication question + the open issue in prior work, in the first breath.)*
>
> We define a **corrective cue** as a publicly visible, peer-authored signal that a claim is contested,
> and theorize its mechanism as **perceived injunctive-norm activation** — distinct from belief change in
> the original poster. This yields three predictions. **H1:** visible corrections reduce onward sharing
> relative to identical uncorrected posts. **H2:** the effect is mediated by perceived injunctive norms
> about sharing, not by belief change. **H3:** the effect is stronger among bystanders who did not engage
> with the original post. *(construct defined and distinguished from a neighbor; mechanism stated as a
> mediator; boundary stated as a moderator — the `commres-theory-building` core, built into numbered
> hypotheses.)*
>
> We test these in a **preregistered** online experiment (N = 1,200) that randomizes correction
> *visibility* while holding the post and the correction text constant, with **validated multi-item
> measures** of injunctive norms (α = .89) and belief, and an automated correction-detection check
> **validated against a human-coded gold standard** (Krippendorff's α = .84). The visible-vs-hidden
> contrast adjudicates the two accounts: if corrections worked through belief, hidden and visible
> corrections would move sharing equally; if through norms, only *visible* ones would.
> *(design in one paragraph; the `commres-research-design` adjudication test stated plainly; measurement
> validated, not assumed.)*
>
> Visible corrections cut onward-sharing intention relative to identical uncorrected posts (illustrative
> *d* = 0.43, 95% CI [0.31, 0.55]), while otherwise-identical hidden corrections did not (*d* = 0.05,
> 95% CI [−0.07, 0.17]); a bootstrap mediation test showed the effect ran through perceived injunctive
> norms, not belief change (illustrative indirect effect *ab* = −0.18, 95% CI [−0.27, −0.10]), and was
> largest among non-engaging bystanders (H3 supported). *(headline finding with effect sizes and CIs in
> APA; the rival is ruled out via the mediation pattern — `commres-data-analysis`.)*
>
> Our contribution is to reframe peer fact-checking as **audience-directed normative communication**
> rather than source-directed belief correction, bounded to settings with visible corrections and
> legible sharing norms. *(tested mechanism + boundary condition; portability without overclaiming.)*

---

## A CR-style abstract for the same paper (`commres-writing-style`)

> Does visible peer fact-checking reduce the spread of misinformation, and through what process? We
> argue that publicly visible, peer-authored corrections — **corrective cues** — reduce onward sharing
> not by changing the misinformed source's beliefs but by activating perceived injunctive norms among
> bystanders. A preregistered online experiment (N = 1,200) randomized correction *visibility* with
> validated measures of injunctive norms (α = .89) and a human-validated correction-detection check
> (Krippendorff's α = .84). Visible corrections reduced onward-sharing intention (d = 0.43) while
> otherwise-identical hidden corrections did not (d = 0.05); a bootstrap mediation test showed the
> effect operated through injunctive norms (ab = −0.18, 95% CI [−0.27, −0.10]) and concentrated among
> non-engaging bystanders. We reframe peer fact-checking as audience-directed normative communication,
> bounded to settings with visible corrections and legible sharing norms.

---

## Why the "after" meets the CR bar

Mapped to the skill checklists:

- **Builds to numbered hypotheses; reads as cumulative social science** — H1–H3 follow from the theory,
  and the Results test them in order (`commres-writing-style`, `commres-theory-building`).
- **Tested mechanism, not a bare effect** — the mediator (injunctive norms) and moderator (bystander
  engagement) are pre-specified and tested, distinguishing the norm account from belief change
  (`commres-theory-building` mechanism core; `commres-research-design` adjudication test).
- **Valid measurement** — multi-item scales with reliability, and the automated measure **validated
  against human coding**, not trusted as ground truth (`commres-research-design`,
  `commres-transparency-and-data`).
- **APA reporting** — effect sizes (*d*) with confidence intervals and a bootstrap indirect effect, not
  significance stars alone (`commres-data-analysis`, `commres-tables-figures`).
- **Preregistration noted; theory before tests** — avoids HARKing, and preregistration is the kind of
  thing to flag in the cover letter (`commres-theory-building`, `commres-transparency-and-data`).
- **Format-disciplined** — no throat-clearing or literature dump, respecting the 45-page limit
  (`commres-writing-style`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified**
> *Communication Research* papers whose intros execute a version of this arc, and
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
> plus the [`../code/`](../code/) skeleton for stress-testing and estimating the design referenced above.
