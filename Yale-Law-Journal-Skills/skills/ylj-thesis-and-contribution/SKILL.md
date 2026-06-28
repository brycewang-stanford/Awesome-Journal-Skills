---
name: ylj-thesis-and-contribution
description: Use when sharpening the central legal-scholarly claim and contribution for a The Yale Law Journal (YLJ) piece. It forces a falsifiable, generalist thesis and names the contribution type; it does not search prior literature (use ylj-preemption-check) or build the argument (use ylj-argument-structure).
---

# Thesis & Contribution (ylj-thesis-and-contribution)

A YLJ piece lives or dies on a **single, sharp claim** that a generalist reader can restate. Student
editors (and faculty advisors they consult) reject pieces whose "thesis" is really a topic or a survey.
This skill nails the claim and labels the contribution; it does not yet prove novelty
(`ylj-preemption-check`) or sequence the argument (`ylj-argument-structure`).

## When to trigger

- You can name the *area* but cannot state the *claim* in one sentence
- A reader asks "so what's the argument?" and you give a paragraph, not a sentence
- The introduction promises several things and the reader cannot tell which is the point
- You are unsure whether the contribution is descriptive, doctrinal, theoretical, or normative

## The one-sentence thesis test

Write: **"This [Article/Essay] argues that ____, and therefore ____."** It must be:

- **Contestable** — a smart reader could disagree; if no one would dispute it, it is not a thesis.
- **Generalist** — legible to a reader outside the subfield (see `ylj-topic-selection`).
- **Load-bearing** — every Part of the piece exists to establish or apply this claim.
- **Yours** — it is the move *you* make, not a restatement of existing scholarship.

If you need "and" three times, you have three theses; pick the one the piece is actually about.

## Name the contribution (most YLJ pieces blend two)

| Type | What it adds | Tell |
|------|--------------|------|
| **Descriptive** | A pattern no one has named (a doctrine is incoherent, a practice is widespread) | "Courts/agencies are actually doing X." |
| **Doctrinal** | A better reading of authority (statute, precedent, constitutional text) | "The correct rule is X, not Y." |
| **Theoretical** | A framework that reorganizes how we understand a field | "X is best understood as Y." |
| **Normative** | A reform: what the law *should* be and who should change it | "Congress/the Court should do X." |
| **Critical** | An immanent critique exposing a hidden assumption | "The standard account rests on an untenable Z." |

State which type(s) you are making — and to **whom** the normative payoff is addressed (court,
Congress, agency, bar), because YLJ readers include all of them.

## Build the YLJ contribution contract

Do not leave the contribution as a label. Convert it into a four-part contract that a student editor
can defend to the Articles & Essays Committee:

| Contract field | Required answer | Failure mode |
|----------------|-----------------|--------------|
| **Claim** | What is the one legal proposition the piece asks the reader to accept? | A topic, survey, or issue-spotter memo |
| **Intervention** | What legal understanding changes if the claim is right? | A restatement of an existing debate |
| **Authority base** | Which doctrine, statute, institutional practice, archive, empirical record, or theory bears the weight? | A thesis that floats above sources |
| **Payoff** | Who should reason or act differently: court, legislature, agency, litigants, scholars, or legal educators? | A "so what" paragraph with no actor |

The contract must be short enough to fit in the first-page roadmap, but strong enough to survive
preemption review. If one field is missing, route back before polishing prose.

## Student-editor screen

YLJ's first screen is by excellent generalist student editors, not specialists already committed to
your subfield. Before moving to `ylj-preemption-check`, test whether the thesis can pass a two-minute
committee pitch:

1. **Hook:** "The legal system currently assumes X, but this piece shows Y."
2. **Why now:** a doctrinal split, institutional change, regulatory moment, social practice, or scholarly blind spot makes the claim timely.
3. **Why YLJ:** the claim travels beyond a narrow specialty and changes how a general legal audience understands the field.
4. **Risk:** the strongest objection is named honestly, not hidden until Part III.

A thesis that only works after ten minutes of background is probably too narrow, too jargon-heavy, or
still a literature review. Use `ylj-writing-style` later, but fix the claim here first.

## Preemption handoff

This skill does not perform the literature search, but it must create a search-ready hypothesis for
`ylj-preemption-check`. Output the following before leaving:

- **Search terms:** the doctrine, statutory phrase, institutional label, and conceptual term that would surface near-preempting work.
- **Closest likely rivals:** at least three article/note/work-in-progress categories that might already make the move.
- **Distinctive move:** the exact sentence explaining why your thesis is not merely an application, update, or footnote to those rivals.
- **Fallback thesis:** a narrower but still interesting version if the broad claim is preempted.

Do not claim novelty here. The right output is "novelty hypothesis ready to test," not "no one has done this."

## Stress-test the contribution

- **The "we already knew that" test** — if a knowledgeable reader says it, the descriptive layer is thin; deepen or drop it.
- **The "so what" test** — articulate the consequence if you are right; a claim with no stakes is not YLJ-worthy.
- **The "compared to what" test** — name the prevailing view your claim displaces (this previews `ylj-preemption-check`).
- **The "committee pitch" test** — a generalist student editor can explain the claim, why now, and why YLJ without reading your whole draft.
- **The "authority weight" test** — the claimed intervention rests on sources the piece can actually prove, not on a clever abstract frame.

## Checklist

- [ ] Thesis fits the one-sentence template and is contestable
- [ ] A generalist reader can restate it without your jargon
- [ ] Contribution type(s) named; normative addressee identified
- [ ] The prevailing view the claim displaces is named
- [ ] Every planned Part maps to establishing or applying the claim
- [ ] Contribution contract completed: claim, intervention, authority base, payoff
- [ ] Committee-pitch version names hook, timeliness, YLJ fit, and strongest objection
- [ ] Preemption handoff ready: search terms, likely rivals, distinctive move, fallback thesis

## Anti-patterns

- A "thesis" that is a topic ("This Article examines X") rather than a claim
- Three theses stitched with "and" — the piece reads as unfocused to a student editor
- A purely descriptive contribution dressed as theory (no framework actually emerges)
- A normative payoff with no named decision-maker who could act on it
- Overclaiming novelty before running `ylj-preemption-check`
- A generalist pitch that depends on prestige cues, topical buzz, or urgency without a legal intervention
- A "novelty" claim that has no search terms or likely rivals for the preemption check

## Output format

```
【Thesis】"This [Article/Essay] argues that ___, and therefore ___."
【Contribution】descriptive / doctrinal / theoretical / normative / critical (+ blend)
【Contract】claim / intervention / authority base / payoff
【Committee pitch】hook + why now + why YLJ + strongest objection
【Displaces】the prevailing view this claim challenges
【Addressee】who should act on the normative payoff
【Preemption handoff】search terms + closest likely rivals + distinctive move + fallback thesis
【Next】ylj-preemption-check to confirm the claim is genuinely new
```

## Supplementary resources

- [`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md) — a before→after YLJ introduction built around one claim
- [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) — YLJ pieces grouped by contribution type
