# The Retrieval Hackathon — Instructor Flow

**Week 4, Lecture 7 · ~60 min in class · teams of 2–4.**

End-to-end runbook for the exercise. The in-class SAY/DO/WATCH cues are in
`ISBA2411_L7_Hackathon_RunSheet.pdf`; this is the operational flow around them.

**Learning goal:** keyword search matches *words*, semantic search matches
*meaning*; the best system fuses them, and which to trust depends on the query
and the cost budget.

---

## 1. Before class (T–1 day)

- [ ] **Pre-run the starter notebook** once, top to bottom — caches the dataset and
      embedding models, and confirms the baseline (main MRR ≈ 0.78, curveball ≈ 0.47).
- [ ] **Publish** the Canvas module item *"In-Class: The Retrieval Hackathon (open in Colab)"*.
- [ ] **Share the leaderboard sheet** → *Anyone with the link · Editor*. (The link is
      already in the notebook's last cell.)
- [ ] **Teams:** assign them, or leave method choice fully open (recommended — more
      hackathon energy). Optionally pre-assign starting approaches to guarantee coverage.
- [ ] Tell anyone using large embedding models to switch to a **GPU runtime**
      (Runtime → Change runtime type → GPU).
- [ ] Have the **run-sheet PDF** open for the in-class cues.

---

## 2. Run of show

| Time | Phase | What you do |
|---|---|---|
| 0:00–0:05 | **Kickoff** | Put the Colab + leaderboard links on screen. Everyone runs Section 0 + the TF-IDF baseline cell — that's the number to beat (main MRR ≈ 0.78). State the rule: same corpus/queries/metric, open on method. |
| 0:05–0:35 | **Build sprint** | Teams iterate and submit rows to the live leaderboard. Circulate; nudge the ladder TF-IDF → BM25 → dense → hybrid → re-rank. |
| 0:35–0:45 | **Curveball reveal** | Direct attention to the **Curveball MRR** column and announce it now counts. The board reorders. |
| 0:45–0:56 | **Demos** | ~2 min/team: one query their engine nails that the baseline misses + their quality-vs-cost trade-off. |
| 0:56–1:00 | **Awards + frontier** | Hand out awards, plot quality vs. build-time, connect forward. |

---

## 3. How the mechanics actually work

- **Submitting:** `submit()` prints a tab-separated line; students paste it into the
  sheet — it drops cleanly into the columns.
- **The curveball is not a re-run.** Every `submit()` already computes the Curveball
  MRR (on the 30 paraphrase queries) and prints it. The "reveal" is purely you
  *directing attention* to that column and reframing — no cell to trigger.
- **Reading the board:** sort by **Main MRR** for literal-query winners, by
  **Curveball MRR** for paraphrase winners. The *gap between the two columns* for a
  team tells you how semantic their method is (big gap up = keyword-only; small gap =
  meaning-aware).

---

## 4. The expected arc (so nothing surprises you)

1. **Early sprint:** keyword/BM25 teams lead the Main column. This is correct — don't
   spoil why. It's the "keyword is a strong baseline" surprise.
2. **Curveball reveal:** semantic teams surge (curveball MRR ≈ 0.66), keyword-only
   teams sink (≈ 0.47). The lesson lands physically on the board.
3. **Frontier close:** hybrid (BM25 + dense) usually tops both rounds — the point that
   the best system fuses methods, and the winner is whoever can say *why*.

---

## 5. Judging & awards

Rubric is in `RUBRIC.md`: 50% objective score (from the board), 50% pitch & insight
(the demo). Hand out several awards so more teams get a moment: **Best Recall ·
Fastest Index · Best Value (frontier) · Biggest Comeback (main→curveball) · Meaning
over Words · Best Pitch / People's Choice.**

A team that tops the board but can't explain the curveball gap scores below a team
with a modest number and a sharp read on the frontier.

---

## 6. Wrap-up / connect forward

- **The frontier:** plot Main MRR vs. index build-time. TF-IDF is the cheap corner;
  hybrid is the quality corner; dense-only often gets dominated on the main round.
- **To the project:** this retrieval step is the **R in the RAG** they'll build in
  Week 8, and a candidate representation for their Milestone.

---

## 7. Troubleshooting

| Problem | Fix |
|---|---|
| Model download / GPU stalls a team | Fall back to **TF-IDF + BM25** (CPU, no download) — still competes on the main round. |
| Dataset won't load | Loader reads from the repo; the three `.jsonl` files also work as a **local upload** (download from the repo, drop into Colab — local fallback is built in). |
| Leaderboard link opens "view only" | Sheet sharing is set to Viewer — change to **Editor**. |
| Board looks saturated | It shouldn't (Recall@1 ≈ 0.4–0.7). If everyone's near 1.0, they're scoring the wrong split — check they used `main`, not a tiny slice. |

---

## Reference numbers (validated on this dataset)

| Method | Main MRR@10 | Curveball MRR | Recall@5 | Build (s) |
|---|---|---|---|---|
| TF-IDF keyword (baseline) | 0.782 | 0.474 | 0.92 | ~0.1 |
| Dense MiniLM (all-MiniLM-L6-v2) | 0.737 | 0.664 | 0.85 | ~3–8 |
| Dense mpnet (all-mpnet-base-v2) | ~0.78–0.82 | ~0.70+ | ~0.88 | ~15–30 |
| Hybrid (BM25 + dense, RRF) | ~0.82+ | ~0.70+ | ~0.93 | ~5–10 |

*ISBA 2411 · Natural Language Processing & AI · Summer 2026*
