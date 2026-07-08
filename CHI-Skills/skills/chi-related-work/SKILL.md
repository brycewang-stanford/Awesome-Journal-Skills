---
name: chi-related-work
description: Use when building the related-work section of an ACM CHI paper — covering the HCI venue family and the non-CS disciplines CHI draws on, positioning against the last few CHI cycles, keeping self-citation anonymous — in a venue where insufficient contextualization is the top assisted desk-reject ground.
---

# CHI Related Work

At CHI, related work is screened before it is reviewed: **ADR-Context — "grossly
insufficient literature review to contextualize the contribution" — was the most
frequently cited assisted desk-reject reason at CHI 2026**, applied jointly by
subcommittee chairs and ACs before external review (chi2026.acm.org outcome posts,
read 2026-07-08). A thin or misaimed section no longer just lowers scores; it can
end the submission in October.

## Five lanes, all checked

| Lane | What belongs there | Who notices its absence |
|---|---|---|
| CHI itself, last ~3 cycles | The ongoing conversation your paper joins | 1AC/2AC — instantly |
| The HCI family (CSCW, UIST, DIS, IUI, ASSETS, IMWUT, TOCHI, IJHCS) | The specialist thread of your topic | The external recruited from that thread |
| Foundational HCI | The classic your framing stands on (or contradicts) | Senior reviewers |
| Feeder disciplines | Psychology, sociology, design, communication, health, ML — wherever your constructs come from | The reviewer trained in that discipline |
| Domain/application literature | The practice context you study (education, accessibility, health...) | The reviewer who lives in that context |

The feeder-discipline lane is CHI-distinctive and the most common hole: a paper
measuring "trust" that cites no trust literature outside HCI, or one deploying
thematic analysis citing only its HCI users, reads as unserious to exactly the
reviewer the subcommittee recruited to check it.

## Position, don't inventory

The paragraph unit that survives review states a *front* — what the cited cluster
established, where it stops, and how your work moves it:

> Prior deployments of voice assistants with older adults established adoption
> barriers in home settings [x, y, z], but studied single-user households;
> multi-resident care contexts, where addressee ambiguity dominates, remain
> unexamined. We provide the first such deployment.

Three tests per paragraph: it cites ≥2 works in tension or sequence (else it is an
annotation), it ends with a gap or relationship claim, and deleting it would weaken
the introduction's contribution list. A related-work section whose paragraphs all
pass is *positioning*; anything else is coverage theater — and coverage theater at
excessive length also feeds the ADR-Contribution ground (small contribution relative
to paper length).

## Searching the field properly

The ACM Digital Library (now fully open access since January 2026) is the canonical
index for the HCI family; Google Scholar catches the feeder disciplines and preprints.

```text
Working queries (adapt per project):
- dl.acm.org: [Title: <construct>] AND [Conference: CHI] — filter to 2022-2026
- dl.acm.org: same construct in TOCHI + CSCW + ASSETS (the thread often lives
  in a sibling, published a year before the CHI wave)
- Scholar: <construct> + the feeder discipline's own term (e.g. "technology
  acceptance" vs "adoption"; "self-efficacy" vs "confidence")
- Forward-citation pass on your 3 closest papers — who cited them in the last
  two cycles is your actual competitive set
- arXiv/OSF preprint sweep for concurrent work; cite-and-distinguish preprints
  rather than pretending the lane is empty
```

Log the search date. Between September submission and the December 3 resubmission,
re-run the sweep — a five-week revision that misses a newly published near-neighbor
hands round-2 reviewers a free objection (`chi-author-response`).

## Distinguishing near-neighbors without combat

When a close paper exists (it does), CHI reviewers expect precise, generous
differentiation: name the axis of difference — population, setting, method,
theoretical lens, system capability — and what your position on that axis newly
shows. Dismissive comparisons ("however, they only...") backfire in a community
small enough that the neighbor may be your external reviewer.

## Self-citation under anonymity

CHI review is anonymized but your prior work is often the nearest neighbor. The
standing convention: cite yourself in the third person ("Building on the probe
deployed by [12]...") and never write "our previous study." Omitting your own
essential prior paper is worse than citing it — reviewers who find it later infer
concealment. Anonymize the *prose*, not the record. Link hygiene (no named
repositories in citations) is covered in `chi-submission`.

## Two structural choices that read as competence

- **Placement:** background the reader needs *before* understanding the study can
  come early (§2); comparisons that only make sense after seeing your findings can
  legitimately sit in the discussion ("our finding extends [x]'s account..."). CHI
  accepts both; choosing deliberately signals control.
- **Organization:** organize by intellectual front, never by venue or chronology.
  Section headings like "Trust in automation," "Voice interfaces in shared spaces"
  do positioning work; "Related work A/B/C" does not.

## Output format

```text
[Lane audit] CHI-recent: <n cited> · HCI-family: <n> · foundational: <n> ·
             feeder: <n> · domain: <n> — weakest lane: <which>
[Positioning test] paragraphs passing front-gap-relevance: <n>/<n>
[Nearest neighbors] <3 papers + the axis distinguishing each>
[Concurrent work] preprint sweep date: <date> — hits handled: yes/no
[Self-citation] third-person clean: yes/no
[ADR-Context exposure] low / medium / high — <reason>
```
