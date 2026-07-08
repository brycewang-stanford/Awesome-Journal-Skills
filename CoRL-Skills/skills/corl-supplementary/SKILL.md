---
name: corl-supplementary
description: Use when assembling CoRL supplementary material — the strongly encouraged overview video under the 250 MB cap and roughly three minutes, the optional appendix inside the same PDF that reviewers need not read, code and data attachments, and anonymization of everything, with the PMLR no-video rule shaping camera-ready plans.
---

# CoRL Supplementary Material

CoRL supplementary material splits into three channels with different rules and
different reader guarantees: the **appendix** (same PDF, optional reading), the
**supplementary upload** (files and the venue's signature overview video), and —
after acceptance — **external hosting**, because the PMLR proceedings pipeline
does not take videos at all. Content placed in the wrong channel either never
gets seen or violates a rule.

## Channel rules (2026 cycle, corl.org, read 2026-07-08)

| Channel | 2026 rule | Reader guarantee |
|---|---|---|
| Appendix | Optional; follows references in the same PDF; uncounted against the 8 pages | Reviewers are **not required** to read it |
| Supplementary file(s) | Encouraged for further details; video ≤ 250 MB (strict), ~3 min suggested | Also optional reading; must be anonymous |
| External links during review | Only if fully anonymous — the URL included | Assume most reviewers won't click |
| Camera-ready / PMLR | **No video as supplementary**; host video/code/data externally, link from the main text or a project page | Permanent record; plan durable hosting |

The uniform consequence of "optional reading": nothing decision-critical may live
outside the 8-page body. The body must stand alone; supplementary material
corroborates, it never carries.

## The video: evidence, not advertisement

For a learned-policy paper the video has a specific evidentiary job — showing
that printed success rates correspond to real behavior. Reviewers at this venue
watch with a checklist mindset:

- **Uncut executions.** At least a few complete episodes per headline task with
  no cuts inside an attempt; jump-cut montages are read as concealment.
- **Playback honesty.** Label every speed change on screen ("4x"); real-time
  segments for anything you call reactive or real-time.
- **Failure cases.** Include representative failures matching your Limitations
  section — the pairing is checked, and showing them buys credibility that
  no success reel can.
- **Regime labels.** Mark sim vs real footage explicitly; a photoreal simulator
  clip mistaken for hardware, then discovered, poisons the whole packet.
- **Anonymity.** No faces, badges, lab signage, institution-branded robot
  livery, or watermarks; mute or scrub audio (voices identify people).

```bash
# Fit the strict 250 MB cap without shredding quality (H.264 target ~8 Mbps)
ffmpeg -i raw_cut.mp4 -c:v libx264 -preset slow -b:v 8M -maxrate 10M \
       -bufsize 16M -vf scale=1920:-2 -an overview_anon.mp4   # -an strips audio
stat -c '%s bytes' overview_anon.mp4          # verify < 250*1024*1024
# Frame-level anonymity spot check: export stills every 5 s and eyeball them
ffmpeg -i overview_anon.mp4 -vf fps=1/5 frames/check_%03d.png
```

Suggested three-minute arc: task family and setup (20 s) → method in one
diagram (20 s) → uncut successes across tasks/objects (90 s) → failures +
limitations (30 s) → generalization or sim-to-real side-by-side (20 s).

## The appendix: overflow with a contract

Because reviewers may skip it, apply a simple contract test to every block you
move there: *if a reviewer never reads this, does any claim in the body lose its
support?* If yes, it stays in the body (or the claim softens).

Belongs in the appendix: full hyperparameter and architecture tables, per-task
result breakdowns behind body-level aggregates, extra qualitative rollouts,
prompt lists for language-conditioned systems, rig photographs, dataset
datasheets, extended related work.

Does not belong: the only statement of the evaluation protocol, the only
sim-to-real numbers, the definition of the success criterion, or the honest
version of a claim the body states more boldly.

## Code and data attachments during review

- Ship a self-contained, anonymized bundle: training config, evaluation scripts,
  environment definitions, and a small demo-data sample if the full set is heavy.
- Scrub before zipping — usernames in paths, git history, W&B project names,
  internal hostnames, license files naming the lab (`corl-submission` has the
  mechanical sweep).
- A `README` at the bundle root mapping files to paper tables costs ten minutes
  and is the difference between "code provided" and "code checked."

## Camera-ready transition (the PMLR pivot)

On acceptance the channels reorganize (deadline: October 12, 2026, 23:59 AoE for
the 2026 cycle):

1. Appendix merges into the end of the camera-ready PDF (`corl-camera-ready`).
2. The review-time video cannot follow the paper into PMLR — publish it on a
   project page or stable video host, de-anonymized, and cite the link in the
   main text.
3. Code/data move to their permanent public homes; prefer an archival DOI for
   datasets you expect others to benchmark against (`corl-artifact-evaluation`).

## Assembly checklist

```text
[ ] Body stands alone with supplementary deleted (contract test passed)
[ ] Video: uncut episodes, labeled speeds, failures included, regimes marked
[ ] Video ≤ 250 MB, audio stripped, frame-level anonymity check done
[ ] Appendix in the same PDF, after references, no load-bearing content
[ ] Code bundle anonymized, README maps files → tables
[ ] External links (if any) anonymous including the URL itself
[ ] Post-acceptance hosting plan drafted (PMLR takes no video)
```

Caps, encouragement language, and the PMLR handoff are all cycle-specific:
re-open https://www.corl.org/contributions/instruction-for-authors for the live
year before finalizing the bundle.
