# Movie Review Sentiment Classifier

TF-IDF + logistic regression baseline on the `rotten_tomatoes` dataset.

## Setup
    pip install -r requirements.txt

## Train
    python train.py        # trains, prints held-out test accuracy, writes model.pkl

## Predict
    python predict.py "a sharp, funny movie that earns its ending"

## Test
    python -m pytest -q
