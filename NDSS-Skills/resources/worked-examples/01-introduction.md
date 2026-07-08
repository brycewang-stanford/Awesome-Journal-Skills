> **Illustrative teaching example.** The paper, system names, measurements, and every number
> below are **fictional**, invented solely to demonstrate how an NDSS first page is built.
> No real vulnerability, vendor, or dataset is described, and no NDSS policy is invented.
> Companion skills: [`ndss-writing-style`](../../skills/ndss-writing-style/SKILL.md),
> [`ndss-experiments`](../../skills/ndss-experiments/SKILL.md), and
> [`ndss-topic-selection`](../../skills/ndss-topic-selection/SKILL.md).

# Worked Example: Rebuilding an NDSS Abstract + Introduction (before → after)

The scenario: a team has found that expired cloud-DNS delegations let an attacker silently
re-register abandoned nameserver names and answer queries for still-live domains. Their
first draft reads like a generic "we found bugs" report. The rewrite reorganizes the same
material around what an NDSS Round-1 reader needs in order to *not* early-reject it: a
named adversary with realistic capabilities, a measurement method that scales beyond
anecdotes, an explicit harm-and-disclosure story, and claims sized to the evidence.

**Fictional paper:** *"Orphaned Authority: Measuring and Preventing Stale-Delegation
Takeover in Managed DNS."*

---

## Before — the draft that gets early-rejected

> **Abstract.** DNS is one of the most critical protocols on the Internet. Unfortunately, it
> suffers from many security problems. In this paper we present a new attack called
> stale-delegation takeover that can hijack domains. We scanned the Internet and found that
> a huge number of domains are vulnerable, including many popular websites. We also propose
> a defense that completely prevents the attack. Our results show that DNS security needs
> more attention.
>
> **Introduction.** The Domain Name System underpins nearly every Internet transaction, and
> attacks against it have a long history. We discovered that when organizations migrate away
> from managed DNS providers, delegations often remain pointing at nameserver names that no
> longer exist. An attacker can register these names and gain control. We believe this is a
> serious problem. We performed a large-scale study and found many vulnerable domains. We
> then built a tool to detect the issue and a defense to stop it. Experiments show our
> defense works with low overhead.

**Why Round 1 kills this draft:**

- **The adversary is never specified.** Who can register what, at what cost, with what
  visibility? "An attacker can register these names" hides the entire capability model.
- **"Huge number" and "many popular websites" are unfalsifiable.** NDSS measurement claims
  need a defined population, a sampling method, and validation of the vulnerability test —
  none appear.
- **The ethics silence is disqualifying, not neutral.** The draft admits to Internet-wide
  scanning and to identifying hijackable production domains, yet says nothing about scan
  etiquette, notification, or disclosure. Reviewers will flag it to the Ethics Review Board.
- **"Completely prevents" is a claim no evaluation can carry**, and it invites the reviewer
  to construct the counterexample for you.
- **No why-now, no delta.** Subdomain-takeover and dangling-record work exists; the draft
  neither cites the neighborhood nor states what is new (measurement scale? a new precondition?
  the defense?).

---

## After — the same work, NDSS-shaped

> **Abstract.** When a domain leaves a managed-DNS provider, its parent-zone delegation often
> keeps pointing at provider-hosted nameserver names that the provider later releases. We
> call the resulting condition a *stale delegation* and show it enables a low-cost, fully
> off-path takeover: an adversary who re-registers the released nameserver name — requiring
> only an ordinary provider account and no network vantage point — answers authoritatively
> for the victim domain. We design a takeover test that confirms exploitability *without*
> serving live victim traffic, and apply it to delegation records for a defined population
> of 41M registered domains observed over six months. Stale delegations are rare but
> long-lived and concentrated at a small set of providers, and exploitability persists for a
> median of [k] weeks (all numbers fictional). We disclosed to the affected providers, two of
> which have deployed our proposed release-time check, a provider-side defense that blocks
> the takeover precondition at delegation-release time and requires no registrant action. We
> release our scanner and the anonymized measurement dataset.
>
> **Introduction.** *(¶1 — the adversary and the condition, immediately.)* The attack we
> study needs no privileged position: the adversary is any party able to open an account at
> a managed-DNS provider and register a nameserver name the provider has released. We show
> this weak adversary inherits full authoritative control over domains whose parent-zone
> delegations have gone stale — a condition invisible to the domain owner, who long ago
> stopped using the provider.
>
> *(¶2 — why existing understanding is insufficient.)* Dangling-record abuse is known at the
> resource-record layer (subdomain takeover via CNAME, A, and MX remnants). Delegation-layer
> staleness is different in both mechanism and blast radius: it hands the adversary the whole
> zone, survives record-level hygiene, and — as we show — is not detected by the checks
> providers run today. Prior measurements also could not distinguish *registered-but-stale*
> from *exploitable*, which inflates or obscures risk; our test resolves that distinction.
>
> *(¶3 — method and its ethical envelope, together.)* Our scanner enumerates delegations,
> identifies released nameserver names, and confirms exploitability by registering candidate
> names inside our own provider accounts and answering only our own probe queries — victim
> traffic is never served, and every confirmed domain entered our notification pipeline.
> Scan rate, opt-out handling, and the disclosure timeline follow the protocol in our Ethics
> Considerations section, developed with our institution's review board and shared with
> providers before publication.
>
> *(¶4 — findings and defense, each sized to its evidence.)* Across six months of
> observation, exploitable stale delegations are heavily provider-concentrated, and their
> lifetime distribution implies remediation-by-luck is slow (Section 5; numbers fictional).
> Because the precondition is created at *release time*, we propose the provider check the
> parent delegation before releasing a nameserver name; the check needs no registrant
> cooperation. We evaluate coverage against our measured corpus and adversarial workarounds
> in Section 6, and report the limits: registrant-side migrations that bypass providers
> remain out of scope.
>
> *(¶5 — contributions list, one line each: condition + adversary model; non-intrusive
> exploitability test; six-month population measurement; deployed provider-side defense;
> released scanner and dataset.)*

---

## What changed, mapped to the skills

| Draft failure | Rewrite move | Skill |
| --- | --- | --- |
| Unspecified attacker | ¶1 names capabilities, cost, and vantage (off-path, account only) | `ndss-writing-style` |
| "Huge number" | Defined 41M-domain population, six-month window, exploitability test | `ndss-experiments` |
| Ethics silence | Method and ethical envelope stated in the same paragraph; ERB-ready | `ndss-writing-style` |
| "Completely prevents" | Defense scoped to the precondition it blocks; limits paragraph | `ndss-experiments` |
| No delta | ¶2 separates delegation-layer staleness from record-layer takeover | `ndss-related-work` |
| No deployment story | Two providers running the check; scanner and data released | `ndss-reproducibility` |

The structural lesson: at NDSS the adversary model, the measurement discipline, and the
disclosure posture are not compliance boxes — they are the *content* of the first page.
Real first pages that execute this are collected in
[`../exemplars/library.md`](../exemplars/library.md); current policy lives in
[`../official-source-map.md`](../official-source-map.md).
