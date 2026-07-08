---
name: iccv-artifact-evaluation
description: Use when packaging code, models, or data for an ICCV paper at review or release time, covering anonymous in-archive code under the do-not-cite-your-repo rule, the June-to-October release runway after acceptance, weight and license decisions in a field whose landmark releases became infrastructure, and reuse-grade packaging.
---

# ICCV Artifact Evaluation

ICCV grants no artifact badges; the judgment is social and it is severe, because
the venue's own history sets the bar. ICCV papers like Mask R-CNN (2017), Swin
Transformer (2021), ControlNet (2023), and Segment Anything (2023) are cited as
much for their released artifacts as for their PDFs — at this venue, the release
*is* part of the contribution's afterlife. Package for two moments: the anonymous
review in spring, and the public release whose natural deadline is the October
conference.

## Review-time: the sealed archive

The 2025 rules shape review packaging in two specific ways. First, do not cite or
link your public codebase — anonymity guidance says to write that code "will be
made publicly available" instead. Second, paper and supplement land on the same
day, so the code package cannot be an afterthought of a post-deadline week
(`iccv-supplementary`). Inside the archive:

- Ship source, configs, and exact environment pins; leave the weights out unless
  small — describe which checkpoints the release will include.
- Scrub identity the way archives actually leak: git metadata, usernames in
  paths, experiment-tracker entity names, cluster hostnames in launcher scripts.
- Include five-sample inference with expected outputs, so a reviewer can smoke-
  test without your datasets.

```bash
# Anonymized review package from a live repo, reproducibly
git archive HEAD -o /tmp/pkg.tar && mkdir -p /tmp/pkg && tar -xf /tmp/pkg.tar -C /tmp/pkg
cd /tmp/pkg
rm -rf .github wandb outputs
grep -rliE "$(git config user.name | awk '{print $1}')|$(hostname -s)" . | head   # identity residue
python -m pip freeze > requirements.lock                                          # pin exactly what ran
printf 'table→command map:\n  Tab.1: bash run/eval_main.sh\n' > REPRODUCE.md
zip -qr ../iccv_code.zip .
```

`REPRODUCE.md` — one command per paper table/figure — is the highest-value file
per byte in the archive; it converts "trust the tables" into "verify one row."

## The four-month release runway

ICCV's calendar gives artifact work a gift no November-deadline venue offers:
decisions in late June, conference in mid-October. Plan the runway backward from
conference week, when attention peaks:

| Weeks after decision | Release milestone |
|---|---|
| 0–2 | License chosen; hosting decided; repo made public with paper, citation, and "weights coming <date>" |
| 2–6 | Weights uploaded with checksums; inference path verified from a clean machine outside your network |
| 6–10 | Training/eval reproduction path documented; issues from early adopters triaged |
| by conference | Everything in the paper's availability statement is live; project page links CVF open access |

A repo that goes live during conference week arrives exactly when thousands of
people are reading the paper; a repo that goes live three months later arrives
after the field has moved to reproducing someone else's implementation of your
method — which then becomes the cited one.

## Decisions to make on purpose

- **License, split by asset**: code (permissive vs copyleft), weights (research-
  only vs unrestricted — decide who may fine-tune and redistribute), data (can
  you even relicense what you scraped?). "No license" reads as "do not use" to
  every industrial lab.
- **Checkpoint provenance**: name checkpoints for the table rows they reproduce
  and record the code commit that evaluates each to the printed number.
- **Data documentation**: sources, filtering, consent posture for human imagery.
  Vision datasets get audited years later; write the provenance section while
  the facts are fresh.
- **Generative-model posture**: for synthesis work, decide what ships (full
  weights, adapters, inference-only) and write the misuse considerations
  yourself before a journalist does.
- **Benchmark freeze**: if you release evaluation code others will report
  numbers from, version it and changelog every metric fix — silent corrections
  fork leaderboards.

## The infrastructure test

Before calling the release done, run the test the field will run:

1. Fresh cloud machine, no lab credentials: does `git clone` → env setup →
   five-image inference work inside an hour?
2. Do the printed numbers reproduce? State the tolerance you observed
   (`iccv-reproducibility`); a ±0.2 note preempts a hundred issues.
3. Is there exactly one entry point per use case (inference / train / eval),
   each documented in under a screen of README?
4. Would a person with only the checkpoint and the eval script get your Table 1
   row? If not, what unstated asset is missing — and can it be shipped?

## Maintenance as reputation

The two-year gap to the next ICCV means your artifact is the state of the record
for a long time. Budget light maintenance: pin dependencies against rot, tag the
camera-ready state (`v1.0-iccv<year>`), answer the first month's reproduction
issues (usually environment drift), and keep a short log of community-confirmed
reproductions. The venue's landmark releases earned their citation counts in
this phase, not at upload.

## Reverify each cycle

- The availability-statement and repo-citation wording in the current Author
  Guidelines.
- Supplement size limits that constrain review-time code (待核实 for 2025).
- Any artifact checklist or badge program the 2027 chairs may introduce.

## Output format

```text
[Phase] review-archive / release-runway / maintenance
[Archive] identity-clean · pinned · smoke-testable · REPRODUCE.md maps n/m tables
[Runway] weeks to conference: <n>; milestones on track: yes/no
[Licenses] code/weights/data each decided: yes/no
[Infrastructure test] clean-machine hour test: pass/fail at <step>
[Debt] <unshipped promises from the availability statement>
```
