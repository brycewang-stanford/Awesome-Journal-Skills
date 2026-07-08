---
name: chi-writing-style
description: Use when drafting or revising the prose of an ACM CHI paper — contribution statements, structure for mixed reviewer audiences, participant voice, calibrated claims, accessible and bias-free writing, and length discipline in a venue that reviews words against contribution instead of pages.
---

# CHI Writing Style

A CHI paper is read by a jury that rarely shares one methodological culture: a
quantitative experimenter, a design researcher, and an ethnographer may all review
the same submission. The prose must therefore do explicit work that a single-culture
venue lets authors skip — naming the contribution type, justifying the method choice
to outsiders, and calibrating claims to human evidence. And because CHI reviews
length against contribution ("papers should be commensurate with their contribution";
5,000–8,000 words encouraged, per the CHI 2027 Papers page, read 2026-07-08), every
paragraph is auditable: does this paragraph earn its words?

## The contribution statement is load-bearing

CHI convention puts an explicit contribution list at the end of the introduction.
Write it first, keep it honest, and let it govern the paper:

```text
This paper contributes:
(1) <empirical finding>: the first interview study (n=24) of <population>
    doing <activity>, showing <the finding in one clause>;
(2) <artifact>: <system>, an open-source <what>, which embodies <the design claim>;
(3) <design implications>: five implications for <who>, grounded in (1) and
    tested against (2).
```

Each bullet must name its *type* (finding, artifact, method, theory — the taxonomy in
`chi-topic-selection`), its evidence, and its beneficiary. A bullet you cannot phrase
this way is not yet a contribution; cutting it now is cheaper than a reviewer doing
it in November.

## Section-by-section: what each reviewer culture checks

| Section | The question it must answer | Style failure that costs papers |
|---|---|---|
| Abstract | What was done, with whom, what was found | Motivation essay; findings withheld like a plot twist |
| Introduction | Why this, why now, contributions | Three pages of stage-setting before any claim |
| Related work | Where this sits in HCI's conversation | Annotated bibliography instead of positioning (`chi-related-work`) |
| Method | Enough to replicate and to trust | Narrative gloss; missing recruitment, analysis, ethics |
| Findings/Results | Evidence, organized by claim | Organized by chronology of what the team did |
| Discussion | So what — for design, theory, practice | Restating results with "interestingly" attached |
| Limitations | Honest scope boundaries | Ritual humility ("small sample") without consequences |

## Participant voice without ventriloquism

Quotes are evidence at CHI, and their handling is a style signature:

- Attribute with stable IDs (P7), balance across participants, and never let one
  articulate participant carry three themes.
- Interpret after quoting; a quote is not self-explanatory.
- Report speech faithfully but humanely — mark elisions, do not correct grammar
  silently, do not mock dialect through excessive `[sic]`.
- Describe people the way current bias-free-language guidance and the communities in
  question prefer (identity-first vs person-first varies by community — accessibility
  research has explicit norms; when studying a specific community, follow *its*
  stated preference and say so).

## Calibration is the house register

HCI findings are situated. The credible CHI register scopes claims in the sentence
that makes them, not only in the limitations section: "participants in our two-week
deployment", "for information-seeking tasks like ours", "we observed, among these
24 U.S.-based teachers". Reviewers punish two opposite failures — universal claims
from situated studies, and findings hedged into vapor. The discipline: one claim
sentence per finding, scoped, in active voice, with the evidence pointer attached.

## Write for the ear and the screen reader

Accessibility is a review-community value and a camera-ready requirement
(`chi-camera-ready`), and it starts in drafting: expand every acronym at first use,
keep sentences parseable when heard rather than seen, never encode meaning purely in
color or spatial position ("the red bars", "as seen on the left"), and write figure
references that work without the figure ("error rates halved (Fig. 3)" not "see
Fig. 3"). These habits also serve the many CHI reviewers reading in their second or
third language.

## Length discipline in a no-page-limit venue

No maximum length means the *justification* is on you. Practical passes:

- Run `texcount -inc -sum main.tex` at every full draft; drift above ~8,000 words
  needs a reason you could state to a reviewer, and 12,000+ risks desk rejection
  (`chi-submission`).
- The three chronic bloat sites in CHI drafts: related work written as coverage
  proof (halve it by making every citation do positioning work), methods detail
  that belongs in the supplement (move instruments out, keep decisions in), and
  discussion sections that re-narrate findings (each discussion move must add an
  implication, comparison, or consequence).
- Short papers (<5,000 words) are a legitimate, reviewed-to-scale form — cutting to
  short is often the strongest move for a single clean finding.

## Output format

```text
[Contribution statement] <n> bullets, each typed+evidenced: yes/no
[Audience test] method justified for non-specialist reviewer: yes/no
[Claim calibration] unscoped universals found: <list or none>
[Voice] quote balance across participants: ok / dominated by <IDs>
[Accessible prose] acronyms, color-independence, hearable sentences: pass/fail
[Word count] <n> words — verdict: short / standard / justify / cut
```
