---
name: ieeesp-topic-selection
description: Use when deciding whether a security or privacy project belongs at IEEE S&P (Oakland), including the threat-model test, SoK fit, routing among USENIX Security, CCS, NDSS, PETS, and CRYPTO, and whether the one-year resubmission embargo or the 40% overlap rule constrains the plan.
---

# IEEE S&P Topic Selection

Use this before any writing starts: is the project an Oakland paper, and if so,
as a research paper or as an SoK? S&P has been the field's flagship since 1980
(first held at the Claremont Resort in the Oakland hills — hence the nickname),
and its reviewer pool reads for adversarial rigor above topical fashion.

## The two-question fit test

1. **Is there a real adversary?** State who attacks, with what access, and what
   they win. If the paper has no defensible threat model — or the "attack" needs
   an adversary who could already do worse things more cheaply — Oakland
   reviewers will say so in round one. Papers where security is a motivating
   anecdote rather than the analyzed object usually belong at a systems, ML, or
   networking venue instead.
2. **Does the evidence close the loop?** An attack needs an end-to-end
   demonstration against a realistic target; a defense needs evaluation against
   an adaptive adversary who knows the defense exists; a measurement study needs
   a sampling story and an ethics story. A promising idea with simulation-only
   evidence is a workshop paper, not yet an S&P submission.

## SoK is a first-class lane

Both the 2026 and 2027 CFPs solicit Systematization of Knowledge papers,
marked with the `SoK:` title prefix and a submission-form checkbox
(sp2027.ieee-security.org/cfpapers.html, checked 2026-07-08). An SoK is judged
on its treatment of existing work — a new viewpoint on a major area, evidence
that challenges a long-held belief, or a genuinely new taxonomy — not on new
results. If your "survey" cannot name the belief it overturns or the structure
it reveals, it is a literature review, and S&P rejects those.

## Routing among the security venues

| Signal in your project | Better-fit venue | Why |
|---|---|---|
| Adversarial rigor + broad security relevance | **IEEE S&P** | Flagship generalist bar; SoK lane; Revise pathway rewards deep-but-fixable work |
| Deployable systems artifact, engineering depth | USENIX Security | Artifact-forward culture, open-access proceedings |
| Applied crypto protocols, broad ACM community | ACM CCS | Larger program, more topical tracks |
| Network/protocol attacks needing fast turnaround | NDSS | February conference, distinct cycle timing |
| Privacy is the community, not just the property | PETS/PoPETs | Journal-style revisions, privacy-native reviewers |
| Theorems about cryptographic constructions | CRYPTO/EUROCRYPT | Proof-depth reviewing S&P cannot give |

Route by contribution type and by calendar, not prestige: the four flagships
alternate deadlines across the year, and S&P's own two cycles (June and
November for the 2027 symposium) may simply not be the next open door.

## Embargo math changes the answer

Two S&P-specific rules constrain venue strategy (2027 CFP, checked 2026-07-08):

- A rejected paper may not return to S&P for **one year from the original
  submission date** — so a weak submission burns the venue, not just the cycle.
- A new submission counts as a resubmission when roughly **40% or more
  overlaps** a previously rejected one; splitting a rejected paper into two
  does not reset the clock.

If the evidence will not be ready, targeting a sibling venue first and S&P
with the mature version is often the higher-expected-value order.

## Quick self-interrogation

```text
Oakland fit worksheet (answer in one line each):
1. Adversary + access + payoff: ..............................
2. Evidence type that closes the loop (exploit / adaptive eval /
   measurement + ethics / systematization): ..................
3. If SoK: which belief or structure does it change? .........
4. Embargo status: any ≥40%-overlap rejection at S&P in the
   last 12 months? ...........................................
5. Which cycle is realistically reachable with finished
   evidence (not finished writing)? ..........................
→ Any blank line = not ready to pick S&P yet.
```

## Signals you are choosing S&P for the wrong reason

- The main argument for Oakland is "it is ranked highest" — the four flagships
  are close peers; wasted cycles are the real cost.
- The threat model was written after the experiments, to justify them.
- The contribution is a faster/cheaper version of a published system with the
  same security argument — reviewers will ask what the *security* delta is.
- The plan depends on the Revise outcome as a safety net; Revise is offered to
  a limited set of papers reviewers already believe in, not to drafts.

## Output format

```text
[S&P fit] Strong / Plausible / Re-route (one-line reason)
[Paper type] research / SoK
[Threat-model status] stated & realistic / stated but strained / missing
[Evidence gap] <the one experiment or analysis that closes the loop>
[Embargo check] clear / blocked until <date> / 40%-overlap risk
[Alternative order] <e.g., USENIX Sec first, S&P with mature version>
```
