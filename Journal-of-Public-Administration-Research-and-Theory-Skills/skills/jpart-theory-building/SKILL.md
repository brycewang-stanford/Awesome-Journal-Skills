---
name: jpart-theory-building
description: Use when building the theoretical argument of a Journal of Public Administration Research and Theory (JPART) manuscript into a public-management contribution. JPART's defining demand is theory — its abstract template asks for the theoretical approach first and the implications for theory last. Structures the argument; it does not run analyses.
---

# Theory Building (jpart-theory-building)

At JPART a result is not a contribution until it is attached to **public-management theory the field can
use elsewhere.** The journal's own abstract template asks authors to state the **theoretical approach**
first and to end with **implications for theory** — that ordering is the whole brief. This skill turns
findings into theory: explicit constructs, mechanisms, scope conditions, and observable implications.

## When to trigger

- The empirics are strong but the "so what for theory" is thin
- A reviewer said the paper is "atheoretical," "ad hoc," or "a finding in search of a theory"
- You need to state the mechanism and scope conditions of a PA relationship explicitly
- You are deciding whether you *extend*, *test*, *bound*, or *overturn* an existing PA theory

## Build the argument

1. **Concept.** Define the key constructs precisely and distinguish them from neighbors — e.g., red tape
   vs. administrative burden, PSM vs. job satisfaction, passive vs. active representation. Measurement
   follows the concept (see `jpart-research-design`).
2. **Mechanism.** The causal story in public-management terms: which actors (street-level bureaucrats,
   managers, citizens, principals) do what, under which incentives, identities, motivations, or
   institutional constraints. A named mechanism is what makes the result portable.
3. **Observable implications.** What we should see if the mechanism operates — *and what we should not*.
   These become the tests in `jpart-research-design` and the conditions in the analysis.
4. **Scope conditions.** Where the theory holds and where it does not (sector, level of government,
   task type, regime). Public-management theory rarely travels unconditionally; say where it breaks.

## Theory contribution ledger

Before drafting, turn the theory section into a ledger. Each row must connect a public-administration
construct to a mechanism, a rival account, and a testable implication. If a row cannot be filled, the
paper is not ready to claim a JPART-level theory contribution.

| Ledger field | Strong entry | Weak entry |
|--------------|--------------|------------|
| Construct | "Administrative burden as learning, compliance, and psychological costs" | "Bureaucracy" |
| Mechanism | "Managers reduce discretion because error costs are politically visible" | "It affects behavior" |
| Rival account | "Observed effect is agency selection, not frontline discretion" | "Other factors" |
| Observable implication | "Effects concentrate where rule ambiguity is high and audit threat is salient" | "There should be an effect" |
| Scope boundary | "Applies to rule-bound service delivery, not emergency response" | "Generalizes broadly" |
| Theory payoff | "Bounds red-tape theory by enforcement visibility" | "Has implications" |

## Mechanism-to-evidence gate

Use the mechanism to decide what the empirical design must show. This prevents a theory section from
promising more than the design in `jpart-research-design` can support.

| Theory claim | Evidence needed before claiming it | Safer wording if evidence is weaker |
|--------------|------------------------------------|-------------------------------------|
| X causes Y through mechanism M | Identification for X -> Y plus evidence that M moves in the predicted direction | "The pattern is consistent with M" |
| The effect differs across public-sector settings | Pre-specified heterogeneity, adequate power, and measurement invariance | "Exploratory heterogeneity suggests..." |
| A theory fails outside boundary B | Direct comparison across inside/outside-boundary cases | "Boundary B is a plausible limit" |
| A mechanism travels across countries or sectors | Comparable constructs and institutional translation | "The mechanism may travel where..." |
| Qualitative evidence revises theory | Case-selection logic, process observations, and rival-mechanism checks | "The case elaborates a possible revision" |

## Rival-theory stress test

JPART reviewers often reject theory sections that merely attach a familiar theory label to a result.
Write the strongest rival theory in the same vocabulary as your own claim.

1. Name the rival: selection, common-method perception, political principal control, resource capacity,
   professional norms, citizen sorting, or a competing PA theory.
2. State its prediction in the same units as your mechanism.
3. Identify the one result, pattern, or qualitative observation that would distinguish the two.
4. If the manuscript cannot distinguish them, downgrade the claim from "shows" to "is consistent with"
   and make the rival a future-test agenda rather than hiding it.

## Theory moves JPART rewards

| Move | What it looks like | Example shape |
|------|--------------------|---------------|
| **Extend** | add a condition or actor to an existing theory | PSM matters, but only under low red tape |
| **Test** | bring a credible design to a claim long asserted | does passive representation become active under threat? |
| **Bound** | show where a theory fails | performance information shifts citizens — except for co-partisans |
| **Overturn** | replace a mechanism with a better one | the "effect" is selection, not motivation |

## The portability test (JPART-specific)

Ask: *Could a public-management scholar studying a different function, level, or country import this
mechanism?* If yes, you have a theory contribution. If it only works for your exact agency, tighten it
into a general public-management logic or reframe (back to `jpart-topic-selection`).

## Abstract-to-conclusion alignment

Because JPART asks the abstract to lead with theoretical approach and end with implications for theory,
the theory contract must be visible at both ends of the paper.

- Abstract opening: name the theory or construct, not only the setting or policy problem.
- Introduction: state the theory move and the rival account before previewing the estimate.
- Theory section: define constructs, mechanism, observable implications, and scope conditions in that order.
- Results section: label each test by the observable implication it adjudicates.
- Conclusion: return to what changes for public-administration theory, not only what managers should do.

## Anti-patterns

- "Hypothesizing after results are known" (HARKing) — state theory before tests; preregister where possible
- Constructs named but never distinguished from their neighbors (red tape ≈ burden, PSM ≈ satisfaction)
- A mechanism asserted but never made observable
- Universal claims with no scope conditions across sectors/levels of government
- Burying the theoretical payoff under the empirics — the abstract must lead with the theory approach

## Output format

```
【Core claim】one sentence (public-management theory)
【Construct(s)】defined + distinguished from neighbors
【Mechanism】the causal story (actors + incentives/identity/institutions)
【Observable implications】testable consequences → research-design
【Scope conditions】sector / level / task where it holds or fails
【Theory move】extend / test / bound / overturn
【Rival theory】strongest alternative + distinguishing evidence
【Evidence gate】claim strength supported / needs softer wording / redesign needed
【Abstract alignment】theoretical approach first + implications for theory last? [Y/N]
【Next】jpart-research-design
```

## Supplementary resources

- [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) — JPART theory papers (PSM, red tape, representation)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JPART abstract template (theory-first)
