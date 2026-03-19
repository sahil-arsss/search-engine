import re
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))


def clean_text(text):
    # Edge Case 1: None input
    if text is None:
        return ""

    # Convert to string (Edge Case: non-string input)
    if not isinstance(text, str):
        text = str(text)

    # Lowercase
    text = text.lower()

    # Remove punctuation & special characters
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def tokenize(text):
    # Edge Case: empty string
    if not text:
        return []

    return text.split()


def remove_stopwords(tokens):
    # Edge Case: empty tokens
    if not tokens:
        return []

    filtered = [word for word in tokens if word not in STOPWORDS]

    # Edge Case: all stopwords → return empty list safely
    return filtered


def preprocess_text(text):
    text = clean_text(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)

    return tokens