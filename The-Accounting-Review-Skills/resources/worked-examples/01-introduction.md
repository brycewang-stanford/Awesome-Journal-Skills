> **Illustrative teaching example.** The paper, setting, firms, and every number below are **fictional**
> and exist only to demonstrate *The Accounting Review* (TAR) house style. No real-paper facts are
> stated, and **no journal policy is invented** — policy claims are limited to what this pack's own
> skills already say. Corresponding skills:
> [`tar-writing-style`](../../skills/tar-writing-style/SKILL.md),
> [`tar-contribution-framing`](../../skills/tar-contribution-framing/SKILL.md),
> [`tar-topic-selection`](../../skills/tar-topic-selection/SKILL.md),
> [`tar-theory-development`](../../skills/tar-theory-development/SKILL.md),
> [`tar-literature-positioning`](../../skills/tar-literature-positioning/SKILL.md), and
> [`tar-methods`](../../skills/tar-methods/SKILL.md).

# Worked Example: A TAR-Style Introduction (before → after)

This demonstrates the **TAR archival-introduction arc** that the skills require: within the first page
or two, state **the question, the setting/identification, the finding, and the contribution** —
result first, written for an accounting reader, with an explicit accounting construct doing the
theoretical work (`tar-writing-style`, `tar-contribution-framing`, `tar-topic-selection`). The
mechanism rests on a **named friction and channel** (`tar-theory-development`), the paper is
**positioned in a live accounting conversation** rather than gap-spotting (`tar-literature-positioning`),
and the **identifying variation is named and defended** (`tar-methods`).

**Illustrative paper (fictional):** *"Mandatory Disclosure of Cyber-Incident Materiality and the Cost
of Debt: Evidence from a Staggered State Breach-Notification Regime."* Fictional setting: 23 U.S.
states adopted, in different years, a rule requiring firms headquartered there to disclose the
*materiality assessment* behind a data-breach incident in their financial reports. The focal
accounting construct is **disclosure of a materiality assessment**; the outcome is the **cost of debt**.

---

## Before (buries the result — typical first-draft intro)

> Cybersecurity has become an important topic for firms, regulators, and investors. A large
> literature in accounting and finance has examined disclosure and its consequences. In this paper, we
> use a staggered difference-in-differences design with the Callaway and Sant'Anna (2021) estimator to
> study the effect of breach-notification regulation on firms. We assemble a panel of Compustat firms
> matched to loan data and estimate event-study specifications with firm and year fixed effects. In our
> earlier work we documented disclosure effects, and we extend that analysis here to a new setting and
> a larger, more recent sample. Cyber risk is clearly material to debt investors, so understanding
> disclosure in this area is valuable. Section 2 reviews the literature, Section 3 describes the data,
> Section 4 presents the research design, Section 5 reports results, and Section 6 concludes.

**What's wrong (against the TAR skills):**

- **Buried lede** — no question, no finding, no contribution on page one; the reader cannot tell what
  was found by the end of the page (`tar-writing-style` anti-pattern "buried lede").
- **Leads with the estimator** ("we use a Callaway and Sant'Anna design") instead of the accounting
  question; method is demoted to a tool in TAR's archival arc (`tar-methods`).
- **Gap-spotting / database extension** — "extend … to a new setting and a larger, more recent sample"
  is the named incremental-extension red flag in `tar-literature-positioning`; the contribution
  sentence could be written before seeing the results.
- **No friction, no channel** — "disclosure relates to outcomes" with no economic mechanism; a
  `tar-theory-development` anti-pattern ("mechanical prediction," "borrowed friction").
- **Self-identifying prose** — "In our earlier work we documented" breaks double-blind anonymization;
  `tar-writing-style` requires third-person self-citation.
- **Throat-clearing** ("has become an important topic," "is clearly valuable") that burns the 55-page
  budget without stating stakes.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (TAR arc — question + setting/identification + finding + contribution, result first)

