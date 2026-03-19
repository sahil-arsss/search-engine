import json
from collections import defaultdict

from preprocessing.processor import preprocess_text
from config import INDEX_FILE, DEBUG


def build_inverted_index(documents):
    """
    Build inverted index:
    word -> set(doc_ids)
    """
    index = defaultdict(set)

    for doc in documents:
        doc_id = doc["id"]
        content = doc["content"]

        tokens = preprocess_text(content)

        # Use set to avoid duplicate words in same doc
        unique_tokens = set(tokens)

        for token in unique_tokens:
            index[token].add(doc_id)

    if DEBUG:
        print(f"[DEBUG] Built index with {len(index)} terms")

    return index


def save_index(index):
    """
    Save index to disk as JSON
    """
    # Convert set -> list for JSON
    serializable_index = {
        word: list(doc_ids) for word, doc_ids in index.items()
    }

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(serializable_index, f, indent=2)  

    if DEBUG:
        print(f"[DEBUG] Index saved to {INDEX_FILE}")


def load_index():
    """
    Load index from disk
    """
    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            index = json.load(f)

        # Convert list back to set
        return {word: set(doc_ids) for word, doc_ids in index.items()}

    except FileNotFoundError:
        if DEBUG:
            print("[DEBUG] No index found. Need to build.")
        return None