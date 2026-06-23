---
name: pnasnexus-rebuttal
description: Use after PNAS Nexus reviews arrive to triage the decision, prioritize experiments, and draft a point-by-point response that is respectful, evidence-led, and honest about limits. Covers the case where reviews were carried over from a PNAS transfer. Do not run before the main text is actually revised.
---

# Reviewer Rebuttal (pnasnexus-rebuttal)

## When to trigger

- A decision letter arrives (reject / major or minor revision / accept-with-revisions).
- You have reviewer comments and need a strategy before writing.
- A revision is drafted and you need the point-by-point response letter.
- The reviews include **transferred PNAS reviews** plus new PNAS Nexus reviews.

## Step 0: read the editor's letter first

The **handling editor's** framing outranks individual reviewers. At PNAS Nexus the paper was assigned to an Editorial Board member and then a handling/guest editor; that editor's letter tells you what is load-bearing. Identify:

- The decision type and whether a new review round is implied.
- Which concerns the editor **emphasizes** (these are load-bearing — address fully).
- Any **deal-breaker** the editor names (e.g., "the central claim needs independent validation").

> A "reject but would consider a new submission" is an invitation gated on the deal-breaker. Don't treat it as a flat reject, but don't under-deliver either.

## Special case: reviews carried over from a PNAS transfer

If the paper was **transferred from flagship PNAS**, prior PNAS reviews travel with it. When responding:

- Treat the **carried-over PNAS comments** as part of the record — the PNAS Nexus editor can see them. Address them too, not just the new PNAS Nexus reviews.
- If a PNAS reviewer's concern was about **fit/priority** (why the transfer happened), you usually don't need to re-litigate it for PNAS Nexus — but if it was about **rigor**, it still applies and must be answered with evidence.
- Don't assume the transfer "used up" the criticism; the PNAS Nexus editors assess independently.

## Triage every comment into 4 buckets

| Bucket             | Action                                                            |
|--------------------|------------------------------------------------------------------|
| **Do** (fair, feasible) | Make the change; show it; quote the new text/figure.        |
| **Do-partial**     | Do what's feasible; explain the boundary with evidence.          |
| **Defend** (wrong/out of scope) | Push back respectfully, with data/citations — not assertion. |
| **Defer** (future work) | Acknowledge; add a sentence to the text; don't over-promise. |

Most rejections-on-revision come from **silently skipping** a load-bearing comment or **defending** when an experiment was actually needed.

## Prioritize the experiments

- Rank requested experiments by **(impact on the central claim) × (feasibility)**.
- The reviewer's #1 concern about the **main claim** must be answered with data, not prose.
- If an experiment is infeasible, offer the **strongest alternative evidence** and say why it suffices.

## Response-letter format

For each comment:

```
Reviewer N, Comment k: <verbatim quote of the reviewer>

Response: <what we did / our reasoning>. <Evidence: new Fig./table, statistics.>
Changes: "<quoted new manuscript text>" (p. X, lines Y–Z; new SI Fig. Sk).
```

- Open with a short thank-you and a 3–4 line summary of the **major changes** across the whole revision.
- Quote each comment verbatim; never paraphrase a reviewer in a way that softens their point.
- **Quote the new manuscript text** so the editor can verify without hunting.
- Use a consistent visual convention (reviewer text plain, your response indented, manuscript quotes in italics/color).

## Tone rules

- Respectful and non-defensive, even when the reviewer misread the paper — if they misread it, the writing was unclear; fix the writing **and** explain.
- Concede real limitations explicitly; an honest limitation paragraph builds credibility.
- No sarcasm, no "as we clearly stated" — assume good faith.

## Claim-integrity / over-claiming watch

If a reviewer says the conclusion outruns the data, this is the **most dangerous** comment. Either add the evidence or **narrow the claim** in the title, Significance Statement, abstract, and last paragraph — and say you did. Because the **Significance Statement** is public-facing and broad, re-check it specifically for over-claiming when you narrow (link `pnasnexus-significance`), and re-confirm it stays within 50–120 words; re-run `pnasnexus-fit` if the narrowed claim weakens broad significance.

## PNAS Nexus revision ledger

Build a separate ledger for the parts of a PNAS Nexus revision the editor can audit quickly:

| PNAS Nexus surface | What to verify before response drafting |
|---|---|
| Significance Statement | Still a broad, non-hyped contribution claim, matching the narrowed evidence, within 50–120 words? |
| Abstract / title | Public-facing claims aligned with the strongest validated result, not the original aspiration? |
| Main figures | Did each new analysis change a main-text figure, SI figure, or stated null result? |
| Supporting Information | New robustness, data-processing, and method details findable by reviewer-comment number? |
| Data / code availability | New dataset/software/accession require an updated availability statement and `[dataset]` citation? |
| Page budget | After additions, is the revision still within the article-type page limit, or do items move to SI? |

When reviewers ask for extra validation, prefer a response package that shows **where** the evidence landed: "new main Fig. 3C", "new SI Fig. S7", "new Methods paragraph", or "new Data and Code Availability sentence." Do not bury PNAS-Nexus-specific changes only in the response letter.

## Output format

```
【Decision type】 reject / reject-resubmit / major / minor
【Editor's load-bearing concerns】 [...]
【Transferred PNAS reviews?】 N/A | yes → which carried-over concerns still apply (rigor) vs not (fit)
【Deal-breaker】 ... → plan to resolve
【Comment triage】 Do [...] / Do-partial [...] / Defend [...] / Defer [...]
【Experiment priority】 ranked by impact × feasibility
【Claim integrity】 narrowing needed? (re-check Significance Statement 50–120w + pnasnexus-fit)
【Revision ledger】 Significance Statement / SI / data-code availability / page-budget changes
【Response letter】 drafted point-by-point with quoted changes
```

## Anti-patterns

- **Do not** silently skip a comment the editor emphasized.
- **Do not** ignore carried-over PNAS reviews on a transferred paper — they are part of the record.
- **Do not** defend by assertion where the reviewer asked for data.
- **Do not** over-promise future work to dodge a needed experiment.
- **Do not** forget to update (and re-count) the Significance Statement and abstract if you narrow the claim.
- **Do not** draft the response before the manuscript is actually revised.
