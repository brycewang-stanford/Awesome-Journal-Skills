---
name: en-natsci-journal-workflow
description: Use when deciding which English natural-science / clinical / physical / formal-science journal skill to invoke next, comparing fit across the 100-journal natural-science roadmap, or routing a manuscript before venue-specific re-framing.
---

# English natural-science journal workflow (en-natsci-journal-workflow)

## Purpose

This is the routing skill. It does not replace a single-journal profile; it first
classifies the manuscript by **discipline, advance type, evidence shape, and
audience breadth**, then routes into the matching per-journal skill for fit and
re-framing. It is a sibling to `en-journal-workflow`, which covers the
econ / finance / management 100.

## Resources to Load When Needed

- If the target family is unclear, read `../../resources/worked-examples/venue-routing.md`
  before choosing a venue.
- If a manuscript sits between broad and specialist venues, read
  `../../resources/exemplars/selection-patterns.md`.
- Before submission-ready advice, use `../../resources/journal-roster.md` and
  `../../resources/official-source-map.md` to open the current official author
  instructions for the chosen journal.

## Ask four things first

1. **Advance type:** a single broadly-significant discovery, a mechanism, a new
   method/tool, a definitive clinical result, a theoretical/mathematical result,
   or an authoritative review/synthesis?
2. **Evidence shape:** molecular/mechanistic experiment, in vivo / animal model,
   human clinical trial or cohort, observational/field data, simulation/theory,
   structure determination, benchmark/algorithm, or proof?
3. **Audience breadth:** all of science (Nature/Science/PNAS), a whole discipline
   (Nature-subject / society flagship), or a specialty community?
4. **Submission goal:** swing for a general-science or flagship venue, or optimize
   topic–venue fit and review odds at a strong specialty journal?

## Quick routing

| Manuscript signature | Prefer skill |
|---|---|
| Single advance significant to *all* science | `nature` / `science` / `pnas` |
| Solid complete advance, broad but not flagship | `nature-communications` / `science-advances` / `national-science-review` / `the-innovation` |
| Complete mechanistic molecular story | `cell` / `molecular-cell` / `nature-cell-biology` / `the-embo-journal` |
| Genetics / genomics / functional genomics | `nature-genetics` / `genome-biology` / `nucleic-acids-research` |
| New method / tool / platform | `nature-methods` / `nature-biotechnology` |
| Stem cell / cancer biology / metabolism | `cell-stem-cell` / `cancer-cell` / `cell-metabolism` / `developmental-cell` |
| Immunology mechanism | `immunity` / `nature-immunology` / `science-immunology` / `journal-of-experimental-medicine` |
| Microbiology / host–microbe / microbiome | `nature-microbiology` / `cell-host-and-microbe` |
| Neuroscience / human behaviour | `neuron` / `nature-neuroscience` / `nature-human-behaviour` / `molecular-psychiatry` |
| Ecology / evolution / plant | `nature-ecology-and-evolution` / `ecology-letters` / `molecular-biology-and-evolution` / `the-plant-cell` / `nature-plants`→`the-plant-cell` |
| Open-access general biology | `elife` / `plos-biology` / `current-biology` |
| Practice-changing clinical trial, general medicine | `nejm` / `the-lancet` / `jama` / `the-bmj` / `annals-of-internal-medicine` |
| Translational mechanism-to-bedside | `nature-medicine` / `science-translational-medicine` / `journal-of-clinical-investigation` |
| Oncology (clinical / translational) | `journal-of-clinical-oncology` / `the-lancet-oncology` / `cancer-discovery` / `annals-of-oncology`→`journal-of-clinical-oncology` |
| Cardiology | `circulation` / `journal-of-the-american-college-of-cardiology` / `european-heart-journal` |
| GI / hematology / ID / neurology / diabetes | `gastroenterology` / `gut` / `blood` / `the-lancet-infectious-diseases` / `the-lancet-neurology` / `diabetes-care` |
| Public-health / OA medicine | `plos-medicine` / `the-bmj` |
| Physics Letter, broad + immediate | `physical-review-letters` / `physical-review-x` |
| Condensed matter / particles-gravitation | `physical-review-b` / `physical-review-d` |
| Physics conceptual advance / photonics / quantum | `nature-physics` / `nature-photonics` / `prx-quantum` |
| Authoritative physics review | `reviews-of-modern-physics` / `reports-on-progress-in-physics` |
| Astronomy / astrophysics | `nature-astronomy` / `the-astrophysical-journal` / `monthly-notices-of-the-royal-astronomical-society` |
| Broad chemistry, significant + general | `journal-of-the-american-chemical-society` / `angewandte-chemie-international-edition` / `nature-chemistry` |
| Catalysis / nano / Cell-Press chemistry | `nature-catalysis` / `acs-nano` / `nature-nanotechnology` / `chem` |
| Authoritative chemistry review | `chemical-reviews` / `chemical-society-reviews` / `accounts-of-chemical-research` |
| Materials / energy | `nature-materials` / `advanced-materials` / `nature-energy` / `joule` / `energy-and-environmental-science` |
| Earth / climate / sustainability / environment | `nature-geoscience` / `nature-climate-change` / `nature-sustainability` / `one-earth` / `environmental-science-and-technology` |
| AI/ML / robotics / CV methods | `nature-machine-intelligence` / `science-robotics` / `ieee-transactions-on-pattern-analysis-and-machine-intelligence` / `journal-of-machine-learning-research` |
| Pure mathematics, top result | `annals-of-mathematics` / `inventiones-mathematicae` / `journal-of-the-american-mathematical-society` |

