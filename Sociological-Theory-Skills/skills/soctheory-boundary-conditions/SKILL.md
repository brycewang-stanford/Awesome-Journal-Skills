---
name: soctheory-boundary-conditions
description: Use when specifying the scope, domain, and limits of a Sociological Theory (ST) manuscript's theory — stating where it holds, where it does not, and what it does NOT claim. Bounds the theory as a contribution; it does NOT build the concepts (soctheory-theory-construction) or audit the reasoning (soctheory-argument-development).
---

# Boundary Conditions: Scope, Domain, What It Does NOT Claim (soctheory-boundary-conditions)

## When to trigger

- The theory is built and the argument is valid, but its limits are unstated
- A reviewer would say "this claims to explain everything, so it explains nothing"
- You cannot name a case the theory deliberately excludes
- A counter-case from `soctheory-argument-development` needs to be converted into a boundary

> Boundary conditions are a **contribution at ST, not a disclaimer.** A bounded theory is a
> sharper theory: stating the domain is itself a theoretical claim about how the social world
> is segmented. An unbounded theory reads as over-reach and invites rejection.

## The three dimensions of scope

Specify the domain along each axis explicitly:

1. **Substantive scope.** Which social phenomena does the theory govern (e.g., trust in
   markets, not trust in intimate relations)? Name the included and excluded substantive
   domains.
2. **Level scope.** At which level(s) of analysis does it operate (interactional, organizational,
   field, societal)? If it claims a micro-macro bridge, state where the bridge load-bears and
   where it does not.
3. **Contextual / historical scope.** Under what social conditions does the mechanism run —
   particular institutional settings, historical periods, cultural configurations? A mechanism
   that assumes modern bureaucratic states should say so.

## Turning limits into theory

| Move | Weak form (disclaimer) | Strong form (theorized boundary) |
|------|------------------------|----------------------------------|
| Scope | "This is limited to organizations" | "The mechanism requires formalized roles, so it operates in organizations but not in diffuse networks — because…" |
| Level | "We focus on the micro level" | "Aggregation to the macro fails when interaction is non-additive; the theory therefore bounds itself at the meso transition" |
| History | "Our examples are Western" | "The mechanism presupposes a differentiated cultural field, present after X but not before — so the theory is historically indexed" |

The strong form names *why* the boundary falls where it does — the same mechanism that powers
the theory also explains its limit.

## What the theory does NOT claim

State the non-claims explicitly. This pre-empts the most common reviewer move ("you're
implying…") and protects the contribution:

- It does not claim to explain phenomena outside the substantive domain.
- It does not claim the mechanism is the *only* one operating, only that it is operative and
  consequential.
- It does not claim empirical confirmation (ST does not test) — only theoretical adequacy.
- It does not claim to subsume the rival theories it engages, unless argued for in
  `soctheory-argument-development`.

## Scope conditions and the propositions

Each proposition should inherit the scope: if P3 only holds under condition C, say so where P3
is stated, not in a buried caveat. Tie the boundary back to the conceptual figure
(`soctheory-conceptual-exhibits`) so the diagram does not silently over-claim.

## Checklist

- [ ] Substantive, level, and contextual/historical scope are each stated
- [ ] Each boundary is theorized (the mechanism explains why the limit falls there), not just asserted
- [ ] Counter-cases from argument development are converted into named boundary conditions
- [ ] The explicit "does NOT claim" list is present
- [ ] Scope-bearing propositions carry their condition where stated
- [ ] The boundary is consistent with the theory's assumptions and figure

## Anti-patterns

- Boundary conditions written as apologies ("limited to…", "we cannot generalize…")
- A theory that claims to hold everywhere, so its content is empty
- A "limitations" paragraph copied from an empirical template (sample size, generalizability of data)
- Burying scope conditions far from the propositions they govern
- A conceptual figure that quietly extends past the stated domain
- Conceding so much scope that the contribution evaporates

## Output format

```
【Substantive scope】holds for [...] ; excludes [...]
【Level scope】operates at [...] ; bridge load-bears where [...]
【Contextual/historical scope】requires conditions [...]
【Why the boundary falls here】[mechanism-based reason, per axis]
【Does NOT claim】[explicit non-claims]
【Next step】soctheory-conceptual-exhibits
```
