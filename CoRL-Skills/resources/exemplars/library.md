# CoRL Exemplar Library

Access date: 2026-07-08. Every entry below was verified against a PMLR volume
page or an equivalently authoritative record on that date; the verification
recipe at the end shows how to add entries without importing citation errors.

Use these papers to calibrate what "learning is the contribution AND the claim
needs a robot" looks like in accepted form — and to benchmark evaluation scale,
limitations honesty, and artifact practice against work this community has
already endorsed.

## Verified exemplars

### 1. A System for General In-Hand Object Re-Orientation (CoRL 2021 — Best Paper)

- Tao Chen, Jie Xu, Pulkit Agrawal. PMLR 164:297–307 (note: PMLR year 2022,
  conference year 2021 — the year-offset trap in the wild).
- URL: https://proceedings.mlr.press/v164/chen22a.html
- Why it is an exemplar: a model-free RL system reorienting 2,000+ geometrically
  distinct objects, hand facing up **and down**, with zero-shot transfer to new
  objects — evaluation breadth as the headline, not a single lucky task.
- Study for: scaling an evaluation axis (object diversity) until the claim
  becomes statistical rather than anecdotal.

### 2. Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (CoRL 2022)

- Ahn et al. (SayCan). PMLR 205:287–318.
- Volume page: https://proceedings.mlr.press/v205/
- Why: the canonical "LLM meets robot" routing datapoint — the language model
  was not the contribution; grounding its plans in learned affordance/value
  functions on a mobile manipulator was, which is why it lived at CoRL and not
  at an NLP venue.
- Study for: drawing the learned-vs-pretrained-vs-engineered boundary clearly,
  and evaluating long-horizon tasks on real hardware at scale.

### 3. RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (CoRL 2023)

- Zitkovich et al. PMLR 229:2165–2183.
- Volume page: https://proceedings.mlr.press/v229/
- Why: defined the VLA framing that now dominates the field — web-scale
  vision-language pretraining expressed directly as robot actions, with
  emergent-generalization evaluations (novel objects, symbols, reasoning).
- Study for: designing generalization splits that measure what "web knowledge
  transfer" means physically, instead of gesturing at it.

### 4. OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)

- Kim et al. PMLR volume 270 (Munich cycle; page numbers 待核实).
- Volume page: https://proceedings.mlr.press/v270/
- Why: the open-weights counterpart to the closed VLA wave — artifact release
  (weights, code, fine-tuning recipes) as a first-class contribution the
  community could actually adopt as a baseline.
- Study for: `corl-artifact-evaluation` in practice; what a release looks like
  when the artifact is meant to become infrastructure.

### 5. Visual Imitation Enables Contextual Humanoid Control (CoRL 2025 — Best Student Paper)

- Arthur Allshire, Hongsuk Choi, Junyi Zhang, David McAllister, et al.
  PMLR 305:794–815.
- URL: https://proceedings.mlr.press/v305/allshire25a.html
- Why: the real-to-sim-to-real pipeline (VideoMimic) — everyday videos of humans
  reconstructed jointly with their environments, distilled into a single
  whole-body humanoid policy handling stairs, chairs, and terrain from
  environment + root commands.
- Study for: pipeline papers — how to evaluate each stage *and* the end-to-end
  claim, and how to present dynamic whole-body results honestly on video.

### 6. AnyPlace: Learning Generalizable Object Placement for Robot Manipulation (CoRL 2025)

- Zhao et al. PMLR volume 305.
- URL: https://proceedings.mlr.press/v305/zhao25b.html
- Why: a non-award companion datapoint from the same volume — task-family
  breadth (placement across object/receptacle variation) at normal-paper scale;
  useful for calibrating the *typical* accepted bar, not just the award bar.

## Cross-venue confusion guards

- **Diffusion Policy** and the ALOHA/ACT line are **RSS** papers, not CoRL —
  frequently misattributed because they are standard CoRL baselines.
- RT-**1** (the predecessor of RT-2) was also published at **RSS**; only RT-2 is
  the CoRL entry. Check before citing the pair.
- PMLR hosts many venues; a `proceedings.mlr.press` URL alone does not imply
  CoRL. Volume anchors verified for this pack: v78 = 2017, v164 = 2021,
  v205 = 2022, v229 = 2023, v270 = 2024, v305 = 2025.
- The CoRL 2025 **Best Paper** (as opposed to Best Student Paper) was reported
  in organizer/social sources as the "UniFP" loco-manipulation work; its exact
  title and PMLR record were not pinned down on 2026-07-08 — 待核实 before
  citing it as an award anchor.

## Self-check questions when benchmarking against an exemplar

1. Where does my evaluation breadth (tasks × objects × seeds × episodes) sit
   relative to the exemplar closest to my claim type?
2. Does my paper draw its learned/engineered boundary as legibly as SayCan?
3. If my contribution is an artifact, does my release plan match the OpenVLA
   pattern (weights + recipes + adoption path), or just "code on request"?
4. Would my video survive the comparison with a best-paper video — uncut runs,
   failures shown, speeds labeled?

## Verification recipe for adding entries

1. Locate the paper on its PMLR volume page (`proceedings.mlr.press/vNNN/`);
   record volume, pages, and the exact author list from that page — not from a
   citation manager or a lab website.
2. Confirm the volume ↔ edition mapping against the volume's front matter
   ("Proceedings of the Nth Conference on Robot Learning, <city>, <dates>").
3. Note both years when they differ (conference vs PMLR publication) — see
   `../../skills/corl-related-work/SKILL.md`.
4. For award claims, require an official awards page or organizer statement with
   URL and access date; social-media congratulations alone earn a 待核实 tag.
5. Record the access date next to the entry, as done above.
