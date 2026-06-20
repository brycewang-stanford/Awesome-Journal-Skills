# GCB Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked on Wiley Online
> Library (`onlinelibrary.wiley.com`) to confirm it actually appeared in *Global Change Biology* (GCB),
> with a GCB DOI (`10.1111/gcb...` or the legacy `10.1046/j.1365-2486...` / `10.1111/j.1365-2486...`
> prefix), and with author/year/volume confirmed. Papers lacking full GCB confirmation —
> or whose full citation was not cleanly confirmed — were **omitted and documented** below. This is
> deliberately a short, clean list (5 fully verified) rather than a long, uncertain one.
>
> **Sibling-confusion guard.** GCB is published by **Wiley** and is **not** any of these adjacent
> titles, which must never be cited as GCB: *Nature Climate Change*, *Global Ecology and Biogeography*,
> *Ecology*, *New Phytologist*, or *Global Change Biology Bioenergy* (a separate GCB-family journal).
> Several search hits for the queries below were in those siblings and were excluded.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does **not**
> reproduce or invent effect sizes, intervals, or specific findings — read the original on Wiley before
> citing any number. For GCB-specific policy, scope, and data/code rules, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes a
**driver → biological-response** link *mechanistic* and *broadly relevant* — the GCB bar (see
[`../../skills/gcb-topic-selection/SKILL.md`](../../skills/gcb-topic-selection/SKILL.md) and
[`../../skills/gcb-writing-style/SKILL.md`](../../skills/gcb-writing-style/SKILL.md)). For each, ask the
self-check question before claiming your paper is "GCB-shaped."

---

## By method

### Multi-model process simulation (DGVM ensemble; carbon–climate feedback)

- **Cramer, Bondeau, Woodward, Prentice, Betts, Brovkin, Cox, Fisher, Foley, Friend, Kucharik, Lomas,
  Ramankutty, Sitch, Smith, White & Young-Molling, "Global response of terrestrial ecosystem structure
  and function to CO2 and climate change: results from six dynamic global vegetation models," GCB 2001,
  7(4):357–373.**
  Verified: `onlinelibrary.wiley.com/doi/10.1046/j.1365-2486.2001.00383.x` (DOI
  10.1046/j.1365-2486.2001.00383.x).
  - **Why it is an exemplar:** an **ensemble** of six DGVMs, rather than a single run, turns scenario and
    structural uncertainty into the result itself — the canonical GCB "match scale and inference,
    prefer ensembles" modelling paper. Pairs with `gcb-study-design` (process-model family) and the
    DGVM/Earth-system toolchain in [`../external_tools.md`](../external_tools.md).
  - **Self-check:** does your model claim rest on an ensemble with structural/scenario uncertainty
    shown, not a single run reported as if it had none?

### Meta-analysis / evidence synthesis (manipulative-experiment synthesis)

- **Zhou, Zhou, Shao, Nie, He, Jiang, Wu & Hosseini Bai, "Interactive effects of global change factors
  on soil respiration and its components: a meta-analysis," GCB 2016, 22(9):3157–3169.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.1111/gcb.13253` (DOI 10.1111/gcb.13253).
  - **Why it is an exemplar:** synthesizes manipulative experiments to isolate **interactive** effects of
    multiple global-change drivers on a biogeochemical flux — a mechanism-resolving meta-analysis, not a
    vote count. Models the meta-analysis discipline in `gcb-data-analysis` (effect sizes, heterogeneity,
    moderators).
  - **Self-check:** does your synthesis resolve a *mechanism* (here, driver interaction on a flux), with
    pre-specified effect size, heterogeneity, and bias checks?

- **Wang, Quesada, Xia, Butterbach-Bahl, Goodale & Kiese, "Effects of climate warming on carbon fluxes
  in grasslands — A global meta-analysis," GCB 2019, 25(5):1839–1851.**
  Verified: `onlinelibrary.wiley.com/doi/10.1111/gcb.14603` (DOI 10.1111/gcb.14603).
  - **Why it is an exemplar:** a single global-change driver (experimental warming) synthesized across
    grassland sites to quantify a **carbon-flux** response — a clean driver→response synthesis with
    broad, cross-site relevance.
  - **Self-check:** can you state one driver, one response, and a quantified global effect size with an
    interval, across many sites rather than one?

