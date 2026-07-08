# NDSS Exemplars Library (contribution type × era)

> **Verified via web search, access date 2026-07-08.** Direct fetches of `ndss-symposium.org`
> and `dblp.org` were blocked in the verification environment, so each paper below was
> confirmed through search-engine renderings of its official NDSS proceedings page and/or its
> dblp `conf/ndss` record, matched on title, author list, and edition. Anything that could
> not be pinned to a specific NDSS edition was left out or moved to the misattribution list.
> Short and verified beats long and guessed.
>
> **Attribution guard:** NDSS shares its author community with USENIX Security, IEEE S&P,
> CCS, IMC, and PETS, and famous "network security" papers are scattered across all of them.
> NDSS papers live in the free proceedings at `ndss-symposium.org` and in dblp's `conf/ndss`
> stream, and modern ones carry a `10.14722/NDSS.<year>.<id>` DOI — check one of those three
> signals before calling anything an NDSS paper.
>
> **Zero-hallucination rule:** rows give positioning only. No result numbers, no CVE counts,
> no figure claims are restated here — read the open-access original before citing details.

---

## How to use this library

Each exemplar shows one way a paper clears the NDSS bar: a concrete adversary in a networked
or distributed setting, a mechanism or measurement that works against real systems, and
evidence gathered with visible care about harm. Pick the row nearest your contribution type,
then answer its self-check question honestly before claiming your draft is NDSS-shaped
(see [`../../skills/ndss-topic-selection/SKILL.md`](../../skills/ndss-topic-selection/SKILL.md)
and [`../../skills/ndss-experiments/SKILL.md`](../../skills/ndss-experiments/SKILL.md)).

---

## Verified exemplars

### Binary-level defense mechanism — TaintCheck (NDSS 2005)

- **Newsome & Song, "Dynamic Taint Analysis for Automatic Detection, Analysis, and Signature
  Generation of Exploits on Commodity Software," NDSS 2005 (12th edition, San Diego).**
  Verified: `ndss-symposium.org/ndss2005/dynamic-taint-analysis-automatic-detection-analysis-and-signaturegeneration-exploits-commodity/`.
- **Why it is an exemplar:** protects *commodity* software with no source code and no
  recompilation — the deployment-realism constraint is stated up front and drives the whole
  design. It defined dynamic taint tracking for a generation of defense work.
- **Self-check:** does your defense state, on page one, what it refuses to assume about the
  systems it protects?

### Automated vulnerability discovery — SAGE whitebox fuzzing (NDSS 2008)

- **Godefroid, Levin & Molnar, "Automated Whitebox Fuzz Testing," NDSS 2008.**
  Verified: `ndss-symposium.org/ndss2008/automated-whitebox-fuzz-testing/`; NDSS 2022 Test of
  Time award (Internet Society announcement).
- **Why it is an exemplar:** pairs a clean technique (symbolic execution over recorded
  traces) with evidence from real, large, ugly targets rather than toy corpora — the tool
  went on to run inside an industrial pipeline. Impact-through-deployment is the NDSS
  Test-of-Time signature.
- **Self-check:** would your technique still look good if evaluated only on targets you did
  not choose?

### Minimal-hardware security architecture — SMART (NDSS 2012)

- **El Defrawy, Francillon, Perito & Tsudik, "SMART: Secure and Minimal Architecture for
  (Establishing a Dynamic) Root of Trust," NDSS 2012 (19th edition).**
  Verified: NDSS 2024 Test of Time award announcements (Internet Society / UC Irvine),
  cross-checked against citing literature.
- **Why it is an exemplar:** asks what is the *least* hardware change that yields remote
  attestation for low-end embedded devices — a minimality claim, argued explicitly, instead
  of another maximal TEE. Distributed-systems trust with a precise cost budget.
- **Self-check:** can you state the smallest assumption set under which your guarantee still
  holds, and did you argue why nothing smaller works?

### Online network defense under resource limits — Kitsune (NDSS 2018)

- **Mirsky, Doitshman, Elovici & Shabtai, "Kitsune: An Ensemble of Autoencoders for Online
  Network Intrusion Detection," NDSS 2018 (25th edition, San Diego, February 18-21, 2018).**
  Verified: `dblp.org/rec/conf/ndss/MirskyDES18.html`; DOI `10.14722/NDSS.2018.23204`.
- **Why it is an exemplar:** the ML is subordinated to the operational constraint — unsupervised,
  online, and cheap enough for gateway hardware. An ML-for-security paper that survives NDSS
  review because the *network deployment envelope* shapes the method, not the reverse.
- **Self-check:** if a reviewer deleted the words "deep" and "neural" from your draft, would
  a security contribution remain?

### Black-box attack discovery at the ecosystem boundary — IoTFuzzer (NDSS 2018)

- **Chen, Diao, Zhao, Zuo, Lin, Wang, Lau, Sun, Yang & Zhang, "IoTFuzzer: Discovering Memory
  Corruptions in IoT Through App-based Fuzzing," NDSS 2018.**
  Verified: `dblp.org/rec/conf/ndss/ChenDZZL0LSYZ18.html` and the official paper PDF under
  `ndss-symposium.org/wp-content/uploads/2018/02/ndss2018_01A-1_Chen_paper.pdf`.
- **Why it is an exemplar:** reaches firmware bugs *without* firmware access by fuzzing
  through the companion app's protocol layer — the attack path mirrors what a real adversary
  can touch, and findings were validated on physical devices from many vendors.
- **Self-check:** does your attack operate through interfaces the stated adversary actually
  has, and were findings confirmed on real deployments with responsible handling?

---

## Coverage matrix

| Contribution type | Exemplar | Edition | What NDSS rewarded |
| --- | --- | --- | --- |
| Runtime defense for unmodified software | TaintCheck | 2005 | Deployment constraint drives design |
| Automated bug finding | SAGE whitebox fuzzing | 2008 | Real targets; industrial afterlife (ToT 2022) |
| Hardware root of trust | SMART | 2012 | Explicit minimality argument (ToT 2024) |
| Online intrusion detection | Kitsune | 2018 | Method fitted to gateway resource budget |
| IoT attack surface analysis | IoTFuzzer | 2018 | Realistic adversary interface; device validation |

Two of the five are Test of Time winners, anchoring what "influential at NDSS" has meant in
practice; the two 2018 rows show the modern evidence bar for ML-flavored and IoT work.

---

## Common misattributions (checked and excluded)

Papers people reflexively call "NDSS papers" that are not — do not cite them as NDSS:

- **"Understanding the Mirai Botnet"** — USENIX Security 2017, not NDSS. The botnet-analysis
  genre thrives at NDSS, but this flagship instance is USENIX.
- **"DROWN: Breaking TLS using SSLv2"** — USENIX Security 2016. Protocol-attack subject
  matter is NDSS-typical; this paper is not NDSS.
- **"The Matter of Heartbleed"** — the canonical Heartbleed measurement study is IMC 2014.
  Internet-scale measurement often routes to IMC when there is no adversarial contribution.
- **SoK papers** — the `SoK:` systematization lane belongs to IEEE S&P; NDSS has no
  equivalent labeled track, so do not promise reviewers an "NDSS SoK."

## Adding a new exemplar

Confirm the paper on the free NDSS proceedings (`ndss-symposium.org/ndss<year>/...`), in
dblp's `conf/ndss` stream, or via a `10.14722/NDSS.*` DOI; record title, full author list,
edition, and the verification URL; update the access date at the top. If none of the three
signals can be checked, add the row as 待核实 with no venue attribution rather than guessing.
