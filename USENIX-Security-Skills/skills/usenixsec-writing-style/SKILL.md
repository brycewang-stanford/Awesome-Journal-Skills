---
name: usenixsec-writing-style
description: Use when drafting or revising prose for a USENIX Security Symposium paper — threat-model-first structure, calibrated security claims, disclosure narrative woven into the text, 13-page discipline in the USENIX template, and the plain systems-security register this program committee rewards.
---

# USENIX Security Writing Style

A USENIX Security paper argues like an engineer under oath: state what the
adversary can do, show what you built or broke, measure it honestly, and say
plainly what does not follow. The style advice here is calibrated to the '26 CFP's
format rules and to the venue's reviewing culture; format numbers are one cycle's
snapshot.

## Structure: the threat model is load-bearing

Readers at this venue locate every claim relative to an adversary. Put the threat
model early (typically Section 2 or 3), make it precise, and never let the
evaluation quietly assume a stronger or weaker attacker than the model granted:

- Name capabilities concretely: network position, code execution level, query
  budget, physical access, knowledge of the defense.
- Name non-goals just as concretely — "side channels are out of scope" is a
  legitimate sentence that prevents an entire review thread.
- For measurement papers, the analogue is the **vantage and validity statement**:
  where you measured from, when, and what the view cannot see.

A body plan that fits the 13 pages without heroics:

| Section | Budget | Job |
|---|---|---|
| Intro | 1–1.25 pp | Problem, adversary, contribution bullets with numbers |
| Background + threat model | 1.5–2 pp | Just enough context; precise adversary |
| Design / attack technique | 3–4 pp | The mechanism, end to end |
| Evaluation | 3.5–4.5 pp | Setup, headline results, adaptive/robustness analysis |
| Discussion + limitations | 0.75–1 pp | What breaks, what it costs, what's unknown |
| Related work | 0.75–1 pp | Positioning (see usenixsec-related-work) |

Then the two mandatory appendices, then references — geometry per
`usenixsec-supplementary`.

## Claim calibration, the house dialect

Security prose fails in two symmetric ways: marketing ("we completely prevent...")
and false modesty that buries a real result. The venue's fix is quantified
hedging — every strong verb carries its measurement:

```text
Weak:    Our defense stops code-reuse attacks with negligible overhead.
Better:  Against the 412 ROP chains in our corpus, the defense blocks all
         chains that pivot through heap pointers (387/412; the remaining 25
         use stack-only gadgets, Section 6.3) at a 2.1% median CPU overhead
         (max 4.8%) on SPEC CPU 2017.

Weak:    Attackers can trivially bypass existing scanners.
Better:  Eight of the eleven scanners we tested miss payloads transformed by
         our encoder; the three that detect it do so via rule R117, which
         also flags 4% of benign traffic in our enterprise trace.
```

Rules of thumb: numbers beat adverbs; populations beat anecdotes ("all 412" not
"attacks"); every "first" gets a scope ("first *automated* analysis of X at ISP
scale"); failure cases appear in the same paragraph as the success rate.

## The disclosure narrative belongs in the prose

Papers here often describe live harm potential. Beyond the mandatory Ethical
Considerations appendix, weave the responsible-conduct thread into the body where
the reader needs it: the scan methodology paragraph states the rate limits and
opt-out handling; the vulnerability section states "reported to the vendor on
<date>; patched in version Y" at the moment the flaw is introduced. Reviewers
should never wonder, mid-section, whether the experiment was run responsibly.

## Register and mechanics

- Plain systems English. Define acronyms once; this community tolerates jargon
  density but punishes ambiguity about *which* TEE/DOM/EL2 you mean.
- Present tense for the system and its properties; past tense for experiments run.
- Figures carry the argument in evaluation sections — a reviewer flipping pages
  should reconstruct the results story from captions alone.
- Name the system early and use the name consistently; anonymize any name that is
  publicly attached to your group at submission time.
- Unaltered USENIX LaTeX template; compression comes from cutting re-narration of
  tables and consolidating examples, never from spacing tricks (forbidden by CFP).

## Revision passes that pay at this venue

1. **Adversary-consistency pass**: every evaluation claim re-checked against the
   stated threat model.
2. **Calibration pass**: hunt "completely / trivially / negligible / guarantees"
   and attach numbers or delete.
3. **Cold-reader pass**: someone outside the subfield reads intro + threat model
   only, then writes down what they think the paper claims — mismatch means the
   framing leaks.
4. **Caption pass**: figures/tables self-contained, units and populations stated.

## Reverify each cycle

- Page budget and template version in the current CFP ('27 values 待核实).
- Any new style-adjacent mandates (AI-writing disclosure, reporting checklists).

## Output format

```text
[Threat model] section, precision verdict, evaluation-consistency check
[Calibration] flagged claims + rewrites
[Disclosure thread] present at point-of-need in body: yes / gaps
[Budget] per-section page usage vs plan; overflow routing
```
