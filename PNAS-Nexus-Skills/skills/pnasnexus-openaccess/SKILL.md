---
name: pnasnexus-openaccess
description: Use to settle PNAS Nexus's open-access decisions — confirm the gold-OA model and the article processing charge (APC), check eligibility for waivers/discounts (low-/middle-income countries, Read & Publish, membership) and funder compliance, and choose the license (CC BY vs CC BY-NC). This is PNAS Nexus's signature pre-submission decision; it replaces flagship PNAS's Direct/Contributed track choice (PNAS Nexus has no such track).
---

# Open Access, APC & License (pnasnexus-openaccess)

## Why this skill exists

PNAS Nexus is **fully gold open access**: every published article is free to read, and there is **no subscription or hybrid option**. That means an **article processing charge (APC)** and a **license choice** are part of the submission, not an afterthought. This is the PNAS-Nexus-specific decision that has **no analogue at flagship PNAS** — and it takes the slot that the Direct/Contributed *track* choice occupies in the `pnas-skills` pack. Settle it right after `pnasnexus-fit`, because funding and eligibility can affect whether and how you submit.

> **There is no Direct vs Contributed track at PNAS Nexus.** Unlike flagship PNAS, an NAS member **cannot "contribute"** a paper, and there is no prearranged-editor route. **All** submissions go through standard editor-assigned peer review (assigned to an Editorial Board member, then a handling/guest editor, with ≥2 independent reviews). If someone expects to use a member-communicated track, correct that expectation here.

## When to trigger

- Before submitting, to confirm the APC, funding, and license.
- The author asks "how much does this cost?" or "can we get a waiver?"
- A funder (NIH, Wellcome, UKRI, Gates, an ERC/Plan-S grant) requires open access with a specific license.
- A co-author who is an NAS member assumes they can communicate the paper (they cannot — see above).

## The gold-OA model and the APC

- **Gold OA, mandatory.** Every article is OA on publication under a Creative Commons license; **authors retain copyright**. The journal states it "complies with all major funder mandates."
- **An APC applies, but OUP publishes no fixed figure.** OUP prices the APC through a **region/category-personalized calculator** on the author-instructions page, so the amount billed depends on **article category, the corresponding author's region/country, and any membership/institutional discount**, and **LMIC waivers or Read & Publish can reduce or eliminate it**. Public trackers **disagree** on the headline number (DOAJ ≈US$4,202 vs ≈US$2,200 elsewhere), and neither is confirmable on the live calculator — so treat the APC as **indicative only (roughly US$2,200–4,200)** and **confirm the exact amount live in the OUP calculator at submission**.
- **No separate submission/editorial fee** is documented — the APC is the only charge (confirm at submission).

## Ways the APC can be reduced or waived (check all that apply)

| Mechanism | Who it helps |
|-----------|--------------|
| **Low-income-country full waiver** | Corresponding authors based in countries in OUP's low-income tier — fees fully waived. |
| **Middle-income-country discount** | Corresponding authors in OUP's middle-income tier — reduced APC (applied before other discounts). |
| **Read & Publish / transformative agreements** | Authors at institutions with an OUP agreement — the institution covers the charge. Note: you **may not** switch the corresponding author just to access this funding. |
| **Membership discount** | A membership-discount option exists in the calculator; the exact eligibility/amount is **待核实** — confirm. |
| **Discretionary waiver** | Authors without sufficient funds may **request a waiver at submission** (historically via openaccess@oup.com) — confirm the current route. |

> Eligibility usually hinges on the **corresponding author's** affiliation/region. Decide who the corresponding author is **before** you price the APC — and never reassign corresponding authorship purely to capture Read & Publish funding.

## Choosing the license: CC BY vs CC BY-NC

PNAS Nexus offers **two** Creative Commons licenses (as of the February-2024 change, CC BY-NC-ND is **no longer offered**):

| License | What it allows | Choose it when |
|---------|----------------|----------------|
| **CC BY 4.0** | Anyone may reuse, including commercially, with attribution. | Your funder requires CC BY (Plan S / cOAlition S, Wellcome, UKRI, Gates, NIH 2025 public-access expectations). **The safe default for compliance.** |
| **CC BY-NC 4.0** | Reuse with attribution, **non-commercial only**. | You specifically want to restrict commercial reuse **and** no funder mandate forbids NC. |

- **If a funder mandates open access, default to CC BY** — many mandates do not accept NC or ND. Confirm against your grant's policy.
- The named technical default on the journal page is **待核实**; do not assert which is pre-selected — make the choice deliberately.

## Funder-compliance quick check

- **Plan S / cOAlition S:** a fully-OA journal with a **CC BY** route satisfies the route; confirm the journal/your route in the Journal Checker Tool if your grant requires it.
- **NIH / Wellcome / UKRI / Gates:** all accept publication in a fully gold-OA journal under CC BY. Pick CC BY and deposit as the funder requires (PMC etc.).
- The journal claims compliance with "all major funder mandates," but **per-funder confirmation is your responsibility** — match the license to the strictest mandate on the author team.

## Eligibility & decision checklist

- [ ] Confirmed PNAS Nexus is fully gold OA and an APC applies (no hybrid/subscription escape).
- [ ] Corresponding author decided (drives waiver/discount eligibility) and **not** reassigned just for funding.
- [ ] APC figure obtained **live from the OUP calculator** for this article category + region (not from memory or a third-party tracker).
- [ ] Waiver/discount checked: LMIC waiver/discount? Read & Publish? membership? discretionary waiver?
- [ ] License chosen deliberately — **CC BY** if any funder mandate applies; CC BY-NC only with a clear reason and no conflicting mandate.
- [ ] Funder open-access requirements (license + deposit) satisfied by the chosen route.
- [ ] (Reminder) no Contributed/Direct track — standard editor-assigned review for everyone.

## Output format

```
【OA model】 gold OA confirmed (no hybrid/subscription option)
【APC】 confirm-live via OUP calculator (category + region) — figure NOT asserted from memory
【Waiver/discount path】 LMIC full-waiver / LMIC discount / Read&Publish / membership / discretionary / none
【Corresponding author】 ___ (drives eligibility; not reassigned for funding)
【License】 CC BY 4.0 / CC BY-NC 4.0 + one-line reason
【Funder mandate】 funder(s): ___ → license/deposit requirement satisfied? yes/no
【Track reminder】 no Direct/Contributed track — standard editor-assigned review
【Next】 pnasnexus-writing
```

## Anti-patterns

- **Do not** treat any APC figure (trackers disagree, ≈US$2,200–4,200) as the final amount — OUP publishes no fixed figure; it is region/category-personalized and may be waived/discounted; confirm it live in the OUP calculator.
- **Do not** assume there is a subscription/non-OA way to avoid the APC — there isn't.
- **Do not** pick CC BY-NC when a funder requires CC BY — it can break compliance.
- **Do not** reassign the corresponding author solely to capture Read & Publish funding (not permitted).
- **Do not** tell an NAS-member co-author they can "contribute" or "communicate" the paper — PNAS Nexus has no such track.
- **Do not** leave the OA/APC/license decision to the final upload; it gates submission.
