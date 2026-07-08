---
name: chi-artifact-evaluation
description: Use when packaging the artifacts behind an ACM CHI paper — prototypes, study instruments, codebooks, datasets, analysis code — for anonymous review scrutiny and for post-acceptance archival release, in a venue with no formal artifact-evaluation committee doing it for you.
---

# CHI Artifact Evaluation

CHI's Papers track posted no separate artifact-evaluation committee or badge track
for the cycles checked (2026, 2027; confirm each year — 待核实 as a standing item).
That absence cuts both ways: nobody certifies your artifacts, and nobody but you
ensures a skeptical reviewer can inspect them. At CHI the "artifact" is rarely just
code — it is the prototype, the study instruments, the codebook, the dataset, and
the video evidence of the system working. Package for two audiences with opposite
needs: the anonymous reviewer with five minutes, and the future researcher with a
real use for your materials.

## The CHI artifact inventory

| Artifact | Reviewer's question | Archival value after acceptance |
|---|---|---|
| Prototype / system code | "Does the claimed interaction actually exist?" | Others extend or compare against it |
| Video figure of real use | "Does it work outside the authors' hands?" | Permanent DL evidence (`chi-supplementary`) |
| Study instruments (guides, questionnaires, tasks) | "Was the study what the paper says?" | Direct reuse in replications |
| Codebook / analysis audit trail | "Do the themes live in the data?" | Methods teaching material |
| Dataset (de-identified) | "Do the numbers re-derive?" | Secondary analysis |
| Design files (3D prints, schematics, figma) | "Could this be rebuilt?" | Fabrication replication |
| Prompts / model configs for AI conditions | "What system did participants face?" | The only record once the API moves |

Inventory first, then decide per artifact: reviewed now, released later, or honestly
withheld with a reason (`chi-reproducibility` has the data-sharing ladder).

## Reviewer-facing packaging (anonymous, five minutes)

The review-phase archive rides the single September deadline with everything else.
Design it so the first five minutes land:

1. **Root README** with a claims map: "Claim in §5.1 → `analysis/h1_test.R` →
   Table 2." Three such lines are worth thirty pages of appendix.
2. **One command per claim** where code is involved; vendor the environment
   (`requirements.txt`, `renv.lock`) because a reviewer will not debug pip.
3. **A demo path that does not require your hardware.** If the contribution is a
   physical device, the video figure *is* the reviewable artifact; the archive adds
   schematics and firmware so the claim is auditable in principle.
4. **Anonymity end to end**: no `.git`, no metadata, no named accounts, anonymized
   platform views only, usernames scrubbed from notebook outputs and file paths.

```bash
# Cold-simulate the reviewer on the exact ZIP you will upload
rm -rf /tmp/ae && unzip -q supplement.zip -d /tmp/ae && cd /tmp/ae
cat README* | head -30                      # does the claims map appear immediately?
grep -rEil 'author|university|(^|[^a-z])lab' --include='*.md' . | head
time bash run_minimal_demo.sh               # the five-minute budget is literal
```

## Post-acceptance release is a separate product

At the publication-ready stage (February for CHI 2027), rebuild the artifact set
under real names for permanence, not for review:

- Deposit in a persistent home — the DL supplemental record, OSF, Zenodo, an
  institutional archive — with a DOI; a lab URL is a dead link in five years.
- License deliberately: code (MIT/Apache/GPL), data and instruments (CC BY or
  CC BY-NC), and record third-party constraints (stimuli copyrights, model terms
  of service for cached AI outputs).
- Re-check de-identification *harder* than at review: public release is forever,
  and participant re-identification harms real people. Where consent was narrow,
  release the instruments and codebook instead of the data — respected practice.
- Tag the released version to match the camera-ready ("as-published"), then develop
  onward in a separate branch; future readers need the paper's version, not HEAD.

## Honest holes beat cosmetic completeness

A packaging note that says "the deployment used partner infrastructure we cannot
ship; this archive contains the full client, the API contract, and a mock server
reproducing the study conditions" earns more trust than a repo padded with dead
code that hides the same gap. Reviewers at CHI read many partial artifacts; what
they punish is discovering the gap themselves after the README implied completeness.

## Timing inside the CHI year

- Build the claims-map README while writing §4–5 of the paper — it doubles as your
  own claim-evidence audit (`chi-experiments`).
- Freeze the review archive at T−1 week; sweep it with `chi-submission`'s checks.
- Diary the February release rebuild at acceptance time; rushed public releases in
  the TAPS window are where consent violations happen.

## Output format

```text
[Inventory] <artifact: reviewed / released-later / withheld+reason, per row>
[Claims map] present in README: yes/no · claims covered: <n>/<n>
[Five-minute test] cold demo ran in <time> / failed at <step>
[Anonymity] archive clean: yes/no — <channels checked>
[Release plan] home: <DL/OSF/Zenodo> · license: <code/data> · consent re-check owner: <name>
```
