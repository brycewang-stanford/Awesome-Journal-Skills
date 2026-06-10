---
name: geb-literature-positioning
description: Use when positioning a game-theory manuscript against the existing literature for Games and Economic Behavior (GEB) — staking what is new relative to known solution concepts, theorems, mechanisms, and prior experiments. Sharpens the contribution; it is not a standalone survey.
---

# Literature Positioning (geb-literature-positioning)

## When to trigger

- The relation to prior game-theory results is vague ("related to a large literature")
- You cannot name the two or three papers you most directly generalize or beat
- A reviewer might say "this is already known" or "this is just a special case of X"
- The paper reads as a survey with a result attached, instead of a result with placement

## The GEB positioning bar

GEB is a **specialist** journal, so its referees and Advisory Editors are game-theory experts who know the canonical results cold. Positioning here is sharper than at a general-economics journal: you are not explaining game theory to outsiders, you are convincing insiders that your theorem, mechanism, or experiment is **not implied by what they already know**. Because the chief editor routes your paper to an **anonymous Advisory Editor** (one of ~45) who selects referees, the people judging novelty are likely to include authors of the nearest prior work — position honestly and precisely.

GEB also spans **economics, political science, biology, computer science, mathematics, and psychology**, so the "nearest neighbor" to your result may live in a CS/EC or biology literature, not only in economics. Search across those fields; a result already known in algorithmic game theory or evolutionary biology is not novel just because it is new to economics.

## How to stake the contribution

- **Name the frontier.** Cite the specific prior theorem / mechanism / experiment your work advances, not a vague cluster.
- **State the delta in one sentence.** "Relative to [X], we drop assumption A / weaken B / cover a new class / get a tight bound where [X] gave a loose one."
- **Pre-empt the special-case objection.** Show explicitly what your result gives that the nearest result does not — ideally a corollary recovering theirs as a limit.
- **Distinguish a prior conference version.** If your own earlier conference paper (EC, WINE, SAGT, etc.) exists, say what is new here; GEB requires this disclosure and referees will know the conference work.
- **Credit across fields.** If the idea echoes a CS/biology/political-science result, cite it and explain the added game-theoretic value.

## Anti-patterns

- A literature "wall" of citations with no stated delta against any single paper
- Ignoring near-identical CS/EC or evolutionary-game results because they are outside economics
- Claiming novelty that a reader can refute with one well-known theorem
- Burying the contribution sentence on page 6
- Hiding overlap with your own prior conference paper


## Positioning pass for Games and Economic Behavior

Use this as a second-pass capability check. First lock the primitives, equilibrium concept, comparative statics, and proof or experiment boundary; then test whether the manuscript addresses game theorists who ask what the model teaches beyond a clever example.

- **Primary move:** Map incumbent conversation, unresolved tension, this manuscript's delta, and the sibling-venue omission a referee might notice.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JET for theory abstraction, Theoretical Economics for compact theory contribution, Experimental Economics for experiment-first designs; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Nearest prior work】[2-3 specific papers / theorems / mechanisms]
【Delta sentence】"relative to X, we ..."
【Special-case defense】recovers X as a limit / corollary? [Y/N]
【Cross-field check】CS-EC / biology / poli-sci neighbors cited? [Y/N]
【Conference-version overlap】disclosed + differentiated? [Y/N / NA]
【Next step】geb-contribution-framing
```
