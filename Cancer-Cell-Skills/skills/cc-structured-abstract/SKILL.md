---
name: cc-structured-abstract
description: Use when writing the Cancer Cell (Cell Press) front matter — the Summary, eTOC blurb, Highlights, and graphical abstract. It crafts these short items for accuracy and impact; it does not write Results or calibrate statistics.
---

# Summary, Highlights & Graphical Abstract (cc-structured-abstract)

## When to trigger

- Need a Cancer Cell **Summary** (the abstract)
- Need **Highlights** (the short bullet list Cell Press requires)
- Need the **eTOC blurb** (one-paragraph teaser for the table of contents)
- Building or refining the **graphical abstract**

## The Summary (abstract)

Cell Press uses a single-paragraph **Summary** (verify the current word limit on the author page). Structure it as a tight mechanistic arc:

1. **Context / gap** — the cancer problem and the unknown (1 sentence).
2. **Approach** — the systems used (cells / in vivo / human), at a high level.
3. **Core finding** — the mechanism: what regulates what, with direction.
4. **Validation** — that it holds in vivo and/or in patient data.
5. **Significance** — the translational implication (vulnerability / biomarker / therapy), calibrated to the evidence.

Lead with the discovery, not the background. Name the molecule/axis and the cancer context concretely. Avoid hype words ("novel," "unprecedented") and unsupported clinical promises.

## Highlights

- Provide the required number of short bullets (commonly four; verify current count), each ~85 characters.
- Each highlight is a **result**, not a method or aim.
- Order them as a mini-story: key mechanism → validation → translational point.
- Make them specific and declarative ("X drives Y via Z in pancreatic tumors"), not vague ("X plays a role").

## eTOC blurb

- One short paragraph (a few sentences) written for a broad cancer audience.
- Third person, present tense; names the authors' key finding and why it matters.
- Often written as "Author et al. show that ..." — confirm the current style.
- No abbreviations that a non-specialist would not know.

## Graphical abstract

- One panel that conveys the **mechanism and its consequence** at a glance.
- Show the axis (input → node → output) and the tumor context; minimal text.
- Must match the paper's actual claims — no implied results beyond the data.
- Build in BioRender/Illustrator at required resolution; legible at thumbnail size.

## Checklist

- [ ] Summary leads with the discovery and names the mechanism concretely
- [ ] Summary states orthogonal validation (in vivo / human) and a calibrated significance line
- [ ] Summary within the current word limit; no hype words
- [ ] Highlights are results, specific, ordered as a story, within length
- [ ] eTOC blurb is broad-audience, present tense, accurate
- [ ] Graphical abstract shows mechanism → consequence and matches the data
- [ ] Front matter is consistent with the paper's actual claims and `n`/evidence

## Anti-patterns

- Background-heavy Summary that buries the finding
- Highlights that restate aims/methods or are vague
- Overclaiming therapeutic impact in the Summary or graphical abstract
- Graphical abstract implying results not shown in the paper
- eTOC blurb stuffed with jargon and abbreviations
- Inconsistent gene/protein nomenclature across front matter and text


## Abstract pass for Cancer Cell

Use this as a second-pass capability check. First lock the cancer context, mechanism, model system, validation chain, and translational boundary; then test whether the manuscript addresses cancer-biology reviewers who expect mechanistic oncology, translational relevance, and strong multi-modal validation.

- **Primary move:** Compress to question, design, population/object, result, limitation, and contribution; remove generic importance sentences.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Cell for broader biology, Nature Cancer for oncology breadth, Clinical Cancer Research for clinical translation; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Summary】drafted; words = ...; leads with finding? Y/N
【Validation line】in vivo / human stated? Y/N
【Highlights】n bullets; all results? within length?
【eTOC blurb】broad-audience? accurate? Y/N
【Graphical abstract】mechanism→consequence? matches data? Y/N
【Overclaim check】hype/clinical promises removed? Y/N
【Next step】cc-ethics-registration or cc-writing-style
```
