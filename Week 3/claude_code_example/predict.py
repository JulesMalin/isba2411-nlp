"""CLI: classify a review string as positive or negative."""
import sys
import pickle

LABELS = {0: "negative", 1: "positive"}

def predict(text):
    with open("model.pkl", "rb") as f:
        m = pickle.load(f)
    return LABELS[int(m["classifier"].predict(m["vectorizer"].transform([text]))[0])]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('usage: python predict.py "your review text"')
        sys.exit(1)
    review = " ".join(sys.argv[1:])
    print(predict(review))
