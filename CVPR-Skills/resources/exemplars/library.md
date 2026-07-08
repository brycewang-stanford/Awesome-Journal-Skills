# CVPR Exemplars Library (contribution type × era)

> **Verified via web search against CVF open access, dblp, and proceedings metadata,
> access date 2026-07-08.** Every row below was checked to have appeared at **CVPR
> specifically** (IEEE/CVF Conference on Computer Vision and Pattern Recognition), not a
> sibling venue. Direct fetches of `openaccess.thecvf.com` were blocked in the
> verification environment, so confirmation used search renderings of the open-access
> paper pages plus dblp records; re-open the URLs before citing details.
>
> **Sibling-confusion guard:** the most famous vision papers scatter across CVPR's
> siblings, and misattributing them in a CVPR submission's related-work section is a
> credibility wound. See the do-not-misattribute list at the bottom — several
> "obviously CVPR" papers are not CVPR papers.
>
> **Zero-hallucination rule:** this file records positioning lessons only. It does not
> restate results, exact numbers, or architectural detail from memory — read the paper
> on CVF open access before citing anything beyond the metadata here.

---

## How to use this library

These five papers span CVPR's main contribution types — recognition backbone, real-time
system, data structure, dataset, and generative method. Pick the row matching your
contribution type and study *how the first page earns the claim*: each of these leads
with a mechanism, proves it on the benchmarks of its day, and shipped artifacts the
field could build on — the pattern `cvpr-topic-selection`, `cvpr-writing-style`, and
`cvpr-experiments` teach.

## Verified exemplars

### Recognition backbone (architecture as contribution)

- **He, Zhang, Ren & Sun, "Deep Residual Learning for Image Recognition," CVPR 2016,
  pp. 770–778.** Verified: CVF open access (`content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html`).
  - **Positioning lesson:** one mechanism (the residual connection), one enabling claim
    (depth becomes trainable), then evidence at every scale the community cared about.
    The contribution sentence survives being read alone.
  - **Self-check:** can your architecture claim be stated as a *trainability or
    capability* change, not a leaderboard delta?

### Real-time system (speed/accuracy frontier as contribution)

- **Redmon, Divvala, Girshick & Farhadi, "You Only Look Once: Unified, Real-Time Object
  Detection," CVPR 2016, pp. 779–788.** Verified: dblp `conf/cvpr/RedmonDGF16` and CVF
  open access.
  - **Positioning lesson:** reframes the task (detection as single regression) and buys
    a new operating point — the paper claims the *frontier*, not the metric maximum,
    and names its accuracy costs. A model for efficiency claims aligned with what the
    modern Compute Reporting Form asks you to substantiate.
  - **Self-check:** is your speed claim tied to named hardware and an accuracy
    trade-off you state yourself?

### Data-structure method (new input regime)

- **Qi, Su, Mo & Guibas, "PointNet: Deep Learning on Point Sets for 3D Classification
  and Segmentation," CVPR 2017, pp. 652–660.** Verified: CVF open access
  (`content_cvpr_2017/html/Qi_PointNet_Deep_Learning_CVPR_2017_paper.html`).
  - **Positioning lesson:** the contribution is *consuming a data structure natively*
    (unordered point sets) with an invariance argument, opening a subfield rather than
    winning one benchmark.
  - **Self-check:** does your method claim rest on a property (invariance, geometry)
    you can both argue and ablate?

### Dataset as contribution

- **Deng, Dong, Socher, Li, Li & Fei-Fei, "ImageNet: A Large-Scale Hierarchical Image
  Database," CVPR 2009, pp. 248–255.** Verified: dblp `conf/cvpr/DengDSLL009`.
  - **Positioning lesson:** the dataset paper argues *what new science the resource
    enables*, with structure (the hierarchy) as the intellectual contribution, not the
    byte count. Note the modern policy edge: a CVPR dataset contribution must now be
    public by camera-ready (verified 2026 rule).
  - **Self-check:** does your dataset unlock a question, or only enlarge an answer?

### Generative method (compute-realistic synthesis)

- **Rombach, Blattmann, Lorenz, Esser & Ommer, "High-Resolution Image Synthesis with
  Latent Diffusion Models," CVPR 2022 (New Orleans).** Verified: CVF open access CVPR
  2022 listing and dblp.
  - **Positioning lesson:** the claim is *where computation happens* (a learned latent
    space), sold as a democratization of a compute-bound method class — an efficiency
    argument and a quality argument kept explicitly separate.
  - **Self-check:** if your generative result depends on scale, does the paper separate
    the method's contribution from the compute's?

## Coverage matrix

| Contribution type | Exemplar | Year | Anchor |
| --- | --- | --- | --- |
| Backbone / architecture | Deep Residual Learning | 2016 | pp. 770–778 |
| Real-time system | You Only Look Once | 2016 | pp. 779–788 |
| New input regime | PointNet | 2017 | pp. 652–660 |
| Dataset / benchmark | ImageNet | 2009 | pp. 248–255 |
| Generative method | Latent Diffusion Models | 2022 | CVF open access, CVPR 2022 |

## Do not misattribute to CVPR (verified elsewhere)

- **NeRF** (Mildenhall et al.) — **ECCV 2020**, not CVPR.
- **Mask R-CNN** (He et al.) — **ICCV 2017**, not CVPR.
- **Segment Anything** (Kirillov et al.) — **ICCV 2023**, not CVPR.
- **ViT / "An Image is Worth 16x16 Words"** (Dosovitskiy et al.) — **ICLR 2021**.
- **CLIP** (Radford et al.) — **ICML 2021**.
- **U-Net** (Ronneberger et al.) — **MICCAI 2015**.
- **DDPM** (Ho et al.) — **NeurIPS 2020**.

Before adding any row, confirm the paper on `openaccess.thecvf.com` (the CVPR-year
index page names the venue) or via a dblp `conf/cvpr/...` key, record authors, year,
and pages, and update the access-date header. Cite the proceedings version, not the
arXiv preprint, once one exists. If verification is unavailable, add the candidate as
**待核实 with no venue attribution** rather than guessing.
