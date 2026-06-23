---
name: en-agrienv-journal-workflow
description: Use when deciding which English agriculture / environment / earth-science journal skill to invoke next, comparing fit across the 30-journal agriculture-and-environment roadmap, or routing a manuscript before venue-specific re-framing. Routes by sub-field (agronomy / plant / soil / food / environment / earth / climate), contribution type, and evidence shape (field trial / lab assay / observational survey / model / dataset).
---

# Agriculture & environment journal workflow (en-agrienv-journal-workflow)

## Purpose

This is the routing skill for the agriculture-and-environment bundle. It does not
replace a single-journal profile; it first classifies the manuscript by **sub-field,
contribution type, and evidence shape**, then routes into the matching per-journal
skill for fit and re-framing. It is a sibling to `en-natsci-journal-workflow`
(natural science) and `en-engtech-journal-workflow` (engineering).

## Ask four things first

1. **Sub-field:** crop/agronomy, plant biology, soil science, food science,
   ecosystem/environmental science, pollution/health, climate/atmosphere, hydrology/water,
   ocean/limnology, or solid-earth geoscience?
2. **Contribution type:** a mechanism, a field/management result, a synthesis/review,
   a model or projection, a new dataset/data product, or a methods/measurement advance?
3. **Evidence shape:** controlled field trial, glasshouse/lab assay, observational or
   monitoring survey, remote sensing, long-term record, process/earth-system model, or
   a documented public dataset?
4. **Audience breadth:** broad significance (a Nature Portfolio title), a whole
   sub-field (a society flagship), or a specialist community?

## Pre-routing evidence gates

Before naming a journal, classify the manuscript through these gates. A weak gate
does not always mean "do not submit"; it usually means route down to a specialist
venue, reframe the claim, or fix the evidence before testing a higher-prestige
venue.

| Gate | Pass signal | If weak |
|---|---|---|
| Contribution | A mechanism, management implication, method, projection, or dataset that transfers beyond the study site | Reframe as a local case study, technical note, or specialist-field result |
| Evidence strength | Replicated sites/seasons/systems, transparent uncertainty, and controls matched to the claim | Do not route to broad Nature/society flagships; strengthen replication first |
| Scale match | Claim scale matches the evidence scale: plot, field, landscape, regional, global, or dataset | Narrow the title/abstract and select a venue that accepts the actual scale |
| Data/code readiness | Data, code, model configuration, and metadata can be deposited or shared under field norms | Treat deposition as a blocker for ESSD, earth-system, hydrology, and reuse claims |
| Compliance | Permits, ethics, biosafety, field-site permissions, and competing-interest disclosures are known | Pause final routing until the single-journal checklist can verify requirements |

## Evidence-shape escalation

- **Single site-year field trial:** usually specialist agronomy/crop venue; do not
  pitch as general food-security evidence without multi-site or mechanistic support.
- **Multi-site or multi-season field trial:** can support field flagship routing if
  management implications and uncertainty are explicit.
- **Lab/glasshouse mechanism:** plant or soil mechanism venues; needs field or
  ecological validation before claiming landscape or management impact.
- **Remote sensing / monitoring survey:** route by validation and generalizability;
  benchmark against independent observations and document processing code.
- **Process or earth-system model:** route by the model contribution, sensitivity
  analysis, and reproducibility package, not only by the application region.
- **Dataset/data product:** `earth-system-science-data` only when the dataset itself
  is the product, has persistent identifiers, rich metadata, and a public archive.

## Quick routing

| Manuscript signature | Prefer skill |
|---|---|
| Food-systems advance with broad significance | `nature-food` |
| Plant-science advance, broad and high-impact | `nature-plants` |
| Fundamental plant biology / physiology / ecology | `new-phytologist` / `the-plant-journal` |
| Authoritative plant-biology review | `annual-review-of-plant-biology` |
| Crop yield, agronomy, cropping-system field research | `field-crops-research` / `agronomy-for-sustainable-development` |
| Agroecosystem nutrient/GHG/biodiversity at field-to-landscape scale | `agriculture-ecosystems-and-environment` |
| Soil biology, biogeochemistry, soil carbon/microbiome | `soil-biology-and-biochemistry` |
| Food chemistry / composition / safety | `food-chemistry` |
| Food-technology trends and synthesis | `trends-in-food-science-and-technology` |
| Climate-change impacts on ecosystems/biota | `global-change-biology` |
| Human-exposure environmental health | `environment-international` / `environmental-health-perspectives` |
| Sustainability, circular economy, cleaner production | `journal-of-cleaner-production` / `resources-conservation-and-recycling` |
| Authoritative environment & resources review | `annual-review-of-environment-and-resources` |
| Environmental contamination / ecotoxicology | `environmental-pollution` |
| Broad earth/environment advance, OA | `communications-earth-and-environment` |
| Climate dynamics / variability | `journal-of-climate` |
| New, documented public dataset | `earth-system-science-data` |
| Catchment / surface / groundwater hydrology | `journal-of-hydrology` / `water-resources-research` |
| Solid-earth, geochemistry, planetary-scale processes | `earth-and-planetary-science-letters` / `geology` |
| Carbon/nutrient cycling, biogeochemistry | `global-biogeochemical-cycles` |
| Land–atmosphere flux / agro-meteorology | `agricultural-and-forest-meteorology` |
| Forest ecology and management | `forest-ecology-and-management` |
| Aquatic / freshwater / ocean ecology and limnology | `limnology-and-oceanography` |
| Meteorological-society review / community article | `bulletin-of-the-american-meteorological-society` |