### Trait-based meta-analysis (biodiversity redistribution)

- **MacLean & Beissinger, "Species' traits as predictors of range shifts under contemporary climate
  change: A review and meta-analysis," GCB 2017, 23(10):4094–4105.**
  Verified: `onlinelibrary.wiley.com/doi/10.1111/gcb.13736` (DOI 10.1111/gcb.13736).
  - **Why it is an exemplar:** asks *why* range shifts vary — using species' traits as moderators — turning
    a "that species move" observation into a **mechanistic, transferable** account of redistribution under
    warming.
  - **Self-check:** does your synthesis explain *variation* in a response with mechanistic moderators,
    rather than just confirm a direction everyone expects?

### Observational gradient / long-term phenology synthesis

- **Ge, Wang, Rutishauser & Dai, "Phenological response to climate change in China: a meta-analysis,"
  GCB 2015, 21(1):265–274.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.1111/gcb.12648` (DOI 10.1111/gcb.12648).
  - **Why it is an exemplar:** long observational phenological series across many taxa, synthesized into a
    coherent warming→phenology signal — a model of turning scattered observational records into a
    quantified global-change response while stating space-for-time and observational caveats
    (`gcb-study-design`).
  - **Self-check:** do your observational data support a *directional, quantified* response to a
    global-change driver, with confounders and space-for-time limits stated?

---

## By topic (each cell is a verified GCB paper above)

| Topic | Verified GCB exemplar | Year, vol(issue):pp | Method | DOI |
| --- | --- | --- | --- | --- |
| Carbon–climate feedback / vegetation dynamics | Cramer et al., "Six DGVMs" | 2001, 7(4):357–373 | DGVM ensemble (process model) | 10.1046/j.1365-2486.2001.00383.x |
| Soil respiration / biogeochemistry | Zhou et al., "Interactive effects on soil respiration" | 2016, 22(9):3157–3169 | Meta-analysis (multifactor) | 10.1111/gcb.13253 |
| Grassland carbon flux under warming | Wang et al., "Warming & grassland C fluxes" | 2019, 25(5):1839–1851 | Meta-analysis (warming) | 10.1111/gcb.14603 |
| Species range shifts / redistribution | MacLean & Beissinger, "Traits & range shifts" | 2017, 23(10):4094–4105 | Trait meta-analysis | 10.1111/gcb.13736 |
| Phenology under warming | Ge et al., "Phenology in China" | 2015, 21(1):265–274 | Observational meta-analysis | 10.1111/gcb.12648 |

---

## Omitted for lack of full verification (do not attribute to GCB without re-checking)

To keep the list zero-hallucination, these candidates were **excluded** after checking:

- **Norby et al., forest-FACE net-primary-productivity synthesis ("Forest response to elevated CO2 is
  conserved across a broad range of productivity," 2005)** — verified to be in the *Proceedings of the
  National Academy of Sciences* (PNAS), **not GCB**. A frequently-cited FACE landmark, listed here only
  as a guardrail against misattribution.
- **Burrows et al. marine "velocity of climate change" / poleward-shift work (2014)** — referenced
  widely in the GCB range-shift literature, but the specific paper's venue and full citation were not
  cleanly confirmed as GCB by web search (the velocity-of-climate-change paper appeared in *Science*;
  related work is dispersed across venues), so it is omitted pending re-check.
- **"Temperature change effects on marine fish range shifts: a meta-analysis" (DOI 10.1111/gcb.16770)** —
  appears to be a genuine GCB article, but its full author/year/volume citation was **not** cleanly
  confirmed in this pass, so it is held out rather than cited with a guessed attribution.

Before adding any new paper to this library: confirm it on `onlinelibrary.wiley.com` with a GCB DOI
(`10.1111/gcb...` or legacy `j.1365-2486...`) **and** confirm author/year/volume, check it is **not** a
sibling title (Nature Climate Change, Global Ecology and Biogeography, Ecology, New Phytologist, GCB
Bioenergy), and update the access-date header. When in doubt, omit.
