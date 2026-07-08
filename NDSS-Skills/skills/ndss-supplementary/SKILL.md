---
name: ndss-supplementary
description: Use when dividing an NDSS paper between the 13-page body, the Ethics Considerations section, references, and appendices — deciding what reviewers must see in-body, what the page-limit exclusions really buy, and how the camera-ready gains a 2-page artifact appendix.
---

# NDSS Supplementary Material

NDSS 2027's limit is 13 pages — but the boundary is unusual: the **Ethics Considerations
section, references, and appendices are all excluded** from the count (CFP, checked
2026-07-08). That exclusion is an invitation to structure, not a loophole to exploit. The
governing rule: the 13 pages must contain everything the accept/reject decision rests on,
because nothing obliges a reviewer to read past them.

## What goes where

| Content | Placement | Reasoning |
| --- | --- | --- |
| Threat model, design/attack, headline evaluation | Body | Decision-critical; must survive the Round-1 fast read |
| Disclosure timeline, harm analysis, IRB/ERB detail | Ethics Considerations (before references) | Uncounted, but the *signal* still needs a page-one sentence and method-level mentions |
| Proofs of stated theorems, protocol message formats | Appendix | Verification material — reviewers check it if inclined |
| Full config matrices, extra target versions, per-vantage breakdowns | Appendix | Robustness depth backing an in-body summary row |
| Additional case studies repeating the in-body pattern | Appendix (or cut) | Repetition earns no Round-2 points |
| Artifact description | 2-page appendix added at camera-ready if AE passed | Defined by the Call for Artifacts; not part of submission |

## The dependency test

For each appendix, ask: *if a reviewer never opens this, does the body still justify
acceptance?*

- **Yes** → correctly placed. The body carries a self-contained summary (one sentence or
  one table row) with a forward pointer.
- **No** → decision-critical content has leaked out of the body. Promote the load-bearing
  part, demote something decorative instead.

The most common leak in security drafts: the *only* evidence that a defense survives
adaptive attack sits in an appendix table. Round 2's discussion phase will treat unread
appendix evidence as missing evidence.

## Anti-patterns with the exclusions

- **Ethics-section stuffing** — parking methodology or results in the uncounted ethics
  section. Reviewers and the Ethics Review Board read it for ethics; off-topic content
  there signals gaming and invites scrutiny of everything else.
- **The 40-page appendix** — bulk unedited output dumped after the references. Appendices
  are written documents with headings and topic sentences, or they are noise.
- **Ghost pointers** — "see Appendix F" where F does not exist or answers a different
  question. Every pointer gets checked during the anonymity/format pass (`ndss-submission`).
- **Anonymity decay** — appendices and supplementary files are inside double-blind scope:
  screenshots with usernames, configs with institutional hostnames, and dataset paths leak
  identity exactly as body text would.

## Suggested skeleton

```text
p.1-13   BODY
         1 Introduction (first-page contract — see ndss-writing-style)
         2 Threat model & background
         3 Attack / system design
         4 Evaluation (headline results incl. adaptive-adversary summary)
         5 Discussion & limitations
         6 Related work
         7 Conclusion
uncounted
         Ethics Considerations        (immediately before references, per CFP)
         References
         A  Proofs / protocol details
         B  Full experimental matrix  (body shows the summary row)
         C  Additional case studies
         [camera-ready only] Artifact Appendix (2 pp., per Call for Artifacts)
```

## Working the split during writing

1. Draft body-first; open an appendix only when a section exceeds its page budget *and*
   the overflow fails the dependency test.
2. Give every appendix a one-line contract at its top: what question it answers for which
   body claim.
3. At each freeze, re-run the dependency test — content drifts appendix-ward under page
   pressure, and load-bearing tables get pushed out silently.
4. Keep supplementary code/data links anonymized at submission (anonymous hosting; no
   institutional URLs); the de-anonymized versions return at camera-ready
   (`ndss-camera-ready`).

## Output format

```text
[Body self-sufficiency] pass/fail — decision-critical items found outside body
[Ethics section] scope-clean? content that belongs elsewhere
[Appendix inventory] per appendix: contract line + dependency-test verdict
[Pointer audit] dangling or mismatched forward references
[Anonymity sweep] identity leaks found in appendices/supplements
```
