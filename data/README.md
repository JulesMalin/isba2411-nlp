# Data

## Shared corpus: FOMC transcripts

`fomc_corpus.txt` is the provided corpus for the **Milestone 2 worked example**
(`milestones/Milestone2_FOMC_representation_comparison.ipynb`). It contains the
verbatim FOMC **meeting transcripts for 2019** (8 meetings, ~3.3 MB, ~29k
sentences / ~658k word tokens) — enough to fit a trigram language model and
contrast its perplexity with GPT-2, while still running in seconds on Colab CPU.

Source: U.S. Federal Reserve (public domain). Full verbatim transcripts are
released on a ~5-year lag, so 2019 is a complete, fully released set.

### Rebuilding / changing the year

```bash
pip install pypdf
python data/fetch_fomc.py              # default: 2019 -> data/fomc_corpus.txt
python data/fetch_fomc.py --year 2018  # 2017 and 2018 are also configured
python data/fetch_fomc.py --keep-pdfs  # also save raw PDFs under data/raw/ (git-ignored)
```

## Your team's dataset

- Place raw files here. CSV/JSON and `data/raw/` are git-ignored by default
  (see `.gitignore`).
- Keep large/raw data out of version control; commit a small sample + a download
  script (like `fetch_fomc.py`) instead.
