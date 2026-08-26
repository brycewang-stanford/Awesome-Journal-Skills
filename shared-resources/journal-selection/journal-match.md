# Journal-Match — from an abstract to a ranked submission shortlist

A cross-journal capability: given a paper (or just an abstract + a few facts), produce a
**ranked shortlist of target venues** with a reach / match / safe split and a
**resubmission ladder** for if the first target rejects. It spans the whole repository —
all **744 venues** are in [`venue-index.tsv`](venue-index.tsv), whether they have their
own depth pack (290) or are profiled inside a discipline breadth bundle (454).

> **What this is and is not.** This file is the *matching methodology* + a stable venue
> index. It does **not** restate volatile facts (APC/fees, acceptance/desk-reject rates,
> turnaround, page limits) — those live in each pack's
> `resources/official-source-map.md`, kept current by the live-check campaign. Read them
> **at match time**; never quote a fee or an acceptance rate from memory.

---

**Worked end to end:** [`worked-example.md`](worked-example.md) runs one paper through
all six steps with the real tool output.

## When to use

- The author has a result/draft and asks "where should I send this?"
- A paper was just rejected and needs the best next target ("downgrade ladder").
- A reviewer/editor suggested the paper is "not a fit" and the scope needs rethinking.

## Step 1 — Profile the paper (extract five signals)

Write these down **once**, in the shape of [`paper-profile.md`](paper-profile.md). Every
downstream skill reads that file rather than re-deriving the five signals from the
manuscript — three readings of one paper produce three slightly different papers, and
the disagreement shows up as advice that contradicts itself.

From the abstract / draft, pin down:

1. **Discipline + subfield** — maps to the `discipline` column of `venue-index.tsv`
   (e.g. `finance`, `economics/labor`, `sociology`, `marketing`, `information-systems`).
2. **Method / design** — DiD / IV / RDD / structural / lab-experiment / survey-SEM /
   qualitative / theory / meta-analysis. Determines empirical-`lane` fit and which
   venues' bars you can clear.
3. **Contribution type** — new fact, new mechanism, new method, new theory, replication,
   policy evaluation. Different venues reward different types (a pack's
   `*-topic-selection` / `*-contribution-framing` skill is the authority on this).
4. **Setting / data / region** — country, dataset, proprietary vs public (drives the
   `region` column: `international` vs `china`, and data-policy feasibility).
5. **Ambition / strength** — how general-interest and how clean the identification is.
   Calibrates reach vs safe (be honest here; over-reaching wastes months).

## Step 2 — Build the candidate set (run the matcher)

```bash
python3 tools/match_venues.py \
    --title "..." --abstract "..." \
    --discipline economics/labor --lane empirical --top 15
```

This step used to read "filter the index by discipline, then narrow on
`scope_keywords`" — an instruction carried out by eye, differently every time, over a
570 KB file. It is now a command, for three reasons: it is reproducible, it searches the
full 900-term scope vocabulary per venue rather than the 40 published in the index, and
it is **the same code path the evaluation scores**, so the number in
[`eval/RESULTS.md`](eval/RESULTS.md) describes what you actually ran.

It searches **two** vocabularies per venue, and the difference between them matters when
you read a result. The scope vocabulary comes from the venue's pack — prose about a
*process*. The subject vocabulary ([`topic-postings.tsv`](topic-postings.tsv)) comes from
the titles of articles the venue *published* — words about a *subject*, which is the
register your query is in. Not every venue has the second one: where no bibliographic
source could be resolved, the candidate is marked `°` and the matcher warns that part of
the shortlist was searched over less evidence than the rest. Treat a `°` venue's low
placement as a gap in the index, not as a judgement about fit.

Useful flags: `--only-discipline` to hard-filter when you are certain,
`--exclude <venue_id>` for venues that already rejected the paper, `--lane` / `--region`
/ `--venue-type` / `--coverage` to narrow, `--json` to pipe, `--list-disciplines` for the
vocabulary.

**`--discipline` is a prior, not a filter.** The discipline and its adjacents
([`discipline-adjacency.tsv`](discipline-adjacency.tsv), derived from the venue graph —
a labour paper reaches general `economics` and `economics/public` automatically) are
boosted, but a strong match elsewhere still surfaces. Getting Step 1 right is worth a
lot — a correct discipline lifts recall@10 from 46.7% to 55.7%, and to 70.8% if you
trust it enough to filter — but a wrong guess under a hard filter deletes the right
answer outright, which is why the default is soft.

