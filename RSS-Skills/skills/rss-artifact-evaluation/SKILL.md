---
name: rss-artifact-evaluation
description: Use when packaging the artifacts behind an RSS (Robotics: Science and Systems) paper — code, trained policies, trial ledgers, hardware documentation, and footage — first as anonymous review-time evidence and then as the public release the venue's free open-access proceedings culture expects, without any badge program to structure it.
---

# RSS Artifact Evaluation

Package the artifacts as if a skeptical peer lab will pick them up — because at RSS,
that is the actual evaluation mechanism. No badge track or artifact committee was
verified for the 2026 cycle (待核实 each edition); the discipline is therefore
self-imposed, and the reward is post-publication: RSS papers are free to every reader
at roboticsproceedings.org, so strong artifacts get found and reused quickly.

## The robotics artifact stack

Inventory what the paper's claims actually rest on, layer by layer:

| Layer | Artifact | Review-time state | Release state |
|---|---|---|---|
| Claim analysis | Scripts turning logs into tables | in supplement | public repo |
| Evidence corpus | Trial ledger + footage | anonymized | full, licensed |
| Learned components | Policy/model weights + training configs | weights or recipe | both |
| Software stack | Planner/controller code, sim environments | source in archive | tagged release |
| Hardware layer | Platform ledger, CAD for custom parts, BOM | described in PDF | files where possible |
| Protocol | Reset/intervention/success-criterion doc | in supplement | versioned doc |

The stack ordering is a triage order: the top layers are cheap and non-negotiable;
the bottom layers may be partially closed for legitimate reasons — but each closure
needs one honest sentence in the paper.

## Review-time state (anonymous)

- Everything ships through the supplementary channel by its own deadline
  (`rss-supplementary`); no external links — the 2026 CFP admits links only in the
  camera-ready.
- Scrub authorship trails ML packaging misses: ROS package names carrying lab
  acronyms, URDF files naming custom rigs after people, commit history, notebook
  metadata, cluster paths.
- Optimize for a ten-minute inspection: a reviewer who opens the archive should be
  able to regenerate one small table and watch one labeled clip without reading
  documentation twice.

## Release-time state (public)

- Swap placeholders for a public repository, choose a real license (code and data may
  need different ones), and archive a citable snapshot (e.g., a DOI-minting service)
  so citations outlive lab servers.
- Publish the trial ledger and analysis scripts together — this is the pairing that
  lets others *audit* rather than merely admire the result.
- Weights too large to host? Publish the training recipe, seeds, and the evaluation
  harness, and say which reported numbers depend on the exact checkpoint.
- Update the camera-ready to point at the release; RSS explicitly welcomes links
  there (`rss-camera-ready`).

## Mechanical anonymity sweep for robotics archives

Robotics repositories leak identity in places generic checklists never look; run
greps before packaging:

```bash
# lab and platform tells in code, configs, and robot descriptions
grep -riE "(lab|univ|institute|group)[-_a-z]*" --include="*.yaml" --include="*.xacro" .
grep -rl "<your-lab-acronym>" .                    # ROS package prefixes
find . -name "*.urdf" -o -name "*.xacro" | xargs grep -l "author\|copyright"
# history and metadata
rm -rf .git; find . -name "*.ipynb" -exec jq '.metadata' {} \;
exiftool supplement_video.mp4 | grep -iE "creator|artist|gps|serial"
```

Then rename: packages, launch files, and URDF link names that encode the lab or a
person ("annas_gripper_v3") are as identifying as an author block.

## Sizing the inspection to reality

- Assume the archive gets ten minutes at review time and an afternoon
  post-publication; order the README for the ten-minute reader and link deeper.
- Put the one-command table regeneration *first* in the README; it is the highest
  belief-per-minute artifact the package contains.
- State expected runtimes next to every command — a reviewer who hits a silent
  20-minute script assumes it is broken.

## Handling the un-releasable

Robotics has honest closure cases — proprietary platforms, safety-critical
controllers, partner data. The rule: closure is declared per stack layer, with a
replication path around it ("the controller API is proprietary; we release the
planner and the recorded command streams so the planning claim remains auditable").
What kills credibility is not the closed layer; it is discovering it after
publication.

## License and citation plumbing at release

- Code and data usually want different licenses; a permissive code license does not
  cover collected trial data or footage of identifiable environments.
- Third-party components inherited through the software stack (simulators, vendor
  SDKs, ROS packages) carry terms that survive your packaging — audit before
  promising "fully open."
- Add a machine-readable citation file pointing at the roboticsproceedings.org
  entry and its `10.15607/RSS.*` DOI, so downstream users cite the venue version
  rather than a preprint.
- Pin a release tag matching the camera-ready ("as-published"); development can
  continue on main without eroding the paper's evidentiary snapshot.
- Record hosting longevity: lab servers rot, which is why the citable snapshot in
  an archival service is the load-bearing copy.

## Output format

```text
[Stack inventory] <layer -> artifact -> state>
[Ten-minute test] table regenerated <y/n> | clip labeled <y/n>
[Anonymity findings] <ros-names/urdf/history/paths>
[Closure declarations] <layer -> reason -> replication path>
[Release checklist] repo / license / citable snapshot / ledger+scripts / camera-ready link
```
