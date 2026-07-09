---
name: sensys-supplementary
description: Use when deciding what goes in a SenSys paper's body versus its unlimited references and appendices versus HotCRP fields — keeping the double-column body carrying the argument, moving full protocols, extra plots, and derivations to the appendix, blinding anonymous artifact links, and keeping the Response to Reviewers out of the body.
---

# SenSys Supplementary Material

SenSys gives you an unusual amount of room *outside* the page cap: **references and appendices
are unlimited**. That freedom is a trap if it becomes a dumping ground. The discipline is to keep
the ≤ 12-page (full) or ≤ 6-page (short) body carrying the **argument**, and to place everything a
reviewer might *want* but does not *need to judge the claim* in the appendix — reachable, but not
in the way of the story.

## The placement decision

For each piece of content, ask: *must a reviewer read this to believe the headline claim?*

| Content | Body (in the cap) | Appendix (unlimited) | HotCRP field |
|---|---|---|---|
| The mechanism and its constraint model | Yes | — | — |
| The headline energy/latency/accuracy results | Yes | — | — |
| Full measurement protocol (instrument settings, calibration steps) | Summary only | Full detail | — |
| Extra ablations and secondary plots | The load-bearing ones | The rest | — |
| Derivations / proofs of a bound | Statement + intuition | Full proof | — |
| Complete hardware BOM and wiring | — | Yes | — |
| Deployment logs, per-node uptime tables | Summary | Full tables | — |
| Title, abstract, topics, conflicts | — | — | Yes (verbatim-match PDF) |
| Anonymous artifact link | Cited in text (blinded) | — | If the form asks |

## The body earns its space

Because appendices are free, the body must be *ruthless*: every paragraph either advances the
sensing-pain → mechanism → measured-behavior arc (`sensys-writing-style`) or moves to the
appendix. A body padded with protocol detail reads as unfocused; a body that states results and
points to `App. B` for the protocol reads as confident. Reviewers are not obligated to read
appendices, so **nothing load-bearing may hide there** — if the claim depends on it, summarize it
in the body and expand in the appendix.

## Blind the artifact links

Supplementary artifact links are the classic anonymity leak. During double-blind review:

```text
[ ] Repo link is an anonymized mirror (no username, no lab/org in the URL).
[ ] Zenodo/OSF deposit has authors anonymized.
[ ] No link resolves to a personal, lab, department, or company domain.
[ ] Trace/data archives carry no author metadata or identifying paths.
```

A single un-blinded GitHub URL in the supplement can de-anonymize the whole submission — sweep the
appendix with the same rigor as the body (`sensys-submission`).

## Keep the resubmission packet out of the body

If you are resubmitting at the next deadline, the **Response to Reviewers** is a separate document
(`sensys-author-response`), not appended to the paper's body — it must not consume page budget and
must follow the CFP's stated form (待核实 for the exact mechanism). The revised paper stands on its
own; the response explains how it changed.

## Structure the appendix so it is navigable

An unlimited appendix that no one can navigate is wasted. Give it the same structure your body
promises: if §4.2 says "full protocol in App. B," App. B exists, is labeled, and contains exactly
that. Cross-reference precisely — a reviewer checking one number should reach it in one hop.

## Output format

```text
[Body]     is every body paragraph load-bearing? list what should move to appendix
[Appendix] is anything load-bearing hiding in the (optional-to-read) appendix?
[Blind]    artifact/data links swept for anonymity — pass/gap
[Resub]    response-to-reviewers kept out of the body? (if applicable)
[Nav]      body cross-references resolve to labeled appendix sections? pass/gap
[Open]     the one placement decision most affecting how the paper reads
```
