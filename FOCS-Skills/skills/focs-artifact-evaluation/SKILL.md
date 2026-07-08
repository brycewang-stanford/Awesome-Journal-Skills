---
name: focs-artifact-evaluation
description: Use when planning the durable evidence objects around a FOCS (IEEE Symposium on Foundations of Computer Science) paper — a venue with no artifact track where the public arXiv/ECCC full version is the artifact of record, plus proof certificates, checker code, and the IEEE Xplore version's supporting role.
---

# FOCS Artifact Evaluation

There is no artifact-evaluation committee, badge system, or code-submission
channel at FOCS — the 2026 CFP contains none of that machinery (checked
2026-07-08). What it does contain is an expectation with teeth: authors of
accepted papers are expected to make full versions, with complete proofs,
publicly available by the camera-ready deadline. Read that as the venue's
actual artifact policy. The proceedings entry in IEEE Xplore is the citable
announcement; the public full version is the object the community will
actually consult, teach from, and check. Plan the evidence around that split
from day one, not after acceptance.

## The FOCS evidence inventory

| Object | Host | Audience | Obligation level |
|---|---|---|---|
| Full version with all proofs | arXiv (cs.DS/cs.CC/quant-ph...) or ECCC | Referees (they look, even under double-blind), then everyone | Expected by camera-ready; wise at submission time |
| Proceedings version | IEEE Xplore / IEEE CS Digital Library | Citation graph, indexing | Required deliverable of acceptance |
| Certificates for computed proof steps | Ancillary files beside the full version | Skeptics re-verifying a machine-checked lemma | Required whenever a proof leans on computation |
| Independent checker code | Same, plus a tagged repository | Same skeptics | Required with the certificate |
| Illustration/search code | Repository linked from the full version | Curious readers | Courtesy |
| Formalization (Lean/Rocq/Isabelle) | Repository + explicit coverage statement | Growing formal-methods audience | Optional; state honestly *which* theorems are formalized |

## Packaging a certificate that strangers can trust

The trust chain for a computer-assisted step must survive your own
infrastructure disappearing. A packaging recipe that does:

```bash
# Everything a verifier needs, content-addressed and self-describing
mkdir lemma47-certificate
cp check_lemma47.py configs.enum README-VERIFY.md lemma47-certificate/
sha256sum lemma47-certificate/* > lemma47-certificate/SHA256SUMS
git tag -a focs2026-submitted -m "state at FOCS submission"
# README-VERIFY.md states: input, claim certified, expected output,
# runtime (~90 s), and environment ("Python 3.12, stdlib only")
```

Include the certificate directory with the arXiv upload as ancillary files so
it shares the paper's persistence guarantees — a departmental URL in a proof
is a dead link on the timescale over which FOCS papers stay relevant. If the
certificate is huge (SAT traces can reach gigabytes), archive it with a DOI
service and print the hash in the paper so the object stays pinned even if
re-hosted.

## Version ledger: keeping three documents honest

The submission, the public full version, and the proceedings version drift
unless actively synchronized. Keep a ledger in the repository:

- `focs2026-submitted` tag — exactly what HotCRP received.
- Full-version updates — each with a changelog entry ("v2: fixed sign error
  in Lemma 6.3; theorem statements unchanged"); statement changes are
  breaking events that require flagging, not silent repair
  (`focs-reproducibility`).
- Proceedings version — page-limited derivative; every omission points to the
  full version ("complete proof in the full version, Section 7").

Under double-blind, the full version may already be public under your names
at submission time; theory practice accepts this, but the *submission* must
still not self-identify (`focs-submission`).

## What not to build

Effort spent on ML-conference artifact rituals is effort taken from proofs.
At this venue, skip: Docker images for illustration scripts (a `README` and
a pinned interpreter version suffice for code carrying no proof weight);
anonymized artifact links inside the submission (there is no artifact
reviewer to follow them — certificates ride with the paper or its ancillary
files); interactive demos and websites (theory referees want the object,
not the experience); and any "artifact appendix" section formatted after
systems-conference templates. The single question that allocates effort
correctly: *will a skeptical reader in ten years need this object to
believe the theorem?* If yes, engineer it to survive ten years; if no, a
courtesy link is enough.

## Formalization claims, calibrated

Mechanized proofs are appearing in the FOCS orbit, and miscalibrated claims
about them are a new failure mode. If you formalize, state coverage
precisely: "Theorem 1 and Lemmas 3.1–3.4 are verified in Lean 4 (commit
`a3f9c2`); the reduction in Section 6 is not formalized." A blanket "our
results are machine-verified" claim that a reviewer falsifies by opening the
repository costs more credibility than formalizing nothing.

## Choosing the host: arXiv vs ECCC

Both satisfy the CFP's expectation; the choice is about audience and
mechanics. arXiv offers subject-class reach beyond TCS, ancillary-file
support, and version history readable by everyone; ECCC (the Electronic
Colloquium on Computational Complexity) offers a complexity-native audience,
lightweight community screening, and a numbering scheme the complexity
literature cites natively. Complexity-central papers often post to both.
Whichever you choose, pick the arXiv license deliberately — the minimal
arXiv license keeps journal options maximally open, while CC licenses ease
reuse; and remember the proceedings version will carry an IEEE copyright, so
the full version is where your distribution freedom lives.

## Planning sequence

1. At project start: decide which lemmas, if any, will be computer-assisted;
   those need certificate engineering, not retrofitting.
2. At submission: repository tagged; certificates packaged; full version
   ready to post (or already posted) on arXiv/ECCC.
3. At acceptance: execute the camera-ready double deliverable
   (`focs-camera-ready`) and make the public record complete before the
   conference — the New York talk should point at a live, final full version.