> **Does requiring firms to disclose *how* they judged a cyber-incident to be material — not merely
> that a breach occurred — lower their cost of debt?** We find that mandated disclosure of the
> materiality assessment reduces the spread on new bank loans by **18 basis points** (off a sample mean
> of 214 bps), concentrated in firms whose breaches were ex ante hardest for lenders to assess.
> *(question + headline finding with units, on page one.)*
>
> The accounting construct doing the work is the **disclosed materiality assessment**, not the breach
> event itself: lenders already learn of large breaches from the press, but they cannot observe
> management's private judgment of expected loss, remediation cost, and exposure. The friction is
> **information asymmetry over loss severity**; the channel is **debt pricing** — a credible, audited
> materiality narrative narrows the lender's posterior variance over the firm's contingent losses, so
> the lender prices less of an uncertainty premium. *(named friction → channel → outcome, per
> `tar-theory-development`; the accounting construct, not a generic finance variable, drives the
> theory, per `tar-topic-selection`.)*
>
> Identifying this effect is hard because firms that disclose more about cyber risk differ from those
> that do not in exactly the ways that also move loan spreads. We exploit a staggered regulatory
> setting: **23 states adopted a materiality-disclosure mandate in different years**, applying to firms
> headquartered there for reasons unrelated to any single firm's credit quality. We compare treated
> firms to not-yet-treated firms, verify **no differential pre-trends** in loan spreads before a
> firm's state adopts, and report dynamic effects that emerge only after adoption. *(identifying
> variation named and defended; pre-trends stated plainly, per `tar-methods`.)*
>
> Our contribution is to show that **the disclosed reasoning behind a materiality judgment is itself
> priced, separately from the underlying event** — a margin prior work could not isolate, because it
> measured *whether* firms disclosed breaches rather than *how* they justified materiality. This
> reconciles the mixed evidence on whether cyber disclosure matters to creditors: it matters where it
> resolves assessment uncertainty, and not otherwise. *(contribution stated as a new answer to a
> disputed question, relative to a specific prior view, per `tar-contribution-framing` and
> `tar-literature-positioning`.)* We document an **association we interpret cautiously as causal** under
> the staggered design, bounded to U.S. public firms with rated bank debt over the sample period; we do
> not claim the result extends to equity pricing or to firms without a comparable disclosure mandate.
> *(causal language calibrated to the identification; boundary conditions stated, per
> `tar-contribution-framing`.)*
>
> The paper proceeds as follows. Section 2 develops the assessment-uncertainty mechanism and
> predictions; Section 3 describes the staggered setting, data, and design; Section 4 reports the
> pricing results and the cross-sectional tests of the channel. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the TAR bar

Mapped to the skill checklists:

- **Result first, on page 1** — the question, the identifying setting, the finding (18 bps, with
  units), and the contribution all appear within the opening, satisfying `tar-writing-style`'s "the
  finding and contribution are stated on the first page or two" and retiring the **buried-lede**
  anti-pattern.
- **Accounting construct drives the theory** — the priced object is the *disclosed materiality
  assessment*, a disclosure construct, not the stock/loan price itself; this clears `tar-topic-selection`
  gate 1 (accounting-centered, not "finance in disguise").
- **Named friction and channel** — information asymmetry over loss severity → debt-pricing channel,
  not a mechanical "disclosure relates to spreads"; satisfies `tar-theory-development` and avoids its
  "borrowed friction" anti-pattern.
- **Problematization, not gap-spotting** — the paper *reconciles mixed prior evidence* on whether
  cyber disclosure matters to creditors rather than asserting "no one has studied X"; this is the
  strong move in `tar-literature-positioning`.
- **Identification named and defended** — staggered state adoption, not-yet-treated comparison,
  explicit no-pre-trends and dynamic effects; matches `tar-methods` and avoids "leading with the
  estimator" and "TWFE on staggered adoption."
- **Claim calibrated to evidence** — "interpret cautiously as causal," with stated boundary conditions
  (U.S. public firms, rated bank debt, sample period), per `tar-contribution-framing`'s causal
  calibration; no policy overreach.
- **Anonymized prose** — the self-citation is third-person, not "in our earlier work," per
  `tar-writing-style`'s anonymization rule.

> **On the abstract (not shown above):** the companion abstract for this paper must be **≤ 150 words**
> and concrete about question, setting, finding, and contribution, with the **AI disclosure statement**
> placed after it — both per `tar-writing-style`. The introduction above front-loads exactly the four
> elements that abstract must compress.

> Next: see [`../code/`](../code/) for the staggered-DiD command chain referenced above. For venue limits
> (page budget, abstract length, Chicago style, data/code regime) defer to this pack's
> [`../official-source-map.md`](../official-source-map.md) — not to this teaching file.
