# main.py

from config import DEBUG
from preprocessing.processor import preprocess_text
from data.loader import load_documents
from indexing.inverted_index import build_inverted_index, save_index, load_index
from query_engine.search import search

test_cases = [
    None,
    "",
    "   ",
    "is the and",
    "Python is GREAT!!!",
    "Hello     World",
    "123 $$$ Python!!!",
    12345
]

for t in test_cases:
    print(f"Input: {t}")
    print(f"Output: {preprocess_text(t)}")
    print("-" * 40)
    
    
documents = []
inverted_index = {}

def initialize_system():
    global documents, inverted_index

    print("[SYSTEM] Initializing...")

    # Step 1: Load documents
    documents = load_documents()
    print(f"[SYSTEM] Loaded {len(documents)} documents")

    # Step 2: Load or build index
    inverted_index = load_index()

    if inverted_index is None:
        print("[SYSTEM] Building index...")
        inverted_index = build_inverted_index(documents)
        save_index(inverted_index)

    print("[SYSTEM] Ready 🚀")


def run_search_engine():
    print("Mini Search Engine Started 🚀")

    while True:
        query = input("\nEnter your search query (or type 'exit'): ")

        if query.lower() == "exit":
            print("Exiting search engine...")
            break

        results = search(query, inverted_index)

        if not results:
            print("No results found ❌")
        else:
            print(f"Found in documents: {results}")

if __name__ == "__main__":
    initialize_system()
    run_search_engine()