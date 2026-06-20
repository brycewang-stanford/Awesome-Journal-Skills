---
name: jeem-rebuttal
description: Use when a Journal of Environmental Economics and Management (JEEM) decision letter or referee report needs a response strategy — triaging R&R demands, planning new spatial/valuation robustness, and writing the response letter the editor and field referees expect. Plans the revision; it loops back to the analysis skills for the actual work.
---

# Rebuttal Strategy (jeem-rebuttal)

## When to trigger

- A JEEM R&R, major-revision, or reject-and-resubmit letter has arrived
- Two referees disagree (a methods referee vs. a policy referee) and you must satisfy both plus the editor
- A referee demands new spatial SEs, an alternative valuation specification, or a leakage analysis
- You need to decide what is a must-do versus a polite-decline before drafting responses
- The headline welfare number moved under a requested check and you must decide how to present it

## Tone and structure of the response document

The response is a professional document the editor and referees will reread alongside the revision, so structure it for their convenience. Open with a short cover note summarizing the major changes and where the core demand was addressed. Then reproduce each referee comment verbatim in a quoted block, followed by your response in plain text, followed by a pointer to the exact location in the revision ("see revised Section 4.2 and Table 5"). Keep the register collegial and evidence-led even when a referee erred; the editor is reading for whether you engaged seriously, not whether you won every exchange. Brevity that shows the work beats long defensive prose.

## Reading a JEEM decision letter

The editor's letter is the contract — read it first and let it set priorities; referee reports are evidence, the editor's summary is the verdict. At JEEM the typical fault lines are field-specific: a referee will press on **sorting/spatial confounding, valuation bias, leakage, or welfare overreach**, and the editor will weight whichever threatens the paper's core welfare claim. Separate (1) requests that go to the headline number (must-do), (2) requests that strengthen but do not threaten it (do well), and (3) requests that are wrong or out of scope (decline with evidence).

## Triage and response craft

1. **Build a point-by-point table.** Every referee comment → your action → where in the revision it appears. Editors at JEEM expect a complete, numbered response; a missed comment reads as evasion.
2. **Lead each response with the action, then the evidence.** "We now report Conley spatial SEs at a 100 km cutoff (Table 3); the estimate is unchanged at 4.5%." Not a paragraph of throat-clearing.
3. **Route new analysis to the right skill.** Spatial/valuation/DiD robustness → `jeem-robustness`; a contested identification claim → `jeem-identification`; a welfare-mapping dispute → `jeem-theory-model`; new exhibits → `jeem-tables-figures`. Do the work there, then report it here.
4. **Decline with evidence, not attitude.** When a referee is wrong (e.g., asks for a check that the design makes irrelevant), show *why* with a sentence and a citation; concede the framing even when you reject the request.
5. **Reconcile the two referees explicitly.** If R1 wants more structure and R2 wants more reduced-form transparency, state how the revision serves both, so the editor sees you navigated the conflict.
6. **Re-check the welfare claim's honesty.** Many JEEM revisions are accepted once the authors bound the claim (marginal not total, local not external) the referees worried about.

## Concession as strategy

The strongest JEEM rebuttals concede where the referee is right and bound the damage rather than fighting every point. If a referee shows the welfare gain is smaller once leakage is netted, report the smaller number and show the conclusion survives — a defended $0.8X beats an indefensible $X. If a check moves the estimate, say so and explain why the headline holds. Editors read graceful concession as scientific maturity; reflexive defense of every claim reads as the opposite and makes the editor side with the referee.

## Checklist

- [ ] The editor's letter is treated as the priority contract; must-do vs. do-well vs. decline sorted
- [ ] A complete numbered point-by-point response table exists; no comment skipped
- [ ] Each response leads with the action and the evidence (table/figure number, new estimate)
- [ ] New analyses were actually run via the relevant jeem-* skill, not promised
- [ ] Declines are backed by a reason and, where possible, a citation — never dismissive
- [ ] Conflicting referees are reconciled explicitly for the editor
- [ ] The welfare claim is re-bounded where a referee challenged its scope
- [ ] Process/style facts re-verified against the current guide for authors (待核实)

