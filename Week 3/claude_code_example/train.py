"""Train a TF-IDF + logistic regression sentiment classifier on rotten_tomatoes."""
import pickle
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def main():
    ds = load_dataset("rotten_tomatoes")
    vec = TfidfVectorizer(ngram_range=(1, 2))
    Xtr = vec.fit_transform(ds["train"]["text"])
    Xte = vec.transform(ds["test"]["text"])
    clf = LogisticRegression(max_iter=1000).fit(Xtr, ds["train"]["label"])
    test_acc = accuracy_score(ds["test"]["label"], clf.predict(Xte))
    print(f"held-out test accuracy: {test_acc:.4f}")
    with open("model.pkl", "wb") as f:
        pickle.dump({"vectorizer": vec, "classifier": clf}, f)
    print("saved model.pkl")

if __name__ == "__main__":
    main()
