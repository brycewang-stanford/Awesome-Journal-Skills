---
name: rss-related-work
description: Use when positioning an RSS (Robotics: Science and Systems) submission within the literature — covering the robotics-conference lanes (RSS/ICRA/IROS/CoRL) plus journals and ML venues, handling fast-moving arXiv concurrency in robot learning, keeping self-references double-blind, and turning related work into claim-sharpening contrasts.
---

# RSS Related Work

Position the paper so its claim's novelty is checkable. At a selective single-track
venue, related work is not a courtesy section — it is where the Area Chair verifies
that the field genuinely lacks what the paper asserts.

## The lanes an RSS reviewer expects covered

| Lane | Where it lives | The question your coverage must answer |
|---|---|---|
| RSS's own line | roboticsproceedings.org (free) / dblp | What did the last 2-3 editions say on this problem? |
| The IEEE siblings | ICRA / IROS proceedings | Is this "known at the mega-conferences" already? |
| Robot learning | CoRL, ML venues | If learning-based: what does the CoRL line already show? |
| Journal depth | T-RO, IJRR, AURO | Does a journal version of this idea predate you? |
| Enabling fields | vision/ML/control theory venues | Is the core mechanism imported? Say so and cite the source |

The venue's own lane deserves priority: RSS proceedings are open-access, so "we
couldn't access it" is never a defense, and reviewers often *are* the recent-edition
authors under the anonymity veil.

## Contrast, don't catalogue

Rewrite tour-style paragraphs into claim-anchored contrasts:

- Weak: "Much work has studied cloth manipulation [3,7,12,19]."
- Strong: "Prior bimanual systems couple contact timing with trajectory optimization
  [3,7]; we show decoupling them isolates the dominant failure source, which [3,7]
  cannot attribute."

One contrast sentence per nearest neighbor; the neighbor set is usually 3-5 papers,
not 30. Everything else earns at most a grouped citation.

## arXiv concurrency in a fast field

Robot learning moves preprint-first, so the January deadline lands amid unrefereed
neighbors:

- **Cite visible preprints neutrally.** A same-quarter arXiv paper with your idea is
  a fact reviewers will know; acknowledging it with a technical distinction beats
  hoping nobody noticed.
- **Do not claim priority races.** "Concurrent work [x] differs in A and B" is
  verifiable; "we were first" is not.
- **Cutoff hygiene:** state comparisons against the literature as of submission; the
  rebuttal (if invited) can acknowledge anything that landed after.

## Double-blind self-citation

- Cite your own prior papers in third person, exactly like a stranger's work.
- The robotics-specific trap is the *platform chain*: citing the paper that built
  your exact rig, in a sentence that only makes sense if it is yours, de-anonymizes
  as surely as a name. Describe hardware provenance generically at submission and
  restore attribution at camera-ready.
- Unpublished own work needed for the argument: include as anonymized supplement,
  not as a citation to a findable preprint.

## Coverage protocol (an hour, well spent)

A repeatable sweep that catches the misses reviewers catch:

```text
1. roboticsproceedings.org: open the last three volumes' tables of contents;
   keyword-scan titles (all free, no login).
2. dblp.org/db/conf/rss: confirm venue attribution for anything you plan to
   call "prior RSS work" — folklore misfiles ICRA papers as RSS constantly.
3. dblp author pages of your 3-5 nearest neighbors: find their newest
   follow-ups, including the IROS/CoRL versions of ideas you know from RSS.
4. arXiv: search your claim's key nouns filtered to the last 12 months;
   list hits in a concurrency ledger with a one-line distinction each.
5. Reverse pass: for each baseline you compare against, read who cites it
   *this year* — that citation neighborhood is your reviewer pool's memory.
```

## Common positioning failures at this venue

| Failure | How it reads to the AC |
|---|---|
| Only ML venues cited for a manipulation claim | Authors don't know the robotics line |
| The venue's own recent papers absent | Didn't check the free proceedings |
| Nearest neighbor cited but never contrasted | The delta may not exist |
| "First to..." with a findable counterexample | Credibility damage spreads to the claims |
| 60-reference tour, 3 contrasts | Coverage substituting for positioning |

## Overlap declarations

- Prior workshop or abstract versions of this work: verify the current CFP's stance
  and declare rather than gamble — workshop archival status varies.
- Same-cycle submissions to sibling venues with shared content are the routing
  hazard of the packed robotics calendar (`rss-workflow`); resolve before, not after,
  the abstract deadline.

## Vignette: positioning a contact-rich manipulation claim

A paper claims contact-timing decoupling explains bimanual failure rates. Its
neighbor set after the protocol sweep: a recent RSS paper on bimanual planning
(contrast: couples timing and motion, cannot attribute failures), an ICRA system
with higher raw success on one garment class (contrast: no mechanism isolation, so
the number and the claim answer different questions), a CoRL policy-learning line
(contrast: learns timing implicitly; this paper measures it explicitly), and a
T-RO stability analysis (contrast: quasi-static assumption excludes the regime
studied here). Four contrasts, four sentences, and the novelty claim is now
checkable by any reviewer who knows one of the four lanes.

## Output format

```text
[Lane coverage] rss-line / icra-iros / corl / journals / enabling -> gaps
[Nearest neighbors] <3-5 papers, each with a contrast sentence>
[Concurrent preprints] <item -> neutral handling>
[Self-citation sweep] third-person ok / platform-chain risk found
[Overlap declarations] <none / listed>
[Novelty sentence] <the claim's delta, one line>
```
