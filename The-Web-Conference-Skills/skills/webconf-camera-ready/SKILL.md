---
name: webconf-camera-ready
description: Use when preparing a Web Conference (WWW) camera-ready after acceptance, covering the uniform 12-page/8-content proceedings budget, de-anonymization and restored acknowledgements, ACM e-rights and TAPS production, ACM Open cost exposure, author registration, and the artifact-badging submission that rides along with the final files.
---

# Web Conference Camera-Ready

The 2026 notification-to-camera-ready gap was twelve days (January 13 to January 25,
2026) — short enough that de-anonymization, rights forms, registration, and artifact
deposit must be prepared *before* the decision arrives. Everything below is anchored
to the 2026 edition; the ACM pipeline steps are the publisher's standard flow and
the WWW-specific instructions arrive by email after acceptance, so treat the
sequence as fixed and the details as 待核实 until that email lands.

## The proceedings budget is a different shape

Accepted papers all receive the same maximum length: **12 pages, of which 8 are
content pages**, in the ACM Digital Library. Note what did *not* change from
submission: the content allowance. Unlike venues that grant an extra page for
addressing reviews, the 2026 Web Conference held content at 8 pages, so every
rebuttal promise ("we will add baseline B to Table 2") must be paid for by cutting
something. Budget the cuts when writing the rebuttal, not after acceptance.

| Task | Depends on | Can be done before notification? |
|---|---|---|
| De-anonymized source with author block | acmart, no `anonymous` option | Yes — keep a parallel branch |
| Acknowledgements + funding numbers restored | grant records | Yes |
| Rebuttal-promised edits drafted | review packet | Yes |
| ACM e-rights form | acceptance email | No — but decide licensing stance now |
| TAPS source upload and HTML/PDF proof check | e-rights completion | No |
| Author registration | fee schedule | Decide payer now |
| Artifact deposit + badge application | camera-ready deadline | Yes — deposit early |

## De-anonymization sweep

Reverse every anonymity edit deliberately; half-reversed papers are the classic
failure. Check: author block and ORCIDs (ACM requires ORCIDs for the publishing
workflow — have every co-author's ready), acknowledgements, grant numbers,
third-person self-citations back to first person where natural, dataset names that
were masked ("a large e-commerce platform" → the real name, *if* the data agreement
permits naming it), and repository links now pointing at the real, non-anonymous
archive.

```bash
# Sanity greps on the de-anonymized LaTeX before TAPS upload
grep -rn "anonymous\|Anonymized\|redacted\|our institution" *.tex   # leftovers
grep -rn "\\\\documentclass" main.tex   # 'anonymous' and 'review' options removed?
grep -c "orcid" main.tex                # one per author expected in acmart
pdfinfo main.pdf | grep -i "author\|title"  # metadata restored, not "anonymous"
```

## ACM production pipeline (e-rights → TAPS → DL)

1. **e-rights**: the corresponding author receives the ACM rights form. The choice
   set (copyright transfer, licence, or open access under ACM Open) determines what
   appears in the copyright block — the `\setcopyright{...}` and conference metadata
   commands in the final source must match the form, or TAPS bounces the paper.
2. **TAPS** (The ACM Publishing System) compiles your *source*, not your PDF, and
   emits both PDF and responsive HTML for the Digital Library. Non-standard
   packages, hand-positioned floats, and bitmap-only figures are the usual
   casualties; run the source through TAPS early in the window and read the HTML
   rendering, which is what many readers will actually see.
3. **ACM Open exposure**: whether an APC applies depends on the corresponding
   author's institutional agreement with ACM; amounts, waivers, and any subsidy for
   the 2026 volume were not verifiable when this pack was built — check the
   acceptance email and https://www.acm.org/publications/openaccess before assuming
   either "free" or a specific fee.

## Registration and presentation

At least one author registering is the norm for ACM proceedings venues, and the
2026 edition's postponement announcement explicitly extended the **author
registration deadline to March 30, 2026** — evidence that author registration was a
tracked obligation. The postponement also promised a format decision (in-person vs.
hybrid) "by May," so presentation-mode rules for 2026 were genuinely fluid;
whatever edition you are in, get the current attendance rule in writing from the
official site rather than from precedent.

## The artifact rider

Artifact badging submissions were due **together with the camera-ready** in 2026.
If the paper has a dataset, model, or code artifact, run `webconf-artifact-evaluation`
in parallel with this checklist — the archival deposit (DOI-bearing repository, not
a bare GitHub URL) takes longer than the badge form. The final paper should cite
the deposited artifact's persistent identifier, which means the deposit must exist
*before* the final PDF freezes.

## Edge cases the twelve days do not forgive

- **Author corrections after the freeze.** The submission-time freeze allowed only
  spelling and affiliation fixes; a co-author who changed institutions between
  October and January updates their affiliation now, but a missing contributor
  cannot be added at camera-ready either — that door closed at the abstract
  deadline, and pleading at production time fails.
- **The masked platform that must stay masked.** If the data agreement never
  permitted naming the platform, the camera-ready keeps the anonymized
  description permanently. Decide this with the data owner *before* acceptance;
  legal review does not fit in twelve days.
- **Postponement fallout.** The 2026 edition moved its dates after camera-ready
  closed. Published papers were unaffected, but visa letters, talk scheduling,
  and registration transfers all reopened. Keep the team's travel plans decoupled
  from the publication pipeline — the paper is done when TAPS accepts it.
- **The rebuttal promise that no longer fits.** If a promised addition cannot be
  honored within 8 content pages, honor its *substance* in condensed form and
  note the full version in the artifact. Silently dropping a commitment that
  reviewers conditioned acceptance on is the one camera-ready sin with reputation
  cost.

## Twelve-day sequence

1. Days 1-2: e-rights form; lock licensing; start registration.
2. Days 3-6: apply rebuttal-promised edits inside the 8-content-page budget;
   de-anonymization sweep; artifact deposit finalized, DOI cited in the paper.
3. Days 7-9: TAPS upload; fix compile and HTML-rendering issues.
4. Days 10-12: proof-read TAPS output (PDF *and* HTML), submit badge application,
   confirm registration receipt.

## Output format

```text
[Camera-ready status] on track / blocked
[Budget] content=<n>/8, total=<n>/12; rebuttal promises paid for: yes/no
[De-anonymization] author block / acks / self-citations / data names / metadata
[ACM pipeline] e-rights done? TAPS compiled? HTML proof read?
[Money] registration state; ACM Open status (verified / 待核实)
[Artifact rider] deposit DOI in paper: yes / no / N-A
```