Each row reports the terms it matched on. **Read them.** A candidate that scored on one
generic word is not a candidate; the matched terms are there so that a nonsense hit is
visible as one. Scope terms are *derived, not curated*: a hit is a reason to open the
venue's profile, never a fit judgement on its own.

The matcher raises two warnings, and both mean *stop and re-aim* rather than *proceed
carefully*:

- **Weak evidence** — the leading candidates each matched one or two words. Words the
  language reuses across fields will beat a real subject match at that depth; a paper on
  a cytosolic DNA *sensor* is offered sensor-network conferences. Add the abstract.
- **Coverage gap** — nothing in the discipline you named scored at all. The prior can
  only re-rank venues that matched, never conjure one, so what you are looking at is
  another field's venues. Check the discipline label, and if the subject area really is
  thin here, say so (hard rule 4) instead of recommending what happened to surface.

Coverage is uneven by discipline, and [`eval/RESULTS.md`](eval/RESULTS.md) publishes the
breakdown. Life sciences and natural science are the thinnest: those packs describe how
to *submit* in far more detail than what the venue is *about*, so a molecular-biology
title often shares no vocabulary with its own journal.

Every venue is in the index. `coverage` tells you what you will find behind it:
`depth` → a full pack with a live-checked `source_map`; `breadth` → a single venue
profile at `profile_path` carrying fit, framing, evidence bar, house style and
desk-reject triggers in condensed form.

## Step 3 — Score each candidate (five dimensions)

For each candidate, open its `source_map` (and, where deeper judgment is needed, its
`*-topic-selection` / `*-workflow` skill) and score:

| Dimension | What to read | Higher score = |
|---|---|---|
| **Fit** | the pack's scope / topic-selection skill + source-map scope notes | the paper's question & contribution type are squarely in scope |
| **Acceptance odds** | desk-reject + acceptance rate in the source-map, vs. the paper's strength (Step 1.5) | realistic given the design's cleanliness and general interest |
| **Turnaround** | first-decision / review-time figures in the source-map | faster first decision (matters under job-market / tenure clocks) |
| **Cost / policy** | APC / submission fee + data-&-code policy in the source-map | affordable and feasible to comply (proprietary data ⇒ check disclosure rules) |
| **Audience** | the venue's readership (general-interest vs specialist) | reaches the readers the contribution needs |

Combine into an overall judgment — **do not invent a precise weighted number**; the
inputs (especially acceptance odds) are uncertain. Use the scores to *sort and tier*,
and state the reasoning.

## Step 4 — Output a reach / match / safe shortlist

Return **3 tiers, ~2–3 venues each**, each with a one-line rationale and the live facts
that matter:

- **Reach** — top venues where Fit is high but acceptance odds are long; worth it if the
  result is genuinely general-interest.
- **Match** — strong Fit and plausible odds given the paper's strength; the primary
  targets.
- **Safe** — high Fit, higher acceptance odds, faster turnaround; a credible home that
  protects the timeline.

Sequence them: submit top-down, and pre-write the resubmission ladder.

## Step 5 — Long-tail coverage (breadth bundles)

Long-tail venues are covered as per-venue **profiles** inside the discipline breadth
bundles. They are **already rows in `venue-index.tsv`** (`coverage = breadth`), so
Step 2 shortlists them like any other venue; follow `profile_path` to read the profile
before recommending. The bundles and what they cover:

| Bundle | Covers |
|---|---|
| `English-SocialScience-Journal-Skills` | ~100 English econ / finance / management / accounting / marketing / OM / IS journals |
| `English-NaturalScience-Journal-Skills` | ~154 English natural-science / clinical / physical / formal-science journals |
| `Chinese-SocialScience-Journal-Skills` | ~100 Chinese social-science journals |
| `Computer-Science-Conference-Skills` | ~155 CS/AI conferences |
| `Engineering-Technology-Journal-Skills` | ~40 engineering / technology journals |
| `Agriculture-Environment-Journal-Skills` | ~30 agriculture / environment / earth-science journals |
| `Clinical-Medicine-Journal-Skills` | ~30 clinical specialty journals |
| `English-Humanities-Journal-Skills` | ~36 English humanities journals |
| `Chinese-Sport-Science-Journal-Skills` | ~12 Chinese sport-science journals |

