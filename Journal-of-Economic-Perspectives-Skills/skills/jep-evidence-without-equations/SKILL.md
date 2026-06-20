---
name: jep-evidence-without-equations
description: Use when presenting empirical or theoretical evidence credibly in a Journal of Economic Perspectives (JEP) article with minimal math — intuition, examples, well-chosen numbers, and honest caveats. Handles how evidence is conveyed in prose; defer figures/tables to jep-exhibits-for-general-readers and fairness across studies to jep-balance-and-objectivity.
---

# Evidence Without Equations (jep-evidence-without-equations)

## When to trigger

- You need to convince a reader of a finding without a regression table in the body
- The draft leans on "significant at the 1% level" or coefficient dumps to make its case
- You have many numbers and aren't sure which few to feature
- You worry that going light on math will make the evidence look soft

## The JEP evidence bar

JEP communicates evidence through **intuition, well-chosen numbers, and honest caveats**, not through equations and estimation tables in the body. The credibility comes from *which* evidence you feature, *how clearly* you convey magnitude, and *how honestly* you state limits — not from displaying machinery. A JEP reader should finish a paragraph knowing the *size* of an effect, *how sure* the field is, and *what could be wrong*.

## How to present evidence credibly with little math

- **Lead with magnitude in plain units.** "Roughly a third of the cost is passed through to prices" beats a coefficient. Translate elasticities/log points into amounts a reader feels (dollars, percentage points, days).
- **Pick a few load-bearing numbers.** Two or three vivid, well-sourced figures land; a wall of estimates does not. Each featured number should earn its place in the argument.
- **Convey precision plainly.** Instead of asterisks, say how settled it is: "estimates cluster between 5% and 8%," or "studies disagree, ranging from near zero to large." Give the reader a sense of the *range*, not a star.
- **Use examples and analogies.** A concrete case or a familiar analogy makes a mechanism stick where a model would not.
- **Characterize the body of evidence, not one study.** "A dozen studies across countries find…" is more JEP than "Smith (2019) estimates…". Synthesis means describing the *weight* and *consistency* of evidence.
- **State caveats in the same breath.** "This holds for short horizons; over decades the evidence thins" builds trust and is the JEP norm.

## Honesty devices (build credibility without machinery)

- **Name the identification in words, once.** A reader should know *why* a number is believable (a natural experiment, a long literature, a clean comparison) without seeing the design.
- **Distinguish settled from contested.** Tell the reader what is consensus, what is debated, and what is unknown — this is also the bridge to `jep-balance-and-objectivity`.
- **Flag external validity.** Say where a result travels and where it likely doesn't.
- **Avoid false precision.** "About 6%" is more honest than "6.23%" when the range is wide.
- **Anchor with a benchmark.** A number means more next to a familiar reference point: "about the size of a typical recession's effect on employment," or "roughly a month's rent." Benchmarks let a non-specialist judge whether an effect is big or small.

## Checklist

- [ ] Effect sizes given in plain, feelable units (not raw coefficients)
- [ ] Only a few load-bearing numbers featured, each well-sourced
- [ ] Precision conveyed as ranges / degree of agreement, never asterisks
- [ ] Evidence characterized as a *body* (weight, consistency), not one study
- [ ] Identification/credibility explained in words, once, not displayed
- [ ] Caveats and external-validity limits stated alongside the claims
- [ ] Key magnitudes anchored against a familiar benchmark
- [ ] No false precision; magnitudes rounded to what the evidence supports

## Worked vignette (illustrative)

A draft says: "The treatment effect is 0.184 log points (s.e. 0.061), significant at the 1% level (***)." A JEP rewrite drops the asterisks and the raw coefficient: "Workers in the program earned about **20% more** a year later — an effect large enough to matter for a household budget, and one that **a dozen studies in different settings find consistently**, though the gains **fade after a few years**." The reader now has magnitude in feelable units, a sense of how settled it is (many consistent studies), and the key caveat (fading) — all without an equation or a star.

## Anti-patterns

- A regression table or estimating equation in the body to "prove" a point
- "Significant at the 1% level" (and asterisks) standing in for magnitude and precision
- A blizzard of numbers with no hierarchy — the reader can't tell which matter
- Citing a single study as if it settled a question (synthesis means weighing many)
- Hiding caveats to make the evidence look stronger (a balance and an honesty failure)
- False precision ("6.23%") that overstates how much the field actually knows

## Output format

```
【Headline magnitude (plain units)】[...]
【Load-bearing numbers (≤3)】1) … 2) … 3) … (sources)
【Precision conveyed as】[range / degree of agreement]
【Why believable (in words)】[natural experiment / long literature / clean comparison]
【Caveats + external validity】[...]
【Body of evidence framed?】many studies vs. one: [Y/N]
【Next step】jep-exhibits-for-general-readers
```
