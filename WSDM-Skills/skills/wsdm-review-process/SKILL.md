---
name: wsdm-review-process
description: Use when reasoning about how WSDM reviews and decides papers - the hybrid single/double-blind architecture with Associate-Chair metadata visibility, at-least-three PC reviews plus senior PC assessment, the absence of a rebuttal phase, the August-to-October window, and what ~17% selectivity at a single-track venue implies.
---

# WSDM Review Process

Model the machinery that turns an August submission into an October decision.
Understanding it changes writing decisions months earlier, because WSDM's
process has two properties that most neighboring venues lack: authors never get
to reply, and the venue's blinding design is unusually explicit about who sees
what. Process details are re-set by each edition's chairs - the 2026-cycle
anchors below are for calibration, not prediction.

## The pipeline

```text
Aug 7   abstract registered      -> bidding/assignment signal for the PC
Aug 14  full paper (AoE)         -> desk screening (format, scope, anonymity,
                                     ethics section present)
Aug-Oct at least 3 PC reviews    -> written independently; no author contact
        + senior PC (SPC)        -> meta-assessment, consensus-building
        Associate Chairs         -> see metadata incl. authorship, manage COI
Oct 23  notification (2026 anchor)
        camera-ready + ACM production (dates 待核实 per edition)
Feb     single-track conference
```

Roughly ten weeks from paper to decision - among the fastest of the major
mining venues, which is precisely why there is no room for a rebuttal round.

## Who sees what: the hybrid-blind design

The 2025 and 2026 CFPs describe "a combination of single-blind reviewing and
double-blind reviewing": reviewers and SPCs get anonymized PDFs; Associate
Chairs see submission metadata, including authorship, to detect undisclosed
conflicts. Implications for authors:

- Your scientific evaluators judge the anonymized artifact only. All the
  self-containment and anonymization discipline of `wsdm-submission` exists for
  their benefit.
- The metadata layer is an integrity mechanism, not a reputational one - it does
  not transmit prestige to the people scoring you.
- This design is historically literate: WSDM 2017 hosted the controlled
  experiment (Tomkins, Zhang & Heavlin, published in PNAS 2017) in which
  single-blind reviewers bid more on and rated more favorably the papers of
  famous authors and top institutions. The venue then engineered a process
  that keeps scoring blind while still policing conflicts. Expect chairs to
  take anonymity breaches personally; the policy is theirs by conviction.

## Reading the reviewer pool

WSDM's PC blends academic IR/mining researchers with industry scientists from
search, recommendation, and ads groups - the conference was founded as, and
markets itself as, the venue where "practical yet principled" work lives.
Consequences:

| Reader | What convinces them | What loses them |
|---|---|---|
| Academic IR/mining reviewer | Clean formalization, bias-aware offline evaluation, strong recent baselines | Undefined novelty over last year's WSDM/SIGIR papers |
| Industry reviewer | Data realism, latency/cost awareness, deployment plausibility | Toy datasets presented as web-scale; ignoring serving constraints |
| SPC (writes the meta-review) | Consistency across claims, evidence, limitations | One overclaimed sentence that a reviewer flags and the paper never defends |

Write for the intersection: every headline claim should survive both the
"is it sound?" and the "would it survive contact with a platform?" reads.

## No rebuttal: decision dynamics

With no author input after submission, disagreement resolution happens between
reviewers and the SPC. Practical consequences:

- A single confident negative review carries more terminal weight than at
  rebuttal venues, because you cannot dilute it with a reply. The counter is
  preemptive: the objection-inventory method in `wsdm-author-response`.
- Borderline papers live or die on the SPC's reading of whether weaknesses are
  fixable presentation issues or structural flaws. Make fixability visible:
  explicit limitation paragraphs signal self-awareness and give the SPC
  language to defend the paper.
- Reviews arrive as feedback for the *next* venue. Their consensus items are
  the revision contract; their misreadings are your ambiguity bugs.

## Decoding review language after notification

Because no dialogue ever occurred, WSDM reviews compress judgments into stock
phrases. A translation layer for triage (heuristics, not officialdom):

- "The evaluation does not control for..." - a validity-quadrant hit; at this
  venue this is usually the decisive sentence in the packet.
- "The contribution is incremental over [WSDM/SIGIR paper]" - a lineage
  positioning failure more often than a novelty failure; check whether your
  contrast sentence for that exact paper existed (`wsdm-related-work`).
- "Unclear whether this would work in practice" - the industry read rejected
  the setting's realism; the fix is data-regime honesty, not more benchmarks.
- "Well written but I am not convinced of the significance" - the
  choose-this-paper test failed; the work may be short-track shaped.
- Three lukewarm-positive reviews and a rejection - normal at one-in-six
  selectivity with fixed program capacity; read the SPC's meta-review for the
  actual ranking rationale before blaming any reviewer.

## Selectivity arithmetic

2025 anchor: more than 600 submissions, just over 100 acceptances (~16-17%).
Single-track scheduling caps how many talks the program can hold, so acceptance
volume does not stretch with submission growth the way multi-track venues
absorb it. Strategic readings:

- "Solid but unremarkable" occupies the rejection region: at one-in-six, papers
  need a reason to be *chosen*, not merely no reason to be rejected.
- The short-paper track (new since 2026) is the pressure valve for focused
  contributions that cannot win a long-paper slot on breadth.
- Deadlines are annual: a rejection costs twelve months at this venue, which
  makes the pre-submission adversarial pass cheap by comparison.
- Selectivity plus a compact PC also means repeat encounters: the reviewer
  pool sees your resubmission next year. Papers that visibly absorbed last
  year's reviews start ahead; papers that ignored them start behind zero.

## Output format

```text
[Cycle model] deadlines / notification / process confirmed from current CFP: <list + gaps>
[Blinding] hybrid design implications applied to this paper: <notes>
[Pool coverage] academic read / industry read / SPC read: convinced or at-risk
[Terminal-review risk] strongest single objection with no in-PDF answer: <item>
[Selectivity call] long paper / short paper / different venue, with reason
```
