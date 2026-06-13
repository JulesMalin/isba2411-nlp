# CLAUDE.md — ISBA 2411 Course Repo

Guidance for AI-assisted development of this repository. Read this before editing.

## What this repo is

The companion repo for **ISBA 2411 — Natural Language Processing** (Santa Clara University,
Leavey School of Business, Summer 2026, taught by Professor Malin). It is a *course companion*,
not a code library:

- It **links** to publishers' openly licensed notebooks (HOLLM, Tunstall) — it does **not**
  redistribute the textbooks.
- It maps each publisher notebook to the **10-week schedule** (see the table in `README.md`).
- It houses the **capstone milestone starter notebooks** that student teams copy into their own
  project repos and fill in.

The audience is students running everything on **Google Colab** (SCU Google Suite) or the
**SCU WAVE** cluster. Assume no local GPU and minimal local setup.

## Texts (for alignment, do not redistribute)

- **J&M** — Jurafsky & Martin, *Speech and Language Processing*, 3rd-ed. draft (Jan 6, 2026).
  **Reading only, no companion code.** Chapter numbers in `README.md` follow this draft.
- **HOLLM** — Alammar & Grootendorst, *Hands-On Large Language Models*. Apache-2.0 notebooks.
- **Tunstall** — Tunstall, von Werra & Wolf, *NLP with Transformers*. Apache-2.0 notebooks.

## Layout

```
README.md           Student-facing landing page: weekly notebook map + milestone table
CLAUDE.md           This file
requirements.txt    Pinned-by-name deps; install cell at top of each notebook on Colab
.gitignore          Ignores raw data (data/*.csv, data/*.json), models/, checkpoints, .env
data/               Shared corpora (e.g. FOMC transcripts) + where teams drop their dataset
  README.md         Data conventions (keep raw/large data OUT of version control)
milestones/         Five sequenced capstone starters (see below)
```

### Milestones (the capstone spine)

Five sequenced assignments, each applying that part of the course to the team's own project.
Topic is open but must fit a **baseline → measured improvement** frame.

| # | File | Week | Type |
|---|------|------|------|
| 1 | `milestones/Milestone1_Business_Brief.md` | 1 | Markdown brief (individual) |
| 2 | `milestones/Milestone2_Baseline_and_Representation.ipynb` | 3 | Starter notebook |
| 2 | `milestones/Milestone2_FOMC_representation_comparison.ipynb` | 3 | **Worked example** (FOMC) |
| 3 | `milestones/Milestone3_Model_Adaptation.ipynb` | 5 | Starter notebook |
| 4 | `milestones/Milestone4_System_Prototype.ipynb` | 7 | Starter notebook |
| 5 | `milestones/Milestone5_Final_Deliverable.md` | 9 | Deliverable checklist |

## Conventions when editing

- **Notebooks are starters.** Student-facing cells students must complete are marked with `TODO`.
  Preserve that pattern — scaffold structure and prompts, don't hand students a finished solution.
  The `_FOMC_representation_comparison` notebook is the exception: it's a fully worked example.
- **Colab-first.** Each notebook should run top-to-bottom on a clean Colab runtime. Put a `pip
  install` cell at the top rather than assuming a local environment. Don't rely on local file paths.
- **Don't redistribute textbook content.** Link to the publisher repos; never paste book text or
  copy their notebooks verbatim into this repo (beyond what their Apache-2.0 license permits, with
  attribution).
- **Keep the weekly map honest.** If you change a notebook link or week alignment in `README.md`,
  keep the "Notebook alignment" notes (below the table) consistent. A `—` means that book has no
  matching chapter for that week — that's intentional, not a gap to fill.
- **Data stays out of git.** Raw corpora are git-ignored. Commit a small sample + a download
  script, never large/raw files. See `data/README.md`.
- **J&M chapter numbers** track the Jan 6, 2026 draft (Embeddings = Ch. 5, Transformers = Ch. 8,
  LLMs = Ch. 7, IR & RAG = Ch. 11, alignment/RLHF = Ch. 9). J&M Ch. 1 is an unreleased
  placeholder — not assigned.

## Key dates (Summer 2026)

- Week 6: Team Update Jul 21 · Midterm Jul 23
- Milestone 5 deliverable due end of Week 9
- Final presentations: Aug 18 & 20

## Editing notebooks

Use the NotebookEdit tool for `.ipynb` files (not raw text edits). Validate that a notebook still
parses as JSON after edits. Don't commit executed output with large embedded data/images — clear
outputs before committing where practical.
