---
name: interspeech-supplementary
description: Use when deciding what accompanies an INTERSPEECH paper beyond its 4 pages — audio sample pages and multimedia for listening-based judgment, what reviewers may ignore versus must see, the references-and-acknowledgments page's strict scope, and packaging extra analyses when no reviewed appendix exists.
---

# INTERSPEECH Supplementary Material

Interspeech's supplement story is inverted from big-ML venues: there is **no
reviewed appendix**. A regular paper is 4 pages of content plus one page for
references and acknowledgments only — everything else is optional accompaniment
that reviewers may open but never owe you. Design the paper to stand alone, then
design the accompaniment to be irresistible. (Long Papers, new in 2026, follow
their own reported 8+2 contract — verify before assuming appendix room.)

## The three shelves

| Shelf | What lives there | Review status |
|---|---|---|
| The 4 pages | Every claim, the decisive table, the assumption set, protocol one-liners | Reviewed; the paper *is* this |
| References/acks page | Citations; acknowledgments (camera-ready only) | Policed — nothing else allowed |
| Accompaniment | Audio demo page, code repo, extended tables, media attachments | Optional reading; anonymity rules apply |

The classic failure: a decisive ablation "in the demo page" that a reviewer never
opens, followed by a review saying the claim is unsupported. If the paper's fate
depends on it, it goes in the 4 pages — compression is the skill (see
`interspeech-writing-style`), not relocation.

## Audio: the supplement that actually gets consumed

Interspeech is the one major venue where reviewers routinely *listen*. For
synthesis, conversion, enhancement, and separation papers, the sample page is
effectively part of the evidence:

- Curate like an experiment, not a highlight reel: same utterances across systems,
  including the baseline and the failure cases your error analysis discusses.
- Label conditions exactly as the paper's tables do, so a listener can map sample
  → table row in seconds.
- Keep it short: reviewers give minutes, not hours. Ten well-chosen triplets beat
  a hundred files.
- Cherry-picking is detectable and remembered; note explicitly whether samples are
  random or selected, and match the paper's claim ("randomly drawn from test").
- Anonymity: neutral hosting, clean metadata, no lab-identifiable voices — the full
  sweep in `interspeech-artifact-evaluation` applies to every linked byte.

## Attachments vs links

Cycles differ on whether media files may be attached in CMT and what the size cap
is — check the current author instructions rather than assuming. Attached media is
frozen and safely anonymous; linked pages are richer but riskier (identity,
mutability). When policy is unclear: attach the minimum decisive audio, link the
rest, freeze both.

## Extended analyses without an appendix

Where an AISTATS or NeurIPS author would write "App. C", an Interspeech author
chooses:

1. **Compress into the body** — one row, one sentence, one footnote-density claim.
2. **Cite the arXiv extended version** — but only outside the anonymity period and
   per the current preprint policy; during review this is usually unavailable.
3. **Repo `RESULTS.md`** — full sweeps, per-language tables, negative results;
   discoverable post-acceptance, invisible to review.
4. **Save it for the Long Paper track or a journal extension** (TASLP, CSL, Speech
   Communication) — Interspeech-to-journal extension is a standard community path.

Pick consciously per artifact; the default of "dump everything in the repo" leaves
reviewable evidence outside the review.

## A sample-page layout that respects reviewer time

```text
Anonymous demo — Paper #1234
Section 1: Main comparison (Table 2 systems, 6 utterances × 4 systems)
  utt-01  [GT] [Baseline] [Ablation] [Proposed]     ← same grid every row
Section 2: Failure cases discussed in Sec 4.3 (3 utterances)
Section 3: Operating points (320/480/640 ms, 2 utterances each)
Selection: utterances drawn randomly from test; seed 17.
```

The grid mirrors the paper's tables, failure cases are volunteered rather than
hidden, and the selection policy is printed on the page itself. A reviewer can
audit the audio claims in under five minutes — which is the entire budget you
realistically have.

## Media-file craft

- Normalize loudness across systems before publishing; a louder system "wins"
  MOS-by-ear unfairly and reviewers know the trick.
- Same utterance text, same speaker (where applicable), same sample rate across
  systems — any mismatch invites suspicion of stacked comparisons.
- Keep individual clips short (3–8 s); attention decays per clip, and short
  clips force you to choose genuinely diagnostic material.
- Provide file-level captions ("proposed, 480 ms, repair-bearing"), never bare
  `audio_final_v2.wav` names.

## Packaging checklist

```text
[ ] Paper stands alone: no claim depends on unreviewed material
[ ] Sample page: same utterances across systems, failure cases included,
    selection policy stated, mapped to table rows
[ ] Hosting anonymous, page frozen, media metadata scrubbed
[ ] Attachment rules of the current cycle checked (size, formats)
[ ] References page contains references (and, at camera-ready, acks) only
[ ] Extended-material route chosen: body / arXiv-later / repo / journal
```

## Output format

```text
[Shelf audit] what sits on each shelf; anything decisive off-page?
[Audio evidence] curation quality, selection policy, anonymity result
[Attachment plan] attach vs link, per current-cycle rules (cite source)
[Overflow route] compress / arXiv / repo / Long Paper / journal — per item
[Risk] <the unreviewed item most likely to be assumed reviewed>
```

Current-cycle attachment and preprint rules were checked 2026-07-08 against the
Interspeech 2026 author pages via renderings (`resources/official-source-map.md`);
the anonymity-period wording there governs anything you host.
