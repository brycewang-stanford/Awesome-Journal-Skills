---
name: wsdm-camera-ready
description: Use when preparing a WSDM camera-ready after acceptance - de-anonymization order, ACM rights and TAPS production into the Digital Library proceedings, CCS concepts and keywords, page-allowance verification, artifact link restoration, and registration/presentation duties at a single-track winter conference.
---

# WSDM Camera-Ready

Turn an accepted WSDM paper into its archival form in the ACM Digital Library.
WSDM proceedings are ACM proceedings (WSDM '26 is DOI 10.1145/3773966; each
edition gets its own volume), so the mechanics run through ACM's standard
production chain. Warning up front: the pack could not verify the current
edition's camera-ready deadline or final page allowance - both are 待核实 items
that the acceptance email and author-kit page settle, and nothing here
substitutes for them.

## The order of operations that avoids rework

```text
1. Read the acceptance email twice; extract deadline, page allowance,
   required class options, and the rights-form sender to whitelist.
2. Complete the ACM e-rights form FIRST - it generates the exact
   copyright block and \setcopyright values your LaTeX must carry.
3. De-anonymize: author block, third-person self-citations back to
   first person where natural, acknowledgements and grants restored.
4. Restore real artifact URLs (the anonymous repo becomes the public
   one) and re-run every link.
5. Add/verify CCS concepts and keywords via the ACM CCS tool.
6. Rebuild with the camera-ready class options; check the allowance.
7. Submit source (TAPS-style production expects LaTeX/Word source,
   not just a PDF); fix validation errors early - TAPS queues clog
   near deadlines.
8. Register an author and confirm who presents (talk and/or poster).
```

Steps 2 before 3-6 matters: the rights confirmation dictates copyright text,
DOI string, and reference format, and TAPS-produced output will be rejected or
regenerated if the rights block is wrong.

## De-anonymization is an editing pass, not a toggle

Removing `anonymous` from the class options is the trivial part. The real work:

- Self-citations written as "Prior work [12] showed..." to hide identity often
  read strangely once names return; decide sentence by sentence whether to
  restore first person.
- The rounded or role-anonymized platform descriptions (see `wsdm-submission`)
  can now be made precise *if* your organization's disclosure review permits it.
  Industry authors: start internal publication approval the day of acceptance -
  it is the most common cause of missed camera-ready deadlines, not LaTeX.
- Acknowledge funders and colleagues; ACM's authorship policy governs who may be
  listed as an author, and additions after acceptance typically need chair
  approval - ask, never quietly add.

## Reviewer-requested changes without a rebuttal record

Because WSDM historically has no rebuttal, there is no author-committed change
list from a discussion phase. The reviews and the SPC meta-review are still a
soft contract: implement the factual and presentational fixes they request, and
keep a one-page internal log of what changed. If the meta-review conditions
acceptance on specific fixes, treat those as hard requirements and make them
findable (a sentence in the right section beats a silent table tweak).

## Production checklist

| Item | Check | Common failure |
|---|---|---|
| Rights form | Completed by the listed corresponding author | Form sat in a spam folder |
| Copyright block | Matches e-rights output exactly | Stale `\setcopyright` from a template |
| Page allowance | Camera-ready cap per the author kit (待核实 each edition) | Assuming the submission cap carries over |
| CCS + keywords | Generated from the CCS tool, pasted as XML/commands | Hand-typed concepts that fail validation |
| Metadata | Title/authors in the form == PDF exactly, including accents | Unicode mismatch breaking DL indexing |
| Artifact links | Public repo resolvable, tagged release, license file | Link still pointing at the anonymous mirror |
| Ethics section | Retained in final form | Deleted to reclaim space |
| ORCID | Current ACM production requests ORCIDs for authors | One coauthor without an ORCID at deadline |

## Edge cases that eat deadlines

- **Author changes.** Adding, removing, or reordering authors after acceptance
  needs explicit chair approval under ACM authorship norms; requests sent the
  week of the camera-ready deadline often cannot be processed in time. Raise
  them the day of acceptance.
- **Title or abstract changes.** Meta-review-driven retitles are usually fine
  but must be mirrored in the production system's metadata, or the DL landing
  page and the PDF will disagree forever.
- **Preprint posture.** Posting the accepted version to arXiv is common in
  this community, but verify the rights form's language about accepted-version
  posting and embargoes before uploading; the form you signed in step 2
  governs, not habit.
- **Figure regressions.** TAPS-style recompilation with the publisher's tool
  chain can shift floats and break subfigure references that looked fine
  locally. Recheck every `\ref` in the produced PDF, not your local build.
- **Third-party content.** A screenshot of a platform UI or a licensed
  dataset's example rows may require permission statements at production time;
  the anonymized submission hid the problem, the camera-ready surfaces it.

## Money and presence

- ACM's open-access arrangements (ACM Open) determine whether your institution
  faces an APC-like charge for open access; WSDM-specific terms and any
  registration-bundled publication fee are 待核实 per edition - verify on the
  edition's registration page before budgeting.
- WSDM is small and traditionally single-track: an accepted long paper's talk is
  in front of essentially the whole community, and the poster session is a real
  hiring/collaboration floor. Decide the presenter early, check visa lead times
  for the host country (2027: Hong Kong, February 15-19), and confirm whether
  the edition requires in-person presentation - the pack found no verified
  remote-presentation policy for current editions.

## Two-week runbook (adjust to the real deadline)

```text
Day 0-1   acceptance email parsed; e-rights kicked off; disclosure
          review opened (industry authors)
Day 2-5   de-anonymization edit pass; meta-review fixes implemented
Day 6-8   artifact goes public: real repo, license, tagged release,
          archival snapshot; links restored in the source
Day 9-11  CCS concepts, ORCID sweep, metadata parity check
Day 12    production submission; validation errors fixed same day
Day 13-14 buffer for the error you did not predict
```

## Output format

```text
[Camera-ready status] on track / at risk (deadline: <from acceptance email>)
[Rights] e-rights done -> copyright block synced: yes / no
[De-anonymization] author block / self-citations / acks / links: done or pending
[Allowance] final page count vs verified cap: pass / over / cap unverified
[Meta-review conditions] <fix -> location implemented>
[Presence] registrant, presenter, visa lead time, disclosure approval status
```
