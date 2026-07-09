# WACV Exemplars Library (track × contribution)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked
> against the **CVF open-access repository** (`openaccess.thecvf.com/content/WACV20XX/...`)
> and, where possible, **IEEE Xplore** and **dblp**, to confirm it actually appeared at the
> **IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)** — matching year,
> author list, and the WACV proceedings volume. Papers that could not be cleanly confirmed
> as **WACV** (as opposed to a CVPR/ICCV/ECCV sibling) were **omitted and documented
> below**. It is deliberately a short, verified list.
>
> **Sibling-confusion guard:** WACV is **not** CVPR, ICCV, or ECCV. Many famous
> vision papers live at those venues; a `thecvf.com` open-access URL is only proof of WACV
> if the path segment reads `WACV20XX`. Direct fetches of the CVF sites were blocked
> (HTTP 403) from the verification environment, so paths were confirmed through search
> renderings — reconfirm on the live open-access page before citing.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It
> does not reproduce or invent results, metrics, or table numbers — read the original on
> CVF open access or IEEE Xplore before citing anything. For WACV policy, scope, and the
> two-round model, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **track × contribution** is closest to yours, then study how that paper
frames its claim for the **track it was reviewed under** — an Applications-track paper that
leads with a real-world constraint and a systems result, or an Algorithms-track paper that
leads with a method and a matched-baseline comparison (see
[`../../skills/wacv-topic-selection/SKILL.md`](../../skills/wacv-topic-selection/SKILL.md),
[`../../skills/wacv-writing-style/SKILL.md`](../../skills/wacv-writing-style/SKILL.md), and
[`../../skills/wacv-experiments/SKILL.md`](../../skills/wacv-experiments/SKILL.md)). For
each, ask the self-check question before claiming your paper is "WACV-shaped."

---

## Verified WACV papers

### Diffusion-based image editing (Algorithms-leaning / method + geometry)

- **Sajnani, Vanbaar, Min, Katyal & Sridhar, "GeoDiffuser: Geometry-Based Image Editing
  with Diffusion Models," WACV 2025.**
  Verified: `openaccess.thecvf.com/content/WACV2025/html/Sajnani_GeoDiffuser_Geometry-Based_Image_Editing_with_Diffusion_Models_WACV_2025_paper.html`.
  Reported **Best Student Paper** (corroborated by a Brown CS news post; treat the award as
  reported, the placement as verified).
  - **Why it is an exemplar:** casts image-editing operations as **geometric transformations
    folded into the attention layers of a diffusion model**, delivering training-free edits
    — a clean, self-contained method contribution with a crisp mechanism, the kind Round 1
    reviewers can accept without asking for a revision.
  - **Self-check:** is your core idea stateable as one mechanism a reviewer can grasp on
    the first page, so it survives Round 1 rather than needing the Revise-and-Resubmit lap?

### Autonomous-driving perception, re-examined (Applications-leaning / benchmark + analysis)

- **Chodosh, Ramanan & Lucey, "Re-Evaluating LiDAR Scene Flow," WACV 2024.**
  Verified: `openaccess.thecvf.com/content/WACV2024/papers/Chodosh_Re-Evaluating_LiDAR_Scene_Flow_WACV_2024_paper.pdf`;
  IEEE Xplore `10484248`; arXiv `2304.02150`. (Award status reported, not confirmed.)
  - **Why it is an exemplar:** instead of a new architecture, it **audits how LiDAR scene
    flow is measured** and shows the standard evaluation rewards the wrong behavior — an
    applications-track contribution where the value is a corrected way to judge a
    real-world driving task, not a leaderboard number.
  - **Self-check:** does your applications paper improve how a deployed task is *evaluated
    or constrained*, with comparative assessment against real conditions, rather than only
    reporting a metric bump?

---

## By track (each cell is a verified WACV paper above)

| Track lean | Verified WACV exemplar | Year | Contribution type |
| --- | --- | --- | --- |
| Algorithms | Sajnani et al., "GeoDiffuser" | 2025 | Training-free diffusion editing via geometric attention |
| Applications | Chodosh, Ramanan & Lucey, "Re-Evaluating LiDAR Scene Flow" | 2024 | Re-evaluation of a driving-perception benchmark |

> Two first-party-verified papers spanning the two review lenses WACV actually uses. The
> pair illustrates the routing question in `wacv-topic-selection`: the same skills that
> reward a tight mechanism (GeoDiffuser) reward a corrected evaluation of a deployed task
> (LiDAR scene flow) — you must know which lens you are asking for.

---

## Omitted for lack of clean WACV verification (do not attribute to WACV without re-checking)

To keep the list zero-hallucination, several well-known "winter-CV-adjacent" papers were
**excluded** after checking, because their open-access path or dblp record placed them at a
**sibling venue**, not WACV:

- Papers whose CVF open-access path reads `CVPR20XX`, `ICCV20XX`, or `ECCV20XX` — a
  `thecvf.com` URL alone does not make a paper WACV; only the `WACV20XX` path segment does.
- WACV **workshop** best-paper items (e.g., GeoCV and other co-located workshops) — these
  are workshop, not main-conference, papers and must not be cited as WACV main-track.
- Any paper for which only an arXiv preprint could be found with no WACV proceedings
  record — a preprint is not proof of a WACV placement.

Before adding any new paper, confirm it on `openaccess.thecvf.com` by matching the
**`WACV20XX` path segment** to the WACV edition (and, ideally, the IEEE Xplore record),
then record author list, year, and the open-access URL, and update the access-date header.
When in doubt, omit. If web search is unavailable, add the row as **待核实 / TO VERIFY**
with **no attribution**.
