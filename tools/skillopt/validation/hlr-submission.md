# Validation set — `hlr-submission`

Held-out researcher queries (the skill text does not contain these) plus the
**verified ground-truth fact sheet** the judge scores against. Ground truth is
drawn from `Harvard-Law-Review-Skills/resources/official-source-map.md`
(re-verified 2026-06-21) and the official submissions page, cross-checked by web
search on 2026-06-21.

## Held-out queries

**Q1 (portal + over-length, the hard one).**
> "I'm submitting my Article to the Harvard Law Review through Scholastica next
> week. It's about 41,000 words including footnotes. What should I check before I
> upload?"

The query embeds two wrong assumptions a good answer must correct.

**Q2 (word limit + footnotes).**
> "How long can a Harvard Law Review article be, and does the length limit include
> the footnotes?"

**Q3 (anonymization + citation style).**
> "Do I need to anonymize my HLR submission, and which edition of The Bluebook do
> they expect?"

**Q4 (rejected-edit probe — fee + turnaround).**
> "What is the Harvard Law Review's submission fee, and how fast will I hear back
> after I submit?"

Q4 is the **gate-integrity probe**. Both the fee and the decision turnaround are
volatile/unstated by HLR (the only committed timing fact is the ≥ 7-day *offer*
window), so a *correct* answer defers them to a live check. It exists to test a
tempting "more helpful" edit that asserts a `$0 fee` and a `4–8 week` turnaround:
the gate must **reject** that edit because it fabricates volatile facts (see the
`E2` rejected edit in `ledger/hlr-submission.json`).

## Ground-truth fact sheet (what a correct answer must reflect)

**Submission portal.** HLR receives Articles, Essays, and Book Review proposals
through **its own electronic submission system** at harvardlawreview.org
(Microsoft **Word** documents encouraged; mailing to the Articles Office is a
fallback). **HLR does *not* take submissions through Scholastica.** Scholastica /
ExpressO are the *general law-review market* platforms used for the multi-submit +
expedite ladder at *other* journals; an author targeting HLR uses HLR's own
system. → Q1 must correct "through Scholastica."

**Word / length limits** (count includes **text, footnotes, and appendices**):
- Articles (Print): preferred **≤ 25,000 words**.
- Length **over 30,000 words weighs against selection**.
- Unconditional acceptance **over 37,500 words is rare**.
- Essays (Print/Forum): **12,000–17,500 words**.
- Forum Responses: 8,000 words. Forum Commentaries: 6,000 words.
- Book Review proposals: a few pages.
→ Q1's 41,000-word manuscript is **well past the soft cap** — the answer must flag
that it is over the threshold that "weighs against" and past where unconditional
acceptance is rare, and advise cutting. → Q2: yes, the count **includes footnotes**
(and appendices).

**Anonymous review preparation.** Review is anonymous: keep **name, affiliation,
bio, and acknowledgments on a separate cover page**; put the **manuscript title on
the first text page**; **anonymize self-citations**. → Q1 and Q3 must surface this.

**Citation style.** Footnotes conform to **The Bluebook, 22nd edition**; pincited,
signal-correct. HLR co-compiles The Bluebook. → Q3.

**Expedite / offer window.** Expedite via the unique link in the confirmation
email; HLR honors requests where it can but **does not skip review stages**; a
**≥ 7-day** offer-decision window is committed.

**Review process.** Anonymous; **≥ 3 editors** per submission; many pieces proceed
through an Articles Committee vote, a **preemption check**, **faculty peer review**,
and a full-body vote. (So "student-edited" is true, but a *faculty peer-review
stage* exists — avoid implying zero peer review.)

**Timing.** Published monthly **November–June** (SCOTUS issue each November,
Developments in the Law each April). Authors who *prefer* HLR are advised to submit
**at least two weeks before** submitting elsewhere.

## Volatile — must be live-checked, NOT stated as fixed (rubric §5)

- Current intake **volume / season status** (e.g. "accepting for Volume 140").
- Exact season **open dates**.
- Any **fee** specifics and account mechanics.
- The **named** current student president / editors (masthead turns over annually).

A correct answer is confident on the stable facts above and explicitly defers
these to a live check.
