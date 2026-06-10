---
name: est-literature-positioning
description: Use when positioning an Environmental Science & Technology (ES&T) manuscript against prior work across environmental chemistry, engineering, toxicology, and policy. ES&T is multidisciplinary, so the paper must engage the right literatures and state the knowledge gap it closes. It frames the gap and citations; it does not fabricate references.
---

# Literature Positioning (est-literature-positioning)

ES&T draws a multidisciplinary readership, and editors decline work that does not engage the relevant
literature or that re-derives what is already known. This skill positions the contribution: what is
known, what is missing, and why this paper closes the gap for a real environmental problem.

## When to trigger

- Writing the introduction or the "knowledge gap" framing
- Building a **Critical Review** or **Perspective** that must map a whole field
- A reviewer said the work "ignores relevant literature" or "is not novel"
- Deciding which adjacent fields (chemistry, engineering, tox, policy) to cite

## How to position for ES&T

1. **State the gap as a process question.** Frame what is unknown about fate, transport,
   transformation, exposure, toxicity, treatment, or management — not just "few studies have looked."
2. **Engage across sub-fields.** Cite the analytical, mechanistic, engineering, and (where relevant)
   policy literatures the broad ES&T audience expects, including prior ES&T/ES&T Letters work.
3. **Differentiate, don't dismiss.** Say precisely how your concentrations, matrices, mechanisms, or
   scale advance beyond the closest prior studies.
4. **Use authoritative sources.** Prefer peer-reviewed work, agency datasets (EPA, NIST), and primary
   measurements over secondary summaries; use ACS numbered citation style.
5. **For Reviews/Perspectives**: organize around an analytical framework, surface contradictions, and
   identify the open questions — synthesis, not annotated bibliography.

## Which literatures a multidisciplinary referee panel expects you to engage

ES&T sends a paper to ~three reviewers who often span sub-fields. A gap framed only in one literature
reads as naive to the others. Map your claim to the adjacent bodies of work before drafting:

| If your contribution is about... | You must also engage... | Reviewer who flags the omission |
|----------------------------------|--------------------------|----------------------------------|
| A new occurrence/measurement | the analytical-method and fate literature | the environmental chemist |
| A treatment/removal process | the engineering and mass-transfer literature | the process engineer |
| An exposure or effect | the toxicology / dose–response literature | the eco/health toxicologist |
| A regulatory or LCA implication | the policy / sustainability literature | the policy-interface reviewer |
| A transport/transformation model | prior model formulations and field validation | the modeler |

## Worked micro-example (illustrative — positioning an emissions-inventory analysis)

Suppose the paper re-estimates methane emissions from a basin's oil-and-gas infrastructure using
aircraft data. A weak introduction cites only prior inventories and claims "few studies have
top-down constrained this basin." A reviewer reads that as incremental. The ES&T-grade positioning
(illustrative):

- **Known:** bottom-up inventories systematically *underestimate* basin emissions; prior top-down
  studies disagree by a factor of ~2 (illustrative) and have not reconciled the discrepancy.
- **Gap (as a process question):** the *attribution* of the excess — which source category and which
  operational state — is unresolved, so mitigation targeting is blind.
- **This paper closes it by:** pairing aircraft fluxes with facility-level activity data to attribute
  the excess to a small fraction of super-emitting sites, changing where regulators should act.

The move that lifts it past desk-screen: the gap is a *mechanism/attribution* question with a policy
consequence, engaging the inventory, atmospheric-measurement, and regulatory literatures at once —
not a "we add another number" claim.

## Referee-pushback patterns and the venue-specific fix

- *"Novelty is incremental — this is another occurrence dataset."* → Reframe the gap as a process,
  attribution, or exposure question the data resolve; differentiate explicitly from the closest prior
  ES&T studies by matrix, scale, or mechanism.
- *"Ignores relevant literature."* → Add the adjacent sub-field (often engineering or tox) the
  multidisciplinary panel expects; cite prior ES&T/ES&T Letters work directly.
- *"'First study' claim is not supported."* → Soften to a specific, defensible advance or remove it.

## Anti-patterns

- A wall of citations with no articulated gap
- Ignoring an obvious adjacent literature (e.g., citing chemistry but not the engineering or tox work)
- "First study to…" claims that a quick search would falsify
- Citing only your own group; missing key prior ES&T papers reviewers will know
- A "review" that summarizes papers in sequence instead of synthesizing them

## Output format

```
【Known】2–3 lines on the state of the art
【Gap】the specific process/exposure/treatment question left open
【This paper closes it by】mechanism / scale / matrix / concentration advance
【Literatures engaged】chemistry / engineering / tox / policy (which apply)
【Citation style】ACS numbered, primary sources
【Next】est-study-design
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference databases and managers; ACS style
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — ES&T scope and article-type expectations
