---
name: acl-topic-selection
description: Use when deciding whether a project fits ACL versus EMNLP, NAACL, EACL, TACL, Computational Linguistics, COLM, or an ML venue, covering contribution typing for NLP work, long-versus-short paper choice, the annual theme track, Findings-tier expectations, and sharpening the computational-linguistics framing before writing starts.
---

# ACL Topic Selection

Use this before the first draft. ACL is the flagship of the \*ACL family:
broadest scope across computational linguistics and NLP, the most competitive
main-program bar, and — under ACL Rolling Review — a venue choice you finalize
at *commitment* time, which gives topic strategy an unusual second chance.

## What ACL rewards

- A contribution about **language**: modeling it, measuring it, resourcing it,
  or explaining how systems process it — with the linguistic question visible,
  not incidental.
- Typed contributions reviewers can classify fast: method, resource,
  evaluation/metric, analysis, theory, or position. Papers that are half
  method and half unvalidated resource read as neither.
- Evidence proportional to breadth (see `acl-experiments`) and an error
  analysis that says something about language, not just scores.
- Work engaging the current field conversation — for ACL 2026, the special
  theme was explainability of NLP models, with a dedicated Thematic Paper
  Award; each edition names its own theme.

## Family routing

| Signal | Better home |
|---|---|
| Core NLP contribution, broad audience, strongest possible reviews wanted | ACL (or whichever \*ACL your ARR package is eligible to commit to) |
| Empirical, engineering-forward NLP; dense experimental papers | EMNLP — historically the empirical sibling, same ARR pipeline |
| Regional relevance, or timing fits its cycle windows | NAACL / EACL / AACL |
| Needs >9 pages, revision-based journal reviewing, no conference clock | TACL (journal, also Anthology-published) |
| Survey-scale or theoretical linguistics depth | Computational Linguistics (journal) |
| LLM-centric work thin on language questions | COLM or an ML venue (NeurIPS/ICML/ICLR) |
| Deployed-system lessons, product constraints | ACL industry track — separate CFP and deadlines |
| Early-stage, student-led | ACL Student Research Workshop |

Because commitment is decoupled, "ACL vs EMNLP" is often not a submission-time
decision: submit to ARR when ready, then commit to the conference whose window
and bar the finished package fits.

## Long or short

- Long (8 pages): a complete arc — method or resource, evaluation, analysis.
- Short (4 pages): one falsifiable point with one decisive experiment; a
  negative result, a focused analysis, an evaluation flaw demonstrated.
  Short papers are judged as short papers — reviewers reject compressed long
  papers but reward genuinely small, sharp claims.

## Fit sharpening before writing

1. Write the one-sentence claim naming the linguistic object: task,
   phenomenon, language set, or evaluation practice.
2. Name the reviewer community: who at ACL wants this answer? If the honest
   answer is "ML engineers," reconsider the venue or reframe toward the
   language question.
3. Check the theme track: a solid paper matching the year's theme gains a
   natural reviewer pool and an award lane.
4. Stress-test the Findings scenario: would a Findings acceptance satisfy
   the project's goals? If not, ask what would push it into the main program
   — usually analysis depth or evaluation breadth — and plan that now.
5. Verify novelty against the last two \*ACL rounds specifically
   (see `acl-related-work`); ACL's most common fit failure is a project
   scooped between conception and cycle deadline.

## Vignette: routing an LLM evaluation project

A team measures whether chat models track discourse referents across long
dialogues. Framed as "LLM long-context benchmark #47," it drifts toward COLM.
Framed with the linguistic object first — anaphora resolution under distance,
with typologically varied test languages and a coreference-aware error
taxonomy — it becomes an ACL analysis paper, and the benchmark becomes a
resource contribution with a data statement. Same experiments; the venue fit
is decided by which question the paper asks.

## Anti-fit signals worth trusting

- The paper's interest evaporates if a specific commercial model updates —
  a snapshot artifact, not a finding about language or method.
- No error analysis is imaginable because outputs are only scores — the
  project measured something but cannot yet explain anything.
- The "multilingual" plan is English plus machine-translated test sets with
  no native-speaker validation — reviewers treat this as English squared.
- The contribution is a wrapper around an API with prompt engineering as
  the method — workshops and system demos exist for exactly this.
- The dataset section cannot answer license and consent questions — fix
  the resource before choosing any venue (see `acl-artifact-evaluation`).

## Questions that settle borderline calls

1. Which existing ACL paper would cite this one first, and in which
   section — methods, data, or related work? No answer means no audience.
2. Does the claim survive being scoped to the tested languages and models?
   If the honest scoped version sounds trivial, the work is not done.
3. Is the evaluation itself a contribution? If yes, consider leading with
   it — evaluation and analysis papers are a strong current at ACL.
4. Could the short-paper version carry the whole point? If yes, submitting
   long dilutes it across pages reviewers will judge as padding.

## Theme-track fine print

- Theme submissions ride the same ARR pipeline and format rules; the theme
  is a reviewing lane and award category, not a separate venue.
- Fit is judged on whether the paper *answers* the theme question, not on
  keyword overlap — retrofitting a theme paragraph onto an unrelated paper
  is transparent to theme-track reviewers.
- Themes change annually and are announced in each edition's call; never
  assume last year's theme (or its reviewer pool) carries over.

## Output format

```text
[Fit] strong ACL / possible ACL / sibling venue / non-*ACL venue
[Contribution type] method / resource / evaluation / analysis / theory / position
[Format] long / short / industry / SRW / theme-track
[Claim sentence] <one sentence with the linguistic object named>
[Scoop check] <nearest recent work + standing delta>
[Route decision] <submit cycle X, commit target Y, fallback Z>
```