## Sibling-Journal Disambiguation

| Confusable targets | Decision rule |
|---|---|
| Nature/Science/Cell/PNAS vs specialist venues | Use broad venues only when the advance changes a field-wide model or practice; completeness alone is not enough. |
| NEJM/Lancet/JAMA/BMJ vs specialty clinical venues | General medicine needs practice-changing clinical evidence; disease-area nuance often belongs in specialty journals. |
| JACS/Angewandte/Nature Chemistry vs ACS Catalysis/materials venues | Decide whether the central advance is molecular chemistry, catalysis mechanism, or materials/device performance. |
| PRL/Nature Physics/Physical Review family | Route by immediacy and conceptual physics breadth, then by subfield and article format. |
| Mathematics vs physics vs CS | Theorem, physical insight, and algorithmic benchmark are different products; pick the reviewer community that evaluates the main claim. |

## Decision rules

- **Significance before submission.** Nature/Science/Cell/PNAS triage most papers
  before review on "broad significance." If the advance is solid but incremental,
  route to the strong specialty or open-access multidisciplinary venue rather than
  burning a flagship desk-reject.
- **"First to report X" is not a contribution** at flagship venues — name the
  conceptual advance, the mechanism, or the definitive evidence.
- **Descriptive ≠ mechanistic.** A correlation, an omics catalogue, or a structure
  with no functional insight routes below Cell/Nature-subject; add mechanism or
  route to a data-resource venue.
- **Clinical evidence hierarchy.** A practice-changing randomized trial belongs at
  NEJM/Lancet/JAMA; an observational cohort or secondary analysis usually routes to
  a society specialty journal. Trial registration + the right reporting checklist
  (CONSORT/PRISMA/STROBE) are prerequisites, not nice-to-haves.
- **Review vs. primary.** Reviews of Modern Physics, Chemical Reviews, Accounts of
  Chemical Research, CA, and Trends are largely *invited* — do not route an
  unsolicited primary-data paper there.
- **Format gates.** A PRL must fit the Letter length limit; a Nature/Cell paper
  must survive editorial triage; an eLife paper enters the Reviewed-Preprint model.
- Always enter the single-journal skill's official-submission checklist before
  submitting; never rely on a stale template.

## Output format

```text
[Top journal skill] <skill-name>
[Alt 1] <skill-name> (reason)
[Alt 2] <skill-name> (reason)
[Do not submit to] <journal> (one-line mismatch reason)
[Biggest current gap] significance / mechanism / evidence / reporting-checklist / formatting / official requirements
[Next step] invoke <skill-name> for single-venue fit and re-framing
```
