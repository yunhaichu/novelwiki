# Type Contract Prompt

Use this prompt before project outline generation for any new novel instance, major reboot, or cross-genre project.

The goal is not to write prose. The goal is to define the reader-facing type contract: what kind of reading promise the project makes, what the reader should expect early, and what must not be falsely promised.

## Required Inputs

Read or ask for:

- project seed or premise
- intended genre or neutral direction
- target reader if known
- forbidden patterns
- style goals
- comparable works or rejected comparisons if available

If the user has not specified a genre, infer the most likely primary genre from the premise and mark it as an assumption.

## Output Object

Produce:

```text
Project title:
Primary genre:
Secondary genre if any:
Primary reader promise:
Main payoff type:
- truth / power / status / relationship / survival / wonder / justice / fear release / other

What reader expects by chapter 1:
What reader expects by chapter 3:
What reader expects by volume 1 end:

Opening must show:
Opening must not hide:
Information that can be delayed:
Forbidden false promises:

If genre-blended, which genre is primary:
How secondary genre supports primary genre:
How the ending should pay the primary promise:

Type drift risks:
1.
2.
3.

One-sentence reader contract:
```

## Rules

- Do not write prose.
- Do not list a genre only as decoration. Define what the reader expects from that genre.
- If the project mixes genres, identify the primary promise and the support role of each secondary promise.
- Do not let setting, profession, magic, technology, or era replace the reader-facing promise.
- The opening promise must be visible on the page, not only in planning notes.
- The type contract should be understandable by someone who has not read the wiki.

## Genre Promise Examples

Use the actual project, not these examples blindly.

```text
mystery: a fair problem, clue trail, contradiction, proof chain, truth payoff
thriller: immediate threat, rising pressure, narrowing options, survival or exposure payoff
horror: dread, contamination, taboo, fear experience, lingering consequence
cultivation/progression: weak position, growth path, resource/rule/power progress, stage payoff
urban/workplace: status, money, reputation, career leverage, social/legal pressure
romance: relationship movement, emotional risk, intimacy, commitment, repair
science fiction: anomaly proof, rule discovery, technical limit, human cost
fantasy: wonder, rule learning, world pressure, quest or power consequence
farming/management: resource chain, production, land, community, market access
officialdom/political: position, procedure, alliance, policy risk, public reputation
```

## Output

Output only the type contract.
