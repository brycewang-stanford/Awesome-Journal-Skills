---
name: jacs-cover-letter
description: Use when drafting the cover letter to the editor for a Journal of the American Chemical Society (JACS) manuscript — stating the advance, broad interest, and fit. Drafts the editor-facing pitch — it does not assess the underlying chemistry.
---

# Cover Letter to the Editor (jacs-cover-letter)

## When to trigger

- The manuscript is ready and you need the cover letter for Paragon Plus
- You must justify broad interest and JACS fit to the handling editor
- You need to disclose related/prior submissions or overlapping work
- You want to flag suggested or excluded reviewers in the letter

## What the editor decides from the letter

The handling editor triages on **broad interest and fit** before sending to
review. The cover letter is your one paragraph to make that case clearly — it
complements, never repeats, the abstract.

## Structure (short, one page)

1. **Submission line** — manuscript type (Article/Communication), title, intended for JACS.
2. **The advance in one or two sentences** — what is new, stated for a general chemistry readership.
3. **Why JACS (broad interest)** — the breadth driver (generality / concept / enabling utility) and who beyond your subfield will care.
4. **Key evidence** — one line on the decisive support (e.g., scope + X-ray + kinetics), signaling rigor.
5. **Integrity statements** — original, not under consideration elsewhere; any prior preprint/related submission disclosed; conflicts and funding noted as required.
6. **Optional** — suggested reviewers and any justified exclusions (see `jacs-referee-strategy`).

## Tone and content rules

- Confident but evidence-anchored; no hype the manuscript can't back up.
- Editor-facing, not reviewer-facing: focus on significance and fit, not method minutiae.
- Honest about format choice (why Communication if urgent/high-impact).
- Disclose overlap with prior work, preprints, or companion submissions explicitly.

## Checklist

- [ ] Manuscript type and title stated; addressed to JACS editors
- [ ] Advance stated in ≤2 sentences for a general chemistry audience
- [ ] Broad-interest case made (named breadth driver + audience)
- [ ] One line of decisive evidence signals rigor
- [ ] Originality / no-concurrent-submission statement included
- [ ] Preprint, prior, or companion work disclosed if applicable
- [ ] Conflicts/funding handled per current ACS requirements
- [ ] Suggested/excluded reviewers added if used

## Anti-patterns

- Copy-pasting the abstract instead of pitching significance and fit
- Hype ("groundbreaking", "paradigm-shifting") not supported by data
- Omitting disclosure of a preprint or a closely related submission
- A page of methodological detail the editor does not need at triage
- Excluding reviewers without a brief, professional justification


## Operating pass for Journal of the American Chemical Society

Treat this skill as an executable review pass, not a prose hint. First lock the chemical novelty, characterization chain, controls, and scope or mechanism evidence; then judge whether the current manuscript answers the venue's real reader: chemistry reviewers who expect a molecule/material/reaction claim to be supported by rigorous characterization and mechanistic insight.

- **Do the pass:** Return a claim-evidence-risk ledger rather than a prose-only diagnosis; every recommendation must point to a manuscript location or missing artifact.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against ACS Central Science for broad conceptual reach, Angewandte for communication style, specialized ACS journals for narrower chemistry; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Type/title】Article|Communication — <title>
【Advance】≤2 sentences
【Broad interest】driver + audience
【Decisive evidence】one line
【Disclosures】original / preprint / related / conflicts — status
【Reviewers】suggested: [...]; excluded (reason): [...]
【Next】jacs-submission
```

## Related resources

- [`jacs-referee-strategy`](../jacs-referee-strategy/SKILL.md) — choosing suggested and excluded reviewers
- [`../jacs-submission/templates/checklist.md`](../jacs-submission/templates/checklist.md) — full submission preflight
