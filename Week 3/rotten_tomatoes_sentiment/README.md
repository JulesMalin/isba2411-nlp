# 🍅 Movie-Review Sentiment Classifier

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JulesMalin/isba2411-nlp/blob/main/Week%203/rotten_tomatoes_sentiment/rotten_tomatoes_sentiment.ipynb)

A tiny, from-scratch **supervised text classifier** for ISBA 2411 (Week 3). It learns to tell
**positive** movie reviews from **negative** ones using classic NLP: **TF-IDF features + Logistic
Regression**. No GPU, no transformers — just a clean baseline that trains in seconds and reaches
**~79% accuracy** on the `rotten_tomatoes` test set.

> 👉 **Click the "Open in Colab" badge above** to run the whole thing in your browser — no install.

## What's in here

| File | What it does |
|------|--------------|
| `rotten_tomatoes_sentiment.ipynb` | The guided Colab notebook (start here for the demo). |
| `train.py` | Trains the model and saves it to `model.joblib`. |
| `predict.py` | Command-line tool: give it a sentence, it predicts the sentiment. |
| `requirements.txt` | The four packages you need. |

## Quickstart (local)

```bash
pip install -r requirements.txt

python train.py                       # trains + evaluates, writes model.joblib
python predict.py "A dazzling, heartfelt triumph."
python predict.py                     # interactive mode — type reviews live
```

Example output:

```
👍  POSITIVE (87% confident)  <- 'A dazzling, heartfelt triumph.'
👎  NEGATIVE (96% confident)  <- 'Boring, predictable, and painfully long.'
```

## How it works (30-second version)

1. **TF-IDF** turns each review into a vector of word/2-word-phrase weights — common words count
   for less, distinctive words count for more.
2. **Logistic Regression** learns a weight for each of those features; positive weights push
   toward "positive," negative weights toward "negative."
3. We keep the whole thing as one scikit-learn **`Pipeline`**, so `predict.py` just calls
   `model.predict([sentence])` — no separate vectorizer to juggle.

**One deliberate choice:** we *keep* stop words like "not," "no," and "never." For sentiment they
flip the meaning of a sentence, so removing them actually *lowers* accuracy (~3 points here).

## The known blind spot 🔍

Because TF-IDF is a "bag of words," it mostly ignores word order — so `"this is not good"` can
fool it. That's the perfect motivation for next week's move to **contextual / transformer models**.
