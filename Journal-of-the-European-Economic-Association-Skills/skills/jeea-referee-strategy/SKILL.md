---
name: jeea-referee-strategy
description: Use when anticipating referee and co-editor objections for a Journal of the European Economic Association (JEEA) manuscript, or calibrating desk-reject risk and timeline expectations. Plans the defense and expectations; it does not draft the response letter (use jeea-rebuttal after a decision).
---

# Referee Strategy (jeea-referee-strategy)

## When to trigger

- Before submission, to stress-test the paper against the objections it will draw
- You want to gauge desk-reject risk and the realistic timeline
- A co-author asks "what will the referees attack?"
- You need to decide what to pre-empt in the paper vs. leave for the response

## The JEEA review reality (source map refreshed 2026-06-20)

JEEA review is **single-blind**: referees know the authors. Every submission is first read by a **co-editor**, who may **desk-reject without peer review** if the fit or contribution is not strong enough for a general-interest journal; otherwise it goes to referees. The editorial team aims for a **fast decision (≈8 weeks where possible)**. Because the co-editor is a general-interest gatekeeper (not necessarily a subfield specialist), the **first hurdle is general-interest fit and a legible contribution**, not subfield depth. Re-verify volatile process facts on the EEA / OUP pages.

## The objections to pre-empt (by source)

| Objection | Pre-emption in the paper |
|-----------|--------------------------|
| "Not general interest enough" (desk-reject risk) | `jeea-topic-selection` + `jeea-literature-positioning`: a lesson that travels, stated up front |
| "Contribution is incremental vs. [close paper]" | name the delta vs. the frontier; defend it (`jeea-literature-positioning`) |
| "Identification is not credible" | design-based defense / sensitivity (`jeea-identification`, `jeea-robustness`) |
| "The model is a special case" | generalize or justify the special case (`jeea-theory-model`) |
| "Results look fragile" | threat-organized robustness (`jeea-robustness`) |
| "Inference is mis-specified" | clustering / wild-cluster / RI (`jeea-robustness`) |
| "Cannot tell if it replicates" | DCAS package ready for the Data Editor (`jeea-replication-package`) |

## Strategy moves

- **Win the co-editor first.** The abstract and intro must make the general-interest contribution unmissable, or the paper never reaches referees.
- **Pre-empt the top three objections in the paper**, not in a hoped-for response letter — anticipate, don't defer.
- **Single-blind means be careful with self-citation and tone** — referees see who you are; avoid territorial framing against close authors who may referee.
- **Pick the right co-editor fit mentally:** match the paper to the breadth of a general-interest editor; if it only makes sense to a specialist, the framing is wrong.
- **Calibrate timeline and outcomes:** a fast first decision is the norm; plan for R&R, not instant acceptance.

## Checklist

- [ ] General-interest contribution unmissable in abstract + intro (beats desk-reject)
- [ ] Top three likely objections identified and pre-empted in the paper
- [ ] Closest competing papers acknowledged fairly (single-blind: tone matters)
- [ ] Identification / robustness / replication defenses in place before submission
- [ ] Realistic timeline and outcome expectations set (fast decision; expect R&R)

## Two-gate model of a JEEA decision

Think of the decision as two gates, and target the defense at the right one:

1. **The co-editor gate (general interest + fit).** Cleared by `jeea-topic-selection`, `jeea-literature-positioning`, and `jeea-writing-style`: a legible, traveling contribution stated in the abstract and intro. Most desk rejections die here, before any referee reads the paper.
2. **The referee gate (execution).** Cleared by `jeea-identification`, `jeea-theory-model`, `jeea-robustness`, and `jeea-replication-package`: a credible design or disciplined model, robust results, and a verifiable replication path.

A paper strong at gate 2 but weak at gate 1 is desk-rejected; a paper strong at gate 1 but weak at gate 2 draws a hostile referee report. Diagnose which gate is at risk and route accordingly.

## Worked vignette (illustrative)

A user has a clean RDD with a tiny, technical question. The execution is excellent (gate 2 is safe) but the general-interest hook is missing (gate 1 is at risk). The strategy is not more robustness — it is reframing the question so the discontinuity answers something a general reader cares about. Route to `jeea-topic-selection` and `jeea-writing-style` before submission, not to another robustness table.

## Anti-patterns

- Submitting a subfield-deep paper with no general-interest hook (desk-reject bait)
- Leaving the obvious identification or robustness objection for the response letter
- Territorial or dismissive framing of close authors (who may referee, under single-blind)
- Assuming referees will supply the general-interest lesson you never stated
- Treating a fast-decision target as a promise of acceptance
- Pouring effort into gate 2 when gate 1 (general-interest fit) is the actual risk

## Output format

```
【Desk-reject risk】[low / medium / high] + the general-interest hook
【Top 3 referee objections】[...]
【Pre-emption status】[in-paper / deferred] for each
【Single-blind cautions】[self-citation / tone]
【Timeline/outcome】[fast decision; expect R&R]
【Next step】jeea-submission
```
