"""
Train a TF-IDF + Logistic Regression sentiment classifier on the
`rotten_tomatoes` movie-review dataset and save it to disk.

Usage:
    python train.py                 # train, evaluate, save model.joblib
    python train.py --out mymodel.joblib

The saved artifact is a single scikit-learn Pipeline, so predict.py only
has to call `model.predict([sentence])` -- no separate vectorizer to manage.
"""

import argparse

import joblib
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline

# rotten_tomatoes labels: 0 = negative, 1 = positive
LABELS = ["negative", "positive"]


def build_pipeline() -> Pipeline:
    """TF-IDF features -> Logistic Regression. One object, easy to save."""
    return Pipeline(
        [
            (
                "tfidf",
                TfidfVectorizer(
                    lowercase=True,
                    # NOTE: we deliberately keep stop words. For sentiment, words
                    # like "not", "no", "never" flip the meaning of a review, so
                    # dropping them actually *hurts* accuracy (~3 points here).
                    stop_words=None,
                    ngram_range=(1, 2),   # unigrams + bigrams ("not good" stays together)
                    min_df=2,             # ignore words that appear in only 1 review
                    sublinear_tf=True,
                ),
            ),
            (
                "clf",
                LogisticRegression(max_iter=1000, C=3.0),
            ),
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out", default="model.joblib", help="where to save the trained model"
    )
    args = parser.parse_args()

    print("Loading the rotten_tomatoes dataset (8,530 train / 1,066 test reviews)...")
    ds = load_dataset("rotten_tomatoes")
    X_train, y_train = ds["train"]["text"], ds["train"]["label"]
    X_test, y_test = ds["test"]["text"], ds["test"]["label"]

    print("Training TF-IDF + Logistic Regression...")
    model = build_pipeline()
    model.fit(X_train, y_train)

    print("\nEvaluating on the held-out test set:")
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"  Accuracy: {acc:.1%}\n")
    print(classification_report(y_test, preds, target_names=LABELS))

    joblib.dump(model, args.out)
    print(f"Saved trained model -> {args.out}")


if __name__ == "__main__":
    main()
