---
name: jleo-writing-style
description: Use when the prose, introduction, or abstract of a Journal of Law, Economics, and Organization (JLEO) manuscript needs to land its institutional/organizational contribution for an OUP economics-of-institutions audience. Sharpens framing and exposition; it does not change the analysis or the model.
---

# Writing Style (jleo-writing-style)

## When to trigger

- The introduction explains what was done before it says what institutional question is answered and why it matters
- The abstract reads like a methods summary, not a claim about how an institution or organization works
- A reader from the TCE/PPE community cannot tell in the first page which conversation the paper joins
- The model and empirics are settled but the prose still buries the mechanism under notation or data description
- The paper is written in JLE price-theory voice or Org-Science behavioral voice rather than the institutional-economics register

## The JLEO voice

JLEO prose is the prose of institutional and organizational economics: it leads with an **institutional puzzle**, names the **mechanism**, and frames the contribution for readers steeped in Coase, Williamson, North, and Hart. Write the introduction last, after the model and identification settle, and make it do this work in order:

1. **Open on the institutional puzzle, not the data.** The first paragraph should pose the governance/organizational/political question — why does this institution take this form, or what does this governance choice do — in terms the field recognizes. Not "We use administrative data on X."
2. **Name the mechanism early.** By the end of the second paragraph the reader should know the institutional mechanism (transaction-cost economizing, residual control, credible commitment, agency) that the paper is about.
3. **State the contribution as a delta on a named frontier.** "Relative to [the TCE / PPE literature], we show ___." Place the paper on its frontier explicitly (see jleo-literature-positioning).
4. **Preview the design or the model honestly.** One paragraph on what identifies the effect or what the model assumes — enough that a skeptic sees the credibility before the results.
5. **Keep the institutional interpretation visible throughout.** Each results paragraph should restate what the number means for the institution, not just report a coefficient.

## Register discipline

| Drift to avoid | JLEO register |
|----------------|---------------|
| Pure applied-micro "we estimate the effect of X on Y" | "We show how [governance form / institution] economizes on / fails to economize on ___" |
| JLE price-theory framing (market efficiency as the payoff) | Institutional/organizational form as the payoff |
| Org-Science behavioral language (culture, identity, sensemaking) | Economics of organization (incentives, contracts, transaction costs) |
| Theory paper that never names a real institution | Mechanism anchored to a recognizable institution |
| Buried mechanism under data description | Mechanism named on page one |

## Checklist

- [ ] The introduction opens on the institutional puzzle, not the data or method
- [ ] The institutional mechanism is named within the first two paragraphs
- [ ] The contribution is stated as a delta on a named JLEO frontier (TCE / firm-theory / PPE)
- [ ] The identification or the model's core assumption is previewed before the results
- [ ] Every results paragraph restates the institutional meaning of the number
- [ ] The register is economics-of-institutions, not JLE price-theory or Org-Science behavioral
- [ ] The abstract states a claim about how an institution/organization works, not a methods recap

## Anti-patterns

- An introduction that spends its first page on data and estimator before the institutional question appears
- An abstract that lists methods and a coefficient but never says what it means for governance/institutions
- Coasean/Williamsonian vocabulary used as decoration over an applied-micro paper with no institutional payoff
- Results prose that reports coefficients without translating them back into the institutional claim
- Polishing the intro before the model and identification are stable (rewrites waste effort)

## Worked vignette (illustrative)

A draft opens: "We use a panel of 12,000 procurement contracts and a difference-in-differences design to estimate the effect of contract duration on disputes." A JLEO rewrite opens on the puzzle: "Public buyers routinely sign long, sole-source contracts that sacrifice competition — a choice that looks inefficient unless quality is non-contractible. We show that this governance form economizes on transaction costs precisely where relationship-specific investment is high." The mechanism (transaction-cost economizing under non-contractibility) is on page one; the data and design come second.

## Output format

```text
【Opening】institutional puzzle stated first? [Y/N]
【Mechanism named by para 2】TCE / agency / commitment / residual-control: ___
【Contribution as delta】on which frontier: ___
【Design/model previewed before results】[Y/N]
【Institutional interpretation in results prose】[Y/N]
【Register】economics-of-institutions (not JLE / Org-Science)? [Y/N]
【Next skill】jleo-replication-package
```
