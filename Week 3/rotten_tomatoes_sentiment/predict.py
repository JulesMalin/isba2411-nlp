"""
Predict the sentiment of a sentence with the trained model.

Usage:
    python predict.py "This movie was an absolute masterpiece."
    python predict.py "Boring, predictable, and way too long."
    python predict.py                       # interactive: type sentences one per line

Requires model.joblib (run `python train.py` first).
"""

import argparse
import sys

import joblib

LABELS = ["negative", "positive"]
EMOJI = {"negative": "👎", "positive": "👍"}


def load_model(path: str):
    try:
        return joblib.load(path)
    except FileNotFoundError:
        sys.exit(
            f"Could not find '{path}'. Train the model first with:  python train.py"
        )


def predict(model, sentence: str) -> None:
    label_idx = int(model.predict([sentence])[0])
    label = LABELS[label_idx]
    # predict_proba gives a confidence we can show off in the demo
    confidence = model.predict_proba([sentence])[0][label_idx]
    print(f"{EMOJI[label]}  {label.upper():8s} ({confidence:.0%} confident)  <- {sentence!r}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sentence", nargs="*", help="sentence to classify")
    parser.add_argument("--model", default="model.joblib", help="path to saved model")
    args = parser.parse_args()

    model = load_model(args.model)

    if args.sentence:
        predict(model, " ".join(args.sentence))
        return

    # No sentence given -> interactive mode (great for a live demo)
    print("Type a movie review and press Enter (Ctrl-C or empty line to quit).\n")
    try:
        while True:
            sentence = input("> ").strip()
            if not sentence:
                break
            predict(model, sentence)
    except (KeyboardInterrupt, EOFError):
        pass
    print("\nThanks for watching! 🎬")


if __name__ == "__main__":
    main()
