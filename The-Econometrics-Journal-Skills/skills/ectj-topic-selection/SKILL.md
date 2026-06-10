---
name: ectj-topic-selection
description: Use when deciding whether an econometrics paper fits The Econometrics Journal's leading-case, applied-value bar rather than Journal of Econometrics, Econometric Theory, Quantitative Economics, Review of Economics and Statistics, or a field journal.
---

# EctJ Topic Selection

Use this before drafting. EctJ is not a generic repository for any econometric technique; it
asks for original econometrics with direct or potential applied value and a leading-case
contribution.

## Fit test

- Prefer EctJ when the paper gives a path-breaking or leading-case method, estimator, test,
  identification result, or applied-econometrics design that can travel beyond one narrow
  dataset.
- Require an empirical application even for theory papers; do not treat Monte Carlo evidence
  as a substitute for applied relevance.
- Route to Econometric Theory if the contribution is almost entirely formal and needs longer
  theorem development.
- Route to Journal of Econometrics if the paper is broader, longer, or more exhaustive than
  EctJ's compact format supports.
- Route to a field journal if the econometric novelty is mainly a tool for a substantive
  economics result.

## Borderline routing rules

- Choose **EctJ** when the contribution is a sharp method with direct applied value and can be taught as a
  leading case within the compact format.
- Choose **Econometric Theory** when the proof architecture, generality, or theorem development is the main
  contribution and needs more formal space.
- Choose **Journal of Econometrics** when the contribution is broad, exhaustive, or method-family defining
  rather than a focused leading case.
- Choose a **field journal** when the economic result matters more than the method, and the method would be
  a technical appendix elsewhere.

If the application can be removed without changing the paper's value, EctJ fit is weak. If the theorem can
be removed without changing the paper's value, EctJ fit is also weak.

## Shape of an accepted EctJ methods paper

Calibration anchors, hedged where practice varies: the modal accepted structure is a compact
chain — motivation through an econometric failure, the leading-case theory, a Monte Carlo section
summarized within about a page of main text, and an empirical illustration that changes a real
decision — inside the roughly 20-page printed format, with full grids and secondary material in
the online appendix where the rules permit. Papers that allocate half their pages to a literature
survey or to institutional background do not match the venue's shape even when technically strong.
For early-career authors, the Royal Economic Society's Denis Sargan Econometric Prize, awarded for
the best EctJ article by a young author, is one more signal that the venue wants sharp
leading-case work rather than encyclopedic treatments.

## Worked fit scoring

Vignette (illustrative): a paper derives an estimator for staggered-adoption designs when
untreated potential outcomes follow an unobserved factor structure.

- Leading case: two factors, balanced panel — sharp and teachable. EctJ-positive.
- Applied value: re-estimates a published minimum-wage application and reverses one headline
  conclusion (illustrative: the pooled effect changes sign at the 10% level). EctJ-positive.
- Empirical application: present and diagnostic, not decorative. EctJ-positive.
- Length pressure: full proofs need 30 printed pages. EctJ-negative — either restructure the
  proofs for the printed appendix or route to a longer-format econometrics journal.

Three positives and one repairable negative reads as possible EctJ with compression to fix first,
not as a venue switch.

## Scope traps specific to this venue

- A method whose applied value exists only in one proprietary dataset fails the travel test; the
  EctJ application should be reproducible under the replication policy, so a public or accessible
  dataset materially raises fit.
- Topics already exhaustively treated in long-format econometrics journals fit only if the paper
  finds a genuinely new leading case, not a cleaner exposition.
- Machine-learning-assisted econometrics fits when the economic parameter and its inference
  guarantees are the contribution; a prediction-accuracy paper without an econometric object
  belongs in an ML venue.
- Pure comparison or replication studies are usually off-shape here; the venue asks for original
  methodology with demonstrated use.

## Output format

```text
[Fit] strong EctJ / possible EctJ / better elsewhere
[Leading case] <methodological or applied-econometrics advance>
[Applied value] <empirical domain and why it matters>
[Routing risk] <too narrow, too theoretical, too empirical, too long>
[Next action] <theory, application, framing, or venue switch>
```