## Mapping the classic JEEM pushback to the revision move

- *"The hedonic still looks like sorting."* → Add the boundary-discontinuity or amenity-shock specification to the main text; show parallel pre-trends in price; report the estimate is unchanged.
- *"Your standard errors ignore spatial correlation."* → Report Conley SEs at multiple cutoffs in the main results table, not an appendix; note the CI still excludes zero.
- *"The welfare number is overstated."* → Re-bound the claim (marginal not total, local not external, PE not GE); restate the policy implication within the bound.
- *"Leakage / reshuffling could flip your sign."* → Add the leakage analysis (uncovered-source response, coverage share) and show the net welfare conclusion survives.
- *"The contingent-valuation result has no scope test."* → Add or surface the scope test and a hypothetical-bias calibration; report adjusted WTP.
- *"This is weather, not climate."* → Separate the short-run shock from the long-run expectation and add the adaptation discussion; restate which estimand the headline number is.

## Worked vignette (illustrative)

A reject-and-resubmit on a cap-and-trade paper: R1 (methods) wants the permit-price endogeneity addressed; R2 (policy) wants the distributional incidence; the editor flags leakage as the binding concern. The plan: route the endogeneity to `jeem-identification` (instrument the cap with a legislated schedule), add a leakage bound to `jeem-robustness` (uncovered-source emissions response), and add an incidence table via `jeem-tables-figures`. The response letter leads each point with the new exhibit number and states that the net welfare gain falls from $X to $0.8X once leakage is netted out but stays positive — conceding the magnitude while defending the conclusion.

## Track the changes for the editor

A revision that the editor cannot verify quickly invites another round. Provide a clearly marked diff or a changes-highlighted manuscript alongside the clean version, and make every response point to a specific, locatable change (section, table, figure number). For new analyses, state the result inline in the letter so the editor sees the answer without hunting through the paper. The goal is to let a busy editor confirm in one read that each demand was met — that confirmability, as much as the analysis itself, is what converts an R&R into an acceptance.

## Anti-patterns

- Answering referees while ignoring the editor's stated priorities
- A response that argues in prose but never shows the new number or exhibit
- Promising analysis in the letter without putting it in the revised paper
- Dismissing a wrong referee without evidence (the editor sides with the referee by default)
- Leaving two referees' conflicting demands unreconciled for the editor to untangle
- Re-asserting an overreaching welfare claim the referees already flagged

## Calibrating expectations for the JEEM review cycle

JEEM reviews can be slow and instruments more than one round of revision is common; plan for it rather than treating the first R&R as the last word. Three practical calibrations: (1) a "major revision" that asks for new identification work is a genuine invitation, not a soft reject — invest in it. (2) A "reject and resubmit" is treated as a fresh submission and may incur the fee again (待核实) — confirm before resubmitting, and make the new version substantially stronger, not cosmetically changed. (3) If a referee's demand would turn the paper into a different (e.g., methods-only) contribution, raise it with the editor rather than silently complying — the editor protects the paper's core welfare claim and can adjudicate scope creep.

## Output format

```text
【Journal】Journal of Environmental Economics and Management
【Skill】jeem-rebuttal
【Editor priority】the core demand from the editor's letter
【Triage】must-do: ___ | do-well: ___ | decline-with-evidence: ___
【New analysis routed to】jeem-robustness / jeem-identification / jeem-theory-model / jeem-tables-figures
【Referee reconciliation】how R1 and R2 are both served
【Welfare claim】re-bounded where challenged? [Y/N]
【Source status】verified URL / 待核实 / not asserted
【Next skill】loop to the routed analysis skill, then jeem-submission for the resubmission
```
