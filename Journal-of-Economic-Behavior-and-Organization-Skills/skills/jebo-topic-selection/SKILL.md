---
name: jebo-topic-selection
description: Use when deciding whether a behavioral, experimental, or organizational question fits the Journal of Economic Behavior & Organization (JEBO) rather than a sibling outlet, and how to frame it. Sharpens scope and the behavioral hook; it does not invent evidence, editors, or citations.
---

# Topic Selection (jebo-topic-selection)

## When to trigger

- You have a clean result but are unsure whether JEBO or a sibling (Experimental Economics, GEB, J. Economic Psychology, J. Public Economics) is the right home
- The paper is a good causal study but the **behavioral** angle is thin or bolted on
- A coauthor asks "is this behavioral enough for JEBO?"
- The question is interesting but the audience that would cite it is unclear

## What JEBO actually rewards

JEBO's organizing idea is **economic behavior outside the frictionless, fully-rational benchmark**: bounded rationality, social and other-regarding preferences, heuristics and biases, learning and adaptation, institutions and organizations as responses to behavioral constraints. A JEBO paper leads with a **behavioral mechanism** and uses whatever method (experiment, empirics, theory, simulation) best identifies it. The test is not "is the design clean?" but "does this teach us something about how real economic agents actually decide and organize?"

Run the topic through three filters, in order:

1. **Behavioral content.** Is there a genuine deviation from the rational-actor benchmark — a preference, belief, heuristic, or institutional response — that the paper measures or models? If the behavioral element is decorative ("we add a behavioral interpretation in the discussion"), the paper belongs elsewhere.
2. **Generality of the lesson.** JEBO is broad but not a field journal for one micro-topic. The mechanism should travel beyond the specific lab task or one dataset.
3. **Method-fit, not method-purity.** JEBO is pluralist; the method is judged by how well it serves the behavioral question, not by whether it is the most fashionable estimator.

## Sibling boundary — where JEBO ends and others begin

| If the paper's real contribution is… | Better home than JEBO | Why |
|--------------------------------------|-----------------------|-----|
| A new experimental method / design (deception detection, elicitation tool) for its own sake | Experimental Economics | ESA outlet is method-of-experiment-focused; JEBO wants the behavioral economics the experiment reveals |
| A theorem about equilibrium, learning dynamics, or mechanism design | Games and Economic Behavior | GEB is formal game theory; JEBO theory must yield a *testable behavioral* prediction |
| A psychology-first account (affect, personality, cognition) with light economic stakes | Journal of Economic Psychology | JEBO keeps an economic decision/organization at the center |
| A clean policy-evaluation number where the behavioral story is secondary | AEJ: Applied / J. Public Economics | those reward the causal estimand; JEBO rewards the mechanism behind it |
| A management/strategy contribution to organizational theory | Management Science / AMJ | JEBO's "organization" is economic, behaviorally micro-founded |

If two filters pass and the boundary table keeps the paper at JEBO, the topic fits. If only one passes, the paper is *adjacent* — reframe around the behavioral mechanism or redirect.

## Framing the hook

State the contribution as: **"agents do X (a behavioral regularity) because of Y (mechanism), with consequence Z for markets/organizations/institutions."** That sentence should survive deletion of the dataset name — if the paper collapses to "we ran an RCT and found an effect," the behavioral hook is missing.

## Checklist

- [ ] The behavioral mechanism (preference / belief / heuristic / institutional response) is named in one sentence, not implied
- [ ] The lesson generalizes beyond the single task, sample, or institution studied
- [ ] The method is justified by the question, not by fashion (experiment, empirics, theory, or simulation all welcome)
- [ ] The sibling-boundary table places the paper at JEBO, not at ExpEcon / GEB / JEP / a policy journal
- [ ] No fabricated editor, fee, or word limit; volatile facts marked 待核实

## Anti-patterns

- A clean causal study with a behavioral interpretation tacked on in the conclusion (desk-reject risk: "right method, wrong journal")
- A pure experimental-method or pure game-theory contribution sent to JEBO because it "involves behavior"
- A single-task lab result with no argument that the mechanism travels
- Pitching to "the JEBO audience" generically without naming which segment (behavioral, experimental, organizational, evolutionary) would cite it
- Claiming a process fact (e.g., "JEBO requires pre-registration") that the source map does not verify

## Output format

```text
【Journal】Journal of Economic Behavior & Organization
【Skill】jebo-topic-selection
【Behavioral hook】agents do X because of Y, with consequence Z
【Archetype】experiment / observational / theory / simulation
【Fit verdict】fits JEBO / adjacent — reframe / redirect to <sibling>
【Sibling boundary】why not ExpEcon / GEB / JEP / policy journal
【Source status】verified / 待核实 / not asserted
【Next skill】jebo-literature-positioning
```
