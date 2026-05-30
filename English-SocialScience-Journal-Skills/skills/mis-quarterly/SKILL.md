---
name: mis-quarterly
description: Use when targeting MIS Quarterly (MISQ) or deciding whether an information-systems behavioral / design-science / economics-of-IS manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# MIS Quarterly (mis-quarterly)

## Journal positioning

MIS Quarterly is the premier journal of the information-systems discipline and a member of the AIS Senior Scholars' Basket of eight. It publishes research that contributes to knowledge and theory about the development, use, management, and impact of information systems, across the field's major traditions — behavioral, design-science, and economics-of-IS. The defining test is an *IS contribution*: a paper must advance IS theory or knowledge, not merely apply a method. A pure machine-learning benchmark with no IS-theoretic contribution does not fit. The readership is the global IS research community.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the MISQ / AIS site and the editorial submission system.

## When to trigger

- The author names MISQ (or the AIS Senior Scholars' Basket) as the target venue.
- A behavioral, design-science, or economics-of-IS paper needs the field's flagship home.
- An analytics or ML paper using IS data needs re-framing around an IS theoretical contribution — or re-routing if there is none.
- The author needs MISQ's desk-reject risks and a credible Basket / INFORMS alternative list before submitting.

## Scope & topic fit

- Behavioral IS: technology adoption and use, IS and individuals/teams/organizations, IT and work, digital behavior.
- Design science: novel IT artifacts, design theories, and evaluated systems with prescriptive knowledge contributions.
- Economics of IS: IT business value, platforms, digital markets, network effects, and the economics of digital goods.
- IS management and strategy; the societal and organizational impacts of information technology.

## Method & evidence bar

- An explicit IS contribution to theory or knowledge is mandatory; the method (survey/SEM, experiment, econometrics, design-science, qualitative, computational/ML) serves that contribution.
- Behavioral work needs validated constructs, sound measurement, attention to common-method bias, and adequate power.
- Design-science work needs a clearly articulated artifact, design principles/theory, and rigorous evaluation per established DSR guidelines.
- Econometric/analytics work needs credible identification or a defensible model and must yield IS insight, not just predictive accuracy.

## Structure & house style

- The front end frames an IS problem and an explicit theoretical or design contribution; the "so what for IS" is answered early.
- Theory development is substantial; methods are transparent; appendices carry instruments, proofs, or design details.
- MISQ values writing quality and a clear arc from theory to evidence to contribution.
- The discussion states contributions to IS theory and to practice, with boundary conditions.

## Official-submission checklist

- Search the live site for "MIS Quarterly submission guidelines / author guidelines / editorial statements" and follow the current version, including any research-genre statements (e.g., design science, theory development).
- Re-check word/length limits, abstract/structured-abstract format, anonymization for double-blind review, and reference style.
- Re-check the current open-science, data/code availability, and AI-use disclosure policies.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the IS contribution — what the field now knows or can now design that it could not before.
- [ ] The contribution is stated as IS theory / design knowledge / mechanism, not as predictive accuracy or significance.
- [ ] Method matches the genre (behavioral / DSR / econometric) and meets that genre's rigor standards.
- [ ] Constructs/artifacts are validated/evaluated; identification or measurement concerns are addressed.
- [ ] Length, abstract, anonymization, references, and open-science policy match the current MISQ guide.

## Common desk-reject triggers

- A machine-learning benchmark or analytics application with no IS theoretical contribution.
- A behavioral paper with weak constructs, common-method bias, or a borrowed model with no IS advance.
- A design-science paper with an artifact but no design theory or rigorous evaluation.
- A paper that is really a CS, marketing, or economics paper wearing IS clothing.

## Re-routing decision

- Rigorous IS with a quantitative/economic emphasis and an INFORMS audience → `information-systems-research`.
- Management-of-IS, IT business value, IS strategy → `journal-of-management-information-systems`.
- Theory-rich, methodologically broad IS for the AIS flagship → `journal-of-the-association-for-information-systems`.
- Computational/algorithmic or ML-for-OR contribution with no IS theory → `informs-journal-on-computing`; broad quantitative management → `management-science` (IS department).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] MIS Quarterly
[Topic tags] <2–3 closest topics + genre: behavioral/DSR/econ-of-IS>
[Method/evidence] <is there a genuine IS contribution at MISQ's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / genre statement / blinding / open-science / data-code>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
