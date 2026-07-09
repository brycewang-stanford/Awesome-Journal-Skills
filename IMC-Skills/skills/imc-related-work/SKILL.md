---
name: imc-related-work
description: Use when writing or auditing the related-work and positioning of an ACM IMC paper, covering the measurement literature lanes, positioning against prior datasets and vantage points, delta-first framing, citing the datasets and tools you build on, distinguishing IMC from SIGCOMM/NSDI/PAM prior art, and keeping self-citations double-blind.
---

# IMC Related Work

Use this to position an IMC paper. In measurement, related work is not just prior *claims* — it is
prior **datasets, vantage points, tools, and methodologies**. IMC reviewers know the measurement
landscape intimately; a positioning that ignores the dataset or platform your finding builds on, or
that misattributes measurement work to the wrong venue, reads as unfamiliarity with the field.

## Cover the measurement literature lanes

Position against the relevant lanes, not a generic "prior work" pile:

- **The same phenomenon, measured before:** who measured this, from which vantage points, when, and
  what did they find? Your delta is usually breadth, recency, a better vantage point, or a
  correction.
- **The datasets and platforms you use:** RIPE Atlas, CAIDA data, scan datasets, DNS platforms, top
  lists, telescopes — cite the paper that introduced the instrument, and note its known biases.
- **The methodology you extend or question:** if you improve or audit a measurement technique, cite
  its origin and state what you change.
- **Adjacent findings that frame significance:** related measurements that make your question
  matter.

## Delta-first positioning

Lead each comparison with the difference, not a summary:

- "Prior work measured X from a single vantage point in 2019; we measure it from N vantage points
  across M regions over a 12-week window in 2026, revealing a diurnal pattern invisible to a
  snapshot."
- Make the delta a **measurement delta**: more/better vantage points, longer window, better ground
  truth, a corrected input, or a newly reachable dataset — not merely "we also study this."

## Position against prior datasets and vantage points

This is IMC-specific and easy to underdo:

- If you reuse a dataset, say **which version/vintage** and why it still supports your claim.
- If you build a new dataset, contrast its **coverage and provenance** with existing ones — this is
  also the seed of a Community Contribution Award case (`imc-artifact-evaluation`).
- Acknowledge the **biases** of instruments you rely on (e.g., top-list instability, telescope
  coverage gaps); a reviewer who introduced that instrument may be reading you.

## Get the venue attribution right

Measurement work is spread across venues, and misattribution signals unfamiliarity:

- Much scanning/tooling landed at **USENIX Security or CCS** (e.g., ZMap, Censys), not IMC.
- Systems and protocol design with a measurement flavor is often **SIGCOMM, NSDI, or CoNEXT**.
- Focused active-measurement work often appears at **PAM**.
- Check dblp before writing "as shown at IMC" — cite the actual venue (see
  `resources/exemplars/library.md` for the sibling-confusion guard).

## Keep self-citations double-blind

IMC is double-blind, so positioning against your own prior work is a leak risk:

- Refer to your prior work in the **third person**: "Prior work [12] measured..." not "In our
  earlier work we...".
- Do not let a chain of self-citations, a reused private vantage point, or a distinctive testbed
  name deanonymize you.
- Cite your own datasets by their anonymized/public identifier, not an account or lab URL.

## Failure patterns

| Pattern | Why it hurts | Fix |
|---|---|---|
| Prior work summarized, delta implied | Reviewer cannot see the contribution | Lead every comparison with the measurement delta |
| Instrument reused without citing its origin/bias | Reads as unaware of the field | Cite the dataset/tool paper and its known biases |
| Measurement misattributed to IMC | Signals unfamiliarity | Verify the venue on dblp; cite correctly |
| Self-citation in first person | Double-blind leak | Third-person; anonymized dataset references |

## Output format

```text
[Lane coverage] phenomenon / datasets-platforms / methodology / adjacent framing — all covered?
[Delta] stated as a measurement delta (vantage points/window/ground truth/dataset)? yes/no
[Dataset positioning] instruments cited with vintage + biases? yes/no
[Venue attribution] measurement prior art cited to the correct venue? yes/no
[Anonymity] self-citations third-person, no infrastructure leak? passed/issues
[Edits] <ordered list>
```
