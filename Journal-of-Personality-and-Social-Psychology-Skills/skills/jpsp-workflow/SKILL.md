---
name: jpsp-workflow
description: Use as the entry point for any Journal of Personality and Social Psychology (JPSP) manuscript. Routes to the right JPSP sub-skill based on where you are in the lifecycle and — first of all — which of the three independently edited sections (ASC, IRGP, PPID) fits the paper. It dispatches; it does not draft content.
---

# JPSP Workflow Router (jpsp-workflow)

The orchestrator for a JPSP submission. JPSP is **not** one journal with one editor — it is **three
independently edited sections**, each with its own editor, masthead, rules, and Editorial Manager
portal. It is also a **long-format, multi-study** journal: a developed theory plus several related
studies, not a single short report. The router's first job is to lock the **section**, then route by
stage.

## When to trigger

- Starting a new JPSP paper and unsure where to begin
- Unsure which of the **three sections** the paper belongs to
- Mid-project and unsure which skill applies next
- Returning with a decision letter (route to `jpsp-rebuttal`)

## First question: which section?

| Your contribution is about… | Section | Portal |
|------------------------------|---------|--------|
| Attitudes, persuasion, social cognition, emotion/motivation in social context | **Attitudes and Social Cognition (ASC)** | `editorialmanager.com/asc` |
| Close relationships, dyads, intragroup/intergroup processes, group behavior | **Interpersonal Relations and Group Processes (IRGP)** | `editorialmanager.com/irg` |
| Personality structure/development/assessment, individual differences, traits | **Personality Processes and Individual Differences (PPID)** | `editorialmanager.com/pid` |

> One paper, one section. The sections are edited separately and apply their **own** length rules
> (ASC intro+discussion ≤ 3,500 words; IRGP ≤ 5,000 words and ≤ 5 studies in the main text; PPID
> "as succinctly as possible"). Confirm the live per-section page — see 待核实 in the source map.

## Routing map (stage → skill)

```text
Section + idea fit?              → jpsp-topic-selection
Where does it sit in the field?  → jpsp-literature-positioning
What's the theory + hypotheses?  → jpsp-theory-and-hypotheses
Is the multi-study package sound?→ jpsp-study-design
Are analyses + meta-analysis ok? → jpsp-data-analysis
Are the exhibits APA-clean?      → jpsp-tables-figures
Does it read in APA long-format? → jpsp-writing-style
Transparency / JARS / TOP?       → jpsp-open-science-and-transparency
How will the section judge it?   → jpsp-review-process
Ready to submit (masked)?        → jpsp-submission
Got an R&R / decision?           → jpsp-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-and-hypotheses → study-design → data-analysis →
tables-figures → writing-style → open-science-and-transparency → review-process → submission → rebuttal`

Iterate: most JPSP papers loop theory ↔ study-design ↔ data-analysis several times as the package
grows from Study 1 to a coherent set with an internal meta-analysis.

## Anti-patterns

- Treating JPSP like a short-report journal (it is long-format, multi-study) — see Psychological Science instead for short reports
- Drafting before choosing a section, then forcing the paper into the wrong one
- Building one study and hoping reviewers waive the multi-study expectation
- Leaving the internal meta-analysis / integrative analysis to "later"

## Calibration anchors for a JPSP submission

The fixed expectations to hold while routing — binding figures (caps, portals) must be confirmed against the journal's submission guidelines (待核实):

| Anchor | JPSP expectation | Why it shapes routing |
|--------|------------------|------------------------|
| Package size | A converging **multi-study** set, not one study | An inherently single study → a short-report venue, not JPSP |
| Sections | Three independently edited: **ASC / IRGP / PPID** | Lock the section before any other step |
| Innovation | Theoretical advance precedes data strength | Theory comes before design |
| Open science | **TOP Level 2**, JARS, prereg, effect sizes with CIs | Transparency is gated at the editor's desk, not polish |
| Integration | **Internal meta-analysis** across studies | Plan comparable metrics from Study 1 |

These anchors are the post-credibility-revolution defaults the pack operationalizes; when a stage is unclear, return to the anchor it touches.


## Router pass for Journal of Personality and Social Psychology

Treat this skill as an executable review pass, not a prose hint. First lock the construct validity, study sequence, power/robustness plan, and boundary conditions; then judge whether the current manuscript answers the venue's real reader: psychology reviewers who need a theoretical construct, validated measurement, and cumulative-study logic.

- **Do the pass:** Run the pack as a sequence: fit gate, evidence gate, writing gate, source-map gate, and final output contract; stop when a gate lacks evidence.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Psychological Science for shorter general-interest findings, Personality and Social Psychology Bulletin for field scope, Journal of Experimental Social Psychology for experiment-centered claims; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Section】ASC / IRGP / PPID  (why this section, one line)
【Stage】section-fit / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Route to】jpsp-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — personality/social-psych data + software by design
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official APA JPSP URLs behind every fact in this pack
