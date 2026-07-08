---
name: cscw-related-work
description: Use when positioning a CSCW paper's related work — engaging the venue's own concept lineage, the PACMHCI-era literature, neighboring HCI venues, and the social sciences CSCW borrows from, with era-correct citations and anonymity-safe self-references for journal-model review.
---

# CSCW Related Work

Related work at CSCW is not a defensive perimeter; it is where the paper joins a
forty-year conversation. Reviewers here are unusually likely to *be* the authors of
the traditions you cite, to know the concept lineage personally, and — because of
Revise and Resubmit — to check in round two whether the engagement you added in
round one is real.

## The four literatures to braid

| Literature | What reviewers check | Failure smell |
| --- | --- | --- |
| CSCW's own lineage | That you know the concept history (awareness, articulation work, incentive misalignment, place/space) before renaming a piece of it | "We introduce the novel notion of..." for an idea with a 1992 citation |
| Recent PACMHCI-era CSCW work | Engagement with the last ~3-5 years of the venue on your topic | A related-work section whose newest CSCW citation predates the journal era |
| Neighboring venues | CHI, ICWSM, GROUP, DIS, and TOCHI work on the same phenomenon, cited by contribution rather than lumped | Treating a CHI interface study and a CSCW practice study as interchangeable |
| Source disciplines | The sociology, organization studies, communication, or STS work your framing borrows | Invoking a social theory via a secondary HCI citation only |

Braiding matters more than coverage: a paragraph per literature, each ending in what
*this* paper takes from or contests in it, beats an alphabetical tour.

## Era-correct citation of CSCW itself

CSCW's publication record has a seam in it, and sloppy citations tear on the seam:

- **Before 2017:** conference proceedings papers — "In Proceedings of CSCW '96."
- **2017 onward:** journal articles — "Proc. ACM Hum.-Comput. Interact., Vol. 1,
  No. CSCW, Article 31." There is no "Proceedings of CSCW 2019" for papers; a
  bibliography entry claiming one signals the authors have not read carefully.
- Verify each CSCW citation on dblp (`conf/cscw` stream) or the ACM DL PACMHCI
  CSCW track; fix venue strings your reference manager guessed.

The Lasting Impact lineage in `resources/exemplars/library.md` doubles as a spine
for concept-history paragraphs: if your topic touches failure-of-adoption, cite
through Grudin 1988; awareness, through Dourish & Bellotti 1992; place and presence,
through Harrison & Dourish 1996; sensitive-community storytelling, through Dimond et
al. 2013; moderation at platform scale, through the PACMHCI-era trace canon.

## Positioning moves that survive re-review

- **Contest, don't just cite.** "Unlike X, we find..." is only safe when you can
  name the condition that explains the difference; otherwise write "extending X to
  a setting where..."
- **Give every neighboring-venue citation a job.** A CHI citation should mark the
  interaction-level boundary of your claim; an ICWSM citation should mark the
  measurement baseline you build past.
- **Import theory at the source.** If Suchman, Star, Goffman, or Ostrom is doing
  analytic work in your paper, cite and quote the primary text; reviewers from the
  source discipline will notice a chain of second-hand paraphrases.
- **Date your snapshot.** For fast-moving topics (moderation policy, AI-mediated
  collaboration), state when the literature search closed — the R&R gap can span
  most of a year, and round-two reviewers may expect newer work acknowledged.

## Self-citation under anonymous journal review

Submissions are anonymized. Your own prior work must be cited in the third person
("Building on the deployment reported by [12]...") and must not be the only
scaffolding the argument stands on — a paper that cites one anonymous-adjacent
thread six times deanonymizes itself structurally even with names removed. If prior
work is on arXiv or a personal site, do not link it in a way that resolves identity.

## Audit block

```text
[Lineage]    Oldest CSCW concept engaged: <paper, year> — engaged or name-dropped?
[Recency]    Newest CSCW/PACMHCI citation: <year>; search-close date stated? y/n
[Neighbors]  CHI/ICWSM/GROUP/DIS citations each given a boundary-marking job? y/n
[Sources]    Primary-text citation for each imported theory? y/n
[Era check]  All post-2017 CSCW refs cite PACMHCI vol/issue/article? y/n
[Anonymity]  Self-citations third-person, load-bearing count ≤ 2? y/n
```

Re-run the audit at every R&R: reviewers who asked for missing literature will read
the new paragraphs first, and they can tell insertion from integration.

Citation-form facts verified against the ACM DL and dblp on 2026-07-08.