## Sibling-journal disambiguation

| Confusable targets | Decision rule |
|---|---|
| `nature-food` vs `field-crops-research` | Nature Food wants food-systems significance and transdisciplinary reach; FCR wants a rigorous crop/agronomy field result. |
| `new-phytologist` vs `the-plant-journal` | New Phytologist favors plant ecology/physiology/interactions breadth; The Plant Journal favors molecular/cellular plant biology with mechanism. Re-check current scopes. |
| `journal-of-hydrology` vs `water-resources-research` | WRR (AGU) favors fundamental water-science methodology/theory; Journal of Hydrology spans process, observational, and applied hydrology more broadly. |
| `agriculture-ecosystems-and-environment` vs `soil-biology-and-biochemistry` | AEE emphasizes field-to-landscape agroecosystem outcomes; SBB emphasizes soil-process mechanism and soil biota. |
| `global-change-biology` vs `agriculture-ecosystems-and-environment` | GCB needs a global-change framing and biological response; AEE needs an agroecosystem-management framing. |
| Nature Portfolio (`nature-food`/`nature-plants`/`communications-earth-and-environment`) vs society flagships | Nature titles need broad significance and framing; a complete sub-field result routes to the society/specialist journal. |
| `earth-system-science-data` vs an analysis journal | ESSD is for the dataset itself (documented, publicly deposited with a DOI); the scientific analysis of that data belongs in an analysis journal. |
| `environment-international` / `environmental-health-perspectives` vs pollution journals | Human-exposure or health-risk inference routes to the health journals; contaminant behavior, remediation, or ecotoxicology routes to the pollution/environmental-process venues. |
| `journal-of-climate` vs `agricultural-and-forest-meteorology` | Climate dynamics and variability route to Journal of Climate; land-atmosphere fluxes, crop/forest microclimate, and agro-meteorological applications route to AFM. |
| `global-biogeochemical-cycles` vs `global-change-biology` | Element cycles, fluxes, and earth-system budgets route to GBC; organismal, ecosystem, or biological responses to global change route to GCB. |
| `resources-conservation-and-recycling` vs `journal-of-cleaner-production` | Circular-material-flow and recycling systems route to RCR; cleaner production, industrial sustainability, and management interventions route to JCP. |

## Decision rules

- **Name the advance, not the site.** "We measured X at our site" is not a
  contribution unless it yields a generalizable mechanism, management result,
  projection, or dataset.
- **Field evidence discipline.** Field/observational claims need adequate replication,
  controls, and uncertainty; a single site-year or unreplicated trial is a common reject
  at the agronomy and ecology venues.
- **Data deposition is a gate, not a nicety.** Earth-science and environmental venues
  increasingly mandate FAIR data/code deposition; data journals (ESSD) require the public
  dataset itself. Sort this before submission.
- **Review vs. primary.** Annual Review titles and the synthesis-leaning venues are
  largely invited/scoped — do not route an unsolicited primary-data paper there without
  checking scope.
- **Scale and framing.** Plot/lab, field, landscape, regional, and global results route
  to different venues; match the claim's scale to the journal's audience.
- **Health, policy, and management claims need the right endpoint.** Do not route
  a contaminant-detection paper as environmental health unless exposure/outcome
  inference is actually measured; do not route a sustainability paper as policy unless
  a decision, intervention, or system boundary is specified.
- Always enter the single-journal skill's official-submission checklist before
  submitting; never rely on a stale template.

## Handoff protocol

After routing, hand off only the minimum needed context to the single-journal skill:

- the strongest claim the evidence can honestly support;
- the rejected broader claim, if any, and why it was narrowed;
- the evidence shape and weakest gate from the table above;
- the one official requirement most likely to block submission;
- the alternative venue to keep warm if the first-choice fit fails.

## Output format

```text
[Top journal skill] <skill-name>
[Alt 1] <skill-name> (reason)
[Alt 2] <skill-name> (reason)
[Do not submit to] <journal> (one-line mismatch reason)
[Evidence gates] contribution / evidence-strength / scale / deposition / compliance: pass|watch|block
[Biggest current gap] significance / field-evidence / replication / data-deposition / scale-framing / official requirements
[Claim to narrow] <claim, or none>
[Next step] invoke <skill-name> for single-venue fit and re-framing
```
