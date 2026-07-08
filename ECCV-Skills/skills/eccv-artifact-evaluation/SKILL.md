---
name: eccv-artifact-evaluation
description: Use when packaging code, models, and data around an ECCV paper — the anonymous review-time archive under the trailing supplement deadline, the do-not-cite-your-own-repo rule, and the June-to-September post-acceptance runway for a public release aligned with the ECVA and Springer copies of the paper.
---

# ECCV Artifact Evaluation

Use this for artifact strategy at ECCV, which has no badge-granting artifact
track: artifacts live in two phases with opposite rules. Before decisions,
code is a **sealed, anonymous supplement**; after the June decision, it
becomes a **public release with a ten-week runway** before the September
conference makes the paper visible to the whole field.

## Phase 1 — sealed archive (review time)

- Upload with the supplement by the trailing deadline (March 12 in 2026,
  one week after the paper).
- The submission text must not link to the authors' public repository even
  if it already exists — ECCV 2026 policy treated that as an anonymity
  break, while arXiv posting itself was fine.
- Assume one reviewer opens the archive for ten minutes. Optimize for that
  reader: a README that maps each main-table row to a command, pinned
  dependencies, and one tiny demo input that runs on CPU.
- Scrub the usual vision-stack leaks: wandb entity names in configs,
  dataset paths containing lab or cluster names, git history, notebook
  metadata, license headers with author names, model cards naming the group.

## What vision reviewers actually probe

| Artifact | Probe | Failure they report |
|---|---|---|
| Inference code + checkpoint | Run the demo image | Output does not resemble the paper's qualitative figures |
| Training configs | Diff against the paper's Sec. 4 numbers | Config hyperparameters contradict the text |
| Evaluation script | Check the metric implementation | Nonstandard IoU/FID variant silently inflates scores |
| Data tooling | Check preprocessing + splits | Test-set contamination via cropping or dedup choices |

The metric-implementation row is the highest-yield check to run on yourself:
vision metrics have venue-standard reference implementations, and a rebuttal
cannot repair a nonstandard one discovered in review.

## Phase 2 — the ten-week release runway

The 2026 calendar gave accepted authors June 17 (decisions) to roughly
mid-August (ECVA/Springer open-access copies appear ~4 weeks pre-conference)
to ship the release the paper's readers will find:

1. Week 1–2: de-anonymize the sealed archive; make the repo the camera-ready
   URL points to, not a placeholder.
2. Week 3–5: release checkpoints with hashes, licences chosen deliberately
   (the Springer copyright covers the paper, not your code or weights —
   pick code and model licences yourself).
3. Week 6–8: project page linking arXiv, the upcoming ECVA page, data cards,
   and a results table that matches the camera-ready exactly.
4. Week 9–10: freeze; conference week issues should be answered from a
   stable main branch, because Malmö attendees will clone it during the
   poster session.

## Dataset and benchmark releases

If the contribution *is* a dataset or benchmark, plan hosting that outlives
the conference cycle: institutional or community storage rather than a
personal drive link, versioned splits, a datasheet, and licence terms
compatible with the source imagery. A benchmark whose test server or
download link dies before the next even-year ECCV is a citation dead end.

```bash
# minimal release self-check before announcing
git clone <public-url> fresh && cd fresh
pip install -r requirements.txt          # pinned, resolvable
python demo.py --input assets/demo.jpg   # CPU-runnable smoke test
python eval.py --split val --ckpt <hash> # reproduces one paper row
```

## Output format

```text
[Phase] sealed-supplement / release-runway / post-conference
[Anonymity scrub] <leaks found in configs, paths, metadata, history>
[Reviewer-probe risks] <metric impl / config-text mismatch / demo gap>
[Release plan] <repo, checkpoints, licences, hosting, freeze date>
[Paper-artifact consistency] <camera-ready row -> reproducing command>
```