## Step 6 — The resubmission ladder (after a reject)

Rejection is the modal outcome at the top — plan for it up front.

Start from [`ladder.tsv`](ladder.tsv), which records, for each venue, the other venues
its own pack names as siblings or alternatives (`mentions` = how often;
`same_discipline` flags the safest rungs). This is **candidate adjacency, not a
ranking** — it tells you which venues the people who know this one treat as neighbours,
and nothing about your paper. Filter it, then apply the judgement below.

Build a **downgrade ladder**: from the reach/match target, the next rung is the venue
that (a) keeps the
contribution's audience, (b) has materially higher acceptance odds or faster turnaround,
and (c) needs the *least* reframing. Note what each rung would require (e.g. shorter
format, added robustness, a policy-framing). A desk reject at a general-interest venue
often re-aims cleanly to a strong field journal; a referee reject usually means address
the binding objection (via the pack's `*-robustness` / `*-identification` skill) before
re-sending.

Then **cost the ladder**, because the sequence is what spends the year, not the venue:

```bash
python3 tools/ladder_ev.py \
    --rung "Journal of Finance:0.05:4.5" \
    --rung "Review of Financial Studies:0.08:5.0" \
    --rung "JFQA:0.20:3.5" --rung "Journal of Banking and Finance:0.35:2.5"
```

It returns expected months, the probability of placing at all, and the probability of
running the ladder out — with a sensitivity band, because `p_accept` is a judgement and
not a measurement. See [`rt-ladder-ev`](../../Research-Toolkit-Skills/skills/rt-ladder-ev/SKILL.md).

---

## Output format

```
【Paper profile】discipline / method / contribution / setting / ambition
【Reach】  V1 — why; key live facts (desk-reject, turnaround, fee) · V2 — …
【Match】  V3 — why; key live facts · V4 — …
【Safe】   V5 — why; key live facts · V6 — …
【Submit order & ladder】V_top → if reject → V_next (what to change) → …
【Open questions】(facts to re-verify in the source-map before submitting)
```

## Anti-patterns

- Quoting a fee, APC, acceptance rate, or page limit **from memory** — always read the
  pack's `official-source-map.md` (volatile; live-checked).
- Recommending only reaches (wastes the timeline) or only safes (undersells the paper).
- Ignoring `lane` — sending a qualitative or theory paper to an empirical-only venue.
- Treating the `tier` column as a precise ranking — it is an indicative bucket
  (`top-5 econ`, `top-3 finance`, `FT50/UTD24`, `field`), not a score.
- Overriding a pack's own `*-topic-selection` judgment of fit — defer to it.

## Hard rules

1. **Live facts from the source-map, never from memory.** Fees / acceptance / turnaround
   / page limits / data policy are read at match time.
2. **Fit judgment defers to the venue's own skill** (`*-topic-selection` /
   `*-contribution-framing`); this file only shortlists and sequences.
3. **Be honest about odds.** Don't inflate a paper into a reach it cannot clear, or
   bury a realistic match.
4. **Coverage honesty.** If a plausible venue is outside the index and its breadth bundle,
   say so rather than forcing a poor fit — and route to
   [`rt-venue-integrity`](../../Research-Toolkit-Skills/skills/rt-venue-integrity/SKILL.md)
   before the author submits somewhere this repository cannot vouch for.
5. **The matcher retrieves; you recommend.** Its ranking is a reading list. Nothing
   reaches the author that you have not read the pack for.

---
*Runs on: [`tools/match_venues.py`](../../tools/match_venues.py) (step 2) and
[`tools/ladder_ev.py`](../../tools/ladder_ev.py) (step 6).
Stable index: [`venue-index.tsv`](venue-index.tsv) (744 venues) and
[`ladder.tsv`](ladder.tsv) (1,511 adjacency edges) — both generated from the repository;
regenerate when packs are added. Retrieval quality is measured in
[`eval/`](eval/README.md). Volatile facts: each pack's `resources/official-source-map.md`.
Part of the cross-journal capability layer — the loop is **pick** (this file) → **execute**
([`../empirical-methods/execution-with-mcp.md`](../empirical-methods/execution-with-mcp.md))
→ **pass the bar before submitting**
([`../submission-readiness/`](../submission-readiness/README.md)).*
