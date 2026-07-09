> **Illustrative teaching example.** The paper, dataset, system, and every number below are
> **fictional** and exist only to demonstrate FAccT house style. No real-paper facts, systems, or
> results are stated, and no policy is invented. Corresponding skills:
> [`facct-writing-style`](../../skills/facct-writing-style/SKILL.md),
> [`facct-topic-selection`](../../skills/facct-topic-selection/SKILL.md), and
> [`facct-experiments`](../../skills/facct-experiments/SKILL.md).

# Worked Example: A FAccT-Style Abstract + Introduction (before → after)

This demonstrates the **FAccT first-page arc** from `facct-writing-style`:
**sociotechnical problem → who is affected → why the current state is inadequate → contribution
(method/audit/framework/critique/study) → disaggregated evidence on real people → what changes and
what harms remain** — with the FAccT expectations that fairness/accountability/transparency is the
**first-class contribution**, evidence is **proportional to the claim and disaggregated**, and the
work is legible to a **mixed CS + law + social-science panel** with limitations and adverse impacts
visible from the start.

The framing also reflects `facct-topic-selection`: FAccT is strongest when the contribution *is* the
fairness/accountability/transparency question — here, whether an automated benefits-screening tool
denies people recourse — rather than a modeling result whose equity angle is incidental (which would
route to a pure-ML venue), and when the work survives the **delete-the-equity** and **mixed-reviewer**
tests.

**Illustrative paper (fictional):** *"Denied Without Recourse: An Audit and Contestability Analysis
of an Automated Benefits-Eligibility System."* Fictional artifact: a disaggregated audit of a
deployed eligibility model plus interviews with denied claimants and a contestability mechanism.

---

## Before (buries the FAccT contribution — typical first-draft abstract + intro)

> **Abstract.** Machine learning is increasingly used in public services. We build a model that
> predicts benefits eligibility using a state-of-the-art gradient-boosted classifier and a novel
> feature pipeline. Our approach achieves high accuracy on a large administrative dataset and
> outperforms baselines, showing the promise of AI for efficient public administration. We also
> discuss some fairness considerations.
>
> **Introduction.** Public benefits administration is expensive and slow. Many agencies now use
> automated tools to decide eligibility. In this paper we train an accurate model on a large dataset
> and evaluate it, showing strong results. We briefly note that fairness and ethics are important.
> Section 2 covers related work, Section 3 our model, Section 4 experiments, Section 5 ethics, and
> Section 6 concludes.

**What's wrong (against `facct-writing-style` / `facct-topic-selection` / `facct-experiments`):**

- **No fairness/accountability/transparency contribution on the first page** — it leads with an
  accuracy win for the *agency*, not with the people who are wrongly denied. FAccT wants the harm and
  accountability question up front.
- **Wrong claim shape.** Aggregate accuracy says nothing about *who is denied in error* or whether
  they can contest it — the actual FAccT outcomes. No disaggregation, no recourse.
- **Fails the delete-the-equity test.** Remove the two "fairness/ethics" sentences and a complete
  (ML) paper remains — the `facct-topic-selection` signal that this is a pure-ML paper wearing a
  FAccT title.
- **Ethics is a Section 5 afterthought**, and there is no adverse-impacts reflection, no consent
  story, and nothing a legal or qualitative reviewer can hold.
- **Single-discipline framing** — a mixed FAccT panel has nothing for the lawyer or the social
  scientist to evaluate.
- **Over-signposted roadmap** substituting for an argument.

---

## After (FAccT arc — problem → who is affected → inadequacy → contribution → disaggregated evidence → harms)

