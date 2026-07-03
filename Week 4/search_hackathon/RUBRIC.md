# The Retrieval Hackathon — Judging Rubric

Same corpus, queries, and metric for every team, so scores compare directly.

## Score (50%) — objective, from the leaderboard
- **Main MRR@10** — ranking quality on literal queries.
- **Curveball MRR** — ranking quality on paraphrased queries (the meaning-vs-words test).
- **Index build time** — the cost axis. A small model that nearly matches a big one wins on value.

## Pitch & insight (50%) — from the 2-minute demo
- **Live win** — show one query your retriever nails that the keyword baseline misses.
- **Trade-off reasoning** — where does your method sit on quality vs. cost, and would you ship it?
- **Understanding** — can you explain *why* your method wins where it wins?

A team that tops the board but can't explain the curveball gap scores lower than a
team with a modest score and a sharp read on the frontier.

## Awards (hand out several — more teams get a moment)
- **Best Recall** — highest Main MRR@10
- **Fastest Index** — lowest build time with a competitive score
- **Best Value** — best score-per-second (the frontier point)
- **Biggest Comeback** — largest jump from main to curveball round
- **Meaning over Words** — most impressive paraphrase catch in the demo
- **Best Pitch / People's Choice** — class vote
