---
name: naacl-related-work
description: Use when building the related-work and positioning story for a NAACL submission — covering the ACL Anthology lineages reviewers expect, citing Findings, workshop, and regional venues correctly, handling resubmission histories and concurrent preprints under ARR rules, and stating the delta in one falsifiable sentence.
---

# NAACL Related Work

A NAACL reviewer's first suspicion about related work is not that you missed
a paper — it is that you missed a *lineage*: the chain of prior datasets,
task definitions, and evaluation critiques your work silently inherits from.
The section's job is to prove you know what you inherited and to state, in
one checkable sentence, what you changed.

## Lineages a NAACL reviewer walks

| Lineage | Question asked | Where it lives |
|---|---|---|
| Task lineage | Who defined this task and its metrics? | Anthology main + Findings volumes |
| Data lineage | What corpus is yours derived from, and what did *its* paper warn about? | Dataset papers, LREC-COLING, data cards |
| Method lineage | What is the nearest prior system, and is it a baseline? | *ACL venues + ML conferences |
| Evaluation critique | Has this metric or protocol been challenged? | Methodology papers, often at this very family of venues |
| Regional/community lineage | Who worked on these languages before, including outside English-language venues? | AmericasNLP and sibling workshops, LatinX in AI resources, regional journals |

The fifth row is where NAACL differs from its siblings. For work on
languages of the Americas there is frequently a body of prior effort in
workshop proceedings, regional publications, or Spanish- and
Portuguese-language venues; a related-work section that cites only
high-prestige anthology hits while ignoring the community that built the
field's resources reads, at this chapter, as exactly the erasure the venue
renamed itself to counter.

## Citation-status precision

- **Findings papers are archival.** Cite them as published work, volume and
  all; treating a Findings paper as "unpublished" is wrong and noticed.
- **Workshop papers are archival** when their proceedings are in the
  Anthology; their evidentiary weight differs, their citability does not.
- **Preprints** are citable but never load-bearing for a "prior work already
  established X" claim — flag them as preprints.
- **Concurrent work** (surfaced within a few months of your upload): cite,
  mark as concurrent, and do not contort your delta statement around it;
  ARR guidance shields authors from being scooped by weeks.
- Verify every citation resolves to a real Anthology or DOI entry.
  Fabricated references — an LLM-era failure ARR now polices explicitly —
  are treated as integrity violations, not typos.

```bash
# Sweep the bibliography for suspicious entries before upload
grep -oE 'https?://aclanthology\.org/[^ }]+' refs.bib | sort -u | \
  xargs -I{} sh -c 'curl -s -o /dev/null -w "%{http_code} {}\n" {}' | grep -v '^200'
# Anything non-200 gets hand-checked; no URL, no trust.
```

## Bibliography hygiene for the Anthology era

- Pull BibTeX from the Anthology's own export, not from aggregator sites
  that mangle venue fields and drop the `naacl`/`findings` distinction.
- Keep author-name diacritics exactly as the Anthology renders them —
  flattening *Muñoz* to *Munoz* in a reference list is the citation-level
  version of the metadata errors `naacl-camera-ready` guards against.
- When a paper exists as both a preprint and an Anthology publication,
  cite the Anthology version; citing the arXiv copy of a published *ACL
  paper signals careless lineage work to exactly the wrong readers.
- Normalize venue strings once (`Proceedings of NAACL`, `Findings of the
  ACL: NAACL 2025`) rather than letting three formats coexist.

## Resubmission positioning under ARR

If the paper was reviewed in an earlier cycle, related work is one of the
places the mandatory change summary must be visible: reviewers get your
prior reviews, so "R3 named two uncited baselines" followed by an unchanged
section is a documented broken promise. Update the section, then say so in
the summary with section numbers.

## The delta sentence

End the section with one sentence a reviewer could falsify:

> "Unlike [nearest prior system], which evaluates on translated test sets,
> we evaluate on natively authored Spanish and Quechua data and show the
> translation-based protocol overstates accuracy by 6-9 points."

Test it: does it name the nearest work? Does it state a difference in
*method or evidence*, not adjectives? Could a reviewer check it against
your tables? If any answer is no, the section has organized citations but
not positioned the paper.

## Assembly order

1. Build the five-lineage inventory before writing any prose.
2. Draft the delta sentence; let it dictate which citations get sentences
   versus bracketed lists.
3. Compress narrative history into contrastive claims tied to your
   contributions.
4. Run the resolution sweep; fix or cut anything unverifiable.
5. Re-read as the author of the nearest prior work — is your account of
   them fair, current, and specific?

## Output format

```text
[Lineage coverage] task / data / method / evaluation / regional -> ok or gap
[Delta sentence] <the falsifiable sentence>
[Citation-status errors] <Findings/workshop/preprint mislabels>
[Resolution sweep] <all resolve / list of failures>
[Resubmission trace] n/a | <reviewer ask -> section change>
```
