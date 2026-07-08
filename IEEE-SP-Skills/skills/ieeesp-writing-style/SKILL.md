---
name: ieeesp-writing-style
description: Use when writing or revising an IEEE S&P (Oakland) paper's prose, including the threat-model-first structure, calibrating security claims to evaluated boundaries, the first-round survival test for introductions, SoK voice, and fitting the argument into 13 compsoc pages.
---

# IEEE S&P Writing Style

Use this for drafting and revision passes. The controlling constraint is
S&P's round structure: first-round reviewers cut papers **without a
rebuttal** (`ieeesp-review-process`), so the paper's first two pages must
survive a professional skeptic reading alone, unaided, and slightly tired.

## The first-round survival test

By the end of page 2, a reviewer must be able to answer:

1. **Who is the adversary?** Capabilities, access, and what winning means.
2. **What is the claim?** One sentence, bounded: "we show an attacker with
   <access> can <effect> on <target class>, demonstrated on <n> systems."
3. **What is the evidence?** The map: which section demonstrates, which
   measures, which proves.
4. **Why now / why hard?** What made this un-done until this paper.
5. **Was it done responsibly?** One early signal — disclosure initiated,
   IRB obtained — expanded later.

A draft that spends page 1 on the importance of cybersecurity fails this
test; Oakland reviewers assume importance and grade specificity.

## Threat model as a load-bearing section

The threat model is not scene-setting — every later claim is evaluated
against it:

- State capabilities **and** non-capabilities ("the attacker cannot observe
  physical access patterns"); reviewers probe boundaries you leave implicit.
- Justify realism with citations to incidents or measurements, not
  intuition.
- Keep one threat model. Papers that quietly strengthen the adversary in
  §5 to make the defense interesting get caught in reviewer discussion.
- For defenses: state the adaptive adversary — one who knows the design —
  and point to where that adversary is evaluated.

## Claim calibration table

| Overclaim | Calibrated form |
|---|---|
| "Our defense stops X attacks" | "blocks all X instances in our corpus (n=…); adaptive variants in §6.3" |
| "The first work to…" | "the first *demonstration on production systems* of…" (and verify) |
| "Devastating real-world impact" | measured impact + affected-population estimate + fix status |
| "Provably secure" | "secure under <model> against <adversary class> (Thm 2)" |
| "Negligible overhead" | "<n>% median overhead on <workload> (Fig 7)" |

The pattern: every security adjective is replaced by a boundary plus a
pointer. This is also rebuttal insurance — calibrated claims leave less for
reviewers to dispute.

## SoK voice is a different register

An `SoK:` paper argues a *thesis about the literature*: the organizing claim
("defenses in this area implicitly assume X, and the assumption fails")
appears on page 1 like any other claim, the taxonomy is the evidence, and
the systematization must earn its verbs — *compare*, *reconcile*,
*invalidate* — not just *survey*. Per the CFP, value to the community is the
review criterion; a section explicitly stating what practitioners and
researchers should do differently is the strongest close.

## Compression for 13 compsoc pages

Two-column IEEE compsoc punishes sprawl. Cuts that preserve the argument,
in order:

1. Background that a security-generalist PC member already knows (they know
   what ASLR is; they need your bypass's delta).
2. Repeated attack-flow narration — one figure with a numbered walkthrough
   replaces a page of prose.
3. Per-experiment methodology boilerplate — one Evaluation Setup subsection,
   referenced thereafter.
4. Defensive hedging paragraphs — one Limitations subsection beats hedges
   scattered through every section.

```text
Revision pass, one command per pass:
pass 1: page-2 test — answers to the 5 questions all present? mark gaps
pass 2: grep -n "first\|novel\|significant\|devastating\|completely" body.tex
        → each hit: boundary + pointer, or delete
pass 3: threat-model diff — list every capability §4–§7 assumes;
        confirm each appears in §2
pass 4: read only topic sentences aloud — does the argument survive?
```

## House conventions worth matching

- Present tense for the system and attack ("the attack proceeds in three
  stages"); past tense for what you measured.
- Third-person self-citation everywhere in the anonymous version.
- Numbered attack stages and named components; reviewers reference "stage 2"
  and "the monitor" in discussion — make that easy.
- Figures readable in grayscale at print size; compsoc columns are narrow.

## Output format

```text
[Page-2 test] adversary ✓/✗ · claim ✓/✗ · evidence map ✓/✗ · why-now ✓/✗ · ethics signal ✓/✗
[Threat model] boundaries explicit? drift across sections? <findings>
[Claim audit] <n> uncalibrated claims with locations>
[Compression] current <n> pp → 13 pp plan: <cut list in order>
[Register] research / SoK — voice matches? <note>
```
