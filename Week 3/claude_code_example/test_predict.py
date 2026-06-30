from predict import predict

def test_clear_positive():
    assert predict("a brilliant, moving, beautifully acted film") == "positive"

def test_clear_negative():
    assert predict("a dull, lifeless waste of time") == "negative"

def test_negation_known_failure():
    # bag-of-words ignores word order; this is expected to mislabel.
    assert predict("this is not a good film") == "positive"  # documents the blind spot
