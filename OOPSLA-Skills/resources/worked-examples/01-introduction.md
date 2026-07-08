# Worked Example: Reframing an Introduction for OOPSLA (before → after)

> **Fictional throughout.** The system, language feature, measurements, and citations in this
> example are invented to teach a rewrite pattern; none may be quoted as fact. Venue policy
> comes from [`../official-source-map.md`](../official-source-map.md), and the craft rules
> exercised here live in [`oopsla-writing-style`](../../skills/oopsla-writing-style/SKILL.md),
> [`oopsla-topic-selection`](../../skills/oopsla-topic-selection/SKILL.md), and
> [`oopsla-experiments`](../../skills/oopsla-experiments/SKILL.md).

**Scenario.** A team built *Gradia*, a (fictional) gradual ownership checker retrofitted onto
an existing scripting language, and drafted the paper for a general software-engineering
audience. They now want to submit to an OOPSLA round. The draft's introduction reads like a
tool advertisement; OOPSLA reviewers will read it asking *what is the language-design or
semantic insight, what mechanism produces the benefit, and would the evidence survive the
SIGPLAN empirical checklist?*

---

## Before

> Memory bugs cost the industry billions of dollars every year. Many tools have been
> proposed, but developers still struggle in practice. We present Gradia, a novel and
> practical tool that brings the benefits of ownership types to dynamic languages. Gradia is
> easy to adopt: developers annotate only the code they care about. We evaluated Gradia on
> several real-world projects and found that it detects many bugs with low overhead and that
> developers find it useful. Our contributions are: (1) the Gradia tool; (2) an evaluation
> on real-world projects; (3) lessons for practitioners.

### Diagnosis against the OOPSLA bar

| Symptom in the draft | Why it fails at OOPSLA | Fixing skill |
| --- | --- | --- |
| "Novel and practical tool" leads; no principle stated | OOPSLA wants the design insight *before* the artifact; a tool is evidence, not thesis | `oopsla-writing-style` |
| "Brings ownership to dynamic languages" with no semantics question | The interesting problem — what ownership *means* when only part of the heap is annotated — is never posed | `oopsla-topic-selection` |
| "Detects many bugs with low overhead" | Unquantified claims invite the empirical-guidelines checklist to fail: no baseline, no workload rationale, no variance | `oopsla-experiments` |
| "Developers find it useful" | A human claim with no study design behind it is a liability, not a bonus | `oopsla-experiments` |
| Contribution list restates the sections | Contributions must be falsifiable statements a reviewer can test against the paper | `oopsla-writing-style` |
| No word about artifact or data availability | The submission must carry a Data-Availability Statement; the intro should set up what will be reproducible | `oopsla-reproducibility` |

---

## After

> Ownership type systems prevent aliasing bugs, but they assume the whole program is typed.
> When annotations are partial — the only realistic assumption for an existing codebase — the
> guarantee's meaning is unsettled: what may checked code conclude about a reference that
> crossed the unannotated boundary? We answer with a *boundary-provenance* semantics: each
> value entering annotated code carries the obligation history of its crossing, and blame for
> a violation falls on the earliest crossing that discharged an obligation unsoundly. This is
> a design choice with teeth — we prove it is the weakest semantics that preserves
> per-module ownership soundness (Theorem 3.4), and we show two published alternatives
> silently forfeit that property (§3.5).
>
> We realize the semantics in Gradia, a checker for an existing dynamic language, and
> evaluate the design rather than the branding: across a 21-project corpus selected by
> stratified dependency rank (§5.1), provenance tracking prices the guarantee at a geometric
> mean of 4.1% runtime overhead (95% CI reported per project, 30 runs after warmup), and a
> 12-participant annotation study measures where partial annotations stop paying for
> themselves. All corpora, scripts, and the study protocol are in the artifact accompanying
> this paper (Data-Availability Statement, p. 23).
>
> **Contributions.** (1) A provenance semantics for partially-annotated ownership, with a
> minimality theorem; (2) a blame-assignment mechanism implementable by call-site rewriting
> alone; (3) an evaluation designed around the SIGPLAN empirical guidelines that separates
> the semantics' cost from the implementation's.

### Why the rewrite lands

- **A question, then a stance.** The first paragraph poses a semantic question a reviewer
  can care about independently of the tool, then commits to an answer and names its cost.
  The artifact appears only as the vehicle.
- **Falsifiable claims.** Minimality theorem, comparison to named alternatives, quantified
  overhead with stated measurement discipline, and a scoped human study — each contribution
  can be checked, which is what the two-round review model does with revision demands.
- **Evidence anticipates the checklist.** Corpus selection rationale, warmup, repetition,
  and confidence intervals are declared in the introduction, signaling the evaluation was
  *designed*, not salvaged (`oopsla-experiments`).
- **Reproducibility is plumbed through.** The Data-Availability Statement is referenced from
  page one, so the artifact-evaluation story (`oopsla-artifact-evaluation`) starts at
  submission time, not after acceptance.

## Transfer checklist

When applying this pattern to a real draft, verify in order:

1. Can the core insight be stated without the system's name in the sentence?
2. Does some claim have a shape a reviewer could refute — a theorem, a measured bound, a
   study result?
3. Is every evaluative adjective ("practical," "low," "useful") replaced by a number, a
   comparison, or deleted?
4. Would the introduction still justify the paper if a competing tool shipped tomorrow?
   (If not, the contribution was the tool, and the routing question reopens —
   `oopsla-topic-selection`.)
