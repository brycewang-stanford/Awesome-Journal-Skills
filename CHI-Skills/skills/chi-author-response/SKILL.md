---
name: chi-author-response
description: Use when an ACM CHI paper receives a revise-and-resubmit invitation and the five-week window opens — planning the revision triage, making tracked changes reviewers can audit, and writing the response letter that carries the paper through round 2 and the PC meeting.
---

# CHI Author Response

CHI does not run a short rebuttal where you argue in a text box. An invited paper gets
roughly **five weeks** to deliver two artifacts: a genuinely revised manuscript with
changes visibly tracked, and a response letter mapping every reviewer concern to what
changed. For CHI 2027 the resubmission deadline is **December 3, 2026** (posted on
chi2027.acm.org, read 2026-07-08). The stakes are real: the posted process warns up to
50% of revised papers may still be rejected; CHI 2026 accepted 65.5% of resubmissions.

## The first 48 hours: triage, not writing

Read all reviews twice, write nothing outward, then sort every distinct criticism:

| Triage class | Test | Response strategy |
|---|---|---|
| Must-fix | Named by the 1AC meta-review or ≥2 reviewers | Change the paper substantively; show the diff |
| Cheap win | Clarity, missing citation, terminology, figure | Fix all of them, every single one |
| Analysis request | Wants a new analysis of *existing* data | Run it if the pipeline is alive; report honestly either way |
| New-study request | Wants data you cannot collect in five weeks | Do not fake it; scope the claim down instead and say so |
| Misreading | Reviewer misunderstood something actually present | Treat as your writing defect: fix the text, then point to it |
| Genuine disagreement | Legitimate difference of research values | Push back once, respectfully, with evidence and citations |

The meta-review is the priority list. Reviewers at CHI re-read revisions against their
own round-1 comments, and the PC meeting discusses the 1AC's summary of how well you
responded — not the eloquence of your prose.

## Revising so the diff does the arguing

The instructions ask for a revision with tracked changes — highlighted, conventionally
in color — plus the response letter. Make the audit trail mechanical:

```bash
# LaTeX: generate the tracked-changes PDF from the submitted vs revised source
latexdiff --type=CULINECHASE submitted/main.tex revised/main.tex > diff.tex \
  && latexmk -pdf diff.tex
# Sanity: confirm the revision still respects CHI length norms after additions
texcount -inc -sum revised/main.tex | tail -3
# Keep anonymization intact through round 2 — new text leaks too
pdftotext revised/main.pdf - | grep -nEi 'our (lab|university)|github\.com/[a-z]' | head
```

Five weeks invites over-revision. Do not restructure sections no reviewer questioned,
and do not let the word count balloon past what the contribution justifies — length
norms still apply at resubmission, and a bloated revision reads as panic.

## The response letter

Structure it per reviewer, with numbered items quoting or precisely paraphrasing each
concern, in the reviewers' own order. For each item: what changed, where (section and
page in the revised PDF), and — where relevant — one sentence of substance. A workable
skeleton:

```text
Response to Reviews — Submission #1234
Summary of changes: <5-8 bullets, the big moves only>

R1.1 "<concern>" → Revised §4.2 (p.7): we now report <what>. <One sentence of
     substance or evidence.>
R1.2 "<concern>" → We respectfully keep <choice> because <evidence/citation>,
     and now state this rationale explicitly in §3.1.
2AC.1 ...
```

Tone rules that decide borderline cases at the PC meeting:

- Thank reviewers once, globally; do not lard every item with gratitude.
- Never write "the reviewer is wrong." Write what the paper now says and where.
- Concede real limitations plainly and move them into the limitations section —
  reviewers reward honesty at CHI more reliably than at most venues, because study
  limitations are expected in human-subjects work.
- If two reviewers conflict, name the conflict neutrally and state which path you
  took and why, so the 1AC can resolve it rather than rediscover it.

## What you may and may not change

The revision is expected to *respond to the reviews*; it is not a fresh submission.
Safe: new analyses of existing data, reframed claims, restructured argument, improved
figures, expanded related work, fixed statistics. Risky without flagging: changing the
core claims, swapping the method story, adding an entirely new study — if the paper
needed those, discuss withdrawing and resubmitting next cycle instead, because the
same review team will judge whether the new material was reviewed properly. Author
lists and anonymization rules stay as they were (待核实 for edge cases: check the
current cycle's instructions before touching authorship).

## If you decide not to resubmit

Withdrawing is legitimate — 27 of 2,603 invited CHI 2026 papers did not return. Do it
formally in PCS, keep the reviews, and fold them into the next venue's draft while
they are fresh. An RR invitation you decline is still market information: the paper
was in the top ~39% of a 6,700-paper pool.

## Output format

```text
[Window] opens <date> → due 2026-12-03; days remaining: <n>
[Triage] must-fix: <n> / cheap: <n> / analysis: <n> / out-of-scope: <n>
[Meta-review demand] <the 1AC's central ask, one line>
[Riskiest item] <the concern you cannot fully satisfy + chosen strategy>
[Deliverables] tracked-changes PDF ✓/✗ · response letter ✓/✗ · length re-check ✓/✗
```
