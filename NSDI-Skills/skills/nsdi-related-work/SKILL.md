---
name: nsdi-related-work
description: Use when positioning an NSDI submission against the networked-systems literature — covering the NSDI/SIGCOMM/OSDI/SOSP lanes plus both accepted-paper cohorts of the current edition, verifying venues against dblp and open-access USENIX proceedings, and handling self-citations and concurrent submissions under double-blind rules.
---

# NSDI Related Work

Related work at NSDI answers one reviewer question: *what does this design let us do
that the systems we already have do not?* Coverage gaps read as either ignorance or
evasion, and the venue's open-access record removes every excuse for both.

## The lanes an NSDI reviewer expects swept

| Lane | Where it lives | What must be said about it |
|---|---|---|
| Direct competitors | NSDI, SIGCOMM, OSDI, SOSP | Mechanism-level delta, ideally measured head-to-head |
| Same problem, other stack layer | SIGCOMM (protocol), OSDI/SOSP (host), FAST (storage) | Why this layer is the right place to solve it |
| Same technique, other domain | broad systems + ML-systems venues | What the networked setting breaks or changes |
| Measurement/characterization basis | IMC, NSDI measurement papers | Which observed phenomena motivated the design |
| Deployed/industrial precedent | operational-track papers, provider tech reports | What production experience the design inherits or contradicts |
| Early/idea-stage neighbors | HotNets, frontiers-track papers | That the idea's grown-up form differs from the sketch |

Both **cohorts of the current edition** count as literature: NSDI posts spring
accepted-paper lists months before the symposium (e.g.,
`usenix.org/conference/nsdi26/spring-accepted-papers`), so "it wasn't published yet"
fails for a fall submission when the spring list was public at deadline time. Sweep
the sibling deadlines too — SIGCOMM's accepted list frequently contains the closest
neighbor of an NSDI submission.

## Verification: the venue must be proven

Systems folklore misfiles its classics; citing Raft "at NSDI" or B4 "from NSDI"
signals secondhand reading (Raft is USENIX ATC 2014, B4 is SIGCOMM 2013 — see the
guard list in
[`../../resources/exemplars/library.md`](../../resources/exemplars/library.md)). Every
NSDI paper since the venue began is a free PDF on `usenix.org`, and dblp's
`conf/nsdi` stream gives the authoritative edition/pages. Verify before the
bibliography freezes:

```bash
# Cross-check claimed venues in the .bib against dblp keys / USENIX URLs
grep -E '^@' paper.bib | wc -l                       # inventory
grep -A3 -iE 'booktitle.*(nsdi|sigcomm|osdi|sosp)' paper.bib | head -40
# For each NSDI claim: the usenix.org/conference/nsdi<yy>/presentation/<key>
# page or the dblp record must exist. No render, no citation-as-NSDI.
```

Read the PDF of any paper you compare against quantitatively. Comparing against a
system's abstract is how "prior work cannot handle churn" ends up in front of the
reviewer who wrote the churn section.

## Positioning moves that work at this venue

- **Delta by mechanism, not by adjective.** "X batches at the NIC; we batch at the
  RPC layer, which preserves per-request deadlines" beats "unlike X, our approach is
  more flexible."
- **Concede the overlap, then locate the divergence.** NSDI reviewers usually know
  the neighbor papers personally; a generous one-clause summary of the competitor
  buys credibility for the distinction that follows.
- **Use operational precedent as evidence, not decoration.** If a provider's
  operational-track paper reports the failure mode your design removes, that citation
  is motivation-grade, not related-work filler.
- **Position against the measurement literature.** A design justified by workload
  properties should cite where those properties were measured — or measure them in §2.

## Double-blind mechanics for citations

- **Self-citations stay, in third person.** "We extend Ballast [12]" reveals; "This
  work extends Ballast [12]" written as if by strangers does not. Omitting your own
  prior paper to hide identity is explicitly against the CFP.
- **Concurrent NSDI submissions** are cited with the CFP's fixed sentence: "Under
  submission. Details omitted for double-blind reviewing."
- **Tech reports and arXiv versions of your own work**: cite in third person like any
  prior art; do not link author-revealing artifacts in the text.
- **Operational-track nuance:** the anonymization exception covers *your paper's*
  system and company names — it does not license identifying the *author list* through
  possessive phrasing.

## Sequencing the sweep across the two-deadline year

Because NSDI publishes cohort lists mid-cycle, the sweep has a rhythm:

1. **At project start:** lanes 1-3 in depth; identify the two or three systems the
   paper must beat or distinguish, since they shape the evaluation
   (`nsdi-experiments`).
2. **Four weeks before the gate:** re-sweep the current edition's earlier cohort
   list and the most recent SIGCOMM/OSDI/SOSP programs; new neighbors get a
   mechanism-delta sentence, not a panicked rewrite.
3. **At bibliography freeze:** run the venue-verification pass below; fix
   misattributions before reviewers find them.
4. **In a one-shot revision:** re-check whether the reviewers' cited omissions have
   themselves been published since — the same reviewers will notice both presence
   and absence (`nsdi-author-response`).

## Failure patterns

- The wall of one-line citations ("Much work has studied datacenter transport
  [3-19]") — coverage theater with no deltas.
- Comparing only against academic prototypes when a widely deployed system solves an
  adjacent problem — reviewers from industry will supply the omission.
- Treating a spring-cohort paper of the same edition as invisible.
- Venue misattribution in the bibliography — cheap to fix, expensive in credibility.
- A related-work section that never mentions the paper's own limits relative to prior
  work; positioning is bidirectional.

## Where the section lives

NSDI drafts split positioning across two homes, both inside the 12 pages: a short
contrast in the introduction (the two nearest neighbors, one delta sentence each)
and the fuller section — conventionally late, before or after discussion — carrying
the lane-by-lane sweep. Whichever home a comparison occupies, the quantitative
version belongs in the evaluation: a related-work sentence claiming superiority
that §6 never measures is a self-inflicted reviewer question.

## Output format

```text
[Lane coverage] table lane -> covered / gap (paper to add)
[Nearest neighbor] <paper, venue-verified> + mechanism delta
[Cohort sweep] current-edition spring list checked? sibling deadlines?
[Verification] # citations venue-proven / total NSDI-venue claims
[Blind check] self-cites third-person? concurrent-submission wording?
[Fix list] ordered corrections before bibliography freeze
```
