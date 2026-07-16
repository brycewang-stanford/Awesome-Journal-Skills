---
name: advmat-referee-strategy
description: Use when choosing suggested and opposed referees for an Advanced Materials submission and pre-empting the objections materials reviewers most often raise. Plans referee selection and objection defense; does not write the manuscript or the rebuttal.
---

# Advanced Materials Referee Strategy (advmat-referee-strategy)

## When to trigger

- The submission form asks for suggested and opposed referees and you have not planned them
- You want to pre-empt the objections a materials reviewer will raise before they raise them
- You are unsure who can judge both the *novelty* and the *characterization rigor* of the work
- A prior submission was rejected on a predictable objection you could have addressed

## Who should judge an Adv. Mater. paper

Adv. Mater. work sits at the intersection of synthesis/characterization and function/device. A good referee set covers **both** competences, plus the breadth the gate demands:

- **A synthesis/characterization expert** — can assess whether the structure/phase/composition claims are proven by the technique set.
- **A property/device expert** — can assess whether the performance and benchmarking are fair and meaningful.
- **A neighboring-field / application referee** — supports the broad-impact claim by judging why the advance matters beyond the immediate subfield.

Aim for referees who are current in the field, not conflicted, and not exclusively from your own collaboration network. Follow the journal's rules on number and eligibility.

## Suggesting referees well

- Suggest people who can evaluate the *whole* chain — someone who only knows the synthesis may wave through a weak device claim, and vice versa.
- Include at least one referee from the claimed neighboring/device community to substantiate breadth.
- Avoid conflicts: recent coauthors, collaborators, same-institution colleagues, and advisors/advisees are ineligible.
- Do not stack the panel with people certain to be friendly; obvious partisan suggestions undermine credibility.

## Opposing referees (use sparingly)

- List direct competitors with a genuine conflict, or individuals with a documented dispute — briefly and professionally.
- Keep the list short; a long opposed list reads as defensiveness.
- State a factual rationale ("direct competitor on the same material system"), not a personal complaint.

## Pre-empt the objections materials reviewers raise

Address these *in the manuscript* before submitting; each is a common Adv. Mater. rejection lever:

| Likely objection                                          | Pre-empt by                                                        |
|-----------------------------------------------------------|--------------------------------------------------------------------|
| "The advance is incremental / optimization only"          | Frame the design rule / trade-off broken; contrast with SOTA       |
| "The structure/phase is not proven"                       | Triangulate with complementary techniques (see `advmat-methods`)   |
| "The hero image is not representative"                     | Give distributions and statistics, not one micrograph              |
| "The benchmarking is unfair / cherry-picked"              | Compare under matched conditions; cite the best reported systems   |
| "It won't reproduce / batch variation hidden"             | Report n, mean ± s.d., and batch-to-batch data in the SI           |
| "Stability/durability not shown"                          | Include cycling/aging/operational-stability data                   |
| "Not broad enough for Adv. Mater."                        | Name the out-of-subfield beneficiary; make the impact case (cover letter) |

## Checklist

- [ ] Referee set covers synthesis/characterization AND property/device competence
- [ ] At least one suggested referee substantiates the broad-impact claim
- [ ] No conflicts (recent coauthors, collaborators, same institution, advisors/advisees)
- [ ] Suggestions are current and credible, not merely friendly
- [ ] Opposed list is short, factual, and professional
- [ ] The manuscript pre-empts the incremental, characterization, benchmarking, and stability objections
- [ ] Referee choices are consistent with the cover-letter impact case

## Anti-patterns

- Suggesting only friendly names or only your own subfield
- Suggesting referees with obvious conflicts (recent coauthors, same institution)
- A long opposed list that signals defensiveness
- Leaving a predictable objection (no benchmarking, single-technique proof) unaddressed
- Naming a "breadth" referee while the manuscript makes no breadth argument

## Output format

```
【Suggested referees】synth/char: ... | property/device: ... | neighbor/impact: ...
【Conflicts screened】yes / fix
【Opposed referees】name — factual rationale (short)
【Objections pre-empted】incremental / structure / hero-image / benchmarking / stability — covered?
【Consistent with cover letter】yes / fix
【Next】advmat-submission (enter referees) or advmat-revision (after reports)
```

> Rules on referee numbers, eligibility, and conflicts are set by Wiley and evolve — verify on the official Advanced Materials author page.
