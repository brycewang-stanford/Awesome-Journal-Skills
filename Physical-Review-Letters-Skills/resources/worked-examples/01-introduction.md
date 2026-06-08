> **Illustrative teaching example.** The Letter, the measurement, and every number below are
> **fictional** and exist only to demonstrate Physical Review Letters house style. No real-paper facts
> are stated and no policy is invented. Corresponding skills:
> [`prl-results-framing`](../../skills/prl-results-framing/SKILL.md),
> [`prl-writing-style`](../../skills/prl-writing-style/SKILL.md),
> [`prl-scope-fit`](../../skills/prl-scope-fit/SKILL.md), and
> [`prl-length-management`](../../skills/prl-length-management/SKILL.md).

# Worked Example: A PRL Abstract + Opening (before → after)

This demonstrates the **PRL opening arc** from `prl-results-framing` —
**general physics context → open question/gap → what this Letter shows (the central claim) → why it
matters broadly** — together with the `prl-scope-fit` two-part gate (**importance AND broad interest**),
the `prl-writing-style` rule that the opening must be readable **out-of-subfield**, and the hard
`prl-length-management` reality that a Letter is short (on the order of **~3750 words / ~4 journal pages
including figures, equations, and references — verify the current limit on the APS author page**).

**Illustrative Letter (fictional):** *"Acoustic Topological Pumping of Heat Across a Disordered
Interface."* Fictional result: a measured, quantized phonon heat current that survives strong disorder.

---

## Before (buries the result; reads like a lab report; fails the gate on the page)

> **Abstract.** In this work we have performed a series of measurements on a phononic metamaterial
> structure. The sample was fabricated using standard lithographic techniques and characterized over a
> range of temperatures. We employed a modulation scheme and recorded the thermal response under various
> conditions. A number of control experiments were also carried out. Our results may possibly suggest
> that topological effects could perhaps play a role in the observed thermal transport, which may be of
> interest for future applications in phononics.
>
> **Opening.** The study of heat transport in engineered materials has a long and rich history, and many
> groups have investigated phononic crystals over the past decades [1–14]. Topology has become an
> important theme in condensed matter physics. In order to explore these questions, we constructed a
> device and performed measurements, which we describe below. Section II describes the fabrication,
> Section III the apparatus, and Section IV the data.

**What's wrong (against the PRL skills):**

- **Leads with method and apparatus**, not the result — the `prl-results-framing` anti-pattern
  ("abstract that is a methods summary rather than a result statement").
- **No central claim and no number** with an uncertainty anywhere in the abstract — fails
  `prl-writing-style` ("quote uncertainties with every headline number").
- **Hedging stack** ("may possibly suggest ... could perhaps") — the named `prl-writing-style`
  anti-pattern; the claim is not calibrated to evidence.
- **Importance/breadth not argued** — an editor cannot tell why this clears the `prl-scope-fit` gate, or
  why a non-phononics physicist should read it. There is no "prior belief changed."
- **Literature tour + over-signposted roadmap** ("Section II ... Section III ...") burns the scarce
  length budget that `prl-length-management` says figures and references are already competing for; a
  Letter barely has numbered sections.
- **Jargon-first opening** ("phononic metamaterial," "modulation scheme") with no out-of-subfield gloss.

---

## After (PRL arc — finding first, breadth named, calibrated, length-aware)

> **Abstract.** Topological pumping moves a quantized amount of a conserved quantity per cycle and is
> famously robust to disorder, but it has been demonstrated almost entirely for charge and for photons.
> Whether *heat* — carried by phonons, which are strongly scattered by disorder — can be pumped in the
> same quantized, disorder-immune way has remained open. We show that it can: in an acoustically
> modulated lattice we measure a phonon heat current that is quantized to within **2%** and is
> **unchanged (within uncertainty) as we increase interface disorder over an order of magnitude**. The
> result establishes thermal transport as a setting for topological pumping and offers a route to heat
> flow that is protected by topology rather than by material perfection.
> *(context → open question → central claim with number+robustness → why it matters — all out-of-subfield
> legible, finding first.)*
>
> **Opening.** A topological pump transfers an exactly quantized amount of something — charge, in the
> original setting — once per modulation cycle, and the quantization survives disorder because it is set
> by topology, not by the details of the sample. *(general physics context, one sentence a non-specialist
> grasps.)* This protection has been seen for electrons and engineered for light, but heat is the hard
> case: phonons scatter strongly off defects, so it was not known whether a *thermal* current could be
> pumped in a quantized, disorder-immune way, or whether scattering would wash the effect out. *(the open
> question / gap — stated as the physical obstacle, not a literature list.)* Here we show that an
> acoustically modulated lattice pumps heat in discrete quanta: the measured heat current per cycle is
> quantized to **2%** and stays constant as we raise interface disorder tenfold. *(what this Letter shows
> — the central claim with the key number, within the first paragraph.)* Because the protection comes
> from topology rather than from a clean lattice, the result turns "robust heat routing" from a materials
> problem into a design principle, and it imports a tool the photonics and electronics communities
> already use into thermal physics. *(why it matters broadly — names the out-of-subfield audience and the
> prior belief it changes.)*

---

## Why the "after" meets the PRL bar

Mapped to the skill checklists:

- **One central claim, finding first** — "heat can be pumped in quantized, disorder-immune quanta"; the
  title would encode it and the abstract leads with it, satisfying `prl-results-framing`
  ("abstract leads with the finding"; "exactly one primary claim").
- **Opening executes the four moves** — context → gap → claim → broad significance — and reaches the
  result inside the first paragraph, not after a literature tour (`prl-results-framing` opening pattern).
- **Clears the two-part `prl-scope-fit` gate explicitly:** *importance* = a new effect (quantized,
  disorder-protected heat pumping), and *broad interest* = a named out-of-subfield audience (photonics,
  electronics, materials) plus the prior belief changed ("scattering would wash it out"). The "neighbor
  test" and "displacement test" both pass.
- **Calibrated, uncertainty-bearing prose** — every headline number carries its tolerance ("2%",
  "tenfold"), and the hedging stack is gone, per `prl-writing-style` precision discipline.
- **Out-of-subfield readable** — "topological pump" is glossed in one clause before any subfield notation
  appears, meeting the `prl-writing-style` broad-readability requirement.
- **Length-aware** — no literature tour, no apparatus dump, no over-signposted roadmap; that reclaimed
  budget is what `prl-length-management` says you need for the figures, equations, and references that
  also count against the ~3750-word / ~4-page deductible (**verify the current limit on the APS author
  page**). Fabrication and the full disorder sweep would go to Supplemental Material per `prl-methods`.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** PRL Letters
> whose abstracts and openings execute this arc, and confirm the live length/abstract limits and
> submission categories on the official APS / PRL author page (see [`../external_tools.md`](../external_tools.md)).
