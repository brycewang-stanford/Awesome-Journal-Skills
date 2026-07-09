---
name: icdm-artifact-evaluation
description: Use when packaging code, data, and logs for an ICDM (IEEE International Conference on Data Mining) paper - building the anonymized, history-scrubbed repository that the PDF must cite for a triple-blind Research Track submission, how the single-blind Applied Track changes what may be revealed, and the smoke checks that make an ICDM artifact reviewer-usable.
---

# ICDM Artifact Evaluation

Package the artifact so a reviewer can actually use it, under ICDM's anonymity rules. ICDM does
not run a separate stamped artifact-badging track the way some venues do (verify per edition);
instead, the artifact's job is to be the **cited, anonymized evidence** that supports the paper.
Because the Research Track is triple-blind and traditionally offers no rebuttal, the repository
must be complete and anonymous *at submission time* — there is no later chance to reveal it.

## The repository the PDF must cite

- Reference the code/data repository **inside the submitted PDF**. A repository not cited at
  submission is invisible to reviewers for the entire cycle (no rebuttal to add it later).
- For the Research Track, the link must resolve to an **anonymized** location, not a named
  account, and the contents must reveal no identity.
- For the 2026 **Applied Track (single-blind)**, anonymization of the artifact is not required
  the same way — but confirm the current call, and still avoid shipping secrets or private data.

## Anonymize for the triple-blind regime (Research Track)

| Leak surface | Fix |
|---|---|
| Git history (author names, emails) | Export a fresh repo with **no history** |
| File paths (`/home/alice/...`, cluster hostnames) | Rewrite to relative, generic paths |
| Internal dataset/system names | Rename to public source + version |
| README acknowledgements, funding | Remove until camera-ready |
| Hosting account that identifies you | Use an anonymized hosting option |

A triple-blind leak in the artifact is as fatal as one in the PDF, and it is the surface authors
most often forget.

## Make it reviewer-usable

- Ship a single entry point and pinned dependencies so a reviewer reproduces a headline table in
  one command.
- Include the seeds and configs behind the reported variance (see `icdm-reproducibility`).
- Provide a small runnable slice for methods whose full run is expensive, plus instructions to
  scale up.

```bash
# smoke-check an anonymized ICDM reproduction package before citing it in the PDF
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/anonymized-repo
# then manually confirm: no .git, no author paths, no internal dataset names,
# one entry script, pinned deps, seed list present, README free of identity.
```

## Handle un-releasable data honestly

- If data cannot be released, ship the **code plus a synthetic proxy** that runs end to end, and
  document the protocol so the private-data numbers are attested rather than opaque.
- State the scope of what the artifact does and does not reproduce; an honest boundary beats an
  artifact that silently omits the main result.

## Vignette: the commit that would have unmasked the authors

A team built a clean anonymized zip of their code, but linked their normal lab repository whose
first commit read "initial import — Alice, BigState University." Under triple-blind that is an
identity leak that could invalidate the submission. The fix: export a fresh repository with no
history, rewrite absolute paths to relative, rename the internal dataset to its public source and
version, strip the acknowledgements from the README, host it anonymously, and cite that link in
the PDF. Same artifact, now safe for a triple-blind reviewer.

## Output format

```text
[Cited in PDF] repository referenced in the submitted paper: yes / no
[Regime] Research(triple-blind) -> anonymized required | Applied(single-blind)
[Anonymization] no history / no author paths / no internal names: pass / leaks
[Usability] one-command headline table + pinned deps + seeds: yes / no
[Un-releasable data] synthetic proxy + attested protocol: yes / N-A
[Top fix] <single most important artifact fix before submission>
```
