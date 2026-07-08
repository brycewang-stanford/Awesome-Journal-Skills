---
name: ndss-writing-style
description: Use when drafting or revising an NDSS paper's prose — building the first page around a capability-bounded networked adversary, sizing claims to evidence, weaving the ethics signal into the narrative, and fitting the argument into NDSS's 13-page body ahead of a two-round read.
---

# NDSS Writing Style

An NDSS paper is read twice under different pressure. Round 1 decides, from a fast read,
whether the paper continues at all — the early reject arrives with no rebuttal for the cut.
Round 2 reads closely with your rebuttal in hand. Write the first page for the fast read
and the rest for the close one.

## The first-page contract

By the end of page one, a Round-1 reviewer should be able to fill in this table from memory:

| Question | Your first page must answer it as... |
| --- | --- |
| Who attacks? | A capability-bounded adversary: vantage (on/off-path, insider, tenant), budget, access |
| What breaks / what holds? | The precise property violated or guaranteed, in protocol/system terms |
| Against what? | Real systems named at the right granularity (protocol version, deployment class) |
| Why now? | The deployment shift, protocol change, or measurement gap that opens the question |
| How proven? | The evidence type: end-to-end exploit, testbed defense evaluation, population measurement |
| Is it handled responsibly? | One sentence signaling disclosure/harm posture, expanded later |

The single most common Round-1 kill is an adversary described by adjective ("powerful",
"realistic") instead of by capability. Write attackers the way you would write an API
contract: what they can call, what they cannot.

## Sizing claims

- Bind every claim to the tested envelope: *"defeats resolver-side validation as deployed
  in versions X-Y"*, never *"defeats DNS validation."*
- Quantify with populations, not superlatives. "Widespread" is an argument you have not
  made; "present in N of M sampled deployments, sampled by ⟨method⟩" is one you have.
- Negative space is credibility: a visible limitations paragraph that names the adversary
  who *does* beat your defense reads as competence, not weakness, to this PC.
- Never promise what evaluation cannot show — "completely prevents", "provably secure"
  (without a proof and a model), "first ever" (without a search you can defend).

## The ethics thread

NDSS expects ethics to be woven through, not appended: a signal on page one, method-level
handling where the risky procedure is described, and the optional **Ethics Considerations
section immediately before the references** (excluded from the 13-page count, per the 2027
CFP, checked 2026-07-08) carrying the full protocol — disclosure timeline, harm analysis,
Menlo-style reasoning, review-board interaction. Prose that describes live scanning or user
data with no ethical acknowledgment reads to reviewers as a paper that has not understood
the venue.

## Fitting 13 pages

The 2027 limit is 13 pages excluding the ethics section, references, and appendices, in the
NDSS template. Discipline that works:

- Budget pages at outline time: ~1 intro, ~1 background+threat model, ~4-5 design/attack,
  ~4 evaluation, ~1 related work, ~1 discussion+limitations. Adjust, but on purpose.
- One figure that explains the attack path or architecture is worth a page of prose;
  a figure that decorates costs a fifth of your evaluation budget.
- Compress with structure, not font tricks — template tampering is a desk-reject class
  offense at every security flagship, this one included.
- Move proofs, extra configurations, and protocol message details to appendices, but keep
  every result the acceptance decision depends on inside the body (see
  `ndss-supplementary` for the split rules).

## Revision drill for an existing draft

```text
PASS 1 (adversary): highlight every sentence that grants or assumes attacker
        capability. They must all appear in the threat model — no capability
        may debut inside the evaluation.
PASS 2 (claims): list every claim sentence; append its evidence pointer
        (§/Fig/Table). Claims with no pointer get weakened or cut.
PASS 3 (vocabulary): replace "secure", "practical", "realistic", "large-scale"
        with the number, version, or bound that justified the word.
PASS 4 (fast read): read only title, abstract, section heads, figure captions,
        and the conclusion in 4 minutes — the Round-1 experience. Does the
        contribution survive? If not, restructure headings, not sentences.
PASS 5 (ethics thread): page-one signal present? method-level handling present?
        ethics section consistent with both?
```

## Tone

Third person or first-person plural, past tense for what was measured, present for what the
system does. No exclamation of severity — the exploit speaks for itself or it does not.
Double-blind: strip names, funders, internal system codenames, and self-identifying phrases
like "our previous work" (cite yourself in third person; details in `ndss-submission`).

## Output format

```text
[First-page contract] 6/6 answered? list the misses
[Claim ledger] N claims, M without evidence pointers → actions
[Adversary discipline] capabilities that debut outside the threat model
[Ethics thread] page-1 signal / method handling / section — present or missing
[Page budget] planned vs actual per section
```