> **Abstract.** Automated eligibility systems now decide access to public benefits for millions, but
> a wrongful denial can cut off food or housing with no clear way to appeal. We ask not "how accurate
> is the model?" but **"who is wrongly denied, and can they contest the decision?"** We audit a
> deployed benefits-screening model on **210,000 administrative case records** and find its error
> concentrates on a protected subgroup — false-denial rates for that group are markedly higher than
> the population rate (reported with confidence intervals and validated group proxies; §4). Through
> **34 interviews with denied claimants** we show that the existing appeal path is effectively
> inaccessible to the people most affected (coded themes and protocol in the supplementary). Building
> on both, we present a **contestability mechanism** that surfaces the decisive factors and a
> claimant-initiated recourse route, and we discuss what it does and does not fix. *(problem → who is
> affected → inadequacy → audit finding → lived experience → mechanism → residual harm — all on the
> first page.)*
>
> **Introduction.** *(¶1 — the sociotechnical problem and who bears it, first breath.)* For a family
> waiting on benefits, an automated denial is not a metric — it is a month without rent. As agencies
> delegate eligibility to models, the engineering question is no longer "can the model predict
> eligibility?" but **"who does it wrongly deny, and what can they do about it?"**
>
> *(¶2 — why the current state is inadequate, across disciplines.)* Prior work reports aggregate
> accuracy or a single fairness metric, but **aggregate accuracy hides subgroup harm**, and a
> fairness number says nothing about **accountability** — whether a denied person can understand or
> challenge the decision, a due-process concern the legal literature treats as central. No prior
> study connects *who is wrongly denied* to *whether they can contest it* for a deployed system.
>
> *(¶3 — contribution, stated as FAccT claims.)* We make three contributions. First, a **disaggregated
> audit** of a deployed eligibility model showing error concentrated on a protected subgroup. Second,
> an **interview study** of denied claimants showing the appeal path is inaccessible to them in
> practice. Third, a **contestability mechanism** grounded in both, evaluated for whether it restores
> a usable route to recourse.
>
> *(¶4 — disaggregated evidence on real people, each claim paired.)* We tie every claim to evidence:
> false-denial rates are reported **by subgroup and intersection** with bootstrap confidence
> intervals and a validated proxy for group membership (Table 1); the appeal-access findings come
> from interviews coded with a documented scheme and inter-coder agreement (§5); and the mechanism is
> assessed on held-out cases and with claimant feedback (Table 3). Analysis code, the datasheet, the
> interview protocol, and the codebook are in the anonymized supplementary material.
>
> *(¶5 — limitations, adverse impacts, and what changes.)* We state the central threat plainly: our
> group proxy is inferred and carries error we quantify and bound, and an audit like ours could be
> misread as endorsing the system if the recourse gap is ignored — an adverse impact we address in the
> endmatter. The payoff is concrete: agencies can see *who* their system fails and give those people a
> real way to contest it. Section 2 details the audit; Section 3 the interviews; Section 4 the
> mechanism; limitations are argued alongside each result, not deferred. *(brief roadmap, no
> over-signposting.)*

---

## Why the "after" meets the FAccT bar

Mapped to the skill checklists:

- **FAccT contribution on the first page** — the abstract and ¶1 pose a harm-and-accountability
  question about affected people before any model detail (`facct-writing-style`: "lead with the FAccT
  contribution").
- **Evidence proportional to the claim, and disaggregated** — the claim is about *who is wrongly
  denied and whether they can appeal*, so the evidence is per-subgroup error rates with intervals
  plus interviews with the affected, not aggregate accuracy (`facct-experiments`: match the evidence
  to the claim shape; disaggregate).
- **Passes the delete-the-equity and mixed-reviewer tests** — remove the fairness/accountability
  framing and nothing survives; and a CS reviewer (the audit), a legal reviewer (due-process
  recourse), and a qualitative reviewer (the interviews) each have something to evaluate
  (`facct-topic-selection`).
- **Limitations and adverse impacts engaged where they live** — proxy validity is quantified in ¶4-5
  and the misuse risk is named and pushed to the Adverse Impacts endmatter, not quarantined in a
  closing paragraph (`facct-writing-style`; `facct-supplementary`).
- **Accountability documentation and honest release** — analysis code, a datasheet, the protocol, and
  the codebook are in an anonymized artifact, matching FAccT's transparency norms and mutual anonymity
  (`facct-reproducibility`, `facct-artifact-evaluation`).
- **Consent and care for participants** — the interview protocol and coding are documented and the
  ethics basis feeds the endmatter statements (`facct-experiments`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified FAccT/FAT\***
> papers whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for FAccT-specific submission policy and the
> Accept/Revise/Reject cycle.
